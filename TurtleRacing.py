import string
import turtle
import time
import random

WIDTH, HEIGHT = 500,500
COLORS = ['blue', 'red', 'black', 'purple', 'yellow', 'orange', 'gold', 'brown', 'cyan', 'pink']

def get_number_racers():
    racers = 0
    while True:
        Racer_num = input("Input the number of racers (2-10): ")
        if Racer_num.isdigit():
            Racer_num = int(Racer_num)
        else:
            print("Must input numeric !!")
            continue

        if 2 <= Racer_num <= 10:
            return Racer_num
        else:
            print("Must with in 2 to 10")

def race(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtle(colors):
    turtles = []
    distance = WIDTH // (len(colors) + 1)


    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        #####set posistion
        racer.setpos(-WIDTH//2 + (i + 1) * distance, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_game():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")


Run = get_number_racers()
init_game()

random.shuffle(COLORS)
colors = COLORS[:Run]

winner = race(colors)
print ("winner is ", winner)
time.sleep (5)

#turtle.done()
