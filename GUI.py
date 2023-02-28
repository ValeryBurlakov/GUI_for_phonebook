import tkinter as tk # импорт библиотеки
from tkinter import * # импорт всех методов
from tkinter import messagebox # явное импортирование




window = Tk()
window.title("Телефонная книга")
window.geometry('400x300')

def main():
    input_ = int(user_input.get())
    if user_input == str(0):
        messagebox.showinfo('command-pythonguides', f'Вы ввели 0')
    elif user_input == str(1):
        messagebox.showinfo('command-pythonguides', f'Вы ввели 1')
frame = Frame(
    window, # указывает окно для размещения frame
    padx = 10, # отступы
    pady = 10
)
frame.pack(expand=True) # позиционируем виджет в окне

# добавили виджет label для поля ввода
entry_field = Label(
    frame, # заготовка виджета в которой уже настроены отступы по фертикали и горизонтали
    text = "Введите что-нибудь "
)

entry_field.grid(row=3, column=1) # grid метод позиционирования виджета в окне
user_input = Entry(
    frame, # заготовка с отступами
)
user_input.grid(row=3, column=2, pady=5)




button_start = Button(
    frame,
    text= 'Ввод',
    command = main
)
button_start.grid(row=5, column=2) # разместили кнопку в ячейке






window.mainloop() # функция запуска цикла событий
