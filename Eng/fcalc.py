import tkinter as t
from tkinter import ttk
from tkinter import messagebox as tmb
import tkinter.font as tfont
import pyglet as pglt
import platform 

window = t.Tk()
window.resizable(0,0)
window.geometry('600x480')
window.title('Frogzen Calculator')
window.iconbitmap("./assets/icon.ico")

# imports the fonts from ./font folder
pglt.options['win32_gdi_font'] = True
pglt.font.add_file('./fonts/AppleGaramond.ttf')
AppleGaramond11 = tfont.Font(family="AllpeGaramond", size=11)
AppleGaramond16 = tfont.Font(family="AllpeGaramond", size=16)

# defines the style for main buttons
btstyle = ttk.Style()
btstyle.configure(style="BW.TButton", foreground="black", font=AppleGaramond11)
if platform.system() == "Windows":
    btstyle.theme_use("vista")
elif platform.system == "Darwin":
    btstyle.theme_use("aqua")

# defines the calculation history
history = list()

#defines the history labels
hist  =  t.Label(window)
hist.config(text='History')
hist.place(anchor='center', x=545, y=25)

hr1v = t.StringVar()
hr1v.set('No history')
histrec1 = t.Label(window)
histrec1.config(textvariable=hr1v)
histrec1.place(anchor='center', x=545, y=50)

hr2v = t.StringVar()
hr2v.set('')
histrec2 = t.Label(window)
histrec2.config(textvariable=hr2v)
histrec2.place(anchor='center', x=545, y=100)

hr3v = t.StringVar()
hr3v.set('')
histrec3 = t.Label(window)
histrec3.config(textvariable=hr3v)
histrec3.place(anchor='center', x=545, y=150)

hr4v = t.StringVar()
hr4v.set('')
histrec4 = t.Label(window)
histrec4.config(textvariable=hr4v)
histrec4.place(anchor='center', x=545, y=200)

hr5v = t.StringVar()
hr5v.set('')
histrec5 = t.Label(window)
histrec5.config(textvariable=hr5v)
histrec5.place(anchor='center', x=545, y=250)

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

# The version window
def ver():
    ver = t.Toplevel()
    ver.resizable(0,0)
    ver.title('About')
    ver.iconbitmap("./assets/icon.ico")
    ver.geometry('320x260')
   
    verlabel = ttk.Label(ver)
    verlabel.config(text='V1.2-tr2(English)', image=logo, font=AppleGaramond16, compound='top')
    verlabel.place(anchor='center', x=160, y=100)

    verexit = ttk.Button(ver)
    verexit.config(text='Got it!', style='BW.TButton', command=ver.destroy)
    verexit.place(anchor='center', x=160, y=160)

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
menubar.add_cascade(label='Settings', menu=settings_menu)
window.config(menu=menubar)

# function that controls the indicator

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

def appendChar(val: str, charType: str, ):
    global status
    
    if charType == 'Num':
        indicator_value.set(f'{indicator_value.get()}{val}')
        status = 'symbol'
    elif charType == "Sym" and status == 'symbol':
        indicator_value.set(f'{indicator_value.get()}{val}')
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
    DoErrorAppear = False
    result = indicator_value.get()
    result = result.replace('×','*')
    result = result.replace('÷','/')
    result = result.replace('²','**2')
    try:
        indicator_value.set(eval(result))
    except ZeroDivisionError:
        indicator_value.set('')
        tmb.showwarning(title='error', message='Cannot divide a number by zero')
        DoErrorAppear = True
    except SyntaxError:
        indicator_value.set('')
        tmb.showwarning(title='error', message='There are syntax error(s)')
        DoErrorAppear = True
    result = indicator_value.get()
    if result[(len(result) - 2):] == '.0' :
        indicator_value.set(result[:(len(result) - 2)])
    elif len(result) < 12:
        indicator_value.set(result)
    elif '.' in result:
        indicator_value.set(result[:(len(result) - 6)])

    if DoErrorAppear == False:
        history.append(result)
        hr1v.set(str(history[len(history)-1]))
       
        if len(history)-2 >= 0:
            hr2v.set(str(history[len(history)-2]))
        if len(history)-3 >= 0:
            hr3v.set(str(history[len(history)-3]))
        if len(history)-4 >= 0:
            hr4v.set(str(history[len(history)-4]))
        if len(history)-5 >= 0:
            hr5v.set(str(history[len(history)-5]))
    

# create the indicator
indicator = t.Label(window)
indicator.config(textvariable=indicator_value, height=2, width=62,  \
                bd=3, relief='solid')
indicator.place(anchor='center', x=240, y=33)

# create the frame for helding the main buttons
mainFrame = t.Frame(window)
mainFrame.config(height=242, width=500)
mainFrame.place(anchor='center', x=260, y=300)


# create the buttons
button1 = ttk.Button(mainFrame)
button1.config(text='\n1\n', width=12, command=lambda val='1' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button1.place(anchor='center', x=50, y=30)

button2 = ttk.Button(mainFrame)
button2.config(text='\n2\n', width=12, command=lambda val='2' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button2.place(anchor='center', x=150, y=30)

button3 = ttk.Button(mainFrame)
button3.config(text='\n3\n', width=12, command=lambda val='3' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button3.place(anchor='center', x=250, y=30)


button4 = ttk.Button(mainFrame)
button4.config(text='\n4\n', width=12, command=lambda val='4' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button4.place(anchor='center', x=50, y=90)

button5 = ttk.Button(mainFrame)
button5.config(text='\n5\n', width=12, command=lambda val='5' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button5.place(anchor='center', x=150, y=90)

button6 = ttk.Button(mainFrame)
button6.config(text='\n6\n', width=12, command=lambda val='6' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button6.place(anchor='center', x=250, y=90)


button7 = ttk.Button(mainFrame)
button7.config(text='\n7\n', width=12, command=lambda val='7' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button7.place(anchor='center', x=50, y=150)

button8 = ttk.Button(mainFrame)
button8.config(text='\n8\n', width=12, command=lambda val='8' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button8.place(anchor='center', x=150, y=150)

button9 = ttk.Button(mainFrame)
button9.config(text='\n9\n', width=12, command=lambda val='9' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button9.place(anchor='center', x=250, y=150)

button0 = ttk.Button(mainFrame)
button0.config(text='\n0\n', width=12, command=lambda val='0' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button0.place(anchor='center', x=150, y=210)

buttonLB = ttk.Button(mainFrame)
buttonLB.config(text='\n(\n', width=5, command=appendLB, style="BW.TButton")
buttonLB.place(anchor='center', x=25, y=210)

buttonRB = ttk.Button(mainFrame)
buttonRB.config(text='\n)\n', width=5, command=appendRB, style="BW.TButton")
buttonRB.place(anchor='center', x=75, y=210)

buttonAC = ttk.Button(mainFrame)
buttonAC.config(text='\nAC\n', width=12, command=clear, style="BW.TButton")
buttonAC.place(anchor='center', x=450, y=30)

buttonC = ttk.Button(mainFrame)
buttonC.config(text='\nC\n', width=12, command=delete, style="BW.TButton")
buttonC.place(anchor='center', x=450, y=90)

button_equal = ttk.Button(mainFrame)
button_equal.config(text='\n=\n', width=12, command=calculate, style="BW.TButton")
button_equal.place(anchor='center', x=250, y=210)

button_plus = ttk.Button(mainFrame)
button_plus.config(text='\n+\n', width=12, command=lambda val='+', charType = "Sym": appendChar(val, charType), style="BW.TButton")
button_plus.place(anchor='center', x=350, y=30)

button_minus = ttk.Button(mainFrame)
button_minus.config(text='\n-\n', width=12, command=lambda val='-', charType = "Sym": appendChar(val, charType), style="BW.TButton")
button_minus.place(anchor='center', x=350, y=90)

button_mutipliation = ttk.Button(mainFrame)
button_mutipliation.config(text='\n×\n', width=12, command=lambda val='×', charType = "Sym": appendChar(val, charType), style="BW.TButton")
button_mutipliation.place(anchor='center', x=350, y=150)

button_divition = ttk.Button(mainFrame)
button_divition.config(text='\n÷\n', width=12, command=lambda val='÷', charType = "Sym": appendChar(val, charType), style="BW.TButton")
button_divition.place(anchor='center', x=350, y=210)

buttonDP = ttk.Button(mainFrame)
buttonDP.config(text='\n.\n', width=12, command=lambda val='.' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
buttonDP.place(anchor='center', x=450, y=150)

button_pos2Neg = ttk.Button(mainFrame)
button_pos2Neg.config(text='\n(-\n', width=12, command=pos2Neg, style="BW.TButton")
button_pos2Neg.place(anchor='center', x=450, y=210)

button_square = ttk.Button(window)
button_square.config(text='²', width=8, command=lambda val='²', charType = "Num": appendChar(val, charType), style="BW.TButton" )
button_square.place(anchor='center', x=55, y=98)

window.mainloop()