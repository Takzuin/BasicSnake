import turtle
import time

posponer = 0.1

#Configuracion de la ventana ventana = wnd
wnd = turtle.Screen()

wnd.title("L4N4C0ND4")
wnd.bgcolor("black")
wnd.setup(width= 600, height= 600)
wnd.tracer(0)

#Snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = ("left")

#Funciones
def mov():
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y + 5)
    
    if head.direction == "down" :
        y = head.ycor()
        head.sety(y - 5)

    if head.direction == "left" :
        x = head.xcor()
        head.setx(x - 5)

    if head.direction == "right" :
        x = head.xcor()
        head.setx(x + 5)
    

while True:
    wnd.update()

    mov()
    time.sleep(posponer)
