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

## Оценка качества результатов работы

1. Программа в большинстве случаев верно распознает контуры предметов. Незначительные проблемы возникают с предметами, которые на изображении сливаются с фоном (напрмер прозрачные края скотча приобретают оттенок фона). Но так как полученный контур не сильно отличается от ожидаемого, то на работе программы и получаемых результатах это не сказывается.

2. Если контуры распознаны верно, то результат размещения зависит от шага смещения и угла поворот: чем они меньше - тем выше точность результатов. Однако, от них зависит и время работы алгоритма, поэтому для оптимального соотношения время-качество были выбраны параметры, основанные на результатах работы программы для представленных входных данных.

3. Если многоугольник большой и/или предметов много, то в худшем случае программа перебирает все вожможные варианты размещений, что занимает много времени.

4. Все результаты на датасете представлены в таблицы. Был получен один неверный результат из-за того, что для конкретной фотографии шаг смещения получился большим: надо использовать меньший шаг.

![image](https://user-images.githubusercontent.com/72768554/206437108-4e8ea331-2b1a-45aa-9e22-8061bb00c341.png)

## Идеи по дальнейшему улуччшению алгоритма

На данном этапе был найден компромисс между временем и точностью, но из-за того, что в таком случае для одного предмета шаг оказался слишком большим, возникла ошибка. Для избежания этого есть следующая идея: добавить оценку сложности размещения для входных данных (например, оценивать площадь многоугольника и количество предметов), и в зависимости от нее задавать шаг.






