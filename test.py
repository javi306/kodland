meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Una respuesta muy común a algo gracioso",
            }

word = input("Escribe una palabra que no entiendas: ")
if word in meme_dict.keys():
    print(meme_dict[word])
