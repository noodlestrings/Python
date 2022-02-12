import pygame
import random
import time
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Rock Paper Scissors")
 

#player_rock
playerrock = pygame.image.load('rock.png')
playerrockX = 50
playerrockY = 460

def player_rock():
	screen.blit(playerrock, (playerrockX, playerrockY))



#player_paper
playerpaper = pygame.image.load('paper.png')
playerpaperX = 340
playerpaperY = 415

def player_paper():
	screen.blit(playerpaper, (playerpaperX, playerpaperY))



#player_scissors
playerscissors = pygame.image.load('scissors.png')
playerscissorsX = 625
playerscissorsY = 415

def player_scissors():
	screen.blit(playerscissors, (playerscissorsX, playerscissorsY))



#text for instructions
message_displayed = """Press \'r\' for rock, \'p\' for paper, and \'s\' for scissors"""
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 32)
text = font.render(message_displayed, True, white, black)
textRect = text.get_rect()
textRect.center = (screenwidth // 2, 25)















#text for winning or losing
win_message = "You win!"
win_text = font.render(win_message, True, white, black)
win_textRect = win_text.get_rect()
win_textRect.center = (screenwidth // 2, 200)

los_message = "You lost!"
los_text = font.render(los_message, True, white, black)
los_textRect = win_text.get_rect()
los_textRect.center = (screenwidth // 2, 250)#

draw_message = "You drew!"
draw_text = font.render(draw_message, True, white, black)
draw_textRect = draw_text.get_rect()
draw_textRect.center = (screenwidth // 2, 250)#


#text for computer selection
cpu_message1 = "Computer selects paper"
cpu1_text = font.render(cpu_message1, True, white, black)
cpu1_textRect = cpu1_text.get_rect()
cpu1_textRect.center = (screenwidth // 2, 100)

cpu_message2 = "Computer selects rock"
cpu2_text = font.render(cpu_message2, True, white, black)
cpu2_textRect = cpu2_text.get_rect()
cpu2_textRect.center = (screenwidth // 2, 100)

cpu_message3 = "Computer selects scissors"
cpu3_text = font.render(cpu_message3, True, white, black)
cpu3_textRect = cpu3_text.get_rect()
cpu3_textRect.center = (screenwidth // 2, 100)






#random generator for response to input
random_select_paper = 1
random_select_rock = 2
random_select_scissors = 3

random_select_master = random.randint(1,3)

def random_enemy_log():
	if random_select_master == random_select_paper:
		return(print("computer selects paper"))
	elif random_select_master == random_select_rock:
		return(print("computer selects rock"))
	elif random_select_master == random_select_scissors:
		return(print("computer selects scissors"))

def random_enemy_function():
	if random_select_master == random_select_paper:
		return(random_select_paper)
	elif random_select_master == random_select_rock:
		return(random_select_rock)
	elif random_select_master == random_select_scissors:
		return(random_select_scissors)

#main game code
keypressed = 0
running = True
while running:

	screen.fill((0, 0, 0))
	screen.blit(text, textRect)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:

			if event.key == pygame.K_r:
				print("r")
				playerrockY += -400
				random_enemy_log()
				if random_enemy_function() == 1:
					print("paper wins")
					playerpaperY += -350
					playerpaperX += 285
					player_paper()
					playerrockY += 400
					player_rock()
					screen.blit(cpu1_text, cpu1_textRect)
					screen.blit(los_text, los_textRect)
					pygame.display.update()
					time.sleep(4.5)
					exit()

				elif random_enemy_function() == 2:
					print("draw")
					player_rock()
					screen.blit(cpu2_text, cpu2_textRect)
					screen.blit(draw_text, draw_textRect)
					pygame.display.update()
					time.sleep(4.5)
					exit()

				elif random_enemy_function() == 3:
					print("rock wins")
					player_scissors()
					playerrockY += 35
					player_rock()
					screen.blit(cpu3_text, cpu3_textRect)
					screen.blit(win_text, win_textRect)
					pygame.display.update()
					time.sleep(4.5)
					exit()

			elif event.key == pygame.K_p:
				print("p")
				playerpaperY += -325
				playerpaperX += 50
				random_enemy_log()
				if random_enemy_function() == 1:
					print("draw")
					playerpaperX += 200
					player_paper()
					screen.blit(cpu1_text, cpu1_textRect)
					screen.blit(draw_text, draw_textRect)
					pygame.display.update()
					time.sleep(4.5)
					exit()

				elif random_enemy_function() == 2:
					print("paper wins")
					playerpaperX += 200
					player_paper()
					player_rock()
					screen.blit(cpu2_text, cpu2_textRect)
					screen.blit(win_text, win_textRect)
					pygame.display.update()
					time.sleep(4.5)
					exit()

				elif random_enemy_function() == 3:
					print("scissors wins")
					playerpaperY += 325
					playerpaperX += -50
					playerscissorsY += - 325
					player_scissors()
					player_paper()
					screen.blit(cpu3_text, cpu3_textRect)
					screen.blit(los_text, los_textRect)
					pygame.display.update()
					time.sleep(4.5)
					exit()

			elif event.key == pygame.K_s:
				print("s")
				playerscissorsY += -400
				playerscissorsX += -20
				random_enemy_log()
				if random_enemy_function() == 1:
					print("scissors wins")
					player_paper()
					playerscissorsY += 100
					player_scissors()
					screen.blit(cpu1_text, cpu1_textRect)
					screen.blit(win_text, win_textRect)
					pygame.display.update()
					time.sleep(4.5)
					exit()

				elif random_enemy_function() == 2:
					print("rock wins")
					playerrockY += -365
					player_rock()
					playerscissorsY += 400
					playerscissorsX += 20
					player_scissors()
					screen.blit(cpu2_text, cpu2_textRect)
					screen.blit(los_text, los_textRect)
					pygame.display.update()
					time.sleep(4.5)
					exit()

				elif random_enemy_function() == 3:
					print("draw")
					playerscissorsY += 100
					player_scissors()
					screen.blit(cpu3_text, cpu3_textRect)
					screen.blit(draw_text, draw_textRect)
					pygame.display.update()
					time.sleep(4.5)
					exit()



	player_scissors()
	player_paper()
	player_rock()



	pygame.display.update()
