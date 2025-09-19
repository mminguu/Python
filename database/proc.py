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
        # 프로시저 호출
        cursor.callproc(
            "AddCodeWithTransaction",
            ['ADDR','서울','서울특별시',7,'Y']  # 프로시저 파라미터 순서대로 입력
        )
        
        # 프로시저 안에서 SELECT 한 결과 가져오기
        result = cursor.fetchall()
        print(result)  # ex) [('code added success',)] 또는 [('code already existes',)]

    conn.commit()  # commit은 select만 하는 프로시저면 불필요, insert/update 포함이면 안전하게!
finally:
    conn.close()