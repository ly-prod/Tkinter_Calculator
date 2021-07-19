from tkinter import *

root = Tk()

num_input = Entry(root, width=40, borderwidth=5)
num_input.grid(row=0, column=0, columnspan=4, padx=7, pady=5)


# functions
# add functionalities here...

# Buttons

btn1 = Button(root, text="1", padx=40, pady=20)
btn2 = Button(root, text="2", padx=40, pady=20)
btn3 = Button(root, text="3", padx=40, pady=20)
btn4 = Button(root, text="4", padx=40, pady=20)
btn5 = Button(root, text="5", padx=40, pady=20)
btn6 = Button(root, text="6", padx=40, pady=20)
btn7 = Button(root, text="7", padx=40, pady=20)
btn8 = Button(root, text="8", padx=40, pady=20)
btn9 = Button(root, text="9", padx=40, pady=20)
btn0 = Button(root, text="0", padx=40, pady=20)
btn_plus = Button(root, text="+", padx=37, pady=20)
btn_minus = Button(root, text="-", padx=40, pady=20)
btn_mul = Button(root, text="*", padx=40, pady=20)
btn_div = Button(root, text="/", padx=40, pady=20)
btn_equal = Button(root, text="=", padx=40, pady=20)
btn_clear = Button(root, text="C", padx=40, pady=20, fg="red")

# Buttons layout
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn_plus.grid(row=1, column=3)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn_minus.grid(row=2, column=3)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn_mul.grid(row=3, column=3)

btn0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)
btn_div.grid(row=4, column=3)

root.mainloop()
