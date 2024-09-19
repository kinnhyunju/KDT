# 모듈 로딩
# 모델 관련 모듈
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torch.optim as optim
from torchmetrics.classification import F1Score, BinaryF1Score, BinaryConfusionMatrix, MulticlassF1Score, BinaryAccuracy
from torchmetrics.regression import R2Score, MeanSquaredError
from torchinfo import summary

# 데이터 및 시각화 관련 모듈
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def check_version():
    print(f'Pytorch v.{torch.__version__}')
    print(f'Pandas v.{pd.__version__}')

# ---------------------------------------------------------
# 아이리스 회귀 모델
# ---------------------------------------------------------
class IrisRegModel(nn.Module):
    # 모델 구조 구성 및 인스턴스 생성 메서드
    def __init__(self):
        super().__init__()
        self.in_layer = nn.Linear(3,10)
        self.hidden_layer = nn.Linear(10,30)
        self.out_layer = nn.Linear(30,1)

    #순방향 학습 진행 메서드
    def forward(self,x) : 
        # 입력층
        y = self.in_layer(x)    # 
        y=F.relu(y)             # relu 값의 범위 : 0<=y / 시그모이드 : 0~1
        # 은닉층 : 10개 숫자의 값(>=0)
        y = self.hidden_layer(y)
        y = F.relu(y)
        # 출력층 : 30개 숫자값 / 회귀이므로 바로 반환
        return self.out_layer(y)

# ---------------------------------------------------------
# 아이리스 이진분류 모델
# ---------------------------------------------------------
class IrisBCFModel(nn.Module):
    # 모델 구조 구성 및 인스턴스 생성 메서드
    def __init__(self):
        super().__init__()
        self.in_layer = nn.Linear(4,10)
        self.hidden_layer = nn.Linear(10,5)
        self.out_layer = nn.Linear(5,1)

    #순방향 학습 진행 메서드
    def forward(self,x) : 
        # 입력층
        y = self.in_layer(x)    # 
        y=F.relu(y)             # relu 값의 범위 : 0<=y / 시그모이드 : 0~1
        # 은닉층 : 10개 숫자의 값(>=0)
        y = self.hidden_layer(y)
        y = F.relu(y)
        # 출력층 : 5개 숫자값 / 분류이므로 시그모이드 함수 적용해서 반환
        return F.sigmoid(self.out_layer(y))

# ---------------------------------------------------------
# 아이리스 이진분류 모델
# ---------------------------------------------------------
class IrisMCFModel(nn.Module):
    # 모델 구조 구성 및 인스턴스 생성 메서드
    def __init__(self):
        super().__init__()
        self.in_layer = nn.Linear(4,10)
        self.hidden_layer = nn.Linear(10,5)
        self.out_layer = nn.Linear(5,3)

    #순방향 학습 진행 메서드
    def forward(self,x) : 
        # 입력층
        y = self.in_layer(x)    # 
        y=F.relu(y)             # relu 값의 범위 : 0<=y / 시그모이드 : 0~1
        # 은닉층 : 10개 숫자의 값(>=0)
        y = self.hidden_layer(y)
        y = F.relu(y)
        # 출력층 : 5개 숫자값 / 다중 분류이므로 소프트맥스 함수 적용 => 손실함수 CrossEntropy는 소프트맥스 자동으로 진행 => 그대로 반환하기
        return self.out_layer(y)    

# ---------------------------------------------------------
# 아이리스 데이터셋 설계
# ---------------------------------------------------------
class IrisDataset(Dataset):

    def __init__(self, featureDF, targetDF):
        self.featureDF = featureDF
        self.targetDF = targetDF
        self.n_rows = featureDF.shape[0]
        self.n_features = featureDF.shape[1]

    def __len__(self) : 
        return self.n_rows

    def __getitem__(self, index):
        # 텐서화
        feaureTS = torch.FloatTensor(self.featureDF.iloc[index].values)
        targetTS = torch.FloatTensor(self.targetDF.iloc[index].values)
        
        # 피처와 타겟 반환
        return feaureTS, targetTS    

