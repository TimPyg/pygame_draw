import pygame
from pygame.draw import *
from colorf.color import *

pygame.init()

FPS = 28
WIDTH,HEIGHT = 800, 500
screen = pygame.display.set_mode( (WIDTH,HEIGHT) )

# sky
rect(screen, BLUE, (0, 0, 800, 250))
# glass
rect(screen, (0, 128, 0), (0, 250, 800, 270))
# house
rect(screen, BROWN, (140, 220, 200, 140))
# windows
rect(screen, BEREZOVY, (200, 260, 60, 55))
# крыша                 вершина
polygon(screen, RED, [[230, 120], [140, 220], [340, 220]])
# облака
#tree
pygame.draw.line(screen, BROWN, [580,320], [580, 230], 12)
#ЛИСТВА
pygame.draw.circle(screen, DARK_GREEN, [580, 150], 40)
pygame.draw.circle(screen, BLACK, [580, 150], 40, 1)

pygame.draw.circle(screen, DARK_GREEN, [540, 180], 40)
pygame.draw.circle(screen, BLACK, [540, 180], 40, 1)
pygame.draw.circle(screen, DARK_GREEN, [620, 180], 40)
pygame.draw.circle(screen, BLACK, [620, 180], 40, 1)

pygame.draw.circle(screen, DARK_GREEN, [580, 200], 40)
pygame.draw.circle(screen, BLACK, [580, 200], 40, 1)
# нижние листья
pygame.draw.circle(screen, DARK_GREEN, [550, 240], 40)
pygame.draw.circle(screen, BLACK, [550, 240], 40, 1)
pygame.draw.circle(screen, DARK_GREEN, [610, 240], 40)
pygame.draw.circle(screen, BLACK, [610, 240], 40, 1)
#sun
pygame.draw.circle(screen, YELLOW, [700, 80], 40, )
#cloud
pygame.draw.ellipse(screen, WHITE, [420,40, 40, 40]) 
pygame.draw.ellipse(screen, BLACK, [420,40, 40, 40], 1)
pygame.draw.ellipse(screen, WHITE, [400,40, 40, 40]) 
pygame.draw.ellipse(screen, BLACK, [400,40, 40, 40], 1)
pygame.draw.ellipse(screen, WHITE, [380,40, 40, 40]) 
pygame.draw.ellipse(screen, BLACK, [380,40, 40, 40], 1)
pygame.draw.ellipse(screen, WHITE, [360,40, 40, 40]) 
pygame.draw.ellipse(screen, BLACK, [360,40, 40, 40], 1)

pygame.draw.ellipse(screen, WHITE, [400,20, 40, 40]) 
pygame.draw.ellipse(screen, BLACK, [400,20, 40, 40], 1)
pygame.draw.ellipse(screen, WHITE, [380,20, 40, 40]) 
pygame.draw.ellipse(screen, BLACK, [380,20, 40, 40], 1)



pygame.display.update()
clock = pygame.time.Clock()
Finish = False

while not Finish:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Finish = True

pygame.quit()


# Задание
# github - репозиторий с именем pygame_drow
# загрузить файл draw_pg1.pt на репозиторий
#                 pg1.png
# скинуть ссылку на репозиторий
# нарисовать мачту, зонтик, 

