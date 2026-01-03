from tkinter import *
from tkinter import messagebox

tic_tac_toe = Tk()
tic_tac_toe.title("Tic Tac Toe")
tic_tac_toe.geometry("450x460+700+250")
tic_tac_toe.resizable(False,False)

turn = True
count = 0
winner = False

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

# סוף התוכנית
tic_tac_toe.mainloop()