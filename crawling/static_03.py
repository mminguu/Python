
# database 접속
# insert 쿼리문을 이용하여 수집한 데이터를 db에 저장
# DB 에 접속

import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv() 

# 1. DB 연결
def get_connection():
    return pymysql.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database='shopinfo'
    )
import crawlingcoffee
for page_num in range(1,47):
    with get_connection() as conn:
        with conn.cursor() as cur:
            sql = '''
            insert into shop_base_tbl
            values(null,%s,%s,%s,%s,%s)
            '''
            # cur.execute(sql,(, , , ,))  요로케 작성해야함
            #executemany - 같은 SQL 문을 여러 데이터에 대해 반복 실행 
            cur.executemany(sql,crawlingcoffee.get_data(page_num)) # row를 구성하는 튜플들의 리스트
            conn.commit()
