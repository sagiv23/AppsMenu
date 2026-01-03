from tkinter import *
import time
from tkinter import messagebox
import random
import os
import turtle

main_window = Tk() #פתיחת חלון ראשי
main_window.title("menu") #שם לחלון הראשי
main_window.geometry("1960x1102") #קורדינציות וגודל לחלון הראשי

#משתנים עבור המחשבון
equation_text = ""
equation_label = StringVar()

#משתנים עבור הנחש


#משתנים עבור איקס עיגול
turn = True
count = 0
winner = False

def calc_func(): #פונקצייה של מחשבון
    calc_window = Toplevel()
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

    

def snake_func(): #פונקצייה של נחש
    pass



def tic_tac_toe_func(): #פונקצייה של איקס עיגול
    tic_tac_toe = Toplevel()
    tic_tac_toe.title("Tic Tac Toe")
    tic_tac_toe.geometry("450x460+700+250")
    tic_tac_toe.resizable(False,False)

    # פונקציה שיוצרת את האופציה לעשות משחק חדש
    def new_game():
        global count, winner, b1,b2,b3,b4,b5,b6,b7,b8,b9, turn
        turn = True
        count = 0
        winner = False

        b1 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#00FFFF", command=lambda: func(b1))
        b2 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#007575", command=lambda: func(b2))
        b3 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#00FFFF", command=lambda: func(b3))
        b4 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#007575", command=lambda: func(b4))
        b5 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#00FFFF", command=lambda: func(b5))
        b6 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#007575", command=lambda: func(b6))
        b7 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#00FFFF", command=lambda: func(b7))
        b8 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#007575", command=lambda: func(b8))
        b9 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#00FFFF", command=lambda: func(b9))

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)
        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)
        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

    # פונקציה שמבטלת את אפשרות הלחיצה על הכפתורים אחרי ניצחון
    def disable():
        global b1,b2,b3,b4,b5,b6,b7,b8,b9
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)

    # פונקציה שבודקת מי ניצח
    def check_win():
        global winner
        # בדיקת x
        if (b1["text"] == 'X' and b2["text"] == 'X' and b3["text"] == 'X'):
            winner = True
            b1.config(bg = "cyan")
            b2.config(bg = "cyan")
            b3.config(bg = "cyan")

            b4.config(bg = "#0A0904")
            b5.config(bg = "#0A0904")
            b6.config(bg = "#0A0904")
            b7.config(bg = "#0A0904")
            b8.config(bg = "#0A0904")
            b9.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " X won!!")
            disable()

        elif (b4["text"] == 'X' and b5["text"] == 'X' and b6["text"] == 'X'):
            winner = True
            b4.config(bg = "cyan")
            b5.config(bg = "cyan")
            b6.config(bg = "cyan")

            b1.config(bg = "#0A0904")
            b2.config(bg = "#0A0904")
            b3.config(bg = "#0A0904")
            b7.config(bg = "#0A0904")
            b8.config(bg = "#0A0904")
            b9.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " X won!!")
            disable()

        elif (b7["text"] == 'X' and b8["text"] == 'X' and b9["text"] == 'X'):
            winner = True
            b7.config(bg = "cyan")
            b8.config(bg = "cyan")
            b9.config(bg = "cyan")

            b1.config(bg = "#0A0904")
            b2.config(bg = "#0A0904")
            b3.config(bg = "#0A0904")
            b4.config(bg = "#0A0904")
            b5.config(bg = "#0A0904")
            b6.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " X won!!")
            disable()

        elif (b1["text"] == 'X' and b5["text"] == 'X' and b9["text"] == 'X'):
            winner = True
            b1.config(bg = "cyan")
            b5.config(bg = "cyan")
            b9.config(bg = "cyan")

            b2.config(bg = "#0A0904")
            b3.config(bg = "#0A0904")
            b4.config(bg = "#0A0904")
            b6.config(bg = "#0A0904")
            b7.config(bg = "#0A0904")
            b8.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " X won!!")
            disable()

        elif (b3["text"] == 'X' and b5["text"] == 'X' and b7["text"] == 'X'):
            winner = True
            b3.config(bg = "cyan")
            b5.config(bg = "cyan")
            b7.config(bg = "cyan")

            b1.config(bg = "#0A0904")
            b2.config(bg = "#0A0904")
            b4.config(bg = "#0A0904")
            b6.config(bg = "#0A0904")
            b8.config(bg = "#0A0904")
            b9.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " X won!!")
            disable()

        elif (b1["text"] == 'X' and b4["text"] == 'X' and b7["text"] == 'X'):
            winner = True
            b1.config(bg = "cyan")
            b4.config(bg = "cyan")
            b7.config(bg = "cyan")

            b2.config(bg = "#0A0904")
            b3.config(bg = "#0A0904")
            b5.config(bg = "#0A0904")
            b6.config(bg = "#0A0904")
            b8.config(bg = "#0A0904")
            b9.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " X won!!")
            disable()

        elif (b2["text"] == 'X' and b5["text"] == 'X' and b8["text"] == 'X'):
            winner = True
            b2.config(bg = "cyan")
            b5.config(bg = "cyan")
            b8.config(bg = "cyan")

            b1.config(bg = "#0A0904")
            b3.config(bg = "#0A0904")
            b4.config(bg = "#0A0904")
            b6.config(bg = "#0A0904")
            b7.config(bg = "#0A0904")
            b9.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " X won!!")
            disable()

        elif (b3["text"] == 'X' and b6["text"] == 'X' and b9["text"] == 'X'):
            winner = True
            b3.config(bg = "cyan")
            b6.config(bg = "cyan")
            b9.config(bg = "cyan")

            b1.config(bg = "#0A0904")
            b2.config(bg = "#0A0904")
            b4.config(bg = "#0A0904")
            b5.config(bg = "#0A0904")
            b7.config(bg = "#0A0904")
            b8.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " X won!!")
            disable()

        # בדיקת O
        elif (b1["text"] == 'O' and b2["text"] == 'O' and b3["text"] == 'O'):
            winner = True
            b1.config(bg = "cyan")
            b2.config(bg = "cyan")
            b3.config(bg = "cyan")

            b4.config(bg = "#0A0904")
            b5.config(bg = "#0A0904")
            b6.config(bg = "#0A0904")
            b7.config(bg = "#0A0904")
            b8.config(bg = "#0A0904")
            b9.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " O won!!")
            disable()

        elif (b4["text"] == 'O' and b5["text"] == 'O' and b6["text"] == 'O'):
            winner = True
            b4.config(bg = "cyan")
            b5.config(bg = "cyan")
            b6.config(bg = "cyan")

            b1.config(bg = "#0A0904")
            b2.config(bg = "#0A0904")
            b3.config(bg = "#0A0904")
            b7.config(bg = "#0A0904")
            b8.config(bg = "#0A0904")
            b9.config(bg = "#0A0904")
        
            messagebox.showinfo("Tic Tac Toe", " O won!!")
            disable()

        elif (b7["text"] == 'O' and b8["text"] == 'O' and b9["text"] == 'O'):
            winner = True
            b7.config(bg = "cyan")
            b8.config(bg = "cyan")
            b9.config(bg = "cyan")

            b1.config(bg = "#0A0904")
            b2.config(bg = "#0A0904")
            b3.config(bg = "#0A0904")
            b4.config(bg = "#0A0904")
            b5.config(bg = "#0A0904")
            b6.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " O won!!")
            disable()

        elif (b1["text"] == 'O' and b5["text"] == 'O' and b9["text"] == 'O'):
            winner = True
            b1.config(bg = "cyan")
            b5.config(bg = "cyan")
            b9.config(bg = "cyan")

            b2.config(bg = "#0A0904")
            b3.config(bg = "#0A0904")
            b4.config(bg = "#0A0904")
            b6.config(bg = "#0A0904")
            b7.config(bg = "#0A0904")
            b8.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " O won!!")
            disable()

        elif (b3["text"] == 'O' and b5["text"] == 'O' and b7["text"] == 'O'):
            winner = True
            b3.config(bg = "cyan")
            b5.config(bg = "cyan")
            b7.config(bg = "cyan")

            b1.config(bg = "#0A0904")
            b2.config(bg = "#0A0904")
            b4.config(bg = "#0A0904")
            b6.config(bg = "#0A0904")
            b8.config(bg = "#0A0904")
            b9.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " O won!!")
            disable()

        elif (b1["text"] == 'O' and b4["text"] == 'O' and b7["text"] == 'O'):
            winner = True
            b1.config(bg = "cyan")
            b4.config(bg = "cyan")
            b7.config(bg = "cyan")

            b2.config(bg = "#0A0904")
            b3.config(bg = "#0A0904")
            b5.config(bg = "#0A0904")
            b6.config(bg = "#0A0904")
            b8.config(bg = "#0A0904")
            b9.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " O won!!")
            disable()

        elif (b2["text"] == 'O' and b5["text"] == 'O' and b8["text"] == 'O'):
            winner = True
            b2.config(bg = "cyan")
            b5.config(bg = "cyan")
            b8.config(bg = "cyan")

            b1.config(bg = "#0A0904")
            b3.config(bg = "#0A0904")
            b4.config(bg = "#0A0904")
            b6.config(bg = "#0A0904")
            b7.config(bg = "#0A0904")
            b9.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " O won!!")
            disable()

        elif (b3["text"] == 'O' and b6["text"] == 'O' and b9["text"] == 'O'):
            winner = True
            b3.config(bg = "cyan")
            b6.config(bg = "cyan")
            b9.config(bg = "cyan")

            b1.config(bg = "#0A0904")
            b2.config(bg = "#0A0904")
            b4.config(bg = "#0A0904")
            b5.config(bg = "#0A0904")
            b7.config(bg = "#0A0904")
            b8.config(bg = "#0A0904")
            messagebox.showinfo("Tic Tac Toe", " O won!!")
            disable()

        # אם יש תיקו
        elif(count == 9 and winner == False):
            messagebox.showinfo("Tic Tac Toe", "Game draw!!\nTry again")
            disable()


    # פונקציה שמשנה את הריבוע לאיקס או עיגול
    def func(b):
        global turn, count
        if (b["text"] == ' ' and turn == True):
            b["text"] = 'X'
            turn = False
            count = count + 1
            check_win()
        elif (b["text"] == ' ' and turn == False):
            b["text"] = 'O'
            turn = True
            count = count + 1
            check_win()
        else:
            messagebox.showerror("Error message:", "You can't press the same button twice. try again.\n")

    # יצירת כפתור
    b1 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#00FFFF", command=lambda: func(b1))
    b2 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#007575", command=lambda: func(b2))
    b3 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#00FFFF", command=lambda: func(b3))
    b4 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#007575", command=lambda: func(b4))
    b5 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#00FFFF", command=lambda: func(b5))
    b6 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#007575", command=lambda: func(b6))
    b7 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#00FFFF", command=lambda: func(b7))
    b8 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#007575", command=lambda: func(b8))
    b9 = Button(tic_tac_toe, text=" ", height=10, width=20, font=("Arial", 9), bg="#00FFFF", command=lambda: func(b9))

    # מיקןם של הכפתור
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    # יצירת תפריט
    Game_Menu = Menu(tic_tac_toe)
    tic_tac_toe.config(menu = Game_Menu)

    #יצירת חלון בתפריט 
    Restart = Menu(Game_Menu)
    Game_Menu.add_command (label = "New game" , command = new_game)

def clock(): #פונקציה של שעון
    Hour = str(time.strftime("%H"))
    Minute = str(time.strftime("%M"))
    Second = str(time.strftime("%S"))
    l_hours.config(text=Hour)
    l_minute.config(text=Minute)
    l_seconds.config(text=Second)
    l_hours.after(200 , clock)


img = PhotoImage(file="window.png") #תמונת חלון ראשי
label = Label(main_window,image=img)
label.place(x=0, y=0) 

l_hours = Label(main_window, text = "12", font = ("Arial",15), fg = "black", bg="#5DADEC") #יצירת שעות
l_hours.place(x = 50, y = 850, width = 100, height = 100) #מיקום שעון - שעות
l_minute = Label(main_window, text = "11", font = ("Arial",15), fg = "black", bg="#5DADEC") #יצירת דקות
l_minute.place(x = 120, y = 850, width = 100, height = 100) #מיקום שעון - דקות
l_seconds = Label(main_window, text = "10", font = ("Arial",15), fg = "black", bg="#5DADEC") #יצירת שניות
l_seconds.place(x = 190, y = 850, width = 100, height = 100) #מיקום שעון - שניות

l1 = Label(main_window, font = ("Ariel", 30), fg = "blue", bg = "black")
l1.pack()
l2 = Label(main_window, font = ("Ariel", 30), fg = "blue", bg = "black")
l2.pack()

l_label = Label(main_window, text = "תפריט ראשי", font = ("Ariel", 30), fg = "blue", bg = "#5DADEC") #יצירת כותרת
l_label.pack() #מיקום לכותרת


b_calc = Button(main_window, text= "מחשבון", height=5, width=15,font=("Ariel",26), bg = "#5DADEC",command = calc_func) #יצירת כפתור מחשבון
b_calc.place(x = 150, y = 400) #מיקום כפתור מחשבון

b_tic_tac_toe = Button(main_window, text= "איקס עיגול", height=5, width=15, font=("Ariel",26), bg = "#5DADEC",command = tic_tac_toe_func) #יצירת כפתור איקס עיגול
b_tic_tac_toe.place(x = 850, y = 400) #מיקום כפתור איקס עיגול

b_snake = Button(main_window, text= "נחש", height=5, width=15, font=("Ariel",26), bg = "#5DADEC",command = snake_func) #יצירת כפתור משחק נחש
b_snake.place(x = 1550, y = 400) #מיקום כפתור משחק נחש







clock() #קריאה לפונקצייה של שעון
main_window.mainloop() #סיום החלון הראשי