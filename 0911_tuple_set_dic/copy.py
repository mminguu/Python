
def change(obj):
     obj[0] = 100

data = [1,2,3] # 리스트는 할당된 값이 변경되기 때문에 .copy()를 쓰면 됨.

change(data) # data 리스트가 변경 되기 원치 않으면 .copy()를 쓰면 됨
print(data)
print('-'*30)

a =10
b = a
b = 1000
print(f'a={a} b={b}')
print('-'*30) #

list_a = [1,2,3]
list_b = list_a.copy() #리스트를 복사하려면 할당 된 주소를 별도로 다시 생성해야하니 복사해야함. -> copy()를 쓰는거임
list_b[0] = 100
print(f'list_a = {list_a} list_b = {list_b}')
print('-'*30) # copy()를 사용하지 않으면 리스트 안에 있는 메모리가 변경됨.






