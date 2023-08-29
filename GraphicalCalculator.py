from tkinter import *

#------------------------------COLORS------------------------
NAVY_BLUE = "#445069"
GRAY = "#9E9FA5"
LIGHT_BLUE = "#C5DFF8"



#-----------------------------UI design----------------------
calculator = Tk()
calculator.title("Calculator")
calculator.geometry("395x500")

text_input = StringVar()

#row = 0
display = Entry(calculator,textvariable=text_input,width=16,bd=5,font=("Arial", 32), bg=NAVY_BLUE,fg="#FAF0D7")
display.grid(columnspan=4)

#row = 1
btn7 = Button(calculator,text="7", bg=GRAY, fg="black",width=5,padx=16,pady=16  ,font=("Arial",15), command=lambda:show_display(7))
btn7.grid(row=1,column=0)

btn8 = Button(calculator,text="8", bg=GRAY, fg="black",width=5,padx=16,pady=16 ,font=("Arial",15), command=lambda:show_display(8))
btn8.grid(row=1,column=1)

btn9 = Button(calculator,text="9", bg=GRAY, fg="black",width=5,padx=16,pady=16 ,font=("Arial",15), command=lambda:show_display(9))
btn9.grid(row=1,column=2)

btn_addition = Button(calculator,text="+", bg=GRAY, fg="black",width=5,padx=16,pady=16 ,font=("Arial",15), command=lambda:show_display("+"))
btn_addition.grid(row=1,column=3)

#row = 2
btn4 = Button(calculator,text="4", bg=GRAY, fg="black",width=5,padx=16,pady=16  ,font=("Arial",15), command=lambda:show_display(4))
btn4.grid(row=2,column=0)

btn5 = Button(calculator,text="5", bg=GRAY, fg="black",width=5,padx=16,pady=16 ,font=("Arial",15), command=lambda:show_display(5))
btn5.grid(row=2,column=1)

btn6 = Button(calculator,text="6", bg=GRAY, fg="black",width=5,padx=16,pady=16 ,font=("Arial",15), command=lambda:show_display(6))
btn6.grid(row=2,column=2)

btn_subtraction = Button(calculator,text="-", bg=GRAY, fg="black",width=5,padx=16,pady=16 ,font=("Arial",15), command=lambda:show_display("-"))
btn_subtraction.grid(row=2,column=3)

#row = 3
btn1 = Button(calculator,text="1", bg=GRAY, fg="black",width=5,padx=16,pady=16  ,font=("Arial",15), command=lambda:show_display(1))
btn1.grid(row=3,column=0)

btn2 = Button(calculator,text="2", bg=GRAY, fg="black",width=5,padx=16,pady=16 ,font=("Arial",15), command=lambda:show_display(2))
btn2.grid(row=3,column=1)

btn3 = Button(calculator,text="3", bg=GRAY, fg="black",width=5,padx=16,pady=16 ,font=("Arial",15), command=lambda:show_display(3))
btn3.grid(row=3,column=2)

btn_multiplication = Button(calculator,text="*", bg=GRAY, fg="black",width=5,padx=16,pady=16 ,font=("Arial",15), command=lambda:show_display("*"))
btn_multiplication.grid(row=3,column=3)

#row = 4
btn0 = Button(calculator,text="0", bg=GRAY, fg="black",width=5,padx=16,pady=16  ,font=("Arial",15), command=lambda:show_display(0))
btn0.grid(row=4,column=0)

btn00 = Button(calculator,text="00", bg=GRAY, fg="black",width=5,padx=16,pady=16 ,font=("Arial",15), command=lambda:show_display("00"))
btn00.grid(row=4,column=1)

btn_point = Button(calculator,text=".", bg=GRAY, fg="black",width=5,padx=16,pady=16 ,font=("Arial",15), command=lambda:show_display("."))
btn_point.grid(row=4,column=2)

btn_division = Button(calculator,text="/", bg=GRAY, fg="black",width=5,padx=16,pady=16 ,font=("Arial",15), command=lambda:show_display("/"))
btn_division.grid(row=4,column=3)

#row = 5
btn_clear = Button(calculator,text="CLEAR", bg=LIGHT_BLUE, fg="black",width=5,padx=16,pady=16  ,font=("Arial",15), command=clear)
btn_clear.grid(row=5,column=0,columnspan=2,sticky="we")

btn_calculate = Button(calculator,text="=", bg=LIGHT_BLUE, fg="black",width=5,padx=16,pady=16 ,font=("Arial",15), command=calculate)
btn_calculate.grid(row=5,column=2,columnspan=2,sticky="we")

calculator.mainloop()


