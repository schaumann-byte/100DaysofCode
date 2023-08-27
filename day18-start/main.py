import random
from turtle import Turtle, Screen, colormode
from random import randint

timmy = Turtle()
#timmy.shape("turtle")

#Draw a square

# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

#Draw a Dashed line
# for i in range(20):
#     timmy.fd(10)
#     timmy.penup()
#     timmy.fd(10)
#     timmy.pendown()

#Draw various polygons random color
# colormode(255)
# for i in range(3, 20):
#     timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     for j in range(i):
#         timmy.forward(100)
#         timmy.right(360/i)

#Draw a random walk

# colormode(255)
# timmy.pensize(10)
# timmy.speed("fastest")
# angles = [0, 90, 180, 270]
#
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return r, g, b
#
# for i in range(1000):
#     rcolor = random_color()
#     timmy.color(rcolor)
#     timmy.setheading(random.choice(angles)) #eu tinha colocado timmy.right
#     timmy.fd(20)

#Draw a Spirograph

# colormode(255)
# timmy.speed("fastest")
#
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return r, g, b
#
# def draw_spirograph(size):
#     for i in range(int(360/size)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size)
#
# draw_spirograph(1)

#Create Hirst Paiting

# import colorgram
# colors = []
# colors_extracted = colorgram.extract('image.jpg', 30)
# for color in colors_extracted:
#     colors.append(tuple(color.rgb))
#
# print(colors)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
colormode(255)
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()
timmy.setposition(-250,-250)

for i in range(10):
    for j in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.setposition(timmy.xcor()+50, timmy.ycor())
    timmy.setposition(timmy.xcor() - 500, timmy.ycor() + 50)


screen = Screen()
screen.exitonclick()
