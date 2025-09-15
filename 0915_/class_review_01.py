# 기본 클래스 생성
class Review: # review라는 이름의 클래스
    # 클래스 변수 생성
    count = 0 # 모든 객체들이 바라봄. # 클래스 변수는 객체가 아닌 클래스에 종속됨.
    # 생성자 메소드
    def __init__(self,name=''): # __init__ = > 메소드 (생성자) : 객체가 생성될 때 자동으로 호출되는 메소드
         self.name = '강민지' # name을 자체적으로 가지고 있음

# 인스턴스 생성
r1 = Review()
r2 = Review()

# 인스턴스 변수 변경
r1.name = '첫번째 리뷰' # 점 앞에 있는 변수 = 객체
print(f'r1 인스턴스 변수 : {r1.name} / r2 인스턴스 변수 : {r2.name}')
print(f'클래스 변수 : {Review.count} / r1 클래스 변수 : {r1.count} / r2 클래스 변수 : {r2.count}') 
# 모든 인스턴수 변수는 객체에 의존함.
# lambda = 익명함수(이름 없는 함수)
