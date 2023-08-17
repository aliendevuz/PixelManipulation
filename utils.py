from values import Const


def print_test_information():
    print()
    info = f"###                                Start test for {Const.width}x{Const.height} size and {Const.test_quantity} times                                ###"
    print("#" * len(info))
    print(info)
    print("#" * len(info))


def print_matrix_result(test_quantity, class_name, result_for_pixels, result_for_pixel):
    print()
    tab_count = 3 - len(class_name) // 4
    print(class_name, "pixels: Hamma pikselni o'zgartirish uchun ketadigan o'rtacha vaqt -" + "\t" * (tab_count),
          result_for_pixels, "mikrosekund")
    print(
        f"{class_name} pixels: Har bir pikselni o'zgartirish uchun ketadigan o'rtacha vaqt -{chr(9) * (tab_count + 1 - int(len(class_name) % 4 >= 2))} {result_for_pixel:.20f} mikrosekund")
    print(class_name, "pixels: Erishish mumkin bo'lgan ekran yangilanish tezligi -" + "\t" * (tab_count + 1),
          1_000_000 / result_for_pixels, "FPS")
    print(
        f"{class_name} pixels: Biz kutgan natijadan nechchi marta tez -{chr(9) * (tab_count + 3 - int(len(class_name) % 4 > 2))} {0.008 / result_for_pixel} marta")
    print(class_name, "pixels: Biz kutgan natijadan nechchi marta sekin -" + "\t" * (tab_count + 2),
          result_for_pixel / 0.008, "marta")
    print("Yuqoridagi qiymatlar displeyni yangilash uchun ketadigan vaqtni hisobga olmaydi!" if test_quantity != 0
          else "TKinter eng sekin ishlovchi bo'lgani uchun faqat 1 marta sinovdan o'tkaziladi!")


def print_convert_result(result):
    print()
    print("Ko'rib turganingizdek displeyni eng tez yangilovchi kutubxona PyGame")
    print("Shuningdek piksellarni eng tez o'zgartirish usuli 2 o'lchamli massiv yaratish")
    print("Piksellarni tez o'zgartirgan bilan uni ekranda tasvirlash uchun yordamchi kutubxona kerak (PyGame)")
    print("Shuning uchun MatrixArray2D ni PyGame ga convert qilish uchun qancha vaqt ketishini hisoblaymiz ;)")
    print("MatrixArray2D'ni PyGame'ga o'tkazishga ketgan vaqt -" + chr(9) * 5, result, "mikrosekund")
    print("Ushbu holat uchun erishish mumkinn bo'lgan ekran yangilanish tezligi -" + chr(9) * 3, 1_000_000 / result,
          "mikrosekund")


def print_result():
    print()
    print("Sinov muvafaqqiyatli amalga oshirildi!")
    print("Xulosa:")
    print(
        "Siz yaratayotgan o'yinning ishlash tezligi siz tanlagan kutubxonadan ko'ra siz tuzgan algoritmga bog'liq bo'ladi")
    print(
        "O'yin yaratish uchun displeyni eng tez boshqaruvchi kutubxona PyGame hisoblanadi, yozgan kodlaringizni optimallashtirish orqali uni tezligini oshirishingiz mumkin")
    print("Katta 2 o'lchamli matritsani boshqarish kompyuter uchun qiyin topshiriq")
    print("Protsessor o'rtacha tezligi 3 MHz, ya'ni bir sekundda 3,000,000 ta amal")
    print(
        "1920x1080 o'lchamdagi piksellar soni - 2,073,600, demak 1 sekund ichida hamma piksellarni qiymatini o'zgartirish mumkin")
    print(
        "Lekin 60 FPS uchun 16 millisekund ichida 2,073,600 ta qiymatni o'zgartirish kerak bo'ladi, protsessor bunday qila olmaydi :(")
    print(
        "Shuning uchun PyGame uchun hamma piksellarni o'zgartirish 1 sekund uchun 3.2075299656845684 marta amalga oshiriladi")
    print("Tavfsiyalar:")
    print(" - piksellari o'zgarmaydigan joylar uchun qiymatlarni o'zgartirishdan qoching")
    print(" - tezlikni oshirish uchun displey o'lchamini kichraytirish ham foydali bo'lishi mumkin")
    print(" - barcha o'zgarmaydigan layerlarni o'yin boshlanishidan oldin yaratib oling")
    print("Batafsil README.md faylini ichidan topasiz ;)")
