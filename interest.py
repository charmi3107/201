from time import time
from tkinter import *
window = Tk()

# add widgets here


window.title('Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

# function for button


def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i, 2)

    msg = ""

    if bmi < 18.5:
        msg = "you areUnderweight"
    elif bmi > 18.5 and bmi <= 24.9:
        msg = "is in Normal Range"
    elif bmi > 25 and bmi <= 29.9:
        msg = "you are Overweight"
    elif bmi > 30:
        msg = "you are Obese"
    else:
        msg = "Something Went Wrong"

    output_message = Label(result_frame, text=name+", your BMI is " +
                           str(bmi)+" and "+msg, bg="lightcyan", font=("Calibri", 12), width=42)
    output_message.place(x=20, y=40)
    output_message.pack()


app_label = Label(window, text="Interest CALCULATOR", fg="black",
                  bg="lightcyan", font=("Calibri", 20), bd=5)
app_label.place(x=50, y=20)

name_label = Label(window, text="Rate of Interest", fg="black",
                   bg="lightcyan", font=("Calibri", 12), bd=1)
name_label.place(x=20, y=90)

time_label = Label(window, text="Time", fg="black",
                   bg="lightcyan", font=("Calibri", 12), bd=1)
time_label.place(x=20, y=90)

# entry- input box
username = Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

#label- heading
time_label = Label(window, text="Enter time (cm)",
                     fg="black", bg="lightcyan", font=("Calibri", 12))
time_label.place(x=20, y=140)

time_entry = Entry(window, text="", bd=2, width=15)
time_entry.place(x=150, y=142)

rateofinterest_label = Label(window, text="rate of interest",
                     fg="black", bg="lightcyan", font=("Calibri", 12))
rateofinterest_label.place(x=20, y=185)

rateofinterest_entry = Entry(window, text="", bd=2, width=15)
rateofinterest_entry.place(x=150, y=187)

# command in button inpython is like onpress in reactnative, mousepressed in button of js
calculate_button = Button(window, text="CALCULATE",
                          fg="black", bg="cyan", bd=4, command=calculate_bmi)
calculate_button.place(x=20, y=250)

result_frame = LabelFrame(window, text="Result",
                          bg="grey", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20, y=300)

result_label = Label(result_frame, text=" ", bg="lightcyan",
                     font=("Calibri", 12), width=33)
result_label.place(x=20, y=20)
result_label.pack()


window.mainloop()