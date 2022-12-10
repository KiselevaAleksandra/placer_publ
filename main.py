import time
import cv2
import os
from intelligent_placer_lib.starter import check_image


def save_res(num):
    num_str = str(num)
    path = 'output/' + num_str + '_res.jpg'
    return path

# Функция обрабатывает .input изображения с основного датасета
if __name__ == '__main__':
    for num in range(1, 36):
        time_start = time.time()
        path = 'input/polygon_' + str(num) + '.jpg'
        img = cv2.imread(path)

        print("№", num)
        res, img = check_image(img)


        if res == 1:
            print("     YES")
        if res == 0:
            print("     NO")
        if res == -1:
            print('     FALSE: нет многоугольников')
            print('     NO')
        if res == -2:
            print('     FALSE: нет предметов')
            print('     NO')
        if res == -3:
            print('     polygon area < objects area')
            print('     NO')

        print('     Time:', "{0:.2f}".format(time.time() - time_start))

        if not os.path.exists('output'):
            os.mkdir('output')

        cv2.imwrite(save_res(num), img)


