# Table of Contents
- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Stretch Goals](#stretch-goals)
- [Class Breakdown](#class-breakdown)
- [OOP Check List](#oop-check-list)
  - [Abstraction](#abstraction)
  - [Polymorphism](#polymorphism)
  - [Encapsulation](#encapsulation)
  - [Inheritance](#inheritance)

# Description
Our game is a side scroller where a yeti is trying to save his baby yeti. He will have to jump over holes and other dangerous things
while fighting off Chuck(s). 

# Stretch Goals  

	- At the end, he has to fight off the Karen  
	- Climbing into the clouds 
	- Power ups that make him more awesome
	- Ammunition count
	- Cheat code(s)
	- Awesome sound effects
	
# Class Breakdown 
	Entities
		Entity (abstract) - Jake/Evan collaberation 
			Player  - Jake
			Enemy - Evan
				Boss (stretch)
			Projectile?
			Powerups (stretch)
			

	Services -- Tom / Copy paste from before
		Vid
		Audio
		Key

	Game  -- Everyone
		Start
	World -- Tom
		Background
		Obsticle
			Fading (stretch)

		
	Actions -- Everyone 
		*






---------------------------------------

# OOP Check List

## Abstraction  

Abstraction is providing a simple interface to something that has complexity behind it. Breaking a complex problem into
		smaller ones.  

	print("Hello World") uses many lines of code, but is simple.  


Our example would be something like game calling all the code that we need run, but not showing all the complex functions
		like "draw" is actually calling py.drawText("blah", 20,20,20,0)

	
	
## Polymorphism
The Actions class will use this for the execute method. Method overriding is the type.
	

## Encapsulation
	
Be sure to use _variables and _methods where appropriate for access control.
	

## Inheritance
	Entity(abstract)
		player / Enemy
	Service
		Vid/audio/keyboard
	Obsticle
		Wall/hole



Back to [Table of Contents](#table-of-contents)