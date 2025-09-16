from abc import ABC , abstractmethod

class Parents(ABC):
    def make_money(self):
        raise NotImplementedError
    
    @abstractmethod # 추상화메소드를 사용할경우 반드시 자식클래스에서도 정의되야함.
    def save_money(self):
        # print('저축')
        pass

class Child(Parents):
    def make_money(self): # 부모의 make_money를 재정의(override)
        print('장사')
    def save_money(self):
        print('투자')
         
c = Child() # 두 부모의 추상메소드를 상속받으면 클래스에서 반드시 재 정의 안하면 객체생성 불가.
c.make_money() # 다형성 자식클래스에서 재 정의 안하면 예외 발생되도록 설계.

# 부모꺼랑 똑같은걸 정의할 경우 자식껄 씀.


