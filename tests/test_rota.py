from uzay_oyunu.rota import rota_sayaci

TEST_BAGLANTILAR = {
	"dünya": ["centauri", "sirius"],
	"centauri": ["dünya", "orion"],
	"sirius": ["dünya", "kara_delik"],
	"orion": ["centauri", "kara_delik"],
	"kara_delik": ["sirius", "orion", "dünya"]
}

def test_rota_sayaci():
	say = rota_sayaci(TEST_BAGLANTILAR)
	assert say("dünya", 3) == 9
	assert say("dünya", 10) == 2004
	assert say("dünya", 40) == 24928276228585