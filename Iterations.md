## 1 итерация
### Было сделано:
1.	Распознавание предметов с заранее сделанных фотографий: сделано как в описанном плане с теми же шагами (шаги описаны в комментариях к коду).

Замечания: 
Сейчас обработка разных предметов описана разными функциями из-за возникающих во время реализации трудностей с выделением границ. Впоследствии я постараюсь сделать это одной функцией.
Также в некоторых предметах границы выделяются недостаточно четко (замазка и игрушка), это также постараюсь.

2.	Распознавание многоугольника с основного датасета: сделано как в описанном плане (шаги также описаны в комментариях к коду).

Замечания:
В процессе реализации была замечена существенная неточность в датасете, а именно нечеткие границы многоугольников, из-за чего не получалось точно выделить их границы. Поэтому я добавила требование о отрисовывании многоугольника маркером, а также переделала основной датасет в соответствии с этим требованием.

### Результаты:
1. Выделение контуров на предметах с заранее сделанных фотографий.

![1_contour](https://user-images.githubusercontent.com/72768554/197344979-afda431f-7e81-4b61-b7bd-4df5e1eab351.png)

![2_contour](https://user-images.githubusercontent.com/72768554/197344989-ac5395b5-acf8-49e7-9cad-6e7e632e0cae.png)

![3_contour](https://user-images.githubusercontent.com/72768554/197344995-03d677e4-b4d2-4342-a3ef-ee1d905892ab.png)

![4_contour](https://user-images.githubusercontent.com/72768554/197345000-0fce7908-69cf-4df5-ae34-2607458aab53.png)

![5_contour](https://user-images.githubusercontent.com/72768554/197345005-01e72376-ed07-44d1-bdd5-f39d62f73862.png)

![6_contour](https://user-images.githubusercontent.com/72768554/197345013-7fae247b-690a-4c2c-b771-7af16b6033d5.png)

![7_contour](https://user-images.githubusercontent.com/72768554/197345018-b8f8f3f7-b7bc-48ea-a530-3137650cad00.png)

![8_contour](https://user-images.githubusercontent.com/72768554/197345023-67c3efcd-d9cb-4bcf-a28a-fae99cf1e580.png)

![9_contour](https://user-images.githubusercontent.com/72768554/197345037-ac68b5f7-a615-41bb-9a09-cc7799e5c30e.png)

![10_contour](https://user-images.githubusercontent.com/72768554/197345040-ba59c778-4e8b-4c60-b51d-e96a23e7d805.png)


3. Выделение границ многоугольников.

![polygon_1_contour](https://user-images.githubusercontent.com/72768554/197345087-7b084e3d-aef5-405f-8c8d-c8a98eeae186.png)

![polygon_3_contour](https://user-images.githubusercontent.com/72768554/197345241-246fd183-7304-4960-a515-21d9dcf2e030.png)

![polygon_4_contour](https://user-images.githubusercontent.com/72768554/197345244-51694666-ace0-4852-b3bd-ed956fc90b1f.png)

![polygon_6_contour](https://user-images.githubusercontent.com/72768554/197345265-92ef15d2-e7af-4e83-8ca7-f85d4beb4834.png)

![polygon_7_contour](https://user-images.githubusercontent.com/72768554/197345271-5331358f-2a3a-4a5a-8377-b9f88f4f7a3a.png)

![polygon_8_contour](https://user-images.githubusercontent.com/72768554/197345291-89f7c47b-6e4c-4cc3-8d42-b1be833cccc4.png)

![polygon_19_contour](https://user-images.githubusercontent.com/72768554/197345325-fe421910-ee2b-4090-b97b-70f987b6cfcb.png)
