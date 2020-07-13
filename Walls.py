from colorama import *


class Walls:
	def __init__(self):
		self.list1=[]
		for i in range(38):
			vari = [] 
			for j in range(76):
				vari.append(' ')
			self.list1.append(vari)
         
		
	def func1(self):
		
		for i in range(0,2):
			for j in range(0,76):
				self.list1[i][j] = '#'


		for i in range(2,36):
			for j in range(0,76):
				if j==0 or j==1 or  j==2 or j==3 or j==72 or j==73 or j==74 or j==75:
					self.list1[i][j] = '#'

				if i%4 == 1 or i%4 == 0 :
					for j in range(4,72):
						if  j%8==4 or j%8==5 or j%8==6 or j%8==7 :
							self.list1[i][j] = ' '
						else :
							self.list1[i][j] = '#'

		for i in range(36,38):
			for j in range(0,76):
				self.list1[i][j] = '#'

		self.list1[2][4]="["
		self.list1[2][5]="^"
		self.list1[2][6]="^"
		self.list1[2][7]="]"
		self.list1[3][5]="]"
		self.list1[3][6]="["		
		'''for i in range(38):
			for j in range(76):
				print (self.list1[i][j]),
			print(" ")'''


				

			


				
			
			

	


w=Walls();
w.func1();

