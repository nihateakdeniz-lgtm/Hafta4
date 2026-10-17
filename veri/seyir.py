from typing import Generator, Tuple

def satirlari_oku(yol: str) -> Generator [str, None, None]:
#Boş ve # ile başlayan satırları atlayarak satır üretir
	with open(yol, "r") as f:
		for satir in f:
			satir = satir.strip()
			if satir and not satir.startswith("#"):
				yield satir

def ayristir(satirlar: Generator[str, None, None]) -> Generator[Tuple[str, str, int], None, None]:
#Satırları alıp (kaynak, hedef, yakit demetine çevirir.
	for satir in satirlar:
		parts = satir.split(maxsplit=1)
		if len(parts) == 2:
			rota, yakit_str = parts
			kaynak, hedef = rota.split("->")
			yield (kaynak.strip(), hedef.strip(), int(yakit_str))

def uzun_yolculuklar(kayitlar: Generator, esik: int) -> Generator[Tuple[str, str, int], None, None]:
#Yakıtı eşikten büyük olan kayıtları süzer.
	for kaynak, hedef, yakit in kayitlar:
		if yakit > esik:
			yield (kaynak, hedef, yakit)