from typing import Tuple


def min_max(t: Tuple[float, ...]) -> Tuple[float, float]:
	return (min(t), max(t))


if __name__ == "__main__":
	t = (3, 1, 7, 4)
	print(min_max(t))

