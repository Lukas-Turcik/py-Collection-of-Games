import turtle
from turtle import Screen, Turtle
import time
import random
from datetime import datetime

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
ALIGN = "center"
FONT = ('Courier', 15, 'bold')

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_score(0)

    def update_score(self,i_score):
        self.score = i_score
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGN, font=FONT)
        with open("snake_score.txt","a") as file:
            file.write(f"Score: {str(self.score)} on {datetime.now().replace(microsecond=0)}" + "\n")

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

def run_snake():
    screen = Screen()
    turtle.TurtleScreen._RUNNING = True
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Moja hra Hadik")
    turtle.tracer(0)
    your_score = 0

    s = Snake()
    f = Food()
    sb = Scoreboard()


    screen.listen()
    screen.onkey(s.up, "Up")
    screen.onkey(s.down,"Down")
    screen.onkey(s.left,"Left")
    screen.onkey(s.right, "Right")



    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.15)
        s.move()

        if s.segments[0].distance(f) < 15:
            your_score += 1
            sb.update_score(your_score)
            f.refresh()
            s.extend()

        #detect collision with wall
        if s.segments[0].xcor() > 300 or s.segments[0].xcor() < -300\
            or s.segments[0].ycor() > 300 or s.segments[0].ycor() < -300:
            game_is_on = False
            sb.game_over()

        #detect collision with tail
        for segment in s.segments[1:]:
            if s.segments[0].distance(segment) < 10:
                game_is_on = False
                sb.game_over()

    screen.update()
    time.sleep(2)
    screen.bye()