from time import time as current_time
import tkinter as tk
from utils import *


class TkinterTest:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

    def create_task(self):
        for x in range(self.width):
            for y in range(self.height):
                self.canvas.create_line(x, y, x + 1, y, fill="#0000ff")

    def test(self):
        time = float(current_time())
        self.create_task()
        result_for_pixels = (float(current_time()) - time) * 1_000_000.0
        result_for_pixel = result_for_pixels / float(self.width * self.height)
        print_matrix_result(0, TkinterTest.__name__, result_for_pixels, result_for_pixel)
