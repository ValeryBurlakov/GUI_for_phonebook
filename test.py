import tkinter as tk

global counter
counter = "Ввод"
def counter_label(label):
  
  def count():
    if (counter == 'Ввод'):
        
        label.config(text='Записал')
        # counter = "Записал"
        label.after(3000, count) 
        counter = "Записал"
        return counter
        
    else:
        if (counter == "Записал"):
            label.config(text='Ввод')
            label.after(3000, count)
            counter = "Ввод"
            return counter
  count()
 
 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()

# def finish():
#     window.destroy()  # ручное закрытие окна и всего приложения
#     print("Закрытие приложения")
#     messagebox.showinfo('answer-pythonguides', f'Ты закрыл это божественное приложение!!!')

# def enter_(event):
#     # messagebox.showinfo('answer-pythonguides', f'Вы ввели enter')
#     main_()


# def main_():
#     global answer
#     answer = user_input.get() # получение ответа из виджета user input
#     # dt = datetime.now()
#     # messagebox.showinfo('Ебучая книга', f'Доброго времени суток! {dt.strftime("%A, %d %B %Y %I:%M%p")}')
#     if answer == '0':
#                 # messagebox.showinfo('answer-pythonguides', f'Ты гандон ввёл 0')
#                 menu()
#     elif answer == '1':
#         try:
#             out_field_menu.destroy()
#             lbox.destroy()
#             printt_phone_book()
#             out_field_print = Label(
#             frame_2, 
#             text = f'Вывод контактов'
#             )
#             out_field_print.grid(row=0, column=0)
#             # messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Вывод контактов в консоль')
#         except:
#             printt_phone_book()
#             out_field_print = Label(
#             frame_2, 
#             text = f'Вывод контактов'
#             )
#             out_field_print.grid(row=0, column=0)
#             messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Вывод контактов в консоль')
#     elif answer == '2':
#         import new_contact as new_
#         new_.new_contactt()
#         messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Новый контакт')
#     elif answer == '3':
#         messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Ты ввёл 3')
#     elif answer == '4':
#         messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Ты ввёл 4')
#     elif answer == '5':
#         messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Ты ввёл 5')
#     elif answer == '6':
#         messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Ты ввёл 6')
#     elif answer == '7':
#         messagebox.showinfo('ИНФОРМАЦИОННОЕ ТАБЛО', f'Ты ввёл 7')
#     elif answer == '8':
#         out_field_8 = Label(
#         frame_2, 
#         text = f'Ты ввёл 8'
#         )
#         out_field_8.grid(row=0, column=0)
#         # messagebox.showinfo('answer-pythonguides', f'Ты гандон ввёл 8')
#     elif answer == '9':
#         print("получай в консоли exit")
#     else:
#          menu()




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
# entry_field_1 = Label(
#     frame, # заготовка виджета в которой уже настроены отступы по вертикали и горизонтали
#     padx=0,
#     text = "Введите команду(0 - меню):",
#     bg='yellow'
# )
# entry_field_1.grid(row=0, column=2) # grid метод позиционирования виджета в окне






# ВИДЖЕТ ВВОДА
# user_input = Entry(
#     frame, # заготовка с отступами
#     bg="red"
# )
# user_input.grid(row=1, column=2)

# кнопки

# button_start = ttk.Button(
#     frame,
#     text= 'Enter',
#     command = main_
# )
# button_start.grid(row=2, column=2) # разместили кнопку в ячейке



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


