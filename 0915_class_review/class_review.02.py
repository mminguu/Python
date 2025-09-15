# 학생 클래스 생성
# 인스턴스 변수 : 이름 국어 영어 수학
# 인스턴스 메소드 : 총점, 평균, 학점
class Student:
    # 인스턴스 변수 : 이름 , 국어 , 영어 , 수학
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self): # 총점
        return self.kor + self.eng + self.math

    def average(self): # 평균
        return self.total() / 3

    def grade(self): # 학점
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
        
    def to_string(self): # 문자열로 출력
        return f'이름: {self.name}, 국어: {self.kor}, 영어: {self.eng}, 수학: {self.math}, 총점: {self.total()}, 평균: {self.average():.2f}, 학점: {self.grade()}'
    
    # 인스턴스 생성
s1 = Student('강민지', 95, 85, 90)
s2 = Student('강감찬', 80, 70, 75)  
s3 = Student('이순신', 60, 65, 70)





