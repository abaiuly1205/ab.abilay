import pygame

def R(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1-x2)
    h = abs(y1-y2)
    return (x, y, w, h)
def C(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    return (x, y)

pygame.init()
FPS = 60
clock = pygame.time.Clock()

mode = 'blue'

screen = pygame.display.set_mode((400, 300))
another_layer = pygame.Surface((400, 300))

x1 = 0
x2 = 0
y1 = 0
y2 = 0

w = 100
h = 100
color = (0, 128, 255)
isMouseDown = False
screen.fill((0, 0, 0))
mode = 'rect'

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: color = (194, 6, 6) 
            elif event.key == pygame.K_g: color = (95, 235, 52)
            elif event.key == pygame.K_b: color = (58, 52, 235)
###         elif event.key == pygame.K_1: mode = 'pen'
            elif event.key == pygame.K_2: mode = 'rect'
            elif event.key == pygame.K_3: mode = 'circle'
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1 = event.pos[0]
            y1 = event.pos[1]
            isMouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        isMouseDown = False
                        another_layer.blit(screen, (0, 0))
        if mode == 'rect':
             if event.type == pygame.MOUSEMOTION:
                        if isMouseDown:
                            x2 = event.pos[0]
                            y2 = event.pos[1]
                            screen.blit(another_layer, (0, 0))
                            pygame.draw.rect(screen, color, pygame.Rect(R(x1, y1, x2, y2)), 1)
        elif mode == 'circle':
             if event.type == pygame.MOUSEMOTION:
                        if isMouseDown:
                            x2 = event.pos[0]
                            y2 = event.pos[1]
                            screen.blit(another_layer, (0, 0))
                            pygame.draw.circle(screen, color, C(), abs(x1-x2)/2)            
    screen.fill((0, 0, 0))