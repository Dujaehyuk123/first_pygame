import pygame


pygame.init() #init

screen_width = 480 #width
screen_height = 640 #height
screen = pygame.display.set_mode((screen_width, screen_height))


#set of display title

pygame.display.set_caption("hahahaha") #game name

#FPS
clock = pygame.time.Clock()


# background pic load
background = pygame.image.load("C:/Users/Hyuk/Desktop/apartment/apartment/apt_price/pygames/background.png")

# chracter pic load
character = pygame.image.load("C:/Users/Hyuk/Desktop/apartment/apartment/apt_price/pygames/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height -  character_height

#ememy character

enemy = pygame.image.load("C:/Users/Hyuk/Desktop/apartment/apartment/apt_price/pygames/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)


#coordination to move
to_x = 0
to_y = 0

#moving speed
character_speed = 0.6




#event loop
running = True  #is the game proceeding?
while running:
    dt = clock.tick(60) #game screen set of fps(frame per second)

    print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get(): #what event occureed?
        if event.type == pygame.QUIT: #quit event occured?
            running = False  #finish
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

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

    # update rect info for collision process
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # check collision
    if character_rect.colliderect(enemy_rect):
        print("Collided")
        running = False

    screen.blit(background, (0, 0)) #draw background
    screen.blit(character, (character_x_pos, character_y_pos)) #draw character
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #draw enemy

    
    pygame.display.update()
    
#pygame finish

pygame.quit()

