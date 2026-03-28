from colorama import *
import psycopg2 as ps
import os
from typing import Annotated
from pydantic import BaseModel, ValidationError
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
from streamlit import streamlit as stml, chat_message
#cmd='streamlit run main.py --server.port 1000'
stml.title('ДОБАВИТЬ ПЛАТОК')
with stml.form(key='ДОБАВИТЬ ПЛАТОК'):
    id=stml.number_input(label='Артикул_Платка',value=1,max_value=500, min_value=1)
    Название_Платка = stml.text_input(label='Название_Платка')
    Автор_Платка = stml.text_input(label='Автор_Платка')
    Колорит_1 = stml.text_input(label='Колорит_1')
    Колорит_2 = stml.text_input(label='Колорит_2')
    Колорит_3 = stml.text_input(label='Колорит_3')
    Колорит_4 = stml.text_input(label='Колорит_4')
    Колорит_5 = stml.text_input(label='Колорит_5')
    Узор_Темени = stml.text_input(label='Узор_Темени')
    Узор_Сердцевины = stml.text_input(label='Узор_Сердцевины')
    Узор_Сторон = stml.text_input(label='Узор_Сторон')
    Узор_Углов = stml.text_input(label='Узор_Углов')
    Узор_Края = stml.text_input(label='Узор_Края')
    Цветы_Орнамент = stml.text_input(label='Цветы_Орнамент')
    Изображённый_Цветок_1 = stml.text_input(label='Изображённый_Цветок_1')
    Изображённый_Цветок_2 = stml.text_input(label='Изображённый_Цветок_2')
    Изображённый_Цветок_3 = stml.text_input(label='Изображённый_Цветок_3')
    Изображённый_Цветок_4 = stml.text_input(label='Изображённый_Цветок_4')
    Изображённый_Цветок_5 = stml.text_input(label='Изображённый_Цветок_5')
    Размер_Платка = stml.text_input(label='Размер_Платка')
    Материал_Платка = stml.text_input(label='Материал_Платка')
    Материал_Бахромы = stml.text_input(label='Материал_Бахромы')
    submit_button=stml.form_submit_button(label='Отправить')
if submit_button:
    platok_vvod={}
    platok_vvod["id"] = id
    platok_vvod["Название_Платка"]=Название_Платка
    platok_vvod["Автор_Платка"]=Автор_Платка
    platok_vvod["Колорит_1"] = Колорит_1
    platok_vvod["Колорит_2"] = Колорит_2
    platok_vvod["Колорит_3"] = Колорит_3
    platok_vvod["Колорит_4"] = Колорит_4
    platok_vvod["Колорит_5"] = Колорит_5
    platok_vvod["Узор_Темени"] = Узор_Темени
    platok_vvod["Узор_Сердцевины"] = Узор_Сердцевины
    platok_vvod["Узор_Сторон"] = Узор_Сторон
    platok_vvod["Узор_Углов"] = Узор_Углов
    platok_vvod["Узор_Края"] = Узор_Края
    platok_vvod["Цветы_Орнамент"] = Цветы_Орнамент
    platok_vvod["Изображённый_Цветок_1"] = Изображённый_Цветок_1
    platok_vvod["Изображённый_Цветок_2"] = Изображённый_Цветок_2
    platok_vvod["Изображённый_Цветок_3"] = Изображённый_Цветок_3
    platok_vvod["Изображённый_Цветок_4"] = Изображённый_Цветок_4
    platok_vvod["Изображённый_Цветок_5"] = Изображённый_Цветок_5
    platok_vvod["Размер_Платка"] = Размер_Платка
    platok_vvod["Материал_Платка"] = Материал_Платка
    platok_vvod["Материал_Бахромы"] = Материал_Бахромы
    platok_kontrol=Platok_Schema(**platok_vvod)
    stml.toast(platok_kontrol)
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