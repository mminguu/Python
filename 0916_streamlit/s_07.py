import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="Streamlit 레이아웃 예제",
    layout="wide"  # 전체 페이지를 wide 모드로 설정
)

# 사이드바 메뉴 생성
with st.sidebar:
    st.title("메뉴")
    selected_menu = st.radio(
        "원하시는 게임을 선택하세요:",
        ["홈", "숫자맞추기", "가위바위보", "도움말"]
    )

# 메인 컨텐츠 영역
def show_home():
    st.header("홈")
    st.write("환영합니다! 이곳은 홈 페이지입니다.")

import random    
def show_game1():
    st.header("숫자맞추기")
    st.write("숫자 맞추기 게임에 오신걸 환영합니다.")

    if 'c_number' not in st.session_state:
        st.session_state.c_number = random.randint(0, 100)    
    c_num = st.session_state.c_number   
#   number_input 위젯에서 Enter키가 입력됐을때 값을 return해서 h_number에 저장     
    h_number = st.number_input("1에서 100 사이의 숫자를 입력하세요:", 0, 100)
    st.write('입력한 숫자 : ', h_number)
    # if st.button("확인"):
    if h_number < c_num:
        st.warning("예측한 값이 낮습니다.")
    elif h_number > c_num:
        st.warning("예측한 값이 높습니다.")
    else:
        st.balloons()
        st.success(f"정답! {c_num}였습니다.")
        del st.session_state.c_number        

def show_game2():
    st.header("가위바위보")
    st.write("가위바위보 게임에 오신걸 환영합니다.")
    # 가위 , 바위 , 보 이미지를 출력하고 다음이미지를 대처하는 방식으로 연속 출력
    # img 이미지 파일 경로
    scissors_img = ""
    rock_img = ""
    paper_img = ""
    images = [scissors_img, rock_img, paper_img]
    placeholder = st.empty()  
    import time  
    for i in range(100):
        img_path = random.choice(images)
        time.sleep(0.05)
        placeholder.image(img_path, width=200)





def show_help():
    st.header("도움말")
    st.write("도움이 필요하시다면 아래 연락처로 문의해주세요:")
    st.write("이메일: help@example.com")


# 선택된 메뉴에 따라 해당하는 컨텐츠 표시
if selected_menu == "홈":
    show_home()
elif selected_menu == "숫자맞추기":
    show_game1()
elif selected_menu == "가위바위보":
    show_game2()
elif selected_menu == "도움말":
    show_help()