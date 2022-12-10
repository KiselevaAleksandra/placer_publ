import cv2
import numpy as np
from intelligent_placer_lib.detectcontours import find_polygon_contour, find_objects_contour
from intelligent_placer_lib.placer import recursive_placer
from intelligent_placer_lib.rotate import make_rotate_center_list
from intelligent_placer_lib.extremepoints import extreme_points


def compress_image(img):  # сжатие
    new_height = int(img.shape[0] * 50/ 100)
    new_width = int(img.shape[1] * 50 / 100)
    compressed_image = cv2.resize(img, (new_width, new_height), cv2.INTER_AREA)
    return compressed_image


def check_image(img):
    img = compress_image(img)

    # получаем список точек контуров
    poly_area, approx_poly_list = find_polygon_contour(img)
    count_obj, sum_area, approx_obj_list = find_objects_contour(img)

    # обрабатываем ошибки
    if poly_area == 0:
        return -1, img
    if count_obj == 0:
        return -2, img
    if poly_area < sum_area:
        return -3, img

    # распологаем контуры предметов в порядке уменьшения площади
    approx_obj_list = sorted(approx_obj_list, reverse=True, key=cv2.contourArea)

    # получаем крайние точки поля
    top, bottom, left, right = extreme_points(approx_poly_list[0])
    p_top = top[1]
    p_bottom = bottom[1]
    p_left = left[0]
    p_right = right[0]

    rotate_center_list = []
    rotate_center_table = []

    # составляем таблицу значений контуров при повороте предметов в начале коорднат, чтобы не рассчитывать их каждый раз заново
    # globalvar.rotate_center_table.clear()
    for i in range(0, count_obj):
        rotate_center_list.clear()
        rotate_center_list = make_rotate_center_list(approx_obj_list[i], rotate_center_list)
        rotate_center_table.append(np.array(rotate_center_list))

    # с помощью рекурсивной функции размещаем предметы
    res = recursive_placer(0, img, count_obj, approx_obj_list, approx_poly_list, p_top, p_bottom, p_left, p_right,
                           rotate_center_table)

    if res == 1:
        return 1, img
    else:
        return 0, img
