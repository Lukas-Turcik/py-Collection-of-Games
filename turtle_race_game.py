from turtle import Turtle, Screen
import turtle
import random
import tkinter.messagebox as messagebox

def show_yes_no_box():
    response = messagebox.askyesno("Question", "Play again?")
    return response

def run_turtle_race():
    import turtle
    is_game_on = True
    screen = Screen()
    screen.title("Turtle Race")
    turtle.TurtleScreen._RUNNING = True

    while is_game_on:
        is_race_on = False
        screen.setup(width=500, height=400)
        user_bet = screen.textinput(title="Your bet", prompt="Which turtle is going to win? Guess a color: ")
        colors = ["red","orange","yellow","green","blue","purple"]
        all_turtles = []

        for _ in range(6):
            y_c = int(-100 + _*30)
            tim = Turtle(shape="turtle")
            tim.penup()
            tim.color(colors[_])
            tim.goto(x=-230, y=-y_c)
            all_turtles.append(tim)

        if user_bet:
            is_race_on = True

        while is_race_on:
            for turtle in all_turtles:
                if turtle.xcor() > 230:
                    is_race_on = False
                    winning_color = turtle.pencolor()
                    if winning_color == user_bet:
                        print(f"You won! {winning_color} is the winning turtle.")
                        messagebox.showinfo("End of race.", f"Hooray! You won! {winning_color.capitalize()} is the winning turtle.")
                        break
                    else:
                        print(f"You lost! {winning_color} is the winning turtle.")
                        messagebox.showinfo("End of race.", f"Too bad, you lost! Try your luck again. {winning_color.capitalize()} is the winning turtle.")
                        break

                rand_distance = random.randint(0,10)
                turtle.forward(rand_distance)

        if show_yes_no_box():
            is_game_on = True
        else:
            is_game_on = False

        screen.clear()

    #screen.exitonclick()
    screen.bye()