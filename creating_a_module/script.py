#!/usr/bin/env python3

# * This will import the file or module 'first_module'
# * and give it the alias 'fm'
import first_module as fm

# * Let's use oue 'first_module now'

# * call the triangle function from the 'fm' module
triangle = fm.triangle(5, 3)
print(triangle)

# * call the rectangle function from the 'fm' module
rectangle = fm.rectangle(8, 4)
print(rectangle)


# * Finally let's call the circle function from the 'fm' module
circle = fm.circle(6)
print(circle)
