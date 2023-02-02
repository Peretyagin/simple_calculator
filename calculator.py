import math
from tkinter import *

root = Tk()
root.geometry("265x400")
root.title("Calculator")
root.config(background="Orange")

expression = ""

result = StringVar()
expression_field = Entry(textvariable=result)
expression_field.grid(columnspan=4,ipadx=70)

coins = ["Rub to Dollar" , "Dollar to Rub" , "Rub to Euro" , "Euro to Rub"]
list_of_coins = Listbox(width=15,height=5)
list_of_coins.grid(row=7,column=1)
for coin in coins:
    list_of_coins.insert(0 , coin)

def press_num(num):
    global expression
    expression += str(num)
    result.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        result.set(total)
        expression = total
    except:
        result.set("error")

def converter():
    actual_coin = list_of_coins.get(list_of_coins.curselection())
    umn = 1
    if actual_coin == "Rub to Dollar":
        umn = 0.014
    elif actual_coin == "Dollar to Rub":
        umn =  70
    elif actual_coin == "Rub to Euro":
        umn = 0.013
    elif actual_coin == "Euro to Rub":
        umn = 76
    global expression
    total = str(eval(expression) * umn)
    result.set(total)
    expression = total

def sqrt_exp():
        global expression
        total = str(math.sqrt(eval(expression)))
        result.set(total)
        expression = total


def sqr_exp():
    global expression
    total = str(eval(expression) * eval(expression) )
    result.set(total)
    expression = total

def reset():
    global expression
    total = ""
    result.set(total)
    expression = total


button1 = Button(text= "1",height=1,width=7, command=lambda: press_num(1))
button1.grid(row = 2, column=0)

button2 = Button(text= "2",height=1,width=7,command=lambda: press_num(2))
button2.grid(row = 2, column=1)

button3 = Button(text= "3",height=1,width=7,command=lambda: press_num(3))
button3.grid(row = 2, column=2)

button4 = Button(text= "4",height=1,width=7,command=lambda: press_num(4))
button4.grid(row = 3, column=0)

button5 = Button(text= "5",height=1,width=7,command=lambda: press_num(5))
button5.grid(row = 3, column=1)

button6 = Button(text= "6",height=1,width=7,command=lambda: press_num(6))
button6.grid(row = 3, column=2)

button7 = Button(text= "7",height=1,width=7,command=lambda: press_num(7))
button7.grid(row = 4, column=0)

button8 = Button(text= "8",height=1,width=7,command=lambda: press_num(8))
button8.grid(row = 4, column=1)

button9 = Button(text= "9",height=1,width=7,command=lambda: press_num(9))
button9.grid(row = 4, column=2)

plus = Button(text= "+",height=1,width=7,command=lambda: press_num("+"))
plus.grid(row = 5, column=0)

button0 = Button(text= "0",height=1,width=7,command=lambda: press_num(0))
button0.grid(row = 5, column=1)

minus = Button(text= "-",height=1,width=7,command=lambda: press_num("-"))
minus.grid(row = 5, column=2)

equal = Button(text= "=",height=1,width=7,command=equalpress)
equal.grid(row = 6, column=1)

multiplication = Button(text= "*",height=1,width=7,command=lambda: press_num("*"))
multiplication.grid(row = 6, column=0)

fission = Button(text= "/",height=1,width=7,command=lambda :press_num("/"))
fission.grid(row = 6, column=2)

"""rub_to_dol = Button(text= "RTD",height=1,width=7, command = lambda: converter(0.014))
rub_to_dol.grid(row = 7, column=0)

dol_to_rub = Button(text= "DTR",height=1,width=7, command = lambda: converter(70))
dol_to_rub.grid(row = 7, column=1)"""

convert  = Button(text= "convert",height=1,width=7,command=converter)
convert.grid(row = 8, column=1)

sqrt  = Button(text= "sqrt",height=1,width=7,command=sqrt_exp)
sqrt.grid(row = 8, column=0)

sqr = Button(text= "sqr",height=1,width=7,command=sqr_exp)
sqr.grid(row = 8, column=2)

reset = Button(text= "R",height=1,width=7,command=reset)
reset.grid(row = 9, column=1)



root.mainloop()
