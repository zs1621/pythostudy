#!/usr/bin/env python
# coding: utf-8

"""
使用 turtle 可视化递归

"""
import turtle
myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

#drawSpiral(myTurtle,100)


def tree(branchLen, t):
	if branchLen > 5:
		t.forward(branchLen)
		t.right(20)
		t.color('red')
		tree(branchLen-15, t)
		t.left(40)
		tree(branchLen-10, t)
		t.right(20)
		#backward 只是向反方向走给定的距离  走完距离后 不会改变方向
		t.backward(branchLen)

def main():
	t = turtle.Turtle()
	myWin = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.color('green')
	tree(75, t)
	myWin.exitonclick()

#main()

#draw 三角形
def drawTriangle(points, color, myTurtle):
	myTurtle.fillcolor(color)
	myTurtle.up()
	myTurtle.goto(points[0][0], points[0][1])
	myTurtle.down()
	myTurtle.begin_fill()
	myTurtle.goto(points[1][0], points[1][1])
	myTurtle.goto(points[2][0], points[2][1])
	myTurtle.goto(points[0][0], points[0][1])
	myTurtle.end_fill()


def getMid(p1, p2):
	return ( (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, myTurtle):
	colormap = ['red', 'green', 'white', 'yellow', 'blue']
	drawTriangle(points, colormap[degree], myTurtle)
	if degree > 0:
		sierpinski([points[0], \
				getMid(points[0], points[1]), \
				getMid(points[0], points[2])], \
				degree - 1, myTurtle)
		sierpinski([points[1], \
				getMid(points[0], points[1]), \
				getMid(points[1], points[2])],\
				degree - 1, myTurtle)
		sierpinski([points[2], \
				getMid(points[2], points[1]),
				getMid(points[0], points[2])],
				degree - 1, myTurtle)
		sierpinski([points[2],\
				getMid(points[2], points[1]),\
				getMid(points[2], points[2])],\
				degree - 1, myTurtle)
def main0():
	points = [[-100, -50], [0, 100], [100, -50]]
	myTurtle = turtle.Turtle()
	#drawTriangle(points, 'green', myTurtle)
	sierpinski(points, 4, myTurtle)
	myWin = turtle.Screen()
	myWin.exitonclick()

main0()
	
	