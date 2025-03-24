meme_sozlugu = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "ROFL bir şakaya karşılıktır, LOL gibidir"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if kelime in meme_sozlugu.keys():
    print(meme_sozlugu[kelime])
else:
    print("Henüz bu kelimeye sahip değiliz... Ama üzerinde çalışıyoruz!")
