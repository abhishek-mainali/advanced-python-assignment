from typing import List, Any
def common_elements_pop(a: List[Any], b: List[Any]) -> List[Any]:

    a_copy = a.copy()
    b_copy = b.copy()
    commons: List[Any] = []

    while a_copy:
        item = a_copy.pop()  
        try:
            idx = b_copy.index(item)
        except ValueError:
            # not found
            continue
        else:
            b_copy.pop(idx)
            commons.append(item)

    # The commons list currently contains items in the reverse order of
    # their last occurrence in `a`; reverse for a more natural order.
    commons.reverse()
    return commons


if __name__ == "__main__":
    list1 = [1, 2, 2, 3, 4]
    list2 = [2, 2, 4, 5]

    print("List1:", list1)
    print("List2:", list2)

    commons = common_elements_pop(list1, list2)
    print("Common elements (using pop on copies):", commons)

    # Demonstrate that originals are intact
    print("List1 after call:", list1)
    print("List2 after call:", list2)

    l1 = list1.copy()
    l2 = list2.copy()
    print("\nDemonstrating mutation if caller uses pop on originals:")
    while l1:
        item = l1.pop()
        if item in l2:
            l2.remove(item)
            print("Matched and removed:", item)
    print("l1 after manual popping:", l1)
    print("l2 after manual removals:", l2)
