from source.values import width, height, duration
from source.utils import result_matrix
from pygame import PixelArray
from time import time


class Matrix:
    def __init__(self):
        self.__pixels = [[0 for _ in range(height)] for _ in range(width)]

    def set_pixels(self, color: int):
        start = time()
        quantity = 0
        while start + duration > time():
            quantity += 1
            for x in range(width):
                for y in range(height):
                    self.__pixels[x][y] = color
        elapsed = (time() - start) * 1000.0 / float(quantity)
        result_matrix("matrix set_pixels", quantity, elapsed)

    def get_pixels(self):
        return self.__pixels

    def from_dict(self, matrix: dict):
        start = time()
        quantity = 0
        while start + duration > time():
            quantity += 1
            for point, color in matrix.items():
                self.__pixels[point % width][point // width] = color
        elapsed = (time() - start) * 1000.0 / float(quantity)
        result_matrix("matrix from_dict", quantity, elapsed)

    def from_pixelarray(self, matrix: PixelArray):
        start = time()
        quantity = 0
        while start + duration > time():
            quantity += 1
            for x in range(width):
                for y in range(height):
                    self.__pixels[x][y] = matrix[x][y]
        elapsed = (time() - start) * 1000.0 / float(quantity)
        result_matrix("matrix from_pixelarray", quantity, elapsed)
