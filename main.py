from turtle import Turtle, Screen
import heroes
import random

tim = Turtle()
tim.shape("turtle")
tim.color("blue")


# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)
#
# print(heroes.gen())

# for _ in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# #triangle
# for _ in range(3):
#     tim.pencolor((100.0, 200.0, 255.0))
#     tim.forward(100)
#     tim.right(120)
#
# #square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# tim.forward(100)
#
# #pentagon
# for _ in range(5):
#     tim.right(72)
#     tim.forward(100)
#
#
# #hexagon
# for _ in range(6):
#     tim.right(60)
#     tim.forward(100)
#
# #heptagon
# for _ in range(7):
#     tim.right(51.428571428571428571428571428571)
#     tim.forward(100)
#
# #octagon
# for _ in range(8):
#     tim.right(45)
#     tim.forward(100)
#
# #nonagon
# for _ in range(9):
#     tim.right(40)
#     tim.forward(100)
#
# for _ in range(10):
#     tim.right(36)
#     tim.forward(100)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360/ num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

#iterates through range of numbers that corresponds to sides of shape.
#3 for triangle
#4 for square
#5 for pentago ... etc.
for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
























screen = Screen()
screen.exitonclick()



