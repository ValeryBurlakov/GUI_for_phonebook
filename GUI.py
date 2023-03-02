import json
import tkinter as tk # импорт библиотеки
from tkinter import * # импорт всех методов
from tkinter import messagebox # явное импортирование
from tkinter import ttk, scrolledtext, Menu
from datetime import datetime
import print_phone_book as ppb

# def finish():
#     window.destroy()  # ручное закрытие окна и всего приложения
#     print("Закрытие приложения")
#     messagebox.showinfo('answer-pythonguides', f'Ты закрыл это божественное приложение!!!')

def enter_(event):
    # messagebox.showinfo('answer-pythonguides', f'Вы ввели enter')
    main_()


def main_():
    global answer
    answer = user_input.get() # получение ответа из виджета user input
    # dt = datetime.now()
    # messagebox.showinfo('Ебучая книга', f'Доброго времени суток! {dt.strftime("%A, %d %B %Y %I:%M%p")}')
    if answer == '0':
                # messagebox.showinfo('answer-pythonguides', f'Ты гандон ввёл 0')
                menu()
    elif answer == '1':
        
        out_field_menu.destroy()
        printt_phone_book()
        out_field_print = Label(
        frame_3, 
        text = f'Вывод контактов'
        )
        out_field_print.grid(row=0, column=0)
        messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Вывод контактов в консоль')
    elif answer == '2':
        messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Ты ввёл 2')
    elif answer == '3':
        messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Ты ввёл 3')
    elif answer == '4':
        messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Ты ввёл 4')
    elif answer == '5':
        messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Ты ввёл 5')
    elif answer == '6':
        messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Ты ввёл 6')
    elif answer == '7':
        messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Ты ввёл 7')
    elif answer == '8':
        out_field_8 = Label(
        frame_2, 
        text = f'Ты гандон ввёл 8'
        )
        out_field_8.grid(row=0, column=0)
        # messagebox.showinfo('answer-pythonguides', f'Ты гандон ввёл 8')
    elif answer == '9':
        print("получай в консоли exit")
    else:
         menu()

def menu():
    global out_field_menu
    out_field_menu = Label(
    frame, 
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
    out_field_menu.grid(row=5, column=0) 
    # out_field_menu.destroy()

def printt_phone_book():

    with open('BD.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
        data = json.load(f)  # загнали все, что получилось в переменную
        # pprint(text) #вывели результат на экран
        # lg.logging.info('Read DATABASE')

    t = data["phone_book"]  # ключ от главного словаря с данными контактов
    # обращаемся к словарю получаем список имён
    list_name = list(map(lambda x: x.get('name'), t))
    list_phone = list(map(lambda x: x.get('phone'), t))  # получаем номера телефонов
    list_surname = list(map(lambda x: x.get('surname'), t))  # получаем фамилии
    list_email = list(map(lambda x: x.get('E-mail'), t))  # получаем адреса почты
    # print(t)
    lbox = Listbox(width=70, height=10)
    lbox.pack()
    for i in range(len(list_name)):
        text = (f'ID {i + 1} {list_name[i]} {list_surname[i]} '
        f'Номер: {list_phone[i]} '
        f'Почта: {list_email[i]}')
        lbox.insert(0, text)



global window
window = Tk()
window.title("Телефонная книга")
window.geometry('600x400')
window.bind('<Return>', enter_)
# window.protocol("WM_DELETE_WINDOW", finish) закрытие программы вывод окна закрытия

# =================== ЗАГОТОВКИ РАСПОЛОЖЕНИЯ ВИДЖЕТОВ==============================
frame = Frame(
window, # указывает окно для размещения виджета frame для контроля расположения элементов
padx = 5, # отступы
pady = 5
)
frame.pack(anchor="n") 

frame_2 = Frame(
window, # указывает окно для размещения виджета frame для контроля расположения элементов
padx = 0, # отступы
pady = 0
)
frame_2.pack(anchor="nw")

frame_3 = Frame(
window, # указывает окно для размещения виджета frame для контроля расположения элементов
padx = 0, # отступы
pady = 0
)
frame_3.pack(anchor="n") 

# позиционируем виджет в окне в центре
# n: положение вверху по центру
# e: положение в правой части контейнера по центру
# s: положение внизу по центру
# w: положение в левой части контейнера по центру
# nw: положение в верхнем левом углу
# ne: положение в верхнем правом углу
# se: положение в нижнем правом углу
# sw: положение в нижнем левом углу
# center: положение центру

# ===================================================

# добавили виджет label для поля ввода
entry_field = Label(
    frame, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
    text = "Введите ваше имя: "
)
entry_field.grid(row=0, column=0) # grid метод позиционирования виджета в окне



# ВИДЖЕТ ВВОДА
user_input = Entry(
    frame, # заготовка с отступами
)
user_input.grid(row=1, column=0, pady=1)

# кнопка

button_start = ttk.Button(
    frame,
    text= 'Enter',
    command = main_
)
button_start.grid(row=2, column=0) # разместили кнопку в ячейке





window.mainloop() # функция запуска цикла событий

# Activate: окно становится активным.
# Deactivate: окно становится неактивным.
# MouseWheel: прокрутка колеса мыши.
# KeyPress: нажатие клавиши на клавиатуре.
# KeyRelease: освобождение нажатой клавиши
# ButtonPress: нажатие кнопки мыши.
# ButtonRelease: освобождение кнопки мыши.
# Motion: движение мыши.
# Configure: изменение размера и положения виджета
# Destroy: удаление виджета
# FocusIn: получение фокуса
# FocusOut: потеря фокуса.
# Enter: указатель мыши вошел в пределы виджета.
# Leave: указатель мыши покинул виджет.

# menu = Menu(window)
# menu.add_command(label='first')
# window.config(menu=menu)
# # добавление в меню
# new_item = Menu(menu)
# new_item.add_command(label='Новый')
# menu.add_cascade(label='Файл', menu=new_item)
# window.config(menu=menu)

# добавление вкладки
# tab_control = ttk.Notebook(window)
# tab1 = ttk.Frame(tab_control)
# tab_control.add(tab1, text='Первая вкладка')
# tab_control.pack(expand=1, fill='both')
