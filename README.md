# Лабораторная работа "Intelligent Placer"
## Постановка задачи
На вход поступает фотография в формате .jpg, на которой на однотонной горизонтальной поверхности изображены один или несколько предметов, выбранных из заранее заготовленных и отснятых (см. пункт "Список предметов"), а также нарисованный на белом листе бумаги А4 многоугольник. Необходимо определить, можно ли данные предметы поместить в данный многоугольник одновременно так, чтобы никакая часть предметов не выходила за границы многоугольника. В качестве выходных данных в консоль выводится результат в виде одного из слов:

Yes - предметы можно разместить в многоугольнике

No - предметы нельзя разместить в прямоугольнике или входные данные неверные

## Список предметов
1. Замазка
2. Расческа
3. Скотч
4. Ножницы
5. Флешка
6. Набор закладок
7. Транспортир
8. Клубок ниток
9. Губная помада
10. Игрушка

## Фотографии предметов
Примеры предметов находятся в документе "Data.md"

## Набор входных данных для тестирования
Набор входных данных вместе с ожидаемым результатом работы находится в документе "Data.md"

## Требования
### К фотографиям
1. Формат фотографий - .jpg 
2. Условия съемки: 
Фотографии сделаны отчетливо, без бликов или интенсивных теней, на одну и ту же камеру.
Цвет фона - однотонный, темнее листа бумаги.
Расположение камеры - сверху перпендикулярно предмету без существенных отклонений (не более 10 градусов).
Ориентация фотографий может быть произвольной.

### К предметам:
Предметы по размеру не могут быть больше листа бумаги А4.
Предметы не сливаются с листом бумаги и не накладываются друг на друга.
Границы предмета чёткие.
Предмет на фотографии может быть только в единственном экземпляре.

### К поверхности:
Поверхность горизонтальная, темнее листа бумаги, однотонная.
На поверхности полностью помещается лист бумаги и предметы.
Поверхность выбирается однажды и не меняется для каждой фотографии.

### К исходным данным
В качестве исходных данных используются фотографии, на которых в центре белого листа А4 расположен по очереди каждый предмет. Всего предметов 10. Лист помещается на фотографию полностью. Фотографии сделаны согласно всем требованиям к фотографии. 

### К входным данным
В качестве входных данных подаётся фотография, сделанная по всем требованиям. 
На фотографии находится белый лист бумаги А4, на котором отчетливо маркером нарисован многоугольник, а так же один или несколько предметов.
Предметы выбранны из заранее заготовленных и находятся в непосредственной близости от листа бумаги. Лист полностью помещается на фотографию.
Лист бумаги и предметы не перекрывают друг друга.

## План решения задачи

### Распознавание многоугольника 
1.	Перевести изображение из RGB в grayscale.
2.	Бинаризовать изображение.
3.	Находим контур многоугольника внутри белого листа. Контуры вне белого листа не рассматриваем.
4.	Если многоугольник не найден, то работа завершается, выводится No.
5.	Производим аппроксимацию контура многоугольника для упрощения работы с контуром и уменьшения скорости расчетов.

### Распознавание предметов
1.	Для отделения предметов от фона применяем цветовой фильтр.
2.	Находим все контуры на изображении.
3.	Находим контур листа бумаги и в качестве контуров предметов берем те, которые обнаружили вне контура листа бумаги.
4.	Если предметы не найдены, то работа завершается, выводится No.
5.	Отбрасываем внутренние контуры предметов (для ножниц и скотча).

### Размещение предметов в многоугольнике
1.	Найти сумму площадей распознанных предметов, сравнить с площадью многоугольника.
Если площадь многоугольника оказалась меньше, то работа завершается, выводится No.

2.	С помощью рекурсивной функции размещать предметы в многоугольнике в порядке уменьшения площади. 
Функция вызывается для каждого предмета отдельно (см. пункт 3). Размещение предмета считается успешным, если удастся успешно разместить следующий предмет.
Если предмет разместить не удалось, то работа завершается, выводится No.

3.	Алгоритм размещения каждого объекта в многоугольнике:

- размещение происходит в описанном вокруг данного многоугольника прямоугольнике и начинается с верхнего левого угла описанного прямоугольника

- происходит перемещение объекта сначала по х затем по у на заранее заданный шаг

- проверяется не пересекается ли предмет с другими предметами и находится ли предмет внутри многоугольника

- если разместить не удалось, то происходит поворот объекта относительно его центральной точки с проверкой на возможность размещения объекта 

4.	Если все предметы удалось разместить, то работа завершается, выводится Yes.





