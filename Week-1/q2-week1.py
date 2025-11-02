
class A:
	def greet(self):
		print("Hello from A")


class B:
	def greet(self):
		print("Hello from B")


class C(A, B):
	"""C inherits from A and B (in that order)."""
	pass


if __name__ == "__main__":
	c = C()
	print("Calling c.greet():")
	c.greet()

	# Show the method resolution order for clarity
	print("C MRO:", [cls.__name__ for cls in C.mro()])

	# Demonstrate how to explicitly call the other greet if needed
	print("\nExplicit calls:")
	print("A.greet(c):", end=" ")
	A.greet(c)
	print("B.greet(c):", end=" ")
	B.greet(c)

