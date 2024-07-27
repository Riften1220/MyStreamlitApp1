import pandas as pd
import streamlit as st
import numpy as np
import altair as alt

st.markdown('<style>p { font-size: 16px; }</style>', unsafe_allow_html=True)
 
st.title(r"Welcome To Billy's English Lesson!")

st.header('Question1')
st.write('___ it is today!',unsafe_allow_html=True)
options = ['A. What fine weather', 'B. What a fine weather' ,'C. How a fine weather' ,'D. How fine a weather']
selection = st.radio('**Select an option:**', options)

if st.button('查看答案和解析',1,type='primary'):
    if selection == options[0]:
        st.write('Well Done, your answer is correct')
    else:
        st.write('what a pity! Let Billy tell you why.Because...')



st.header('Question2')
st.write('Which is the way to the ______?')
options2 = ['A. shoe factory', 'B. shoes factory', r"C. shoes' factory",r"D. shoe's factory"]
selection2 = st.radio('Your Answer is:', options2)

if st.button('查看答案和解析',2):
    if selection2 == options2[1]:
        st.write('Well Done, your answer is correct')
    else:
        st.write('what a pity! Let Billy tell you why.')
