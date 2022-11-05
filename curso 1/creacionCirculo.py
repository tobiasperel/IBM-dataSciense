import turtle

t = turtle.Turtle()

# radius for smallest circle
r = 10

# number of circles
n = 100

# loop for printing tangent circles
for i in range(1, n + 1, 1):
    t.circle(r * i)