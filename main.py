import streamlit as st
import pandas as pd

st.title('횡단보도 우회전 사고현황')

data_2021 = {'사고건수': [140,126,189,201,217,200,177,168,191,216,222,179],
        '사망자수': [4,1,3,2,2,1,0,1,2,2,2,1,],
        '부상자수': [141,131,196,211,230,210,188,177,199,223,238,187]}

data_2020 = {'사고건수': [170,150,138,143,163,190,187,144,168,231,191,140],
        '사망자수': [3,1,2,0,4,0,2,2,1,5,5,1],
        '부상자수': [177,156,142,150,178,204,190,150,175,237,191,146]}

data_2019 = {'사고건수': [175,161,200,195,212,185,199,181,203,208,224,192],
        '사망자수': [2,1,5,2,0,3,3,4,4,2,6,5],
        '부상자수': [184,178,207,211,225,188,214,188,214,219,238,201]}

data_2018 = {'사고건수': [177,172,202,197,174,183,182,150,170,195,209,183],
        '사망자수': [5,3,6,1,0,3,2,7,4,5,2,3],
        '부상자수': [182,186,207,204,195,193,193,156,200,206,214,194]}

data_2017 = {'사고건수': [98,71,111,102,118,120,86,167,205,171,212,160],
        '사망자수': [2,1,2,1,3,5,1,3,7,2,6,3],
        '부상자수': [101,79,119,114,129,125,94,174,214,182,223,166]}

index_name = ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']

df_2021 = pd.DataFrame(data_2021, index = index_name)
df_2020 = pd.DataFrame(data_2020, index = index_name)
df_2019 = pd.DataFrame(data_2019, index = index_name)
df_2018 = pd.DataFrame(data_2018, index = index_name)
df_2017 = pd.DataFrame(data_2017, index = index_name)

option = st.selectbox(
    '연도',
    (['2021', '2020', '2019', '2018', '2017']))

st.subheader('사고현황')

if option == '2021':
    st.table(df_2021)
if option == '2020':
    st.table(df_2020)
if option == '2019':
    st.table(df_2019)
if option == '2018':
    st.table(df_2018)
if option == '2017':
    st.table(df_2017)


col1, col2 = st.columns(2)

with col1:
    if option == '2021':
        st.line_chart(df_2021)
    if option == '2020':
        st.line_chart(df_2020)
    if option == '2019':
        st.line_chart(df_2019)
    if option == '2018':
        st.line_chart(df_2018)
    if option == '2017':
        st.line_chart(df_2017)

with col2:
    if option == '2021':
        st.bar_chart(df_2021)
    if option == '2020':
        st.bar_chart(df_2020)
    if option == '2019':
        st.bar_chart(df_2019)
    if option == '2018':
        st.bar_chart(df_2018)
    if option == '2017':
        st.bar_chart(df_2017)
