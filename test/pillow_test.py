from time import time as current_time
from PIL import Image
from utils import *


class PILTest:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (self.width, self.height), "black")

    def create_task(self):
        pixels = self.image.load()
        for x in range(self.width):
            for y in range(self.height):
                pixels[x, y] = (255, 255, 255)

    def test(self, test_quantity):
        time = float(current_time())
        for i in range(test_quantity):
            self.create_task()
        result_for_pixels = (float(current_time()) - time) / float(test_quantity) * 1_000_000.0
        result_for_pixel = result_for_pixels / float(self.width * self.height)
        print_matrix_result(test_quantity, PILTest.__name__, result_for_pixels, result_for_pixel)
