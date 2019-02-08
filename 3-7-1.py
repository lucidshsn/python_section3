import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class NcafeWriteAtt:
    #초기화 실행
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") #CLI user-agent
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='D:/workspace/section3/webdriver/chrome/chromedriver')
        self.driver.implicitly_wait(5)

        #cafe 로그인 출석체크
    def writeAttendCheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login?mode=number')
        self.driver.find_element_by_id('disposable_num').send_keys('42245284')
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span/input').click()
        self.driver.implicitly_wait(3)
        self.driver.get('https://cafe.naver.com/esyori?iframe_url=/AttendanceView.nhn%3Fsearch.clubid=10080092%26search.menuid=62')
        self.driver.implicitly_wait(30)

        self.driver.switch_to_frame('cafe_main')
        self.driver.find_element_by_id('cmtinput').send_keys('출석합니다.')
        self.driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/a/img').click()
        time.sleep(3)

        #소멸자
    def __del__(self):
        #self.driver.close()  # 현재의 실행 포커스된 영역을 종료
        self.driver.quit()   # Selenium 전체 프로그램 종료
        print("removed driver object")


#실행
if __name__ == '__main__':
    # 객체 생성
    a = NcafeWriteAtt()
    # 시작
    start_time = time.time()
    # 프로그램 실행
    a.writeAttendCheck()
    # 종료시간 출력
    print("--Total %s Second ---" % (time.time() - start_time))
    # 객체 소멸
    del a
