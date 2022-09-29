# Лабораторная работа "Intelligent Placer"
## Постановка задачи
На вход поступает фотография в формате .jpg, на которой на светлой горизонтальной поверхности изображены один или несколько предметов, выбранных из заранее заготовленных и отснятых (см. пункт "Список предметов"), а также нарисованный на белом листе бумаги А4 многоугольник. Необходимо определить, можно ли данные предметы поместить в данный многоугольник одновременно так, чтобы никакая часть предметов не выходила за границы многоугольника. В качестве выходных данных в консоль выводится результат в виде одного из слов:

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
Цвет фона - однотонный светлый.
Расположение камеры - сверху перпендикулярно предмету без существенных отклонений (не более 10 градусов).
Ориентация фотографий может быть произвольной.

### К предметам:
Предметы по размеру не могут быть больше листа бумаги А4.
Предметы не сливаются с листом бумаги и не накладываются друг на друга.
Границы предмета чёткие.
Предмет на фотографии может быть только в единственном экземпляре.

### К поверхности:
Поверхность горизонтальная, светлого цвета, однотонная.
На поверхности полностью помещается лист бумаги и предметы.
Поверхность выбирается однажды и не меняется для каждой фотографии.

### К исходным данным
В качестве исходных данных используются фотографии, на которых в центре белого листа А4 расположен по очереди каждый предмет. Всего предметов 10. Лист помещается на фотографию полностью. Фотографии сделаны согласно всем требованиям к фотографии. 

### К входным данным
В качестве входных данных подаётся фотография, сделанная по всем требованиям. 
На фотографии находится белый лист бумаги А4, на котором отчетливо нарисован многоугольник, а так же один или несколько предметов.
Предметы выбранны из заранее заготовленных и находятся в непосредственной близости от листа бумаги. Лист полностью помещается на фотографию.
Лист бумаги и предметы не перекрывают друг друга.

## План решения задачи

### Распознавание предметов с заранее сделанных фотографий
1.	Найти границы предмета с использованием алгоритма Кэнни, убрать шумы.

### Распознавание многоугольника и предметов 
1.	Найти границы предметов и многоугольника с использованием алгоритма Кэнни, убрать шумы.
2.	Отделить многоугольник от предметов. Предполагаемое решение: многоугольник искать, используя информацию о его расположении на белом листе, предметы – используя информацию о расположении на фоне.
3.	Если предметы или многоугольник не найдены или многоугольник незамкнут, то работа завершается, выводится No. 
4.	Образы предметов, которые были распознаны, с помощью особых точек сопоставить с образами предметов с заранее сделанных фотографий.

### Размещение предметов в многоугольнике
1.	Найти сумму площадей распознанных предметов и площадь многоугольника. Если площадь многоугольника оказалась меньше, то работа завершается, выводится No.
2.	В цикле по одному предмету размещать внутри многоугольника. Если на какой-то итерации этого сделать не удалось, то работа завершается, выводится No. 
Размещения есть два варианта: параллельным переносом и перебором вариантов поворота изображения. Пока не понятно, удастся ли продумать, как реализовать возможность без полного перебора учитывать размещение предметов с различными поворотами.
3.	Если все предметы удалось разместить, то работа завершается, выводится Yes, а полученное изображение сохраняется.




