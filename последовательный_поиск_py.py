# sequential_search.py

def sequential_search(arr, target):
    """
    ��������� ���������������� ����� �������� target � ������ arr.

    Args:
        arr: ������, � ������� ����� ������.
        target: �������, ������� ����� �����.

    Returns:
        ������ �������� target � ������ arr, ���� �� ������.
        ���������� -1, ���� ������� target �� ������.
    """
    for i in range(len(arr)):  # ����������� �� ������� �������� ������
        if arr[i] == target: # ���������, ����� �� ������� ������� �������� ��������
            return i          # ���� �����, ���������� ������ �������� ��������

    return -1             # ���� ������� �� ������ ����� �������� ����� ������, ���������� -1

# ������ ������������� (����� ����������� � ��������� ���� main.py, ��� � � ���������� ��������)
if __name__ == "__main__":
    my_list = [5, 2, 9, 1, 5, 6]
    target_value = 9

    index = sequential_search(my_list, target_value)

    if index != -1:
        print(f"������� {target_value} ������ �� ������� {index}")
    else:
        print(f"������� {target_value} �� ������ � ������")