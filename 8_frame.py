import pygame

###############################################################3
#neccesary things
pygame.init() #init

screen_width = 480 #width
screen_height = 640 #height
screen = pygame.display.set_mode((screen_width, screen_height))


#set of display title

pygame.display.set_caption("hahahaha") #game name

#FPS
clock = pygame.time.Clock()
################################################################3

#1. user game initialization(background, image, coordinate, speed, font...)

#2. event (keyboard, mouse,...)

while running:
    dt = clock.tick(60) 

    print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False  
# 3. game characters position definition
   

# 4. handling Collision
   
# 5. draw upon display


    pygame.display.update()

pygame.quit()

