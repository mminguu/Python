# 가위바위보 게임
# 사용자로부터 입력을 받아 컴퓨터와 대결하는 간단한 가위바위보 게임을 만들어보자.
# 게임의 승패를 판단하고 결과를 출력.
# 가위는 1 , 바위는2, 보는 3으로 표현
# 게임이 끝나면 다시 할지 물어보고, 사용자가 원하면 게임을 반복.
# 어떻게 코드작성을 하면 좋을지 생각 (기획)
# 동시에 생성 => 컴퓨터의 값과 사용자의 값이 필요 객체가 살아있어야함(객체 하나 = 게임1판)

import random

class RPSGame:
    choices = {1: "가위", 2: "바위", 3: "보"} # 클래스 변수

    def __init__(self):
        self.user_choice = None
        self.computer_choice = None

    def get_user_choice(self):
        while True:
            try:
                choice = int(input("가위(1), 바위(2), 보(3) 중 하나를 선택하세요: "))
                if choice in self.choices: # 딕셔너리 방식 
                    self.user_choice = choice
                    break
                else:
                    print("잘못된 입력입니다. 1, 2, 3 중 하나를 선택하세요.")
            except ValueError:
                print("숫자를 입력하세요.")

    def get_computer_choice(self): # 메소드로 표현 /
        self.computer_choice = random.randint(1, 3) # 생성자로도 표현 가능

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            return "무승부"
        elif (self.user_choice == 1 and self.computer_choice == 3):
            return "사용자 승리"
        else:
            return "컴퓨터 승리"
        
    def play(self):
        while True:
            self.get_user_choice()
            self.get_computer_choice()
            print(f"사용자 선택: {self.choices[self.user_choice]}, 컴퓨터 선택: {self.choices[self.computer_choice]}")
            result = self.determine_winner()
            print(f"결과: {result}")
            
            again = input("다시 하시겠습니까? (y/n): ").lower()
            if again != 'y':
                print("게임을 종료합니다.")
                break

# for _ in range(1): # 반복문을 통해서 게임을 계속 진행
while True:
    RPSGame().play() # 객체 생성할 필요가 없음
    again = input("다시 하시겠습니까? (y/n): ").strip().lower()
    if again != 'y':
        print("게임을 종료합니다.")
    break



# 학생 관리 시 학생들 마다 각각 각체를 생성하지만, 가위바위보는 하나의 게임만 존재
# 그래서 객체를 하나만 생성해서 사용

