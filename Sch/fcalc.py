import os
import sys
from platform import system
# This environment flag MUST be set before pyglet is imported
if system() == "Linux":
    os.environ["PYGLET_HEADLESS"] = "1"
import pyglet as pglt
import tkinter as t
from tkinter import ttk
from tkinter import messagebox as tmb
import tkinter.font as tfont
import ttkthemes as ttkt
from math import sqrt
from sys import version_info

# defines the current software version (need to be constantly changed every time version number changes)
verMajor = 1
verMinor = 2
verPatch = 0
verAttr = "Beta1"

sqrt(1)

# setting the locale dictionary

window = t.Tk()
window.resizable(0,0)
window.geometry('550x500')
window.title("Frogzen Calculator")
icon_files = ['./assets/icon-1.png', './assets/icon-2.png', './assets/icon-3.png', \
              './assets/icon-4.png','./assets/icon-5.png',]
icons = []
for path in icon_files:
    if os.path.exists(path):
        icons.append(t.PhotoImage(file=path))
window.iconphoto(False, *icons)

if system() == "Windows":
    currButtonWidth = 12
elif system() == "Linux":
    currButtonWidth = 10

# imports the fonts from ./font folder
pglt.options['win32_gdi_font'] = True
pglt.font.add_file('./fonts/AppleGaramond.ttf')
AppleGaramond11 = tfont.Font(family="AppleGaramond", size=11)
AppleGaramond16 = tfont.Font(family="AppleGaramond", size=16)

# defines the style for main buttons
btstyle = ttkt.ThemedStyle()
btstyle.configure(style="BW.TButton", foreground="black")
if system() == "Windows":
    btstyle.set_theme("vista")
elif system() == "Darwin":
    btstyle.set_theme("aqua")
elif system() == "Linux":
    btstyle.set_theme("adapta")
window.configure(background=btstyle.lookup("TFrame", "background"))

# defines the calculation history
history = list()

# set the indicator value
indicator_value = t.StringVar()
indicator_value.set('')

# status
status = 'num'
isNeg = False

#define the logo
logo = t.PhotoImage(file='./assets/logo.png')

# memory var declaration
memory = 0

def doNothing():
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
                tmb.showwarning(title='故障', message='记忆为空')

def mem_minus():
    try:
        global memory
        memory -= int(indicator_value.get())
    except ValueError:
            try:
                memory -= float(indicator_value.get())
            except ValueError:
                indicator_value.set('')
                tmb.showwarning(title='故障', message='记忆为空')

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
    verWin = t.Toplevel()
    verWin.configure(background=btstyle.lookup("TFrame", "background"))
    verWin.resizable(False,False)
    verWin.title("关于")
    verWin.iconphoto(False, *icons)
    verWin.geometry('320x260')
    
    verlabel = ttk.Label(verWin)
    verlabel.config(text=f'V{verMajor}.{verMinor}.{verPatch}-{verAttr}(简体中文)', image=logo, font=AppleGaramond16, compound='top')
    verlabel.place(anchor='center', x=160, y=100)

    pyverlabel = ttk.Label(verWin)
    pyverlabel.config(text=f'Python {version_info[0]}.{version_info[1]}.{version_info[2]} 在 {system()} 上' \
                      ,font=AppleGaramond11)        # version_info[0] is major, version_info[1] is minor, version_info[2] is patch
    pyverlabel.place(anchor='center', x=160, y=150)

    verexit = ttk.Button(verWin)
    verexit.config(text='明白了！', style='BW.TButton', command=verWin.destroy)
    verexit.place(anchor='center', x=160, y=200)

def historyWin():
    histWin = t.Toplevel()
    histWin.configure(background=btstyle.lookup("TFrame", "background"))
    histWin.resizable(False,False)
    histWin.title("计算历史")
    histWin.iconphoto(False, *icons)
    histWin.geometry('400x600')

    global history
    history.reverse()
   
    i = 0
    if len(history) != 0:
        for results in history:
            print(results)
            histrec = ttk.Label(histWin)
            histrec.config(text=f'{i+1}. {results}', font=AppleGaramond11)
            histrec.place(anchor='center', x=200, y=12 + 25 * i)
            if i == 23 :
                break
        
            i += 1
    else:
        histrec = ttk.Label(histWin)
        histrec.config(text="No history", font=AppleGaramond11)
        histrec.place(anchor='center', x=200, y=50 + 30 * i)

    history.reverse()

def keyMapWin():
    keyMapWindow = t.Toplevel()
    keyMapWindow.configure(background=btstyle.lookup("TFrame", "background"))
    keyMapWindow.resizable(False,False)
    keyMapWindow.iconphoto(False, *icons)
    keyMapWindow.geometry("400x500")

    keyMapLabel = ttk.Label(keyMapWindow)
    with open("./resource/keybind.txt", "r", encoding="utf-8") as keyBindText:
        i = 0
        keybind = ""
        for lines in keyBindText.readlines():
            keybind = f"{keybind}{lines}"

    keyMapLabel.config(text=keybind, font=AppleGaramond16)
    keyMapLabel.place(anchor='center', x=200, y=250)

# defines the button to history window
hist = ttk.Button(window)
hist.config(text='计算历史', style="BW.TButton", command=historyWin)
hist.place(anchor='center', x=460, y=98)

bg_color = btstyle.lookup("TFrame", "background")
fg_color = btstyle.lookup("TLabel", "foreground")
active_bg = btstyle.lookup("TEntry", "selectbackground", ["focus"])
active_fg = btstyle.lookup("TEntry", "selectforeground", ["focus"])
dis_fg = btstyle.lookup("TEntry", "foreground", ["disabled"])

# menubar and menu code
menubar = t.Menu(window)
menubar.configure(background=bg_color, foreground=fg_color, activebackground=active_bg, activeforeground=active_fg, \
    font=AppleGaramond11, borderwidth=0, activeborderwidth=0) 

memory_menu = t.Menu(menubar, tearoff=0)
memory_menu.configure(background=bg_color, foreground=fg_color, activebackground=active_bg, activeforeground=active_fg, \
    disabledforeground=dis_fg, font=AppleGaramond11, borderwidth=1, activeborderwidth=0)

memory_menu.add_command(label="M+", command=mem_plus)
memory_menu.add_command(label="M-", command=mem_minus)
memory_menu.add_command(label="MR", command=get_mem)
memory_menu.add_command(label="MC", command=clear_mem)
menubar.add_cascade(label="记忆", menu=memory_menu)

help_menu = t.Menu(menubar, tearoff=0)
help_menu.configure(background=bg_color, foreground=fg_color, activebackground=active_bg, activeforeground=active_fg,
    disabledforeground=dis_fg, font=AppleGaramond11, borderwidth=1, activeborderwidth=0)

help_menu.add_command(label='版本', command=ver)
help_menu.add_command(label='键盘快捷键', command=keyMapWin)
help_menu.add_command(label="退出", command=window.quit)

menubar.add_cascade(label="帮助", menu=help_menu)
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
    if not isNeg:
        indicator_value.set(f'{indicator_value.get()}(-')
        isNeg = True

def appendSqrt():
    indicator_value.set(f'{indicator_value.get()}sqrt(')


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
    result = result.replace('³','**3')
    result = result.replace('^','**')
    try:
        indicator_value.set(eval(result))
    except ZeroDivisionError:
        indicator_value.set('')
        tmb.showwarning(title='故障', message='不能除以零')
        DoErrorAppear = True
    except SyntaxError:
        indicator_value.set('')
        tmb.showwarning(title='故障', message='格式不正确')
        DoErrorAppear = True
    result = indicator_value.get()
    if result[(len(result) - 2):] == '.0' :
        indicator_value.set(result[:(len(result) - 2)])
    elif len(result) < 12:
        indicator_value.set(result)
    elif '.' in result:
        indicator_value.set(result[:(len(result) - 6)])

    if not DoErrorAppear:
        global history
        history.append(result)
    
# create the indicator
indicator = t.Label(window)
indicator.config(textvariable=indicator_value, height=2, width=60,  \
                bd=3, relief='solid')
indicator.place(anchor='center', x=275, y=33)

# create the frame for holding the main buttons
mainFrame = t.Frame(window)
mainFrame.config(height=320, width=550, bg=btstyle.lookup("TFrame", "background"))
mainFrame.place(anchor='center', x=280,  y=300)

# bind keypress to inputs
window.bind('<KeyPress-1>', lambda p, val='1' ,charType = 'Num': appendChar(val, charType))
window.bind('<KeyPress-2>', lambda p, val='2' ,charType = 'Num': appendChar(val, charType))
window.bind('<KeyPress-3>', lambda p, val='3' ,charType = 'Num': appendChar(val, charType))

window.bind('<KeyPress-4>', lambda p, val='4' ,charType = 'Num': appendChar(val, charType))
window.bind('<KeyPress-5>', lambda p, val='5' ,charType = 'Num': appendChar(val, charType))
window.bind('<KeyPress-6>', lambda p, val='6' ,charType = 'Num': appendChar(val, charType))
window.bind('<KeyPress-7>', lambda p, val='7' ,charType = 'Num': appendChar(val, charType))
window.bind('<KeyPress-8>', lambda p, val='8' ,charType = 'Num': appendChar(val, charType))
window.bind('<KeyPress-9>', lambda p, val='9' ,charType = 'Num': appendChar(val, charType))

window.bind('<KeyPress-0>', lambda p, val='0' ,charType = 'Num': appendChar(val, charType))

window.bind('<parenleft>', lambda p: appendLB())
window.bind('<parenright>', lambda p: appendRB())

window.bind('<BackSpace>', lambda p: delete())
window.bind('<Delete>', lambda p: clear())

window.bind('<plus>', lambda p, val='+' ,charType = 'Sym': appendChar(val, charType))
window.bind('<minus>', lambda p, val='-' ,charType = 'Sym': appendChar(val, charType))
window.bind('<asterisk>', lambda p, val='×' ,charType = 'Sym': appendChar(val, charType))
window.bind('<slash>', lambda p, val='÷' ,charType = 'Sym': appendChar(val, charType))
window.bind('<equal>', lambda p: calculate())
window.bind('<Return>', lambda p: calculate())

window.bind('<period>', lambda p, val='.' ,charType = 'Num': appendChar(val, charType))

window.bind('<Shift-at>', lambda p, val='²', charType = "Num": appendChar(val, charType)) # Shift + 2
window.bind('<Shift-numbersign>', lambda p, val='³', charType = "Num": appendChar(val, charType)) # Shift + 3
window.bind('<Shift-Q>', lambda p: appendSqrt())

window.bind('<Shift-asciicircum>', lambda p, val='^' ,charType = 'Sym': appendChar(val, charType)) # Shift + 6

# create the buttons
button1 = ttk.Button(mainFrame)
button1.config(text='\n1\n', width=currButtonWidth, command=lambda val='1' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button1.place(anchor='center', x=50, y=30)

button2 = ttk.Button(mainFrame)
button2.config(text='\n2\n', width=currButtonWidth, command=lambda val='2' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button2.place(anchor='center', x=160, y=30)

button3 = ttk.Button(mainFrame)
button3.config(text='\n3\n', width=currButtonWidth, command=lambda val='3' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button3.place(anchor='center', x=270, y=30)


button4 = ttk.Button(mainFrame)
button4.config(text='\n4\n', width=currButtonWidth, command=lambda val='4' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button4.place(anchor='center', x=50, y=110)

button5 = ttk.Button(mainFrame)
button5.config(text='\n5\n', width=currButtonWidth, command=lambda val='5' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button5.place(anchor='center', x=160, y=110)

button6 = ttk.Button(mainFrame)
button6.config(text='\n6\n', width=currButtonWidth, command=lambda val='6' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button6.place(anchor='center', x=270, y=110)


button7 = ttk.Button(mainFrame)
button7.config(text='\n7\n', width=currButtonWidth, command=lambda val='7' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button7.place(anchor='center', x=50, y=190)

button8 = ttk.Button(mainFrame)
button8.config(text='\n8\n', width=currButtonWidth, command=lambda val='8' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button8.place(anchor='center', x=160, y=190)

button9 = ttk.Button(mainFrame)
button9.config(text='\n9\n', width=currButtonWidth, command=lambda val='9' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button9.place(anchor='center', x=270, y=190)

button0 = ttk.Button(mainFrame)
button0.config(text='\n0\n', width=currButtonWidth, command=lambda val='0' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
button0.place(anchor='center', x=160, y=270)

buttonLB = ttk.Button(mainFrame)
buttonLB.config(text='\n(\n', width=4, command=appendLB, style="BW.TButton")
buttonLB.place(anchor='center', x=25, y=270)

buttonRB = ttk.Button(mainFrame)
buttonRB.config(text='\n)\n', width=4, command=appendRB, style="BW.TButton")
buttonRB.place(anchor='center', x=75, y=270)

buttonAC = ttk.Button(mainFrame)
buttonAC.config(text='\nAC\n', width=currButtonWidth, command=clear, style="BW.TButton")
buttonAC.place(anchor='center', x=490, y=30)

buttonDEL = ttk.Button(mainFrame)
buttonDEL.config(text='\nDEL\n', width=currButtonWidth, command=delete, style="BW.TButton")
buttonDEL.place(anchor='center', x=490, y=110)

button_equal = ttk.Button(mainFrame)
button_equal.config(text='\n=\n', width=currButtonWidth, command=calculate, style="BW.TButton")
button_equal.place(anchor='center', x=270, y=270)

button_plus = ttk.Button(mainFrame)
button_plus.config(text='\n+\n', width=currButtonWidth, command=lambda val='+', charType = "Sym": appendChar(val, charType), style="BW.TButton")
button_plus.place(anchor='center', x=380, y=30)

button_minus = ttk.Button(mainFrame)
button_minus.config(text='\n-\n', width=currButtonWidth, command=lambda val='-', charType = "Sym": appendChar(val, charType), style="BW.TButton")
button_minus.place(anchor='center', x=380, y=110)

button_multiplication = ttk.Button(mainFrame)
button_multiplication.config(text='\n×\n', width=currButtonWidth, command=lambda val='×', charType ="Sym": appendChar(val, charType), style="BW.TButton")
button_multiplication.place(anchor='center', x=380, y=190)

button_division = ttk.Button(mainFrame)
button_division.config(text='\n÷\n', width=currButtonWidth, command=lambda val='÷', charType ="Sym": appendChar(val, charType), style="BW.TButton")
button_division.place(anchor='center', x=380, y=270)

buttonDP = ttk.Button(mainFrame)
buttonDP.config(text='\n.\n', width=currButtonWidth, command=lambda val='.' ,charType = 'Num': appendChar(val, charType), style="BW.TButton")
buttonDP.place(anchor='center', x=490, y=190)

button_pos2Neg = ttk.Button(mainFrame)
button_pos2Neg.config(text='\n(-\n', width=currButtonWidth, command=pos2Neg, style="BW.TButton")
button_pos2Neg.place(anchor='center', x=490, y=270)

button_square = ttk.Button(window)
button_square.config(text='²', width=8, command=lambda val='²', charType = "Num": appendChar(val, charType), style="BW.TButton" )
button_square.place(anchor='center', x=55, y=98)

button_cube = ttk.Button(window)
button_cube.config(text='³', width=8, command=lambda val='³', charType = "Num": appendChar(val, charType), style="BW.TButton" )
button_cube.place(anchor='center', x=145, y=98)

button_sqrt = ttk.Button(window)
button_sqrt.config(text='√', width=8, command=appendSqrt, style="BW.TButton" )
button_sqrt.place(anchor='center', x=235, y=98)

button_npower = ttk.Button(window)
button_npower.config(text='^', width=8, command=lambda val='^', charType = "Sym": appendChar(val, charType), style="BW.TButton" )
button_npower.place(anchor='center', x=325, y=98)

window.mainloop()