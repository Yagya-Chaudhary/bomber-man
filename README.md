BOMBERMAN GAME 

use of python only

IT IS HAVING THREE FILES OR MODULES:-> # MOdularity 
	1. Walls.py
	2. Person.py
	3. Bricks.py
IN Walls :
	CLASS :-> Walls
	FUNCTIONS:-> func1()
	w is the instance of the class Walls


IN Person :
1. USE of INHERITANCE
	CLASS:-> Person which is the parent class
	Bomberman -> sub class of Person 
	Enemy -> sub class of Person  
	both Bomberman and Enemy inherited the functions from the parent class
	checkleft
	checkright
	checkup
	checkdown
	movement
	__EnemyPos
		pass
	 1. Bomberman:-> 
	 	functions :-> 	checkleft
						checkright
						checkup
						checkdown
						movement
	2. Enemy:-> 
		functions :-> movement
					__EnemyPos

2. USE OF ENCAPSULATION 
	__EnemyPos
	so use of this while calling is e._Enemy__pos
3. USE OF POLYMORPHISM
	movement : which is been used in both Bomberman and Enemy with a different functionality in them .
	q=Bomberman #instance of Bomberman
		q.movement()
	e=Enemy # instance of Enemy
		e.movement()


IN Bricks:
	functions :-> Brickpos


symbols used :
	# -> walls
	% -> bricks
	[^^] -> bomberman
	 ][
	 E  -> enemy
	 ^ -> explosion  
movement of enemy is random 
and bricks are generated randomly

how to play 
run the file Person.py using python Person.py
	To start the game press any key and for moving the bomberman press:
																	w for up movement
																	a for the left movement
																	s for the down movement
																	d for the right movement
																	b for blasting the bomb
	after pressing the b key 3 times we can press the key and after the 3rd key is pressed bomb will be blast.
	and its life get reduced
