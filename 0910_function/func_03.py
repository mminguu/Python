# 다양한 매개변수
# 기본 매개변수  default , parament

def myAdd(num1,num2,num3):     # 함수에 변수를 설정
    return num1 + num2 + num3  # 변수 더한값을 반환
result = myAdd(10,19)          # 변수값을 지정하여 result에 할당 
print(f'내 나이는 : {result}')  # 출력
# 함수에 들어가는 매개변수는 순차적으로 들어가기에 
# 뒤에 있는 매개변수에 값을 할당해주면 됨.