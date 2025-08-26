# program where turtle are racing randomly, and you have to bet on which one is winning
import turtle
import random
import time

WIDTH, HEIGHT = 500, 500
COLORS = ["red","green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]

def select_racers():  # function to select the number of racer
    racers = 0
    while True:
        racers = input("Select the number of racers (2 - 10): ")

        if racers.isdigit():
            racers = int(racers)

        else:
            print("You have to enter a numerical value!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Numbers must be in range 2 - 10, Try Again !!")

def race_colors(colors):  # 4- function where we have the racing
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT //2 - 10:
                return colors[turtles.index(racer)]



def create_turtles(colors): # 3 - define the turtles with the colors

    turtles = []
    spacingx = WIDTH // (len(colors) +1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 +((i+1)* spacingx), -HEIGHT // 2 + 20)  # defining the x position
        #since width = 500 it goes from -250 till 250$
        racer.pendown()

        turtles.append(racer)

    return turtles


def init_turtle():  # 2 Initialize the windows / console
    screen = turtle.Screen()
    screen.setup( WIDTH, HEIGHT)
    screen.title("Turtle Racing !!!")

print("*************************")
print("***** Turtle Racing ***** ")
print("*************************")

racers = select_racers()


random.shuffle(COLORS)
colors = COLORS[:racers]

print("Turtle colors that are participating: ")
print(colors)
guess = input("Guess the winning color: ")

init_turtle()
winner = race_colors(colors)
print(f"the winner is the turtle with the color: {winner.upper()}")
if guess == winner:
    print(" You have won !!!!")
else:
    print("Sorry, YOU LOSE !!!")
time.sleep(5)




