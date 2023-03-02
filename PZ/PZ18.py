from tkinter import *
from tkinter import ttk

# root = Tk()  # создаем корневой объект - окно
# root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
# # root.iconbitmap(default="favicon.ico") # можно задать любую иконку
# root.geometry("300x250")  # устанавливаем размеры окна
# root.update_idletasks()     # Чтобы приложение еще до метода mainloop()
#                             # принименило для окна переданные ему значения по ширине, высоте и позиции
# # root.resizable(False, False) # делает размер окна фиксированным
# label = Label(text="Hello METANIT.COM")  # создаем текстовую метку
# # root.minsize(200, 150)   # минимальные размеры: ширина - 200, высота - 150
# # root.maxsize(400, 300)   # максимальные размеры: ширина - 400, высота - 300
# label.pack()  # размещаем метку в окне
# btn = ttk.Button()
# btn.pack()
# # устанавливаем параметр text
# btn.config(text="Send Email")
# root.mainloop()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
# btn = ttk.Button(text="Click me")
# btn.pack(expand=True, anchor="nw", fill=X)
# root.mainloop()

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
btn1 = ttk.Button(text="BOTTOM")
btn1.pack(side=BOTTOM)
btn2 = ttk.Button(text="RIGHT")
btn2.pack(side=RIGHT)
btn3 = ttk.Button(text="LEFT")
btn3.pack(side=LEFT)
btn4 = ttk.Button(text="TOP")
btn4.pack(side=TOP)
root.mainloop()
