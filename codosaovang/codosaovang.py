import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Codosaovang")
screen.setup(width=800, height=500)
screen.bgcolor('red')

# Set up the turtle for drawing the star
star_turtle = turtle.Turtle()
star_turtle.speed(5)
star_turtle.color('yellow')

# Set up the turtle for writing text
text_turtle = turtle.Turtle()
text_turtle.penup()
text_turtle.hideturtle()
text_turtle.color('white')


# Function to draw a star and display text progressively
def draw_star(turtle, x, y, length, text, text_turtle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    for i in range(5):
        turtle.forward(length)
        turtle.right(144)
        time.sleep(0.4)

        # Progressively display the text
        text_progress = int((i + 1) * len(text) / 5)
        current_text = text[:text_progress]
        text_turtle.clear()
        text_turtle.goto(0, -200)
        text_turtle.write(current_text, align='center', font=('Arial', 24, 'bold'))

    turtle.end_fill()


# Star size and position
star_size = 150
center_x = -star_size / 2
center_y = star_size / 4

# Text to display
display_text = "Chào Mừng Quốc Khánh 2/9"

# Draw the star
draw_star(star_turtle, center_x, center_y, star_size, display_text, text_turtle)

# Hide the turtle after drawing
star_turtle.hideturtle()

# Keep the window open until it is closed by the user
turtle.done()
