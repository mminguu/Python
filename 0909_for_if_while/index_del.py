import random # 랜덤 라이브러리 가져오기

random_numbers = random.sample(range(100),5) # 랜덤 라이브러리 중에서 smaple 함수를 호출하여 0~99 중 랜덤으로 5개를 추첨
print(random_numbers)

# 0부터 10 중 랜덤하게 정수의 하나를 출력 
random_int = random.randint(0,10)

random_numbers.append(random_int) # 랜덤으로 정수 하나를 뒤에 넣기.

# 50이 있는지 확인하기
print(50 in random_numbers)
print(random_numbers)



print('-' * 50)



# 삭제하기

# 뭘 삭제하는지 반환하지 않기때문에 변수 지정이 안됨.
del random_numbers[0] # del은 바로 삭제하는거라 del 하기 전에 데이터 위치를 확인해야함. 
print(random_numbers)

# 얘는 꺼내오는 느낌이라 변수를 지정해줘도 출력이 되므로 변수를 출력해보면 뭐가 삭제 되었는지 알 수 있음 (insert기능으로 다시 복원 가능)
random_numbers.pop(0) # 리스트에서 꺼내오는 느낌이라 그 값을 확인할 수 있음
print(random_numbers)


