from typing import List


def sum_list(lst: List[float]) -> float:
    total = 0
    while lst:
        total += lst.pop()
    return total


if __name__ == "__main__":
    original = [1, 2, 3, 4, 5]
    print("Original before:", original)

    # Using pop directly (this will empty the list)
    sample = original.copy()
    s = sum_list(sample)
    print("Sum using pop (on a copy):", s)
    print("Copy after sum_list (mutated):", sample)
    print("Original still intact:", original)

    # If you call sum_list on the original, it will be mutated
    s2 = sum_list(original)
    print("Sum using pop (on original):", s2)
    print("Original after sum_list (now empty):", original)
