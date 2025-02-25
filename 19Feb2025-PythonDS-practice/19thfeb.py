# -*- coding: utf-8 -*-
"""

Set Exercises, Tuple Exercises, Dictionary Exercises.
"""

from collections import OrderedDict
from operator import itemgetter
from typing import Sequence, Tuple, Dict, Any, Union, List


def find_max(my_set: set) -> Any:
    """
    Return the maximum value in a set.
    """
    return max(my_set)


def find_min(my_set: set) -> Any:
    """
    Return the minimum value in a set.
    """
    return min(my_set)


def demo_min_max() -> None:
    """
    Demonstrate usage of find_max and find_min on a set.
    """
    set_1 = {1, 2, 3, 4, 5}
    print("Max of set_1:", find_max(set_1))
    print("Min of set_1:", find_min(set_1))


def insertion_deletion_example() -> None:
    """
    Show insertion/deletion operations on sets.
    """
    s = {1, 2}
    s.add(3)
    s.remove(2)
    s.discard(2)  # Safe removal, no error if element not present
    print("Popped:", s.pop())
    s.clear()
    print("Cleared set:", s)


def check_common_elements(list_a: List[int], list_b: List[int]) -> None:
    """
    Check if two lists have at least one element in common
    and print the common elements if they exist.
    """
    common = set(list_a) & set(list_b)
    if common:
        print("Common elements:", common)
    else:
        print("None")


def union_n(input_lists: List[List[int]]) -> List[int]:
    """
    Return the union of n lists as a single list.
    """
    res = set(input_lists[0])
    for array in input_lists[1:]:
        res.update(array)
    return list(res)


def demo_union_n() -> None:
    """
    Demonstrate usage of union_n function.
    """
    s = [
        [1, 2, 2, 4, 3, 6],
        [5, 1, 3, 4],
        [4, 7, 9, 10, 29]
    ]
    print("Union of lists:", union_n(s))


def intersection_difference_symmetric() -> None:
    """
    Intersection, difference, and symmetric difference of sets from user input.
    (Requires user input in the form of space-separated integers.)
    """
    a = map(int, input("Enter elements for set A: ").split())
    b = map(int, input("Enter elements for set B: ").split())
    set_a = set(a)
    set_b = set(b)

    print("Intersection:", set_a & set_b)
    print("Difference (A-B):", set_a - set_b)
    print("Symmetric Difference:", set_a ^ set_b)


def find_divisible_tuples(
    test_list: Sequence[Tuple[int, ...]],
    k: int
) -> List[Tuple[int, ...]]:
    """
    Find tuples which have all elements divisible by k from a sequence of tuples.
    """
    res: List[Tuple[int, ...]] = []
    for tup in test_list:
        if all(item % k == 0 for item in tup):
            res.append(tup)
    return res


def sort_tuples_by_second_item(
    tuples_list: Sequence[Tuple[Any, Any]]
) -> List[Tuple[Any, Any]]:
    """
    Sort a sequence of 2-item tuples by their second item, avoiding a lambda.
    """
    return sorted(tuples_list, key=itemgetter(1))


def extract_2digit_elements(
    test_list: Sequence[Tuple[int, ...]]
) -> List[Tuple[int, ...]]:
    """
    Extract tuples that have only 2-digit elements from a sequence of tuples.
    Example: 12, 45, 99 are valid; 9, 100 are not.
    """
    res: List[Tuple[int, ...]] = []
    for tup in test_list:
        if all(10 <= item <= 99 for item in tup):
            res.append(tup)
    return res


def extract_symmetric_tuples(
    test_list: Sequence[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    """
    Extract symmetric tuples (like (x, y) and (y, x)) from a sequence of pairs.
    """
    temp_set = set()
    res: List[Tuple[int, int]] = []
    for tpl in test_list:
        if tpl in temp_set or (tpl[1], tpl[0]) in temp_set:
            res.append(tpl)
        else:
            temp_set.add(tpl)
    return res


def sort_tuples_by_max(test_list: Sequence[Tuple[int, ...]]) -> List[Tuple[int, ...]]:
    """
    Sort a sequence of tuples by the maximum element in each tuple (descending).
    """
    return sorted(test_list, key=lambda x: max(x), reverse=True)


def sort_lists_in_tuple(
    tuple_list: Tuple[List[int], ...]
) -> Tuple[List[int], ...]:
    """
    Sort each list within a tuple of lists.
    Returns a tuple of sorted lists.
    """
    return tuple(sorted(sub_list) for sub_list in tuple_list)


def merge_dicts(d1: Dict[Any, Any], d2: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Merge two dictionaries.
    """
    merged = d1.copy()
    merged.update(d2)
    return merged


def remove_dict_keys(d: Dict[str, Any]) -> Dict[str, Any]:
    """
    Remove keys 'a' and 'b' from a dictionary (if they exist),
    and pop the last item (LIFO).
    """
    d_copy = d.copy()
    d_copy.pop('a', None)  
    d_copy.pop('b', None)  
    if d_copy:
        d_copy.popitem()
    return d_copy


def mean_dict_values(some_dict: Dict[Any, Union[int, float]]) -> float:
    """
    Calculate the mean of the dictionary values (which may be int or float).
    """
    return sum(some_dict.values()) / len(some_dict)


def sort_dict_by_key(my_dict: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Sort a dictionary by its keys, using itemgetter instead of a lambda.
    """
    return dict(sorted(my_dict.items(), key=itemgetter(0)))


def sort_dict_by_value(my_dict: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Sort a dictionary by its values, using itemgetter instead of a lambda.
    """
    return dict(sorted(my_dict.items(), key=itemgetter(1)))


def sum_dict_values(my_dict: Dict[Any, Union[int, float]]) -> float:
    """
    Find the sum of all values in a dictionary that may hold int or float.
    """
    return sum(my_dict.values())


def insertion_beginning_ordered_dict() -> OrderedDict:
    """
    Demonstrate insertion of an item at the beginning of an OrderedDict.
    """
    my_odict = OrderedDict([('a', '1'), ('b', '2')])
    my_odict.update({'c': '3'})
    my_odict.move_to_end('c', last=False)
    return my_odict


def find_winner_election(votes: List[str]) -> Tuple[str, Dict[str, int]]:
    """
    Given a list of votes, return the candidate with
    the maximum votes and the full vote count dictionary.
    """
    count: Dict[str, int] = {}
    for v in votes:
        count[v] = count.get(v, 0) + 1
    winner = max(count, key=lambda x: count[x])
    return winner, count


def find_duplicates_in_string(s: str) -> List[str]:
    """
    Find all duplicate characters in a string.
    """
    char_count: Dict[str, int] = {}
    duplicates: List[str] = []
    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1
    for ch, cnt in char_count.items():
        if cnt > 1:
            duplicates.append(ch)
    return duplicates


def main() -> None:
    """
    Main function to demonstrate all exercises.
    """
    print("== Set Exercises ==")
    demo_min_max()
    insertion_deletion_example()
    check_common_elements([1, 2, 3, 4], [5, 6, 3, 8])
    demo_union_n()
    intersection_difference_symmetric()

    print("\n== Tuple Exercises ==")
    test_list = [(6, 12, 2), (60, 12, 6), (12, 18, 21)]
    print("Tuples divisible by 6:", find_divisible_tuples(test_list, 6))

    scores = [("x", 100), ("y", 90), ("z", 60), ("a", 70), ("b", 80)]
    sorted_by_second = sort_tuples_by_second_item(scores)
    
    print("Sorted by second item (descending):", sorted_by_second[::-1])

    test_list_digits = [
        (54, 2), (34, 55), (222, 23), (12, 45),
        (78, 12), (9, 11), (333, 100)
    ]
    print(
        "Tuples with only 2-digit items:",
        extract_2digit_elements(test_list_digits)
    )

    symmetric_test = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]
    print("Symmetric tuples:", extract_symmetric_tuples(symmetric_test))

    test_list_sort = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]
    print("Sorted by max element:", sort_tuples_by_max(test_list_sort))

    tuple_list = ([3, 1, 2], [9, 7, 8], [5, 4, 6])
    print("Sorted lists in tuple:", sort_lists_in_tuple(tuple_list))

    print("\n== Dictionary Exercises ==")
    d1 = {'x': 1, 'y': 2}
    d2 = {'y': 3, 'z': 4}
    print("Merged dict:", merge_dicts(d1, d2))

    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    print("Dict after removing keys and last item:", remove_dict_keys(d))

    my_dict = {"a": 12, "b": 9, "c": 15, "d": 18, "e": 10}
    print("Mean of values:", mean_dict_values(my_dict))

    my_dict_2 = {'banana': 3, 'apple': 5, 'cherry': 2, 'date': 4}
    print("Sorted by key:", sort_dict_by_key(my_dict_2))
    print("Sorted by value:", sort_dict_by_value(my_dict_2))

    my_dict_3 = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
    print("Sum of values:", sum_dict_values(my_dict_3))

    print(
        "OrderedDict with insertion at beginning:",
        insertion_beginning_ordered_dict()
    )

    votes = [
        "a", "b", "c", "a", "a", "b", "c", "c", "c", "b",
        "a", "a", "a", "b", "b", "c", "b", "b", "b", "c",
        "c", "c", "b", "c", "a", "a", "b", "c", "d", "c",
        "b", "b"
    ]
    winner, count_dict = find_winner_election(votes)
    print(f"Election winner: {winner}, Votes count: {count_dict}")

    s_string = "qwertyuertyuipokjbvcxswertyuikmnbvfcx"
    print("Duplicate characters in string:", find_duplicates_in_string(s_string))


if __name__ == "__main__":
    main()
