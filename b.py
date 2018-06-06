import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

ecran_height = 600
ecran_width = 800
Display= pygame.display.set_mode((ecran_width, ecran_height))

pygame.display.set_caption('Dana paint')
Display.fill(white)
pygame.display.update()

Exit = False

ok = 0
tip_pen = 1
color = black
clock = pygame.time.Clock()

while not Exit :
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Exit = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			ok = 1
		elif event.type == pygame.MOUSEBUTTONUP:
			ok = 0
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				tip_pen = 1
			elif event.key == pygame.K_s:
				tip_pen = 2
			elif event.key == pygame.K_d:
				tip_pen = 3
			elif event.key == pygame.K_e:
				tip_pen = 4
			
			elif event.key == pygame.K_h:
				color = black
			elif event.key == pygame.K_j:
				color = red
			elif event.key == pygame.K_k:
				color = green
			elif event.key == pygame.K_l:
				color = blue

		if ok == 1:
			new_x, new_y = pygame.mouse.get_pos()
		

	if ok == 1:
		position = [new_x, new_y]
		
		if tip_pen == 1:	
			pygame.draw.circle(Display, color, position, 10)
		elif tip_pen == 2:
			pygame.draw.rect(Display, color, [new_x, new_y,1,20])
		elif tip_pen == 3:
			pygame.draw.rect(Display, color, [new_x, new_y,2,2])
		elif tip_pen == 4:	
			pygame.draw.circle(Display, white, position, 10)
			

	pygame.display.update()

	#clock.tick(1000)



pygame.quit()

quit()
