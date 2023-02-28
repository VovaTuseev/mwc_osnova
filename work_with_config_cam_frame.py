import customtkinter
from tkinter import *
import psycopg2

import start_window
from start_window import password_postgres
from start_window import login_acc
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def set_text(entry, text):
    entry.delete(0, END)
    entry.insert(0, text)


# Функция записи данных в таблицу БД
def set_data_options_cam(name, ip, password):
    # start_window.login_acc = "tuseev"
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password=start_window.password_postgres,
                                      host="127.0.0.1",
                                      port="5432",
                                      database="database_cam")

        # Создайте курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        # SQL-запрос для создания новой таблицы
        create_table_query = """UPDATE USER_CAM SET ip_cam = %s, password_cam = %s WHERE username = %s AND name_cam 
        = %s """
        # Выполнение команды: это создает новую таблицу
        cursor.execute(create_table_query, (ip, password, start_window.login_acc, name))
        connection.commit()
        print("Запись успешно обновлена в PostgreSQL")
        connection.close()

    except Exception as error:
        print("Ошибка при обновлении записей в PostgreSQL", error)


# Функция проверки не занят ли такой логин

