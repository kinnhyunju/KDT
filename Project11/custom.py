### 모듈 로딩
import torch
from torch import nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset
from torch import optim
from konlpy.tag import *

from collections import Counter

import os
import re

import pandas as pd
import json
import numpy as np


# ----------------------------------------------------------------------------
# 문장 분류
# ----------------------------------------------------------------------------
class SentenceClassifier(nn.Module):
    def __init__(self, n_vocab, hidden_dim, embedding_dim, n_layers, dropout=0.5, bidirectional=True, model_type = "lstm"):
        super().__init__()
        self.embedding = nn.Embedding(num_embeddings=n_vocab, embedding_dim=embedding_dim, padding_idx=0)

        if model_type == 'rnn':
            self.model = nn.RNN(input_size=embedding_dim, hidden_size=hidden_dim, num_layers=n_layers, bidirectional=bidirectional, dropout=dropout, batch_first=True)
        elif model_type == 'lstm':
            self.model = nn.LSTM(input_size=embedding_dim, hidden_size=hidden_dim, num_layers=n_layers, bidirectional=bidirectional, dropout=dropout, batch_first=True)
        
        if bidirectional:
            self.classifier = nn.Linear(hidden_dim*2, 1)
        else :
            self.classifier = nn.Linear(hidden_dim, 1)
        
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, inputs):
        embeddings = self.embedding(inputs)
        output,_ = self.model(embeddings)
        last_output = output[:,-1,:]
        last_output = self.dropout(last_output)
        logits = self.classifier(last_output)
        return logits

# ----------------------------------------------------------------------------
# 단어사전 만들기
# ----------------------------------------------------------------------------
def build_vocab(corpus, n_vocab, special_tokens):
    counter = Counter()
    for tokens in corpus:
        counter.update(tokens)
    vocab = special_tokens

    for token, count in counter.most_common(n_vocab):
        vocab.append(token)
        
    return vocab

# ----------------------------------------------------------------------------
# 정수 인코딩 및 패딩
# ----------------------------------------------------------------------------
def pad_sequences(sequences, max_length, pad_value):
    result = list()
    for sequence in sequences:
        sequence = sequence[:max_length]
        pad_length = max_length - len(sequence)
        padded_sequence = sequence + [pad_value] * pad_length
        result.append(padded_sequence)
    return np.asarray(result)


# ----------------------------------------------------------------------------
# 모델 학습 및 테스트
# ----------------------------------------------------------------------------
def train_model(model, datasets, criterion, optimizer, device, interval):
    model.train()
    losses = list()

    for step, (input_ids, labels) in enumerate(datasets):
        input_ids = input_ids.to(device)
        labels = labels.to(device).unsqueeze(1)

        logits = model(input_ids)
        loss = criterion(logits, labels)
        losses.append(loss.item())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if step% interval == 0:
            print(f'Train Loss {step} : {np.mean(losses)}')

def test_model(model, datasets, criterion, device):
    model.eval()
    losses = list()
    corrects = list()

    for step, (input_ids, labels) in enumerate(datasets):
        input_ids = input_ids.to(device)
        labels = labels.to(device).unsqueeze(1)

        logits = model(input_ids)
        loss = criterion(logits, labels)
        losses.append(loss.item())
        yhat = torch.sigmoid(logits)>.5
        corrects.extend(torch.eq(yhat, labels).cpu().tolist())

    print(f"Val Loss : {np.mean(losses)}, Val Accuracy : {np.mean(corrects)}")
    return np.mean(losses), np.mean(corrects)