import streamlit as st
import pandas as pd
import numpy as np
import streamlit_folium as sf
import folium
from DB_work import *

st.set_page_config(page_title='Подключение к БД',page_icon=":bar_chart",layout="wide")

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.write(st.session_state)