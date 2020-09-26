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

#coordination to move

to_x = 0
to_y = 0



#event loop
running = True  #is the game proceeding?
while running:
    for event in pygame.event.get(): #what event occureed?
        if event.type == pygame.QUIT: #quit event occured?
            running = False  #finish
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    #width bondary 
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos =  screen_width - character_width

    #height boundary
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


            
    screen.blit(background, (0, 0)) #draw background
   
    screen.blit(character, (character_x_pos, character_y_pos)) #draw character
    
    pygame.display.update()
    
#pygame finish

pygame.quit()

