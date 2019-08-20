import turtle
import random
turtle.tracer(7)
t=turtle.Turtle()
wn=turtle.Screen()
wn.screensize(800,800,'dark blue')
t.speed(10)

s = turtle.Shape("compound")
import time

stars=turtle.Turtle()
def star(x,y,size):
    stars.up()
    stars.goto(x,y)
    stars.down()
    stars.color('white','white')
    stars.begin_fill()
    stars.left(36)
    for i in range(5):
        stars.fd(size)
        stars.left(144)

    stars.end_fill()

stars1=turtle.Turtle()
stars1.hideturtle()
def star1(x,y,size):
    stars1.up()
    stars1.goto(x,y)
    stars1.down()
    stars1.color('gold','gold')
    stars1.begin_fill()
    stars1.left(36)
    for i in range(5):
        stars1.fd(size)
        stars1.left(144)

    stars1.end_fill()

#Draw 50 random stars
for i in range(50):
    starX=random.randint(-400,400)
    starY=random.randint(-400,400)
    starsize=random.randint(10,20)
    star(starX,starY,starsize)


t.hideturtle()

#Space Shuttle

poly1=((0,0),(25,0),(25,10),(0,10))
poly2=((25,0),(35,5),(25,10))
poly3=((0,10),(-5,30),(10,10))
poly4=((0,0),(-5,20),(10,0))

s.addcomponent(poly1,'red','black')
s.addcomponent(poly2,'pink','black')
s.addcomponent(poly3,'green','black')
s.addcomponent(poly4,'green','black')

wn.register_shape('roket',s)



Merk=turtle.Turtle(shape='roket')
Merk.penup()
Merk.hideturtle()
Merk.tilt(90)
Merk.showturtle()
Merk.shapesize(3)
Merk.goto(-600,-600)
Merk.setheading(20)

#-------------------

#Astronaut 1
s=turtle.Shape('compound')
t1=turtle.Turtle()
t1.up()
t1.color('dark blue')
t1.up()
t1.setheading(-10)
t1.goto(50,150)
t1.down()
t1.begin_poly()
t1.circle(-100,70)
t1.circle(-10,170)
t1.circle(100,60)
t1.circle(-12,210)
t1.end_poly()
m1=t1.get_poly()
s.addcomponent(m1,'white','dark blue')

t2=turtle.Turtle()
t2.up()
t2.color('dark blue')
t2.setheading(-100)
t2.goto(0,120)
t2.down()
t2.begin_poly()
t2.circle(-100,70)
t2.circle(-10,170)
t2.circle(100,60)
t2.circle(-12,250)
t2.end_poly()
m2=t2.get_poly()
s.addcomponent(m2,'white')

t5=turtle.Turtle()
t5.color('dark blue')
t5.up()
t5.setheading(-5)
t5.goto(40,170)
t5.down()

t5.begin_poly()
t5.circle(100,70)
t5.circle(10,170)
t5.circle(-100,60)
t5.circle(12,250)
t5.end_poly()
m5=t5.get_poly()
s.addcomponent(m5,'white')

t6=turtle.Turtle()
t6.color('dark blue')
t6.up()
t6.setheading(185)
t6.goto(-50,210)
t6.down()

t6.begin_poly()
t6.circle(100,70)
t6.circle(10,170)
t6.circle(-100,60)
t6.circle(12,250)
t6.end_poly()
m6=t6.get_poly()
s.addcomponent(m6,'white')

t3=turtle.Turtle()
t3.color('dark blue')
t3.up()
t3.setheading(-65)
t3.goto(-60,150)
t3.down()
t3.begin_poly()
t3.circle(60,175)
t3.fd(80)
t3.left(90)
t3.fd(90)
t3.left(90)
t3.end_poly()
m3=t3.get_poly()
s.addcomponent(m3,'red')

t4=turtle.Turtle()
t4.color('dark blue')
t4.up()
t4.goto(-20,220)
t4.down()
t4.begin_poly()
t4.circle(70,360)
t4.end_poly()
m4=t4.get_poly()
s.addcomponent(m4,'grey')


wn.register_shape('man',s)
t7=turtle.Turtle(shape='man')
t7.up()
t7.tilt(90)
t7.shapesize(0.3)
t7.goto(-500,-300)
#------------------------------------------

#Moon

t.up()
t.goto(0,-120)
t.down()
t.color('yellow','yellow')
t.begin_fill()
t.circle(120)
t.end_fill()
t.circle(120,20)
t.up()
t.fd(60)
t.down()
t.color('dark blue')
t.begin_fill()
t.circle(120)
t.end_fill()
#---------------------------------

#Astronaut 2
image1='astr1.gif'
wn.addshape(image1)

t8=turtle.Turtle()
t8.shape(image1)
t8.up()
q=0
#---------------------------

while True:
    
    starX=random.randint(-400,400)
    starY=random.randint(-400,400)
    starsize=random.randint(20,40)
    star1(starX,starY,starsize)    

    for m in range (250):
#while True:
    #q=q+1
    
    #if q%10==0:
        #stars1.clear()
    
    
        #star1(starX+300,starY-300,starsize)
        
    
    
        Merk.fd(5)
        #t7.fd(5)
        time.sleep(0.03)
        
        X=Merk.xcor()
        Y=Merk.ycor()
        t7.setposition(X+40,Y+60)
        t7.fd(60)
        t7.right(1)

        t8.setposition(X+290,Y+290)
        t8.fd(60)
        t8.right(5)


        if abs(X-600)<10 or abs(Y-600) <10:
            stars1.clear()
            Merk.goto(-600,-600)
            t7.goto(-600,-400)
        
            Merk.setheading(random.randint(20,70))
    

