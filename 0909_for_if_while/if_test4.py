# 사용자로부터 점수를 입력받아서 A B C D F 학점을 출력
score = int(input('총점을 입력하세요 : '))
print(f'score = {score}') # "중괄호 안에 있는 파이썬 코드 실행해서 문자열에 넣어줄게!" 라는 뜻

if score > 90:
    print('A')
elif score > 80:
    print('B')
elif score > 70:
    print('C')
elif score > 60:
    print('D')
else:
    print('F')