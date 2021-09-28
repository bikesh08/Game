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


