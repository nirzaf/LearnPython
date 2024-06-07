import tkinter as tk
import turtle

my_turtle = None  # Define my_turtle as a global variable

def move_forward():
    my_turtle.forward(100)

def turn_left():
    my_turtle.left(90)

def turn_right():
    my_turtle.right(90)

def move_backward():
    my_turtle.backward(100)

def main():
    global my_turtle  # Declare my_turtle as a global variable

    root = tk.Tk()
    root.title("Turtle Command Game")

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    turtle_screen = turtle.TurtleScreen(canvas)
    turtle_screen.bgcolor("white")

    my_turtle = turtle.RawTurtle(turtle_screen)
    my_turtle.shape("turtle")
    my_turtle.color("green")

    forward_button = tk.Button(root, text="Forward", command=move_forward)
    forward_button.pack(side=tk.LEFT)

    left_button = tk.Button(root, text="Left", command=turn_left)
    left_button.pack(side=tk.LEFT)

    right_button = tk.Button(root, text="Right", command=turn_right)
    right_button.pack(side=tk.LEFT)

    backward_button = tk.Button(root, text="Backward", command=move_backward)
    backward_button.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()
