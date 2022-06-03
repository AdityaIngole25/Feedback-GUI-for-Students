# Note : Import Logo File 'logo.gif' To The Same Directory where the Program File is located...
# OR Add '#' infront of 'logo' , 'logolabel' & 'logolabel.grid' to run the program without any error...
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
#root.configure(bg = '#87939A')
frame_header = ttk.Frame(root)
frame_header.pack()
logo = PhotoImage(file='logo.gif').subsample(4, 4)
logolabel = ttk.Label(frame_header, text='logo', image=logo)
logolabel.grid(row=0, column=0, rowspan=2)
headerlabel = ttk.Label(frame_header, text=" Vasantdada Patil Pratishthan's College of Engineering & Visual Arts" , foreground='maroon',
                        font=('Arial', 24))
headerlabel.grid(row=0, column=1)
messagelabel = ttk.Label(frame_header,
                         text='Please Give your feedBack below.\nIt will help us to know in which section we need to take care of.',
                         foreground='purple', font=('Arial', 20))
messagelabel.grid(row=1, column=1)

frame_content = ttk.Frame(root)
frame_content.pack()
# def submit():
#     username = entry_name.get()
#     print(username)
myvar = StringVar()
var = StringVar()
# cmnt= StringVar()
namelabel = ttk.Label(frame_content, text=" STUDENTS'  NAME ")
namelabel.grid(row=0, column=0, padx=5, sticky='sw')
entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar)
entry_name.grid(row=1, column=0)

emaillabel = ttk.Label(frame_content, text='Email')
emaillabel.grid(row=0, column=1, sticky='sw')
entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=var)
entry_email.grid(row=1, column=1)

commentlabel = ttk.Label(frame_content, text='Comment', font=('Arial', 10))
commentlabel.grid(row=2, column=0, sticky='sw')
textcomment = Text(frame_content, width=55, height=10)
textcomment.grid(row=3, column=0, columnspan=2)


textcomment.config(wrap ='word')
# def clear():
#     textcomment.delete(1.0,'end')
def clear():
    global entry_name
    global entry_email
    global textcomment
    messagebox.showinfo(title='clear', message='Do you want to clear?')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)


def submit():
    global entry_name
    global entry_email
    global textcomment
    print('Name:{}'.format(myvar.get()))
    print('Email:{}'.format(var.get()))
    print('Comment:{}'.format(textcomment.get(1.0, END)))
    messagebox.showinfo(title='Submit', message='Your Comments Submited')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)


submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=4, column=0, sticky='e')
clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=4, column=1, sticky='w')

mainloop()