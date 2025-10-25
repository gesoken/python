# sequential_search.py

def sequential_search(arr, target):
    """
    Выполняет последовательный поиск элемента target в списке arr.

    Args:
        arr: Список, в котором нужно искать.
        target: Элемент, который нужно найти.

    Returns:
        Индекс элемента target в списке arr, если он найден.
        Возвращает -1, если элемент target не найден.
    """
    for i in range(len(arr)):  # Итерируемся по каждому элементу списка
        if arr[i] == target: # Проверяем, равен ли текущий элемент искомому элементу
            return i          # Если равен, возвращаем индекс текущего элемента

    return -1             # Если элемент не найден после перебора всего списка, возвращаем -1

# Пример использования (можно переместить в отдельный файл main.py, как и в предыдущих примерах)
if __name__ == "__main__":
    my_list = [5, 2, 9, 1, 5, 6]
    target_value = 9

    index = sequential_search(my_list, target_value)

    if index != -1:
        print(f"Элемент {target_value} найден по индексу {index}")
    else:
        print(f"Элемент {target_value} не найден в списке")