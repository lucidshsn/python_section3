import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class NcafeMemberExr:
    #초기화 실행
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") #CLI user-agent
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='D:/workspace/section3/webdriver/chrome/chromedriver')
        self.driver.implicitly_wait(5)

        #cafe 회원정보 추출
    def getMemberList(self):
        self.driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        self.driver.find_element_by_name('id').send_keys('wrtipo')

        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(10)
        self.driver.get('https://cafe.naver.com/sun4369?iframe_url=/AttendanceView.nhn%3Fsearch.clubid=11868252%26search.menuid=6')
        self.driver.implicitly_wait(10)
        self.driver.switch_to_frame('cafe_main')
        print('switch_to_frame 이게 안됨,, ㅠㅠㅠㅠ?')
        # self.driver.find_element_by_id('cmtinput').send_keys('출석합니다.')
        # self.driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/a/img').click()
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
