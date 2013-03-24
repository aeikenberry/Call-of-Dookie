import os
import pygame
from pygame.compat import geterror

working_dir = os.path.split(os.path.abspath(__file__))[0]
images_dir = os.path.join(working_dir, 'img')
audio_dir = os.path.join(working_dir, 'audio')


def load_image2(file_name, colorkey=False, image_directory='img'):
    'Loads an image, file_name, from image_directory, for use in pygame'
    file = os.path.join(image_directory, file_name)
    _image = pygame.image.load(file)
    if colorkey:
        if colorkey == -1:
        # If the color key is -1, set it to color of upper left corner
            colorkey = _image.get_at((0, 0))
        _image.set_colorkey(colorkey)
        _image = _image.convert()
    else:  # If there is no colorkey, preserve the image's alpha per pixel.
        _image = _image.convert_alpha()
    return _image


def load_sound(name):
    class NoneSound:
        def play(self):
            pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(audio_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('Cannot load sound: %s' % fullname)
        raise SystemExit(str(geterror()))
    return sound
