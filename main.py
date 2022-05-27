import time

import pygame

from datetime import datetime
import math

RES = WIDTH, HEIGHT = 1200, 800

# Half of screen
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2 

RADIUS = H_HEIGHT - 50

radius_list = {
    'level': RADIUS - 5,
    'sec': RADIUS - 10,
    'min': RADIUS - 55,
    'hour': RADIUS - 100,
    'digit': RADIUS - 30}


pygame.init()

BG_COLOR = (0, 0, 0)

font = pygame.font.SysFont('Verdana', 60)


surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))
zero10 = dict(zip(range(91), range(0, 91, 1)))
level = 80

my_switch = False

def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y 


def get_to_zero():
    global level
    if level > 30 < 35:
        level -= 1
   # if level > 35 < 40:
   #     level -= 10


    if level > 40:
        level -= 1

    else:
        pass



start_time = None

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if level > 88:
                    start_time = pygame.time.get_ticks()
                    get_to_zero()
                else:
                    level += 2

    surface.fill(BG_COLOR)

    if start_time:
        #my_switch = True
        time_since_enter = pygame.time.get_ticks() - start_time
        message = 'M since : ' + str(time_since_enter)
        surface.blit(font.render(message, True, (0, 255, 0)), (20, 20))

        if time_since_enter % 10 == 1:
            get_to_zero()

    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12), t.minute, t.second

    pygame.draw.circle(surface, pygame.Color('darkslategray'), (H_WIDTH, H_HEIGHT), RADIUS)

    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(zero10, level, 'level'), 10)

    pygame.display.set_caption(f'LEVEL: {level :.2f}')
    pygame.display.flip()
    clock.tick(60)


