import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# chrome_options = Options()
# chrome_options.add_argument("--headless")

#driver =webdriver.Chrome(chrome_options=chrome_options,executable_path='D:/workspace/section3/webdriver/chrome/chromedriver')
driver =webdriver.Chrome('D:/workspace/section3/webdriver/chrome/chromedriver')
driver.set_window_size(1920, 1280)
driver.implicitly_wait(3)

driver.get('https://www.inflearn.com')
time.sleep(5)
driver.implicitly_wait(3)

print('스크린샷 완료')
