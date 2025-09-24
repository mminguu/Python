from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# 웹 드라이버 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 사이트 접속
url = 'https://www.hyundai.com/kr/ko/faq.html'
driver.get(url)
# driver.maximize_window()
print('사이트 접속했습니다.')
time.sleep(3)


try:
    # FAQ 카테고리 클릭 (차량정비)
    print("차량정비 카테고리 찾는 중...")
    category = driver.find_element(By.XPATH,'//*[@id="contents"]/div[2]/div/div[2]/div/div[1]/div[1]/dl[3]/dt/button')
    category.click()
    print("차량정비 카테고리 클릭 완료")
    time.sleep(3)

    # 페이지의 FAQ 내용 가져오기
    print("FAQ 내용 가져오는 중...")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # FAQ 질문들 찾기
    faq_questions = soup.select('button', class_='ui_accordion acc_01')
    
    # 각 질문에 대해 처리
    for question in faq_questions:
        print("-" * 50)
        print("질문:", question.get_text().strip())
        
        # 해당 질문의 답변 찾기
        parent_dl = question.find_parent('dl')
        if parent_dl:
            answer_dd = parent_dl.find('dd')
            if answer_dd:
                print("답변:", answer_dd.get_text().strip())

except Exception as e:
    print("오류 발생:", str(e))

finally:
    print("\n브라우저를 종료합니다.")
    driver.quit()