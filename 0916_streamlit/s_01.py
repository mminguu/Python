# 터미널에서 실행  =>  pip install streamlit
import streamlit as st # 별칭으로 많이 씀 as st / streamlit 장점은 기본적인 반응형도 만들 수 있음
st.title('hello word')
st.header('헤더얌.')
st.subheader('서브헤더임.')
st.write('첫번째 앱')
name = st.text_input('이름을 입력하세요')
st.write(f'{name}님 안녕하세요!')
st.button('버튼')
st.checkbox('체크박스')
st.radio('라디오박스',('a','b','c'))
st.selectbox('셀렉트박스',('일번','이번'))
st.slider('슬라이더',0,100,50)











