import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.listen()
t.speed(0)
t.width(5)

def up():
    t.setheading(90)

def down():
    t.setheading(270)

def right():
    t.setheading(0)

def left():
    t.setheading(180)

def right_angle():
    t.rt(15)

def left_angle():
    t.lt(15)
    
def square():
    t.color("black", "white")
    t.begin_fill()
    for i in range(4):
        t.fd(100)
        t.rt(90)
    t.end_fill()
        
def triangle():
    t.rt(60)
    t.color("black", "white")
    t.begin_fill()
    for j in range(3):
        t.fd(100)
        t.rt(120)
    t.end_fill()
    t.lt(60)   

def circle():
    t.color("black", "white")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

def penup():
    t.penup()

def pendown():
    t.pendown()

def move():
    t.fd(10)

def undo():
    t.undo()

def novice():
    t.showturtle()
    t.clear()
    t.penup()
    t.goto(20, 350)
    t.pendown()

    for i in range(4):
        t.fd(650)
        t.rt(90)

    t.penup()
    t.goto(-20, 350)
    t.pendown()
    t.setheading(180)

    for i in range(4):
        t.fd(650)
        t.lt(90)

    t.setheading(0)
    t.penup()
    t.goto(550, -370)

    t.color("red")
    t.write("[B] Back", font=("arial", 20, "bold"))
    t.color("black")

    t.penup()
    t.goto(-350, 50)
    t.pendown()

    t.circle(100)
    t.rt(90)
    t.fd(60)
    t.lt(90)
    t.fd(40)
    t.bk(80)
    t.fd(40)
    t.rt(90)
    t.fd(60)

    t.rt(45)
    t.fd(50)
    t.bk(50)
    t.lt(90)
    t.fd(50)

    t.penup()
    t.goto(350, 50)
    t.setheading(0)


def intermediate():
    t.showturtle()
    t.clear()
    t.penup()
    t.goto(20, 350)
    t.pendown()

    for i in range(4):
        t.fd(650)
        t.rt(90)

    t.penup()
    t.goto(-20, 350)
    t.pendown()
    t.setheading(180)

    for i in range(4):
        t.fd(650)
        t.lt(90)

    t.setheading(0)
    t.penup()
    t.goto(550, -370)

    t.color("red")
    t.write("[B] Back", font=("arial", 20, "bold"))
    t.color("black")

    t.penup()
    t.goto(-350, 50)
    t.pendown()


    for i in range(4):
        t.rt(45)
        t.rt(60)
        t.color("black", "white")
        t.begin_fill()
        for j in range(3):
            t.fd(100)
            t.rt(120)
        t.end_fill()
        t.lt(60)
        t.rt(45)

    t.setheading(270)
    t.fd(150)
    t.setheading(0)

    t.rt(60)
    t.color("black", "white")
    t.begin_fill()
    for j in range(3):
        t.fd(100)
        t.rt(120)
    t.end_fill()
    t.lt(60)

    t.penup()
    t.goto(350, 50)
    t.setheading(0)


def expert():
    t.showturtle()
    t.clear()
    t.penup()
    t.goto(20, 350)
    t.pendown()

    for i in range(4):
        t.fd(650)
        t.rt(90)

    t.penup()
    t.goto(-20, 350)
    t.pendown()
    t.setheading(180)

    for i in range(4):
        t.fd(650)
        t.lt(90)

    t.setheading(0)
    t.penup()
    t.goto(550, -370)

    t.color("red")
    t.write("[B] Back", font=("arial", 20, "bold"))
    t.color("black")

    t.penup()
    t.goto(-350, 50)
    t.pendown()

    for i in range(4):
        t.color("black", "white")
        t.begin_fill()
        t.circle(100)
        t.end_fill()
        t.rt(90)

    for i in range(4):
        t.color("black", "white")
        t.begin_fill()
        for j in range(4):
            t.fd(100)
            t.rt(90)
        t.end_fill()
        t.rt(90)

    for k in range(4):
        t.rt(60)
        t.color("black", "white")
        t.begin_fill()
        for j in range(3):
            t.fd(100)
            t.rt(120)
        t.end_fill()
        t.lt(60)
        t.rt(90)

    t.penup()
    t.goto(350, 50)
    t.setheading(0)


def start():
    t.hideturtle()
    t.clear()
    t.penup()
    t.home()

    t.penup()
    t.goto(-280, 150)
    t.pendown()

    t.color("red")
    t.write("Three-ky", font=("arial", 100, "bold"))
    t.color("black")
    
    t.penup()
    t.home()

    t.goto(-200,-50)
    t.write("[1] Start", font=("arial", 50, "normal"))
    t.goto(-200,-180)
    t.write("[2] Instruction", font=("arial", 50, "normal"))

    t.penup()
    t.goto(-300, 300)
    t.pendown()

    for i in range(4):
        t.fd(600)
        t.rt(90)

    t.penup()
    t.home()

def instruction():
    t.hideturtle()
    t.clear()
    t.penup()
    t.goto(-350, 350)
    t.pendown()

    for i in range(2):
        t.fd(750)
        t.rt(90)
        t.fd(700)
        t.rt(90)

    t.penup()
    t.goto(-330, 280)
    t.write("Instructions:", font=("Arial", 40, "bold"))

    t.goto(-320, 250)
    t.write("Use the arrow keys and other command keys to combine", font=("Arial", 20, "normal"))

    t.goto(-320, 215)
    t.write("shapes and lines that fit the figure on the left side.", font=("Arial", 20, "normal"))

    t.goto(-330, 120)
    t.write("Commands:", font=("arial", 40, "bold"))

    t.goto(-300, 80)
    t.write("'S' = Square", font=("arial", 20, "normal"))

    t.goto(-300, 40)
    t.write("'T' = Triangle", font=("arial", 20, "normal"))

    t.goto(-300, 0)
    t.write("'C' = Circle", font=("arial", 20, "normal"))

    t.goto(-300, -40)
    t.write("'U' = Pen up", font=("arial", 20, "normal"))

    t.goto(-300, -80)
    t.write("'D' = Pendown", font=("arial", 20, "normal"))

    t.goto(-300, -120)
    t.write("'M' = Move", font=("arial", 20, "normal"))

    t.goto(-300, -160)
    t.write("'Z' = Undo", font=("arial", 20, "normal"))

    t.goto(0, 80)
    t.write("'Arrow key up' = Face up", font=("arial", 20, "normal"))

    t.goto(0, 40)
    t.write("'Arrow key down' = Face down", font=("arial", 20, "normal"))

    t.goto(0, 0)
    t.write("'Arrow key right' = Face right", font=("arial", 20, "normal"))

    t.goto(0, -40)
    t.write("'Arrow key left' = Face left", font=("arial", 20, "normal"))

    t.goto(0, -80)
    t.write("'<' = Rotate left 15°", font=("arial", 20, "normal"))

    t.goto(0, -120)
    t.write("'>' = Rotate right 15°", font=("arial", 20, "normal"))

    t.goto(210, -330)
    t.color("red")
    t.write("[B] Back", font=("arial", 30, "bold"))
    t.color("black")

def level():
    t.hideturtle()
    t.clear()
    t.penup()
    t.goto(-250, 250)
    t.pendown()

    for i in range(4):
        t.fd(500)
        t.rt(90)

    t.penup()
    t.goto(-220, 180)
    t.write("Level:", font=("arial", 30, "bold"))

    t.goto(-80, 80)
    t.write("[N] Novice", font=("arial", 20, "bold"))

    t.goto(-80, -20)
    t.write("[I] Intermediate", font=("arial", 20, "bold"))

    t.goto(-80, -120)
    t.write("[E] Expert", font=("arial", 20, "bold"))

    t.goto(70, -230)
    t.color("red")
    t.write("[B] Back", font=("arial", 30, "bold"))
    t.color("black")
    

screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(right, 'Right')
screen.onkey(left, 'Left')
screen.onkey(right_angle, ',')
screen.onkey(left_angle, '.')
screen.onkey(square, 's')
screen.onkey(triangle, 't')
screen.onkey(circle, 'c')
screen.onkey(penup, 'u')
screen.onkey(pendown, 'd')
screen.onkey(move, 'm')
screen.onkey(undo, 'z')
screen.onkey(start, 'b')
screen.onkey(instruction, '2')
screen.onkey(level, '1')
screen.onkey(novice, 'n')
screen.onkey(expert, 'e')
screen.onkey(intermediate, 'i')

t.hideturtle()
t.penup()
t.goto(-280, 150)
t.pendown()

t.color("red")
t.write("Three-ky", font=("arial", 100, "bold"))
t.color("black")

t.penup()
t.home()

t.goto(-200,-50)
t.write("[1] Start", font=("arial", 50, "normal"))
t.goto(-200,-180)
t.write("[2] Instruction", font=("arial", 50, "normal"))

t.penup()
t.goto(-300, 300)
t.pendown()

for i in range(4):
    t.fd(600)
    t.rt(90)
    
t.penup()
t.home()








