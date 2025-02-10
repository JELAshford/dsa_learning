from typing import List, Union


def binary_search(array: List, value: int) -> Union[int, None]:
    """Get the index of the `value` in the sorted `array`.

    Args:
        array (List): Array to search
        value (int): Value to search for
    """
    low, high = 0, len(array)
    while low < high:
        mid = (high + low) // 2
        val = array[mid]
        if val == value:
            return mid
        if (low == mid) or (high == mid):
            break
        if val < value:
            low = mid
        else:
            high = mid
    return None
