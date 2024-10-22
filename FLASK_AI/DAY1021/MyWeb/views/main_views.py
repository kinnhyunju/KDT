# -----------------------------------------------------------------------------
# Flask Framework에서 '/' URL에 대한 라우팅 처리 파일
# - 파일명 : main_views.py
# -----------------------------------------------------------------------------
# 모듈 로딩 -------------------------------------------------------------------
from flask import Blueprint, render_template

# Blueprint 인스턴스 생성 -----------------------------------------------------
# http://127.0.0.1:5000/
main_bp = Blueprint('main', import_name=__name__, url_prefix='/', 
                    template_folder='templates')

# 라우팅 기능 함수 정의
# 플라스크에서 endpoint는 함수의 별칭을 의미함 (원래는 클라이언트의 url 경로를 의미)
# 함수명을 변경할 때 덜 복잡하게 하고, 외부에 함수명을 노출하지 않기 위해 endpoint 사용

@main_bp.route('/', endpoint='hello')
def index():
    return render_template('index.html')