# Implement a class `Counter` with a class variable that keeps track of the number
# of instances created. Run the demo in `__main__` to create several objects and
# print the count.



class Counter:
	# class variable shared across all instances
	count = 0

	def __init__(self):
		# increment the shared counter when a new instance is created
		Counter.count += 1

	@classmethod
	def get_count(cls) -> int:
		"""Return the number of Counter instances created so far."""
		return cls.count


if __name__ == "__main__":
	print("Creating three Counter instances...")
	a = Counter()
	b = Counter()
	c = Counter()
	print("Instances created:", Counter.get_count())

	print("Creating two more in a loop...")
	for _ in range(2):
		Counter()
	print("Instances created now:", Counter.get_count())


