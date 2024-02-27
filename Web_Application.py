import streamlit as st
import pandas as pd
import numpy as np

df=pd.read_csv("Model_Feature.csv")

     
sidebar=st.sidebar.selectbox('Anazliler',options=('MEtrics','Feature'))

if sidebar =='Feature':
     st.subheader('Veri Seti')
     st.write('Below is feature how values',df,'Top Three Feature',df[:3])
     st.markdown('Hello!* :sunglasses:')
else:
     st.header('İlk Deneme')
     

     if st.button('Say hello'):
          st.write('Why hello there')
     else:
          st.write('Goodbye') 
