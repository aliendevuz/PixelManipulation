from time import time as current_time
from utils import *


class MatrixArray1D:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [0 for _ in range(width * height)]

    def create_task(self):
        for x in range(self.width):
            for y in range(self.height):
                self.matrix[y * self.width + x] = 16777215

    def test(self, test_quantity):
        time = float(current_time())
        for i in range(test_quantity):
            self.create_task()
        result_for_pixels = (float(current_time()) - time) / float(test_quantity) * 1_000_000.0
        result_for_pixel = result_for_pixels / float(self.width * self.height)
        print_matrix_result(test_quantity, MatrixArray1D.__name__, result_for_pixels, result_for_pixel)
