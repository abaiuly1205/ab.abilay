import pygame
import math
import datetime

pygame.init()

display = pygame.display.set_mode((1400, 1050))
pygame.display.set_caption('Clock')
clock = pygame.time.Clock()
CENTER = (1400 / 2, 1050 / 2)

back = pygame.image.load('images/mainclock.png')
mickey_second_hand = pygame.image.load('images/leftarm.png')
mickey_minute_hand = pygame.image.load('images/rightarm.png')
mickey_rect1 = mickey_second_hand.get_rect(center=CENTER)
mickey_rect2 = mickey_minute_hand.get_rect(center=CENTER)


def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        display.blit(back, (0, 0))
        mickey_second_hand = pygame.image.load('images/leftarm.png')
        mickey_minute_hand = pygame.image.load('images/rightarm.png')
        
        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute

        #second
        theta1 = (second)*(360/60)
        rotated_second_hand = pygame.transform.rotate(mickey_second_hand, -theta1)
        display.blit(rotated_second_hand, mickey_rect1)

        #minute
        theta2 = (minute+second/60)*(360/60)
        rotated_minute_hand = pygame.transform.rotate(mickey_minute_hand, -theta2)
        display.blit(rotated_minute_hand, mickey_rect2)


        pygame.display.flip()
        clock.tick(50)
    
game()
pygame.quit()