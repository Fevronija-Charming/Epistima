from colorama import *
import psycopg2 as ps
import os
import asyncio
from dotenv import find_dotenv, load_dotenv
from faststream.annotations import FastStream
load_dotenv(find_dotenv())
from typing import Annotated
#брокер
from faststream.rabbit import RabbitBroker,RabbitMessage
broker=RabbitBroker(url=os.getenv("AMQP_LINK"))
#app=FastStream(broker)
@broker.publisher(queue='PLATOKY')
@broker.subscriber(queue='PLATOKY')
async def exchanger(msg: RabbitMessage) -> None:
    await msg.ack()
import pika
Rabbit_Host=os.getenv("AMQP_LINK")
Rabbit_Port=os.getenv("AMQP_PORT")
Rabbit_User=os.getenv("AMQP_USER")
Rabbit_Password=os.getenv("AMQP_PASSWORD")
connection_params = pika.URLParameters(Rabbit_Host)
def get_connection():
    return pika.BlockingConnection(parameters=connection_params)
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr,BaseModel
from typing import List
configuracija_pochty=ConnectionConfig(MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
                                      MAIL_FROM=os.getenv("MAIL_FROM"),
                                      MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
                                      MAIL_FROM_NAME=os.getenv("MAIL_FROM_NAME"),
MAIL_PORT=os.getenv("MAIL_PORT"),MAIL_SERVER=os.getenv("MAIL_SERVER"),MAIL_STARTTLS=os.getenv("MAIL_STARTTLS"),
MAIL_SSL_TLS=os.getenv("MAIL_SSL_TLS"),USE_CREDENTIALS=os.getenv("USE_CREDENTIALS"))
#фоновая задача
from fastapi import BackgroundTasks
async def send_email_async(subject: str, recipients:str, body:str):
    recipient_list = []
    recipient_list.append(recipients)
    message=MessageSchema(subject=subject,recipients=recipient_list,body=body,subtype=MessageType.plain)
    fast_mail = FastMail(configuracija_pochty)
    await fast_mail.send_message(message)
#валидация
from pydantic import BaseModel, ValidationError
from pydantic import Field
#работа с базой данных
from sqlalchemy import  DateTime, String, Float, Column, Integer, func,Text
from sqlalchemy import  select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from psycopg2.errors import *
engine = create_async_engine(os.getenv("DBURL"),echo=True,max_overflow=5,pool_size=5)
session_factory = async_sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False,autoflush=True)
class Base(DeclarativeBase):
    pass
class Platoky(Base):
    __tablename__="ПППЛАТКИ"
    id: Mapped[int]=mapped_column(primary_key=True, autoincrement=True, nullable=False)
    Название: Mapped[str]=mapped_column(String(128), nullable=False)
    Автор: Mapped[str]=mapped_column(String(128), nullable=False)
    Колорит_1: Mapped[str]=mapped_column(String(128), nullable=False)
    Колорит_2: Mapped[str] = mapped_column(String(128), nullable=False)
    Колорит_3: Mapped[str] = mapped_column(String(128), nullable=False)
    Колорит_4: Mapped[str] = mapped_column(String(128), nullable=False)
    Колорит_5: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_темени: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_сердцевины: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_сторон: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_углов: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_края: Mapped[str] = mapped_column(String(128), nullable=False)
    Цветы_Орнамент: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_1: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_2: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_3: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_4: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_5: Mapped[str] = mapped_column(String(128), nullable=False)
    Размер_Платка: Mapped[str]=mapped_column(String(128), nullable=False)
    Материал_Платка: Mapped[str]=mapped_column(String(128), nullable=False)
    Материал_Бахромы: Mapped[str]=mapped_column(String(128), nullable=False)
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
async def send_platok(platok_kontrol: BaseModel):
    async with get_connection() as connection:
        async with connection.channel() as channel:
            channel.queue_declare(queue='PLATOKY2', durable=True)
            channel.basic_publish(exchange='', routing_key='PLATOKY2',body=platok_kontrol)
            channel.close()
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
async def registracija():
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
    session = session_factory()
    query = select(Platoky).where(Platoky.Название == Название_Платка)
    result = await session.execute(query)
    await session.close()
    unikalnost_platka = result.scalar_one_or_none()
    if unikalnost_platka is None:
        session = session_factory()
        query2 = select(Platoky).where(Platoky.id == id)
        result2 = await session.execute(query2)
        await session.close()
        unikalnost_id = result2.scalar_one_or_none()
        if unikalnost_id is None:
            try:
                platok_kontrol = Platok_Schema(**platok_vvod)
                try:
                    platoch_eksemp = Platoky(id=platok_kontrol.id,
                    Название=platok_kontrol.Название_Платка,Автор=platok_kontrol.Автор_Платка,
                    Колорит_1=platok_kontrol.Колорит_1, Колорит_2=platok_kontrol.Колорит_2,
                    Колорит_3=platok_kontrol.Колорит_3, Колорит_4=platok_kontrol.Колорит_4,
                    Колорит_5=platok_kontrol.Колорит_5, Узор_темени=platok_kontrol.Узор_Темени,
                    Узор_сердцевины=platok_kontrol.Узор_Сердцевины, Узор_сторон=platok_kontrol.Узор_Сторон,
                    Узор_углов=platok_kontrol.Узор_Углов, Узор_края=platok_kontrol.Узор_Края,
                    Цветы_Орнамент=platok_kontrol.Цветы_Орнамент,
                    Изображенный_Цветок_1=platok_kontrol.Изображённый_Цветок_1,
                    Изображенный_Цветок_2=platok_kontrol.Изображённый_Цветок_2,
                    Изображенный_Цветок_3=platok_kontrol.Изображённый_Цветок_3,
                    Изображенный_Цветок_4=platok_kontrol.Изображённый_Цветок_4,
                    Изображенный_Цветок_5=platok_kontrol.Изображённый_Цветок_5,
                    Размер_Платка=platok_kontrol.Размер_Платка, Материал_Платка=platok_kontrol.Материал_Платка,
                    Материал_Бахромы=platok_kontrol.Материал_Бахромы)
                    session = session_factory()
                    session.add(platoch_eksemp)
                    #await session.commit()
                    await session.close()
                    stml.toast(platok_kontrol)
                    try:
                        async with broker:
                            await broker.publish(message=f"{platok_kontrol}", queue="PLATOKY")
                            try:
                                platok_predstav = ["id:", "Название платка:", "Автор платка:", "Вариант окраски 1:",
                                "Вариант окраски 2:", "Вариант окраски 3", "Вариант окраски 4:", "Вариант окраски 5:",
                                "Узор темени:", "Узор сердцевины:", "Узор сторон:", "Узор углов:", "Узор края:",
                                "Соотношение цветов и узора:", "Нарисованный цветок 1:", "Нарисованный цветок 2:",
                                "Нарисованный цветок 3:", "Нарисованный цветок 4:", "Нарисованный цветок 5:",
                                "Размер платка:", "Материал платка:", "Материал бахромы:"]
                                svedenija_platok = [str(id), Название_Платка, Автор_Платка, Колорит_1, Колорит_2,
                                Колорит_3, Колорит_4, Колорит_5, Узор_Темени, Узор_Сердцевины, Узор_Сторон, Узор_Углов,
                                Узор_Края, Цветы_Орнамент, Изображённый_Цветок_1, Изображённый_Цветок_2,
                                Изображённый_Цветок_3, Изображённый_Цветок_4, Изображённый_Цветок_5,Размер_Платка,
                                Материал_Платка,Материал_Бахромы]
                                peremycka1 = " -> "
                                peremycka2 = "; "
                                soobshenije = ""
                                for i in range(len(svedenija_platok)):
                                    soobshenije = soobshenije + platok_predstav[i] + peremycka1 + svedenija_platok[i] + peremycka2
                                recipient = os.getenv("RECIPIENT1")
                                background_task=BackgroundTasks()
                                background_task.add_task(send_email_async, "Добавлен новый проект", recipient, soobshenije)
                            except: stml.warning('Проблема с почтой')
                    except: stml.warning('Проблема с брокером')
                except: stml.warning('Проблема с БД')
            except ValidationError: stml.warning('Данные не прошли валидацию')
        else:
            stml.warning('id занят')
    else:
        stml.warning('Этот платок уже записан')

if submit_button:
    asyncio.run(registracija())
def main():
    pass
if __name__ == '__main__':
    main()
    init(autoreset=True)
    #from streamlit.runtime.scriptrunner import get_script_run_ctx
    #if get_script_run_ctx() is None:
    #from streamlit.web.cli import main
    #import sys
    #sys.argv=['streamlit', 'run', 'main.py','--server.port=1000']
    #main()
#создать ДБparol=''
#Uspech481516232Uspech
#heroku addons:attach --app sekleteja dd1j1646963s9k
#Hydroksydypropildikrahmalfosfat