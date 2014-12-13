import random
import time
import hashlib
from math import cos, sin, pi
try:
	from tkinter import * # 3.3
except ImportError:
	from Tkinter import * # 2.7


def generate_tanks():
	global tanks, tank_one, tank_two
	# Clears old tanks
	tanks = [0, 0]
	canvas.delete('tank')
	# Generates two random tanks
	tanks[0] = random.randint(10, int(w/2)-50)
	tanks[1] = random.randint(int(w/2)+50, w-10)
	tank_one = canvas.create_rectangle(tanks[0]-20, h, tanks[0], h-20, fill='blue', tags=('tank'))
	tank_two = canvas.create_rectangle(tanks[1]-20, h, tanks[1], h-20, fill='red', tags=('tank'))
	generate_obstacle()
	
def generate_obstacle():
	global obstacle
	canvas.delete(obstacle)
	i = random.randint(tanks[0]+20, tanks[1]-20)
	obstacle = canvas.create_rectangle(i-20, h, i, h-40, fill='brown', tags=('obstacle'))
	
def fire():
	global player, winner, sx, clicked, scores
	fire_button.config(state=DISABLED)
	# Clears old arc and win message
	canvas.delete('line')
	win.config(text='')
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
		canvas.update()
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
		scores[winner-1] += 1
		win.config(text='Player {0} Wins!'.format(winner))
		canvas.delete('tank')
		canvas.delete('line')
		generate_tanks()
	if player == 1:
		player = 2
	else:
		player = 1
	player_turn.config(text='Player {0}\'s go.'.format(player))
	score_label.config(text=score_text.format(scores[0], scores[1]))
	fire_button.config(state=NORMAL)
 
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
	# A password is used to stop players fiddling with the settings, and so I can
	# test out the best values easily.
	if hashlib.md5(unlock.get()).hexdigest() == '5f4dcc3b5aa765d61d8327deb882cf99':
		unlock_dev()
	else:
		print('Fail.')
	

# Starting variables	
winner = 0
player = 1
tanks = [0, 0]
tank_one = None
tank_two = None
obstacle = None
h = 400
scores = [0, 0]
score_text = 'Scores\nPlayer 1: {0}\nPlayer 2: {1}'
m = hashlib.md5()

# Creates base windows
master = Tk()
master.wm_title('Tanks!')
w = master.winfo_screenwidth()

dev = Tk()
dev.wm_title('Dev')
controls = Tk()
controls.wm_title('Controls')

# Main window
canvas = Canvas(master, width=w, height=h, bg='gray')
canvas.pack()

# Controller window
win = Label(controls, text='')
player_turn = Label(controls, text='Player 1\'s go.')
theta_label = Label(controls, text='Angle')
theta = Scale(controls, from_=1, to=90, orient=HORIZONTAL)
theta.set(45)
velocity_label = Label(controls, text='Power')
velocity = Scale(controls, from_=0, to=100, orient=HORIZONTAL)
velocity.set(50)
fire_button = Button(controls, text='Fire!', width=20, command=fire)
score_label = Label(controls, text=score_text.format(scores[0], scores[1]))


score_label.pack()
player_turn.pack()
win.pack()

theta_label.pack()
theta.pack()
velocity_label.pack()
velocity.pack()
fire_button.pack()


# Dev window
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
clock.insert(0, '0.1')
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


# Sets the stage
lock_dev()
generate_tanks()

# Runs the program
mainloop()