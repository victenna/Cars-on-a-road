import turtle
import time
wn=turtle.Screen()
wn.setup(1000,500)
turtle.tracer(4)
def object(img,X,Y):
    wn.addshape(img)
    t=turtle.Turtle(img)
    t.up()
    t.goto(X,Y)
    return t
street=object('street.gif',-500,0)
car1=object('car_1.gif',600,-170)
car2=object('car_2.gif',600,-80)

while True:
    wn.update()
    street.fd(2)
    car1.fd(-2)
    car2.fd(-1.5)
    if car1.xcor()<-500:
        car1.goto(600,-170)
    if car2.xcor()<-510:
        car2.goto(600,-80)
    if street.xcor()>490:
        street.goto(-490,0)
    time.sleep(0.01)
    
    

   
   
        
        

        

