import json
import tkinter as tk # импорт библиотеки
from tkinter import * # импорт всех методов
from tkinter import messagebox # явное импортирование
from tkinter import ttk, scrolledtext, Menu
from datetime import datetime
import os.path
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='phonebook.log',
    filemode='w', # при каждом новом запуске перезапись логов
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S ',
)
logging.info('Программа запущена')
# меню
def menu():
    global out_field_menu
    out_field_menu = Label(
    frame_2, 
    text = '0 - вызов меню\n'
        '1 - показать справочник\n'
        '2 - добавить новый контакт\n'
        '3 - удалить контакт\n'
        '4 - поиск контакта(нужно ввести имя целиком)\n'
        '5 - продвинутый поиск(по всем данным)\n'
        '6 - выгрузка данных\n'
        '7 - изменение данных\n'
        '8 - Копирование справочника в файл\n'
        '9 - выход из программы'
    )
    out_field_menu.grid(row=3, column=2) 

# вывод контактов
def printt_phone_book():
    with open('BD.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
        data = json.load(f)  # загнали все, что получилось в переменную

    t = data["phone_book"]  # ключ от главного словаря с данными контактов

    list_name = list(map(lambda x: x.get('name'), t))
    list_phone = list(map(lambda x: x.get('phone'), t))  # получаем номера телефонов
    list_surname = list(map(lambda x: x.get('surname'), t))  # получаем фамилии
    list_email = list(map(lambda x: x.get('E-mail'), t))  # получаем адреса почты
    global lbox
    
    lbox = Listbox(frame_2, width=70, height=10)
    lbox.pack(side=TOP)

    for i in range(len(list_name)):
        text = (f'ID {i + 1} {list_name[i]} {list_surname[i]} '
        f'Номер: {list_phone[i]} '
        f'Почта: {list_email[i]}')
        lbox.insert(0, text)



# =====================ОКНО ПРОГРАММЫ===================================================================
window = Tk()
window.title("Телефонная книга")
window.geometry('800x500')
# window.bind('<Return>', enter_)
# window.protocol("WM_DELETE_WINDOW", finish) закрытие программы вывод окна закрытия

# =================== ЗАГОТОВКИ РАСПОЛОЖЕНИЯ ВИДЖЕТОВ===================================================

# f_top = Frame(window)
# f_bot = Frame(window)
frame = Frame(
window, # указывает окно для размещения виджета frame для контроля расположения элементов
padx = 10, # отступы
pady = 0,
bg="yellow"
)
frame.pack(side=LEFT, anchor="nw") 

frame_3 = Frame(
window, # указывает окно для размещения виджета frame для контроля расположения элементов
padx = 5, # отступы
pady = 5,
bg="lightgreen"
)
frame_3.pack(side=TOP, anchor="w")

frame_2 = Frame(
window, # указывает окно для размещения виджета frame для контроля расположения элементов
padx = 5, # отступы
pady = 5,
bg="green"
)
frame_2.pack(side=TOP, anchor="nw")



# ==========================Поля ввода=================================================================
entry_name_label = Label(
    frame_3, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=0,
    text = "Введите Имя:",
    bg='lightgreen'
)
entry_name_label.grid(row=0, column=2) # grid метод позиционирования виджета в окне
entry_name_entry = Entry(
    frame_3, # заготовка с отступами
    bg="white"
)
entry_name_entry.grid(row=0, column=3)
enter_name = ttk.Button(
    frame_3,
    text= 'Ввод',
    command = menu,
    state=DISABLED # кнопка неактивна
)
enter_name.grid(row=0, column=4) # разместили кнопку в ячейке


entry_surname_label = Label(
    frame_3, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=0,
    text = "Введите Фамилию:",
    bg='lightgreen'
)
entry_surname_label.grid(row=1, column=2) # grid метод позиционирования виджета в окне
entry_surname_entry = Entry(
    frame_3, # заготовка с отступами
    bg="white"
)
entry_surname_entry.grid(row=1, column=3)
enter_surname = ttk.Button(
    frame_3,
    text= 'Ввод',
    command = menu,
    state=DISABLED
)
enter_surname.grid(row=1, column=4) # разместили кнопку в ячейке


entry_phone_label = Label(
    frame_3, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=0,
    text = "Введите номер:",
    bg='lightgreen'
)
entry_phone_label.grid(row=2, column=2) # grid метод позиционирования виджета в окне
entry_phone_entry = Entry(
    frame_3, # заготовка с отступами
    bg="white"
)
entry_phone_entry.grid(row=2, column=3)
enter_phone = ttk.Button(
    frame_3,
    text= 'Ввод',
    command = menu,
    state=DISABLED
)
enter_phone.grid(row=2, column=4) # разместили кнопку в ячейке


entry_email_label = Label(
    frame_3, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=0,
    text = "Введите почту:",
    bg='lightgreen'
)
entry_email_label.grid(row=3, column=2) # grid метод позиционирования виджета в окне
entry_email_entry = Entry(
    frame_3, # заготовка с отступами
    bg="white"
)
entry_email_entry.grid(row=3, column=3)
enter_email = ttk.Button(
    frame_3,
    text= 'Ввод',
    command = menu,
    state=DISABLED
)
enter_email.grid(row=3, column=4) # разместили кнопку в ячейке


# entry_id_label = Label(
#     frame_3, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
#     padx=0,
#     text = "Введите id:",
#     bg='lightgreen'
# )
# entry_id_label.grid(row=4, column=2) # grid метод позиционирования виджета в окне
# # entry_id_entry = Entry(
#     frame_3, # заготовка с отступами
#     bg="white"
# )
# entry_id_entry.grid(row=4, column=3)

# enter_id = ttk.Button(
#     frame_3,
#     text= 'Ввод',
#     command = menu,
#     state=["disabled"]
# )
# enter_id.grid(row=4, column=4) # разместили кнопку в ячейке

add_contact = ttk.Button(
    frame_3,
    text= 'Добавить контакт',
    command = menu,
    state=["disabled"]
)
add_contact.grid(row=5, column=3, )

# ===================================END===============================================================


# ==============================КНОПКИ МЕНЮ============================================================

def click_2():
    try:
        out_field_menu.destroy()
        menu()
    except:
        try:
            lbox.destroy()
            menu()
        except:
            menu()
entry_field_2 = Label(
    frame, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    pady=5,
    text = "Введите команду(0 - меню):",
    bg='green'
)
entry_field_2.grid(row=0, column=0) # grid метод позиционирования виджета в окне
button_menu = ttk.Button(
    entry_field_2,
    text= 'Меню',
    command = click_2
)
button_menu.grid(row=0, column=0)

def click_3():
    try:
        out_field_menu.destroy()
        lbox.destroy()
        printt_phone_book()
    except:
        try:
            out_field_menu.destroy()
            printt_phone_book()
        except: 
            printt_phone_book()
entry_field_3 = Label(
    frame, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=5,
    bg='green'
)
entry_field_3.grid(row=1, column=0) # grid метод позиционирования виджета в окне
button_print = ttk.Button(
    entry_field_3,
    text= 'Показать справочник',
    command = click_3
)
button_print.grid(row=1, column=0)

def click_4():
    # import new_contact as new_
    try:
        out_field_menu.destroy()
        click_button_new()
        # new_contactt()
    except:
        click_button_new()
        # new_contactt()
entry_field_4 = Label(
    frame, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=5,
    bg='green'
)
entry_field_4.grid(row=2, column=0) # grid метод позиционирования виджета в окне
button_add = ttk.Button(
    entry_field_4,
    text= 'Добавить новый контакт',
    command = click_4
)
button_add.grid(row=2, column=0)

def click_5():
    import delete_contact as del_
    try:
        out_field_menu.destroy()
        click_button_del()
        # button_add.config(text="Удалить контакт")
        # del_.deletee_contact()
    except:
        click_button_del()
        # del_.deletee_contact()
entry_field_5 = Label(
    frame, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=5,
    bg='green'
)
entry_field_5.grid(row=3, column=0) # grid метод позиционирования виджета в окне
button_del = ttk.Button(
    entry_field_5,
    text= 'Удалить контакт',
    command = click_5
)
button_del.grid(row=3, column=0)

def click_6():
    try:
        out_field_menu.destroy()
        click_button_search()
    except:
        click_button_search()
entry_field_6 = Label(
    frame, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=5,
    bg='green'
)
entry_field_6.grid(row=4, column=0) # grid метод позиционирования виджета в окне
button_search = ttk.Button(
    entry_field_6,
    text= 'Поиск контакта',
    command = click_6
)
button_search.grid(row=4, column=0)

def click_7():
    try:
        out_field_menu.destroy()
        menu()
    except:
        menu()
entry_field_7 = Label(
    frame, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=5,
    bg='green'
)
entry_field_7.grid(row=5, column=0) # grid метод позиционирования виджета в окне
button_subsearch = ttk.Button(
    entry_field_7,
    text= 'продвинутый поиск',
    command = click_7
)
button_subsearch.grid(row=5, column=0)

def click_8():
    try:
        out_field_menu.destroy()
        menu()
    except:
        menu()
entry_field_8 = Label(
    frame, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=5,
    bg='green'
)
entry_field_8.grid(row=6, column=0) # grid метод позиционирования виджета в окне
button_unload = ttk.Button(
    entry_field_8,
    text= 'Выгрузка данных',
    command = click_8
)
button_unload.grid(row=6, column=0)

def click_9():
    try:
        out_field_menu.destroy()
        menu()
    except:
        menu()
entry_field_9 = Label(
    frame, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=5,
    bg='green'
)
entry_field_9.grid(row=7, column=0) # grid метод позиционирования виджета в окне
button_change = ttk.Button(
    frame,
    text= 'Изменить контакт',
    command = click_9
)
button_change.grid(row=7, column=0)

def click_10():
    try:
        out_field_menu.destroy()
        menu()
    except:
        menu()
entry_field_10 = Label(
    frame, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=5,
    bg='green'
)
entry_field_10.grid(row=8, column=0) # grid метод позиционирования виджета в окне
button_copy = ttk.Button(
    frame,
    text= 'Копирование в файл',
    command = click_10
)
button_copy.grid(row=8, column=0)

def click_11():
    window.destroy()  # ручное закрытие окна и всего приложения
    messagebox.showinfo('ВЫХОД', f'Вы закрыли это божественное приложение !!!')
    logging.info('Закрытие приложения')
entry_field_11 = Label(
    frame, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=5,
    bg='green'
)
entry_field_11.grid(row=9, column=0) # grid метод позиционирования виджета в окне
button_exit = ttk.Button(
    entry_field_11,
    text= 'Выход из программы',
    command = click_11
)
button_exit.grid(row=9, column=0)
# ===================================END==============================================================





# ================================Функции=============================================================



# =============================Ввод данных============================================================
def name_input():
    global iname
    iname = entry_name_entry.get()
    enter_name.config(text="Записал")
    entry_name_entry.delete(0, END)
def surname_input():
    global isurname
    isurname = entry_surname_entry.get()
    enter_surname.config(text="Записал")
    entry_surname_entry.delete(0, END)
def iphone_input():
    global iphone
    iphone = entry_phone_entry.get()
    enter_phone.config(text="Записал")
    entry_phone_entry.delete(0, END)
def iemail_input():
    global iemail
    iemail = entry_email_entry.get()
    enter_email.config(text="Записал")
    entry_email_entry.delete(0, END)
    # entry.delete(0, END) # обнуление поля ввода
    # time.sleep(3)
    # enter_email.after(2000, enter_email.config(text="Ввод"))
# def iid_input():
#     global iid
#     iid = entry_id_entry.get()
# ===================================END===================================================================

# ================================Новый контакт========================================================

def click_button_new():
    logging.info('нажали кнопку добавить контакт')
    enter_name.config(state=tk.NORMAL, command=name_input)
    enter_surname.config(state=tk.NORMAL, command=surname_input)
    enter_phone.config(state=tk.NORMAL, command=iphone_input)
    enter_email.config(state=tk.NORMAL, command=iemail_input)
    add_contact.config(state=tk.NORMAL, command=new_contactt)
    # enter_name.config(text="Ввод")
    # enter_surname.config(text="Ввод")
    # enter_phone.config(text="Ввод")
    # enter_email.config(text="Ввод")


    # new_contactt()

def click_button_del():
    logging.info('нажали кнопку удалить контакт')
    add_contact.config(text="Удалить контакт")
    enter_name.config(state=tk.NORMAL, command=name_input)
    enter_surname.config(state=tk.NORMAL, command=surname_input)
    enter_phone.config(state=tk.DISABLED, command=iphone_input)
    enter_email.config(state=tk.DISABLED, command=iemail_input)
    add_contact.config(state=tk.NORMAL, command=deletee_contact)

def click_button_search():
    logging.info('нажали кнопку поиск контакта')
    add_contact.config(text="Поиск")
    entry_name_label.config(text="Введите данные")
    enter_name.config(state=tk.NORMAL, command=name_input)
    enter_surname.config(state=tk.DISABLED, command=surname_input)
    enter_phone.config(state=tk.DISABLED, command=iphone_input)
    enter_email.config(state=tk.DISABLED, command=iemail_input)
    add_contact.config(state=tk.NORMAL, command=substring_search)


def new_contactt():
    enter_name.config(text="Ввод")
    enter_surname.config(text="Ввод")
    enter_phone.config(text="Ввод")
    enter_email.config(text="Ввод")
    logging.info('Зашли в новый контакт')

    # enter_id.config(state=tk.NORMAL, command=iid_input)


    def added_contact():
        logging.info('Пытаемся добавить контакт')
        # new_data = {
        #     'id': id,
        #     'name': iname,
        #     "surname": isurname,
        #     'phone': iphone,
        #     "E-mail": iemail}
        data['phone_book'].append(new_data)
        print(f'\033[1mКонтакт {iname} успешно добавлен!!!!\033[0m')
        messagebox.showinfo('Добавление контакта', f'Контакт успешно добавлен')
        with open('BD.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)
            logging.info('Added contact succesfull')

    # add_contact.config(command=added_contact)

    global id

    if os.path.exists("BD.json"):

        with open('BD.json', encoding='utf8') as openfile:
            data = json.load(openfile)
            t = data["phone_book"]
            if len(t) > 0:
                logging.info('телефонная книга имеется')

        
                global result_id
                result_name = list(map(lambda x : x.get('name'), t))
                result_surname = list(map(lambda x : x.get('surname'), t))
                result_phone = list(map(lambda x : x.get('phone'), t))
                result_email = list(map(lambda x : x.get('E-mail'), t))
                result_id = list(map(lambda x : x.get('id'), t))
                count_fullname = 0
                count_phone = 0
                count_id = 0
                count_email = 0
                id = max(set(result_id)) + 1
            


                if len(t) > 1:
                    logging.info('контактов больше 1')
                    new_data = {
                    'id': id,
                    'name': iname,
                    "surname": isurname,
                    'phone': iphone,
                    "E-mail": iemail}
                    num = [iname, isurname]
                    for i in range(len(result_name)): # name uniqueness check, если имя уже есть, предложит изменить
                        for j in range(0, len(result_surname)):
                            numb = [result_name[i], result_surname[j]]                    
                            if numb == num:
                                count_fullname += 1

                elif len(t) == 1:
                    logging.info('есть 1 контакт')
                    new_data = {
                    'id': id,
                    'name': iname,
                    "surname": isurname,
                    'phone': iphone,
                    "E-mail": iemail}
                    num = [iname, isurname]
                    for i in result_name[0]:
                        for j in result_surname[0]:
                            numb_ = [result_name[0], result_surname[0]]
                            if num == numb_:
                                count_fullname += 1

                for i in result_phone:
                    if iphone == i:
                        count_phone += 1
        
                for i in result_id:
                    if id == i:
                        count_id += 1

                for i in result_email:
                    if id == i:
                        count_email += 1

                if count_fullname > 0:
                    logging.info('The name is already there')

                    messagebox.showinfo('ОШИБКА ФИО', f'такое фио уже есть, добавьте новый контакт(,\nлибо измените имеющийся в соответствующем меню')
                else:
                    if count_phone > 0:
                        logging.info('the phone number is already there')
                        messagebox.showinfo('НОМЕР', f'Такой номер уже записан')
                    else:
                        if count_id == 0: # проверка на уникальность id
                            added_contact()
                        else:
                            added_contact()

            if len(t) == 0:
                logging.info('нету контактов')
                with open('BD.json', encoding='utf8') as openfile:
                    data = json.load(openfile)
                    logging.info('Open file')
                    # global new_data
                new_data = {
                    'id': 1,
                    'name': iname,
                    "surname": isurname,
                    'phone': iphone,
                    "E-mail": iemail}
                if len(data["phone_book"]) <= 1:
                    logging.info('Идем в добавление контакта')
                    added_contact()
                    logging.info('Added contact succesful')
                    messagebox.showinfo('Контакт успешно добавлен')

    else:         
        with open('BD.json', 'w', encoding='utf-8') as fh:
            BD = {"phone_book": []}
            fh.write(json.dumps(BD,
                                ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
            logging.info('Create phone book')
            print('\033[1mТелефонная книга создана!\033[0m')

        name = input("\033[1mВведите имя:\033[0m ")
        surname = input("\033[1mВведите Фамилию:\033[0m ")
        phone = input("\033[1mВведите номер:\033[0m ")
        email = input("\033[1mВведите почту:\033[0m")

        with open('BD.json', encoding='utf8') as openfile:
            data = json.load(openfile)
            logging.info('Open file')
            new_data = {
                'id': id,
                'name': name,
                "surname": surname,
                'phone': phone,
                "E-mail": email}
            if len(data["phone_book"]) <= 1:
                added_contact()
                logging.info('Added contact succesful')
                messagebox.showinfo('Контакт успешно добавлен')


# изменение контакта
def change_details():
    # name_search = input("\033[1mВведите имя контакта, который хотите изменить:\033[0m ")
    # sur_name_search = input("\033[1mВведите имя контакта, который хотите изменить:\033[0m ")
    with open('BD.json', encoding='utf8') as openfile:
        data = json.load(openfile)
        # lg.logging.info('Open file')

    for i in data["phone_book"]:
        if i["name"] == name_search and i["surname"] == sur_name_search:
            print(f'name: {i["name"]} {i["surname"]}')
            
            print(f'phone: {i["phone"]}')
            print(f'mail: {i["E-mail"]}')
            
            number = i["phone"]
            email = i["E-mail"]
            surname = i["surname"]
            print("\033[1mкакие данный хотите изменить?\033[0m(ФИО, номер, почту): ")
            messagebox.showinfo('какие данный хотите изменить?(ФИО, номер, почту): ')
            answer = int(input("\033[1m1 - ФИО, 2 - номер, почту - 3, 0 - выход в меню:\033[0m "))
            if answer == 0:
                        print("\033[1mвыходим в меню\033[0m")
            if answer == 1:
                answer_name = int(input("1 - имя, 2 - фамилию: "))
                if answer_name == 1:
                    change_name = input(f"\033[1mМеняем имя {name_search} на:\033[0m ")
                    i["name"] = change_name
                    # lg.logging.info('Change name')
                    print("Имя изменено")
                elif answer_name == 2:
                    change_name = input(f"Меняем фамилию {surname} на: ")
                    i["surname"] = change_name
                    # lg.logging.info('Change surname')
                    print("Фамилия изменена")
            elif answer == 2:
                change_phone = input(f"Меняем номер {number} на: ")
                i["phone"] = change_phone
                # lg.logging.info('Change phone number')
                print(f'Теперь номер контакта {i["name"]}: {i["phone"]}')
            elif answer == 3:
                change_email = input(f"Меняем почту контакта {name_search} {surname} с почтой {email} на: ")
                i["E-mail"] = change_email
                # lg.logging.info('Change E-mail')
        else:
            continue
            # i = i + 1
    with open('BD.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)
        # lg.logging.info('Data recording')

# Удаление контакта

def deletee_contact():

    with open('BD.json', encoding='utf8') as openfile:  # Открываем файл
        # Получае все данные из файла (вообще все, да)
        data = json.load(openfile)
        logging.info('Open file')

    index = 0
    found_index = 0
    # items = data.values()
    for i in data["phone_book"]:
        if i["name"] == iname and i["surname"] == isurname:
            print(f'{i["name"]} {i["surname"]}')
            data["phone_book"].pop(index)
            found_index += 1
        else:
            index += 1
    if found_index == 0:
        messagebox.showinfo('Удаление контакта', 'Контакт не найден')
        logging.info('Контакт не найден!')
        add_contact.config(text="Добавить контакт")
    with open('BD.json', 'w', encoding='utf8') as outfile:  # Открываем файл для записи
        # Добавляем данные (все, что было ДО добавления данных + добавленные
        # данные)
        json.dump(data, outfile, ensure_ascii=False, indent=2)
        logging.info('Удалили контакт')
        logging.info('записали данные')
        add_contact.config(text="Добавить контакт")
    messagebox.showinfo('Удаление Контакта', f'Контакт успешно удален')

# Продвинутый поиск
def substring_search():
        logging.info('substring search contact')
        with open('BD.json', encoding='utf8') as openfile:
            data = json.load(openfile)
            t = data["phone_book"]

        # name_search = input("\033[1mВведите данные контакта:\033[0m ")
        rname = str.title(iname)
        result_name = list(map(lambda x : x.get('name'), t))
        result_surname = list(map(lambda x : x.get('surname'), t))
        result_phone = list(map(lambda x : x.get('phone'), t))
        result_email = list(map(lambda x : x.get('E-mail'), t))
        result_id = list(map(lambda x : x.get('id'), t))
        # names = list(result_name)
        # surnames = list(result_surname)
        
        names_list_index = []
        count = 0

        for i in result_name:

            rn = result_name[count]
            rsn = result_surname[count]
            sn = result_surname[count]
            nrp = result_phone[count]
            nre = (result_email[count])
            # name_search_l = name_search.lower()
            nri = result_id[count]

            if rname in rn or rname in sn:
                names_list_index.append(count)
                print(f'\033[1mВозможно вы искали:\033[0m {rn} {rsn}, \033[1mID\033[0m - \033[32m{nri}\033[0m')
                count += 1
                logging.info('contact found')
                entry_name_label.config(text="Введите имя")
            elif rname in nrp or rname.lower() in nre.lower():
                names_list_index.append(count)
                print(f'\033[1mВозможно вы искали:\033[0m {rn} {rsn}, \033[1mmail\033[0m: {nre}, \033[1mID\033[0m - \033[32m{nri}\033[0m')
                count += 1
                logging.info('contact found')
                entry_name_label.config(text="Введите имя")
            else:
                count += 1

        if len(names_list_index) == 0:
            logging.info('No such contact')
            print("\033[1mТакого контакта нет!!!\033[0m")
            entry_name_label.config(text="Введите имя")
        elif len(names_list_index) > 0:
            id_search = int(input("\033[1mВведите\033[0m \033[32mID\033[0m \033[1mконтакта для вывода подробной информации о нём,\033[0m \033[32m0\033[0m - \033[1mвыход в меню:\033[0m "))
            found = 0
            if id_search == 0:
                print("\033[1mвыходим в меню\033[0m")
                logging.info('menu exit')
                found = 1
            for i in t:
                if i["id"] == id_search:
                    print(f'\033[32mname: \033[0m{i["name"]} {i["surname"]} \n' +
                    f'\033[32mphone: \033[0m {i["phone"]} \n' +
                    f'\033[32mE-mail: \033[0m {i["E-mail"]}')
                    logging.info('full output')
                    found += 1
                    return found
            if found == 0:
                print(f"\033[1mКонтакт с id\033[0m - \033[32m{id_search}\033[0m \033[1mотсутствует в телефонной книге!\033[0m]")
                logging.info('contact not found')
                entry_name_label.config(text="Введите имя")

window.mainloop() # функция запуска цикла событий=====================================================