import turtle as t
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

# # 사각형 그리기
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)



# # 점선 그리기
# def draw_dash(obj, length):
#     for i in range(int(length/10)):
#         obj.forward(5)
#         obj.penup()
#         obj.forward(5)
#         obj.pendown()
#
# draw_dash(timmy_the_turtle, 200)



# # 여러 도형 겹쳐 그리기
# color_list = ['blue', 'red', 'green', 'yellow', 'orange', 'purple', 'pink', 'gray', 'ivory', 'lavender blush']
#
# for i in range(3, 11):
#     for j in range(i):
#         timmy_the_turtle.pencolor(color_list[i-3])
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/i)



# # 무작위 행보
# def random_walk(num_of_times):
#     timmy_the_turtle.speed(0)
#     timmy_the_turtle.pensize(10)
#     for i in range(num_of_times):
#         timmy_the_turtle.pencolor(random.choice(color_list))
#         angle = random.randint(0, 3) * 90
#         timmy_the_turtle.setheading(angle)
#         timmy_the_turtle.forward(50)
#
#
# color_list = ['turquoise', 'medium spring green', 'yellow green', 'cornflower blue', 'medium orchid',
#               'purple', 'coral', 'aquamarine', 'burlywood', 'dark gray', 'khaki']
#
#
# random_walk(200)



# # 무작위 색상과 무작위 행보
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
#
# def random_walk(num_of_times):
#     timmy_the_turtle.speed(0)
#     timmy_the_turtle.pensize(10)
#     for i in range(num_of_times):
#         color = random_color()
#         timmy_the_turtle.pencolor(color)
#         angle = random.randint(0, 3) * 90
#         timmy_the_turtle.setheading(angle)
#         timmy_the_turtle.forward(50)
#
# random_walk(200)



# 스피로그래프 그리기
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(num_of_circles):
    timmy_the_turtle.shape('circle')
    timmy_the_turtle.shapesize(0.1,0.1,0.1)
    timmy_the_turtle.speed(0)
    for i in range(num_of_circles):
        timmy_the_turtle.pencolor(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.left(360/num_of_circles)

draw_spirograph(50)






screen = t.Screen()
screen.exitonclick()