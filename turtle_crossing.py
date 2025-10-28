import time
import turtle
from turtle import Screen

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

CAR_GENERATION_INTERVAL = 0

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
RANDOM_CHOICE = {1}

from turtle import Turtle
FONT = ("Courier", 20, "bold")

def run_turtle_crossing():
    screen = Screen()
    turtle.TurtleScreen._RUNNING = True
    screen.setup(width=600, height=600)
    screen.tracer(0)

    p =  Player()
    cm = CarManager()
    s = Scoreboard()

    screen.listen()
    screen.onkey(p.up, "Up")
    cm.generate_cars()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        cm.move_cars()
        cm.generate_cars()

        for car in cm.cars:
            if p.distance(car) < 20:
                s.game_over()
                screen.update()
                time.sleep(2)
                game_is_on = False
                screen.bye()

        if p.ycor() > 300:
            p.reset_player()
            s.level_up()
            cm.level += 1

class Player(Turtle):
    def __init__(self):
       super().__init__()
       self.penup()
       self.shape("turtle")
       self.setheading(90)
       self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)



class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        super().__init__()
        self.hideturtle()
        self.level = 0


    def generate_cars(self):
        random_chance = random.randint(1,6)
        if random_chance in RANDOM_CHOICE:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid = 1)
            new_car.goto(280,random.randint(-250,250))
            new_car.setheading(180)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*self.level)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)