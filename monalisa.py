import turtle
from PIL import Image

# --------------------------
# 1) ตั้งค่ารูปภาพ
# --------------------------
IMAGE_PATH = "monalisa.jpg"  # <-- แก้ชื่อไฟล์ตามจริงได้
WIDTH = 80      # จำนวน pixel แนวนอนหลัง resize
HEIGHT = 120    # จำนวน pixel แนวตั้งหลัง resize
DOT_SIZE = 6    # ขนาดจุดของ turtle (ลองปรับได้)

# --------------------------
# 2) โหลดและเตรียมรูป
# --------------------------
img = Image.open(IMAGE_PATH).convert("RGB")
img = img.resize((WIDTH, HEIGHT))  # ย่อรูปให้เล็กลงจะได้วาดไม่ช้าเกินไป

# --------------------------
# 3) ตั้งค่า turtle
# --------------------------
turtle.colormode(255)
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
turtle.penup()

# ให้รูปอยู่กลางจอ
start_x = -WIDTH * DOT_SIZE / 2
start_y = HEIGHT * DOT_SIZE / 2

# --------------------------
# 4) วาดภาพจาก pixel ทีละจุด
# --------------------------
for y in range(HEIGHT):
    for x in range(WIDTH):
        r, g, b = img.getpixel((x, y))
        turtle.pencolor(r, g, b)
        turtle.goto(start_x + x * DOT_SIZE, start_y - y * DOT_SIZE)
        turtle.dot(DOT_SIZE)  # วาดจุดสี

turtle.done()
