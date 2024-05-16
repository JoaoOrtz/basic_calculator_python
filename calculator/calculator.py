from tkinter import *
from tkinter import ttk

#Entry of values
def entryValues(key):
    if key >= '0' and key <= '9' or key == '(' or key == ')' or key == '.':
        entrance2.set(entrance2.get() + key)

    if key == '*' or key == '/' or key == '+' or key == '-':
        if key == '*':
            entrance1.set(entrance2.get() + '*')
        elif key == '/':
            entrance1.set(entrance2.get() + '/')
        elif key == '+':
            entrance1.set(entrance2.get() + '+')
        elif key == '-':
            entrance1.set(entrance2.get() + '-')
            
        entrance2.set('')

    if key == '=':
        entrance1.set(entrance1.get() + entrance2.get())
        result = eval(entrance1.get())
        entrance2.set(result)

#Deletion of a number
def delete(*args):
    start = 0
    end = len(entrance2.get())
    entrance2.set(entrance2.get()[start:end - 1]) 

#Delete all numbers
def deleteAll(*args):
    entrance1.set('')
    entrance2.set('')

#enter values from the keyboard
def enterValuesKeyboard(event):
    key = event.char

    if key >= '0' and key <= '9' or key == '(' or key == ')' or key == '.':
        entrance2.set(entrance2.get() + key)

    if key == '*' or key == '/' or key == '+' or key == '-':
        if key == '*':
            entrance1.set(entrance2.get() + '*')
        elif key == '/':
            entrance1.set(entrance2.get() + '/')
        elif key == '+':
            entrance1.set(entrance2.get() + '+')
        elif key == '-':
            entrance1.set(entrance2.get() + '-')
            
        entrance2.set('')

    if key == '=':
        entrance1.set(entrance1.get() + entrance2.get())
        result = eval(entrance1.get())
        entrance2.set(result)

#Window creation
root = Tk()
root.title("Calculator")
root.geometry("+500+80")
#Window adaptation
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Style
style = ttk.Style()
style.theme_use('clam')
style.configure('mainframe.TFrame', background="#DBDBDB")

mainframe = ttk.Frame(root, style='mainframe.TFrame')
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))
#Adaptation of window columns
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
#Adaptation of window rows
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)

#label1 styling
style_label1 = ttk.Style()
style_label1.configure('Label1.TLabel', font="arial 25", anchor="e")

#Label1
entrance1 = StringVar()
label_entrance1 = ttk.Label(mainframe, textvariable=entrance1, style="Label1.TLabel")
label_entrance1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))

#label2 styling
style_label2 = ttk.Style()
style_label2.configure('Label2.TLabel', font="arial 40", anchor="e")

#Label2
entrance2 = StringVar()
label_entrance2 = ttk.Label(mainframe, textvariable=entrance2, style="Label2.TLabel")
label_entrance2.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))

#Number buttons styling
style_btn_numbers = ttk.Style()
style_btn_numbers.configure('btn_number.TButton', font="arial 22", width=5, background="#FFFFFF", relief="flast")
style_btn_numbers.map('btn_number.TButton', foreground=[('active','#FFFFFF')], background=[('active','#545454')])

#Number buttons
btn0 = ttk.Button(mainframe, text=0, style="btn_number.TButton", command=lambda: entryValues('0'))
btn1 = ttk.Button(mainframe, text=1, style="btn_number.TButton", command=lambda: entryValues('1'))
btn2 = ttk.Button(mainframe, text=2, style="btn_number.TButton", command=lambda: entryValues('2'))
btn3 = ttk.Button(mainframe, text=3, style="btn_number.TButton", command=lambda: entryValues('3'))
btn4 = ttk.Button(mainframe, text=4, style="btn_number.TButton", command=lambda: entryValues('4'))
btn5 = ttk.Button(mainframe, text=5, style="btn_number.TButton", command=lambda: entryValues('5'))
btn6 = ttk.Button(mainframe, text=6, style="btn_number.TButton", command=lambda: entryValues('6'))
btn7 = ttk.Button(mainframe, text=7, style="btn_number.TButton", command=lambda: entryValues('7'))
btn8 = ttk.Button(mainframe, text=8, style="btn_number.TButton", command=lambda: entryValues('8'))
btn9 = ttk.Button(mainframe, text=9, style="btn_number.TButton", command=lambda: entryValues('9'))

#Delete button styling
style_btn_delete = ttk.Style()
style_btn_delete.configure('btn_delete.TButton', font="arial 22", width=5, background="#72c65f",relief="flast")
style_btn_delete.map('btn_delete.TButton', foreground=[('active','#FFFFFF')], background=[('active','#e4482c')])

#Assignment buttons styling
style_btn_assignment = ttk.Style()
style_btn_assignment.configure('btn_assignment.TButton', font="arial 22", width=5, background="#72c65f", relief="flast")
style_btn_assignment.map('btn_assignment.TButton', foreground=[('active','#FFFFFF')], background=[('active','#545454')])

#Equal buttons styling
style_btn_equal = ttk.Style()
style_btn_equal.configure('btn_equal.TButton', font="arial 22", width=5, background="#72c65f", relief="flast")
style_btn_equal.map('btn_equal.TButton', foreground=[('active','#FFFFFF')], background=[('active','#feff48')])

#Assignment buttons
btn_delete = ttk.Button(mainframe, text=chr(9003), style="btn_delete.TButton", command=lambda: delete())
btn_delete_all = ttk.Button(mainframe, text="C", style="btn_delete.TButton", command=lambda: deleteAll())
btn_parenthesis1 = ttk.Button(mainframe, text="(", style="btn_assignment.TButton", command=lambda: entryValues('('))
btn_parenthesis2 = ttk.Button(mainframe, text=")", style="btn_assignment.TButton", command=lambda: entryValues(')'))
btn_spot = ttk.Button(mainframe, text=".", style="btn_assignment.TButton", command=lambda: entryValues('.'))
btn_equal = ttk.Button(mainframe, text="=", style="btn_equal.TButton", command=lambda: entryValues('='))

#Basic operations buttons
btn_addittion = ttk.Button(mainframe, text="+", style="btn_assignment.TButton", command=lambda: entryValues('+'))
btn_subtraction = ttk.Button(mainframe, text="-", style="btn_assignment.TButton", command=lambda: entryValues('-'))
btn_multiplication = ttk.Button(mainframe, text="x", style="btn_assignment.TButton", command=lambda: entryValues('*'))
btn_division = ttk.Button(mainframe, text=chr(247), style="btn_assignment.TButton", command=lambda: entryValues('/'))

#Button placements on the screen
#Row 1
btn_parenthesis1.grid(column=0, row=2, sticky=(W, N, E, S))
btn_parenthesis2.grid(column=1, row=2, sticky=(W, N, E, S))
btn_delete_all.grid(column=2, row=2, sticky=(W, N, E, S))
btn_delete.grid(column=3, row=2, sticky=(W, N, E, S))
#Row 2
btn7.grid(column=0, row=3, sticky=(W, N, E, S))
btn8.grid(column=1, row=3, sticky=(W, N, E, S))
btn9.grid(column=2,row=3, sticky=(W, N, E, S))
btn_division.grid(column=3, row=3, sticky=(W, N, E, S))
#Row 3
btn4.grid(column=0, row=4, sticky=(W, N, E, S))
btn5.grid(column=1, row=4, sticky=(W, N, E, S))
btn6.grid(column=2, row=4, sticky=(W, N, E, S))
btn_multiplication.grid(column=3, row=4, sticky=(W, N, E, S))
#Row 4
btn1.grid(column=0, row=5, sticky=(W, N, E, S))
btn2.grid(column=1, row=5, sticky=(W, N, E, S))
btn3.grid(column=2, row=5, sticky=(W, N, E, S))
btn_addittion.grid(column=3, row=5, sticky=(W, N, E, S))
#Row 5
btn_spot.grid(column=0, row=6, sticky=(W, N, E, S))
btn0.grid(column=1, row=6, sticky=(W, N, E, S))
btn_equal.grid(column=2, row=6, sticky=(W, N, E, S))
btn_subtraction.grid(column=3, row=6, sticky=(W, N, E, S))

#Separation
for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.bind('<Key>', enterValuesKeyboard)
root.bind('<KeyPress -b>', delete)
root.bind('<KeyPress -c>', deleteAll)
root,mainloop()


