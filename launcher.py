from test.base import Base
from values import Const
from utils import *


if __name__ == '__main__':
    print_test_information()
    Base(Const.width, Const.height, Const.test_quantity).test()
    print_result()
