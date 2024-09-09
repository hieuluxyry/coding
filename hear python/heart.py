import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("pink")
screen.title("Draw Heart")

# Tạo đối tượng con rùa
heart = turtle.Turtle()
heart.hideturtle()
turtle.tracer(2)


# Hàm vẽ trái tim
def draw_heart(x, y, size, color, thickness):
    heart.penup()
    heart.goto(x, y)
    heart.setheading(140)
    heart.color(color)
    heart.pensize(thickness)
    heart.pendown()
    heart.begin_fill()
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
    (0, -150, 300, "#FFC0CB", 5),  # Light Pink
    (0, -135, 270, "#FF69B4", 5),  # Hot Pink
    (0, -120, 240, "#0000FF", 5),  # Blue
    (0, -105, 210, "#00FF00", 5),  # Green
    (0, -90, 180, "#FFA500", 5),  # Orange
    (0, -75, 150, "#FFFF00", 5),  # Yellow
    (0, -50, 100, "#FF0000", 5)  # Red
]

# Vẽ các trái tim
for heart_params in hearts:
    draw_heart(*heart_params)

# Viết lời chúc
heart.penup()
heart.goto(0, -250)
heart.color('red')
heart.pendown()
heart.write(
    " Quynh Anh ,I Love You Very Much",
    font=("Times New Roman", 15, "italic"),
    align="center"
)
# Giữ màn hình mở
screen.mainloop()
