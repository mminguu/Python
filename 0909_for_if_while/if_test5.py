# 논리연산자 사용 = and(~이면서 ~이다) or(~이거나) 를 사용하겠다
# 나이가 18살 이상(성인) / 주민번호를 가진 사람은 '입장가능' '입장불가능'

has_id = True
age = int(input('나이를 입력하세요 : ')) # 사용자로부터 키보드의 값을 받는 것
print( type(age))

if has_id and age >= 18:
    print('입장 가능')
else:
    print('입장 불가능')

print('종료')