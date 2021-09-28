#includes pause
import pygame
import sys
import random

pygame.init()
FPS = 30
#colours

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# creating windows

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

# background image
co = pygame.image.load("background.jpg")
mp= pygame.image.load("back2.jpg")
bk = pygame.image.load("snake.jpg")

co= pygame.transform.scale(co,(WINDOW_WIDTH,WINDOW_HEIGHT))
mp= pygame.transform.scale(mp,(WINDOW_WIDTH,WINDOW_HEIGHT))
bk = pygame.transform.scale(bk,(WINDOW_WIDTH,WINDOW_HEIGHT))


VELOCITY = 10
SNAKE_WIDTH = 15
APPLE_SIZE = 20
TOP_WIDTH = 40
small_font = pygame.font.SysFont('forte', 25)
medium_font = pygame.font.SysFont('showcard gothic', 30, True)
large_font = pygame.font.SysFont('chiller', 60, True, True)
clock = pygame.time.Clock()

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

#images for items
snake_img = pygame.image.load('block.jpg')
apple_img = pygame.image.load('apple.jpg')
apple_img_rect = apple_img.get_rect()

#music for background,crash and eat
pygame.mixer.music.load('bg_music_1.mp3')

pygame.mixer.music.play(1)


def start_game():
    canvas.fill(BLACK)
    canvas.blit(bk,(0,0))
    start_font1 = large_font.render("Welcome To Snake Game", True,BLUE,RED)
    start_font2 = large_font.render("Play Game", True, RED, YELLOW)
    start_font3 = large_font.render("Rules", True, RED, YELLOW)
    start_font4 = large_font.render("Quit", True, RED, YELLOW)
    start_font5 = large_font.render("Creator", True, RED, YELLOW)
    start_font1_rect = start_font1.get_rect()
    start_font2_rect = start_font2.get_rect()
    start_font3_rect = start_font3.get_rect()
    start_font4_rect = start_font4.get_rect()
    start_font5_rect = start_font5.get_rect()

    start_font1_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 200)
    start_font2_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT/2 + 50)
    start_font3_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT / 2 + 100)
    start_font5_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT / 2 + 150)
    start_font4_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT/2 + 200)

    canvas.blit(start_font1, start_font1_rect)
    canvas.blit(start_font2, start_font2_rect)
    canvas.blit(start_font3, start_font3_rect)
    canvas.blit(start_font4, start_font4_rect)
    canvas.blit(start_font5, start_font5_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameloop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_font3_rect.left and x < start_font3_rect.right:
                    if y > start_font3_rect.top and y < start_font3_rect.bottom:
                        start_inst(start_font1, start_font1_rect)
                if x > start_font2_rect.left and x < start_font2_rect.right:
                    if y > start_font2_rect.top and y < start_font2_rect.bottom:
                        gameloop()
                if x > start_font5_rect.left and x < start_font5_rect.right:
                    if y > start_font5_rect.top and y < start_font5_rect.bottom:
                        creator()
                if x > start_font4_rect.left and x < start_font4_rect.right:
                    if y > start_font4_rect.top and y < start_font4_rect.bottom:
                        pygame.quit()
                        sys.exit()



        pygame.display.update()






