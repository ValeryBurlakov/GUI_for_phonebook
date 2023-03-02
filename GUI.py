import tkinter as tk # импорт библиотеки
from tkinter import * # импорт всех методов
from tkinter import messagebox # явное импортирование
from tkinter import ttk  
from datetime import datetime

def finish():
    window.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")
    messagebox.showinfo('answer-pythonguides', f'Ты закрыл это божественное приложение!!!')

def enter_(event):
    # messagebox.showinfo('answer-pythonguides', f'Вы ввели enter')
    main_()


def main_():
    global answer
    answer = user_input.get()
    dt = datetime.now()
    # messagebox.showinfo('Ебучая книга', f'Доброго времени суток! {dt.strftime("%A, %d %B %Y %I:%M%p")}')
    if answer == '0':
                # messagebox.showinfo('answer-pythonguides', f'Ты гандон ввёл 0')
                menu()
                # out_field = Label(
                # frame, 
                # text = f'Ты ввёл: {answer}',
                # )
                # out_field.grid(row=5, column=1)

                # out_field2 = Label(
                # frame, 
                # text = f'Ты ввёл: {int(answer) + 1}',

                # )
                # out_field2.grid(row=6, column=1)
    elif answer == '1':
            ui.menu()
    elif answer == '2':
                messagebox.showinfo('answer-pythonguides', f'Ты гандон ввёл 2')
    elif answer == '9':
              print("получай в консоли exit")

def menu():
    out_field_0 = Label(
    frame, 
    text = f'0 - вызов меню',
    )
    out_field_0.grid(row=4, column=1) 
    
    out_field_1 = Label(
    frame, 
    text = f'1 - показать справочник',
    )
    out_field_1.grid(row=5, column=1)

    out_field_2 = Label(
    frame, 
    text = f'2 - добавить новый контакт',
    )
    out_field_2.grid(row=6, column=1)

    # print("\033[32m2\033[0m - добавить новый контакт")
    # print("\033[32m3\033[0m - удалить контакт")
    # print("\033[32m4\033[0m - поиск контакта(нужно ввести имя целиком)")
    # print("\033[32m5\033[0m - продвинутый поиск(по всем данным)")
    # print("\033[32m6\033[0m - выгрузка данных")
    # print("\033[32m7\033[0m - изменение данных")
    # print("\033[32m8\033[0m - Копирование справочника в файл")
    # print("\033[32m9\033[0m - выход из программы")



window = Tk()
window.title("Телефонная книга")
window.geometry('600x400')
window.bind('<Return>', enter_)
window.protocol("WM_DELETE_WINDOW", finish)

frame = Frame(
window, # указывает окно для размещения виджета frame для контроля расположения элементов
padx = 10, # отступы
pady = 10
)
frame.pack(expand=True) # позиционируем виджет в окне

# добавили виджет label для поля ввода
entry_field = Label(
    frame, # заготовка виджета в которой уже настроены отступы по фертикали и горизонтали
    text = "Введите ваше имя "
)
entry_field.grid(row=3, column=1) # grid метод позиционирования виджета в окне



# виджет ввода
user_input = Entry(
    frame, # заготовка с отступами
)
user_input.grid(row=3, column=2, pady=5)

# кнопка

button_start = ttk.Button(
    frame,
    text= 'Ввод',
    command = main_
)
button_start.grid(row=5, column=2) # разместили кнопку в ячейке





window.mainloop() # функция запуска цикла событий
