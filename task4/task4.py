import sys


def min_moves_to_equal_nums(file):
    """Вычисление минимального количества ходов для приведения всех элементов к одному числу."""

    with open(file, 'r') as f:                                             # Считывание чисел из файла nums.txt в список
        nums = [int(line.strip()) for line in f]
    nums.sort()                                                            # Сортируем список
    if len(nums) % 2 == 0:                                                 # Вычисляем медианное значение списка
        median = (nums[:len(nums)//2][-1] + nums[len(nums)//2:][0]) // 2   # с четным количеством чисел
    elif len(nums) % 2 != 0:                                               # Вычисляем медианное значение списка
        median = nums[len(nums) // 2]                                      # с нечетным количеством чисел

    moves = sum(abs(num - median) for num in nums)                        # Считаем количество ходов
    return moves


if __name__ == "__main__":                                                 # Запуск через консоль
    file = sys.argv[1]
    print(min_moves_to_equal_nums(file))
