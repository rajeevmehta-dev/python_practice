# from turtle import Turtle, Screen
import random
import turtle as t
import colorgram

colors = colorgram.extract("spot.jpg", 30)
rgb_colors = []
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

timmy_the_turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# for _ in range(0, 4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)
# for _ in range(0, 100):
#     timmy_the_turtle.forward(2)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(2)
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(2)
# screen.exitonclick()
num_slides = 10

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


# def draw_share(sides):
#     angle = 360 / sides
#     for _ in range(0, sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_share(shape_side_n)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


#
#
# print(type(random_color()))
#
# directions = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("normal")
# for _ in range(0, 200):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))
timmy_the_turtle.speed("fastest")

# def draw_spiral_graph(size):
#     for _ in range(int(360 / size)):
#         timmy_the_turtle.color(random.choice(rgb_colors))
#         timmy_the_turtle.circle(100)
#         timmy_the_turtle.setheading(timmy_the_turtle.heading() + 5)
#
#
# draw_spiral_graph(5)

timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy_the_turtle.dot(20, random.choice(rgb_colors))
    timmy_the_turtle.forward(50)

    if dot_count % 10 == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(50)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(500)
        timmy_the_turtle.setheading(0)

screen.exitonclick()
