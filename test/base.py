from test.matrix_array_1d_test import MatrixArray1D
from test.matrix_array_2d_test import MatrixArray2D
from test.tkinter_test import TkinterTest
from time import time as current_time
from test.pillow_test import PILTest
from test.pygame_test import PyGame
from pygame import PixelArray, quit
from utils import *


class Base:
    def __init__(self, width, height, test_quantity):
        self.test_quantity = test_quantity
        self.width = width
        self.height = height
        self.pygame = PyGame(width, height)
        self.tkinter = TkinterTest(width, height)
        self.pil = PILTest(width, height)
        self.matrix_array_1d = MatrixArray1D(width, height)
        self.matrix_array_2d = MatrixArray2D(width, height)

    def test_matrix(self):
        self.pygame.test(self.test_quantity)
        self.tkinter.test()
        self.pil.test(self.test_quantity)
        self.matrix_array_1d.test(self.test_quantity)
        self.matrix_array_2d.test(self.test_quantity)

    def test_convert(self):
        pixels = PixelArray(self.pygame.matrix)
        time = float(current_time())
        for i in range(self.test_quantity):
            for x in range(self.width):
                for y in range(self.height):
                    pixels[x][y] = self.matrix_array_2d.matrix[x][y]
        result = (float(current_time()) - time) / float(self.test_quantity) * 1_000_000.0
        del pixels
        quit()
        print_convert_result(result)

    def test(self):
        self.test_matrix()
        self.test_convert()
