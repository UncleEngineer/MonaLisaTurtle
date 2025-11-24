import turtle
from PIL import Image

# --------------------------
# 1) ตั้งค่ารูปภาพ
# --------------------------
IMAGE_PATH = "monalisa.jpg"
WIDTH = 80
HEIGHT = 120
DOT_SIZE = 6

# --------------------------
# 2) โหลดรูปภาพ
# --------------------------
img = Image.open(IMAGE_PATH).convert("RGB")
img = img.resize((WIDTH, HEIGHT))

# --------------------------
# 3) ตั้งค่า turtle
# --------------------------
turtle.colormode(255)
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
turtle.penup()

# ปิด animation เพื่อให้วาดเร็วขึ้นหลายเท่า
turtle.tracer(False)
# turtle.tracer(20) #ให้เจนภาพช้าลง อัพเดทครั้งละ 20 จุด

start_x = -WIDTH * DOT_SIZE / 2
start_y = HEIGHT * DOT_SIZE / 2

# --------------------------
# 4) วาดแบบรวดเร็ว
# --------------------------
for y in range(HEIGHT):
    for x in range(WIDTH):
        r, g, b = img.getpixel((x, y))
        turtle.pencolor(r, g, b)
        turtle.goto(start_x + x * DOT_SIZE, start_y - y * DOT_SIZE)
        turtle.dot(DOT_SIZE)

# เปิดอัปเดตหน้าจอครั้งเดียวหลังวาดเสร็จ
turtle.update()

turtle.done()
