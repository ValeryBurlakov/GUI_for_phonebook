import json
import tkinter as tk # импорт библиотеки
from tkinter import DISABLED, END, LEFT, TOP # явное импортирование
from tkinter import  Entry, Frame, Label, Listbox, Tk, messagebox 
from tkinter import ttk, scrolledtext, Menu
import os.path
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='phonebook.log',
    filemode='w', # при каждом новом запуске перезапись логов
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S ',
)
logging.info('Приложение запущено')

# вывод контактов
def printt_phone_book():
    enter_name.config(state=tk.DISABLED)
    enter_surname.config(state=tk.DISABLED)
    enter_phone.config(state=tk.DISABLED,)
    enter_email.config(state=tk.DISABLED)
    add_contact.config(state=tk.DISABLED)
    with open('BD.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
        data = json.load(f)  # загнали все, что получилось в переменную

    t = data["phone_book"]  # ключ от главного словаря с данными контактов
    list_id = list(map(lambda x: x.get('id'), t))
    list_name = list(map(lambda x: x.get('name'), t))
    list_phone = list(map(lambda x: x.get('phone'), t))  # получаем номера телефонов
    list_surname = list(map(lambda x: x.get('surname'), t))  # получаем фамилии
    list_email = list(map(lambda x: x.get('E-mail'), t))  # получаем адреса почты
    global lbox

    set_id = list(set(list_id)) # сделали упорядоченное множество, записали это списком, 
    #                             и теперь айдишники будут выводиться по порядку
    #                             зачем это надо не знаю
    
    lbox = Listbox(frame_2, width=76, height=10, bg='#F0FFFF')
    lbox.pack(side=TOP)

    # реагирование на выбор контакта____в будущем
    # def selected_item():
    # # Traverse the tuple returned by
    # # curselection method and print
    # # corresponding value(s) in the listbox
    #     for i in lbox.curselection():
    #         print(lbox.get(i))
    # selected_item

    for i in range(len(list_name)):
        text = (f'ID {set_id[i]} {list_name[i]} {list_surname[i]} '
        f'Номер: {list_phone[i]} '
        f'Почта: {list_email[i]}')
        lbox.insert(0, text)

    add_contact.config(text="операция")

# =====================ОКНО ПРОГРАММЫ===================================================================
window = Tk()
window.title("Телефонная книга")
window.geometry('600x400')
window.resizable(False, False) # фиксированный размер окна
ttk.Style().configure("TButton", foreground="black", padding=3, background="#D3D3D3") # стиль всех кнопок
for c in range(2): window.columnconfigure(index=c, weight=1)
for r in range(2): window.rowconfigure(index=r, weight=1)

# window.bind('<Return>', enter_)
# window.protocol("WM_DELETE_WINDOW", finish) закрытие программы вывод окна закрытия

# =================== ЗАГОТОВКИ РАСПОЛОЖЕНИЯ ВИДЖЕТОВ===================================================

frame = Frame(
window, # указывает окно для размещения виджета frame для контроля расположения элементов
padx = 5, # отступы
pady = 5,
bg="#F0FFFF"
)
frame.place(x=0, y=0, width=200, height=216) 

frame_3 = Frame(
window, # указывает окно для размещения виджета frame для контроля расположения элементов
padx = 6, # отступы
pady = 10,
bg="#F0FFFF"
)
frame_3.place(x=200, y=0, width=400, height=216)

frame_2 = Frame(
window, # указывает окно для размещения виджета frame для контроля расположения элементов
padx = 0, # отступы
pady = 0,
bg="#F0FFFF"
)
frame_2.place(x=0, y=216, width=600, height=184, )

# ==========================Поля ввода=================================================================
entry_name_label = Label(
    frame_3, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=0,
    text = "Введите Имя:",
    bg='#F0FFFF'
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
    state=DISABLED # кнопка неактивна
)
enter_name.grid(row=0, column=4) # разместили кнопку в ячейке


entry_surname_label = Label(
    frame_3, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=0,
    text = "Введите Фамилию:",
    bg='#F0FFFF'
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
    state=DISABLED
)
enter_surname.grid(row=1, column=4) # разместили кнопку в ячейке


entry_phone_label = Label(
    frame_3, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=0,
    text = "Введите номер:",
    bg='#F0FFFF'
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
    state=DISABLED
)
enter_phone.grid(row=2, column=4) # разместили кнопку в ячейке


entry_email_label = Label(
    frame_3, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=0,
    text = "Введите почту:",
    bg='#F0FFFF'
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
    state=DISABLED,
)
enter_email.grid(row=3, column=4) # разместили кнопку в ячейке

add_contact = ttk.Button(
    frame_3,
    text= 'Операция',
    state=["disabled"]
)
add_contact.grid(row=5, column=3, )

# ===================================END===============================================================

printt_phone_book()
# ==============================КНОПКИ МЕНЮ============================================================

def click_3():
    try:
        try:
            logging.info('удаление аут и лбокс')
            # out_field_menu.destroy()
            lbox.destroy()
            lbox2.destroy()
            printt_phone_book()
            
        except:
            try:
                try:
                    logging.info('удаление лбокс')
                    lbox.destroy()
                    lbox2.destroy()
                    printt_phone_book()
                except:
                    logging.info('удаление лбокс2')
                    lbox2.destroy()
                    printt_phone_book()
                
            except:
                logging.info('удаление аут')
                # out_field_menu.destroy()
                printt_phone_book()
                
    except:
        logging.info('вывод книги')
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
    try:
        # out_field_menu.destroy()
        click_button_new()
    except:
        click_button_new()
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
    try:
        # out_field_menu.destroy()
        click_button_del()
    except:
        click_button_del()
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
        try:
            # out_field_menu.destroy()
            lbox.destroy()
            click_button_search()
        except:
            try:
                lbox.destroy()
                click_button_search()
            except:
                # out_field_menu.destroy()
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

def click_9():
    try:
        change_details()
    except:
        change_details
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
        lbox2.destroy()
        lbox.destroy()
        click_button_copy()
    except:
        try:
            try:
                lbox2.destroy()
                click_button_copy()
            except:
                lbox.destroy()
                click_button_copy()
        except:
            click_button_copy()
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
    add_contact.config(text="Добавить контакт")
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

def click_button_copy():
    logging.info('нажали кнопку поиск контакта')
    add_contact.config(text="копировать")
    entry_name_label.config(text="имя новой папки")
    enter_name.config(state=tk.NORMAL, command=name_input)
    enter_surname.config(state=tk.DISABLED, command=surname_input)
    enter_phone.config(state=tk.DISABLED, command=iphone_input)
    enter_email.config(state=tk.DISABLED, command=iemail_input)
    add_contact.config(state=tk.NORMAL, command=copy)


def new_contactt():
    enter_name.config(text="Ввод")
    enter_surname.config(text="Ввод")
    enter_phone.config(text="Ввод")
    enter_email.config(text="Ввод")
    logging.info('Зашли в новый контакт')

    # enter_id.config(state=tk.NORMAL, command=iid_input)
    def added_contact():
        logging.info('Пытаемся добавить контакт')
        data['phone_book'].append(new_data)
        messagebox.showinfo('Добавление контакта', f'Контакт успешно добавлен')
        with open('BD.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)
            logging.info('Added contact succesfull')

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
                # id = max(set(result_id)) + 1
                # теперь все id будут заполняться корректно
                id2 = 1
                for i in result_id:
                    if (id2 not in result_id):
                            id = id2
                    else:
                        id2 += 1

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
                    add_contact.config(text="операция")
                    messagebox.showinfo('Контакт успешно добавлен')

    else:         
        with open('BD.json', 'w', encoding='utf-8') as fh:
            BD = {"phone_book": []}
            fh.write(json.dumps(BD,
                                ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
            logging.info('Create phone book')
            # print('\033[1mТелефонная книга создана!\033[0m')
            messagebox.showinfo('Телефонная книга создана')

        with open('BD.json', encoding='utf8') as openfile:
            data = json.load(openfile)
            logging.info('Open file')
            new_data = {
                'id': id,
                'name': iname,
                "surname": isurname,
                'phone': iphone,
                "E-mail": iemail}
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
        if i["name"] == iname and i["surname"] == isurname:
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
                    change_name = input(f"\033[1mМеняем имя {iname} на:\033[0m ")
                    i["name"] = change_name
                    logging.info('Change name')
                    print("Имя изменено")
                elif answer_name == 2:
                    change_name = input(f"Меняем фамилию {surname} на: ")
                    i["surname"] = change_name
                    logging.info('Change surname')
                    print("Фамилия изменена")
            elif answer == 2:
                change_phone = input(f"Меняем номер {number} на: ")
                i["phone"] = change_phone
                logging.info('Change phone number')
                print(f'Теперь номер контакта {i["name"]}: {i["phone"]}')
            elif answer == 3:
                change_email = input(f"Меняем почту контакта {iname} {isurname} с почтой {email} на: ")
                i["E-mail"] = change_email
                logging.info('Change E-mail')
        else:
            continue
            # i = i + 1
    with open('BD.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)
        logging.info('Data recording')

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
            messagebox.showinfo('Удаление Контакта', f'Контакт успешно удален')
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
        

# Продвинутый поиск
def substring_search():

    # нужно создать выпадающий список контактов при вводе данных
        logging.info('substring search contact')
        with open('BD.json', encoding='utf8') as openfile:
            data = json.load(openfile)
            t = data["phone_book"]

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
        global lbox2
        lbox2 = Listbox(frame_2, width=70, height=10, bg='#F0FFFF')
        lbox2.pack(side=TOP)
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
                text = (f'ФИО: {rn} {rsn} Номер: {nrp} Почта: {nre}')
                lbox2.insert(0, text)
                count += 1
                logging.info('contact found')
                entry_name_label.config(text="Введите имя")
            elif rname in nrp or rname.lower() in nre.lower():
                names_list_index.append(count)
                text = (f'ФИО: {rn} {rsn} Номер: {nrp} Почта: {nre}')
                lbox2.insert(0, text)
                count += 1
                logging.info('contact found')
                entry_name_label.config(text="Введите имя")
            else:
                count += 1

        if len(names_list_index) == 0:
            logging.info('No such contact')
            messagebox.showinfo('Поиск контакта', f'Нет результатов по запросу <<{iname}>>')
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
                # print(f"\033[1mКонтакт с id\033[0m - \033[32m{id_search}\033[0m \033[1mотсутствует в телефонной книге!\033[0m]")
                messagebox.showinfo('Поиск контакта', f'<<{iname}>> Отсутствует в телефонной книге')
                logging.info('contact not found')
                entry_name_label.config(text="Введите имя")


def copy():
    logging.info('Copying')
    with open('BD.json', 'r') as f:  # открыли файл с данными
        text = json.load(f)  # загнали все, что получилось в переменную
        # print(text) #вывели результат на экран
        logging.info('Read DATABASE')
        n = iname + '.json'
        n = str(n)
        print(n)
        if os.path.exists(n):
            messagebox.showinfo('Копирование книги', f'Файл {iname} уже существует')
        with open(n, 'w', encoding='utf-8') as openfile:  # Открываем файл
                    # Получаем все данные из файла (вообще все, да)
                    json.dump(text, openfile, ensure_ascii=False, indent=2)
                    messagebox.showinfo('Копирование книги', f'Справочник сохранен в папку {iname}')
                    add_contact.config(text="операция")
                    logging.info('Copying succesfful')

window.mainloop() # функция запуска цикла событий=====================================================