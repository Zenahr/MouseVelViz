# HOW TO GET MOTIONBLUR WORKING?
# just blit the sprite several times at various time increments and change the per-surface alpha for each blit. You''ll get a pseudo fade-out look. 

import pygame
from pygame.locals import *
from app import track_mouse_movement
import time
from collections import deque
from config import WIDTH, HEIGHT, BACKGROUND_COLOR, FADE_DELTA, POINT_RADIUS, PRIMITIVE, DRAW_STATS, PRIMITIVE_COLOR


def clamp(n, minn, maxn):
    return int(max(min(maxn, n), minn))

pygame.init()

myfont = pygame.font.SysFont('Roboto', 16)

pygame.display.set_caption('Mouse Velocity Visualizer')
clock = pygame.time.Clock()
clock.tick(30)
window = pygame.display.set_mode((WIDTH, HEIGHT))
surf = pygame.Surface(window.get_size(), pygame.SRCALPHA)
alpha_surf = pygame.Surface(surf.get_size(), pygame.SRCALPHA)
surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
rect = surf.get_rect()
# window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME) # No Window Frame
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
    window.fill(BACKGROUND_COLOR)
    mouse_data = track_mouse_movement()
    POINT = mouse_data['new_point']
    if mouse_data['no_movement'] == False:
        if PRIMITIVE == 'line':
            pygame.draw.line(surf, PRIMITIVE_COLOR, (WIDTH/2, HEIGHT/2), POINT)
        elif PRIMITIVE == 'point':
            pygame.draw.circle(surf, PRIMITIVE_COLOR, POINT, POINT_RADIUS, 0)

        if DRAW_STATS:
            # TEXT ------------------------------------------------------------------------------------------
            velocity = myfont.render('velocity: {0}'.format(int(mouse_data['velocity'])), True, (255, 255, 255))
            mouseX   = myfont.render('x: {0}'.format(int(mouse_data['x'])), True, (255, 255, 255))
            mouseY   = myfont.render('y: {0}'.format(int(mouse_data['y'])), True, (255, 255, 255))
            window.blit(mouseX,(10,10))
            window.blit(mouseY,(10,30))
            window.blit(velocity,(10,50))
            # TEXT ------------------------------------------------------------------------------------------

    alpha_surf.fill((255, 255, 255, FADE_DELTA))  # Set the alpha here (4th argument).
    surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        # UNCOMMENT SECOND BLIT TO PERFORM AUGMENTED FADE
        # alpha_surf.fill((255, 255, 255, FADE_DELTA-10))  # Set the alpha here (4th argument).
        # surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    window.blit(surf, rect)
    pygame.display.flip()

pygame.quit()
exit()