import tkinter as t
from tkinter import ttk
from tkinter import messagebox as tmb

window = t.Tk()
window.geometry('490x370')
window.resizable(0,0)
window.title('Frogzen Calculator')
window.iconbitmap("./assets/icon.ico")

# set the indicator value
indicator_value = t.StringVar()
indicator_value.set('')

# status
status = 'num'
isNeg = False

#define the logo
logo = t.PhotoImage(file='./assets/logo.png')

# menu functions
memory = 0

def doNotThing():
    tmb.showinfo(title='Secret window', message='Oh! You just discover a hidden window!')

def mem_plus():
    try:
        global memory
        memory += int(indicator_value.get())
    except ValueError:
            try:
                memory += float(indicator_value.get())
            except ValueError:
                indicator_value.set('')
                tmb.showwarning(title='error', message='Please give the memory a number')

def mem_minus():
    try:
        global memory
        memory -= int(indicator_value.get())
    except ValueError:
            try:
                memory -= float(indicator_value.get())
            except ValueError:
                indicator_value.set('')
                tmb.showwarning(title='error', message='Please give the memory a number')

def get_mem():
    global status
    if status == 'num':
        indicator_value.set(indicator_value.get() + str(memory))
        status = 'symbol'
    else:
        indicator_value.set(str(memory))

def clear_mem():
    global memory
    memory = 0

def ver():
    ver = t.Toplevel()
    ver.resizable(0,0)
    ver.title('Version')
    ver.iconbitmap("./assets/icon.ico")
    ver.geometry('320x220')
   
    verlabel = ttk.Label(ver)
    verlabel.config(text='Frogzen Calculator\nversion 1.0', image=logo, compound='left')
    verlabel.place(anchor='center', x=160, y=100)

    verexit = ttk.Button(ver)
    verexit.config(text='Got it!', style='BW.TButton', command=ver.destroy)
    verexit.place(anchor='center', x=160, y=150)

# menubar and menu code
menubar = t.Menu(window)
memory_menu = t.Menu(menubar, tearoff=0)
memory_menu.add_command(label="M+", command=mem_plus)
memory_menu.add_command(label="M-", command=mem_minus)
memory_menu.add_command(label="MR", command=get_mem)
memory_menu.add_command(label="MC", command=clear_mem)
menubar.add_cascade(label="Memory", menu=memory_menu)

settings_menu = t.Menu(menubar, tearoff=0)
settings_menu.add_command(label='Version', command=ver)
settings_menu.add_command(label="Exit", command=window.quit)
settings_menu.add_command(label='', command=doNotThing)
menubar.add_cascade(label='Settings', menu=settings_menu)
window.config(menu=menubar)

# function that controls the indicator
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

def appendLB():
    indicator_value.set(f'{indicator_value.get()}(')

def appendRB():
    global isNeg
    indicator_value.set(f'{indicator_value.get()})')
    isNeg = False


def pos2Neg():
    global isNeg
    if isNeg == False:
        indicator_value.set(f'{indicator_value.get()}(-')
        isNeg = True

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
    try:
        indicator_value.set(eval(result))
    except ZeroDivisionError:
        indicator_value.set('')
        tmb.showwarning(title='error', message='Cannor divide a number by zero')
    except SyntaxError:
        indicator_value.set('')
        tmb.showwarning(title='error', message='There are syntax error(s)')
    result = indicator_value.get()
    if result[(len(result) - 2):] == '.0' :
        indicator_value.set(result[:(len(result) - 2)])
    elif len(result) < 12:
        indicator_value.set(result)
    elif '.' in result:
        indicator_value.set(result[:(len(result) - 6)])

# create the indicator
indicator = t.Label(window)
indicator.config(textvariable=indicator_value, height=2, width=62,  \
                bd=3, relief='solid')
indicator.place(anchor='center', x=240, y=33)

# defines the style for buttons
btstyle = ttk.Style()
btstyle.configure(style="BW.TButton", foreground="black")

# create the buttons
button1 = ttk.Button(window)
button1.config(text='\n1\n', width=12, command=append1, style="BW.TButton")
button1.place(anchor='center', x=55, y=98)

button2 = ttk.Button(window)
button2.config(text='\n2\n', width=12, command=append2, style="BW.TButton")
button2.place(anchor='center', x=150, y=98)

button3 = ttk.Button(window)
button3.config(text='\n3\n', width=12, command=append3, style="BW.TButton")
button3.place(anchor='center', x=245, y=98)


button4 = ttk.Button(window)
button4.config(text='\n4\n', width=12, command=append4, style="BW.TButton")
button4.place(anchor='center', x=55, y=163)

button5 = ttk.Button(window)
button5.config(text='\n5\n', width=12, command=append5, style="BW.TButton")
button5.place(anchor='center', x=150, y=163)

button6 = ttk.Button(window)
button6.config(text='\n6\n', width=12, command=append6, style="BW.TButton")
button6.place(anchor='center', x=245, y=163)


button7 = ttk.Button(window)
button7.config(text='\n7\n', width=12, command=append7, style="BW.TButton")
button7.place(anchor='center', x=55, y=228)

button8 = ttk.Button(window)
button8.config(text='\n8\n', width=12, command=append8, style="BW.TButton")
button8.place(anchor='center', x=150, y=228)

button9 = ttk.Button(window)
button9.config(text='\n9\n', width=12, command=append9, style="BW.TButton")
button9.place(anchor='center', x=245, y=228)

button0 = ttk.Button(window)
button0.config(text='\n0\n', width=12, command=append0, style="BW.TButton")
button0.place(anchor='center', x=150, y=293)

buttonLB = ttk.Button(window)
buttonLB.config(text='\n(\n', width=5, command=appendLB, style="BW.TButton")
buttonLB.place(anchor='center', x=32, y=293)

buttonRB = ttk.Button(window)
buttonRB.config(text='\n)\n', width=5, command=appendRB, style="BW.TButton")
buttonRB.place(anchor='center', x=78, y=293)

buttonAC = ttk.Button(window)
buttonAC.config(text='\nAC\n', width=12, command=clear, style="BW.TButton")
buttonAC.place(anchor='center', x=435, y=98)

buttonC = ttk.Button(window)
buttonC.config(text='\nC\n', width=12, command=delete, style="BW.TButton")
buttonC.place(anchor='center', x=435, y=163)

button_equal = ttk.Button(window)
button_equal.config(text='\n=\n', width=12, command=calculate, style="BW.TButton")
button_equal.place(anchor='center', x=245, y=293)

button_plus = ttk.Button(window)
button_plus.config(text='\n+\n', width=12, command=append_plus, style="BW.TButton")
button_plus.place(anchor='center', x=340, y=98)

button_minus = ttk.Button(window)
button_minus.config(text='\n-\n', width=12, command=append_minus, style="BW.TButton")
button_minus.place(anchor='center', x=340, y=163)

button_mutipliation = ttk.Button(window)
button_mutipliation.config(text='\n×\n', width=12, command=append_mutiplication, style="BW.TButton")
button_mutipliation.place(anchor='center', x=340, y=228)

button_divition = ttk.Button(window)
button_divition.config(text='\n÷\n', width=12, command=append_divition, style="BW.TButton")
button_divition.place(anchor='center', x=340, y=293)

buttonDP = ttk.Button(window)
buttonDP.config(text='\n.\n', width=12, command=append_decimalPoint, style="BW.TButton")
buttonDP.place(anchor='center', x=435, y=228)

button_pos2Neg = ttk.Button(window)
button_pos2Neg.config(text='\n(-\n', width=12, command=pos2Neg, style="BW.TButton")
button_pos2Neg.place(anchor='center', x=435, y=293)

window.mainloop()