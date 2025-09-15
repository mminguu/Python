# lisst , set , tuple , dict
# key와 value가 쌍으로 구성 => { key(불변(변수X)):value , key:value }
result = dict( [ ['name', '홍길동'] , ['age' , 20] ] )
print(type(result))
print(result)

# 2개의 list
# 1개는 key에 해당하는 값들의 집합
# 1개는 값에 해당하는 집합

names = ['홍길동' , '이순신' , '강감찬']
scores = [100,90,80]

#---------------------------------------------------------------------

# 비어있는 dict 변수를 생성
# 변수 ['key'] = 값 형태로 생성 - 순환문을 통해서 작성

names = ['홍길동','이순신','강감찬']
scores = [100,99,98]
students = {}

count = 0
for name in names:
    students[name] = scores[count]
    count += 1
#--------------------------------------
for i in range(len(names)):
    students[ names[i]  ] = scores[i]








