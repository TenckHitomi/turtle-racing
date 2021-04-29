import turtle
import time 
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
    """Input number of turtles you want to show up on the screen"""
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit(): #Checks if the input is a digit for # of racers. If not prompts for another input
            racers = int(racers)
        else:
            print('Input is not numeric... Try again.')
            continue

        if 2 <= racers <= 10: #Checks input of user to see if it falls between 2 & 10
            return racers
        else:
            print('Number not in range of 2-10...Try again.')

def race(colors): #Create colored turtles
    turtles = create_turtles(colors)

    while True: #Randomly pass a range through each turtle to determine pixels it moves. The further apart the bigger the gap.
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos() #Returns index of first turtle to cross the finish line and returns color value
            if y >= HEIGHT // 2 -10:
                return colors[turtles.index(racer)]

def create_turtles(colors): #Creates Turtle list and evenly spaces each turtle on the screen from each other. 
    turtles = []
    spacingx = WIDTH // len(colors) + 1
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90) #Rotates the turtles to look up on the screen
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    """Produces window on screen"""
    screen = turtle.Screen()
    screen.setup(WIDTH , HEIGHT)
    screen.title('Turtle Racing!') #Sets specific name you want to display on window

racers = get_number_of_racers() #Returns the number of racers after all conditionals have been passed
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is the {winner.title()} turtle.")
time.sleep(5) #Python leaves window open for 5 seconds after race finishes so you can see results on screen


