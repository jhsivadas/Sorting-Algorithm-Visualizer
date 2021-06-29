import pygame

"""
This class creates a button. The button can be placed at any location, can be of any specified size 
(if valid in pygame input), and can contain any text.
The button class has function "hovering" to determine if the current mouse position is over the current. 
"""
class Button:

    def __init__(self, x, y, width, height, color, DSP, font, text=""):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.height = height
        self.width = width
        self.DSP = DSP
        self.font = font

    def draw_button(self):
        pygame.draw.rect(self.DSP, (0, 0, 0), pygame.Rect(self.x - 2, self.y - 2, self.width + 4, self.height + 4))
        pygame.draw.rect(self.DSP, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

        if self.text != "":
            overlay = self.font.render(self.text, True, (0, 0, 0))
            self.DSP.blit(overlay, (self.x + 12, self.y + 12))

    def hovering(self):
        pos = pygame.mouse.get_pos()
        if pos[0] >= self.x and pos[0] <= self.x + self.width:
            if pos[1] >= self.y and pos[1] <= self.y + self.height:
                return True
        return False