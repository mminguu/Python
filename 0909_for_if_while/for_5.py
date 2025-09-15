# 중첩 for

list_1 = [10,20,30]
list_2 = [11,22,33]

list_2th = [list_1 , list_2]

for i in range(len(list_2th)): # 밖의 for문 2번 돌때 안에 for문 3번 돔.
    for j in range(len(list_2th)):
        print(f'list_2th [{i}] [{j}] {list_2th[i][j]}')


# for문의 제약사항 : 무한히 반복 불가능
# while문은 제약사항이 없삼