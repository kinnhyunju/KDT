# 모듈 로딩
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchinfo import summary

import pandas as pd

from classes import *
from func import detecting



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

cancerModel = torch.load(SAVE_MODEL, weights_only=False)

result = detecting('39.0,Female,2014-12-10,Stage I,2014-12-28,No,Former Smoker,17.1,189,1,0,1,0,Radiation,2016-03-10')
print(result)