#  클래스 변수 VS 인스턴스 변수



class StudentMng(): # 부모class 정의된걸 넣을 수 있음 / 상속 o
    name = '강민지'

    def make_instance(self):  #instance 변수는 무조건 self 기입
        self.age = 0
        self.addr = 0

s1 = StudentMng()
s2 = StudentMng()
s3 = StudentMng()

s1.name = '강감찬' # 인스턴스 변수   *******인스턴스 변수로 class 접근 가능 (but 다른 언어에서는 불가능) / 사용 X (현업 X)
StudentMng.name = '이순신' # 클래스 변수 *** class 변수는 class에만 접근 가능


# s1 = StudentMng() # 클래스로 받은 값을 객체라고 함.
# print(s1.name) # s1 객체 안에 있는 name 값 출력



# 디버깅시 클래스변수는 모든 객체가 참조하는 변수
# but 객체가 변수를 재 할당 받으면 해당 객체는 더이상 참조하지 않음.







