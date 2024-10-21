# -----------------------------------------------------------------------------
# Flask Framework에서 Webserver 구동 파일
# - 파일명 : __init__.py
# -----------------------------------------------------------------------------
# 모듈 로딩 -------------------------------------------------------------------
from flask import Flask, render_template

# Flask Web Server 인스턴스 생성
APP = Flask(__name__)

# 라우팅 기능 함수
# Flask Web Server 인스턴스 변수명.route("URL")
# http://127.0.0.1:5000/
@APP.route("/")
def index():
    return render_template("project.html")

# 조건부 실행
if __name__ == '__main__':
    APP.run()


# http://127.0.0.1:5000/menu
# http://127.0.0.1:5000/menu/
@APP.route("/menu")
@APP.route("/menu/")
def menu():
    return render_template("menu.html")