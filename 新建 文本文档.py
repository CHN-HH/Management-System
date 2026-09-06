import turtle
from random import random, randint


def get_screen_width(width, height, color, speed):
    screen_obj = turtle.Screen()
    screen_obj.screensize(width, height, bg=color)
    screen_obj.setup(1.0, 1.0)
    screen_obj.tracer(speed)
    return screen_obj


def draw_petal(turtle_obj, flower):
    for i in range(int(flower / 2)):
        x = flower - 2 * flower * random()
        y = 10 - 20 * random()
        turtle_obj.penup()
        turtle_obj.forward(y)
        turtle_obj.left(90)
        turtle_obj.forward(x)
        turtle_obj.pendown()
        turtle_obj.pencolor("lightcoral")
        turtle_obj.circle(1)
        turtle_obj.penup()
        turtle_obj.backward(x)
        turtle_obj.right(90)
        turtle_obj.backward(y)
        turtle_obj.pendown()


def draw_tree(turtle_obj, branch, tree_color):
    # 递归出口：树枝长度<=0立刻返回，防止负数
    if branch <= 0:
        return

    if branch < 8:
        if randint(0, 1) == 0:
            turtle_obj.pencolor("snow")
        else:
            turtle_obj.pencolor("lightcoral")
        turtle_obj.pensize(max(1, branch / 2))
    elif 8 <= branch <= 16:
        if randint(0, 2) == 0:
            turtle_obj.pencolor("snow")
        else:
            turtle_obj.pencolor("lightcoral")
        turtle_obj.pensize(max(1, branch / 4))
    else:
        turtle_obj.pencolor(tree_color)
        turtle_obj.pensize(max(1, branch / 10))

    turtle_obj.forward(branch)
    a = 1.5 * random()
    turtle_obj.right(20 * a)
    b = 1.5 * random()
    draw_tree(turtle_obj, branch - 10 * b, tree_color)
    turtle_obj.left(40 * a)
    draw_tree(turtle_obj, branch - 10 * b, tree_color)
    turtle_obj.right(20 * a)

    turtle_obj.penup()
    turtle_obj.backward(branch)
    turtle_obj.pendown()

def trees(tree_num):
    color = ['brown', 'tan', 'black']
    for j in range(tree_num):
        tree_color = color[randint(0, len(color) - 1)]
        pensize = randint(2, 5)
        forward = ((-1) ** pensize) * pensize * randint(20, 50)
        if pensize <= 3:
            backward = ((-1) ** pensize) * (5 - pensize) * randint(10, 50)
        else:
            backward = pensize * randint(45, 50)
        turtle_obj = turtle.Turtle()
        turtle_obj.pensize(pensize)
        turtle_obj.penup()
        turtle_obj.forward(forward)
        turtle_obj.left(90)
        turtle_obj.backward(backward)
        turtle_obj.pendown()
        turtle_obj.pencolor(tree_color)
        branch = pensize * 15
        flowers = branch
        draw_tree(turtle_obj, branch, tree_color)
        draw_petal(turtle_obj, flowers)


if __name__ == "__main__":
    screen = get_screen_width(800, 600, "#111111", 0)
    trees(3)
    turtle.done()
