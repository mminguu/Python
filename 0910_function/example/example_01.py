# 가위 바위 보 게임 만들기 (컴터 vs 휴먼)
# 컴퓨터적인 사고방식을 가져야함.
# 주어진것만 바라보고 하나씩 스텝 by 스텝
# 규칙 : 컴퓨터가 임의로 숫자를 선택  -----> random
# 인간이 숫자를 입력                 -----> input
# 3번마다 계속할지 물어본다          ------> for
# 가위 : 1 , 바위 : 2 , 보 : 3



import random
computer= random.choice(['가위', '바위', '보']) # 랜덤하게 컴퓨터가 선택한 값
human = input('가위 바위 보 선택 : ')  # 사용자 값
print(f'컴퓨터 : {computer}')
print(f'사용자 : {human}')
      
# 승패 확인

if human == computer:
        print("비겼습니다!")
elif (human == '가위' and computer == '보') or \
    (human == '바위' and computer == '가위') or \
    (human == '보' and computer == '바위'):
        print('이겼습니다.')
else: 
       print("졌습니다.")
        









