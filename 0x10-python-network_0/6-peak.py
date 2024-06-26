#!/usr/bin/python3
"""Module to find a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int or None: Peak integer if found, None otherwise.
    """
    if not list_of_integers:
        return None
    
    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    
    mid = length // 2
    # Compare the middle element with its neighbors
    if list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    # If the middle element is smaller than its right neighbor, search in the right half
    elif list_of_integers[mid + 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[mid:])
    # Otherwise, search in the left half
    else:
        return find_peak(list_of_integers[:mid])

if __name__ == "__main__":
    # Test cases
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
