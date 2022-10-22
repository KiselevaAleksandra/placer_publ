import cv2

# Функция возвращает путь, по которому надо сохранить файл с контуром для предметов
def takePath(num):
    numstr = str(num)
    numstrpng = numstr + '_contour.png'
    return numstrpng


# Функция возвращает путь, по которому надо сохранить файл с контуром для многоугольника
def takePathPolygon(num):
    numstr = str(num)
    numstrpng = 'polygon_' + numstr + '_contour.png'
    return numstrpng


# Функция находит контур некоторых предметов на заранее сделанных фотографиях
# Клубок ниток и расческа
def find_object_contour_1(img, num):
    # Получение чб изображение
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(imgrgb, cv2.COLOR_RGB2GRAY)

    # Бинаризация изображения
    _, binary = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)
    # plt.imshow(binary, cmap="gray")
    # plt.show()

    # Получение границ объекта
    canny_img = cv2.Canny(binary, 50, 100)
    # cv2.imshow('Edges Detected',canny_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Устранение шумов морфологическими операциями
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
    closing = cv2.morphologyEx(canny_img, cv2.MORPH_CLOSE, kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
    # cv2.imshow('Edges Detected',opening)
    # cv2.imshow('Edges Detected',closing)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Получение контуров объектов
    contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Нанесение нужного контура на изображение для проверки
    img = cv2.drawContours(img, contours, 0, (0, 255, 0), 2)
    # plt.imshow(img)
    # plt.show()

    # Сохранение изображения с нанесенными контурами в файл
    cv2.imwrite(takePath(num), img)
    # Подсчет площади полученного контура
    area = cv2.contourArea(contours[0])
    return area


# Функция находит контур некоторых объектов на заранее сделанных фотографиях
# Для всех остальных объектов
def find_object_contour_2(img, num):
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(imgrgb, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)
    canny_img = cv2.Canny(binary, 50, 100)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (80, 80))
    closing = cv2.morphologyEx(canny_img, cv2.MORPH_CLOSE, kernel)
    contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(img, contours, 2, (0, 255, 0), 2)
    cv2.imwrite(takePath(num), img)
    area = cv2.contourArea(contours[2])
    return area


# Функция находит контур некоторых объектов на заранее сделанных фотографиях
# Игрушка
def find_object_contour_3(img, num):
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(imgrgb, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 76, 255, cv2.THRESH_BINARY)
    canny_img = cv2.Canny(binary, 50, 100)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
    closing = cv2.morphologyEx(canny_img, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
    contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(img, contours, 0, (0, 255, 0), 2)
    cv2.imwrite(takePath(num), img)
    area = cv2.contourArea(contours[0])
    return area


# Функция находит контур некоторых объектов на заранее сделанных фотографиях
# Замазка
def find_object_contour_4(img, num):
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(imgrgb, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)
    canny_img = cv2.Canny(binary, 50, 100)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
    closing = cv2.morphologyEx(canny_img, cv2.MORPH_CLOSE, kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
    contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(img, contours, 1, (0, 255, 0), 2)
    cv2.imwrite(takePath(num), img)
    area = cv2.contourArea(contours[1])
    return area


# Функция находит контур некоторых объектов на заранее сделанных фотографиях
# Транспортир
def find_object_contour_5(img, num):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)
    canny_img = cv2.Canny(binary, 50, 100)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    closing = cv2.morphologyEx(canny_img, cv2.MORPH_CLOSE, kernel)
    contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(img, contours, 3, (0, 255, 0), 2)
    cv2.imwrite(takePath(num), img)
    area = cv2.contourArea(contours[3])
    return area


# Функция находит контур некоторых предметов на заранее сделанных фотографиях
# Блок закладок
def find_object_contour_6(img, num):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 185, 255, cv2.THRESH_BINARY)
    canny_img = cv2.Canny(binary, 50, 100)
    contours, hierarchy = cv2.findContours(canny_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(img, contours, 3, (0, 255, 0), 2)
    cv2.imwrite(takePath(num), img)
    area = cv2.contourArea(contours[3])
    return area


# Функция вызывает нужные функции для предметов
def init(img, num):
    if num == 1:
        find_object_contour_3(img, num)
    elif num == 2 or num == 3:
        find_object_contour_1(img, num)
    elif num == 4:
        find_object_contour_4(img, num)
    elif num == 10:
        find_object_contour_5(img, num)
    elif num == 9:
        find_object_contour_6(img, num)
    else:
        find_object_contour_2(img, num)


# Функция обрабатывает заранее сделанные .jpg изображения с предметами
def load_objects():
    # Цикл по всем фотографиям
    for num in range(1, 11):
        # Переводим .jpg изображения в .png
        numstr = str(num)
        namejpg = numstr + '.jpg'
        namepng = numstr + '.png'
        image = cv2.imread(namejpg)
        cv2.imwrite(namepng, image)
        # Вызов функции init
        image_png = cv2.imread(namepng)
        init(image_png, num)


# Функция находит контур многоугольника на фотографиях с основного датасета
def find_polygon_contour(img, num):
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(imgrgb, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
    canny_img = cv2.Canny(binary, 50, 100)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    closing = cv2.morphologyEx(canny_img, cv2.MORPH_CLOSE, kernel)
    contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Определение номера контура с максимальной площадью (то есть белого листа)
    maxArea = 0
    maxAreaNum = 0
    for k in range(hierarchy.shape[1]):
        area = cv2.contourArea(contours[k])
        if area > maxArea:
            maxArea = area
            maxAreaNum = k

    # Получение контура многоугольника
    # Цикл по всем найденным внури белого листа контурам
    for k in range(maxAreaNum, hierarchy.shape[1]):
        # Подсчет площади очередного контура
        area = cv2.contourArea(contours[k])
        # ищем первый контур внутри белого листа
        if area < maxArea - 1:
            img = cv2.drawContours(img, contours, k, (0, 255, 0), 2)
            # plt.imshow(img)
            # plt.show()
            # print(area)
            cv2.imwrite(takePathPolygon(num), img)
            return area
    return 0


# Функция обрабатывает .jpg изображения с основного датасета
def load_polygon():
    for num in range(1, 24):
        numstr = str(num)
        namejpg = 'polygon_' + numstr + '.jpg'
        namepng = 'polygon_' + numstr + '.png'
        image = cv2.imread(namejpg)
        cv2.imwrite(namepng, image)
        image_png = cv2.imread(namepng)
        find_polygon_contour(image_png, num)


load_objects()
load_polygon()
