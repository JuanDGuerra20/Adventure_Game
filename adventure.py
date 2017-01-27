#--------------------------------------------------------------------------
#GAME BY - JUAN DAVID GUERRA AND GIJS NOTEBOOM
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
#--------------------------------------------------------------------------

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
hydrah = hydraregen(6, 10)

while True:
	fsize = 48
	msg = 'WELCOME TO THE ADVENTURE OF A LIFETIME, PRESS \'S\' TO CONTINUE' 
	font = pygame.font.Font(None, fsize)
	text = font.render(msg, True, (250, 250, 250))
	textRect = text.get_rect()
	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery
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
