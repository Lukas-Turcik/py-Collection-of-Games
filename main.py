from snake_game import run_snake
from turtle_race_game import run_turtle_race
from pong_game import run_pong
from turtle_crossing import run_turtle_crossing
import tkinter as tk

def on_choice(choice):
    global root
    print(f"You chose: {choice}")
    if choice == "Turtle Race":
        run_turtle_race()
    elif choice == "Snake":
        run_snake()
    elif choice == "Pong (Q/A,Up/Down)":
        run_pong()
    elif choice == "Turtle Crossing":
        run_turtle_crossing()
    elif choice == "Quit":
        root.quit()

root = tk.Tk()
root.withdraw()  # Hide main window

dialog = tk.Toplevel(root)
dialog.title("Which game would you like to play?")


tk.Label(dialog, text="Choose a game:").pack(pady=10)

choices = ["Turtle Race", "Snake", "Pong (Q/A,Up/Down)", "Turtle Crossing","Quit"]
for choice in choices:
    tk.Button(dialog, text=choice, command=lambda c=choice: on_choice(c)).pack(fill="x", padx=30, pady=5)

root.mainloop()