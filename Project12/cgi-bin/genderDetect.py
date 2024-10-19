# ------------------------------------------------------------------
# 모듈 로딩
# ------------------------------------------------------------------
import os.path          # 파일 및 폴더 관련
import cgi, cgitb       # cgi 프로그래밍 관련
import sys, codecs      # 인코딩 관련
from pydoc import html  # html 코드 관련 : html을 객체로 처리

# 모듈 로딩
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_curve, roc_auc_score

from joblib import dump, load
import pandas as pd
from joblib import load

# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True      # Jupyter Mode : False, WEB Mode : True
cgitb.enable()          # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

# ------------------------------------------------------------------
# 사용자 정의 함수
# ------------------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드

def showHTML(text,msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    
        <!DOCTYPE html>
        <html lang="en">
         <head>
          <meta charset="UTF-8">
          <title> 성별 진단 </title>
         </head>
         <body bgcolor="azure">
          <form>
            <textarea name="text" rows="10" cols="100" >{text}</textarea>
            <p><input type="submit" value="결과 확인">{msg}</p>
          </form>
         </body>
        </html>""")


def preprocessing(text):
    column = ['forehead_width_cm', 'forehead_height_cm', 'nose_wide','nose_long', 'lips_thin', 'distance_nose_to_lip_long']
    data = text.split(',')
    df = pd.DataFrame([data],columns=column)
    df['forehead_width_cm'] = df['forehead_width_cm'].astype('float32')
    df['forehead_height_cm'] = df['forehead_height_cm'].astype('float32')
    df['nose_wide'] = df['nose_wide'].astype('int')
    df['nose_long'] = df['nose_long'].astype('int')
    df['lips_thin'] = df['lips_thin'].astype('int')
    df['distance_nose_to_lip_long'] = df['distance_nose_to_lip_long'].astype('int')

    return df

# ------------------------------------------------------------------
# 기능 구현
# ------------------------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩
SAVE_PATH = r"C:\Users\kdp\KDT_06\KDT\EX_PY06\KDT\DeepLearning\models\project" # 웹상에서는 절대경로만
SAVE_MODEL = r"C:\Users\kdp\KDT_06\KDT\EX_PY06\KDT\KDT-1\Project12\cgi-bin\models\model.joblib"

if os.path.exists(SAVE_MODEL):
   model = load(SAVE_MODEL)
   print("경로상 파일이 존재합니다.")
else:
   print(f'{SAVE_MODEL} 파일이 존재하지 않습니다. 다시 확인하세요.')

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()

# (3-2) Form안에 textarea 태크 속 데이터 가져오기
text = form.getvalue("text", default="")

# (3-3) 판별하기
msg =""
if text != "":
    df = preprocessing(text)
    result1 = model.predict(df)
    target = ['남성', '여성']
    result = f'예측 결과 : 당신의 성별은 {target[result1[0]]}입니다.'
    msg = f" {result}"
else:
    msg=f' 데이터를 입력하세요.'

# (4) 사용자에게 WEB 화면 제공
showHTML(text,msg)