# 선거시스템
# 유권자들은 기호로 투표를 진행 결과를 리스트에 저장
# ex 1,2,3
# 투표는 순환문을 이용하여 유권자가 10이라면 10번 순환하면서 후보자 (1~5) 선택
# [1,1,2,3,4,1,5,1]
# 리스트에 있는 각 번호의 횟수를 구해서 당선자를 출력

cadidata = ['홍길동' , '이순신' , '강감찬' , '율곡' , '신사임당']
vote = [] # 투표
counts = 10 # 유권자
result ={} # 투표카운트 받아야하는 값

count = 0
vote = [1,1,2,3,4,1,5,1]
# for name in counts:
#     vote.append(int(input('투표를 하세요:')))
# print(f'vote = {vote}')

# dict 기능을 이용

for i in vote: # 1~5
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(result)
print(max(result))
print(max(result, key = result.get))


# max( [1,2,3,4,5]) # max() 가장 큰 값을 찾아내는것.
# 키 값을 가져올때, 딕셔너리변수['키값']이 없으면 에러
# 딕셔너리변수.get('키값')  -> 없으면 none
# .get --> 값을 return 하는 함수




