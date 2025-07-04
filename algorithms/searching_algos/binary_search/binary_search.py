"""
Binary Search - Iterative and Recursive Implementations

Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive
"""

def binary_search(array : list, target) -> int:
    """
    Perform a binary search for the target in the sorted array.

    Parameters
    ---------- 
    array : list
        Sorted list of elements to search through.
    target : Any
        The element to search for.

    Returns
    -------
    int
        The index of the target if found, otherwise -1.
    """

    left, right = 0, len(array) - 1

    while left <= right:

        mid = left + (right - left) // 2 # To avoid possible integer overflow

        if array[mid] == target:
            return mid
        if array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1



def binary_search_recursive(array : list, target, left=0, right=None) -> int:
    """
    Perform a binary search for the target in the sorted array using recursion.

    Parameters
    ----------
    array : list
        Sorted list of elements to search through.
    target : Any
        The element to search for.
    left : int, optional
        The left index of the current search range (default is 0).
    right : int, optional
        The right index of the current search range (default is None).

    Returns
    -------
    int
        The index of the target if found, otherwise -1.
    """

    if right is None:
        right = len(array) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array, target, left, mid - 1)
    else:
        return binary_search_recursive(array, target, mid + 1, right)