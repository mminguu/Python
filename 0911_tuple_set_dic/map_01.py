# map() -> 자료구조의 각 요소에 특정 함수를 적용


# str_numbers = ['1','10','100']
# print(str_numbers)
# print(list(map(int, str_numbers))) # map(int, str_numbers)

scores = input('국어 영어 수학 점수를 공백을 기준으로 입력하세요 : ')
scores = scores.split()
print(scores)
kor , eng , math = map(int, scores) # 각각 scores에 들어가 있는 값에 int map
print(kor + eng + math)

list_2 = [10,20,30]
# 각원소에 x2
print(list(map(lambda data:data*2, list_2)))


# iterble ---> 여러 값을 차례대로 꺼낼 수 있는 객체 / 하나씩 꺼낼 수 있음 (for문, in 연산자 사용 가능)
# 예시: 문자열, 리스트, 튜플, 딕셔너리, 세트, range 등


