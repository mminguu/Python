# 오류를 피해가는 행위 --> 예외처리



# num1 = int(input("숫자를 입력하세여 : "))
# num2 = int(input("숫자를 입력하세여 : "))

try: #예외가 발생할 가능성이 있는 코드가 있을때 사용
    num1 , num2 = map(int , input("공백을 기준으로 두개의 숫자를 입력 : ").split())
    calc_list = [num1 + num2 , num1 - num2 , num1 * num2 , num1 / num2 ]

    print( '1. 더하기' , end = '\t')
    print( '2. 빼기' , end = '\t')
    print( '3. 곱하기' , end = '\t')
    print( '4. 나누기' , end = '\t')
    choice = int(input(' 원하는 결과를 입력하세요 : '))
    print(f'결과는 = {calc_list[choice]}') 
except: # 예외가 발생했을때 실행할 코드
    print('오류발생')
else: #예외가 발생하지 않았을때 실행할 코드 / 현업에서 잘 안씀 / 
     print('프로그램 종료')
finally: # 무조건 실행할 코드
    print('프로그램 종료')

# 오타
# ********* try 구문 : 예외 구분해보기***********




# index기준으로 4번째는 없기때문에 공백 오류
# 0으로 나누기하면 오류
# 문자열 오류











# print(f'{num1} + {num2} = {calc_list[0]}')
# print(f'{num1} - {num2} = {calc_list[1]}')
# print(f'{num1} * {num2} = {calc_list[2]}')
# print(f'{num1} / {num2} = {calc_list[3]}')

# print(f'{num1} + {num2} = {num1 + num2}')
# print(f'{num1} - {num2} = {num1 - num2}')
# print(f'{num1} * {num2} = {num1 * num2}')
# print(f'{num1} / {num2} = {num1 / num2}')









