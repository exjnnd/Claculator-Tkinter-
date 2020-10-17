#written by Amirali Rezaei
#agar ba pycharm ya vs code baz kardin error gereft, erroresh alakie
from tkinter import *

window = Tk()
window.title("Yasan-Calculator")

e = Entry(window, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#e.insert(0, "Enter Your Name: ")

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clearing():
    e.delete(0, END)

def adding():
    global f_num
    global math
    math = "ezafe"
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0, END)

def divisioning():
    global f_num
    global math
    math = "taqsim"
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0, END)

def zarb():
    global f_num
    global math
    math = "zarbkardan"
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0, END)

def menha():
    global f_num
    global math
    math = "minus"
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0, END)

def calculate():
    if(math == "ezafe"):
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num + int(second_number))

    if (math == "zarbkardan"):
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num * int(second_number))

    if(math == "minus"):
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num - int(second_number))

    if(math == "taqsim"):
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num / int(second_number))

#Define buttons
button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(window, text="+", padx=39, pady=20, command=adding)
button_equal = Button(window, text="=", padx=91, pady=20, command=calculate)
button_clear = Button(window, text="Clear", padx=79, pady=20, command=lambda: clearing())

button_division = Button(window, text="÷", padx=40, pady=20, command=divisioning)
button_multiplie = Button(window, text="x", padx=39, pady=20, command=zarb)
button_minus = Button(window, text="-", padx=39, pady=20, command=menha)


#Put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_division.grid(row=6, column=0)
button_multiplie.grid(row=6, column=1)
button_minus.grid(row=6, column=2)


window.mainloop()
