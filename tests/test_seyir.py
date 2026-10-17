from veri.seyir import satirlari_oku, ayristir, uzun_yolculuklar

def test_boru_hatti_toplam_yakt():
	kayitlar = ayristir(satirlari_oku("veri/seyir.txt"))
	toplam = sum(y for _, _, y in kayitlar)
	assert toplam == 88

def test_uzun_yolculuklar():
	kayitlar = ayristir(satirlari_oku("veri/seyir.txt"))
	uzunlar = list(uzun_yolculuklar(kayitlar, 10))
	hedefler = [h for _, h, _ in uzunlar]
	assert hedefler == ['sirius', 'centauri', 'orion', 'kara_delik']