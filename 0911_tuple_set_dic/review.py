# 딕셔너리
    # .items()  .keys()  .values()
dict_1 = {
    '국어' : 100,
    '수학' : 90,
    '영어' : 70
}    
print(dict_1)

# 정렬 할때 .items() 사용
    # sorted()
print(dict_1.items())
print(dict(sorted(dict_1.items(), key=lambda data : data[1]))) # 오름차순
print(dict(sorted(dict_1.items(), key=lambda data : data[1],reverse=True))) # 내림차순

# max()
    # max()
# enumerate()
    # 순환문에서 리스트를 감싸면 (인덱스,리스트의값)
# zip()
    # 여러개의 iterable 들을 각 원소를 쌍으로 하는 집합
    # (1,2), ('사과','배')
    # [ (1,'사과'), (2,'배')  ]
# map()
    # iterable한 객체의 각 요소에 특정 함수를 적용
    # map(int, ['1','2'])  -> [1,2]

import collections
datas = [1,1,1,1,2,1,3,4,1,2,4,1]
print(collections.Counter(datas))
# data에 들어 있는 요소들의 카운트를 세주는 .Counter()
# lambda -> 일회용 함수 (버려진함수)