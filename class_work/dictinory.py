"""Dictionary utilities: print key-values, merge dictionaries, char frequency.

Provides small helpers and a demo when run as __main__.
"""

from typing import Any, Dict


def print_kv(d: Dict[Any, Any]) -> None:
    """Print all key: value pairs in the dictionary `d`."""
    for k, v in d.items():
        print(f"{k}: {v}")


def merge_dicts(d1: Dict[Any, Any], d2: Dict[Any, Any]) -> Dict[Any, Any]:
    """Return a new dictionary containing keys from `d1` and `d2`.

    Values from `d2` override those from `d1` when keys overlap.
    """
    merged = d1.copy()
    merged.update(d2)
    return merged


def char_frequency(s: str) -> Dict[str, int]:
    """Return a dictionary mapping each character in `s` to its frequency."""
    freq: Dict[str, int] = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


if __name__ == "__main__":
    # Example dictionaries (books)
    book1 = {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year_published": 1960}
    book2 = {"title": "To Kill a Mockingbird", "publisher": "J.B. Lippincott & Co.", "year_published": 1961}

    print("Book1 key-values:")
    print_kv(book1)
    print("\nBook2 key-values:")
    print_kv(book2)

    merged = merge_dicts(book1, book2)
    print("\nMerged book (book2 overrides book1 on conflict):")
    print_kv(merged)

    # Character frequency demo
    sample = "hello world"
    print(f"\nCharacter frequency for: '{sample}'")
    freq = char_frequency(sample)
    print_kv(freq)
from typing import Any, Dict


def make_book(title: str, author: str, year: int) -> Dict[str, Any]:
    return {
        "title": title,
        "author": author,
        "year_published": year,
    }


def add_key_value(d: Dict[str, Any], key: str, value: Any) -> None:
    d[key] = value


if __name__ == "__main__":
    book = make_book("To Kill a Mockingbird", "Harper Lee", 1960)

    print("Book dictionary:", book)

    # Access individual fields
    print("Title:", book["title"])
    print("Author:", book.get("author"))
    print("Year published:", book.get("year_published"))

    # Update a field
    add_key_value(book, "year_published", 1961)
    print("Updated year_published:", book["year_published"])

    # Add another field
    add_key_value(book, "publisher", "J.B. Lippincott & Co.")
    print("With publisher added:", book)

    # Demonstrate adding a new arbitrary key
    add_key_value(book, "ISBN", "978-0-06-112008-4")
    print("After adding ISBN:", book)


def make_book(title: str, author: str, year: int) -> dict:
    return {
        "title": title,
        "author": author,
        "year_published": year,
    }


if __name__ == "__main__":
    book = make_book("To Kill a Mockingbird", "Harper Lee", 1960)

    # Print the whole dictionary
    print("Book dictionary:", book)

    # Access individual fields
    print("Title:", book["title"])
    print("Author:", book.get("author"))
    print("Year published:", book.get("year_published"))

    # Update a field
    book["year_published"] = 1961
    print("Updated year_published:", book["year_published"])

    # Add another field
    book["publisher"] = "J.B. Lippincott & Co."
    print("With publisher added:", book)