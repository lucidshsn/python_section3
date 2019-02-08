import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#설치가 안되어 있어서 그랬음. 
firefox_options = Options()
firefox_options.add_argument("--headless")

driver = webdriver.Firefox(firefox_options=firefox_options,executable_path='d:/workspace/section3/webdriver/firefox/geckodriver')
#driver.set_window_size(1920, 1280)

# driver.implicitly_wait(5)

driver.get('https://google.com')
#time.sleep(5)
driver.save_screenshot("d:/workspace/section3/website_ff.png")

# driver.implicitly_wait(5)

driver.get('https://daum.net')
# time.sleep(5)
driver.save_screenshot("d:/workspace/section3/website_ff2.png")

driver.quit()

print('스크린샷 완료')
