# 숫자 입력 1 ~ 100 사이
import streamlit as st
import random


c_num = random.randint(1,50) #컴퓨터 숫자 선택
h_num = st.number_input('숫자 입력',1,50)

if st.button('결과확인'):
    if c_num < h_num:
        st.write('다운')
    elif c_num > h_num:
        st.write('업')
    else:
        st.write('컴퓨터 숫자 : ' , c_num)
        st.write('정답')
        st.balloons() # 축하해주는 애니메이션
 
# st.write('입력한 숫자 : ', h_num)












