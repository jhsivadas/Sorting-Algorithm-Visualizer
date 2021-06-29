import pygame
import math

"""
This class controls the slider location that determines the size of the list being sorted. 
Also has function to determine if the current mouse position is over the slider.
"""
class Slider:

    def __init__(self, x, y, original_x):
        self.x = x
        self.y = y
        self.original_x = original_x

    def return_num(self):
        trans = int((self.x - self.original_x) / 2)
        return trans

    def hovering(self):
        pos = pygame.mouse.get_pos()
        if math.sqrt(pow((pos[0] - self.x), 2) + pow((pos[1] - self.y), 2)) < 10:
            return True
        return False