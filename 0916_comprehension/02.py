list_1  = []
# [ for i in range(5) if i%2 == 0 ] # 2로 나눈 짝수만 list_1에 추가됨


list_1 = [10,20,30,45,69,71,82] # 나이
print(['성인' if i >= 18 else  '미성년' for i in list_1])
