from source.values import width, height, duration
from source.utils import result_matrix
from pygame import PixelArray
from time import time


class Dict:
    def __init__(self):
        self.__pixels = {}

    def set_pixels(self, color: int):
        start = time()
        quantity = 0
        while start + duration > time():
            quantity += 1
            for x in range(width):
                for y in range(height):
                    self.__pixels[y * width + x] = color
        elapsed = (time() - start) * 1000.0 / float(quantity)
        result_matrix("dict set_pixels", quantity, elapsed)

    def get_pixels(self):
        return self.__pixels

    def from_matrix(self, matrix: list):
        start = time()
        quantity = 0
        while start + duration > time():
            quantity += 1
            for x in range(width):
                for y in range(height):
                    self.__pixels[y * width + x] = matrix[x][y]
        elapsed = (time() - start) * 1000.0 / float(quantity)
        result_matrix("dict from_matrix", quantity, elapsed)

    def from_pixelarray(self, matrix: PixelArray):
        start = time()
        quantity = 0
        while start + duration > time():
            quantity += 1
            for x in range(width):
                for y in range(height):
                    self.__pixels[y * width + x] = matrix[x][y]
        elapsed = (time() - start) * 1000.0 / float(quantity)
        result_matrix("dict from_pixelarray", quantity, elapsed)
