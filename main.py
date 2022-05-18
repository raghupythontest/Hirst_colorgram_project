import colorgram
extracted_colors=colorgram.extract("hirst.jpg",30)
print(extracted_colors)
colors=[]
for color in extracted_colors:
    r=color.rgb[0]
    g=color.rgb[1]
    b=color.rgb[2]
    colors.append((r,g,b))
print(colors)

import turtle as t
import random as rd
t.colormode(255)
colors_list=[(235, 235, 241), (230, 222, 200), (235, 221, 229), (135, 162, 193), (66, 93, 121), (154, 79, 56), (211, 167, 109), (135, 184, 145), (76, 104, 85), (214, 83, 65), (225, 209, 110), (201, 150, 177), (215, 228, 216), (226, 165, 189), (31, 58, 74), (224, 79, 93), (69, 56, 46), (39, 63, 59), (141, 136, 109), (118, 125, 162), (78, 63, 45), (98, 141, 152), (56, 62, 78), (118, 160, 94), (173, 190, 215), (49, 71, 73), (227, 174, 166), (51, 70, 66), (176, 202, 182), (85, 57, 43)]
tim=t.Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for dot_count in range(1,100+1):
    tim.dot(20,rd.choice(colors_list))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=t.Screen()
screen.exitonclick()
