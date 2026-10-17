from functools import reduce, partial
from typing import List, Dict

def yolculuk(mesafe: float, hiz: float) -> float:
#Yolculuk süresini hesaplar.
	return mesafe / hiz

hizli_yolculuk = partial(yolculuk, hiz=3)

def istatistik_hesapla(gezegenler: List[str], baglantilar: Dict[str, List[str]]):
#Galaksi verisi üzerinde map, filter, reduce, işlemleri yapar.
	buyuk_harf_listesi = list(map(str.upper, gezegenler))
#Tüm gezegen adlarını büyük harfe çevirir.
	cok_baglantili = list(filter(lambda x: len(baglantilar[x]) >= 2, gezegenler))
#En az iki bağlantısı olan gezegenleri süzer
	toplam_baglanti = reduce(lambda acc, x: acc, + len(baglantilar[x]), gezegenler, 0)
#Tüm bağlantı sayılarını toplar

	return buyuk_harf_listesi, cok_baglantili, toplam_baglanti