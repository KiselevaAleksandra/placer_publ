import cv2
from intelligent_placer_lib.extremepoints import extreme_points
from intelligent_placer_lib.rotate import rotate_center
from intelligent_placer_lib.location import check_place


# перемещаем контур предмета и проверяем, удалось ли предмет разместить
def move(num, img, approx_obj_list, approx_poly, p_top, p_bottom, p_left, p_right, rotate_center_table):
    offset_base = 9

    # перемещает контур в положительном направлении по х на значение offset_base
    approx_obj_list[num] = approx_obj_list[num] + [offset_base, 0]
    o_top, o_bottom, o_left, o_right = extreme_points(approx_obj_list[num])

    # если дошли до правого края многоугольника, то возвращаем контур к левому краю
    # и смещаем в положительном направлении по y на значение offset_base
    if o_right[0] > p_right:
        moment = cv2.moments(approx_obj_list[num])
        cx = int(moment['m10'] / moment['m00'])
        cy = int(moment['m01'] / moment['m00'])
        offsetX = p_left + 1 - cx
        approx_obj_list[num] = approx_obj_list[num] + [offsetX, offset_base]

        # если предмет находится в нижней правой точке  - return -1 (разместить нельзя)
        if cy + offset_base > p_bottom:
            return -1, approx_obj_list[num]

    # проверка, удалось ли разместить предмет
    if check_place(num, img, approx_obj_list, approx_poly):
        return 1, approx_obj_list[num]

    # поворот конура вокруг точки центра предмета
    res, approx_obj_rotate = rotate_center(num, img, approx_obj_list.copy(), approx_poly, rotate_center_table)
    if res == 1:
        return 1, approx_obj_rotate

    return 0, approx_obj_list[num]


# с помощью рекурсивной функции размещаем предмет под номером num
def recursive_placer(num, img, count_obj, approx_obj_list, approx_poly_list, p_top, p_bottom, p_left, p_right,
                     rotate_center_table):
    # если все предметы размещены - return 1
    if num == count_obj:
        return 1

    # центр предмета ставим в точку пересения правой и верхней границ многоугольника
    moment = cv2.moments(approx_obj_list[num])
    cx = int(moment['m10'] / moment['m00'])
    cy = int(moment['m01'] / moment['m00'])
    offset_x = cx - p_left - 1
    offset_y = cy - p_top - 1
    approx_obj_list[num] = approx_obj_list[num] - [offset_x, offset_y]

    # размещаем предмет
    while 1:
        # вызываем функцию размещения для текущего предмета
        # output == 1 если удалось разместить предмет, иначе -1
        res, approx_obj_list[num] = move(num, img, approx_obj_list, approx_poly_list[0], p_top, p_bottom, p_left,
                                         p_right, rotate_center_table)

        # если удалось разместить текущий предмет и удалось разместить следующий предмет - return 1
        if res == 1 and recursive_placer(num + 1, img, count_obj, approx_obj_list, approx_poly_list, p_top, p_bottom,
                                         p_left, p_right, rotate_center_table) == 1:
            cv2.drawContours(img, [approx_obj_list[num]], 0, (255, 0, 255), 3)
            return 1

        # если текущий предмет разместить не удалось  - return -1
        if res == -1:
            return -1
