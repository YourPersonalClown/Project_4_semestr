import streamlit as st
from DB_work import *

DB_object = DB_ORM()

st.set_page_config(page_title='Просмотр', page_icon="∴", layout="wide", initial_sidebar_state = 'expanded')

hide_streamlit_style = """
<style>
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.code(DB_object.get_unique(table_name='test_table', column_name='Route'))