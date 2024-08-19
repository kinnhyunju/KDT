# 네이버 블로그 '데이터 분석가 자격증'
# 네이버 카페 데이터 포럼  - 
import urllib.request
import datetime
import json
import pandas as pd

def get_request_url(url):
    client_id = "oaCRubSPGzexRX5V0O7C"
    client_secret = "6ZP0MAYlw4"

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    
    except Exception as e :
        print(e)
        print(f'Error for URL: {url}')

def get_naver_search(node, search_text, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = f"/{node}.json"
    query_string = f"{urllib.parse.quote(search_text)}"

    parameters = ("?query={}&start={}&display={}".format(query_string,start,display))

    url = base + node + parameters
    response = get_request_url(url)

    if response is None:
        return None
    else:
        return json.loads(response) # json 문자열을 Python 객체로 변환
    
def get_post_data(post, json_result_list, cnt):
    title = post['title']
    description = post['description']
    link = post['link']

    # [번호, 제목, 개요, 네이버링크]
    json_result_list.append([cnt, title, description, link])

def main():
    node = 'blog'
    search_text = '데이터 분석가'
    cnt = 0
    json_result_list = []

    json_response = get_naver_search(node, search_text, 1, 100)
    while cnt <500:
        if (json_response is None) and (json_response['display'] == 0):
            break
        for post in json_response['items']:
            cnt += 1
            get_post_data(post, json_result_list, cnt)
            

        start = json_response['start'] + json_response['display']
        json_response = get_naver_search(node, search_text, start, 100)
    
    print(f'전체 검색 수 : {cnt}')

    # csv 파일로 저장
    columns = ['count', 'title', 'description', 'link']
    result_df = pd.DataFrame(json_result_list, columns=columns)
    result_df.to_csv(f'{search_text}_naver_{node}.csv', index=False, encoding='utf-8')

if __name__ == '__main__':
    main()

