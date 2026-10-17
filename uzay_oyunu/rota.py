from functools import lru_cache

def rota_sayaci(baglantilar: dict):
#Verilen bağlantı haritası için önbellekli rota sayacı döndürür.

	@lru_cache(maxsize=None)
	def  rota_sayisi(gezegen: str, adim: int) -> int:
#Bir gezegenden başlayıp adım kadar yolculuk yapan farklı rota sayısını hesaplar
		if adim == 0:
			return 1
		toplam = 0
		for komsu in baglantilar.get(gezegen, []):
			toplam += rota_sayisi(komsu, adim - 1)
		return toplam
	return rota_sayisi