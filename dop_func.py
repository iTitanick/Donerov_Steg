import secrets
import string

from PIL import Image, ImageDraw
import numpy as np

 # Функция извлекает цвета RGB из изображение
def read_color(img_path, color_metod):


    img = Image.open(img_path)
    img_pix = img.load()

    width = img.size[0]
    height = img.size[1]

    red = []
    green = []
    blue = []
    for x in range(width):
        for y in range(height):
            r, g, b = img_pix[x, y]
            red.append(r)
            green.append(g)
            blue.append(b)

    img.close()

    if color_metod == 'red':
        return red
    elif color_metod == 'green':
        return green
    elif color_metod == 'blue':
        return blue
    elif color_metod == 'pixels':
        data = []
        for i in range(len(red)):
            data.append(red[i])
            data.append(green[i])
            data.append(blue[i])
        return data
    else:
        return red + green + blue

 # Сохранение изменённых пикселей в изображении
def save_color(img_old_path, img_new_path, img_pix_new, color_metod):

   
    img = Image.open(img_old_path)
    img_draw = ImageDraw.Draw(img)
    img_pix = img.load()

    width = img.size[0]
    height = img.size[1]

    index = 0
    for x in range(width):
        for y in range(height):
            r, g, b = img_pix[x, y]
            if color_metod == 'red':
                img_draw.point((x, y), (img_pix_new, g, b))
            elif color_metod == 'green':
                img_draw.point((x, y), (r, img_pix_new, b))
            elif color_metod == 'blue':
                img_draw.point((x, y), (r, g, img_pix_new))
            elif color_metod == 'pixels':
                red = img_pix_new[index]
                green = img_pix_new[index+1]
                blue = img_pix_new[index+2]
                img_draw.point((x, y), (red, green, blue))
                index += 3
            else:
                red = img_pix_new[0:len(r)]
                green = img_pix_new[len(r):len(g)]
                blue = img_pix_new[len(g):]
                img_draw.point((x, y), (red, green, blue))

    img.save(img_new_path, "BMP")
    img.close()

 # Получает размеры изображения
def get_size(img_path):


    img = Image.open(img_path)
    width = img.size[0]
    height = img.size[1]
    img.close()

    return width, height

# Преобразует текст в массив байтов utf-8
def text_to_binary(text):


    text = text.encode("utf-8")
    data = []
    for c in text:
        data.append(c)
    return data

# Преобразует массив байт в текст utf-8
def binary_to_text(data):


    # text = ""
    # for byte in data:
    #     try:
    #         c = bytes([byte]).decode("utf-8")[0]
    #         text += c
    #     except:
    #         continue

    return bytes(data).decode("utf-8")

# Переводи байт в массив длины 8 бит
def number_to_bin_arr(data):


    return [1 if data & (1 << (7 - n)) else 0 for n in range(8)]

 # Обратное преобразование массива бит в байт
def bin_arr_to_number(data):

   
    out = 0
    for bit in data:
        out = (out << 1) | bit
    return out

# заменяет указанный бит в числе на единицу
def set_bit(value, bit):


    return value | (1<<bit)

# заменяет указанный бит в числе на ноль
def clear_bit(value, bit):


    return value & ~(1<<bit)

# Поиск первого вхождения подмассива в массиве
def find_SubarrayStartIndex(array, subArray):

    
    index = -1
    for i in range(len(array) - len(subArray) + 1):
        index = i
        for j in range(len(subArray)):
            if array[i + j] != subArray[j]:
                index = -1
                break
        if index >= 0:
            return index
    return -1

# Извлечение подмассива данных, окруженных двумя дургими подмассивами
def subarr_extract(bit_start, arr, bit_end):


    index_bs = find_SubarrayStartIndex(arr, bit_start)
    index_be = find_SubarrayStartIndex(arr, bit_end)
    return arr[index_bs+len(bit_start):index_be]

# Получение бита числа на определённой позиции
def retn_bit(num, pos):
    
    array_bit = number_to_bin_arr(num)
    return array_bit[pos]

# Деление вектора по модулю 2
def mod_on_2(vector):
    

    div_vector = vector.copy()
    div_vector.fill(2)
    return np.remainder(vector, div_vector)

# Переворачивание бита в векторе
def reverse_bit(vector, index):


    if index == -1:
        return vector
    if vector[index] == 1:
        vector[index] = 0
    else:
        vector[index] = 1
    return vector


def generate_alphanum_crypt_string(length):
    letters_and_digits = string.ascii_letters + string.digits + string.punctuation
    crypt_rand_string = ''.join(secrets.choice(
        letters_and_digits) for i in range(length))
    return crypt_rand_string