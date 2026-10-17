from typing import Generator 
import itertools 

def fibonacci() -> Generator[int, None, None]:
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b

def test_fibonacci():
	g = fibonacci()
	assert next(g) == 0
	assert next(g) == 1
	assert next(g) == 1

def test_fibonacci_islice():
	g = fibonacci()
	ilk_12 = list(itertools.islice(g, 12))
	assert ilk_12 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]