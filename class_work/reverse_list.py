def reverse_with_pop(lst):
    return [lst.pop() for _ in range(len(lst))]

def reverse_in_place(lst):
    lst.reverse()

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("Original:", data)

    c = data.copy()
    print("Reversed with pop (result):", reverse_with_pop(c))
    print("List passed to reverse_with_pop after call (mutated):", c)

    c2 = data.copy()
    reverse_in_place(c2)
    print("After reverse_in_place (mutated):", c2)

    print("Original after operations (unchanged):", data)
