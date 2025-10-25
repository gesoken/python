# interpolation_search.py

def interpolation_search(arr, target):
    """
    Выполняет интерполирующий поиск элемента target в отсортированном списке arr.

    Args:
        arr: Отсортированный список, в котором нужно искать.
        target: Элемент, который нужно найти.

    Returns:
        Индекс элемента target в списке arr, если он найден.
        Возвращает -1, если элемент target не найден.
    """

    low = 0                  # Индекс начала поиска
    high = (len(arr) - 1)     # Индекс конца поиска

    while low <= high and arr[low] <= target <= arr[high]:
        # Проверяем, что low и high не пересеклись и что target находится в пределах значений arr[low] и arr[high]
        # Если target находится вне этого диапазона, он не может быть в списке.

        # Вычисляем предполагаемую позицию элемента target на основе интерполяции
        # Эта формула предполагает, что значения в списке равномерно распределены.
        # Если распределение неравномерное, производительность может ухудшиться.
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])

        if arr[pos] == target: # Если элемент найден
            return pos

        if arr[pos] < target:  # Если элемент в arr[pos] меньше, чем target, ищем в правой части
            low = pos + 1
        else:                  # Если элемент в arr[pos] больше, чем target, ищем в левой части
            high = pos - 1

    return -1  # Если элемент не найден

# Пример использования (можно поместить в отдельный файл main.py)
if __name__ == "__main__":
    # Пример отсортированного списка
    my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target_value = 14

    index = interpolation_search(my_list, target_value)

    if index != -1:
        print(f"Элемент {target_value} найден по индексу {index}")
    else:
        print(f"Элемент {target_value} не найден в списке")