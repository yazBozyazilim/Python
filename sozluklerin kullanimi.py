personel = {}
personel_sayisi = int(input("Personel sayisi giriniz:"))
personel_id = 100
for i in range(1,personel_sayisi+1):
    personel_bilgisi = {}
    adSoyad = input("{}. Personelin adi soyadi nedir -> ".format(i))
    personel_bilgisi["AD-SOYAD"] = adSoyad
    maas = int(input("{}. personele ait maas bilgisini giriniz ->".format(i)))
    personel_bilgisi["MAAS"] = maas
    cs = int(input("{}. personele ait cocuk sayisini giriniz ->".format(i)))
    personel_bilgisi["CS"] = cs
    zam_miktari = int(input("{}. personele ait zam bilgisini giriniz ->".format(i)))
    personel_bilgisi["Zam Bilgisi"] = zam_miktari
    personel[personel_id] = personel_bilgisi
    personel_id += 1

for per_id in personel.keys():
    print("Personel id -> {}".format(per_id))
    for per_bilgi in personel[per_id].keys():
        print("{} -> {}".format(per_bilgi,personel[per_id][per_bilgi]))

zam_guncelleme = int(input("Kac nolu iddeki personelin maasina zam yapmak istiyorsunuz:"))

if zam_guncelleme in personel.keys():
    for per_id in personel.keys():
        if per_id == zam_guncelleme:
            personel[per_id]["Zam Bilgisi"] += personel[per_id]["Zam Bilgisi"] * 0.3

    for per_id in personel.keys():
        print("Personel id -> {}".format(per_id))
        for per_bilgi in personel[per_id].keys():
            print("{} -> {}".format(per_bilgi, personel[per_id][per_bilgi]))
else:
    print("Girdiginiz id sahip bir calisan bulunamadi.")
"""golSayisi_prim = list()
        golSayisi = int(input("{}. ID'deki futbolcunun attigi gol sayisi kactir:".format(ID)))
        Prim = golSayisi + (golSayisi * 40)
        print("Atilan gol sayisina gore futbolcuya odenecek prim miktari : {}".format(Prim))
        golSayisi_prim.append(golSayisi)
        golSayisi_prim.append(Prim)

        for fut_id in bilgiler.keys():
            if fut_id == ID:
                futbolcu_bilgisi.update({"Gol-Prim":golSayisi_prim})
        for fut_bilgi in bilgiler[ID].keys():
            print("{} -> {}".format(fut_bilgi, bilgiler[ID][fut_bilgi]))"""