# 딕셔너리의 정실을 이용한 리스트의 요소를 카운트
# max 함수를 이용하여 기준을 value 로 바꿔서 가장 큰 value에 해당하는 기
# 메소드 .get() 사용

# 키를 이용해서 값을 가져오는 방법
dict_1 = {'사과':10,'포도':20}
print(dict_1['포도'])  # 인덱스 방식 / 없으면 keyerror / 코드의 값을 출력
print(dict_1.get('포도'))  # 메소드 방식 / 없으면 none
print(dict_1.get('파인애플',0))

# 자료구조에서 가장 큰 값을 찾는 내장함수
print(max([1,5,2,3,4,5,1,4,5]))

dict_1 = {'국어' : 80 , '영어' : 100}
print(max(dict_1,key=dict_1.get))  # key=dict_1.get --> 숫자 비교
# max는 문자에서도 ㄱㄴㄷㄹ 순으로 커짐..

# 정렬해주는 함수 --> sorted() 오름차순
list_a = [5,2,1,3,8]
print(sorted(list_a))
print(sorted(list_a,reverse=True)) # reverse=True 내림차순
print(sorted(list_a)[::-1])

#dict
dict_1 = {'국어' : 80 , '영어' : 100,'수학': 40, '국사' : 90}
print(sorted(dict_1)) # key를 기준으로 정렬
print(sorted(dict_1, key=dict_1.get)) # value를 기준으로 정렬
# sorted 오름차순..


