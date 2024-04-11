def z9_1():
    import os
    from PIL import Image, ImageFilter
    #Путь к папке с изображениями
    folder1 = r'D:\Python\lab9\pictures'
    #Новая папка для обработанных изображений
    folder2 = './filters'
    os.makedirs(folder2, exist_ok=True)
    #Получаем список файлов из папки
    f_list = os.listdir(folder1)  #Получаем список всех файлов и папок в указанной директории
    pic_f = []  #Создаем пустой список для файлов изображений
    for f in f_list:
        if os.path.isfile(os.path.join(folder1, f)):  #Проверяем, является ли элемент файлом
            pic_f.append(f)  #Если файл, то добавляем его в список файлов изображений
    for file in pic_f:
        path1 = os.path.join(folder1, file)
        path2 = os.path.join(folder2, file)
        with Image.open(path1) as pic:
            pic_new = pic.filter(ImageFilter.FIND_EDGES)
            pic_new.save(path2)

    print("Обработка изображений завершена!")

def z9_2():
    import os
    from PIL import Image, ImageFilter
    # Путь к папке с изображениями
    folder1 = r'D:\Python\lab9\pictures'
    # Создаем новую папку для обработанных изображений
    folder2 = './filters'
    os.makedirs(folder2, exist_ok=True)
    # Получаем список файлов из папки
    f_list = os.listdir(folder1)  # Получаем список всех файлов и папок из указанной директории
    pic_f = []
    for f in f_list:  # Перебираем все элементы списка
        if os.path.isfile(os.path.join(folder1, f)):  # Проверяем, является ли элемент файлом
            if f.endswith(".png") or f.endswith(".jpg"):
                pic_f.append(f)  # Если файл, то добавляем его в список файлов изображений
            else:
                print("В папке присутствуют файлы другого типа")
    for file in pic_f:
        path1 = os.path.join(folder1, file)
        path2 = os.path.join(folder2, file)
        with Image.open(path1) as pic:
            pic_new = pic.filter(ImageFilter.FIND_EDGES)
            # Сохраняем обработанное изображение
            pic_new.save(path2)

    print("Обработка изображений завершена!")

def z9_3():
    import csv
    t_cost = 0
    with open("Книга1.csv", newline="") as csv_file:
        r = csv.DictReader(csv_file)
        for row in r:
            product = row["Продукт"]
            kolvo = int(row["Количество"])
            price = int(row["Цена"])
            cost = kolvo * price
            t_cost = t_cost + cost
            print(f"{product} - {kolvo} шт. за  {price} руб.")
    print(f"Итоговая сумма: {t_cost} руб.")
