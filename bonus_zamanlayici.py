import time
from typing import Generator

def zamanlayici(aralik: float) -> Generator[float, None, None]:
	baslangic = time.time()
	while True:
		while time.time() - baslangic < aralik:
			pass
		baslangic = time.time()
		yield baslangic
def main():
	print ("Zamanlayıcı başladı (10 saniye sürecek)...\n")
	baslangic = time.time()
	tik_gen = zamanlayici(2)
	tak_gen = zamanlayici(5)
	tik_sayac = 0
	tak_sayac = 0
	while time.time() - baslangic < 10:
		simdi = time.time() - baslangic

		if simdi >= (tik_sayac + 1) * 2:
			next(tik_gen)
			print(f"[{simdi:.1f}s] tik")
			tik_sayac += 1
		if simdi >= (tak_sayac + 1) * 5:
			next(tak_gen)
			print(f"[{simdi:.1f}s] tak")
			tak_sayac += 1

		time.sleep(0.1)

	print("\nZamanlayıcı bitti.")

if __name__ == "__main__":
	main()