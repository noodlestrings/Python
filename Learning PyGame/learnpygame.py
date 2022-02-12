import pygame#REQUIRED CODE


#initialises pygame library for use
pygame.init()#REQUIRED CODE


#creates the window
screen = pygame.display.set_mode((800, 600))


#Title and Icon
pygame.display.set_caption("Window 1")

icon = pygame.image.load('icon.ico')
pygame.display.set_icon(icon)


#insert player
playerimg = pygame.image.load('rocket.png')
playerX = 340
playerY = 480

def player():
	screen.blit(playerimg, (playerX, playerY))


#Game Loop
running = True
while running:

	screen.fill((110, 11, 110))#changes fill color of window

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	

	player()#function to display player
	

	pygame.display.update()#REQUIRED CODE

##https://youtu.be/FfWpgLFMI7w?t=1863