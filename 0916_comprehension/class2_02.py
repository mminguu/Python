# 정수 값이고 주어진 범위를 벗어나면 발생하는 Exception
class OutRangeError(Exception):
    def __init__(self, strname):
        super().__init__(strname)
    def show__init__(self):
        return '사용자가 정의한 예외입니다'
# 사용자 정의 에러 발생 시킴


try:
    number = 100
    if not 0 <= number <= 10:
        raise OutRangeError('0~10 사이의 값을 벗어났습니다.') # 예외 발생
except ValueError:
    print('error')

# except OutRangeError as e:
#     print(e.show_info())






