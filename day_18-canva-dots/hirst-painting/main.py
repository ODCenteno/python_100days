import colorgram
import turtle as t
from turtle import Screen
from random import choice

# colors = colorgram.extract("image.jpeg", 30)
# rgb_colors = []
# for color in colors:
#     if color.rgb.r < 240:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         new_color = (r, g, b)
#         rgb_colors.append(new_color)
#
# print(f'Raw colors:{colors} \nLooper colors{rgb_colors}')
colors_list = [(226, 234, 243), (232, 243, 237), (204, 159, 102), (232, 212, 103), (46, 103, 141), (146, 80, 59), (132, 168, 192), (198, 140, 162), (145, 67, 85), (25, 39, 54), (173, 159, 53), (202, 91, 71), (140, 179, 153), (191, 89, 119), (61, 117, 95), (24, 44, 36), (222, 172, 187), (61, 44, 31), (47, 159, 181), (90, 155, 107), (238, 212, 7), (227, 175, 167), (41, 59, 101), (16, 95, 74), (178, 188, 213), (63, 33, 43), (103, 124, 164), (106, 42, 56)]
t.colormode(255)

def painting():
    """Generates a canvas with coloured dots using turtle modules"""
    # canvas 10 x 10 rows of spots
    # size of dots: 20
    # spaced apart by 50

    brush = t.Turtle()
    brush.hideturtle()
    brush.speed('fastest')
    brush.pensize(20)
    brush.penup()
    paint = 10
    x = -220
    y = -220

    while paint > 0:
        brush.goto(x, y)

        for _ in range(10):
            brush.dot(20, choice(colors_list))
            brush.penup()
            brush.forward(50)
        y = y + 50
        paint -= 1



if __name__ == '__main__':
    painting()
    screen = Screen()
    screen.screensize(800, 800)
    screen.exitonclick()
