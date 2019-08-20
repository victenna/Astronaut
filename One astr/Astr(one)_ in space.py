import turtle
import random
turtle.tracer(4)
t=turtle.Turtle()
wn=turtle.Screen()
wn.screensize(900,600,'dark blue')
t.speed(10)
import time
#Moonsky
moonsky=turtle.Turtle()
image1='moonsky.gif'
wn.bgpic(image1)
#Spaseshuttle
Shuttle=turtle.Turtle()
image2='shuttle1.gif'
wn.addshape(image2)
Shuttle.shape(image2)
Shuttle.penup()
Shuttle.goto(-600,-600)
Shuttle.setheading(40)
#Astronaut 
image3='astr1.gif'
wn.addshape(image3)
Astro=turtle.Turtle()
Astro.shape(image3)
Astro.up()
while True:
    Shuttle.fd(5)
    time.sleep(0.03)
    X=Shuttle.xcor()
    Y=Shuttle.ycor()
    Astro.setposition(X+90,Y+90)
    Astro.fd(60)
    Astro.right(5)

    if abs(X-600)<10 or abs(Y-600) <10:
        Shuttle.goto(-600,-600)
        Astro.goto(-600,-400)
        Shuttle.setheading(random.randint(40,80))
        
