import re
from tkinter import CENTER, StringVar, END
from typing import Pattern
import psycopg2
import customtkinter as ctk
import PIL
from PIL import ImageTk, Image
from customtkinter import CTkLabel


global PASSWORD
global LOGIN


def password_check(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    Пароль считается надежным, если:
    - длина 8 символов или более
    - 1 цифра или более
    - 1 символ или более
    - 1 заглавная буква или более
    - 1 строчная буква или более
    """

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None

    # overall result
    password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)

    if password_ok is True:
        return True
    elif length_error is True:
        return "Слишком короткий пароль"
    elif digit_error is True:
        return "Пароль должен содержать хотя бы 1 цифру"
    elif uppercase_error is True:
        return "Пароль должен содержать хотя бы 1 заглавную букву"
    elif lowercase_error is True:
        return "Пароль должен содержать хотя бы 1 строчную букву"
    elif symbol_error is True:
        return "Пароль должен содержать хотя бы 1 символ"


def registration_function():
    def in_bd(login, password):
        try:
            # Подключиться к существующей базе данных
            connection = psycopg2.connect(user="postgres",
                                          # пароль, который указали при установке PostgreSQL
                                          password="tuiiutVT29072001",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="VKR")

            cursor = connection.cursor()
            postgres_insert_query = """ INSERT INTO login_password (name_login, name_password)
                                               VALUES (%s,%s)"""
            record_to_insert = (login, password)
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print(count, "Запись успешно добавлена ​​в таблицу mobile")

        except Exception as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    def get_text():
        login = entry_login.get()
        password_one = entry_password_first.get()
        password_two = entry_password_second.get()
        r = password_check(password_one)

        if password_one == password_two and r is True:
            in_bd(login, password_one)
            registration_window.destroy()
        else:
            if password_one != password_two:
                label_eror.configure(text="Пароли не совпадают")
            else:
                label_eror.configure(text=password_check(password_one))
            entry_password_first.delete(0, END)
            entry_password_second.delete(0, END)

    registration_window = ctk.CTk()
    registration_window.geometry("300x350")
    registration_window.title("Регистрация")

    main_frame = ctk.CTkFrame(registration_window, fg_color='#242424')

    label_login = ctk.CTkLabel(main_frame, text="Введите логин")
    label_login.pack(anchor=CENTER, pady=10)

    entry_login = ctk.CTkEntry(main_frame)
    entry_login.pack(anchor=CENTER)

    label_password_first = ctk.CTkLabel(main_frame, text="Введите пароль")
    label_password_first.pack(anchor=CENTER, pady=10)

    entry_password_first = ctk.CTkEntry(main_frame, show="*")
    entry_password_first.pack(anchor=CENTER)

    label_password_second = ctk.CTkLabel(main_frame, text="Повторите пароль")
    label_password_second.pack(anchor=CENTER, pady=10)

    entry_password_second = ctk.CTkEntry(main_frame, show="*")
    entry_password_second.pack(anchor=CENTER)

    btn_reg = ctk.CTkButton(main_frame, text="Зарегистрироваться", command=get_text)
    btn_reg.pack(anchor=CENTER, pady=20)

    label_eror = ctk.CTkLabel(main_frame, text="", text_color="red")
    label_eror.pack()

    main_frame.pack(anchor=CENTER, padx=20, pady=20)

    registration_window.mainloop()



