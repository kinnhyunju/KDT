# 모듈 로딩
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchinfo import summary

import pandas as pd

# class CancerModel2(nn.Module):
#     def __init__(self,in_out=5,perceptrons = []) :
#         super().__init__()
#         self.i_layer = nn.Linear(14,perceptrons[0] if len(perceptrons)>0 else in_out)
        
#         self.h_layers = nn.ModuleList()
#         for idx in range(len(perceptrons)-1) :
#             self.h_layers.append(nn.Linear(perceptrons[idx], perceptrons[idx+1]))

#         self.o_layer = nn.Linear(perceptrons[-1] if len(perceptrons)>0 else in_out,1)

#     def forward(self, x):
#         # 입력층
#         y = F.relu(self.i_layer(x))

#         # 은닉층
#         for layer in self.h_layers:
#             y = F.relu(layer(y))
        
#         # 출력층
#         return F.sigmoid(self.o_layer(y))
# Dropout 실시

class CancerModel(nn.Module):
    def __init__(self,in_out=5,perceptrons = []) :
        super(CancerModel, self).__init__()
        self.i_layer = nn.Linear(14,perceptrons[0] if len(perceptrons)>0 else in_out)
        
        self.h_layers = nn.ModuleList()
        for idx in range(len(perceptrons)-1) :
            self.h_layers.append(nn.Linear(perceptrons[idx], perceptrons[idx+1]))
        self.dropout_prob = 0.5

        self.o_layer = nn.Linear(perceptrons[-1] if len(perceptrons)>0 else in_out,1)

    def forward(self, x):
        # 입력층
        y = F.relu(self.i_layer(x))

        # 은닉층
        for layer in self.h_layers:
            y = F.relu(layer(y))
            y = F.dropout(y, p=self.dropout_prob)
        # 출력층
        return F.sigmoid(self.o_layer(y))
## 모델 파일 관련
### models 폴더 아래 프로젝트 폴더 아래 모델 파일 저장
import os

# 저장 경로
SAVE_PATH = '../DeepLearning/models/project/'
# 저장 파일명
SAVE_FILE = SAVE_PATH+'model_train_wb.pth'

# 모델 구조 및 파라미터 모두 저장 파일명
SAVE_MODEL = SAVE_PATH+'model_all.pth'
# 경로상 폴더 존재 여부 체크
if not os.path.exists(SAVE_PATH) : os.makedirs(SAVE_PATH)   # 폴더 / 폴더 / ...  하위폴더까지 생성