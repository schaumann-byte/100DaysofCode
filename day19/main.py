from turtle import Turtle, Screen
import random

# tim = Turtle()
# screen = Screen()

# def move_fowards():
#     tim.forward(10)
#
# screen.listen()
# screen.onkey(key="space", fun=move_fowards) #quando se passa uma função como argumento, vc nao usa os parenteses da função do argumento
# screen.exitonclick()

#Make the etch a sketch game

# def move_fowards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def rotate_clockwise():
#     tim.right(10)
#
# def rotate_counter_clockwise():
#     tim.left(10)
#
# def clear_screen():
#     tim.reset()
#
# screen.listen()
# screen.onkeypress(key="w", fun=move_fowards)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="a", fun=rotate_counter_clockwise)
# screen.onkeypress(key="d", fun=rotate_clockwise)
# screen.onkey(key="c", fun=clear_screen)
#
# screen.exitonclick()

#Make the turtle racing game

ainda_tem_corrida = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Faça sua aposta", prompt="Qual turtle vai ganhar a corrida? Escolha uma cor: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.setposition(x=-230, y=-70 + 30*i)
    turtles.append(new_turtle)

if user_bet:
    ainda_tem_corrida =True

while ainda_tem_corrida:

    for turtle in turtles:
        if turtle.xcor() > 230:
            ainda_tem_corrida = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Vc ganhou! A tartaruga vencedora e {winning_color}")
            else:
                print(f"Vc perdeu! A tartaruga vencedora e {winning_color}")

        distance = random.randint(0, 10)
        turtle.forward(distance)

#editei
screen.exitonclick()