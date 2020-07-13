from Walls import *
import random
from colorama import *
from Bricks import *


class Person:
	def __init__(self):
		pass
	def checkleft(self):
		pass
	def checkright(self):
		pass
	def checkup(self):
		pass
	def checkdown(self):
		pass

	def movement(self,pos):
		pass

	def __EnemyPos(self):
		pass

class Bomberman(Person): # INHERITED FROM PERSON
	def __init__(self):
		self.pos=""
		self.check=0
		self.x=2
		self.y=4
		self.cur1=0
		self.cur2=0
	w.list1[2][4]="["
	w.list1[2][5]="^"
	w.list1[2][6]="^"
	w.list1[2][7]="]"
	w.list1[3][5]="]"
	w.list1[3][6]="["
	w.func1()
	for i in range(38):
		for j in range(76):
			if w.list1[i][j]=="["  or w.list1[i][j]=="]" :
				print (Fore.RED + w.list1[i][j]),
			elif w.list1[i][j]=="^":
				print (Fore.YELLOW + w.list1[i][j]),
			elif w.list1[i][j]=="E":
				print (Fore.GREEN + w.list1[i][j]),
			elif w.list1[i][j]=="%":
				print (Fore.BLUE + w.list1[i][j]),
			else :
				print(Fore.WHITE + w.list1[i][j]),
		print(" ")


	def checkleft(self): #cant move conditions 
		if w.list1[self.x][self.y-4]=="#" or w.list1[self.x+1][self.y-3]=="#" or w.list1[self.x][self.y-4]=="%" or w.list1[self.x][self.y-3]=="%" or w.list1[self.x][self.y-4]=="[" or w.list1[self.x+1][self.y-3]=="[" or w.list1[self.x][self.y-4]=="]" or w.list1[self.x][self.y-3]=="]" or  w.list1[self.x][self.y-4]=="0" or w.list1[self.x][self.y-3]=="0":
			check=1
		elif w.list1[self.x][self.y-4]=="E" or w.list1[self.x+1][self.y-3]=="E":
			w.list1[2][4]="["
			w.list1[2][5]="^"
			w.list1[2][6]="^"
			w.list1[2][7]="]"
			w.list1[3][5]="]"
			w.list1[3][6]="["
			w.list1[self.x][self.y+3]= ' '
			w.list1[self.x][self.y+2]= ' '
			w.list1[self.x][self.y+1]= ' '
			w.list1[self.x][self.y]= ' '
			w.list1[self.x+1][self.y+2]= ' '
			w.list1[self.x+1][self.y+1]=  ' '
			l.reducelife()
		else:
			check =0
		return check
	
	def checkright(self): #cant move conditions 
		if  w.list1[self.x][self.y+7]=="#" or w.list1[self.x][self.y+6]=="#" or w.list1[self.x][self.y+7]=="%" or w.list1[self.x][self.y+6]=="%"or w.list1[self.x][self.y+7]=="]" or w.list1[self.x][self.y+6]=="]" or w.list1[self.x][self.y+7]=="[" or w.list1[self.x][self.y+6]=="[" or w.list1[self.x][self.y+7]=="0" or w.list1[self.x][self.y+6]=="0" :
			check=1
		elif  w.list1[self.x][self.y+7]=="E" or w.list1[self.x][self.y+6]=="E":
			w.list1[2][4]="["
			w.list1[2][5]="^"
			w.list1[2][6]="^"
			w.list1[2][7]="]"
			w.list1[3][5]="]"
			w.list1[3][6]="["
			w.list1[self.x][self.y+3]= ' '
			w.list1[self.x][self.y+2]= ' '
			w.list1[self.x][self.y+1]= ' '
			w.list1[self.x][self.y]= ' '
			w.list1[self.x+1][self.y+2]= ' '
			w.list1[self.x+1][self.y+1]=  ' '
			l.reducelife()
			check=1
		else :																																																																					
			check =0
		return check
	
	def checkup(self): #cant move conditions 
		if w.list1[self.x-2][self.y]=="#" or w.list1[self.x-2][self.y+1]=="#" or w.list1[self.x-2][self.y+2]=="#" or w.list1[self.x-2][self.y+3]=="#" or w.list1[self.x-2][self.y]=="%" or w.list1[self.x-2][self.y+1]=="%" or w.list1[self.x-2][self.y+2]=="%" or w.list1[self.x-2][self.y+3]=="%" or w.list1[self.x-2][self.y]=="[" or w.list1[self.x-2][self.y+1]=="[" or w.list1[self.x-2][self.y+2]=="[" or w.list1[self.x-2][self.y+3]=="[" or w.list1[self.x-2][self.y]=="]" or w.list1[self.x-2][self.y+1]=="]" or w.list1[self.x-2][self.y+2]=="]" or w.list1[self.x-2][self.y+3]=="]" or w.list1[self.x-2][self.y]=="0" or w.list1[self.x-2][self.y+1]=="0" or w.list1[self.x-2][self.y+2]=="0" or w.list1[self.x-2][self.y+3]=="0":
			check=1
		elif w.list1[self.x-2][self.y]=="E" or w.list1[self.x-2][self.y+1]=="E" or w.list1[self.x-2][self.y+2]=="E" or w.list1[self.x-2][self.y+3]=="E":
			w.list1[2][4]="["
			w.list1[2][5]="^"
			w.list1[2][6]="^"
			w.list1[2][7]="]"
			w.list1[3][5]="]"
			w.list1[3][6]="["
			w.list1[self.x][self.y+3]= ' '
			w.list1[self.x][self.y+2]= ' '
			w.list1[self.x][self.y+1]= ' '
			w.list1[self.x][self.y]= ' '
			w.list1[self.x+1][self.y+2]= ' '
			w.list1[self.x+1][self.y+1]=  ' '
			l.reducelife()
			check=1		
		else :
			check =0
		return check	


	def checkdown(self): #cant move conditions 
		if  w.list1[self.x+3][self.y+1]=="#" or w.list1[self.x+3][self.y+2]=="#"  or w.list1[self.x+3][self.y+1]=="%" or w.list1[self.x+3][self.y+2]=="%" or  w.list1[self.x+3][self.y+1]=="]" or w.list1[self.x+3][self.y+2]=="]" or  w.list1[self.x+3][self.y+1]=="[" or w.list1[self.x+3][self.y+2]=="["  or  w.list1[self.x+3][self.y+1]=="0" or w.list1[self.x+3][self.y+2]=="0"  :
			check=1
		elif  w.list1[self.x+3][self.y+1]=="E" or w.list1[self.x+3][self.y+2]=="E" :
			w.list1[2][4]="["
			w.list1[2][5]="^"
			w.list1[2][6]="^"
			w.list1[2][7]="]"
			w.list1[3][5]="]"
			w.list1[3][6]="["
			w.list1[self.x][self.y+3]= ' '
			w.list1[self.x][self.y+2]= ' '
			w.list1[self.x][self.y+1]= ' '
			w.list1[self.x][self.y]= ' '
			w.list1[self.x+1][self.y+2]= ' '
			w.list1[self.x+1][self.y+1]=  ' '
			l.reducelife()
			check=1
		else :
			check =0
		return check


	def movement(self,pos): # POLYMORPHISM
		print self.cur1
		print self.cur2
		if pos=="a":
			#print (w.list1[self.x][self.y-3])
			c = self.checkleft();
			if c==0:
				w.list1[self.x][self.y-4]=w.list1[self.x][self.y]
				w.list1[self.x][self.y-3]=w.list1[self.x][self.y+1]
				w.list1[self.x][self.y-2]=w.list1[self.x][self.y+2]
				w.list1[self.x][self.y-1]=w.list1[self.x][self.y+3]
				w.list1[self.x+1][self.y-3]=w.list1[self.x+1][self.y+1]
				w.list1[self.x+1][self.y-2]=w.list1[self.x+1][self.y+2]
				w.list1[self.x+1][self.y+2]=  " "
				w.list1[self.x][self.y]= " "
				w.list1[self.x][self.y+1]= " "
				w.list1[self.x][self.y+2]= " "
				w.list1[self.x+1][self.y+1]= " "
				w.list1[self.x][self.y+3]= " "
				self.x=self.x
				self.y=self.y-4
				self.cur1=self.x
				self.cur2=self.y
		
			for i in range(38):
				for j in range(76):
					if w.list1[i][j]=="["  or w.list1[i][j]=="]" :
						print (Fore.RED + w.list1[i][j]),
					elif w.list1[i][j]=="^":
						print (Fore.YELLOW + w.list1[i][j]),
					elif w.list1[i][j]=="E":
						print (Fore.GREEN + w.list1[i][j]),
					elif w.list1[i][j]=="%":
						print (Fore.BLUE + w.list1[i][j]),
					else :
						print(Fore.WHITE + w.list1[i][j]),
				print(" ")

		
		if pos=="d":
			c = self.checkright();
			if c==0:
				w.list1[self.x][self.y+7]=w.list1[self.x][self.y+3]
				w.list1[self.x][self.y+6]=w.list1[self.x][self.y+2]
				w.list1[self.x][self.y+5]=w.list1[self.x][self.y+1]
				w.list1[self.x][self.y+4]=w.list1[self.x][self.y]
				w.list1[self.x+1][self.y+6]=w.list1[self.x+1][self.y+2]
				w.list1[self.x+1][self.y+5]=w.list1[self.x+1][self.y+1]
				w.list1[self.x][self.y+3]= ' '
				w.list1[self.x][self.y+2]= ' '
				w.list1[self.x][self.y+1]= ' '
				w.list1[self.x][self.y]= ' '
				w.list1[self.x+1][self.y+2]= ' '
				w.list1[self.x+1][self.y+1]=  ' '
				self.x=self.x
				self.y=self.y+4
				self.cur1=self.x
				self.cur2=self.y
			
			for i in range(38):
				for j in range(76):
					if w.list1[i][j]=="["  or w.list1[i][j]=="]" :
						print (Fore.RED + w.list1[i][j]),
					elif w.list1[i][j]=="^":
						print (Fore.YELLOW + w.list1[i][j]),
					elif w.list1[i][j]=="E":
						print (Fore.GREEN + w.list1[i][j]),
					elif w.list1[i][j]=="%":
						print (Fore.BLUE + w.list1[i][j]),
					else :
						print(Fore.WHITE + w.list1[i][j]),
				print(" ")
		if pos=="w":
			c = self.checkup();
			if c==0:
				w.list1[self.x-2][self.y+3]=w.list1[self.x][self.y+3]
				w.list1[self.x-2][self.y+2]=w.list1[self.x][self.y+2]
				w.list1[self.x-2][self.y+1]=w.list1[self.x][self.y+1]
				w.list1[self.x-2][self.y]=w.list1[self.x][self.y]			
				w.list1[self.x-1][self.y+2]=w.list1[self.x+1][self.y+2]
				w.list1[self.x-1][self.y+1]=w.list1[self.x+1][self.y+1]
				w.list1[self.x][self.y+3]= ' '
				w.list1[self.x][self.y+2]= ' '
				w.list1[self.x][self.y+1]= ' '
				w.list1[self.x][self.y]= ' '
				w.list1[self.x+1][self.y+2]= ' '
				w.list1[self.x+1][self.y+1]=  ' '
				self.x=self.x-2
				self.y=self.y
				self.cur1=self.x
				self.cur2=self.y
			
			for i in range(38):
				for j in range(76):
					if w.list1[i][j]=="["  or w.list1[i][j]=="]" :
						print (Fore.RED + w.list1[i][j]),
					elif w.list1[i][j]=="^":
						print (Fore.YELLOW + w.list1[i][j]),
					elif w.list1[i][j]=="E":
						print (Fore.GREEN + w.list1[i][j]),
					elif w.list1[i][j]=="%":
						print (Fore.BLUE + w.list1[i][j]),
					else :
						print(Fore.WHITE + w.list1[i][j]),
				print(" ")
		if pos=="s":
			c = self.checkdown();
			if c==0:
				w.list1[self.x+2][self.y+3]=w.list1[self.x][self.y+3]
				w.list1[self.x+2][self.y+2]=w.list1[self.x][self.y+2]
				w.list1[self.x+2][self.y+1]=w.list1[self.x][self.y+1]
				w.list1[self.x+2][self.y]=w.list1[self.x][self.y]
				w.list1[self.x+3][self.y+2]=w.list1[self.x+1][self.y+2]
				w.list1[self.x+3][self.y+1]=w.list1[self.x+1][self.y+1]				
				w.list1[self.x][self.y+3]= ' '
				w.list1[self.x][self.y+2]= ' '
				w.list1[self.x][self.y+1]= ' '
				w.list1[self.x][self.y]= ' '
				w.list1[self.x+1][self.y+2]= ' '					
				w.list1[self.x+1][self.y+1]=  ' '
				self.x=self.x+2
				self.y=self.y
				self.cur1=self.x
				self.cur2=self.y
		
			for  i in range(38):
				for j in range(76):
					if w.list1[i][j]=="["  or w.list1[i][j]=="]" :
						print (Fore.RED + w.list1[i][j]),
					elif w.list1[i][j]=="^":
						print (Fore.YELLOW + w.list1[i][j]),
					elif w.list1[i][j]=="E":
						print (Fore.GREEN + w.list1[i][j]),
					elif w.list1[i][j]=="%":
						print (Fore.BLUE + w.list1[i][j]),
					else :
						print(Fore.WHITE + w.list1[i][j]),
				print(" ")

	

class Enemy(Person): #INHERITED FROM PERSON
	def __init__(self):
		self.xx=random.randint(1,25)
		self.yy=random.randint(1,25)
	def __EnemyPos(self): #Encapsulation
		e_x=random.randrange(6,34,2)
		e_y=random.randrange(12,68,4)
		while(w.list1[e_x][e_y]!=' '):
			e_x = random.randrange(6,34,2)
			e_y = random.randrange(12,68,4)
		self.xx = e_x
		self.yy = e_y
		for i in range(self.xx,self.xx+2):
			for j in range(self.yy,self.yy+4):
				w.list1[i][j]="E"
		
	def movement(self): # POLYMORPHISM
		ranum = random.randint(5,8)
		if ranum==5:
			if(w.list1[self.xx-2][self.yy]!="#" and w.list1[self.xx-2][self.yy]!="%" ):
				for i in range (self.xx-2,self.xx):
					for j in range (self.yy,self.yy+4):
						w.list1[i][j]="E"
				self.xx=self.xx-2
				self.yy=self.yy
				for i in range (self.xx,self.xx+2):
					for j in range (self.yy,self.yy+4):
						w.list1[i][j]=" "
			elif w.list1[self.xx-2][self.yy]=="^" and w.list1[self.xx-2][self.yy]=="["  and w.list1[self.xx-2][self.yy]=="]" :
				w.list1[2][4]="["
				w.list1[2][5]="^"
				w.list1[2][6]="^"
				w.list1[2][7]="]"
				w.list1[3][5]="]"
				w.list1[3][6]="["
				w.list1[self.xx][self.yy+3]= ' '
				w.list1[self.xx][self.yy+2]= ' '
				w.list1[self.xx][self.yy+1]= ' '
				w.list1[self.xx][self.yy]= ' '
				w.list1[self.xx+1][self.yy+2]= ' '
				w.list1[self.xx+1][self.yy+1]=  ' '
				l.reducelife()
				self.xx=self.xx-2
				self.yy=self.yy
		elif ranum == 6:
			if(w.list1[self.xx][self.yy-4]!="#" and  w.list1[self.xx][self.yy-4]!="%"):
				for i in range (self.xx,self.xx+2):
					for j in range (self.yy-4,self.yy):
						w.list1[i][j]="E"
				
				for i in range (self.xx,self.xx+2):
					for j in range (self.yy,self.yy+4):
						w.list1[i][j]=" "
				
				self.xx=self.xx
				self.yy=self.yy-4
			elif (w.list1[self.xx][self.yy-4]=="[" and  w.list1[self.xx][self.yy-4]=="]" and  w.list1[self.xx][self.yy-4]=="^") :
				w.list1[2][4]="["
				w.list1[2][5]="^"
				w.list1[2][6]="^"
				w.list1[2][7]="]"
				w.list1[3][5]="]"
				w.list1[3][6]="["
				w.list1[self.xx][self.yy+3]= ' '
				w.list1[self.xx][self.yy+2]= ' '
				w.list1[self.xx][self.yy+1]= ' '
				w.list1[self.xx][self.yy]= ' '
				w.list1[self.xx+1][self.yy+2]= ' '
				w.list1[self.xx+1][self.yy+1]=  ' '
				l.reducelife()
				self.xx=self.xx
				self.yy=self.yy-4
		elif ranum == 7:
			if(w.list1[self.xx+2][self.yy]!="#" and w.list1[self.xx+2][self.yy]!="%"):
				for i in range (self.xx+2,self.xx+4):
					for j in range (self.yy,self.yy+4):
						w.list1[i][j]="E"
				
				for i in range (self.xx,self.xx+2):
					for j in range (self.yy,self.yy+4):
						w.list1[i][j]=" "
				
				self.xx=self.xx+2
				self.yy=self.yy
			elif (w.list1[self.xx+2][self.yy]=="]" and w.list1[self.xx+2][self.yy]=="[" and w.list1[self.xx+2][self.yy]=="^"):
				w.list1[2][4]="["
				w.list1[2][5]="^"
				w.list1[2][6]="^"
				w.list1[2][7]="]"
				w.list1[3][5]="]"
				w.list1[3][6]="["
				w.list1[self.xx][self.yy+3]= ' '
				w.list1[self.xx][self.yy+2]= ' '
				w.list1[self.xx][self.yy+1]= ' '
				w.list1[self.xx][self.yy]= ' '
				w.list1[self.xx+1][self.yy+2]= ' '
				w.list1[self.xx+1][self.yy+1]=  ' '
				l.reducelife()

				self.xx=self.xx+2
				self.yy=self.yy
		elif ranum == 8:
			if(w.list1[self.xx][self.yy+4] !="#" and w.list1[self.xx][self.yy+4] !="%"):
				for i in range (self.xx,self.xx+2):
					for j in range (self.yy+4,self.yy+8):
						w.list1[i][j]="E"
				
				for i in range (self.xx,self.xx+2):
					for j in range (self.yy,self.yy+4):
						w.list1[i][j]=" "
				
				self.xx=self.xx
				self.yy=self.yy+4
			elif (w.list1[self.xx][self.yy+4] =="[" and w.list1[self.xx][self.yy+4] =="^"  and w.list1[self.xx][self.yy+4] =="]"):
				w.list1[2][4]="["
				w.list1[2][5]="^"
				w.list1[2][6]="^"
				w.list1[2][7]="]"
				w.list1[3][5]="]"
				w.list1[3][6]="["
				w.list1[self.xx][self.yy+3]= ' '
				w.list1[self.xx][self.yy+2]= ' '
				w.list1[self.xx][self.yy+1]= ' '
				w.list1[self.xx][self.yy]= ' '
				w.list1[self.xx+1][self.yy+2]= ' '
				w.list1[self.xx+1][self.yy+1]=  ' '
				l.reducelife()
				self.xx=self.xx
				self.yy=self.yy+4


				

######################################################################
class Bomb:
	def __init__(self):
		self.bposx=0
		self.bposy=0

	def bombblast(self,cur1,cur2):
		self.bposx=cur1
		self.bposy=cur2
		self.lll=0
		self.dd=0

	def check(self,cur1,cur2):
		#print "yagyghjbdbd jkhdkjncdndjkdnfjf"
		for i in range(self.bposx,self.bposx+2):
			for j in range(self.bposy-4,self.bposy+8):	
				if  w.list1[i][j]!="#":
					if w.list1[i][j]=="^" or w.list1[i][j]=="]" or w.list1[i][j]=="[":
						self.dd=1
						#print 'chinti' 
						w.list1[i][j]="^"
					else :
						w.list1[i][j]="^"
			

		for i in range(self.bposx-4,self.bposx+6):		
			for j in range(self.bposy,self.bposy+4):
				if w.list1[i][j] !='#':
					if w.list1[i][j]=="^" or w.list1[i][j]=="]" or w.list1[i][j]=="[":
						self.dd=1
						#print 'chinti' 
						w.list1[i][j]="^"
					else :
						w.list1[i][j]="^"
		for i in range(38):
			for j in range(76):
				if w.list1[i][j]=="["  or w.list1[i][j]=="]" :
					print (Fore.RED + w.list1[i][j]),
				elif w.list1[i][j]=="^":
					print (Fore.YELLOW + w.list1[i][j]),
				elif w.list1[i][j]=="E":
					print (Fore.GREEN + w.list1[i][j]),
				elif w.list1[i][j]=="%":
					print (Fore.BLUE + w.list1[i][j]),
				else :
					print(Fore.WHITE + w.list1[i][j]),
			print(" ")

		if self.dd==1:
			w.list1[2][4]="["
			w.list1[2][5]="^"
			w.list1[2][6]="^"
			w.list1[2][7]="]"
			w.list1[3][5]="]"
			w.list1[3][6]="["
			w.list1[cur1][cur2+3]= ' '
			w.list1[cur1][cur2+2]= ' '
			w.list1[cur1][cur2+1]= ' '
			w.list1[cur1][cur2]= ' '
			w.list1[cur1+1][cur2+2]= ' '
			w.list1[cur1+1][cur2+1]=  ' '
			self.lll=1
		
			

		if self.lll==1 and self.dd==1:
			l.reducelife()
		self.lll=0
		for i in range(self.bposx,self.bposx+2):
			for j in range(self.bposy-4,self.bposy+8):
				if  w.list1[i][j]=="^" or w.list1[i][j]!="#" or  w.list1[i][j]=="[" or w.list1[i][j]=="]" or w.list1[i][j]=="E" or w.list1[i][j]=="E=0": 
					w.list1[i][j]=" "
		
		for i in range(self.bposx-4,self.bposx+6):
			for j in range(self.bposy,self.bposy+4):
				if  w.list1[i][j]=="^" or w.list1[i][j]!="#" or w.list1[j][j]=="[" or w.list1[i][j]=="]" or w.list1[i][j]=="0" or w.list1[i][j]=="E": 
					w.list1[i][j]=" "
		
		for i in range(38):
			for j in range(76):
				if w.list1[i][j]=="[" or w.list1[i][j]=="]" :
					print (Fore.RED + w.list1[i][j]),
				elif w.list1[i][j]=="^":
					print (Fore.YELLOW + w.list1[i][j]),
				elif w.list1[i][j]=="E":
					print (Fore.GREEN + w.list1[i][j]),
				elif w.list1[i][j]=="%":
					print (Fore.BLUE + w.list1[i][j]),
				else :
					print(Fore.WHITE + w.list1[i][j]),
			print(" ")

			
	def placing_bomb(self):
		if (w.list1[self.bposx][self.bposy]!="[" or w.list1[self.bposx][self.bposy+1]!="^" or w.list1[self.bposx][self.bposy+2]!="^" or w.list1[self.bposx][self.bposy+3]!="]" or w.list1[self.bposx+1][self.bposy+2]!="]" or w.list1[self.bposx+1][self.bposy+1]!="[") and (w.list1[self.bposx][self.bposy]!="#" or w.list1[self.bposx][self.bposy+1]!="#" or w.list1[self.bposx][self.bposy+2]!="#" or w.list1[self.bposx][self.bposy+3]!="#" or w.list1[self.bposx+1][self.bposy+2]!="#" or w.list1[self.bposx+1][self.bposy+1]!="#"):
			w.list1[self.bposx][self.bposy]="["
			w.list1[self.bposx][self.bposy+1]="0"
			w.list1[self.bposx][self.bposy+2]="0"
			w.list1[self.bposx][self.bposy+3]="]"			
			w.list1[self.bposx+1][self.bposy]="["
			w.list1[self.bposx+1][self.bposy+1]="0"
			w.list1[self.bposx+1][self.bposy+2]="0"
			w.list1[self.bposx+1][self.bposy+3]="]"		




########################################################################

class Life:
	def __init__(self):
		self.life=3
	def reducelife(self):
		#print "ujhdkjdhebd"
		self.life=self.life-1
		for i in range(38):
			for j in range(76):
				if w.list1[i][j]=="["  or w.list1[i][j]=="]" :
					print (Fore.RED + w.list1[i][j]),
				elif w.list1[i][j]=="^":
					print (Fore.YELLOW + w.list1[i][j]),
				elif w.list1[i][j]=="E":
					print (Fore.GREEN + w.list1[i][j]),
				elif w.list1[i][j]=="%":
					print (Fore.BLUE + w.list1[i][j]),
				else :
					print(Fore.WHITE + w.list1[i][j]),
			print(" ")

		if self.life==0:
			print (Fore.RED+"LIFE OVER")





e = Enemy();
b= Bricks()
e._Enemy__EnemyPos(); # ENCAPSULATION
q = Bomberman();	
bb=Bomb()
b.bricksPos()
b.bricksPos()
b.bricksPos()
b.bricksPos()
b.bricksPos()
l = Life()

flag1 =False
flag2=False
while(1):
	pos=raw_input()
	e.movement();
	e.movement();
	e.movement();
	if pos=="b" and flag1==False and flag2==False:
		#print "b is pressed"
		bb.bombblast(q.cur1,q.cur2)
		flag1=True
		count=3
	elif pos=="d" or pos=="s" or pos=="a" or pos=="w":
		#print "tttttttt"
		q.movement(pos)
	if (flag1==True and (pos=="d" or pos=="s" or pos=="w" or pos=="a")):
		bb.placing_bomb()
		count=count-1
		if count==0:
			#print q.cur1, q.cur2
			#print "inside cnt"
			bb.check(q.cur1,q.cur2)
			Bomberman()
			flag2=False
			flag1=False
			q.cur1=2
			q.cur2=4
			w.list1[q.cur1][q.cur2]="["
			w.list1[q.cur1][q.cur2+1]="^"
			w.list1[q.cur1][q.cur2+2]="^"
			w.list1[q.cur1][q.cur2+3]="]"
			w.list1[q.cur1+1][q.cur2+1]="]"
			w.list1[q.cur1+1][q.cur2+2]="["
			
	for i in range(38):
			for j in range(76):
				if w.list1[i][j]=="["  or w.list1[i][j]=="]" :
					print (Fore.RED + w.list1[i][j]),
				elif w.list1[i][j]=="^":
					print (Fore.YELLOW + w.list1[i][j]),
				elif w.list1[i][j]=="E":
					print (Fore.GREEN + w.list1[i][j]),
				elif w.list1[i][j]=="%":
					print (Fore.BLUE + w.list1[i][j]),
				else :
					print(Fore.WHITE + w.list1[i][j]),
			print(" ")

