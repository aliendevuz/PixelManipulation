from time import time as current_time
from utils import *
import pygame


class PyGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN | pygame.SCALED)

    def create_task(self, px):
        for x in range(self.width):
            for y in range(self.height):
                px[x][y] = 16777215

    def test(self, test_quantity):
        pygame.init()
        px = pygame.PixelArray(self.matrix)
        time = float(current_time())
        for i in range(test_quantity):
            self.create_task(px)
        result_for_pixels = (float(current_time()) - time) / float(test_quantity) * 1_000_000.0
        result_for_pixel = result_for_pixels / float(self.width * self.height)
        del px
        print_matrix_result(test_quantity, PyGame.__name__, result_for_pixels, result_for_pixel)
