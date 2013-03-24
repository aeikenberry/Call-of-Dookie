#!/usr/bin/env python

"""
The most intense game of wrangling drunk idiots there
ever was.
"""

import pygame
from pygame.locals import *
from models import *

if not pygame.font:
    print ('fonts are disabled, moron')
if not pygame.mixer:
    print ('sound is fucked.')

# TODO's: 
#   Change resolution


#
#   Static
#

positions = {
    'POS_1': (200, 325),
    'POS_2': (300, 325),
    'POS_3': (400, 325),
    'POS_4': (500, 325),
    'POS_5': (600, 325),
    'POS_6': (700, 325),
    'POS_7': (800, 325)
}

#
#   Main
#


def main():
    "starts the program"

    #init()

    screen = pygame.display.set_mode((1050, 740))
    pygame.init()
    pygame.display.set_caption('Call of Dookie')
    pygame.mouse.set_visible(0)

    #background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # prepage game objects
    clock = pygame.time.Clock()

    # do some sound imports here

    #
    #   Character Inits
    #

    bouncer = Bouncer()
    hand = PointerHand(500, 630)

    whitey = LinePerson(
        'BlondeBoyPatron.png',
        'BlondeBoyPatron_GreenSelect2.png',
        'BlondeBoyPatron_RedSelect2.png',
        3, positions['POS_4'], 4)

    pos5 = LinePerson(
        'BlondeBoyPatron.png',
        'BlondeBoyPatron_GreenSelect2.png',
        'BlondeBoyPatron_RedSelect2.png',
        3, positions['POS_5'], 5)

    pos6 = LinePerson(
        'BlondeBoyPatron.png',
        'BlondeBoyPatron_GreenSelect2.png',
        'BlondeBoyPatron_RedSelect2.png',
        3, positions['POS_6'], 6)

    pos7 = LinePerson(
        'BlondeBoyPatron.png',
        'BlondeBoyPatron_GreenSelect2.png',
        'BlondeBoyPatron_RedSelect2.png',
        3, positions['POS_7'], 7)

    pos1 = LinePerson(
        'SweatshirtHipster.png',
        'SweatshirtHipster_GreenSelect.png',
        'SweatshirtHipster_RedSelect.png',
        3, positions['POS_2'], 2)

    constants = pygame.sprite.LayeredDirty((bouncer, hand))
    all_patrons = pygame.sprite.LayeredDirty(whitey, pos5, pos6, pos7, pos1)

    all_sprites = pygame.sprite.LayeredDirty(constants, all_patrons)
    all_sprites.clear(screen, background)

    #
    #   Game Loop
    #

    def pointed_to(patron, hand):
        if patron.position == hand.position:
            return True
        else:
            return False

    running = True
    while running:
        clock.tick(60)

        # Events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_LEFT:
                    hand.move_left()

                if event.key == K_RIGHT:
                    hand.move_right()

                if event.key == K_RETURN:

                    for patron in all_patrons:
                        if pointed_to(patron, hand):

                            # we hit enter on the one that was chosen already.
                            if patron.chosen and hand.person_chosen:

                                patron.chosen = False
                                hand.person_chosen = False
                                bouncer.stop_pointing()
                                break

                            # noone is selected. Mark them.
                            elif not patron.chosen and not hand.person_chosen:

                                bouncer.start_pointing()
                                patron.chosen = True
                                hand.person_chosen = True
                                break

                            # the first person has been chosen. this is a second person who isn't chosen.
                            elif not patron.chosen and hand.person_chosen:

                                for p in all_patrons:
                                    if p.chosen:
                                        patron.switch_with(p)
                                        p.chosen = False

                                hand.person_chosen = False
                                patron.chosen = False
                                bouncer.stop_pointing()
                                break

        # highlight the person the hand is pointing to.
        for patron in all_patrons:
            if pointed_to(patron, hand) and not patron.selected:
                if not hand.person_chosen:
                    patron.highlight_green()
                else:
                    patron.highlight_red()
            elif not pointed_to(patron, hand) and not patron.chosen:
                    patron.end_selection()

        if bouncer.pointing and not bouncer.point.stopped:
            screen.blit(bouncer.point.next(), (0, 400))

        if bouncer.unpointing and not bouncer.point.stopped:
            screen.blit(bouncer.point.prev(), (0, 400))

        all_sprites.update()

        rects = all_sprites.draw(screen)
        pygame.display.update(rects)

    # game over
    pygame.quit()

# Start the script
if __name__ == '__main__':
    main()
