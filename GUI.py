import tkinter as tk
from tkinter import scrolledtext
from ATMmachineforGUI import *
from account import NumericException
from re import fullmatch
import os
import sys

# синхронизация и возвращение к основному меню
def exit_user(window):
    # atm.deauthorize()
    create_main_window(window)

# возвращение к основному меню после добавления пользователя и инкассации
def exit_not_user(window):
    create_main_window(window)

# получение баланса пользователя
def get_balance_user(window):
    for item in window.winfo_children():
        item.destroy()

    balance_label = tk.Label(window, text=atm.getBalance(), width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid") # atm.getBalance()
    balance_label.config(bg="#FFFF33")
    balance_label.place(x=105, y=60)

    exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: authorize(window))
    exit_button.config(bg="#FFFF33")
    exit_button.place(x=47, y=280)

# обработка зачисления средств на пользовательский счет
def add_money_user(window, amount_entry):
    amount = amount_entry.get()

    try:
        amount = int(amount)
        if (amount <= 0):
            raise NumericException("Недопустимый формат")

    except NumericException as e:
        for item in window.winfo_children():
            item.destroy()
        error_label = tk.Label(window, text=e.message, width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
        error_label.config(bg="#FFFF33")
        error_label.place(x=105, y=10)

        exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: authorize(window))
        exit_button.config(bg="#FFFF33")
        exit_button.place(x=47, y=300)
        return

    except ValueError as e:
        for item in window.winfo_children():
            item.destroy()
        error_label = tk.Label(window, text="Недопустимый формат", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
        error_label.config(bg="#FFFF33")
        error_label.place(x=105, y=10)

        exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: authorize(window))
        exit_button.config(bg="#FFFF33")
        exit_button.place(x=47, y=300)
        return

    atm.putMoney(amount)

    for item in window.winfo_children():
        if isinstance(item, tk.Button):
            if item.cget("text") == "Внести деньги":
                item.destroy()
                break


    done_label = tk.Label(window, text="Средства внесены", width=40, height=7, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
    done_label.config(bg="#FFFF33")
    done_label.place(x=115, y=60)

# внесение средств на счет пользователя
def increase_balance_user(window):
    for item in window.winfo_children():
        item.destroy()

    amount_label = tk.Label(window, text="Введите сумму для внесения на счёт: ", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
    amount_label.config(bg="#FFFF33")
    amount_label.place(x=115, y=60)

    amount_entry = tk.Entry(window, width=35)
    amount_entry.place(x=210, y=160)

    enter_button = tk.Button(window, text="Внести деньги", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: add_money_user(window, amount_entry))
    enter_button.config(bg="#FFFF33")
    enter_button.place(x=47, y=200)

    exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: authorize(window))
    exit_button.config(bg="#FFFF33")
    exit_button.place(x=47, y=300)

# обработка списания средств с пользовательского счета
def take_money_user(window, amount_entry):
    amount = amount_entry.get()

    try:
        amount = int(amount)
        if (amount <= 0):
            raise NumericException("Недопустимый формат")

    except NumericException as e:
        for item in window.winfo_children():
            item.destroy()
        error_label = tk.Label(window, text=e.message, width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
        error_label.config(bg="#FFFF33")
        error_label.place(x=105, y=10)

        exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: authorize(window))
        exit_button.config(bg="#FFFF33")
        exit_button.place(x=47, y=300)
        return

    except ValueError as e:
        for item in window.winfo_children():
            item.destroy()
        error_label = tk.Label(window, text="Недопустимый формат", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
        error_label.config(bg="#FFFF33")
        error_label.place(x=105, y=10)

        exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: authorize(window))
        exit_button.config(bg="#FFFF33")
        exit_button.place(x=47, y=300)
        return

    result = atm.getMoney(amount)

    for item in window.winfo_children():
        if isinstance(item, tk.Button):
            if item.cget("text") == "Списать деньги":
                item.destroy()
                break


    done_label = tk.Label(window, text=result[1], width=40, height=7, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
    done_label.config(bg="#FFFF33")
    done_label.place(x=115, y=60)

# списание средств со счета пользователя
def decrease_balance_user(window):
    for item in window.winfo_children():
        item.destroy()

    amount_label = tk.Label(window, text="Введите сумму для списания со счёта: ", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid") # atm.getBalance()
    amount_label.config(bg="#FFFF33")
    amount_label.place(x=115, y=60)

    amount_entry = tk.Entry(window, width=35)
    amount_entry.place(x=210, y=160)

    enter_button = tk.Button(window, text="Списать деньги", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: take_money_user(window, amount_entry))
    enter_button.config(bg="#FFFF33")
    enter_button.place(x=47, y=200)

    exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: authorize(window))
    exit_button.config(bg="#FFFF33")
    exit_button.place(x=47, y=300)

# получение баланса банкомата
def get_balance_incass(window):
    for item in window.winfo_children():
        item.destroy()

    balance_label = tk.Label(window, text=atm.getAmount(), width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
    balance_label.config(bg="#FFFF33")
    balance_label.place(x=105, y=60)

    exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: incass(window))
    exit_button.config(bg="#FFFF33")
    exit_button.place(x=47, y=280)

# обработка внесения средств в банкомат
def add_money_incass(window, amount_entry):
    amount = amount_entry.get()

    try:
        amount = int(amount)
        if (amount <= 0):
            raise NumericException("Недопустимый формат")

    except NumericException as e:
        for item in window.winfo_children():
            item.destroy()
        error_label = tk.Label(window, text=e.message, width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
        error_label.config(bg="#FFFF33")
        error_label.place(x=105, y=10)

        exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: incass(window))
        exit_button.config(bg="#FFFF33")
        exit_button.place(x=47, y=300)
        return

    except ValueError as e:
        for item in window.winfo_children():
            item.destroy()
        error_label = tk.Label(window, text="Недопустимый формат", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
        error_label.config(bg="#FFFF33")
        error_label.place(x=105, y=10)

        exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: incass(window))
        exit_button.config(bg="#FFFF33")
        exit_button.place(x=47, y=300)
        return

    atm.increaseAmount(amount)

    for item in window.winfo_children():
        if isinstance(item, tk.Button):
            if item.cget("text") == "Внести средства":
                item.destroy()
                break

    done_label = tk.Label(window, text="Средства внесены", width=40, height=7, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
    done_label.config(bg="#FFFF33")
    done_label.place(x=115, y=60)

# внесение средств в банкомат
def increase_balance_incass(window):
    for item in window.winfo_children():
        item.destroy()

    amount_label = tk.Label(window, text="Введите сумму для внесения в банкомат: ", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid") # atm.getBalance()
    amount_label.config(bg="#FFFF33")
    amount_label.place(x=115, y=60)

    amount_entry = tk.Entry(window, width=35)
    amount_entry.place(x=210, y=160)

    enter_button = tk.Button(window, text="Внести средства", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: add_money_incass(window, amount_entry))
    enter_button.config(bg="#FFFF33")
    enter_button.place(x=47, y=200)

    exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: incass(window))
    exit_button.config(bg="#FFFF33")
    exit_button.place(x=47, y=300)

def take_money_incass(window, amount_entry):
    amount = amount_entry.get()

    try:
        amount = int(amount)
        if (amount <= 0):
            raise NumericException("Недопустимый формат")

    except NumericException as e:
        for item in window.winfo_children():
            item.destroy()
        error_label = tk.Label(window, text=e.message, width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
        error_label.config(bg="#FFFF33")
        error_label.place(x=105, y=10)

        exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: incass(window))
        exit_button.config(bg="#FFFF33")
        exit_button.place(x=47, y=300)
        return

    except ValueError as e:
        for item in window.winfo_children():
            item.destroy()
        error_label = tk.Label(window, text="Недопустимый формат", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
        error_label.config(bg="#FFFF33")
        error_label.place(x=105, y=10)

        exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: incass(window))
        exit_button.config(bg="#FFFF33")
        exit_button.place(x=47, y=300)
        return

    result = atm.decreaseAmount(amount)

    for item in window.winfo_children():
        if isinstance(item, tk.Button):
            if item.cget("text") == "Списать средства":
                item.destroy()
                break

    done_label = tk.Label(window, text=result[1], width=40, height=7, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
    done_label.config(bg="#FFFF33")
    done_label.place(x=115, y=60)

# списание средств с банкомата
def decrease_balance_incass(window):
    for item in window.winfo_children():
        item.destroy()

    amount_label = tk.Label(window, text="Введите сумму для списания с банкомата: ", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid") # atm.getBalance()
    amount_label.config(bg="#FFFF33")
    amount_label.place(x=115, y=60)

    amount_entry = tk.Entry(window, width=35)
    amount_entry.place(x=210, y=160)

    enter_button = tk.Button(window, text="Списать средства", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: take_money_incass(window, amount_entry))
    enter_button.config(bg="#FFFF33")
    enter_button.place(x=47, y=200)

    exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: incass(window))
    exit_button.config(bg="#FFFF33")
    exit_button.place(x=47, y=300)

# получение истории операций пользователя
def get_operations_history(window):
    for item in window.winfo_children():
        item.destroy()

    history = atm.getOperations()

    history_scroled = scrolledtext.ScrolledText(window, width=40, height=10)
    history_scroled.config(bg="#FFFF33")
    history_scroled.insert(tk.END, history)
    history_scroled.place(x=175, y=90)

    exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: authorize(window))
    exit_button.config(bg="#FFFF33")
    exit_button.place(x=47, y=280)

# отрисовка окна действий для пользователя
def authorize(window):
    for item in window.winfo_children():
        item.destroy()

    greeting_label = tk.Label(window, text="Выберите действие", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
    greeting_label.config(bg="#FFFF33")
    greeting_label.place(x=105, y=10)

    enter_button = tk.Button(window, text="Узнать баланс", width=35, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: get_balance_user(window))
    enter_button.config(bg="#FFFF33")
    enter_button.place(x=20, y=80)

    enter_button = tk.Button(window, text="Внести деньги", width=35, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: increase_balance_user(window))
    enter_button.config(bg="#FFFF33")
    enter_button.place(x=320, y=80)

    user_add_button = tk.Button(window, text="Снять деньги", width=35, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: decrease_balance_user(window))
    user_add_button.config(bg="#FFFF33")
    user_add_button.place(x=20, y=180)

    bank_button = tk.Button(window, text="Получить историю операций", width=35, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: get_operations_history(window))
    bank_button.config(bg="#FFFF33")
    bank_button.place(x=320, y=180)

    exit_button = tk.Button(window, text="Выход из системы", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: exit_user(window))
    exit_button.config(bg="#FFFF33")
    exit_button.place(x=47, y=280)

# обработка попытки входа в систему
def try_authorize(window, surname_entry, name_entry, pin_entry):
    surname = surname_entry.get()
    name = name_entry.get()
    pin = pin_entry.get()

    if name == "" or surname == "" or pin == "":
        for item in window.winfo_children():
            item.destroy()

        error_label = tk.Label(window, text="Данные введены некорректно", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
        error_label.config(bg="#FFFF33")
        error_label.place(x=105, y=10)

        exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: create_main_window(window))
        exit_button.config(bg="#FFFF33")
        exit_button.place(x=47, y=300)
    else:
        username = name + " " + surname
        try:
            pincode = pin
            if fullmatch("[0-9]{4}", pincode) == None:
                raise NumericException("Некорректный формат pin-кода")
        except NumericException as e:
            for item in window.winfo_children():
                item.destroy()
            error_label = tk.Label(window, text=e.message, width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
            error_label.config(bg="#FFFF33")
            error_label.place(x=105, y=10)

            exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: create_main_window(window))
            exit_button.config(bg="#FFFF33")
            exit_button.place(x=47, y=300)
            return

        result = atm.authorize(surname, name, pincode)
        flag, name = result[0], result[1]
        if flag:
            for item in window.winfo_children():
                item.destroy()

            enter_label = tk.Label(window, text="Авторизация успешна. Здравствуйте, " + name, width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
            enter_label.config(bg="#FFFF33")
            enter_label.place(x=105, y=10)

            exit_button = tk.Button(window, text="Перейти к действиям", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: authorize(window))
            exit_button.config(bg="#FFFF33")
            exit_button.place(x=47, y=280)
        else:
            for item in window.winfo_children():
                item.destroy()

            error_label = tk.Label(window, text="Пользователь не найден", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
            error_label.config(bg="#FFFF33")
            error_label.place(x=105, y=10)

            exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: create_main_window(window))
            exit_button.config(bg="#FFFF33")
            exit_button.place(x=47, y=280)

#отрисовка окна входа в систему
def enter(window):
    for item in window.winfo_children():
        item.destroy()

    surname_label = tk.Label(window, text="Введите фамилию пользователя:", width=35, height=3, font=("Arial", 10), borderwidth=2, relief="solid")
    surname_label.config(bg="#FFFF33")
    surname_label.place(x=35, y=10)

    surname_entry = tk.Entry(window, width=35)
    surname_entry.place(x=350, y=25)

    name_label = tk.Label(window, text="Введите имя пользователя:", width=35, height=3, font=("Arial", 10), borderwidth=2, relief="solid")
    name_label.config(bg="#FFFF33")
    name_label.place(x=35, y=60)

    name_entry = tk.Entry(window, width=35)
    name_entry.place(x=350, y=75)


    pin_label = tk.Label(window, text="Введите пин-код:", width=35, height=3, font=("Arial", 10), borderwidth=2, relief="solid")
    pin_label.config(bg="#FFFF33")
    pin_label.place(x=35, y=110)

    pin_entry = tk.Entry(window, width=35)
    pin_entry.place(x=350, y=130)

    exit_button = tk.Button(window, text="Ввод", width=35, height=8, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: try_authorize(window, surname_entry, name_entry, pin_entry))
    exit_button.config(bg="#FFFF33")
    exit_button.place(x=165, y=240)

# добавления пользователя в банкомат и возврат к основному меню
def add_user_to_atm(window, surname_entry, name_entry, pin_entry):
    surname = surname_entry.get()
    name = name_entry.get()
    pin = pin_entry.get()

    if name == "" or surname == "" or pin == "":
        for item in window.winfo_children():
            item.destroy()

        error_label = tk.Label(window, text="Данные введены некорректно", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
        error_label.config(bg="#FFFF33")
        error_label.place(x=105, y=10)

        exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: create_main_window(window))
        exit_button.config(bg="#FFFF33")
        exit_button.place(x=47, y=280)
    else:
        username = name + " " + surname
        try:
            pincode = pin
            if fullmatch("[0-9]{4}", pincode) == None:
                raise NumericException("Некорректный формат pin-кода")
        except NumericException as e:
            for item in window.winfo_children():
                item.destroy()
            error_label = tk.Label(window, text=e.message, width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
            error_label.config(bg="#FFFF33")
            error_label.place(x=105, y=10)

            exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: create_main_window(window))
            exit_button.config(bg="#FFFF33")
            exit_button.place(x=47, y=300)
            return

        if atm.addAccount(username, pincode):
            for item in window.winfo_children():
                item.destroy()

            enter_label = tk.Label(window, text="Пользователь добавлен", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
            enter_label.config(bg="#FFFF33")
            enter_label.place(x=105, y=10)

            exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: create_main_window(window))
            exit_button.config(bg="#FFFF33")
            exit_button.place(x=47, y=280)
        else:
            for item in window.winfo_children():
                item.destroy()

            error_label = tk.Label(window, text="Пользователь уже существует", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
            error_label.config(bg="#FFFF33")
            error_label.place(x=105, y=10)

            exit_button = tk.Button(window, text="Вернуться в меню", width=65, height=5, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: create_main_window(window))
            exit_button.config(bg="#FFFF33")
            exit_button.place(x=47, y=280)

# окно добавления пользователя
def add_user(window):
    for item in window.winfo_children():
        item.destroy()

    surname_label = tk.Label(window, text="Введите фамилию пользователя:", width=35, height=3, font=("Arial", 10), borderwidth=2, relief="solid")
    surname_label.config(bg="#FFFF33")
    surname_label.place(x=35, y=10)

    surname_entry = tk.Entry(window, width=35)
    surname_entry.place(x=350, y=25)

    name_label = tk.Label(window, text="Введите имя пользователя:", width=35, height=3, font=("Arial", 10), borderwidth=2, relief="solid")
    name_label.config(bg="#FFFF33")
    name_label.place(x=35, y=60)

    name_entry = tk.Entry(window, width=35)
    name_entry.place(x=350, y=75)

    pin_label = tk.Label(window, text="Введите пин-код:", width=35, height=3, font=("Arial", 10), borderwidth=2, relief="solid")
    pin_label.config(bg="#FFFF33")
    pin_label.place(x=35, y=110)

    pin_entry = tk.Entry(window, width=35)
    pin_entry.place(x=350, y=130)

    exit_button = tk.Button(window, text="Добавить пользователя", width=35, height=8, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: add_user_to_atm(window, surname_entry, name_entry, pin_entry))
    exit_button.config(bg="#FFFF33")
    exit_button.place(x=165, y=240)

# окно действий инкассации
def incass(window):
    for item in window.winfo_children():
        item.destroy()

    greeting_label = tk.Label(window, text="Выберите действие", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
    greeting_label.config(bg="#FFFF33")
    greeting_label.place(x=105, y=10)

    enter_button = tk.Button(window, text="Узнать баланс", width=35, height=8, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: get_balance_incass(window))
    enter_button.config(bg="#FFFF33")
    enter_button.place(x=20, y=90)

    enter_button = tk.Button(window, text="Внести средства", width=35, height=8, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: increase_balance_incass(window))
    enter_button.config(bg="#FFFF33")
    enter_button.place(x=320, y=90)

    user_add_button = tk.Button(window, text="Снять средства", width=35, height=8, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: decrease_balance_incass(window))
    user_add_button.config(bg="#FFFF33")
    user_add_button.place(x=20, y=240)

    exit_button = tk.Button(window, text="Выход из системы", width=35, height=8, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: exit_not_user(window))
    exit_button.config(bg="#FFFF33")
    exit_button.place(x=320, y=240)

# завершение работы
def stop(window):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)

    file_path = os.path.join(base_path, 'data.json')
    atm.synchronize(file_path, OperationType.PUT)

    window.destroy()

# отрисовка основного рабочего окна
def create_main_window(window):
    for item in window.winfo_children():
        item.destroy()

    greeting_label = tk.Label(window, text="Выберите действие", width=40, height=3, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
    greeting_label.config(bg="#FFFF33")
    greeting_label.place(x=105, y=10)

    enter_button = tk.Button(window, text="Вход в систему", width=35, height=8, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: enter(window))
    enter_button.config(bg="#FFFF33")
    enter_button.place(x=20, y=90)

    user_add_button = tk.Button(window, text="Добавить пользователя", width=35, height=8, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: add_user(window))
    user_add_button.config(bg="#FFFF33")
    user_add_button.place(x=320, y=90)

    bank_button = tk.Button(window, text="Инкассация", width=35, height=8, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: incass(window))
    bank_button.config(bg="#FFFF33")
    bank_button.place(x=20, y=240)

    exit_button = tk.Button(window, text="Завершение работы", width=35, height=8, font=("Arial", 10), borderwidth=1, relief="raised", activebackground="#FFB266", command=lambda: stop(window))
    exit_button.config(bg="#FFFF33")
    exit_button.place(x=320, y=240)

def main():

    window = tk.Tk()
    window.title("Банкомат")
    window.geometry("630x400")
    window.config(bg="#FFFF33")

    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)

    file_path = os.path.join(base_path, 'data.json')

    global atm
    atm = ATMmachine()
    atm.synchronize(file_path, OperationType.GET)

    create_main_window(window)

    window.protocol("WM_DELETE_WINDOW", lambda: stop(window))
    window.mainloop()