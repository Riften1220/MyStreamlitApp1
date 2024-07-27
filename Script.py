import pandas as pd
import openpyxl
import streamlit as st
import numpy as np
import altair as alt

st.markdown('<style>p { font-size: 16px; }</style>', unsafe_allow_html=True)
 
st.title(r"Welcome To Billy's English Lesson!")

df = pd.read_excel(r'https://raw.githubusercontent.com/Riften1220/MyStreamlitApp1/master/data.xlsx',dtype=object)

st.sidebar.title(r'题库选项')

set_grade = st.sidebar.selectbox(
    '选择题库年级',
    ['全部','初一', '初二']
)

set_difficulty = st.sidebar.selectbox(
    '选择难度等级',
    ['全部','中等', '简单']
)
if set_grade!='全部':
    df=df[df['grade']==set_grade]

if set_difficulty!='全部':
    df=df[df['difficultylevel']==set_difficulty]

count = 1
for i in df.index:
    st.header('第'+str(count)+'题：')
    count=count+1
    st.write(df.loc[i,'stem'])
    
    options = ['A.'+df.loc[i,'choiceA'],'B.'+df.loc[i,'choiceB'],'C.'+df.loc[i,'choiceC'],'D.'+df.loc[i,'choiceD']]
    selection = st.radio('**Select an option:**', options)

    choice = options.index(selection)+1
    right_answer = df.loc[i,'correctanswer']
    is_correct = choice == right_answer


    if st.button('查看答案和解析',count):
        st.write(df.loc[i,'explanation_general'])
        if choice==1:
            st.write(df.loc[i,'explanationA'])
        elif choice==2:
            st.write(df.loc[i,'explanationB'])
        elif choice==3:
            st.write(df.loc[i,'explanationC'])
        elif choice==4:
            st.write(df.loc[i,'explanationD'])