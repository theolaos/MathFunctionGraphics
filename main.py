# Example file showing a basic pygame "game loop"
import pygame
import math
#import pygame.geometry

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
print(math.sin(4))
def math_function_pygame(math_function):
    x1 = 0
    x2 = 0
    y2 = +360
    points_list = []
    dy = 0
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        y1 = math_function(x1)

        # if x1 != 0:
        #     dy = y1 - y2
        #     x1 += dy

        # pygame.draw.circle(screen,(255,255,255),(x,-y+360),1)
        if x1 != 0:
            pygame.draw.line(screen,(255,255,255),(x1,-y1+360),(x2,y2))
        # flip() the display to put your work on screen
        pygame.display.flip()

        if -y1+360 < 0 or y1 > 720:
            print(x1,y1)
            break

        if x1 > 1280:
            break
        # print(x1,y1)
        x2 = x1
        y2 = -y1+360
        
        x1 += 1


# idk what the real name is
def cartesian_lines():
    ...

# def x_y(x): # y = x
#     return (x**2)/30

def x_y2(x):
    return 40*math.cos(x/10)

# math_function_pygame(x_y)
math_function_pygame(x_y2)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)  # limits FPS to 60

pygame.quit()
