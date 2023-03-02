import tkinter as tk
from tkinter import *
from tkinter import messagebox

# app = tk.Tk()
# app.geometry("200x100")

# def callback(event):
#     label["text"] = "You pressed Enter"

# app.bind('<Return>', callback)

# label = tk.Label(app, text="")
# label.pack()

# app.mainloop()


# import tkinter as tk

# class app(tk.Frame):
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("300x200")
#         self.label = tk.Label(self.root, text="")
#         self.label.pack()
#         self.root.bind('<Return>', self.callback)
#         self.root.mainloop()


#     def callback(self, event):
#         self.label["text"] = "You pressed {}".format(event.keysym)
    
# app()


import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack()

circle = canvas.create_oval((150, 100, 170, 120), fill='yellow')
vx = 0
vy = 0


def on_key_press(event):
    global vx, vy
    if event.keysym == 'Left':
        vx = -10
    elif event.keysym == 'Right':
        vx = 10
    elif event.keysym == 'Up':
        vy = -10
    elif event.keysym == 'Down':
        vy = 10


def on_key_release(event):
    global vx, vy
    if event.keysym in ('Left', 'Right'):
        vx = 0
    elif event.keysym in ('Up', 'Down'):
        vy = 0


root.bind('<KeyPress>', on_key_press)
root.bind('<KeyRelease>', on_key_release)


def game_loop():
    canvas.move(circle, vx, vy)
    root.after(50, game_loop)


game_loop()

root.mainloop()




# def calculate_bmi():
#    kg = int(weight_tf.get())
#    m = int(height_tf.get())/100
#    bmi = kg/(m*m)
#    bmi = round(bmi, 1)
 
#    if bmi < 18.5:
#        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
#    elif (bmi > 18.5) and (bmi < 24.9):
#        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
#    elif (bmi > 24.9) and (bmi < 29.9):
#        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
#    else:
#        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')  
 
# window = Tk()
# window.title('Калькулятор индекса массы тела (ИМТ)')
# window.geometry('400x300')
 
 
# frame = Frame(
#    window,
#    padx=10,
#    pady=10
# )
# frame.pack(expand=True)
 
 
# height_lb = Label(
#    frame,
#    text="Введите свой рост (в см)  "
# )
# height_lb.grid(row=3, column=1)
 
# weight_lb = Label(
#    frame,
#    text="Введите свой вес (в кг)  ",
# )
# weight_lb.grid(row=4, column=1)
 
# height_tf = Entry(
#    frame,
# )
# height_tf.grid(row=3, column=2, pady=5)
 
# weight_tf = Entry(
#    frame,
# )
# weight_tf.grid(row=4, column=2, pady=5)
 
# cal_btn = Button(
#    frame,
#    text='Рассчитать ИМТ',
#    command=calculate_bmi
# )
# cal_btn.grid(row=5, column=2)
 
# window.mainloop()