# Pixel Manipulation

Assalomu aleykum!
Ushbu loyihada men `piksellarni yuqori tezlikda boshqarishni aniqlash` uchun tadqiqot o'tkazib, ulardan eng yaxshi usulni aniqlashga harakat qildim 🙂

###### *Maqola hali to'liq yozilmagan, hali yozishim kerak bo'lgan ayrim narsalar bor*

<!--
Shu yerda kiritilishi kerak bo'lgan narsalarni vaqtincha saqlab qo'yamiz
- Men hali qanday qilib displeydan samarali foydalanish va optimal kodlar yozish borasida tavfsiyalar kiritganim yo'q

-->

## Muammo nimada?

Men `python` tilida kod yozish orqali grafik dasturlar yaratishga qiziqaman, lekin displeyni boshqarish men o'ylagandan ham sekinroq jarayon ekan.
Men dasturlarimni yaxshi va tez ishlashini xohlardim, ammo, u juda sekin ishlardi (bu juda yoqimsiz holat).
Menda "Qayerda xato qilayapman?" degan savol paydo bo'ldi va men displeydagi har bir piksellarni eng tez boshqarish usulini aniqlashga qaror qildim.

Xullas kalom, bu loyiha `Piksellarni yuqori tezlikda boshqarishni usullarini aniqlash va o'zaro solishtirish` ga bag'ishlanadi.
Men sinov o'tkazib ko'rgan bo'lsamda 100% aniq natijaga erishganman deb ayta olmayman, balki men bilmagan narsalar bordir.
Agar sizda qandaydir tavfsiyalar va maslahatlar bo'lsa, iltimos menga ayting -> [Alien Developer](https://t.me/khalilov_ibrohim_uz)

## Test natijalari

Test natijalari qurilmalarni sifatiga qarab turlicha bo'lishi aniq. Siz ham o'zingizni qurilmangizda sinov o'tkazib ko'rishingiz mumkin. Istasangiz natijalarni menga yuboring [Alien Developer](https://t.me/khalilov_ibrohim_uz), menga ma'qul kelsa siz yuborgan natijalarni `PixelManipulation/results/` qatoriga qo'shib qo'yaman

Mening qurilmamni xusuiyati shunday:
- Modeli - Asus VivoBook Pro 15 OLED 
- CPU - i5
- RAM - 8GB
- ROM - 256GB
- Intel Iris Xe Graphics (2GB)

Ushbu qurilmada test natijalari quyidagicha:

- [Barcha test natijalari](https://github.com/aliendevuz/PixelManipulation/tree/master/results)
- [Eng yaxshi test natijasi](https://github.com/aliendevuz/PixelManipulation/blob/master/results/test_2.md)

Ha yana bir gap, birinchi test natijasi ikkinchisinikinidan tubdan farq qiladi. Bunga sabab birinchi testda foydalangan samarasiz usullardan voz kechganim va yangisida eng yaxshi usullardan foydalanganim.
Shuningdek men kodlarni qayta ko'rib chiqdim, ular xatosiz ishlashi uchun ko'plab testlar o'tkazdim va eng tartibli ko'rinishga keltirdim (kodlar `clean` deb kafolat berolmayman)

## Sinovda foydalangan usullar
- Dict - `python`ning `dict` tipidan foydalanib faqat piksellari o'zgargan qismini eslab qolish va oxirida `pixelarray` orqali displeyda tasvirlash
- Matrix - `python`ning `list of lists` (2D massiv) tipidan foydalanib piksellarni tezroq o'zgarishini ta'minlash va oxirida `pixelarray` orqali displeyga chiqarish
- PixelArray - `pygame`ning `pixelarray` dan foydalanib piksellarni boshqarish, unda piksellarni boshqarish eng sekini bo'lsada displeyda to'g'ridan to'g'ri tasvirlangani tufayli eng tezkor bo'ldi

`Konvert` (bir turdan boshqasiga o'tkazish) qilishga keladigan bo'lsak ularni har biri uchun `konvert` funksiyasini yaratganman

## Sinov natijalari yuqori aniqlikdami?

Sinov kodlarining sifati juda ham muhim, chunki biz unga ko'ra qarorlar qabul qilamiz.
Meni sinovni amalga oshirishda quyidagilarga e'tibor qaratganman:
- Men sinovni FHD (1920x1080) o'lchamda olib bordim.
- Qiymatlar aniq bo'lishi uchun har bir sinov 60 sekund (`values.duration`) ichida qayta qayta amalga oshirilgan
- Barcha sinov natijalari qo'shilib o'rtacha qiymati hisoblangan
- Hammasi tushunarli bo'lishi uchun sinov natijasini har xil formatlarda chiqardim (ms - millisekund, us - mikrosekund, Hz - chastota)
- Kutilgan natija sifatida FPS ni 60 Hz deb belgiladim (15.0 millisekund ichida vazifa bajarib bo'linsa biz kutgan natija bo'ladi, lekin afsuski biz kutgan natijaga erishmadik (eng tezi 3.10 Hz) ☹️)

Sinov natijalari yuqori aniqlikda bo'lishi uchun bor imkoniyatimni ishga solganman...

## Qanday foydalansa bo'ladi?

Loyihani ishlatish uchun pygame kutubxonasi kerak. Agar sizda bu kutubxona mavjud bo'lmasa, quyidagi buyruqni terminalda bajarishingiz mumkin:

```shell
pip install pygame
```

Sinovni boshlash uchun `launcher.py` ni ishga tushirishni o'zi yetarli

Sinovni sozlash uchun `values.py` faylidagi `width`, `height`, `duration` larni qiymatini o'zgartirish kifoya.
`duration` sekundlardagi qiymatlarni qabul qiladi, sizda u 10.0 deb belgilangan bo'lishi kerak, bu har bir sinov 10 sekund davom etishini anglatadi,
sinovlar soni 9 ta va 10 * 9 = 90 sekund ichida natijasi chiqadi, siz xohishingizga ko'ra uning qiymatini kamaytirishingiz yoki ko'paytirishingiz mumkin.
Qiymat qanchalik kichik bo'lsa sinov tez yakunlanadi va sifati pasayadi, qiymati katta bo'lsa sinov aniqligi ham yuqori bo'ladi (Menimcha 10.0 yaxshi qiymat).
Displey o'lchamlariga keladigan bo'lsak u avtomatik aniqlanadi, xohishingizga ko'ra qo'lda kiritsangiz bo'ladi (masalan 1280x720)

Sinov natijalari `console` da chiqadi (siz uni faylga yozadigan qilib sozlashingiz mumkin 😉), siz o'sha natijani menga yuborsangiz bo'ladi, faqat qurilmangizni xususiyatlarini ham qo'shish esingizdan chiqmasin! ex: i5, 8GB

## Xulosa

Afsuski FHD formatida 60 Hz ga barcha piksellarni boshqarishga uringan holda erishib bo'lmas ekan ☹️ (Displeyda o'zgarish bo'lmasa FPS yuqori bo'ladi).
- `Dict` usuli eng ahmoqona usul bo'lib chiqdi (undan foydalanishni umuman maslaxat bermagan bo'lardim)
- `Matrix` usuli displeyda tasvirlanishi biroz sekinroq kechar ekan, shuni hisobiga undan real time dasturlarda foydalanib bo'lmaydi, lekin piksellarni juda ko'p o'zgartirishga to'g'ri keladigan dastur bo'lsa, yoki, biror rasmni tahrirlovchi (displeyda ko'rsatilishi shart emas) dastur bo'lsa `Matrix` usuliga yetadigani yo'q, u juda tezkor
- `PixelArray` usuli esa displeyda tesvirlanishi bo'yicha eng tezkori bo'lib chiqdi va ko'p hollarda undan foydalanish mumkin

Xullas eng yaxshi usul `PixelArray` orqali piksellarni boshqarish ekan

---

*Hozircha hammasi shu, kelgusi ishlarda omad, e'tiboringiz uchun rahmat* 😊

---

# `Alien Developer 🖼️`

```
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                    ,WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW       ...........::::::..    .      WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW     ..............::::.........:...... ::..    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW               ..................:::......::....::...    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW     .::...........::...........::..::...:::......:.....:....      WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   .:::::...................:::........:.....::::......:.....::......      WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   ..:...........,;;;;::::.....:::,.::..............::....................:,  .   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   .:..........................;:........:...................... .............:.  :.   WWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  ....................::::::........................................  ............ ..:.  WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@  ....................::................................................  .............:   WWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  ............ ....,.........................................   ...........  ........ ..:   WWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  .........  ............................................     ...  ..........  ......  ...  WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWW   .......   .....  ..................::.......... ............    .   ........  ....   ..    WWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWW  .......   ...   .......... ......:..,...............   ....            .... .. ...    .      WWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWW  ......    .    ...........  ..................................              .                 WWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWW:  .. ..         ...........    . .... .........        ..........       @                       WWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWW    .            .. ...     @@    .. ....                        @@@@@@@@@@@@@@@@@@@@@@@@       WWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWW    .            . .   @@@@@@@@@    ..    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       WWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWW                     @@@@@@@@@@@@   .  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       WWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWW                     @@@@@@@@@@@@@@@   *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       WWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWW  @@@,,@@@@           @@@@@@@@@@@@@@... ............@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      WWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW.  @@@++++,,@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@@.......@@@@@@@@@@@@@@@........@@@@@@@@@@@@@      WWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW  @@@++++,++,          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..@@@@@@@@@@@.................@@@@@@@     WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW  @@@++,+    .          .  @@@@@@@@      @@@@+++@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...@@@@    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW  @@@+ .... ;,,@@@@@@        ,  @@  WWWWWWWW        @@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.@@   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWW   @@ ,,, +++,@@@@@@@@@     ......:   WWWWWW         W  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWW   @@@:+++++,@@@@@@@@@@@  .............           WW   @@@@@@@@@@,@@      @@@@++@@@@@@@@@@@  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWW  @@@@+;++,@@@@@@@@@@@@@@@@@@  ......:,WWW.............   @@@@,@ WWWWWWW   ;      ,@@@@@  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWW   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ,.... #############  ...... +@ WWWWW        WW  @   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWW    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ,..######@@@@@@@####@####  .....    WWWWW.  @@@@  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW.    @@@@@@@@@@@@@@@@@@@@@@@@ . +@@@@@@@@****@@@@@@@@@@@@@*.....,,,,,.....     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  @@@@@@@@@@@@@@@@@@@@@@@@@.  ***+++++++++***********@@@,.....,,,....  ;;     ....,,  :WWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  @@@@@@@@@@@@@@@@@@@@@@@@ .  ******+************@@@@@@ ... @@@ ... @@@@@************  ,,,:      WWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  @@@@@@@@@@@@@@@@@@@@@@@@@   ***************@@@@@@@@@    @@@@@@,. +++++++++++++++******* ,::::::    WWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   @@@@@@@@@@@@@@@@@@@@@@@@@    ****@***@**@@@@@@@**   .@@@@@@@@,  +++++++++++++***********,,:::  @@@   WWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  @@@@@@@@@@@@@@@@@@@@@@@@@@@      *******@@***     @@@@@@@@@@@   **+++++++++**********@@ ,, @@ @@ *@@@  WWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             @@@@@@@@@@@@@@@ . ****************@@@@@@@.. @@@@ @@@ @@@  WWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   @@@@@@@@@@@@@@@@@@@@        ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ .  **********@*@@@@@@*...  @@@@ @@@@ @@@. WWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   ;@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,       @@@@@@@@@@@@@@@@@@      ******@@@@@*@**;   @@:@@@@@@@    @@@  WWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   @@@@@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@@  @@@@@@@@@@@   WWWW         ::         @@@@@@@@@@@@@@@@@@  WWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  .*   @@@@@@@@@@@@@@@@@@@@@@@@@@**@@@@@@@@@@@@@@@@@@   WWWWWWWWWW  @@@@@@   WW  @@@@@@@@@@@@@@@@@@@@  WWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@           @@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   WWWWWWWWWWWWWWWW   @@@@@@@@@@@@@   @@@@@@@@@@@@@ .WWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWW      .:. ,,.    @@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    WWWWWWWWWWWWWWWWWWWWWW   @@@@@@@@@@@@@@ @@@@@@@@@@  WWWWW
WWWWWWWWWWWWW             :  :::  ..  @@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@    WWWWWWWWWWWWWWWWWWWWWWWWWWWWW  @@@@@@@@@@@@@@@@@@@@@@+ WWWWWW
WWWWWWWWW    ::::::::::::: ::::  ..  @@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@       WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW    @@@@@@@@@@@@@@@@  WWWWWWW
WWWWWWW   ::::::,:::::::: ::::: ....  @@@@@@@@@@@@@@@@@@@@@@@@@@@@             :::::,  :        WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW    ::::::::::::    WWWW
WWWWW   ::::::::,::::::: ,::::: .......    @@@@@@@@@@@@@@@@@@@@@@    ..... ::::::::,  ::::             WWWWWWWWWWWWWWWWWWWWWW   : :::,::::::::::   WWW
WWWWW  :::::::::,::::::  :::::: ...............              .........  ::::::::::  :::::,:::::::::::::    WWWWWWWWWWWWWWWWWW   :.::::::::::::::   WWW
WWWWW  :::::::::,:::::: ::::,::, ................................  :::::::::::,:  ::::,::::::::::::::::::::    WWWWWWWWWWWWWW  :::::::::::::::::   WWW
```

---
