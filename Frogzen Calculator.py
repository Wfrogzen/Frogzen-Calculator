import tkinter as t
from tkinter import messagebox as tmb

window = t.Tk()
window.geometry('480x380')
window.config(bg='#707070')
window.resizable(0,0)
window.title('Frogzen Calculator')
window.iconbitmap("icon.ico")

#set the indicator value
indicator_value = t.StringVar()
indicator_value.set('')

status = 'num'
#menu functions
memory = 0
def donothing():
    print('1')

def mem_plus():
    try:
        global memory
        memory += int(indicator_value.get())
    except ValueError:
            try:
                memory += float(indicator_value.get())
            except ValueError:
                indicator_value.set('')
                tmb.showwarning(title='calc', message='Please give the memory a number')

def mem_minus():
    try:
        global memory
        memory -= int(indicator_value.get())
    except ValueError:
            try:
                memory -= float(indicator_value.get())
            except ValueError:
                indicator_value.set('')
                tmb.showwarning(title='calc', message='Please give the memory a number')

def get_mem():
    indicator_value.set(str(memory))

def clear_mem():
    global memory
    memory = 0

def ver():
    ver = t.Tk()
    ver.resizable(0,0)
    ver.title('Version')
    ver.iconbitmap("icon.ico")
    ver.geometry('320x220')
    verlabel = t.Label(ver)
    verlabel.config(text='Frogzen Calculator\nvertion 0.0_1(alpha 1)\nFrogzen', \
                    font='Consolas 18')
    verlabel.place(anchor='center', x=160, y=100)

#menubar and menu code
menubar = t.Menu(window)
menubar.config(bg='#707070')
memory_menu = t.Menu(menubar, tearoff=0)
memory_menu.add_command(label="M+", font='Consolas 15', command=mem_plus)
memory_menu.add_command(label="M-", font='Consolas 15', command=mem_minus)
memory_menu.add_command(label="MR", font='Consolas 15', command=get_mem)
memory_menu.add_command(label="MC", font='Consolas 15', command=donothing)
menubar.add_cascade(label="Memory", font='Consolas 15', menu=memory_menu)

settings_menu = t.Menu(menubar, tearoff=0)
settings_menu.add_command(label='Version', font='Consolas 15', command=ver)
settings_menu.add_command(label="Exit", font='Consolas 15', command=window.quit)
menubar.add_cascade(label='Settings', font='Consolas 15',menu=settings_menu)
window.config(menu=menubar)

#function that controls the indicator
def append1():
    global status
    indicator_value.set(f'{indicator_value.get()}1')
    status = 'symbol'

def append2():
    global status
    indicator_value.set(f'{indicator_value.get()}2')
    status = 'symbol'

def append3():
    global status
    indicator_value.set(f'{indicator_value.get()}3')
    status = 'symbol'

def append4():
    global status
    indicator_value.set(f'{indicator_value.get()}4')
    status = 'symbol'

def append5():
    global status
    indicator_value.set(f'{indicator_value.get()}5')
    status = 'symbol'

def append6():
    global status
    indicator_value.set(f'{indicator_value.get()}6')
    status = 'symbol'

def append7():
    global status
    indicator_value.set(f'{indicator_value.get()}7')
    status = 'symbol'

def append8():
    global status
    indicator_value.set(f'{indicator_value.get()}8')
    status = 'symbol'

def append9():
    global status
    indicator_value.set(f'{indicator_value.get()}9')
    status = 'symbol'

def append0():
    global status
    indicator_value.set(f'{indicator_value.get()}0')
    status = 'symbol'

def append00():
    global status
    indicator_value.set(f'{indicator_value.get()}00')
    status = 'symbol'

def append_decimalPoint():
    global status
    indicator_value.set(f'{indicator_value.get()}.')
    status = 'symbol'

def append_plus():
    global status
    if status == 'symbol':
        indicator_value.set(f'{indicator_value.get()}+')
        status = 'num'

def append_minus():
    global status
    if status == 'symbol':
        indicator_value.set(f'{indicator_value.get()}-')
        status = 'num'

def append_mutiplication():
    global status
    if status == 'symbol':
        indicator_value.set(f'{indicator_value.get()}×')
        status = 'num'

def append_divition():
    global status
    if status == 'symbol':
        indicator_value.set(f'{indicator_value.get()}÷')
        status = 'num'

def clear():
    indicator_value.set('')
    global status
    status = 'symbol'

def delete():
    indicator_value.set((indicator_value.get())[:(len(indicator_value.get()) - 1)])
    global status
    status = 'symbol'

def calculate():
    result = indicator_value.get()
    result = result.replace('×','*')
    result = result.replace('÷','/')
    print(result)
    try:
        indicator_value.set(eval(result))
    except ZeroDivisionError:
        indicator_value.set('')
        tmb.showwarning(title='calc', message='Cannor divide a number by zero')
    result = indicator_value.get()
    if result[(len(result) - 2):] == '.0' :
        indicator_value.set(result[:(len(result) - 2)])
    elif len(result) < 12:
        indicator_value.set(result)
    elif '.' in result:
        indicator_value.set(result[:(len(result) - 6)])

# create the indicator
indicator = t.Label(window)
indicator.config(textvariable=indicator_value, fg='#303030', height=2, width=62,  \
                bd=3, bg='#ffffff', relief='solid')
indicator.place(anchor='center', x=240, y=33)

# create the buttons
button1 = t.Button(window)
button1.config(text='1', fg='black', bg='#a0a0a0', height=3, width=12, command=append1)
button1.place(anchor='center', x=55, y=98)

button2 = t.Button(window)
button2.config(text='2', fg='black', bg='#a0a0a0', height=3, width=12, command=append2)
button2.place(anchor='center', x=150, y=98)

button3 = t.Button(window)
button3.config(text='3', fg='black', bg='#a0a0a0',height=3, width=12, command=append3)
button3.place(anchor='center', x=245, y=98)


button4 = t.Button(window)
button4.config(text='4', fg='black', bg='#a0a0a0',height=3, width=12, command=append4)
button4.place(anchor='center', x=55, y=163)

button5 = t.Button(window)
button5.config(text='5', fg='black', bg='#a0a0a0',height=3, width=12, command=append5)
button5.place(anchor='center', x=150, y=163)

button6 = t.Button(window)
button6.config(text='6', fg='black', bg='#a0a0a0',height=3, width=12, command=append6)
button6.place(anchor='center', x=245, y=163)


button7 = t.Button(window)
button7.config(text='7', fg='black', bg='#a0a0a0',height=3, width=12, command=append7)
button7.place(anchor='center', x=55, y=228)

button8 = t.Button(window)
button8.config(text='8', fg='black', bg='#a0a0a0',height=3, width=12, command=append8)
button8.place(anchor='center', x=150, y=228)

button9 = t.Button(window)
button9.config(text='9', fg='black', bg='#a0a0a0',height=3, width=12, command=append9)
button9.place(anchor='center', x=245, y=228)

button0 = t.Button(window)
button0.config(text='0', fg='black', bg='#a0a0a0',height=3, width=12, command=append0)
button0.place(anchor='center', x=55, y=293)

button00 = t.Button(window)
button00.config(text='00', fg='black', bg='#a0a0a0',height=3, width=12, command=append00)
button00.place(anchor='center', x=150, y=293)

buttonAC = t.Button(window)
buttonAC.config(text='AC', fg='black', bg='#a0a0a0',height=3, width=12, command=clear)
buttonAC.place(anchor='center', x=435, y=98)

buttonC = t.Button(window)
buttonC.config(text='C', fg='black', bg='#a0a0a0',height=3, width=12, command=delete)
buttonC.place(anchor='center', x=435, y=163)

button_equal = t.Button(window)
button_equal.config(text='=', fg='black', bg='#a0a0a0',height=3, width=12, command=calculate)
button_equal.place(anchor='center', x=245, y=293)

button_plus = t.Button(window)
button_plus.config(text='+', fg='black', bg='#a0a0a0',height=3, width=12, command=append_plus)
button_plus.place(anchor='center', x=340, y=98)

button_minus = t.Button(window)
button_minus.config(text='-', fg='black', bg='#a0a0a0',height=3, width=12, command=append_minus)
button_minus.place(anchor='center', x=340, y=163)

button_mutipliation = t.Button(window)
button_mutipliation.config(text='×', fg='black', bg='#a0a0a0',height=3, width=12, command=append_mutiplication)
button_mutipliation.place(anchor='center', x=340, y=228)

button_divition = t.Button(window)
button_divition.config(text='÷', fg='black', bg='#a0a0a0',height=3, width=12, command=append_divition)
button_divition.place(anchor='center', x=340, y=293)

button_decimalPoint = t.Button(window)
button_decimalPoint.config(text='.', fg='black', bg='#a0a0a0',height=3, width=12, command=append_decimalPoint)
button_decimalPoint.place(anchor='center', x=435, y=228)


window.mainloop()