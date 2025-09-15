#중첩 for

for i in range(3): # 밖의 for문 1번 돌때 안에 for문 3번 돔.
    for j in range(3):
        print(f'i : {i} j : {j}')
    print()
    