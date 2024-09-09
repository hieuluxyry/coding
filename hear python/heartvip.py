import random
from math import sin, cos, pi, log
from tkinter import *

# Kích thước canvas (tự động lấy theo kích thước màn hình)
root = Tk()
canvas_width = root.winfo_screenwidth()
canvas_height = root.winfo_screenheight()
canvas_center_x = canvas_width / 2
canvas_center_y = canvas_height / 2
image_enlarge = 11
heart_color = 'red'

# Hàm tạo hình trái tim
def heart_function(t, shrink_ratio: float = image_enlarge):
    x = 16 * (sin(t) ** 3)
    y = -(15 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))
    x *= shrink_ratio
    y *= shrink_ratio
    x += canvas_center_x
    y += canvas_center_y
    return int(x), int(y)

# Hàm phân tán điểm bên trong trái tim
def scatter_inside(x, y, beta=0.15):
    ratio_x = -beta * log(random.random())
    ratio_y = -beta * log(random.random())
    dx = ratio_x * (x - canvas_center_x)
    dy = ratio_y * (y - canvas_center_y)
    return x - dx, y - dy

# Hàm thu nhỏ trái tim
def shrink(x, y, ratio):
    force = 1 / (((x - canvas_center_x) ** 2) + ((y - canvas_center_y) ** 2)) ** 0.6
    dx = ratio * force * (x - canvas_center_x)
    dy = ratio * force * (y - canvas_center_y)
    return x - dx, y - dy

# Hàm tạo đường cong
def curve(p):
    return 2 * (2 * sin(4 - p)) / (2 * pi)

# Lớp Heart quản lý việc vẽ trái tim
class Heart:
    def __init__(self, generate_frame=20):
        self._points = set()
        self._edge_diffusion_points = set()
        self._center_diffusion_points = set()
        self.all_points = {}
        self.build(2000)
        self.random_halo = 1000
        self.generate_frame = generate_frame
        for frame in range(generate_frame):
            self.calc(frame)

    # Xây dựng các điểm cho trái tim
    def build(self, number):
        for _ in range(number):
            t = random.uniform(0, 2 * pi)
            x, y = heart_function(t)
            self._points.add((x, y))

        for _x, _y in list(self._points):
            for _ in range(3):
                x, y = scatter_inside(_x, _y, 0.3)
                self._edge_diffusion_points.add((x, y))

        point_list = list(self._points)
        for _ in range(4000):
            x, y = random.choice(point_list)
            x, y = scatter_inside(x, y, 0.2)
            self._center_diffusion_points.add((x, y))

    # Tính toán vị trí
    @staticmethod
    def calc_position(x, y, ratio):
        force = 1 / (((x - canvas_center_x) ** 2) + ((y - canvas_center_y) ** 2)) ** 0.520
        dx = ratio * force * (x - canvas_center_x) + random.randint(-2, 2)
        dy = ratio * force * (y - canvas_center_y) + random.randint(-2, 2)
        return x - dx, y - dy

    # Tính toán các điểm để vẽ trái tim
    def calc(self, generate_frame):
        ratio = 15 * curve(generate_frame / 15 * pi)
        halo_radius = int(4 + 6 * (1 + curve(generate_frame / 15 * pi)))
        halo_number = int(3000 + 4000 * abs(curve(generate_frame / 15 * pi) ** 2))
        all_points = []
        heart_halo_point = set()

        for _ in range(halo_number):
            t = random.uniform(0, 2 * pi)
            x, y = heart_function(t, shrink_ratio=11.5)
            x, y = shrink(x, y, halo_radius)
            heart_halo_point.add((x, y))

        for x, y in self._points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        for x, y in self._edge_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        self.all_points[generate_frame] = all_points

    # Vẽ trái tim trên canvas
    def render(self, render_canvas, render_frame):
        for x, y, size in self.all_points[render_frame % self.generate_frame]:
            render_canvas.create_rectangle(x, y, x + size, y + size, width=0, fill=heart_color)

# Hàm vẽ trái tim
def draw(main: Tk, render_canvas: Canvas, render_heart, render_frame=0):
    render_canvas.delete("all")
    render_heart.render(render_canvas, render_frame)
    main.after(160, draw, main, render_canvas, render_heart, render_frame + 1)

# Điểm bắt đầu chương trình
if __name__ == "__main__":
    root.title("Heart VIP")
    canvas = Canvas(root, bg='pink', width=canvas_width, height=canvas_height)
    canvas.pack(expand=YES, fill=BOTH)
    heart = Heart()
    draw(root, canvas, heart)
    root.mainloop()
