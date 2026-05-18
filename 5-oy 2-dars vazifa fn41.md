**Kino Platformasi — SQLAlchemy Practice Assignment**

Movie modeli yarating:  
 `id`, `title`, `genre`, `release_year`, `duration`, `rating`, `director` ustunlari bo‘lsin. SQLite bazaga bog‘lang va jadval yarating.

Quyidagi kinolarni bazaga qo‘shing:

* Interstellar, Sci-Fi, 2014, 169, 8.7, Christopher Nolan  
* Inception, Sci-Fi, 2010, 148, 8.8, Christopher Nolan  
* Titanic, Drama, 1997, 195, 7.9, James Cameron  
* Joker, Thriller, 2019, 122, 8.4, Todd Phillips  
* Avatar, Fantasy, 2009, 162, 7.8, James Cameron  
* The Batman, Action, 2022, 176, 7.9, Matt Reeves  
* Oppenheimer, Biography, 2023, 180, 8.6, Christopher Nolan  
* Parasite, Thriller, 2019, 132, 8.5, Bong Joon-ho  
* John Wick, Action, 2014, 101, 7.4, Chad Stahelski  
* Dune, Sci-Fi, 2021, 155, 8.0, Denis Villeneuve

---

**Topshiriqlar**

1. Barcha kinolarni chiqarib bering.  
2. Faqat `genre = "Sci-Fi"` bo‘lgan kinolarni chiqaring.  
3. `release_year > 2015` bo‘lgan kinolarni chiqaring.  
4. `rating >= 8.5` bo‘lgan kinolarni chiqaring.  
5. `duration > 150` bo‘lgan kinolarni chiqaring.  
6. Faqat `director = "Christopher Nolan"` bo‘lgan kinolarni chiqaring.  
7. `genre = "Action"` VA `rating > 7.5` bo‘lgan kinolarni chiqaring.  
8. `director = "James Cameron"` YOKI `director = "Christopher Nolan"` bo‘lgan kinolarni chiqaring.  
9. `genre IN ("Thriller", "Drama")` bo‘lgan kinolarni chiqaring.  
10. Nomida `"man"` so‘zi qatnashgan kinolarni chiqaring.  
11. Nomi `"r"` harfi bilan tugaydigan kinolarni chiqaring.  
12. Nomi `"The"` bilan boshlanadigan kinolarni chiqaring.  
13. `release_year BETWEEN 2010 AND 2020` bo‘lgan kinolarni chiqaring.  
14. Kinolarni `rating` bo‘yicha kamayish tartibida chiqaring.  
15. Kinolarni `release_year` bo‘yicha o‘sish tartibida chiqaring.  
16. Eng uzun davomiylikka ega 3 ta kinoni chiqaring.  
17. Dastlabki 4 ta kinoni chiqaring.  
18. 2 ta kinoni tashlab, keyingi 5 tasini chiqaring (`offset` \+ `limit`).  
19. Jadvaldagi jami kinolar sonini aniqlang.  
20. Eng yuqori ratingga ega kino ratingini aniqlang.  
21. Eng eski kino yilini aniqlang.  
22. Kinolarning o‘rtacha rating qiymatini aniqlang.  
23. Barcha kinolar davomiyligining (`duration`) jami yig‘indisini aniqlang.  
24. `genre` bo‘yicha guruhlab, har bir janrda nechta kino borligini chiqaring.  
25. `director` bo‘yicha guruhlab, o‘rtacha ratingni chiqaring.  
26. `rating < 8.0` bo‘lgan kinolarni toping.  
27. `title = "Dune"` bo‘lgan kinoning rating qiymatini `8.3` ga o‘zgartiring.  
28. `director = "Christopher Nolan"` bo‘lgan barcha kinolarning rating qiymatini `0.1` ga oshiring.  
29. `release_year < 2005` bo‘lgan barcha kinolarni o‘chirib tashlang.  
30. `genre = "Sci-Fi"` bo‘lgan kinolarning davomiyligini `10` daqiqaga oshiring.

**2-topshiriq**

Python dasturlash tilidagi **Data Types** mavzusi bo‘yicha kamida **10 minutlik tushuntirish video** tayyorlang.

Video davomida quyidagi mavzularni cover qilishingiz kerak:

* Data type nima?  
* `type()` funksiyasi qanday ishlaydi?  
* Quyidagi data typelar haqida tushuntirish:  
  * `int`  
  * `float`  
  * `str`  
  * `bool`  
* Har bir type uchun:  
  * ta’rif  
  * kamida 1 ta misol  
  * console output ko‘rsatish  
* Type conversion:  
  * `int()`  
  * `str()`  
  * `float()`

Talablar

* Video kamida 10 minut bo‘lishi kerak  
* Kodlarni o‘zingiz yozib tushuntiring  
* Tushuntirish oddiy va aniq bo‘lishi kerak  
* Har bir misolni ishlatib natijasini ko‘rsating

