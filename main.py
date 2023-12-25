from tkinter import *
window= Tk()
b1 = PhotoImage(file='1.png')
b2 = PhotoImage(file='2.png')
b3 = PhotoImage(file='3.png')
b4 = PhotoImage(file='4.png')
b5 = PhotoImage(file='5.png')
b6 = PhotoImage(file='6.png')
b7 = PhotoImage(file='7.png')
b8 = PhotoImage(file='8.png')
b9 = PhotoImage(file='9.png')
btimes = PhotoImage(file='hahaha.png')
bdivided = PhotoImage(file='divided.png')
bminus = PhotoImage(file='minus.png')
bplus = PhotoImage(file='plus.png')
bpr = PhotoImage(file='klamma right.png')
bpl = PhotoImage(file='klamma left.png')
b1dot = PhotoImage(file='dot.png')
b0 = PhotoImage(file='0.png')
equal = PhotoImage(file='equals.png')

clear = PhotoImage(file='clear.png')
plusSlashMinus = PhotoImage(file='plusslashminus.png')
percent = PhotoImage(file='percent.png')

label = Label(window, text='', font=('Consolas', 20), width=30)
label.pack()

frame = Frame(window)
frame.pack()


def pressed(num):
    global text_on_top
    text_on_top = text_on_top + str(num)
    label.config(text=str(text_on_top))


def eveluate():
    try:
        global text_on_top
        evaluated_text = eval(text_on_top)
        label.config(text=str(evaluated_text))
        text_on_top = str(evaluated_text)
    except SyntaxError:
        label.config(text='SYNTAX ERROR!')


def cleared():
    global text_on_top
    text_on_top = ''
    label.config(text=text_on_top)


def turn():
    global text_on_top
    try:
        text_on_top = int(text_on_top)
        text_on_top = text_on_top * -1
        label.config(text=str(text_on_top))
        text_on_top = str(text_on_top)
    except ValueError:

        label.config(text="Sorry can't do that yet!")


def percentage():
    global text_on_top
    text_on_top = int(text_on_top)
    text_on_top = text_on_top / 100
    label.config(text=str(text_on_top))
    text_on_top = str(text_on_top)


text_on_top = ''

buttonclear = Button(frame, image=clear, borderwidth=0, command=lambda: cleared())
buttonclear.grid(row=0, column=0)
turntoopposite = Button(frame, image=plusSlashMinus, borderwidth=0, command=lambda: turn())
turntoopposite.grid(row=0, column=1)
button_percent = Button(frame, image=percent, borderwidth=0, command=lambda: percentage())
button_percent.grid(row=0, column=2)

button1 = Button(frame, image=b1, borderwidth=0, command=lambda: pressed(1))
button1.grid(row=1, column=0)
button2 = Button(frame, image=b2, borderwidth=0, command=lambda: pressed(2))
button2.grid(row=1, column=1)
button3 = Button(frame, image=b3, borderwidth=0, command=lambda: pressed(3))
button3.grid(row=1, column=2)
button4 = Button(frame, image=b4, borderwidth=0, command=lambda: pressed(4))
button4.grid(row=2, column=0)
button5 = Button(frame, image=b5, borderwidth=0, command=lambda: pressed(5))
button5.grid(row=2, column=1)
button6 = Button(frame, image=b6, borderwidth=0, command=lambda: pressed(6))
button6.grid(row=2, column=2)
button7 = Button(frame, image=b7, borderwidth=0, command=lambda: pressed(7))
button7.grid(row=3, column=0)
button8 = Button(frame, image=b8, borderwidth=0, command=lambda: pressed(8))
button8.grid(row=3, column=1)
button9 = Button(frame, image=b9, borderwidth=0, command=lambda: pressed(9))
button9.grid(row=3, column=2)
button0 = Button(frame, image=b0, borderwidth=0, command=lambda: pressed(0))
button0.grid(row=4, column=0, columnspan=2)

buttontimes = Button(frame, image=btimes, borderwidth=0, command=lambda: pressed('*'))
buttontimes.grid(row=1, column=3)
buttondivided = Button(frame, image=bdivided, borderwidth=0, command=lambda: pressed('/'))
buttondivided.grid(row=0, column=3)
buttonplus = Button(frame, image=bplus, borderwidth=0, command=lambda: pressed('+'))
buttonplus.grid(row=3, column=3)
buttonminus = Button(frame, image=bminus, borderwidth=0, command=lambda: pressed('-'))
buttonminus.grid(row=2, column=3)
button_dot = Button(frame, image=b1dot, borderwidth=0, command=lambda: pressed('.'))
button_dot.grid(row=4, column=2)
equal_sign = Button(frame, image=equal, borderwidth=0, command=lambda: eveluate())
equal_sign.grid(row=4, column=3)



def buttonpress(event):
    global text_on_top
    text_on_top = str(text_on_top)
    text_on_top = text_on_top + str(event)
    label.config(text=text_on_top)
    print(event)

def deleteKey(event):
    try:
        global text_on_top
        deletedText=text_on_top.rstrip(text_on_top[-1])
        text_on_top = deletedText
        label.config(text=text_on_top)
    except IndexError:
        label.config(text='There is no text!')


window.resizable(False,False)
window.bind('<Key-1>',lambda event :buttonpress('1'))
window.bind('<Key-2>',lambda event :buttonpress('2'))
window.bind('<Key-3>',lambda event :buttonpress('3'))
window.bind('<Key-4>',lambda event :buttonpress('4'))
window.bind('<Key-5>',lambda event :buttonpress('5'))
window.bind('<Key-6>',lambda event :buttonpress('6'))
window.bind('<Key-7>',lambda event :buttonpress('7'))
window.bind('<Key-8>',lambda event :buttonpress('8'))
window.bind('<Key-9>',lambda event :buttonpress('9'))
window.bind('<Key-0>',lambda event :buttonpress('0'))


window.bind('<BackSpace>',deleteKey)





window.mainloop()