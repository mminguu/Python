# 리스트 컴프리핸션 간단하게 표현 가능
print([i for i in range(1,10)])  # 예시

total = []
for i in range(1,11):
    total.append(i)


import random

total = []
for i in range(5):
    print(total.append(random.randint(1,10)))

print(total)
# 0~9
print([ random.randint for i in range(5) ])






