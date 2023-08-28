from tkinter import *
from tkinter import ttk

tk = Tk()
tk.geometry('335x310')

num1 = ''
num2 = ''
znack = ''

btn = ttk.Button(text = '')
btn.place(x=130,y=150)

def one():
    global num1
    global num2
    global znack
    global btn

    if znack == '':
        num1 += '1'
        btn["text"]=num1

    else:
        num2 += '1'
        btn["text"]=num2




def two():
    global num1
    global num2
    global znack

    if znack == '':
        num1 += '2'
        btn["text"]=num1
    else:
        num2 += '2'
        btn["text"]=num2

def three():
    global num1
    global num2
    global znack

    if znack == '':
        num1 += '3'
        btn["text"]=num1
    else:
        num2 += '3'
        btn["text"]=num2

def four():
    global num1
    global num2
    global znack

    if znack == '':
        num1 += '4'
        btn["text"]=num1
    else:
        num2 += '4'
        btn["text"]=num2

def five():
    global num1
    global num2
    global znack

    if znack == '':
        num1 += '5'
        btn["text"]=num1
    else:
        num2 += '5'
        btn["text"]=num2

def six():
    global num1
    global num2
    global znack

    if znack == '':
        num1 += '6'
        btn["text"]=num1
    else:
        num2 += '6'
        btn["text"]=num2

def seven():
    global num1
    global num2
    global znack

    if znack == '':
        num1 += '7'
        btn["text"]=num1
    else:
        num2 += '7'
        btn["text"]=num2

def eight():
    global num1
    global num2
    global znack

    if znack == '':
        num1 += '8'
        btn["text"]=num1
    else:
        num2 += '8'
        btn["text"]=num2

def nine():
    global num1
    global num2
    global znack

    if znack == '':
        num1 += '9'
        btn["text"]=num1
    else:
        num2 += '9'
        btn["text"]=num2

def zero():
    global num1
    global num2
    global znack

    if znack == '':
        num1 += '0'
        btn["text"]=num1
    else:
        num2 += '0'
        btn["text"]=num2
        

def plus():
    global znack
    znack = '+'

def minus():
    global znack
    znack = '-'

def raz():
    global znack
    znack = '/'

def x():
    global znack
    znack = '*'


def c():
    global znack
    global num1
    global num2
    
    if znack == '':
        num1 = num1[:-1]
        btn["text"]=num1
    else:
        num2 = num2[:-1]
        btn["text"]=num2




def ravn():
    global num1
    global num2
    global znack

    if znack == '+':
        print(int(num1)+int(num2))
        btn["text"]=(int(num1)+int(num2))

    elif znack == '-':
        print(int(num1)-int(num2))
        btn["text"]=(int(num1)-int(num2))

    elif znack == '*':
        print(int(num1)*int(num2))
        btn["text"]=(int(num1)*int(num2))

    elif znack == '/':
        print(int(num1)/int(num2))
        btn["text"]=(int(num1)/int(num2))



btn0 = ttk.Button(text = '0',command=zero)
btn0.place(x=90,y=280)
btn1 = ttk.Button(text = '1',command=one)
btn1.place(x=10,y=250)
btn2 = ttk.Button(text = '2',command=two)
btn2.place(x=90,y=250)
btn3 = ttk.Button(text = '3',command=three)
btn3.place(x=170,y=250)
btn4 = ttk.Button(text = '4',command=four)
btn4.place(x=10,y=220)
btn5 = ttk.Button(text = '5',command=five)
btn5.place(x=90,y=220)
btn6 = ttk.Button(text = '6',command=six)
btn6.place(x=170,y=220)
btn7 = ttk.Button(text = '7',command=seven)
btn7.place(x=10,y=190)
btn8 = ttk.Button(text = '8',command=eight)
btn8.place(x=90,y=190)
btn9 = ttk.Button(text = '9',command=nine)
btn9.place(x=170,y=190)

btnc = ttk.Button(text = 'c',command=c)
btnc.place(x=10,y=280)
btn_raz = ttk.Button(text = '/',command=raz)
btn_raz.place(x=170,y=280)
btn_ravn = ttk.Button(text = '=',command=ravn)
btn_ravn.place(x=250,y=280)
btn_plus = ttk.Button(text = '+',command=plus)
btn_plus.place(x=250,y=250)
btn_x = ttk.Button(text = '*',command=x)
btn_x.place(x=250,y=190)
btn_minus = ttk.Button(text = '-',command=minus)
btn_minus.place(x=250,y=220)

tk.mainloop()

# from tkinter import *
# from tkinter import ttk

# tk = Tk()
# tk.geometry('360x510')


# num1 = ''
# num2 = ''

# def one():
#     n1  = 1
#     for i in range(11):
#         print(f'{n1} * {i} = {n1*i}')

# def two():
#     n1  = 2
#     for i in range(11):
#         print(f'{n1} * {i} = {n1*i}')

# def three():
#     n1  = 3
#     for i in range(11):
#         print(f'{n1} * {i} = {n1*i}')

# def four():
#     n1  = 4
#     for i in range(11):
#         print(f'{n1} * {i} = {n1*i}')

# def five():
#     n1  = 5
#     for i in range(11):
#         print(f'{n1} * {i} = {n1*i}')

# def six():
#     n1  = 6
#     for i in range(11):
#         print(f'{n1} * {i} = {n1*i}')

# def seven():
#     n1  = 7
#     for i in range(11):
#         print(f'{n1} * {i} = {n1*i}')

# def eight():
#     n1  = 8
#     for i in range(11):
#         print(f'{n1} * {i} = {n1*i}')
# def nine():
#     n1  = 9
#     for i in range(11):
#         print(f'{n1} * {i} = {n1*i}')

# def zero():
#     n1  = 0
#     for i in range(11):
#         print(f'{n1} * {i} = {n1*i}')
        

# btn0 = ttk.Button(text = '0',command=zero)
# btn0.place(x=10,y=480)
# btn1 = ttk.Button(text = '1',command=one)
# btn1.place(x=90,y=480)
# btn2 = ttk.Button(text = '2',command=two)
# btn2.place(x=170,y=480)
# btn3 = ttk.Button(text = '3',command=three)
# btn3.place(x=250,y=480)

# btn4 = ttk.Button(text = '4',command=four)
# btn4.place(x=10,y=450)
# btn5 = ttk.Button(text = '5',command=five)
# btn5.place(x=90,y=450)
# btn6 = ttk.Button(text = '6',command=six)
# btn6.place(x=170,y=450)
# btn7 = ttk.Button(text = '7',command=seven)
# btn7.place(x=250,y=450)

# btn8 = ttk.Button(text = '8',command=eight)
# btn8.place(x=10,y=420)
# btn9 = ttk.Button(text = '9',command=nine)
# btn9.place(x=90,y=420)




# tk.mainloop()