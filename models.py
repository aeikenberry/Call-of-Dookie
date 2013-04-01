"""
    Models, characters, objects for Call of Dookie
"""

import pygame
from helpers import load_image2
from sprite_sheet_anim import SpriteStripAnim


class Bouncer(pygame.sprite.DirtySprite):
    """Our star. stands, points, knocks, hits on women."""
    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = load_image2('Bouncer_Sharper.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(0, 400)
        self.surly = 0
        self.point = SpriteStripAnim(
            'BouncerPointerSprite.png', (0, 0, 216, 300), 5, 1, False, 3)
        self.pointing = False
        self.unpointing = False
        # some more initial state stuff here

    def start_pointing(self):
        "move his arm up towards the line authoritatively"
        self.pointing = True
        self.unpointing = False
        self.point.iter()
        self.point.next()

    def stop_pointing(self):
        self.pointing = False
        self.unpointing = True
        self.point.iter_back()
        self.point.prev()

    def drink(self):
        "drink something, get the reward"
        # more to come here
        pass

    def knock_on_door(self):
        pass

    def get_phone_number(self):
        pass

    def update_surly_level(self, incriment):
        pass

    def walk_to(self, coords):
        pass

    def update(self):
        "This is what will run all the time"
        # only put stuff here if it needs to update


class LinePerson(pygame.sprite.DirtySprite):
    """Base class for people standing in line."""
    def __init__(self, image, green, red, speed, coords, pos_number):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = load_image2(image)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(coords)
        self.position = pos_number
        self.selected = False
        self.chosen = False
        self.original_state = image
        self.green = green
        self.red = red

    def walk_into_line(self):
        pass

    def highlight_green(self):
        self.image = load_image2(self.green)
        self.selected = True
        self.dirty = 1

    def highlight_red(self):
        self.image = load_image2(self.red)
        self.selected = True
        self.dirty = 1

    def end_selection(self):
        self.image = load_image2(self.original_state)
        self.selected = False
        self.dirty = 1

    def switch_with(self, patron):
        #position_1, position_2 = 0, 0
        if self.position > patron.position:
            position_1, position_2 = self.position, patron.position
        else:
            position_1, position_2 = patron.position, self.position

        moving = 0

        if position_1 - position_2 == 1:
            moving += 100
        if position_1 - position_2 == 2:
            moving += 200
        if position_1 - position_2 == 3:
            moving += 300
        if position_1 - position_2 == 4:
            moving += 400
        if position_1 - position_2 == 5:
            moving += 500
        if position_1 - position_2 == 6:
            moving += 600

        self.position, patron.position = patron.position, self.position

        if self.position > patron.position:
            self.rect.move_ip(moving, 0)
            patron.rect.move_ip(-moving, 0)
        else:
            self.rect.move_ip(-moving, 0)
            patron.rect.move_ip(moving, 0)

        self.chosen = False
        patron.chosen = False

        self.dirty = 1
        patron.dirty = 1

    def shift_left_one(self):
        self.rect.move_ip(-100, 0)
        self.position -= 1
        self.dirty = 1

    def walk_out(self):
        pass

    def enter_bathroom(self):
        pass

    def keel_over(self):
        pass

    def piss_pants(self):
        pass

    def pee_in_line(self):
        pass

    def look_pissed(self):
        pass

    def vomit(self):
        pass

    def vanish(self):
        self.rect.move_ip(-600, 0)
        self.position = -1
        self.dirty = 1

class PointerHand(pygame.sprite.DirtySprite):
    "Severed Hand"
    def __init__(self, coords):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = load_image2('PointerHand.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(coords)
        self.position = 4
        self.person_chosen = False

    def move_left(self):
        if self.position > 1:
            self.rect.move_ip(-100, 0)
            self.dirty = 1
            self.position -= 1

    def move_right(self):
        if self.position < 7:
            self.rect.move_ip(100, 0)
            self.dirty = 1
            self.position += 1
