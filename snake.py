from tkinter import messagebox
import os
import turtle
import time
import random

messagebox.showinfo("הערה", "חשוב לזכור!\nכדי שהנחש יזוז, צריך להפוך את המקלדת לאנגלית")

score = 0
high_score = 0
delay = 0.1
segment1 = []

window1 = turtle.Screen()
window1.title("Snake")
window1.bgcolor("#0A0904")
window1.setup(width=660,height=660)
window1.tracer(0)

#הגדרות נחש
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

#הגדרות התפוח
apple = turtle.Turtle()
apple.speed(0)
apple.shape("square")
apple.color("red")
apple.penup()
apple.goto(0,100)

#הגדרות לוח תוצאות
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("cyan")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0,260)
scoreboard.write("Score: 0   High Score: 0", align="center",font=("Ariel",20))

#פונקציות שגורמות לנחש לזוז 
def up():
    if snake.direction != "down":
        snake.direction = "up"
def down():
    if snake.direction != "up":
        snake.direction = "down"
def left():
    if snake.direction != "right":
        snake.direction = "left"
def right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y+20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x-20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+20)

#כפתורי המשחק
window1.listen()
window1.onkeypress(up,"w")
window1.onkeypress(down,"s")
window1.onkeypress(left,"a")
window1.onkeypress(right,"d")

while True:
    window1.update()

    #אם הנחש נתקע בלוח
    if snake.xcor()>300 or snake.xcor()<-300 or snake.ycor()>300 or snake.ycor()<-300:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"

        # הסתרת המערך
        for segment in segment1:
            segment.goto(2,3)

        segment1.clear()
        score = 0
        delay = 0.1
        scoreboard.clear()
        scoreboard.write("Score: {}   High Score:   {}".format(score,high_score),align="center",font=("Ariel",20))

    #אם הנחש אכל את התפוח
    if snake.distance (apple) < 40:
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        apple.goto(x,y)

        #הוספת מערך חדש
        segment2 = turtle.Turtle()
        segment2.speed(0)
        segment2.shape("square")
        segment2.color("green")
        segment2.penup()
        segment1.append(segment2)
        delay -= 0.001
        score += 10

        #אם מספר הנקודות שזכית יותר גבוה ממספר הנקודות הגבוה
        if score > high_score:
            high_score = score

        scoreboard.clear()
        scoreboard.write("Score: {}   High Score:   {}".format(score,high_score),align="center",font=("Ariel",20))

    for index in range(len(segment1)-1,0,-1):
         x = segment1[index-1].xcor()
         y = segment1[index-1].ycor()
         segment1[index].goto(x,y)
    
    if len(segment1)>0:
         x = snake.xcor()
         y = snake.ycor()
         segment1[0].goto(x,y)
    move()

    #אם הנחש נתקע בעצמו
    for segment in segment1:
        if segment.distance(snake)<20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"

            #הסתרת המערך
            for segment in segment1:
                segment.goto(1000,1000)

            segment1.clear()
            score = 0
            delay = 0.1
            scoreboard.clear()
            scoreboard.write("Score: {}   High Score:   {}".format(score,high_score),align="center",font=("Ariel",20))
    time.sleep(delay)
window1.mainloop()