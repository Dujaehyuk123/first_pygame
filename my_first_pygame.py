import pygame

pygame.init() #init

screen_width = 480 #width
screen_height = 640 #height
screen = pygame.display.set_mode((screen_width, screen_height))

#set of display title

pygame.display.set_caption("hahahaha") #game name

#event loop
running = True  #is the game proceeding?
while running:
    for event in pygame.event.get(): #what event occureed?
        if event.type == pygame.QUIT: #quit event occured?
            running = False  #finish


#pygame finish

pygame.quit()

