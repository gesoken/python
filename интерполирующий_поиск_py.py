# interpolation_search.py

def interpolation_search(arr, target):
    """
    ��������� ��������������� ����� �������� target � ��������������� ������ arr.

    Args:
        arr: ��������������� ������, � ������� ����� ������.
        target: �������, ������� ����� �����.

    Returns:
        ������ �������� target � ������ arr, ���� �� ������.
        ���������� -1, ���� ������� target �� ������.
    """

    low = 0                  # ������ ������ ������
    high = (len(arr) - 1)     # ������ ����� ������

    while low <= high and arr[low] <= target <= arr[high]:
        # ���������, ��� low � high �� ����������� � ��� target ��������� � �������� �������� arr[low] � arr[high]
        # ���� target ��������� ��� ����� ���������, �� �� ����� ���� � ������.

        # ��������� �������������� ������� �������� target �� ������ ������������
        # ��� ������� ������������, ��� �������� � ������ ���������� ������������.
        # ���� ������������� �������������, ������������������ ����� ����������.
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])

        if arr[pos] == target: # ���� ������� ������
            return pos

        if arr[pos] < target:  # ���� ������� � arr[pos] ������, ��� target, ���� � ������ �����
            low = pos + 1
        else:                  # ���� ������� � arr[pos] ������, ��� target, ���� � ����� �����
            high = pos - 1

    return -1  # ���� ������� �� ������

# ������ ������������� (����� ��������� � ��������� ���� main.py)
if __name__ == "__main__":
    # ������ ���������������� ������
    my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target_value = 14

    index = interpolation_search(my_list, target_value)

    if index != -1:
        print(f"������� {target_value} ������ �� ������� {index}")
    else:
        print(f"������� {target_value} �� ������ � ������")