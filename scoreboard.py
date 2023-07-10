from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.level=0
        self.hideturtle()
        self.penup()
        self.goto(-280,257)
        self.updates()
        
    def updates(self):
        self.clear()
        self.write(f"Level : {self.level}" , align='left' , font=FONT)

    def increse_level(self):    
        self.level+=1
        self.updates()
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER" , align='center' , font= FONT)    
    
