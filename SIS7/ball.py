import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("RED ball")
pygame.display.set_icon(pygame.image.load('images/ball.png'))

done = False
x = 400
y = 400
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                        done = True

    pressed = pygame.key.get_pressed()
    if y <= 760 and y >= 40:
        if pressed[pygame.K_UP] : y -= 20
        if pressed[pygame.K_DOWN] : y += 20
    elif y > 760: 
        if pressed[pygame.K_UP] : y -= 20
        if pressed[pygame.K_DOWN] : y += 0
    elif y < 40: 
        if pressed[pygame.K_UP] : y -= 0
        if pressed[pygame.K_DOWN] : y += 20
    if x <= 760 and x >= 40:
        if pressed[pygame.K_LEFT] : x -= 20
        if pressed[pygame.K_RIGHT] : x += 20
    elif x > 760: 
        if pressed[pygame.K_LEFT] : x -= 20
        if pressed[pygame.K_RIGHT] : x += 0
    elif x < 40: 
        if pressed[pygame.K_LEFT] : x -= 0
        if pressed[pygame.K_RIGHT] : x += 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, 'Red', (x, y), 25)
    pygame.display.flip()