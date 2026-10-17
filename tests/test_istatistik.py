from uzay_oyunu.istatistik import istatistik_hesapla, hizli_yolculuk

def istatistik():
	gezegenler = ["dünya", "centuari", "sirius", "orion", "kara_delik"]
	baglantilar = {
	"dünya": ["centauri", "sirius"],
	"centauri": ["dünya", "orion"],
	"sirius": ["dünya", "kara_delik"],
	"orion": ["centauri", "kara_delik"],
	"kara_delik": ["sirius", "orion", "dünya"]
}
	buyuk, cok_bag, toplam = istatistik_hesapla(gezegenler, baglantilar)
	assert buyuk == ['DÜNYA', 'CENTAURI', 'SIRIUS', 'ORION', 'KARA_DELIK']
	assert cok_bag == ['dünya', 'centauri', 'sirius', 'orion']
	assert toplam == 10

def test_partial():
	assert hizli_yolculuk(15) == 5.0