import random

def get_com_num(start=1, end=3):
    '''
    랜덤값출력(start ~ end)    
    '''
    return random.randint(start,end)

def get_human_num():
    return int(input("입력(1:가위 2:바위 3:보) :"))

def check_winner(computer, human):
    if computer == human:
        print('비겼습니다.')
    else:
        if (computer == 1 and human ==2) or \
            (computer == 2 and human ==3) or \
            (computer == 3 and human ==1):
            print("당신이 이겼습니다.")
        else:
            print("당신이 졌습니다.")