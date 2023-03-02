import customtkinter
from tkinter import *
import psycopg2
import start_window
from start_window import password_postgres
from start_window import login_acc, password_acc
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def check_login_password(login, password):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password=start_window.password_postgres,
                                      host="127.0.0.1",
                                      port="5432",
                                      database="database_cam")

        cursor = connection.cursor()
        # SQL-запрос для создания новой таблицы
        create_table_query = "SELECT login, password FROM login_password WHERE login = %s AND password= %s"
        cursor.execute(create_table_query, (login, password))
        connection.commit()
        if cursor.fetchone() is not None:
            return True
        else:
            return False

    except Exception as error:
        print("Ошибка вводе данных при авторизации в PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


