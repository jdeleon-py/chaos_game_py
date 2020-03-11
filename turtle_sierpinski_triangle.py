import turtle
import random
import math

dez = turtle.Turtle()
dez.speed(0)

ax = -300
ay = -300

bx = 300
by = -300

cx = 0
cy = 219.6

def reference_triangle(turtle):
	turtle.penup()
	turtle.goto(-300, -300)
	turtle.dot(2)
	turtle.pendown()
	
	turtle.penup()
	turtle.goto(300, -300)
	turtle.dot(2)
	turtle.pendown()

	turtle.penup()
	turtle.goto(0, 219.6)
	turtle.dot(2)
	turtle.pendown()

	return ""

def draw_triangle_fractal(turtle, updated_trace_position_x, updated_trace_position_y, count):
	
	new_seed = random.randint(0,2)
	
	if count == 4999:
		return ""	
	
	if new_seed == 0: # ax / ay
		distance = math.sqrt(((ax - updated_trace_position_x) ** 2) + ((ay - updated_trace_position_y) ** 2))
		distance = distance / 2

		turtle.penup()
		turtle.setheading(turtle.towards(ax, ay))
		turtle.forward(distance)
		turtle.pendown()
		turtle.dot(5)
		new_x = turtle.xcor()
		new_y = turtle.ycor()

		updated_count = count + 1
		print(count)
		draw_triangle_fractal(turtle, new_x, new_y, updated_count)

	elif new_seed == 1:
		distance = math.sqrt(((bx - updated_trace_position_x) ** 2) + ((by - updated_trace_position_y) ** 2))
		distance = distance / 2

		turtle.penup()
		turtle.setheading(turtle.towards(bx, by))
		turtle.forward(distance)
		turtle.pendown()
		turtle.dot(5)
		new_x = turtle.xcor()
		new_y = turtle.ycor()

		updated_count = count + 1
		print(count)
		draw_triangle_fractal(turtle, new_x, new_y, updated_count)

	elif new_seed == 2:
		distance = math.sqrt(((cx - updated_trace_position_x) ** 2) + ((cy - updated_trace_position_y) ** 2))
		distance = distance / 2

		turtle.penup()
		turtle.setheading(turtle.towards(cx, cy))
		turtle.forward(distance)
		turtle.pendown()
		turtle.dot(5)
		new_x = turtle.xcor()
		new_y = turtle.ycor()

		updated_count = count + 1
		print(count)
		draw_triangle_fractal(turtle, new_x, new_y, updated_count)
		

reference_triangle(dez)

first_trace_x = random.randint(-300, 300)
first_trace_y = random.randint(-300, 250)
dez.penup()
dez.setpos(first_trace_x, first_trace_y)
dez.pendown()
dez.dot(2)

draw_triangle_fractal(dez, first_trace_x, first_trace_y, 1)

turtle.done()
