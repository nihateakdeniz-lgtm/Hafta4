from uzay_oyunu.yakit_gostergesi import yakit_gostergesi

def test_yakit_gostergesi():
	sonuclar = list(yakit_gostergesi(100,30))
	assert sonuclar == [70, 40, 10, 0]

def test_yakit_gostergesi_stopiteration():
	g = yakit_gostergesi(10, 10)
	assert next(g) == 0
	import pytest
	with pytest.raises(StopIteration):
		next(g)