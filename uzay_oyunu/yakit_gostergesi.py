def yakit_gostergesi(yakit: int, tuketim:int) -> Generator[int, None, None]:

# Her adımda yakıtı azaltır ve kalan miktarı üretir.
# Yakıt 0'a düştüğünde durur.

	while yakit > 0:
		yakit -= tuketim
		if yakit < 0:
			yakit = 0
		yield yakit
		if yakit == 0:
			break