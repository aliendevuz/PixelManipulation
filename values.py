from pygame import display, init


init()


class Const:
    size = display.get_desktop_sizes()[0]
    width = size[0]
    height = size[1]
    test_quantity = 10
