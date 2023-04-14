import pygame
from copy import deepcopy
from random import choice, randrange
from const import *

pygame.init()
sc = pygame.display.set_mode(RES)
game_sc = pygame.time.Clock()

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(WIDTH) for y in range(HEIGHT)]
figures = [[pygame.Rect(x + WIDTH // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in FIGURES_POSITION]
field = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

anim_count, anim_speed, anim_limit = ANIM_COUNT, ANIM_SPEED, ANIM_LIMIT

bg = pygame.image.load('img/b1.jpg').convert()
game_bg = pygame.image.load('img/b2.jpg').convert()

main_font = pygame.font.Font('font/font.ttf', 70)
my_font = pygame.font.Font('font/font.ttf', 50)

title_tetris = main_font.render('TETRIS', True, pygame.Color('darkorange'))
title_record = my_font .render('record:', True, pygame.Color('purple'))
title_score = my_font.render('score:', True, pygame.Color('green'))

get_color = lambda: (randrange(50, 256), randrange(50, 256), randrange(50, 256))
figure, next_figure = deepcopy(choice(figures), deepcopy(choice(figures)))

score, lines = 0, 0
score = {}
