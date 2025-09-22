# 1. DB 연결 방법
# 데이터베이스 연결
# 환경변수 로드
# os를 이용해서 환경변수의 값을 읽어서 connection 객체를 생성
# connection 객체의 cursor 객체를 생성
# 커서객체의 callproc('프로시저이름(AddCodeWithTransaction)', [,,,])

import pymysql
from dotenv import load_dotenv
import os

conn = pymysql.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database = 'sqldb'
)

# 프로시져 호출
try:
    with conn.cursor() as cursor:
        cursor.callproc(
            "AddCodeWithTransaction",
            ['ADDR','서울','서울특별시',7,'Y'] 
        )
        
        # SELECT 한 결과
        result = cursor.fetchall()
        print(result)

    conn.commit()
finally:
    conn.close()