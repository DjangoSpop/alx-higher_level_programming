#!/usr/bin/python3
def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    mid = len(list_of_integers) // 2
    if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
       (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
        return list_of_integers[mid]
    if mid != 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[:mid])
    return find_peak(list_of_integers[mid + 1:])
