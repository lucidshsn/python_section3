import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver =webdriver.PhantomJS('D:/workspace/section3/webdriver/phantomjs/phantomjs')

driver.implicitly_wait(5)

driver.get('https://google.com')
driver.save_screenshot("d:/workspace/section3/website.png")

driver.implicitly_wait(5)

driver.get('https://daum.net')
driver.save_screenshot("d:/workspace/section3/website2.png")

driver.quit()

print('스크린샷 완료')
