#!/usr/bin/python

import os
from copy import deepcopy

# Attention: Config

matrix = [9, 7]  # [width, height]
robot = [5, 4]  # [x, y] counting from one

# Attention: Code

m = []  # working matrix
r = []  # robot's coordinates

### DO NOT TOUCH THIS (shitcode(no(pep8 sosat')))###
# Here we are define 'getch' and 'clear' functions for any OS
if os.name == 'posix':
	import sys, tty, termios
	fd = sys.stdin.fileno()  # getting current stdin file descriptor for.. hmm.. (see below)
	old_settings = termios.tcgetattr(fd)  # getting current input/output mode for file descriptor (see above)
	def getch():
		try:
			tty.setraw(sys.stdin.fileno())  # set mode 'no input/output to file descriptor' to tty(terminal(console))
			c = sys.stdin.read(1)  # WHAT?! Are u seriously could not understand this line?!?!?1!11!!1!7&!&!&77&!&!1!1!!
		finally:  # after read character
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # set previous mode to file descriptor (see above)
		return c
	def clear(): os.system('clear')	 # hmm.. are u shure that u need any explanations?
else:
	import msvcrt
	def getch(): return msvcrt.getch().decode()
	def clear(): os.system('cls')
### OR I WILL FIND YOU AND KILL YOU ###


def init():  # Initialization
	m.clear()
	m.append(['*'] * (matrix[0] + 2))
	for i in range(0, matrix[1]): m.append(['*'] + [' '] * matrix[0] + ['*'])  # https://false.team/patay.html
	m.append(['*'] * (matrix[0] + 2))
	r.clear()
	r.append(robot[1])
	r.append(robot[0])


def up():  # Action 'up'
	if m[r[0] - 1][r[1]] == '*': return
	r[0] -= 1


def down():  # Action 'down'
	if m[r[0] + 1][r[1]] == '*': return
	r[0] += 1


def left():  # Action 'left'
	if m[r[0]][r[1] - 1] == '*': return
	r[1] -= 1


def right():  # Action 'right'
	if m[r[0]][r[1] + 1] == '*': return
	r[1] += 1


def draw_matrix():  # Draw matrix
	tmp = deepcopy(m)  # recursively (!) copy array for not override original (see below)
	tmp[r[0]][r[1]] = '0'  # this override cell of array. because we r copy original (see above)
	for t in tmp: print(*t, sep = ' ')  # hmm.. custom separator?


def redraw():  # Redraw method.. this.. default.. for.. hmm.. any games?
	clear()  # clear screen (see definition above). Because REDRAW!
	draw_matrix()  # after clear screen need to.. draw anything


if __name__ == '__main__':
	init()  # Initialization
	redraw()  # Initialization redraw (first redraw (for display blank field))
	while True:
		c = getch()
		if c == '\x03': break  # ctrl + c (see below)
		elif c == 'q': break  # quit
		elif c == 'w': up()
		elif c == 's': down()
		elif c == 'a': left()
		elif c == 'd': right()
		elif c == 'i': init()  # force init
		elif c == 'r': pass  # force redraw
		else: continue
		redraw()
