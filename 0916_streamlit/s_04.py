# 1 ~ 100 사이 랜덤한 수 리스트에
import random as rd
datas = [rd.randint(1, 100) for i in range(10)]
print(datas)

import streamlit as st
st.write('막대그래프')
st.bar_chart(datas)

st.write('선그래프')
st.line_chart(datas)

st.write('영역그래프')
st.area_chart(datas)

st.write('1x2 layout')
col1, col2 = st.columns(2)
col1.bar_chart(datas)
col2.line_chart(datas)

st.write('2x2 layout')
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
