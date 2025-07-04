"""
Linear Search

Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr : list, target) -> int:
    """
    Perform a linear search for the target in the array.

    Parameters
    ----------
    arr : list
        List of elements to search through.
    target : Any
        The element to search for.

    Returns
    -------
    int
        The index of the target if found, otherwise -1.
    """

    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1