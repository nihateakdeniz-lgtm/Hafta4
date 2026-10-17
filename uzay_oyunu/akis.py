from typing import Generator 
import itertools

def fibonacci() -> Generator[int, None, None]:

	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b