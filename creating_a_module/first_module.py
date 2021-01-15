
import math

# * Let's encapsulate some code in this file
# * Here we declared some functions to be use outside this file
# * Use these functions on the script.py file

# *** Calculate areas *** #

# * Triangle area


def triangle(base, height):
    return base * height / 2

# * Rectangle area


def rectangle(base, height):
    return base*height


# * Circle area

def circle(radius):
    return math.pi*(radius**2)
