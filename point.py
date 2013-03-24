import sys
import pygame
from pygame.locals import Color, KEYUP, K_ESCAPE
from sprite_sheet_anim import SpriteStripAnim

surface = pygame.display.set_mode((600, 800))
FPS = 60

point_frames = FPS / 5
point = SpriteStripAnim(
    'BouncerPointerSprite.png',
    (0, 0, 216, 300), 4, 1, False, point_frames)

black = Color('black')
clock = pygame.time.Clock()
point.iter()
image = point.next()
while True:
    for e in pygame.event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                sys.exit()

    surface.fill(black)
    if not point.stopped:
        image = point.next()
    surface.blit(image, (0, 0))
    pygame.display.flip()

    clock.tick(FPS)
