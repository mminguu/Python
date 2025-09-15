# 숫자 맞추기 게임
# 규칙
# 1. 1~100 사이의 숫자 중 하나를 컴퓨터가 임의로 선택
# 2. 사용자는 숫자를 입력하여 컴퓨터가 선택한 숫자를 맞추려고 시도
# 3. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 크면'너무 큽니다' 출력
# 4. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 작으면 '너무 작습니다' 출력    
# 5. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자와 같으면 '정답입니다.' 출력
# 6. 사용자가 정답을 맞출 때까지 게임은 계속 진행
# 사용자가 번호를 입력하면 맞출때까지 객체값이 살아있어야하는데 값을 외부로부터 받아도 됨

import random

class NumberGuessingGame:
    def __init__(self):
        self.computer = random.randint(1, 100)
        self.mingji = None

    def get_user_guess(self):
        while True:
            try:
                guess = int(input("1부터 100 사이의 숫자를 입력하세요: "))
                if 1 <= guess <= 100:
                    self.mingji = guess
                    break
                else:
                    print("잘못된 입력입니다. 1부터 100 사이의 숫자를 입력하세요.")
            except ValueError:
                print("숫자를 입력하세요.")

    def check_guess(self):
        if self.mingji < self.computer:
            print("너무 작습니다.")
        elif self.mingji > self.computer:
            print("너무 큽니다.")
        else:
            print("정답입니다!")

    def play(self):
        print("숫자 맞추기 게임에 오신 것을 환영합니다!")
        while self.mingji != self.computer:
            self.get_user_guess()
            self.check_guess()




