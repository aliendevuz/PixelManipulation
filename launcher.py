from source.utils import print_info, success, rgb
from source.pixelarray import PixelArray
from source.matrix import Matrix
from source.dict import Dict


matrix_dict = Dict()
matrix_matrix = Matrix()
matrix_pixelarray = PixelArray()


if __name__ == '__main__':
    print_info()
    print("\nset_pixels funksiyalari sinovdan o'tkazilmoqda...")
    matrix_dict.set_pixels(rgb(0, 128, 255))
    matrix_matrix.set_pixels(rgb(128, 0, 255))
    matrix_pixelarray.set_pixels(rgb(128, 192, 255))
    print("\nkonvertatsiya funksiyalari sinovdan o'tkazilayapti...")
    matrix_dict.from_matrix(matrix_matrix.get_pixels())
    matrix_dict.from_pixelarray(matrix_pixelarray.get_pixels())
    matrix_matrix.from_dict(matrix_dict.get_pixels())
    matrix_matrix.from_pixelarray(matrix_pixelarray.get_pixels())
    matrix_pixelarray.from_dict(matrix_dict.get_pixels())
    matrix_pixelarray.from_matrix(matrix_matrix.get_pixels())
    success()
