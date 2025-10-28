from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center", font=("Courier", 60, "bold"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,coordinates):
        super().__init__()
        self.hideturtle()
        self.coordinates = coordinates
        self.direction = +20
        self.color("white")
        self.penup()
        self.goto(self.coordinates)
        self.showturtle()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move(self):
        new_y = self.ycor()+self.direction
        self.goto(self.xcor(),new_y)

    def up(self):
        self.direction = +20
        self.move()

    def down(self):
        self.direction = -20
        self.move()

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.x_direction = 10
        self.y_direction = 10
        self.color("white")
        self.penup()
        self.showturtle()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor()+self.x_direction
        new_y = self.ycor()+self.y_direction
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_direction *= -1

    def bounce_x(self):
        self.x_direction *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.hideturtle()
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
        self.showturtle()

from turtle import Screen
import time
import turtle

def run_pong():
    screen = Screen()
    turtle.TurtleScreen._RUNNING = True
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")

    sb = Scoreboard()
    r_p = Paddle((350, 0))
    l_p = Paddle((-350, 0))
    b = Ball()


    screen.listen()
    screen.onkey(r_p.up, "Up")
    screen.onkey(r_p.down, "Down")

    screen.onkey(l_p.up, "q")
    screen.onkey(l_p.down, "a")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(b.move_speed)
        b.move()

        #Detect collision with wall
        if b.ycor() > 280 or b.ycor() < -280:
            b.bounce_y()

        #Detect collision with paddle
        if (b.distance(r_p) < 50 and b.xcor() > 320) or (b.distance(l_p) < 50 and b.xcor() < -320):
            b.bounce_x()

        #detect r_paddle miss
        if b.xcor() > 380:
            b.reset_position()
            sb.l_point()

        #detect l_paddle miss
        if b.xcor() < -380:
            b.reset_position()
            sb.r_point()

    screen.exitonclick()