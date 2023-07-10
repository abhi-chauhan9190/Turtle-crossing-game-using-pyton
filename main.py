import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
plr=Player()
screen.listen()
screen.onkey(plr.goup,"Up")
car_manage=CarManager()
scrb=Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manage.create()
    car_manage.move_Car()
    for i in car_manage.all_cars:
        
        if i.distance(plr)<20:
            scrb.gameover()
            game_is_on=False

    if plr.ycor()>280:
        plr.goto(0,-280)  
        car_manage.level_up() 
        scrb.increse_level()

screen.exitonclick()