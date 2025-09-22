import requests
# 데이터를 요청 할 주소
url = 'https://www.hollys.co.kr/store/korea/korStore2.do?'
# 서버에 보낼 데이터 ( 1페이지를 보여달라는 의미로 )
from_data = {
    'pageNo' : 1,
    'sido' : '',
    'gugun' : '',
    'store' : ''
}
response = requests.post(url,data=from_data)
# 터미널에서 pip install beautifulsoup4 실행 (pip install beautifulsoup4 이 명령어는 웹 크롤링에 필요한 라이브러리를 설치하는 과정)

from bs4 import BeautifulSoup
# response 에 있는 문자열로 된 데이터를 beautifulsoup 객체로 변환
soup = BeautifulSoup(response.text,'html.parser')

# 원하는 정보를추출
# #contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr
str_table_rows = '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr'
# tbody > tr 줘도 됌. 하지만 플젝할때 여러개 조사할때 겹칠 수 있기때문에 재대로된 경로 정보 추출하여 변수 설정해주는거임.
# print(type(store_rows[0]))
sotre_rows = soup.select(str_table_rows) # 화면 출력
store_lists = []
for row in sotre_rows:(
    store_lists.append( # 튜플로 작성
    row.select('td')[0].text.strip(),  # 지역
    row.select('td')[1].text.strip(),  # 매장명
    row.select('td')[2].text.strip(),  # 현황
    row.select('td')[3].text.strip(),  # 주소
    row.select('td')[5].text.strip()) 
    )  # 전화번호





