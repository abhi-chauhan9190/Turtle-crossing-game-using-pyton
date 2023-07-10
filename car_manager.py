from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) :
        self.all_cars=[]
        self.carb=5

    def create(self):
        random_c=random.randint(1,6)
        if random_c==1:
            ncar=Turtle()
            ncar.shape("square")
            ncar.shapesize(1,2)
            ncar.penup()
            ncar.color(random.choice(COLORS))
            ny=random.randint(-250,250)
            ncar.goto(300,ny)
            self.all_cars.append(ncar)  
    def move_Car(self):
        for car in self.all_cars:
            car.backward(self.carb)  
    def level_up(self):
        self.carb+=2

    
