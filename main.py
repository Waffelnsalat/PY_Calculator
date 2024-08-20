# import for windows
import tkinter
from tkinter import *
import math

# define new window
calculator = Tk()
# configure frame of window
calculator.title("Calculator")

# configure how the frames in the window are build

calculator.rowconfigure(0, weight=1)
calculator.rowconfigure([1, 2, 3, 4, 5], minsize=60, weight=1)
calculator.columnconfigure([0, 1, 2, 3], minsize=60, weight=1)


# define label update when button pressed

def button_one():
    value = counter["text"]
    counter["text"] = value + "1"


def button_two():
    value = counter["text"]
    counter["text"] = value + "2"


def button_three():
    value = counter["text"]
    counter["text"] = value + "3"


def button_four():
    value = counter["text"]
    counter["text"] = value + "4"


def button_five():
    value = counter["text"]
    counter["text"] = value + "5"


def button_six():
    value = counter["text"]
    counter["text"] = value + "6"


def button_seven():
    value = counter["text"]
    counter["text"] = value + "7"


def button_eight():
    value = counter["text"]
    counter["text"] = value + "8"


def button_nine():
    value = counter["text"]
    counter["text"] = value + "9"


def button_plus():
    value = counter["text"]
    counter["text"] = value + "+"


def button_minus():
    value = counter["text"]
    counter["text"] = value + "-"


def button_multiple():
    value = counter["text"]
    counter["text"] = value + "*"


def button_devide():
    value = counter["text"]
    counter["text"] = value + "/"


def button_point():
    value = counter["text"]
    counter["text"] = value + "."


def button_zero():
    value = counter["text"]
    counter["text"] = value + "0"


def button_clamopen():
    value = counter["text"]
    counter["text"] = value + "("


def button_clamclose():
    value = counter["text"]
    counter["text"] = value + ")"


def button_sqrt():
    value = counter["text"]
    counter["text"] = value + "¬/("


# define calculation
def button_calc():
    value = str(counter["text"])
    value = value.replace("¬/", "math.sqrt")
    print(value)
    try:
        result = eval(value)
        counter["text"] = str(result)
    except:
        print("SyntaxError")
        counter["text"] = "Syntax Error"


# define delete button
def button_del2():
    value = str(counter["text"])
    try:
        counter["text"] = value.rstrip(value[-1])
    except:
        print("Nothing to delete")


def button_del():
    try:
        counter["text"] = ""
    except:
        print("Nothing to delete")


def button_p2():
    try:
        counter["text"] = ""
    except:
        print("Nothing to delete")


# connect keyboard with calculator

def do_return(event):
    value = str(counter["text"])
    try:
        result = eval(value)
        counter["text"] = str(result)
    except:
        print("SyntaxError")
        counter["text"] = "Syntax Error"


def do_backspace(event):
    value = str(counter["text"])
    try:
        counter["text"] = value.rstrip(value[-1])
    except:
        print("Nothing to delete")


def do_delete(event):
    try:
        counter["text"] = ""
    except:
        print("Nothing to delete")


def key_pressed(event):
    if event.char == "=":
        button_calc()
    else:
        value = counter["text"]
        counter["text"] = value + event.char


# define dispalte lable
counter = tkinter.Label(text="", font=('times', 15, 'bold'))
counter.grid(row=0, columnspan=4)

# button config
btn_one = tkinter.Button(master=calculator, text="1", command=button_one, font=('times', 15, 'bold'))
btn_one.grid(row=1, column=0, sticky="nsew")

btn_two = tkinter.Button(master=calculator, text="2", command=button_two, font=('times', 15, 'bold'))
btn_two.grid(row=1, column=1, sticky="nsew")

btn_three = tkinter.Button(master=calculator, text="3", command=button_three, font=('times', 15, 'bold'))
btn_three.grid(row=1, column=2, sticky="nsew")

btn_plus = tkinter.Button(master=calculator, text="+", command=button_plus, font=('times', 15, 'bold'))
btn_plus.grid(row=1, column=3, sticky="nsew")

btn_four = tkinter.Button(master=calculator, text="4", command=button_four, font=('times', 15, 'bold'))
btn_four.grid(row=2, column=0, sticky="nsew")

btn_five = tkinter.Button(master=calculator, text="5", command=button_five, font=('times', 15, 'bold'))
btn_five.grid(row=2, column=1, sticky="nsew")

btn_six = tkinter.Button(master=calculator, text="6", command=button_six, font=('times', 15, 'bold'))
btn_six.grid(row=2, column=2, sticky="nsew")

btn_minus = tkinter.Button(master=calculator, text="-", command=button_minus, font=('times', 15, 'bold'))
btn_minus.grid(row=2, column=3, sticky="nsew")

btn_seven = tkinter.Button(master=calculator, text="7", command=button_seven, font=('times', 15, 'bold'))
btn_seven.grid(row=3, column=0, sticky="nsew")

btn_eight = tkinter.Button(master=calculator, text="8", command=button_eight, font=('times', 15, 'bold'))
btn_eight.grid(row=3, column=1, sticky="nsew")

btn_nine = tkinter.Button(master=calculator, text="9", command=button_nine, font=('times', 15, 'bold'))
btn_nine.grid(row=3, column=2, sticky="nsew")

btn_multiple = tkinter.Button(master=calculator, text="*", command=button_multiple, font=('times', 15, 'bold'))
btn_multiple.grid(row=3, column=3, sticky="nsew")

btn_del = tkinter.Button(master=calculator, text="del", command=button_del, font=('times', 15, 'bold'))
btn_del.grid(row=4, column=0, sticky="nsew")

btn_zero = tkinter.Button(master=calculator, text="0", command=button_zero, font=('times', 15, 'bold'))
btn_zero.grid(row=4, column=1, sticky="nsew")

btn_calc = tkinter.Button(master=calculator, text="=", command=button_calc, font=('times', 15, 'bold'))
btn_calc.grid(row=4, column=2, sticky="nsew")

btn_devide = tkinter.Button(master=calculator, text="/", command=button_devide, font=('times', 15, 'bold'))
btn_devide.grid(row=4, column=3, sticky="nsew")

btn_clam1 = tkinter.Button(master=calculator, text="(", command=button_clamopen, font=('times', 15, 'bold'))
btn_clam1.grid(row=5, column=0, sticky="nsew")

btn_clam2 = tkinter.Button(master=calculator, text=")", command=button_clamclose, font=('times', 15, 'bold'))
btn_clam2.grid(row=5, column=1, sticky="nsew")

btn_point = tkinter.Button(master=calculator, text=".", command=button_point, font=('times', 15, 'bold'))
btn_point.grid(row=5, column=2, sticky="nsew")

btn_sqrt = tkinter.Button(master=calculator, text="¬/", command=button_sqrt, font=('times', 15, 'bold'))
btn_sqrt.grid(row=5, column=3, sticky="nsew")

btn_p2 = tkinter.Button(master=calculator, text="->", command=button_p2, font=('times', 15, 'bold'))
btn_p2.grid(row=6, column=3, sticky="nsew")

# testing for pressed key on keyboard
calculator.bind("<BackSpace>", do_backspace)
calculator.bind("<Return>", do_return)
calculator.bind("<Delete>", do_delete)
calculator.bind("<Key>", key_pressed)

# holding window open


calculator.mainloop()
