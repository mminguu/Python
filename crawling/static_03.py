
# database 접속
# insert 쿼리문을 이용하여 수집한 데이터를 db에 저장
# DB 에 접속

import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv() 

# 1. DB 연결
conn = pymysql.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database = 'shopinfo'
)
