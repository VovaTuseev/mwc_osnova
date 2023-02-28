from tkinter import CENTER
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2
import customtkinter as ctk

login_acc = ''
password_acc = ''
registration_acc = ''
password_postgres = ''


def test_connect():  # Функция проверки подключения
    try:
        conn = psycopg2.connect(user="postgres",
                                # пароль, который указали при установке PostgreSQL
                                password=password_postgres,
                                host="127.0.0.1",
                                port="5432",
                                database="database_cam")
        conn.close()
        return True
    except Exception as e:
        return False


def create_database():  # Функция создания БД (Создает, если такой еще нет)
    if test_connect() is False:
        try:
            # Подключение к существующей базе данных
            connection = psycopg2.connect(user="postgres",
                                          # пароль, который указали при установке PostgreSQL
                                          password=password_postgres,
                                          host="127.0.0.1",
                                          port="5432")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            # Курсор для выполнения операций с базой данных
            cursor = connection.cursor()
            sql_create_database = 'create database database_cam'
            cursor.execute(sql_create_database)
        except Exception as error:
            print("Ошибка при работе с PostgreSQL")
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")


def take_pass_postgresql():  # Функция получения пароля от PostgreSQL с помощью всплывающего окна ----------------------

    def close_window_start():
        try:
            global password_postgres
            password_postgres = get_text()
            create_database()
            create_table()
            create_table_pass_login()
            if test_connect() is True:
                start_login_window.destroy()
            else:
                label_error = ctk.CTkLabel(main_frame, text='Неверный пароль', text_color='red')
                label_error.pack(anchor=CENTER)
        except Exception:
            print("Ошибка при работе с БД")

    def get_text():
        return entry_password.get()

    start_login_window = ctk.CTk()
    start_login_window.geometry("300x200")
    start_login_window.title('Первоначальная настройка')

    main_frame = ctk.CTkFrame(start_login_window, fg_color='#242424')

    label_password = ctk.CTkLabel(main_frame, text="Введите пароль PostgreSQL")
    label_password.pack(anchor=CENTER, pady=10)

    entry_password = ctk.CTkEntry(main_frame)
    entry_password.pack(anchor=CENTER)

    btn_password = ctk.CTkButton(main_frame, text='Готово', command=close_window_start)
    btn_password.pack(anchor=CENTER, pady=15)

    main_frame.pack(anchor=CENTER)

    start_login_window.mainloop()


# Функция создания таблицы данных пользователей ------------------------------------------------------------------------
def create_table():
    def check_table():
        conn = psycopg2.connect(user="postgres",
                                # пароль, который указали при установке PostgreSQL
                                password=password_postgres,
                                host="127.0.0.1",
                                port="5432",
                                database="database_cam")
        cur = conn.cursor()
        cur.execute("select * from information_schema.tables where table_name=%s", ('USER_CAM',))
        return bool(cur.rowcount)

    if check_table() is False:
        # Создание таблицы пользователь-данные камер
        try:
            # Подключиться к существующей базе данных
            connection = psycopg2.connect(user="postgres",
                                          # пароль, который указали при установке PostgreSQL
                                          password=password_postgres,
                                          host="127.0.0.1",
                                          port="5432",
                                          database="database_cam")

            # Создайте курсор для выполнения операций с базой данных
            cursor = connection.cursor()
            # SQL-запрос для создания новой таблицы
            create_table_query = '''CREATE TABLE USER_CAM (USERNAME VARCHAR(20) NOT NULL,
            NAME_CAM VARCHAR(10) NOT NULL,
            IP_CAM VARCHAR(20),
            PASSWORD_CAM VARCHAR(20)); '''
            # Выполнение команды: это создает новую таблицу
            cursor.execute(create_table_query)
            connection.commit()
            print("Таблица успешно создана в PostgreSQL")

        except Exception as error:
            print("Ошибка при создании таблицы в PostgreSQL")
        finally:
            if connection:
                cursor.close()
                connection.close()
            print("Соединение с PostgreSQL закрыто")


# Функция создания таблицы данных логин-пароль -------------------------------------------------------------------------
def create_table_pass_login():
    def check_table():
        conn = psycopg2.connect(user="postgres",
                                # пароль, который указали при установке PostgreSQL
                                password=password_postgres,
                                host="127.0.0.1",
                                port="5432",
                                database="database_cam")
        cur = conn.cursor()
        cur.execute("select * from information_schema.tables where table_name=%s", ('LOGIN_PASSWORD',))
        return bool(cur.rowcount)

    if check_table() is False:
        # Создание таблицы пользователь-данные камер
        try:
            # Подключиться к существующей базе данных
            conn = psycopg2.connect(user="postgres",
                                    # пароль, который указали при установке PostgreSQL
                                    password=password_postgres,
                                    host="127.0.0.1",
                                    port="5432",
                                    database="database_cam")

            # Создайте курсор для выполнения операций с базой данных
            cursor = conn.cursor()
            # SQL-запрос для создания новой таблицы
            create_table_query = '''CREATE TABLE LOGIN_PASSWORD (LOGIN VARCHAR(20) NOT NULL,
            PASSWORD VARCHAR(10) NOT NULL); '''
            # Выполнение команды: это создает новую таблицу
            cursor.execute(create_table_query)
            conn.commit()
            print("Таблица успешно создана в PostgreSQL")

        except Exception:
            print("Ошибка при создании таблицы в PostgreSQL")
        finally:
            if conn:
                cursor.close()
                conn.close()
            print("Соединение с PostgreSQL закрыто")
