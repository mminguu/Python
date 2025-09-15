# 집합연산이 가능
import random
list_a = random.sample(range(11),7) # 0~7 중복되지 않은 임의의 7개
list_b = random.sample(range(11),7)

# 중복을 허용하면서 0 ~ 10 임의의 7추측
# random.randint(0,10) 임의의 1개

list_c = []
for _ in range(7): # i의 역할이 없을때 언더바(_)를 씀
    list_c.append(random.randint(0,10))


# 합집합 : 연산자 | (파이브 연산자) ---> or
set_a = { 1,2,3 }
set_b = { 3,4,5 }
union_set = set(set_a) | set(set_b)  # 파이프연산자가 합집합
print(union_set)
#   메서드   .union() --> 두 개(또는 그 이상) 집합의 합집합을 구하는 기능으로 위 코드를 아래처럼 간략하게 만들 수 있다
union_set = set_a.union(set_b)
print(union_set)


# 교집합 : 연산자 &    --> and
set_a = { 1,2,3 }
set_b = { 3,4,5 }
print(set_a & set_b)
#   메서드  .intersection()
print(set_a.intersection(set_b))


# 차집합
#  연산자 - 
print(set_a  - set_b) 
#  메서드  .difference()
print(set_a.difference(set_b))   



