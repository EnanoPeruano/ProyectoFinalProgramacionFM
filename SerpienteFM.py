


import turtle
import time
import random

delay = 0.1

# pantalla
wn = turtle.Screen()
wn.title("Juego serpiente Franco Martinez")
wn.bgcolor("blue")
wn.setup(width=700, height=700)
wn.tracer(0)  # apaga coso de pantalla


# cabeza
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"


# comida
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# cosos de doblar


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# teclas
wn.listen()
wn.onkeypress(go_up, "w")

wn.onkeypress(go_down, "s")

wn.onkeypress(go_left, "a")

wn.onkeypress(go_right, "d")

# cosas del juego
while True:
    wn.update()


    #choque con el borde
    if head.xcor()>350 or head.xcor()<-350 or head.ycor()>350 or head.ycor()<-350:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"


    # choque con comida
    if head.distance(food) < 20:
        # move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

    # ahacerla mas larga
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        segments.append(new_segment)

    # orden de crecer
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)


    #mover coso con la cabeza
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        
        pass



    move()


    #choque con cuerpo
    for segment in segments:
        if segment.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

    #esconder cuerpo
            for segment in segments:
                segment.goto(1000, 1000)

            #borrar el cuerpo
            segments.clear()

    time.sleep(delay)

    
wn.mainloop()