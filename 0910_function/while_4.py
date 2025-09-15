# while_3.py를 함수 형태로 변경해보기

import time
count = 0
is_continue = True

def display_second(count):
    count += 1
    print(f'{count}초') # 몇 초 지났는지 출력
    time.sleep(1)
    return count

count = 0
while is_continue:    
    count = display_second(count)
    
    # 5초단위로 사용자한테 계속 할건지 물어본다.. "To be Continue(Y/y)"
    if count % 5 == 0:
        user_input =  input('To be Continue(Y/N)').upper()
        if not user_input == 'Y':        
            is_continue  = False
