#!/usr/bin/env python3
"""Generator for the 26 November 2026 world-news image.

Build-time only (uses Pillow, which the grader does not have). The shipped
program is main.py, which copies assets/entry.png. Run: python3 draw.py
Writes assets/entry.png (1024x1024).
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
NAVY = (13, 32, 48)
CREAM = (247, 241, 227)
INK = (24, 32, 40)
AMBER = (232, 163, 61)
TEAL = (42, 157, 143)
RED = (192, 57, 43)
GREY = (92, 102, 112)
CARD = (255, 252, 244)

FD = "/usr/share/fonts/truetype/noto/"


def font(name, size):
    return ImageFont.truetype(FD + name, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading=6):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def kicker(draw, x, y, text, color):
    f = font("NotoSans-Bold.ttf", 21)
    draw.rectangle([x, y + 3, x + 26, y + 21], fill=color)
    draw.text((x + 36, y), text, font=f, fill=color)


def card(draw, box, kick, kick_color, head, body):
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=18, fill=CARD, outline=(214, 205, 184), width=2)
    kicker(draw, x0 + 22, y0 + 20, kick, kick_color)
    y = text_block(draw, x0 + 22, y0 + 56, head, font("NotoSans-Black.ttf", 32), INK, x1 - x0 - 44, 4)
    text_block(draw, x0 + 22, y + 6, body, font("NotoSans-Regular.ttf", 22), (52, 62, 72), x1 - x0 - 44, 5)


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 168], fill=(9, 24, 37))
    d.text((48, 26), "THE WORLD IN ONE DAY", font=font("NotoSans-Bold.ttf", 26), fill=AMBER)
    d.text((46, 58), "Thursday 26 November 2026", font=font("NotoSerif-Bold.ttf", 62), fill=CREAM)
    d.text((48, 130), "One image, one day of world news", font=font("NotoSans-Regular.ttf", 24), fill=(176, 190, 202))
    d.rectangle([0, 168, W, 176], fill=AMBER)

    # Lead panel: Thanksgiving storm / Macy's parade
    d.rounded_rectangle([32, 196, 992, 470], radius=20, fill=CREAM)
    kicker(d, 58, 218, "UNITED STATES  ·  WEATHER", RED)
    y = text_block(d, 58, 254, "Storm stops the 100th Macy's parade", font("NotoSans-Black.ttf", 52), INK, 560, 4)
    text_block(d, 58, y + 10,
               "Heavy rain and 60 mph gusts hit New York on Thanksgiving. "
               "The parade moves to Saturday.",
               font("NotoSans-Regular.ttf", 25), (52, 62, 72), 545, 6)
    # skyline + balloon + rain (right side of lead panel)
    bx = 660
    for i, hgt in enumerate([120, 170, 95, 150, 110]):
        x = bx + i * 62
        d.rectangle([x, 430 - hgt, x + 48, 430], fill=(52, 74, 94))
        for wy in range(430 - hgt + 14, 420, 26):
            d.rectangle([x + 10, wy, x + 20, wy + 12], fill=(240, 200, 110))
            d.rectangle([x + 28, wy, x + 38, wy + 12], fill=(240, 200, 110))
    d.ellipse([742, 216, 842, 292], fill=RED)
    d.polygon([(770, 288), (814, 288), (792, 330)], fill=(120, 84, 40))
    d.line([(792, 330), (792, 352)], fill=INK, width=3)
    d.rectangle([774, 352, 810, 374], fill=(120, 84, 40))
    for rx in range(650, 980, 34):
        for ry in range(210, 300, 42):
            d.line([(rx, ry), (rx - 10, ry + 22)], fill=(90, 140, 180), width=3)

    # Middle cards
    card(d, [32, 490, 344, 742], "CHESS  ·  GENEVA", TEAL,
         "World title: Game 3 today",
         "Gukesh (India) vs Sindarov (Uzbekistan). Two draws so far — tied 1–1.")
    card(d, [356, 490, 668, 742], "HONG KONG  ·  TODAY", RED,
         "168 remembered",
         "One year on, survivors return to Wang Fuk Court today.")
    card(d, [680, 490, 992, 742], "SPORT  ·  NFL TODAY", (38, 92, 150),
         "Thanksgiving tripleheader",
         "Bears at Lions · Eagles at Cowboys · Chiefs at Bills — three games today.")

    # Bottom row: India + today strip
    card(d, [32, 758, 500, 930], "INDIA  ·  TODAY", (196, 110, 30),
         "Constitution Day",
         "India marks Samvidhan Divas, the day its constitution was adopted in 1949.")
    d.rounded_rectangle([512, 758, 992, 930], radius=18, fill=(19, 47, 68), outline=AMBER, width=2)
    d.text((538, 780), "TODAY AT A GLANCE", font=font("NotoSans-Bold.ttf", 24), fill=AMBER)
    lines = [
        "US markets closed for Thanksgiving",
        "Macy's parade: Saturday 28 Nov",
        "Black Friday sales begin tomorrow",
    ]
    yy = 818
    for ln in lines:
        d.ellipse([540, yy + 8, 552, yy + 20], fill=AMBER)
        d.text((566, yy), ln, font=font("NotoSans-Regular.ttf", 24), fill=CREAM)
        yy += 36

    # Footer
    d.text((48, 958), "All stories are events of 26 November 2026  ·  Compiled in the first hours of the UTC day",
           font=font("NotoSans-Regular.ttf", 21), fill=(176, 190, 202))

    img.save("assets/entry.png", optimize=True)
    print("wrote assets/entry.png")


if __name__ == "__main__":
    main()
