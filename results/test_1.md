# `1 - test natijasi: 👨‍🔬`

```
################################################################################################################
###                                Start test for 1920x1080 size and 10 times                                ###
################################################################################################################

PyGame pixels: Hamma pikselni o'zgartirish uchun ketadigan o'rtacha vaqt -		 303685.6174468994 mikrosekund
PyGame pixels: Har bir pikselni o'zgartirish uchun ketadigan o'rtacha vaqt -		 0.14645332631505567078 mikrosekund
PyGame pixels: Erishish mumkin bo'lgan ekran yangilanish tezligi -			 3.2928790253784532 FPS
PyGame pixels: Biz kutgan natijadan nechchi marta tez -					 0.05462491157619809 marta
PyGame pixels: Biz kutgan natijadan nechchi marta sekin -				 18.30666578938196 marta
Yuqoridagi qiymatlar displeyni yangilash uchun ketadigan vaqtni hisobga olmaydi!

TkinterTest pixels: Hamma pikselni o'zgartirish uchun ketadigan o'rtacha vaqt -		 6448836.803436279 mikrosekund
TkinterTest pixels: Har bir pikselni o'zgartirish uchun ketadigan o'rtacha vaqt -	 3.10997145227444038440 mikrosekund
TkinterTest pixels: Erishish mumkin bo'lgan ekran yangilanish tezligi -			 0.15506672450869705 FPS
TkinterTest pixels: Biz kutgan natijadan nechchi marta tez -				 0.0025723708795298734 marta
TkinterTest pixels: Biz kutgan natijadan nechchi marta sekin -				 388.74643153430503 marta
TKinter eng sekin ishlovchi bo'lgani uchun faqat 1 marta sinovdan o'tkaziladi!

PILTest pixels: Hamma pikselni o'zgartirish uchun ketadigan o'rtacha vaqt -		 162671.3752746582 mikrosekund
PILTest pixels: Har bir pikselni o'zgartirish uchun ketadigan o'rtacha vaqt -		 0.07844877279834983064 mikrosekund
PILTest pixels: Erishish mumkin bo'lgan ekran yangilanish tezligi -			 6.147363039819245 FPS
PILTest pixels: Biz kutgan natijadan nechchi marta tez -				 0.10197737599495349 marta
PILTest pixels: Biz kutgan natijadan nechchi marta sekin -				 9.80609659979373 marta
Yuqoridagi qiymatlar displeyni yangilash uchun ketadigan vaqtni hisobga olmaydi!

MatrixArray1D pixels: Hamma pikselni o'zgartirish uchun ketadigan o'rtacha vaqt -	 103790.14015197754 mikrosekund
MatrixArray1D pixels: Har bir pikselni o'zgartirish uchun ketadigan o'rtacha vaqt -	 0.05005311542822991205 mikrosekund
MatrixArray1D pixels: Erishish mumkin bo'lgan ekran yangilanish tezligi -		 9.634826569611745 FPS
MatrixArray1D pixels: Biz kutgan natijadan nechchi marta tez -				 0.1598302109979753 marta
MatrixArray1D pixels: Biz kutgan natijadan nechchi marta sekin -			 6.2566394285287386 marta
Yuqoridagi qiymatlar displeyni yangilash uchun ketadigan vaqtni hisobga olmaydi!

MatrixArray2D pixels: Hamma pikselni o'zgartirish uchun ketadigan o'rtacha vaqt -	 53675.222396850586 mikrosekund
MatrixArray2D pixels: Har bir pikselni o'zgartirish uchun ketadigan o'rtacha vaqt -	 0.02588504166514785099 mikrosekund
MatrixArray2D pixels: Erishish mumkin bo'lgan ekran yangilanish tezligi -		 18.63057022114314 FPS
MatrixArray2D pixels: Biz kutgan natijadan nechchi marta tez -				 0.30905880328449936 marta
MatrixArray2D pixels: Biz kutgan natijadan nechchi marta sekin -			 3.235630208143481 marta
Yuqoridagi qiymatlar displeyni yangilash uchun ketadigan vaqtni hisobga olmaydi!

Ko'rib turganingizdek displeyni eng tez yangilovchi kutubxona PyGame
Shuningdek piksellarni eng tez o'zgartirish usuli 2 o'lchamli massiv yaratish
Piksellarni tez o'zgartirgan bilan uni ekranda tasvirlash uchun yordamchi kutubxona kerak (PyGame)
Shuning uchun MatrixArray2D ni PyGame ga convert qilish uchun qancha vaqt ketishini hisoblaymiz ;)
MatrixArray2D'ni PyGame'ga o'tkazishga ketgan vaqt -					 336312.3416900635 mikrosekund
Ushbu holat uchun erishish mumkinn bo'lgan ekran yangilanish tezligi -			 2.9734264135973145 mikrosekund

Sinov muvafaqqiyatli amalga oshirildi!
Xulosa:
Siz yaratayotgan o'yinning ishlash tezligi siz tanlagan kutubxonadan ko'ra siz tuzgan algoritmga bog'liq bo'ladi
O'yin yaratish uchun displeyni eng tez boshqaruvchi kutubxona PyGame hisoblanadi, yozgan kodlaringizni optimallashtirish orqali uni tezligini oshirishingiz mumkin
Katta 2 o'lchamli matritsani boshqarish kompyuter uchun qiyin topshiriq
Protsessor o'rtacha tezligi 3 MHz, ya'ni bir sekundda 3,000,000 ta amal
1920x1080 o'lchamdagi piksellar soni - 2,073,600, demak 1 sekund ichida hamma piksellarni qiymatini o'zgartirish mumkin
Lekin 60 FPS uchun 16 millisekund ichida 2,073,600 ta qiymatni o'zgartirish kerak bo'ladi, protsessor bunday qila olmaydi :(
Shuning uchun PyGame uchun hamma piksellarni o'zgartirish 1 sekund uchun 3.2075299656845684 marta amalga oshiriladi
Tavfsiyalar:
 - piksellari o'zgarmaydigan joylar uchun qiymatlarni o'zgartirishdan qoching
 - tezlikni oshirish uchun displey o'lchamini kichraytirish ham foydali bo'lishi mumkin
 - barcha o'zgarmaydigan layerlarni o'yin boshlanishidan oldin yaratib oling
Batafsil README.md faylini ichidan topasiz ;)
```

### `Sinov o'tkazilgan qurilma xususiyatlari: 💻`

```
• Modeli         - Asus VivoBook Pro 15 OLED 
• CPU            - i5
• RAM            - 8GB
• ROM            - 256GB
• Videokartasi   - Intel Iris Xe Graphics (2GB)
```
