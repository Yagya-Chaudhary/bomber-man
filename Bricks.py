import random
from Walls import *

class Bricks:
	def __init__(self):
		self.xb=random.randint(1,25)
		self.yb=random.randint(1,25)


	def bricksPos(self):
		b_x=random.randrange(6,34,2)
		b_y=random.randrange(12,68,4)
		while(w.list1[b_x][b_y]!=' '):
			b_x = random.randrange(6,34,2)
			b_y = random.randrange(12,68,4)
		self.xb = b_x
		self.yb = b_y
		w.list1[self.xb][self.yb]="%"
		w.list1[self.xb][self.yb+1]="%"
		w.list1[self.xb][self.yb+2]="%"
		w.list1[self.xb][self.yb+3]="%"
		w.list1[self.xb+1][self.yb]="%"
		w.list1[self.xb+1][self.yb+1]="%"
		w.list1[self.xb+1][self.yb+2]="%"
		w.list1[self.xb+1][self.yb+3]="%"