# enumerate() , zip() , .items() , keys() , .values()
# map() , 함수Parameter - 키워드Parameter , 가변키워드Parameter

list_a = ['사과','포도','딸기']
for index,value in enumerate(list_a): # enumerate() tuple 형태로 바꿔줌
    print(f'{index} : {value}')

# zip() 두개의 리스트 또는 집합을 각 원소별로 묶어준다.


names = ['이순신','강감찬']
ages = [50 , 60]
print(zip(names , ages))
print(list(zip(names , ages))) # [('이순신', 50), ('강감찬', 60)]
print(dict(zip(names , ages))) # {'이순신': 50, '강감찬': 60}

print(list(range(3)))
print(range(3))


# items() 딕셔너리의 메소드임.
dict_1 = {'취미' : '수영', '좋아하는 음식': '떡볶이'}
print(dict_1)
print(f'keys() = {dict_1.keys()}')
print(f'values() = {dict_1.values()}')
print(f'items() = {dict_1.items()}') 












