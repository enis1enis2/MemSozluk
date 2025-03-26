#Hocam Bu kısmı yaptığım araştırma ile Yaptım.Yani oyüzden böyle bir bölüm var.
def basit_benzerlik(k1, k2):
    # İki kelimeyi karşılaştırıp, aynı pozisyonda kaç harfin aynı olduğunu hesaplar.
    k1 = k1.upper()
    k2 = k2.upper()
    eslesen = 0
    for harf1, harf2 in zip(k1, k2):
        if harf1 == harf2:
            eslesen += 1
    # Hesaplamayı, iki kelimenin uzunluğu baz alınarak yapıyoruz.
    return eslesen / max(len(k1), len(k2))

def en_yakin_kelime(girdi, esik=0.6):
    # Girilen kelimeye en yakın kelimeyi bulur.
    en_iyi = None
    en_iyi_oran = 0
    for kelime in sozluk.keys():
        oran = basit_benzerlik(girdi, kelime)
        if oran > en_iyi_oran:
            en_iyi_oran = oran
            en_iyi = kelime
    return en_iyi if en_iyi_oran >= esik else None

sozluk = {
    "CRINGE": ("Garip ya da utandırıcı", "Bu video çok CRINGE!"),
    "LOL": ("Komik bir şey", "Adam düştü, LOL!"),
    "ROFL": ("Çok komik, gülmekten kırıldım", "Bu şaka ROFL!"),
    "WTF": ("Şaşkınlık verici", "Bu ne ya, WTF?!"),
    "OMG": ("Aman tanrım, ne oldu?", "OMG! Yeni haber!"),
    "SMH": ("Baş sallama", "Bu notlara bak, SMH!"),
    "BRB": ("Hemen döneceğim", "Biraz ara veriyorum, BRB!"),
    "BTW": ("Bu arada", "BTW, buldun mu?"),
    "TBH": ("Açıkçası", "TBH, o kadar da iyi değil."),
    "FTW": ("Harika!", "Gol FTW!"),
    "TMI": ("Fazla bilgi", "TMI, yeter artık!"),
    "YOLO": ("Hayat bir kez yaşanır", "YOLO, dene bakalım!"),
    "FOMO": ("Kaçırma korkusu", "FOMO yaşıyorum, gitmeliyim!"),
    "BFF": ("En iyi arkadaş", "O benim BFF'im."),
    "IDC": ("Umursamıyorum", "IDC, boşver!"),
    "IKR": ("Aynen", "Hava çok sıcak, IKR!"),
    "NSFW": ("Uygun olmayan içerik", "Bu video NSFW!"),
    "JK": ("Şaka yapıyorum", "Sınav iptal oldu, JK!"),
    "DM": ("Özel mesaj", "Adresini DM at.")
}

girdi = input("Anlamadığın bir kelime yaz: ").strip().upper()

if girdi in sozluk:
    anlam, ornek = sozluk[girdi]
    print(f"Anlam: {anlam}\nÖrnek: {ornek}")
else:
    yakin = en_yakin_kelime(girdi)
    if yakin:
        anlam, ornek = sozluk[yakin]
        print(f"Bunu mu demek istedin? {yakin}\nAnlam: {anlam}\nÖrnek: {ornek}")
    else:
        print("Henüz bu kelime sözlüğümüzde yok, ama üzerinde çalışıyoruz!")
