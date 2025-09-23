import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # enter키 등을 입력하기 위해서 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

url = 'https://auto.danawa.com/newcar/?Work=record'

# 웹 드라이버를 자동으로 설치하고 최신버전을 유지
Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)

# 사이트 접속방법
driver.get(url)
driver.maximize_window() # 전체화면으로 실행
print('사이트 접속했습니다.')
# 사이트가 로드 될때까지 기다림.
WebDriverWait(driver,30).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR,"input[name = rdoMonthPeriod][value='period']"))
)
year_select = driver.find_element(By.ID, 'selMonthFrom')
# 객체로 만든다
select_year = Select(year_select)
select_year.select_by_value('2024')

for month in range(1,13):
    month_value = f"{month:02d}"
    month_select_element = driver.find_element(By.ID, 'selDayFrom')
    select_month = Select(month_select_element)

    # select_month.select_by_value(f'{month:02}')
    time.sleep(60)

time.sleep(60)
driver.quit()



