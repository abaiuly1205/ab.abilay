import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("SoundPlay")
pygame.display.set_icon(pygame.image.load('images/music.png'))
_songs = [
    'music/Дос-Мұқасан - 16 қыз.mp3',
    'music/Kilgore Doubtfire - Escape.mp3',
    'music/The Weeknd - Out of Time.mp3',
    'music/XXXtentacion - Jocelyn Flores.mp3',
    'music/Justin Bieber - Confident.mp3',
    'music/Post Malone - Circles.mp3'
]
covers = [
    pygame.image.load('images/0.jpg'),
    pygame.image.load('images/1.jpg'),
    pygame.image.load('images/2.jpg'),
    pygame.image.load('images/3.jpg'),
    pygame.image.load('images/4.jpg'),
    pygame.image.load('images/5.jpg')
]
def play_next_song():
    global i
    i = (i + 1) % len(_songs)
    screen.blit(covers[i], (0, 0))
    pygame.mixer.music.load(_songs[i])
    pygame.mixer.music.play()


def play_previous_song():
    global i
    i = (i - 1) % len(_songs)
    screen.blit(covers[i], (0, 0))
    pygame.mixer.music.load(_songs[i])
    pygame.mixer.music.play()

done = True
playing = False
i = 0

while done:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RETURN]:
        screen.blit(covers[i], (0, 0))
        pygame.mixer.music.load(_songs[i])
        pygame.mixer.music.play()
    
    if pressed[pygame.K_RIGHT]: 
        play_next_song()
    
    if pressed[pygame.K_LEFT]:
        play_previous_song()
    
    if pressed[pygame.K_SPACE]:
            if playing:
                pygame.mixer.music.pause()
                playing = False
            else:
                pygame.mixer.music.unpause()
                playing = True
    pygame.display.flip()
    clock.tick(15)