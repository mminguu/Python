import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # enter키 등을 입력하기 위해서 

url = 'https://kosis.kr/statisticsList/statisticsListIndex.do?vwcd=MT_ZTITLE&menuId=M_01_01'

# 웹 드라이버를 자동으로 설치하고 최신버전을 유지
Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)

# 사이트 접속방법
driver.get(url)
driver.maximize_window() # 전체화면으로 실행
print()