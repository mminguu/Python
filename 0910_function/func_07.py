# 간단한 함수
# 함수내의 로직인 한줄로 표현 가능한 함수들

def my_add(a,b): # lambda a,b : 랑 같은 의미
    return a + b # a + b

# lambda (람다함수) : 함수를 한줄로 표현하는 것. 괄호 안씀.
# 간단한 함수를 즉석에서 만들때 유용 
# lambda 함수는 무조건 값을 리턴함. return 키워드 사용 안함.
# lambda 함수를 정의 후 변수에 할당해주면 됨.

test = lambda a,b : a + b

a,b = 10, 20

print(test(a,b))




