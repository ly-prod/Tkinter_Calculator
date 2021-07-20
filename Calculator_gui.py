from tkinter import *

root = Tk()


# functions
def d0(text):
    num_input.insert(END, text)
def d1(text):
    num_input.insert(END, text)
def d2(text):
    num_input.insert(END, text)
def d3(text):
    num_input.insert(END, text)
def d4(text):
    num_input.insert(END, text)
def d5(text):
    num_input.insert(END, text)
def d6(text):
    num_input.insert(END, text)
def d7(text):
    num_input.insert(END, text)
def d8(text):
    num_input.insert(END, text)
def d9(text):
    num_input.insert(END, text)
def dp(text):
    num_input.insert(END, text)
def dd(text):
    num_input.insert(END, text)
def dm(text):
    num_input.insert(END, text)
def ds(text):
    num_input.insert(END, text)
def dde():
    num_input.delete(0, END)
def de():
    num_input.delete(0, END)

num_input = Entry(root, width=40, borderwidth=5)
num_input.grid(row=0, column=0, columnspan=4, padx=7, pady=5)

# add functionalities here...

# Buttons

btn1 = Button(root, text="1", padx=40, pady=20, command=lambda: d1("1"))
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda: d2("2"))
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda: d3("3"))

btn4 = Button(root, text="4", padx=40, pady=20, command=lambda: d4("4"))
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda: d5("5"))
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda: d6("6"))

btn7 = Button(root, text="7", padx=40, pady=20, command=lambda: d7("7"))
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda: d8("8"))
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda: d9("9"))
btn0 = Button(root, text="0", padx=40, pady=20, command=lambda: d0("0"))

btn_plus = Button(root, text="+", padx=37, pady=20, command=lambda: dp("+"))
btn_minus = Button(root, text="-", padx=40, pady=20, command=lambda: ds("-"))
btn_mul = Button(root, text="*", padx=40, pady=20, command=lambda: dm("×"))
btn_div = Button(root, text="/", padx=40, pady=20, command=lambda: dd("/"))
btn_equal = Button(root, text="=", padx=40, pady=20, command=de)
btn_clear = Button(root, text="C", padx=40, pady=20, fg="red", command=dde)

# Buttons layout

# row 1
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn_plus.grid(row=1, column=3)
# #row 2
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn_minus.grid(row=2, column=3)
# row 3
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn_mul.grid(row=3, column=3)
# row 4
btn0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)
btn_div.grid(row=4, column=3)

root.mainloop()
