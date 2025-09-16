# 상속의 정의
# 상속은 기존 클래스의 속성과 메소드를 새로운 클래스가 물려받는 것을 의미
# 상속을 통해 코드의 재사용을 높히고 계층적인 관계를 표현
# 상속의 기본 문법
# class 부모클래스(self):
#   print('부모 메소드 호출')

#class 자식클래스(부모클래스):
#  print('자식 메소드 호출')

# 부모클래스
class Parents:
    def __init__(self,name):
        self.p_name = name
        print('부모생성자')
    def parents_methid(self):
        print('부모클래스 메소드')

class child(Parents): # 빈껍데기의 생성자가 자동으로 생성되어 있음
    def __init__(self,name,age): # 자식한테만 있는 생성자 age
        Parents.__init__(self,name)
        self.age = age
        print('자식생성자')
    def child_method(self):
        print('자식클래스 메소드')



# child 클래스 객체 c
c = child("강민지" , 20) # 생성자에 맞게 인자 전달
print(c.p_name , c.age) # 오류
