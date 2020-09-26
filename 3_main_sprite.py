import pygame


pygame.init() #init

screen_width = 480 #width
screen_height = 640 #height
screen = pygame.display.set_mode((screen_width, screen_height))


#set of display title

pygame.display.set_caption("hahahaha") #game name

# background pic load
background = pygame.image.load("C:/Users/Hyuk/Desktop/apartment/apartment/apt_price/pygames/background.png")

# chracter pic load
character = pygame.image.load("C:/Users/Hyuk/Desktop/apartment/apartment/apt_price/pygames/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height -  character_height

#event loop
running = True  #is the game proceeding?
while running:
    for event in pygame.event.get(): #what event occureed?
        if event.type == pygame.QUIT: #quit event occured?
            running = False  #finish
    
    screen.blit(background, (0, 0)) #draw background
   
    screen.blit(character, (character_x_pos, character_y_pos)) #draw character
   
    pygame.display.update() # display keep redrawing
#pygame finish

pygame.quit()

