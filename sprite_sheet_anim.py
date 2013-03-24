import spritesheet


class SpriteStripAnim(object):
    """
        This class creates a spritesheet.

        iter() and iter_back() prepare for animating a sequence.

        next() and prev() return the next or previous image in the sequence
    """
    def __init__(self, filename, rect, count,
                 colorkey=None, loop=False, frames=1):
        """construct a SpriteStripAnim

        filename, rect, count, and colorkey are the same arguments used
        by spritesheet.load_strip.

        loop is a boolean that, when True, causes the next() method to
        loop. If False, the terminal case raises StopIteration.

        frames is the number of ticks to return the same image before
        the iterator advances to the next image.
        """
        self.filename = filename
        ss = spritesheet.spritesheet(filename)
        self.images = ss.load_strip(rect, count, colorkey)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames
        self.stopped = False
        self.count = count

    def iter(self):
        self.i = 0
        self.f = self.frames
        self.stopped = False
        return self

    def next(self):
        if self.i >= len(self.images):
            if not self.loop:
                self.stopped = True
                return self.images[self.i - 1]
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image

    def iter_back(self):
        self.i = self.count - 1
        self.f = self.frames
        self.stopped = False

    def prev(self):
        if self.i < 0:
            self.stopped = True
            return self.images[0]
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i -= 1
            self.f = self.frames
        return image

    def __add__(self, ss):
        self.images.extend(ss.images)
        return self
