import games

count = 0  # 게임 횟수 카운트

while True:
    # 랜덤하게 선택한 컴퓨터의 값
    computer = games.get_com_num()
    # 사용자의 값
    human = games.get_human_num()
    # 승패 확인
    games.check_winner(computer, human)

    count += 1  # 실제 진행된 게임 수
    if count % 3 == 0:  # 3판마다 물어보기
        is_continue = input('계속할꺼야?(Y/N)').upper()
        if not is_continue == 'Y':
            break