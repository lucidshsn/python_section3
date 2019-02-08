import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#요청
URL = 'https://www.wishket.com/accounts/login/'
#fake_useragent 생성
ua=UserAgent()
#print(ua.chrome)

with requests.Session() as s:

    s.get(URL)
    #login 정보 payload
    LOGIN_INFO ={
        'identification': 'wrtipo@knou.ac.kr',
        'password': 'w1w2w3w4w5',
        'csrfmiddlewaretoken' : s.cookies['csrftoken']
    }
    #print('header', s.headers)
    #print('token', s.cookies['csrftoken'])
    #요청
    response = s.post(URL, data=LOGIN_INFO, headers={'User-Agent' :str(ua.chrome), 'Referer':'https://www.wishket.com/accounts/login/'})

    #print('response', response.text)

    if response.status_code ==200 and response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        projectList = soup.select("table.table-responsive > tbody > tr")
        #print(projectList)
        for i in projectList:
            print(i.find('th').string, i.find('td').text)
