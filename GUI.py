import json
import tkinter as tk # импорт библиотеки
from tkinter import * # импорт всех методов
from tkinter import messagebox # явное импортирование
from tkinter import ttk, scrolledtext, Menu
from datetime import datetime
import os.path


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


entry_name = Label(
    frame_3, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=0,
    text = "Введите Имя:",
    bg='lightgreen'
)
entry_name.grid(row=0, column=2) # grid метод позиционирования виджета в окне
entry_name = Entry(
    frame_3, # заготовка с отступами
    bg="white"
)
entry_name.grid(row=0, column=3)
enter_name = ttk.Button(
    frame_3,
    text= 'Ввод',
    command = menu
)
enter_name.grid(row=0, column=4) # разместили кнопку в ячейке


entry_surname = Label(
    frame_3, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=0,
    text = "Введите Фамилию:",
    bg='lightgreen'
)
entry_surname.grid(row=1, column=2) # grid метод позиционирования виджета в окне
entry_surname = Entry(
    frame_3, # заготовка с отступами
    bg="white"
)
entry_surname.grid(row=1, column=3)
enter_name = ttk.Button(
    frame_3,
    text= 'Ввод',
    command = menu
)
enter_name.grid(row=1, column=4) # разместили кнопку в ячейке


entry_phone = Label(
    frame_3, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=0,
    text = "Введите номер:",
    bg='lightgreen'
)
entry_phone.grid(row=2, column=2) # grid метод позиционирования виджета в окне
entry_phone = Entry(
    frame_3, # заготовка с отступами
    bg="white"
)
entry_phone.grid(row=2, column=3)
enter_name = ttk.Button(
    frame_3,
    text= 'Ввод',
    command = menu
)
enter_name.grid(row=2, column=4) # разместили кнопку в ячейке


entry_email = Label(
    frame_3, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    padx=0,
    text = "Введите почту:",
    bg='lightgreen'
)
entry_email.grid(row=3, column=2) # grid метод позиционирования виджета в окне
entry_email = Entry(
    frame_3, # заготовка с отступами
    bg="white"
)
entry_email.grid(row=3, column=3)
enter_name = ttk.Button(
    frame_3,
    text= 'Ввод',
    command = menu
)
enter_name.grid(row=3, column=4) # разместили кнопку в ячейке




# # КНОПКИ МЕНЮ

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
        new_contactt()
    except:
        new_contactt()
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
        del_.deletee_contact()
    except:
        del_.deletee_contact()
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
        menu()
    except:
        menu()
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
    try:
        out_field_menu.destroy()
        menu()
    except:
        menu()
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



window.mainloop() # функция запуска цикла событий


def new_contactt():
    def added_contact():
        data['phone_book'].append(new_data)
        print(f'\033[1mКонтакт {name} успешно добавлен!!!!\033[0m')
        with open('BD.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)
            # lg.logging.info('Added contact succesfull')

    def answer():
        if answer == 1:
            new_contactt()
        elif answer == 2:
            change_details()

    global id

    if os.path.exists("BD.json"):

        with open('BD.json', encoding='utf8') as openfile:
            data = json.load(openfile)
            t = data["phone_book"]
            if len(t) > 0:
                name = input("\033[1mВведите имя:\033[0m ")
                surname = input("\033[1mВведите Фамилию:\033[0m ")
                phone = input("\033[1mВведите номер:\033[0m ")
                email = input("\033[1mВведите почту:\033[0m ")

        
                
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
                new_data = {'id': id, 'name': name, "surname": surname, 'phone': phone, "E-mail": email} #создали переменную, включающую в себя данные, которые мы хотим добавить в уже имеющийся файл

                # pop = list(result_name)
                # prop = list(result_surname)
                num = [name, surname]

                if len(t) > 1:
                    for i in range(len(result_name)): # name uniqueness check, если имя уже есть, предложит изменить
                        for j in range(0, len(result_surname)):
                            numb = [result_name[i], result_surname[j]]                    
                            if numb == num:
                                count_fullname += 1

                elif len(t) == 1:
                    for i in result_name[0]:
                        for j in result_surname[0]:
                            numb_ = [result_name[0], result_surname[0]]
                            if num == numb_:
                                count_fullname += 1

                for i in result_phone:
                    if phone == i:
                        count_phone += 1
        
                for i in result_id:
                    if id == i:
                        count_id += 1

                for i in result_email:
                    if id == i:
                        count_email += 1

                if count_fullname > 0:
                    # lg.logging.info('The name is already there')
                    print("такое имя уже есть, добавьте новый контакт(,\nлибо измените имеющийся в соответствующем меню")

                    answer_user = int(input("\033[1m\033[32m1\033[0m - добавить, \033[32m2\033[0m - изменить, \033[32m3\033[0m - в меню\033[0m: "))
                    if answer_user == 1:
                        new_contactt()
                    elif answer_user == 2:
                        change_details()
                    elif answer_user == 0:
                        print("\033[1mвыходим в меню\033[0m")
                    else: 
                        print("\033[1mТакого пункта нет, верну вас в меню\033[0m")
                else:
                    if count_phone > 0:
                        # lg.logging.info('the phone number is already there')
                        print("\033[1mТакой номер телефона уже записан, добавьте новый контакт,\nлибо измените имеющийся в соответствующем меню\033[0m")
                        answer_user = int(input("\033[1m\033[32m1\033[0m - добавить, \033[32m2\033[0m - изменить, \033[32m3\033[0m - в меню\033[0m: "))
                        if answer_user == 1:
                            new_contactt()
                        elif answer_user == 2:
                            change_details()
                        elif answer_user == 3:
                            print("выходим в меню")
                            # lg.logging.info('menu exit')
                        else: 
                            print("такого пункта нет, верну вас в меню")
                            # lg.logging.info('menu exit')
                    else:
                        if count_id == 0: # проверка на уникальность id
                            added_contact()
                        else:
                            added_contact("Выходим в меню")
            if len(t) == 0:
                name = input("Введите имя: ")
                surname = input("Введите Фамилию: ")
                phone = input("Введите номер: ")
                email = input("Введите почту:")
                with open('BD.json', encoding='utf8') as openfile:
                    data = json.load(openfile)
                # lg.logging.info('Open file')
                new_data = {
                    'id': id,
                    'name': name,
                    "surname": surname,
                    'phone': phone,
                    "E-mail": email}
                if len(data["phone_book"]) <= 1:
                    added_contact()
                    # lg.logging.info('Added contact succesful')

    else:         
        with open('BD.json', 'w', encoding='utf-8') as fh:
            BD = {"phone_book": []}
            fh.write(json.dumps(BD,
                                ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
            # lg.logging.info('Create phone book')
            print('\033[1mТелефонная книга создана!\033[0m')

        name = input("\033[1mВведите имя:\033[0m ")
        surname = input("\033[1mВведите Фамилию:\033[0m ")
        phone = input("\033[1mВведите номер:\033[0m ")
        email = input("\033[1mВведите почту:\033[0m")

        with open('BD.json', encoding='utf8') as openfile:
            data = json.load(openfile)
            # lg.logging.info('Open file')

            new_data = {
                'id': id,
                'name': name,
                "surname": surname,
                'phone': phone,
                "E-mail": email}
            
            if len(data["phone_book"]) <= 1:
                added_contact()
                # lg.logging.info('Added contact succesful')



def change_details():
    name_search = input("\033[1mВведите имя контакта, который хотите изменить:\033[0m ")
    sur_name_search = input("\033[1mВведите имя контакта, который хотите изменить:\033[0m ")
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