import random
import time
import hashlib
from math import cos, sin, pi
from Tkinter import *


def generate_tanks():
	global tanks, tank_one, tank_two
	# Clears old tanks
	tanks = [0, 0]
	canvas.delete('tank')
	# Generates two random tanks
	tanks[0] = random.randint(50, 480)
	tanks[1] = random.randint(520, 950)
	tank_one = canvas.create_rectangle(tanks[0]-20, h, tanks[0], h-20, fill='blue', tags=('tank'))
	tank_two = canvas.create_rectangle(tanks[1]-20, h, tanks[1], h-20, fill='red', tags=('tank'))
	generate_obstacle()
def generate_obstacle():
	global obstacle
	canvas.delete(obstacle)
	i = random.randint(tanks[0]+20, tanks[1]-20)
	obstacle = canvas.create_rectangle(i-20, h, i, h-40, fill='brown', tags=('obstacle'))
def fire():
	global player, winner, sx
	# Clears old arc and win message
	canvas.delete('line')
	win.config(text='')
	player_turn.config(text='Player {0}\'s go.'.format(player))
	# Gets variables from windows
	tick = float(clock.get())
	th = float(theta.get())*pi/180 # Converts to radians
	v = float(velocity.get())
	g = float(gravity.get())
	p = float(radius.get())
	# Sets starting variables
	sx = tanks[player-1]
	t = 0
	x, y = 0, 0
	
	# Where the parabola is created
	while True:
		ox, oy = x, y
		x = v*t*cos(th)
		y = v*t*sin(th) - g*0.5*t**2
		t += tick
		
		# Reverse curve for player 2
		if player == 2:
			x = x*-1
		l = canvas.create_line(ox+sx, h-oy, x+sx, h-y, tags=('line'))
		x1, y1, x2, y2 = canvas.coords(obstacle)
		hit = canvas.find_overlapping(x1, y1, x2, y2)
		if y < 0 or l in hit:
			break
	# Creates explosion
	ex, ey, fx, fy = x-p+sx, h-y-p, x+p+sx, h-y+p
	canvas.create_oval(ex, ey, fx, fy, fill='orange', tags='line')
	canvas.update()
	# Checks for hit
	hit = canvas.find_overlapping(ex, ey, fx, fy)
	if tank_one in hit or tank_two in hit:
		if tank_one in hit:
			canvas.delete(tank_one)
			winner = 2
		elif tank_two in hit:
			canvas.delete(tank_two)
			winner = 1
		win.config(text='Player {0} Wins!'.format(winner))
		canvas.delete('tank')
		canvas.delete('line')
		generate_tanks()
	if player == 1:
		player = 2
	else:
		player = 1

def draw_angle(event):
	'''
	Disabled for now
	
	canvas.delete('angle')
	sx = tanks[player-1]
	th = theta.get()*pi/180
	th = th-90
	canvas.create_line(sx, h, sx-80*sin(th), h-80*cos(th), fill='red', tags=('angle'))
	'''
 	return
 
def lock_dev():
	gravity.config(state=DISABLED)
	radius.config(state=DISABLED)
	clock.config(state=DISABLED)
	tank_button.config(state=DISABLED)
	lock_button.pack_forget()
	unlock.pack()
	unlock_button.pack()

def unlock_dev():
	gravity.config(state=NORMAL)
	radius.config(state=NORMAL)
	clock.config(state=NORMAL)
	tank_button.config(state=NORMAL)
	unlock.pack_forget()
	unlock_button.pack_forget()
	unlock.delete(0,END)
	unlock.insert(0, '')
	lock_button.pack()

def unlock_check():
	
	if hashlib.md5(unlock.get()).hexdigest() == '5f4dcc3b5aa765d61d8327deb882cf99':
		unlock_dev()
	else:
		print('Fail.')
	
winner = 0
player = 1
tanks = [0, 0]
tank_one = None
tank_two = None
obstacle = None
h = 400
w = 1000
m = hashlib.md5()

master = Tk()
master.wm_title('Tanks!')
dev = Tk()
dev.wm_title('Dev')

win = Label(master, text='')
canvas = Canvas(master, width=w, height=h)
player_turn = Label(master, text='Player 1\'s go.')
theta_label = Label(master, text='Angle')
theta = Scale(master, from_=1, to=90, orient=HORIZONTAL)
velocity_label = Label(master, text='Power')
velocity = Scale(master, from_=0, to=100, orient=HORIZONTAL)
fire_button = Button(master, text='Fire!', width=20, command=fire)


win.pack()
canvas.pack()
theta_label.pack()
theta.pack()
velocity_label.pack()
velocity.pack()
player_turn.pack()
fire_button.pack()

theta.bind('<Motion>', draw_angle)

gravity = Spinbox(dev, from_=0, to=100, increment=0.01)
gravity.delete(0,END)
gravity.insert(0, '9.81')
gravity_label = Label(dev, text='Gravity')
radius = Spinbox(dev, from_=0, to=100, increment=0.01)
radius.delete(0,END)
radius.insert(0, '20')
radius_label = Label(dev, text='Shell Strength')
clock = Spinbox(dev, from_=0, to=10, increment=0.01)
clock.delete(0,END)
clock.insert(0, '0.01')
clock_label = Label(dev, text='Smoothness')
tank_button = Button(dev, text='Generate Tanks', width=20, command=generate_tanks)

unlock = Entry(dev, show="*", width=20)
unlock_button = Button(dev, text='Unlock', width=20, command=unlock_check)
lock_button = Button(dev, text='Lock', width=20, command=lock_dev)

gravity_label.pack()
gravity.pack()
radius_label.pack()
radius.pack()
clock_label.pack()
clock.pack()
tank_button.pack()

lock_dev()
generate_tanks()
mainloop()

