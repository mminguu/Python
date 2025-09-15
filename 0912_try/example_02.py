# 사용자 입력 처리 함수
# 함수 이름 : get_data()
#parameter(매개변수)
#   start : 시작값
#   end : 종료값
#   input_Str : 가이드 문구
# 사용자 입력은 input()
# return 정수로 전환된 문자형값 


# 랜덤점수 - 컴퓨터가 선택한 값
import games_util as gu
import random as rd
start , end = 1 , 100 # tuple 형태로 만들어줌
computer = rd.randint(start , end)


count = 0
game_history = []
while True:
    count += 1
    human =gu.get_data(start , end)
# 승자 선택 로직 
    if gu.check_winner(human , computer,game_history , count): # gu라이브러리 사용
        break



#human > computer 크다
# human < computer 작다
# human = get_data 

















