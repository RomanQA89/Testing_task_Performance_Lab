import sys


def cycle_path(n, m):
    """Создание кругового массива от 1 до n."""
    cycle_array = list(range(1, n + 1))
    path = []
    start_index = 0

    while True:
        end_index = (start_index + m - 1) % n       # Находим конец текущего интервала
        path.append(cycle_array[start_index])       # Добавляем начальный элемент интервала в путь
        start_index = end_index                     # Переходим к следующему началу интервала
        if start_index == 0:                        # Если мы вернулись к началу, выходим из цикла
            break
    return path


if __name__ == "__main__":                          # Запуск через консоль
    n = int(sys.argv[1])                            # Присвоение длине матрицы аргумента командной строки
    m = int(sys.argv[2])                            # Присвоение длине обхода матрицы аргумента командной строки
    result = cycle_path(n, m)
    print(''.join(map(str, result)))
