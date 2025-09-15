# 생성자 : 객체 생성 시 함수 자동 생성 해줌

class People():
    def __init__(self):  # __init__
        self.name = None
        self.age = None
        self.addr = None
        print('생성자 호출')

print('h1 객체 생성 전')
h1 = People()
print(h1.addr)
print('h1 객체 생성후')
print(h1.age)