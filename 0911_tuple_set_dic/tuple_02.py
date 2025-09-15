#튜플 -> 리스트   리스트 -> 튜플

list_a =[1,2,3]
tuple_a = (10,20,30)
print(f'type(list_a) = {type(list_a)}')
print(f'type(tuple_a) = {type(tuple_a)}')

print(tuple(list_a)) # list_a 가 tuple로 변경됨
print(type(tuple(list_a)))

list_a = tuple(list_a)
print(list_a)




