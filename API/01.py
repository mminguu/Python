from dotenv import load_dotenv
import os
import requests
# .env 로드
load_dotenv()
# P_KEY = os.getenv('PUBLIC_ENCODE_KEY')
P_KEY = 'U5i63xpIWM48raIRQBYpUXbA%2FwKd0iO6n%2Fn1%2BJISyoEW1gWcEiz2No2fHPeid5TZoQN0HV85WyGv6LPwaQ8n4w%3D%3D'
# print(f'P_KEY : {P_KEY[-10:]}')
# 데이터를 요청 할 주소
url = f'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail?page=1&perPage=10&serviceKey={P_KEY}'
# 서버에 보낼 데이터(1페이지를 보여달라는 의미로)
# from_data = {
#     'serviceKey' : P_KEY,
#     'registYy' : '2024',
#     'registMt' : '12',
#     'vhctyAsortCode' : '2',
#     'registGrcCode':'1',
#     'useFuelCode':'6'
# }
import json
response = requests.get(url) #post 방식이 아닌 get 방식
# print(response.text[:500])
data_dict = response.json() # requests는 파이썬의 HTTP 통신 라이브러리
#indent = 들여쓰기
print(data_dict.keys())
json_print = json.dumps(data_dict,indent=4,ensure_ascii=False) #JSON 데이터를 보기 좋게(들여쓰기) 출력
print(json_print)
# 요론식으로 url 주소를 보여달라고 하면 됌
