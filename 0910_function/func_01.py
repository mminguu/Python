# import random
# print( random.randint(1,5) ) # 1 ~ 5 사이 랜덤 숫자 호출 

# 함수를 정의 해주는 def 키워드 사용
# 매개변수(Parament) : 함수가 전달 받는 값
# 인자 (Argument)    : 함수를 호출할때 전달 하는 값
# 반환값 (Return Value) : 함수가 작업을 마치고 호출한 곳으로 돌려주는 값 
#                       return 키워드 사용


# 함수의 구성요소
def myCalc(num1, num2): # 함수만들고 밑에 '''요거 설명을 달면 함수의 내용을 사용자에게 알려줌 설명 안에 #을 넣으면 글자크기
    '''
    # 두 개의 값을 받아서 더하는 기능 
    num1은 숫자
    num2는 숫자
    '''
    result = num1 + num2
    return result

# myCalc(1,2) # num1 이 1이 되고 , num2 가 2가 됨.


# 1. 매개변수와 반환값이 없는 함수
def say_hello():
    print('안녕하세요')


# 2. 매개변수가 있고 반환값이 없는 함수
def say_hello_name(name):
    print(f'{name}님 안녕하세요')

say_hello_name('홍길동') # 함수 변수 호출하려면 반환값 정의해줘야함


# 3. 매개변수 없고 반환값이 있는 함수
import datetime # 반환값이 있음(데이터)
def get_current_time():
    return datetime.datetime.now()
print(get_current_time())
#-------------------------------------------

# 위에서 만든 4개의 함수 사용해보기
# myCalc(10)











