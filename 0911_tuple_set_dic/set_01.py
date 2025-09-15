# 저금통
list_a = [100 , 500 , 10 , 500 , 100 , 50 , 500 , 10]
# 저금통에 있는 동전의 종류 10 , 50 , 100 , 500
print(set(list_a)) # list_a에 있는 중복 된 리스트 제외

set_a = {1,2,3,1,2,3} # 중복은 제외시킴. set은 {} 를 사용
print(f'set_a = {set_a}')

# print(set_a[0]) # 순서를 보장하지 않기 때문에 인덱스 순서 출력이 안됨
set_a.add(5) 
print(set_a)

set_a.remove(3) # set은 중복은 제외시키기 때문에 set과 remove를 함께 사용 시 해당 값을 찾아 숫자 삭제.
print(set_a)

# pop(0)은 마지막에 있는 데이터가 뭔지 모르기때문에 위치 잘 알고 있어야함.




