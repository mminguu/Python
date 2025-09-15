# 집합을 이루는 요소 : 숫자 , 문자 , 문자열 , 리스트 , set , tuple
# key( 고유의 ID , 주민번호처럼 변하지 않는 요소들만 올 수 있음 ) , value가 한쌍으로 이루어진걸 dict = > set의 성질을 가지고 있어 중복 값이 없음.
# key와 value가 쌍으로 구성 => { key(불변(변수X)) = value , key = value } 
# [ 1 , 1.2 , "1212" , "2" , [1,2] , (1,5,6) , {2,3} ]

student = { # CRUD 가능 , 각 요소에 접근할때 key값으로 접근( index 아님.)
    'name' : '홍길동',
    'age' : 20 , 
    'major' : '컴퓨터'
}
print(f"student['name'] = {student['name']}") # 딕셔너리 만듬

#업데이트
student['name'] = '강감찬'
print(f'student = {student}')

# 삭제
del student["name"]

# 추가
student['addr'] = '서울시 서초구'

# 업데이트와 추가가 같음
# key가 있으면 업데이트 , key가 없으면 추가











