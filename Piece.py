import pygame
import sys
from pygame.locals import *
from random import randint
import copy
from constants import *
import math

colorback = (189, 174, 158)
colorblank = (205, 193, 180)
colorlight = (249, 246, 242)
colordark = (119, 110, 101)

fontSize = [100, 85, 70, 55, 40]

dictcolor1 = {
    0: colorblank,
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 95, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    4096: (237, 190, 30),
    8192: (239, 180, 25)}

dictcolor2 = {
    2: colordark,
    4: colordark,
    8: colorlight,
    16: colorlight,
    32: colorlight,
    64: colorlight,
    128: colorlight,
    256: colorlight,
    512: colorlight,
    1024: colorlight,
    2048: colorlight,
    4096: colorlight,
    8192: colorlight}

class Piece:
    def __init__(self, value):
        self.value = value
        self.color = ''

    def generateLabel(self):
        # search for zero in the game table and randomly fill the places
        order = int(math.log10(self.value))
        myfont = pygame.font.SysFont(
            "Arial", fontSize[order], bold=True)
        label = myfont.render(
            "%4s" % (self.value), 1, dictcolor2[self.value])
        return label

    def generateColor(self):
        # search for zero in the game table and randomly fill the places
        return dictcolor1[self.value]
