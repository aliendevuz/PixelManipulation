from source.values import width, height, duration


def print_info():
    space = " " * 20
    info = f"###{space}{width}x{height} va {duration} sekund qiymatlari bo'yicha sinov boshlandi...{space}###"
    size = len(info)
    print("", "#" * size, info, "#" * size, sep="\n")


def result_matrix(name: str, quantity: int, elapsed: float):
    print(f"\n{name}:")
    print(f"\tTestlar soni{chr(9) * 5}- {quantity}")
    print(f"\tManipulatisya qilishga ketgan vaqt{chr(9) * 2}- {elapsed:.2f} ms")
    print(f"\tHar bir piksel uchun ketgan vaqt{chr(9) * 2}- {elapsed / float(width * height) * 1000.0:.6f} us")
    print(f"\tErishish mumkin bo'lgan FPS{chr(9) * 3}- {1000.0 / elapsed:.2f} Hz" if elapsed != 0.0
          else f"\tErishish mumkin bo'lgan FPS{chr(9) * 4}- Infinity! Hz")
    print(f"\tKutilganidan necha marta tez{chr(9) * 3}- {0.0 if 15.0 / elapsed < 1.0 else 15.0 / elapsed:.2f} marta" if elapsed != 0.0
          else f"\tKutilganidan necha marta tez{chr(9) * 3}- Infinity! marta")
    print(f"\tKutilganidan necha marta sekin{chr(9) * 3}- {0.0 if elapsed / 15.0 < 1.0 else elapsed / 15.0:.2f} marta")


def success():
    print("\nSinov muvafaqqiyatli yakunlandi!")


def rgb(r: int, g: int, b: int) -> int:
    return r << 16 | g << 8 | b << 0
