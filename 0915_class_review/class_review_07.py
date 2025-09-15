# 파이썬 클래스에서 getter setter 사용법

import random
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property # 함수를 변수처럼 사용하고 싶을때 사용 / 
    def age(self):
        return self._age # 언더바age는 getter
    
p1 = Person("홍길동", 30)
print(p1.age) # age() 함수 이름을 변수처럼 사용하는데 대신 () 안붙임 / 직접 값이 아니라는 것을 알려주기 위해서








# def set_age(self,age):
#     if age < 0:
#         print('나이는 음수가 될 수 없어')
#     else:
#         self.age = age

# p = Person("홍길동", 30)
# print(p.name)
# print(p.age)
# p.name = '강민지'
# p.age = 30




