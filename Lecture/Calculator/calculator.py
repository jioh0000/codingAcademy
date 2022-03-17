from tkinter import *

win = Tk()
win.geometry("312x350") #width x height (pixels)
win.resizable(0,0)
win.title("Jiculator")

"""
Input bos: [       ]
First Row:  C / 
Second Row: 7 8 9 *
Third Row:  4 5 6 -
Fourth Row: 1 2 3 +
Fifth Row:  0 . =
"""

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

expression = ""
input_text = StringVar()

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()

#First Row
clear = Button(btns_frame, text="C", fg="black", width=23, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: bt_clear()).grid(row=0,
column=0, columnspan=3, padx=1, pady=1)

divide = Button(btns_frame, text="/", fg="black", width=5, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click('/')).grid(row=0,
column=3, columnspan=3, padx=1, pady=1)

#Second Row
seven = Button(btns_frame, text="7", fg="black", width=5, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click('7')).grid(row=1,
column=0, columnspan=1, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="black", width=5, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click('8')).grid(row=1,
column=1, columnspan=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="black", width=5, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click('9')).grid(row=1,
column=2, columnspan=1, padx=1, pady=1)

multiply = Button(btns_frame, text="*", fg="black", width=5, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click('*')).grid(row=1,
column=3, columnspan=1, padx=1, pady=1)

win.mainloop()