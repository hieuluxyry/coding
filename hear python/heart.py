import turtle
import time

# Thiết lập màn hình
screen = turtle.Screen()
screen.setup(1800, 800)
screen.bgcolor("pink")
screen.title("Draw Heart")

# Tạo đối tượng con rùa
heart = turtle.Turtle()
heart.hideturtle()
heart.speed(1000)

# Hàm vẽ trái tim
def draw_heart(x, y, size, color, thickness):
    heart.penup()
    heart.goto(x, y)
    heart.setheading(0)
    heart.color(color)
    heart.pensize(thickness)
    heart.pendown()
    heart.begin_fill()
    heart.left(140)
    heart.forward(size)

    for _ in range(200):
        heart.right(1)
        heart.forward(size * 0.009)

    heart.left(120)

    for _ in range(200):
        heart.right(1)
        heart.forward(size * 0.009)

    heart.forward(size)
    heart.end_fill()

# Danh sách các thông số để vẽ trái tim
hearts = [
    (0, -150, 300, "#FF9999", 5),
    (0, -135, 270, "#FFCCCC", 5),
    (0, -120, 240, "#FFE6E6", 5),
    (0, -105, 210, "#FFCCCC", 5),
    (0, -90, 180, "#FF99CC", 5),
    (0, -75, 150, "#FFCCFF", 5),
    (0, -50, 100, "#FF6666", 5)
]

# Vẽ các trái tim
for heart_params in hearts:
    draw_heart(*heart_params)
    time.sleep(0.5)

# Viết lời chúc
heart.penup()
screen_width = screen.window_width()
heart.goto(0, -250)
heart.color('red')
heart.pendown()
heart.write(
    "Wishing you a life of silk and velvet.\n"
    "Spring full of happiness, Summer overflowing with love.\n"
    "May you fall in love with a kind person and marry someone talented,\n"
    "With just the right amount of boys and girls, living a peaceful life.",
    font=("Times New Roman", 15),
    align="center"
)
# Giữ màn hình mở
screen.mainloop()

