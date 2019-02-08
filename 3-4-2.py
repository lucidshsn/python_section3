import sys
import io
from bs4 import BeautifulSoup
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#로그인 유저 정보
LOGIN_INFO = {
    'user_id': 'wrtipo',
    'user_pw':'w1w2w3w4w5'
}

#Session 생성, with 구문안 유지
with requests.Session() as s:
    login_req = s.post('https://user.ruliweb.com/member/login_proc', data=LOGIN_INFO)
    #html 소스 확인
    #print('login_req', login_req.text)
    #Header 확인
    #print('header', login_req.headers)
    if login_req.status_code ==200 and login_req.ok:
        post_one = s.get('https://bbs.ruliweb.com/market/board/320103/read/123429?')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.prettify())
        article = soup.select_one("div.view_content").find_all('p')
        #print(article)
        for i in article:
            if i.string is not None:
                print(i.string)
