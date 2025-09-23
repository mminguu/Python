import time
url = 'https://www.coffeebeankorea.com/store/store.asp'
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # enter, space 같은 키를 누르게 할 때 필요해서 

# 웹 드라이버를 자동으로 설치하고 최신버전을 유지
Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)



driver.get('https://www.naver.com/')
time.sleep(5)
print('브라우저가 성공적으로 열렸습니다.')

# 검색창 요소 찾기 ( id 가 ipt_keyword_recruit 인 input 태그를 찾음 )
search_input = driver.find_element(By.ID,'query')
# 검색창에 파이썬을 입력
search_input.send_keys('파이썬') # send_keys->글자를 입력하게 하는 코드
search_input.send_keys(Keys.ENTER) # enter키를 눌러 검색을 실행하게 함
time.sleep(5)
driver.quit()