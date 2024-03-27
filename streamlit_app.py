import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('📊 Interactive Data Explorer')

st.title("this is the app title")
st.image('https://www.bing.com/ck/a?!&&p=126ac7a60d7e3054JmltdHM9MTcxMTQxMTIwMCZpZ3VpZD0wNjZhZDQ4ZS05YjM5LTYxNjYtMTJjOS1kZjQxOWEwNTYwNWEmaW5zaWQ9NTUyNQ&ptn=3&ver=2&hsh=3&fclid=066ad48e-9b39-6166-12c9-df419a05605a&u=a1L2ltYWdlcy9zZWFyY2g_cT1laGRka2VvJTIwdGt3bHMmRk9STT1JUUZSQkEmaWQ9NEZBQTFBNEQ4Nzg0MUI4N0FDNEM1MkVGRTBDRDk3NzcxMDFBOThGNg&ntb=1')

st.sidebar.title('뭘봐')

st.checkbox('yes')
st.button('Click')
st.radio('성별을 고르시오',['Male','Female'])
st.selectbox('고르시오',['롯데','삼성'])
st.slider('Pick a number',0,50)