# 사용자 입력 처리 함수
# 함수 이름 : get_data()
#parameter(매개변수)
#   start : 시작값
#   end : 종료값
#   input_Str : 가이드 문구
# 사용자 입력은 input()
# return 정수로 전환된 문자형값 

def get_number():
    while True:
        try:
            h_num = int(input('정수를 입력하세요(1~100) : '))
            if not 0 <= h_num <= 100: # 만약 0과 100사이의 숫자가 아닐경우 raise 발생
                raise ValueError('1과 100사이의 숫자만 입력 가능합니다.') 
        except Exception as e:
            print(f'오류 : {e}')
        else:
            print(f'딩동댕')
        return h_num

get_number()







def get_number(start , end , input_str):
    while True:
        try:
            h_num = int(input(f'정수를 입력하세요(1~100) : {input_str} ({start}~{end})'))
            if not start <= h_num <= end: # 만약 0과 100사이의 숫자가 아닐경우 raise 발생
                raise ValueError('({start}~{end})사이의 숫자만 입력 가능합니다.') 
        except Exception as e:
            print(f'오류 : {e}')
        else:
            return h_num # 변수는 태어난 곳에서 생을 마감함.

get_number(1,10,'점수') # 변수에 값을 할당






