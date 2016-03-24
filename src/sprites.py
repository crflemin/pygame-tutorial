import pygame, utility
from pygame.locals import *
from utility import *

class Skunk(pygame.sprite.Sprite):
	#this __init__ method is called the constructor
	#it will be called whenever we call the method Skunk(xcoord, ycoord)
	def __init__(self, xcoord, ycoord):
		#call Sprite intializer from pygame first
		pygame.sprite.Sprite.__init__(self)
		#load an image file and rectangle corresponding to that image
		self.image, self.rect = load_image('..\\images\\skunk.png', -1)
		#get a reference to the game area that we're working with
		screen = pygame.display.get_surface()
		#save the dimensions of the game area so that we can check to make sure we don't move outside it
		self.area = screen.get_rect()
		#place the Skunk image at the coordinates given
		self.rect.bottomleft = xcoord, ycoord
		#self.move is a variable belonging to Skunk that we use as a fixed pixel "step size" for walking
		self.move = 10
		#self.dizzy will be used to measure the angle we have rotated during a spin-out
		self.dizzy = 0
		#self.right_last is 1 if we last moved to the right and 0 if we last moved left
		#we need this to determine which way the Skunk is facing and when to flip the sprite
		self.right_last = 1
		#flip the sprite initially, because the image is facing to the left by default
		self.image = pygame.transform.flip(self.image, 1, 0)

	#Skunk's update method is used to animate the spinout if self.dizzy has been set by did_slip	
	def update(self):
		if self.dizzy:
			self._spin()

	def walk_right(self):
		#flip the image if we are still facing left
		if self.right_last == 0:
			self.image = pygame.transform.flip(self.image, 1, 0)
			self.right_last = 1
		#make sure that we are still within the game bounds before moving the sprite rectangle
		if self.rect.right <= self.area.right:
			newpos = self.rect.move((self.move, 0))
			self.rect = newpos
		
	def walk_left(self):
		#flip the image if we are still facing right
		if self.right_last == 1:
			self.image = pygame.transform.flip(self.image, 1, 0)
			self.right_last = 0
		#make sure that we are still within the game bounds before moving the sprite rectangle
		if self.rect.left >= self.area.left:
			newpos = self.rect.move((-self.move, 0))
			self.rect = newpos	

	#used to rotate the Skunk image 12 degrees; called by update to animate spin-out
	#dizzy is used here to store the number of degrees we've rotated so far
	def _spin(self):
		center = self.rect.center
		#add 12 degrees to dizzy
		self.dizzy = self.dizzy + 12
		#if we've already rotated a full 360, reset dizzy to 0 to stop spinning and draw original image
		if self.dizzy >= 360:
			self.dizzy = 0
			self.image = self.original
		#otherwise, perform a pygame rotate on the original image using dizzy as degrees of rotation
		else:
			rotate = pygame.transform.rotate
			self.image = rotate(self.original, self.dizzy)
		self.rect = self.image.get_rect(center=center)
		#this is a great example of print debugging! I wanted to see output to cmd every time we call _spin
		print self.dizzy

	#used to detect collision with a Banana (target)
	def did_slip(self, target):
		#grab a rectangle within Skunk
		hitbox = self.rect.inflate(-5, -5)
		#check whether this rectangle overlaps with the target Banana
		if hitbox.colliderect(target.rect):
			self.dizzy = 1
			self.original = self.image
			return True
		else:
			return False

	#used to detect collision with Cake
	#same as did_slip, but we don't start spinning out
	def did_eat(self, target):
		hitbox = self.rect.inflate(-5, -5)
		return hitbox.colliderect(target.rect)
	
	
class Cake(pygame.sprite.Sprite):
	#this __init__ method is called the constructor
	#it will be called whenever we call the method Cake(xcoord, ycoord)
	def __init__(self, xcoord, ycoord):
		#call Sprite initializer
		pygame.sprite.Sprite.__init__(self)
		#use the image loader in utility.py to give this sprite an image
		self.image, self.rect = load_image('..\\images\\cake.jpg', -1)
		#place the sprite according to its bottom left corner using the coordinates input to this method
		self.rect.bottomleft = xcoord, ycoord

	def update(self):
		pass
		#to give the banana motion, remove the "pass" code from here
		#use the walk methods in skunk.py for examples of moving sprite images, flipping them, and checking game area boundaries
		#be aware of the game area and decide whether it is ok for your images to move off the screen
		

class Banana(pygame.sprite.Sprite):
	#this __init__ method is called the constructor
	#it will be called whenever we call the method Banana(xcoord, ycoord)
	def __init__(self, xcoord, ycoord):
		#call Sprite initializer from pygame first
		pygame.sprite.Sprite.__init__(self)
		#use the image loader in utility.py to give this sprite an image
		self.image, self.rect = load_image('..\\images\\banana_peel.png', -1)
		#place the sprite according to its bottom left corner using the coordinates input to this method
		self.rect.bottomleft = xcoord, ycoord

	def update(self):
		pass
		#to give the banana motion, remove the "pass" code from here
		#use the walk methods in skunk.py for examples of moving sprite images, flipping them, and checking game area boundaries
		#be aware of the game area and decide whether it is ok for your images to move off the screen