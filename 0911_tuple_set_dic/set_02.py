# list_a = [1,10,7,2,8]
# list_b = [28,160, 120, 300]
# print(set(list_a+list_b))

# 집합연산이 가능 
import random
list_a = random.sample(range(10),5)
list_b = [1,5,6,6,7,8,9,9]
find_list = [] # 빈 리스트
for data1 in list_a:
    for data2 in list_b:
        if data1 == data2:
            find_list.append(data1)
print(f'list_a = {list_a}')
print(f'list_b = {list_b}')
print(f'find_list = {find_list}')
print(f'set(find_list) = {set(find_list)}')


