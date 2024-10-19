# ------------------------------------------------------------------
# 모듈 로딩
# ------------------------------------------------------------------
from fileinput import filename
import os.path          # 파일 및 폴더 관련
import cgi, cgitb       # cgi 프로그래밍 관련
import sys, codecs      # 인코딩 관련
from pydoc import html  # html 코드 관련 : html을 객체로 처리

import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
from torchvision.transforms import v2

# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True      # Jupyter Mode : False, WEB Mode : True
cgitb.enable()          # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

# 모델 호출
SAVE_PATH = r"C:\Users\kdp\KDT_06\KDT\EX_PY06\KDT\KDT-1\Project12\cgi-bin\models\cnnmodel.pth"
fruitModel = torch.load(SAVE_PATH, weights_only=False)

MODEL_PATH = '/cnnmodel.pth'

# 데이터 변형 및 전처리
transConvert = transforms.Compose(
    [
        transforms.Resize([256]), 
        transforms.CenterCrop([224]),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ]
)


# ------------------------------------------------------------------
# 사용자 정의 함수
# ------------------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드

def showHTML(msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    
        <!DOCTYPE html>
        <html lang="en">
          
         <head>
          <meta charset="UTF-8">
          <title>♥ 과 일 분 류 ♥</title>
         </head>
          
         <body bgcolor="azure">   
                <br>         
                <form enctype="multipart/form-data" action="" method="post">
                    <div>
                        <input type="file" id = "imageInput" name="file" accept ="image/*">
                    </div>
                    <p><input type="submit">{msg}</p>
                </form>
        </body>
        </html>""")


# 과일 분류 함수---------------------------------------------------------------------------
# 함수명 : fruitPredict
# 재 료 : 사용자 입력 데이터
# 결 과 : 판별 결과 과일 (사과, 바나나, 오렌지, 딸기)

def fruitPredict(Model, filepath):
    try:
        target = ['사과', '바나나', '오렌지', '딸기']
        base_path= r"C:\Users\kdp\Desktop\DATA\Project10\images\\"+filepath

        image = Image.open(base_path)
        image = image.convert('RGB')
        image = transConvert(image)
        image = image.unsqueeze(0)
        
        result = '모델'
        # 모델 테스트
        Model.eval()

        result = Model(image)       
        idx = result.argmax().item()
        result = target[idx]

        return f" 예측 결과 : 이 과일은 {result}입니다! ⊼⌔⊼ ꩀ"

    except Exception as e:
        return f' Error during prediction : {base_path}\n{e}'

# ------------------------------------------------------------------
# 기능 구현
# ------------------------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩
if SCRIPT_MODE:
    pklfile = os.path.dirname(__file__)+ MODEL_PATH # 웹상에서는 절대경로만
else:
    pklfile = MODEL_PATH

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()

# (3-2) Form안에 textarea 태크 속 데이터 가져오기
# file 받아오기...?
img = form.getvalue("file", None)

if img :
    filename = form['file'].filename

# (3-3) 판별하기
if img and form['file'].filename:
    result = fruitPredict(fruitModel, f'{filename}')
    msg = result
else:
    msg=f' │˶˙ᯅ˙˶)꜆ 사진을 선택해주세요!'

# (4) 사용자에게 WEB 화면 제공
showHTML(msg)