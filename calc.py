from tkinter import*
from tkinter import messagebox

calc_window = Tk() 
calc_window.title("calc") 
calc_window.geometry("600x600") 
calc_window.config(bg = "black")
calc_window.resizable(False,False)



def button_press(num):  #פונקציה שמבצעת את הפעולות
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals(): #פונקציה שבודקת תנאיים מסויימים
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        messagebox.showerror("Error message:", "Error.\n")
        equation_text = ""
    except ZeroDivisionError:
        messagebox.showerror("Error message:", "Error, can't divided by 0.\n")
        equation_text = ""


def clear(): #clear פונקציה שמוחקת את הטקסט כאשר לוחצים על הכפתור 
    global equation_text
    equation_label.set("")
    equation_text = ""


equation_text = ""
equation_label = StringVar()

label = Label(calc_window, textvariable=equation_label, font=("Ariel",20), fg="cyan", bg="#0A0904",width=30, height=2) #יצירת שורת פלט אשר תציג את התרגיל והתוצאה
label.pack() #מיקום שורת הפלט

frame = Frame(calc_window) #יצירת פאנל
frame.pack() #מיקום פאנל


button_0 = Button(frame, text=0, height=5, width=10, font=100, fg="cyan",bg="#0A0904",command=lambda: button_press(0)) #יצירת כפתור מספר 0
button_0.grid(row=3, column=0) #מיקום כפתור מספר 0

button_1 = Button(frame, text=1, height=5, width=10, font=100, fg="cyan",bg="#0A0904",command=lambda: button_press(1)) #יצירת כפתור מספר 1
button_1.grid(row=0, column=0) #מיקום כפתור מספר 1

button_2 = Button(frame, text=2, height=5, width=10, font=100, fg="cyan",bg="#0A0904",command=lambda: button_press(2)) #יצירת כפתור מספר 2
button_2.grid(row=0, column=1) #מיקום כפתור מספר 2

button_3 = Button(frame, text=3, height=5, width=10, font=100, fg="cyan",bg="#0A0904",command=lambda: button_press(3)) #יצירת כפתור מספר 3
button_3.grid(row=0, column=2) #מיקום כפתור מספר 3

button_4 = Button(frame, text=4, height=5, width=10, font=100, fg="cyan",bg="#0A0904",command=lambda: button_press(4)) #יצירת כפתור מספר 4
button_4.grid(row=1, column=0) #מיקום כפתור מספר 4

button_5 = Button(frame, text=5, height=5, width=10, font=100, fg="cyan",bg="#0A0904",command=lambda: button_press(5)) #יצירת כפתור מספר 5
button_5.grid(row=1, column=1) #מיקום כפתור מספר 5

button_6 = Button(frame, text=6, height=5, width=10, font=100, fg="cyan",bg="#0A0904",command=lambda: button_press(6)) #יצירת כפתור מספר 6
button_6.grid(row=1, column=2) #מיקום כפתור מספר 6

button_7 = Button(frame, text=7, height=5, width=10, font=100, fg="cyan",bg="#0A0904",command=lambda: button_press(7)) #יצירת כפתור מספר 7
button_7.grid(row=2, column=0) #מיקום כפתור מספר 7

button_8 = Button(frame, text=8, height=5, width=10, font=100, fg="cyan",bg="#0A0904",command=lambda: button_press(8)) #יצירת כפתור מספר 8
button_8.grid(row=2, column=1) #מיקום כפתור מספר 8

button_9 = Button(frame, text=9, height=5, width=10, font=100, fg="cyan",bg="#0A0904",command=lambda: button_press(9)) #יצירת כפתור מספר 9
button_9.grid(row=2, column=2) #מיקום כפתור מספר 9


button_plus = Button(frame, text='+', height=5, width=10, font=35, fg="cyan", bg="#0A0904", command=lambda: button_press('+')) #יצירת כפתור חיבור
button_plus.grid(row=0, column=3) #מיקום כפתור חיבור

button_minus = Button(frame, text='-', height=5, width=10, font=35, fg="cyan", bg="#0A0904", command=lambda: button_press('-')) #יצירת כפתור חיסור
button_minus.grid(row=1, column=3) #מיקום כפתור חיסור

button_multiply = Button(frame, text='*', height=5, width=10, font=35, fg="cyan",bg="#0A0904",command=lambda: button_press('*')) #יצירת כפתור כפל
button_multiply.grid(row=2, column=3) #מיקום כפתור כפל

button_divide = Button(frame, text='/', height=5, width=10, font=35, fg="cyan",bg="#0A0904",command=lambda: button_press('/')) #יצירת כפתור חילוק
button_divide.grid(row=3, column=3) #מיקום כפתור חילוק

button_equal = Button(frame, text='=', height=5, width=10, font=35, fg="cyan",bg="#0A0904",command=equals) #יצירת כפתור שווה
button_equal.grid(row=3, column=2) #מיקום כפתור שווה

button_decimal = Button(frame, text='.', height=5, width=10, font=35, fg="cyan",bg="#0A0904",command=lambda: button_press('.')) #יצירת כפתור נקודה עשרונית
button_decimal.grid(row=3, column=1) #מיקום כפתור נקודה עשרונית

clear = Button(calc_window, text='clear', height=5, width=10, font=35,fg="cyan",bg="#0A0904",command=clear) #יצירת כפתור מחיקה
clear.pack() #מיקום כפתור המחיקה

calc_window.mainloop() #סיום החלון של מחשבון