# Salom yaxshi insonlar

Ushbu loyihada men o'yin yaratish uchun eng yaxshi piksellarni boshqarish imkonini beruvchi texnologiyani aniqlashga harakat qilib ko'raman. Shuningdek, test natijalarini siz bilan baham ko'raman.

Test natijalari har xil qurilmalarda har xil chiqadi, shuning uchun sizga qiziq bo'lsa, siz ham sinov o'tkazib ko'ring va natijasini men bilan baham ko'rishingizni xohlayman. Albatta, siz yuborgan natijalarni ushbu github omborimga joylashtiraman, chunki bizga aniq natija kerak.

<!--
## Sinov maqsadi

Sinov maqsadi o'yin yaratishda grafikalar bo'yicha qaysi biri tezkorroq ekanligini aniqlash, fps qiymatini normal holatda saqlab turish va barcha sinov natijalariga qarab dasturchilar qaysi birini tanlashi kerakligini aniqlashga yordam berishdan iborat. Buning uchun pythonda ham Androidda ham shu sinovni amalga oshiraman. Bu loyiha python uchun, [Android loyihalari uchun ustiga bosing](https://github.com/khalilovibrohimuz/GraphTestForAndroid). Agar sinov muvaffaqiyatli deb baholansa, u orqali bir nechta namunaviy loyihalar chiqaraman (balki, alohida loyiha yaratishim ham mumkin, shunday qilsam havola qoldriaman).

## Test natijalari

Test natijalari bilan quyidagi manzil orqali tanishishingiz mumkin:

- [Barcha test natijalari](https://github.com/khalilovibrohimuz/GraphTestForPython/tree/master/tests)
- [Eng yaxshi test natijasi](https://github.com/khalilovibrohimuz/GraphTestForPython/blob/master/tests/4ndTest.md)

## Maslahatlar

O'yin yaratishda displeyni tezroq boshqarish va optimizatsiya qilish uchun quyidagi maslahatlarni beraman:

- Piksellari o'zgarmaydigan joylar uchun qiymatlarni o'zgartirishdan qoching.
- Tezlikni oshirish uchun displey o'lchamini kichraytirish ham foydali bo'lishi mumkin.
- Barcha o'zgarmaydigan layerlarni o'yin boshlanishidan oldin yaratib oling.
- Loyihangiz uchun AssetManager klassini yaratib olishingiz mumkin, hamma rasmlarni o'sha yerni o'zida yaratib unga ishlov bersangi bo'ladi.
- Piksellarni ko'proq boshqarishga to'g'ri kelsa MatrixArray2D klassiga o'xshash klassdan foydalanishni maslaxat beraman.
- Piksellar kam o'zgarishiga to'g'ri keladigan bo'lsa PyGame'ni o'zida ishni amalga oshiring.
- for yoki while tsikllariga murojaat qilganingizda e'tiborli bo'ling, uni ichida obyekt qayta qayta yaratilishiga yo'l qo'ymang.

## Keyingi qadamlar

Sizga algoritmingizni optimallashtirish haqida ko'p gapirdim, ammo bu siz uchun tushunarsiz bo'layotgani tabiiy hol, shuning uchun amalda sizga buni qanday qilish kerakligini ko'rsatib berishga harakat qilaman. O'yin yaratishda bizga grafikani o'zi yetarli emas, shunday ekan, piksellarni samarali boshqarish texnologiyasini (piksellar o'zgarmaydigan qismi uchun o'zgarish amalga oshirmaslik), ekran yangilanish tezligi(FPS)ni normal ishlab turish va undan foydalanib dastur yaratish borasida bir nechta misollar yarataman. Siz esa men keltirgan misollarni o'rganib chiqib buni qanday amalga oshirishni tushunib olishingiz mumkin ;)
-->

---

*Boshlang'ich ma'lumotlar yozildi*

---

## Hali loyiha nihoyasiga yetmagan

Hali loyiha nihoyasiga yetmagan va men bilmagan piksellarni manipulatsiya qilish usullari bor ekan, men ularni ham sinab ko'rishim kerak, shunday keyin loyiha nihoyasiga yetgan hisoblanadi, nihoyasiga yetsa o'zim e'lon qilaman

Bundan tashqari CV2 kutubxonasi ham bor ekan, eng qizig'i u ham rasmni ekranga chiqarish imkoniyatiga ega va pygame bilan raqobatchi bo'lishi mumkin
[Manipulate pixel with CV2 library](https://www.tutorialspoint.com/how-to-access-and-modify-pixel-value-in-an-image-using-opencv-python)
