#!/usr/bin/env python3
#
# TurtleTriangles.py
#
# Make triangle art with the Python Turtles module.
# Inspired by Runestone Academy's "Foundations of Python Programming"
# (https://runestone.academy/ns/books/published/fopp/index.html)
#
# 2022-May-29 - suuze_linux
#

# Import required modules
import math
import random
import turtle

# Define variables, lists and functions
colorlist = ["blue", "red", "yellow", "hotpink", "grey", "purple", "green", "turquoise"]
sizelist = [50, 100, 150]

def draw_triangle(dorcassize, dorcascolor, dorcasx, dorcasy, dorcasheading):
  dorcas = turtle.Turtle()  # create a turtle named dorcas
  dorcas.color(dorcascolor)
  dorcas.shape("turtle")
  dorcas.pensize(3)

  dorcas.penup()
  dorcas.goto(dorcasx,dorcasy)
  dorcas.setheading(dorcasheading)
  dorcas.pendown()

  dorcas.forward(dorcassize)
  dorcas.left(90)
  dorcas.forward(dorcassize)
  dorcas.left(135)

  hypotenuse = math.sqrt((dorcassize ** 2) * 2)
  dorcas.forward(hypotenuse)

# Setup new screen and turtle
window = turtle.Screen()
window.bgcolor("orange")

# Main program
innumber = input("Enter number of triangles to draw, or 'q' to quit: ")
if innumber == "q":
	print("Click on the triangles' window to exit!")
	# break
else:
	try:
		number = int(innumber)
	except ValueError as ve:
		print("Please enter an integer.")
	for _ in range(1, number):
		# Call function draw_triangle()
		draw_triangle(random.choice(sizelist), \
		  random.choice(colorlist), random.randint(-175, 175), \
		  random.randint(-175, 175), random.randrange(0, 360, 10))

print("Drawing triangles complete, click on triangles' window to exit.")
window.exitonclick()
