import turtle

s = turtle.Screen()
t = turtle.Turtle()

colors = ['violet','indigo','blue','green','yellow','orange','red']

s.bgcolor("black")
t.speed("fastest")
t.hideturtle()

while True:
    for x in range(200):
        t.pencolor(colors[x%len(colors)])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(60)

    t.right(240)

    for x in range(200,0,-1):
        t.pencolor('black')
        t.width(x/100 + 7)
        t.forward(x)
        t.right(60)