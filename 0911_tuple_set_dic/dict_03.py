# dict 생성
# dict에서 값을 출력
# dict에서 값을 추가
# dict 삭제
# dict 특정 키의 데이터를 수정


student = { }

student['홍길동'] = 100  #딕셔너리

print(student)

print('-' * 30)

# keys() , .values()
# map() , 함수Parameter - 키워드Parameter , 가변키워드Parameter

my_bag = {'필통' : '노란색' , '공책' : '수학공책' , '지갑' : '분홍색'}
print(my_bag)
print(f"my_bag[필통 : '노란색']")
print(f"my_bag[공책 : '수학공책']")

my_bag['지갑'] = '가죽지갑'
print(f'my_bag[지갑]')

my_bag['물통'] = '하얀색'
print(my_bag['물통'])

del my_bag['공책']

print(my_bag)

my_bag['지갑'] = '분홍색'

# --------------순환문과 연결

for i in my_bag:
    print(f'key = {i} value = {my_bag[i]}')



