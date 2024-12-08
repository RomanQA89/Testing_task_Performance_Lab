import sys


def point_position_circle(file1, file2):
    """Определение положения точки относительно окружности."""
    with open(file1, 'r') as f:               # Чтение данных из file1.txt (Координаты центра окружности и его радиус)
        circle_data = f.readlines()
    circle_x, circle_y = map(float, circle_data[0].split())     # Координаты центра окружности
    radius = float(circle_data[1])                              # Радиус окружности

    with open(file2, 'r') as f:                                 # Чтение данных из file2.txt (Координаты точек)
        points = [line for line in f.readlines()]

    results = []                                                # Расчет положения каждой точки относительно окружности
    for point in points:
        point_x, point_y = map(float, point.split())
        # Вычисляем квадрат расстояния от точки до центра окружности
        distance_squared = (point_x - circle_x) ** 2 + (point_y - circle_y) ** 2
        if distance_squared == radius ** 2:                     # Проверка равенства:
            results.append('0 - точка лежит на окружности')     # на окружности
        elif distance_squared < radius ** 2:
            results.append('1 - точка внутри')                  # внутри окружности
        else:
            results.append('2 - точка снаружи')                 # вне окружности

    # Вывод результатов
    for result in results:
        print(result)


if __name__ == "__main__":                                     # Запуск через консоль
    file1 = sys.argv[1]                                        # Присвоение пути к файлу 1 аргумента командной строки
    file2 = sys.argv[2]                                        # Присвоение пути к файлу 2 аргумента командной строки
    point_position_circle(file1, file2)
