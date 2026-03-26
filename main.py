from colorama import *
import psycopg2 as ps
import os
import streamlit as st
import streamlit_pydantic as sp
from pydantic import BaseModel
from pydantic import Field
class Platok_Schema(BaseModel):
    id: int
    Название_Платка: str = Field(min_length=5, max_length=50)
    Автор_Платка: str = Field(min_length=5, max_length=50)
    Колорит_1: str= Field(min_length=3, max_length=50)
    Колорит_2: str= Field(min_length=3, max_length=50)
    Колорит_3: str= Field(min_length=3, max_length=50)
    Колорит_4: str= Field(min_length=3, max_length=50)
    Колорит_5: str= Field(min_length=3, max_length=50)
    Узор_Темени: str= Field(min_length=3, max_length=50)
    Узор_Сердцевины: str= Field(min_length=3, max_length=50)
    Узор_Сторон: str= Field(min_length=3, max_length=50)
    Узор_Углов: str= Field(min_length=3, max_length=50)
    Узор_Края: str= Field(min_length=3, max_length=50)
    Цветы_Орнамент: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_1: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_2: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_3: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_4: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_5: str= Field(min_length=3, max_length=50)
    Размер_Платка: str= Field(min_length=3, max_length=50)
    Материал_Платка: str= Field(min_length=3, max_length=50)
    Материал_Бахромы: str= Field(min_length=3, max_length=50)
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
from streamlit import streamlit as st, chat_message
#cmd='streamlit run main.py --server.port 1000'
st.title('ДОБАВИТЬ ПЛАТОК')
with st.form(key='platok_form'):
    st.subheader('Введите данные по платку')
    id=st.text_input
data = sp.pydantic_form(key="Данные по платку", model=Platok_Schema)
if data is not None:
    print(data)
if __name__ == '__main__':
    init(autoreset=True)
    from streamlit.runtime.scriptrunner import get_script_run_ctx
    if get_script_run_ctx() is None:
        from streamlit.web.cli import main
        import sys
        sys.argv=['streamlit', 'run', 'main.py','--server.port=1000']
        main()
#создать ДБparol=''
#Uspech481516232Uspech
#heroku addons:attach --app sekleteja dd1j1646963s9k
#Hydroksydypropildikrahmalfosfat