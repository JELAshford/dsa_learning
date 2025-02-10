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
        elif val < value:
            if low == mid:
                break
            low, high = mid, high
        else:
            if high == mid:
                break
            low, high = low, mid
    return None
