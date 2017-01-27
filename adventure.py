#--------------------------------------------------------------------------
#GAME BY - JUAN DAVID GUERRA, GIJS NOTEBOOM, MICHAEL BATEMAN AND HARRY JIANG
#ADVENTURE STORY GAME
#MAIN CHARACTER - Adrastos, son of Arachne
#VILLAIN - Child molesters
#PLACE - Mythical forest in Canada 
#PLOT - Adrastos got kidnapped by a bunch of child molesters
#He was given a claymore as a way to be able to survive 
#This is a form of entertainment for the child molesters and Satan
#(he will confront as the final boss battle)
#and was dropped off in the middle of a mythical forest full of deadly creatures.
# He has to fight his way out of the forest 
# Clock in the sky, every game time day, new set of monsters appear
#Every time the monsters respawn, they become harder to kill and more dangerous
#Type of game - Choice based game, you control the main character
#--------------------------------------------------------------------------

[![Build Status](https://travis-ci.org/juan-david1025/Adventure_Game.svg?branch=master)](https://travis-ci.org/juan-david1025/Adventure_Game) 

# Imports
import pygame
import time
import sys

#need to init first
pygame.init()

# Load the window and keep track of the surface
# for drawing into the screen/window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 

#Adrastos (main character) will have 500 hitpoints 
health = 500

#BATTLE STATS SWORD HITS = 10 HEALTH 

#Normal ogre health will be 20
ogreh = 20

#Hydra (boss)
#Hydra chance of hitting you increases with the amount of heads he has
def hydraregen (heads, ad):
	hydrahealth = heads * 20
hydrah = hydraregen(6, 30)

#Loading the logo for first frame
asurf = pygame.image.load('LOGO.png')
imgRect = asurf.get_rect()
imgRect.centerx = screen.get_rect().centerx
imgRect.centery = screen.get_rect().centery

while True:
	 
	#loading the message for the second frame
	fsize = 48
	msg = 'WELCOME TO THE ADVENTURE OF A LIFETIME, PRESS \'S\' TO CONTINUE' 
	font = pygame.font.Font(None, fsize)
	text = font.render(msg, True, (250, 250, 250))
	textRect = text.get_rect()
	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery

	#draw the logo
	screen.blit(asurf, imgRect)
	pygame.display.flip()
	
	#stop the time for a bit
	time.sleep(5)
	
	#draw the text to start the game
	screen.blit(text, textRect)
	pygame.display.flip()

	for idle_event in pygame.event.get():
		if idle_event.type == pygame.QUIT:
			sys.exit()

			if idle_event.type == KEYDOWN:
				if idle_event.key == K_ESCAPE:
					sys.exit()	
			
					if idle_event.type == KEYDOWN:
						if idle_event.key == 115:
							sys.exit()
