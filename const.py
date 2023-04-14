WIDTH, HEIGHT = 100, 750
TILE = 35
GAME_RES = WIDTH * HEIGHT
RES = 750, 750
FPS = 60

FIGURES_POSITION = [
    [(-2, -1), (-1, -1), (0, -1), (1, -1)],
    [(0, -1), (-1, -1), (-1, 0), (0, 0)],
    [(-1, -1), (0, 0), (-1, 0), (0, 1)],
    [(0, -1), (0, 0), (-1, 0), (-1, 1)],
    [(0, 0), (0, -1), (0, 1), (-1, -1)],
    [(0, -1), (-1, -1), (-1, 0), (-1, 1)],
    [(0, 0), (0, -1), (0, 1), (-1, 0)],
]

ANIM_COUNT, ANIM_SPEED, ANIM_LIMIT = 0, 60, 2000


score, lines = 0, 0
SCORES = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}