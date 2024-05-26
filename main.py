import pygame
import random
import threading
pygame.init()
pygame.mixer.init()
screen_width = 600 
screen_height = 600 
sound_click = pygame.mixer.Sound("bubble.mp3")
bg_sound = pygame.mixer.Sound("bg.wav")
bg_sound.set_volume(0.2)
screen = pygame.display.set_mode((screen_width, screen_height))  
pygame.display.set_caption("Click rect get points!!")
screen_widthMid = screen_width / 2 
screen_heightMid = screen_height / 2


font = pygame.font.SysFont("Arial",30)


x = 100
white = (255, 255, 255)
black = (0, 0, 0)



clock = pygame.time.Clock()
FPS = 60
running = True
x = 100
y = 100
w = 50
h = 50
points = 0
rand = random.randrange(1,300)
bg_sound.play(-1)
gravity = 4
while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                
                if rect.collidepoint(mouse_pos):
                    sound_click.play()
                    new_x = random.randrange(0,screen_width - x)
                    new_y = random.randrange(0,screen_height -y)
                    x = new_x
                    y = new_y
                    points += 1
                    
    screen.fill(black)

    
    rect = pygame.Rect(x,y,w,h)
    pygame.draw.rect(screen,white,rect)
   


    text_label = font.render("Point: " +str(points) , True, white)

    screen.blit(text_label,(0,0))
   
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
