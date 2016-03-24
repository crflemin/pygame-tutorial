#use "import" to tell python which libraries it needs to have handy to run your program
import os, pygame, sprites
from pygame.locals import *
from sprites import *

#print some warnings if this pygame library is missing
if not pygame.font: print 'Warning, fonts disabled'

def main():
	"""this function is called when the program starts.
	   it initializes everything it needs, then runs in
	   a loop until the function returns."""
#Initialize Everything
	#first, do setup required by pygame
	pygame.init()
	#next, name the game window "screen" and initialize it as a 600 x 400 (pixel) box
	screen = pygame.display.set_mode((800, 400))
	#set the name of the game window
	pygame.display.set_caption('I want cake!')
	#disable the mouse cursor when you hover over the game window
	pygame.mouse.set_visible(0)

#Create The Backgound
	#create an object called "background" that respresents the game area background within "screen"
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	#fill the background with a solid color, represented by (red, green, blue)
	#each component of the color can be a value between 0 and 255
	
	#choose a different color using rgb notation at http://www.w3schools.com/tags/ref_colorpicker.asp
	background.fill((250, 250, 250))
	
	#alternate image background!
	# !!! uncomment this line and comment out background.fill above to load an image instead !!!
	#background, sky_rect = load_image("..\\images\\sky.jpg", -1)
	
	#create a rectangle that is 800 x 50 pixels, and place the top left corner at coordinates (0, 350)
	floor = pygame.Rect(0, 350, 800, 50)
	#draw the rectangle "floor" onto "background" with rgb color (10, 10, 10) and an outline width of 0 (which yields a filled box)
	pygame.draw.rect(background, (10, 10, 10), floor, 0)

#Display The Background
	#draw the background color on the screen
	screen.blit(background, (0, 0))
	#force this change to load
	pygame.display.flip()

#Prepare Game Objects
	#set up a clock that can be used for controlling game timing
	clock = pygame.time.Clock()
	#initialize one of each of our sprite objects
	skunk = Skunk(10, 350)
	banana = Banana(300, 375)
	cake = Cake(700, 350)
	#add all sprites to the sprite list for this game
	allsprites = pygame.sprite.RenderPlain((banana, skunk, cake))

#Main Loop
	#while 1 will loop forever, so after doing setup your game will execute this portion of the code repeatedly
	while 1:
		clock.tick(60)
		moved = False

	#Handle Input Events
		#this loop will check for any game events that you (the user) may have triggered since the last frame update
		#events could be keyboard input, mouse clicks, etc.
		#this loop will look for certain types of events, based on your gameplay, and perform actions when the events happen
		for event in pygame.event.get():
			#escape key will end the game
			if event.type == QUIT:
				return
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				return
			#left arrow key will move skunk left
			elif event.type == KEYDOWN and event.key == K_LEFT:
				skunk.walk_left()
				moved = True
			#right arrow key will move skunk right
			elif event.type == KEYDOWN and event.key == K_RIGHT:
				skunk.walk_right()
				moved = True
		#end for
		
		allsprites.update()
		
		#we set the variable moved to True if the user entered either right or left arrow this frame
		#if the skunk moved, we need to determine whether it has collided with either the banana or the cake
		#if it collides with an object, we remove that object from the sprite list
		if moved:
			if banana != None and skunk.did_slip(banana):
				allsprites.remove(banana)
				banana = None
			#end (if banana != None and skunk.did_slip(banana))
			
			if cake != None and skunk.did_eat(cake):
				allsprites.remove(cake)
				cake = None
			
				if pygame.font:
					#if it is, setup font properties to have size 36 of the default font (indicated by "None")
					font = pygame.font.Font(None, 36)
					#create a drawable game element (called a "surface") that contains "I want cake!" with rgb color (10, 10, 10)
					text = font.render("The cake is a lie.", 1, (10, 10, 10))
					#find the center point of the game screen
					#create a rectangular object from the text surface, centered at centerx
					textpos = text.get_rect(centerx=background.get_width()/2)
					#draw the rectangle on the screen (blit = draw/paste onto background)
					background.blit(text, textpos)
				#end (if pygame.font)
			#end (if cake != None and skunk.did_eat(cake))
		#end (if moved)

		#Draw Everything
		screen.blit(background, (-2, -2))
		allsprites.draw(screen)
		pygame.display.flip()
	
	#end (while 1)
#main

#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()