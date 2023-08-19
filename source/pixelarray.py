from pygame import display, pixelarray, FULLSCREEN, SCALED
from source.values import width, height, duration
from source.utils import result_matrix
from time import time


class PixelArray:
    def __init__(self):
        self.__surface = display.set_mode((width, height), FULLSCREEN | SCALED)
        self.__pixels = None

    def set_pixels(self, color: int):
        start = time()
        quantity = 0
        while start + duration > time():
            quantity += 1
            self.__pixels = pixelarray.PixelArray(self.__surface)
            for x in range(width):
                for y in range(height):
                    self.__pixels[x][y] = color
            self.__pixels = None
            display.flip()
        elapsed = (time() - start) * 1000.0 / float(quantity)
        result_matrix("pixelarray set_pixels", quantity, elapsed)

    def get_pixels(self):
        self.__pixels = pixelarray.PixelArray(self.__surface)
        return self.__pixels

    def from_dict(self, matrix: dict):
        start = time()
        quantity = 0
        while start + duration > time():
            quantity += 1
            self.__pixels = pixelarray.PixelArray(self.__surface)
            for point, color in matrix.items():
                self.__pixels[point % width][point // width] = color
            self.__pixels = None
            display.flip()
        elapsed = (time() - start) * 1000.0 / float(quantity)
        result_matrix("pixelarray from_dict", quantity, elapsed)

    def from_matrix(self, matrix: list):
        start = time()
        quantity = 0
        while start + duration > time():
            quantity += 1
            self.__pixels = pixelarray.PixelArray(self.__surface)
            for x in range(width):
                for y in range(height):
                    self.__pixels[x][y] = matrix[x][y]
            self.__pixels = None
            display.flip()
        elapsed = (time() - start) * 1000.0 / float(quantity)
        result_matrix("pixelarray from_matrix", quantity, elapsed)
