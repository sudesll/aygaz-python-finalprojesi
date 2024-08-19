import random

secim = ["Taş", "Kağıt", "Makas"]
kazanma_listesi = ["Gerçekten onu seçeceğini düşünmedim mi sandın..", "Bir amatör gibi oynuyorsun.",
                   "Bu hamleyi 3 tur öncesinden hesaplamıştım.", "Bir dahakine farklı bir seçim yapmayı dene.."]
kaybetme_listesi = ["Ahhhh!!", "Çok şanslısın...", "Bir dahaki sefer böyle olmayacak.", "Bu sadece bir avanstı."]


def tas_kagit_makas_yunusemretorunler_sudenazsali():
    def win_puan_bildirme():
        print("Bilgisayar düşünüyor....")
        print(f"Bilgisayar {pc_secimi} seçti.")
        print(random.choice(kaybetme_listesi))
        print(f"{oyun_sayaci}. oyun   {tur_sayaci}. tur")
        print(f"Bilgisayar:{pc_puan} Oyuncu: {oyuncu_puan}")
        print("---------------------------")

    def lose_puan_bildirme():
        print("Bilgisayar düşünüyor....")
        print(f"Bilgisayar {pc_secimi} seçti.")
        print(random.choice(kazanma_listesi))
        print(f"{oyun_sayaci}. oyun   {tur_sayaci}. tur")
        print(f"Bilgisayar:{pc_puan} Oyuncu: {oyuncu_puan}")
        print("---------------------------")

    kontrol = True
    toplam_skor = {"oyuncu": 0, "bilgisayar": 0}
    tur_sayaci = 0
    oyun_sayaci = 1
    pc_puan = 0
    oyuncu_puan = 0

    print("Bugün seninle taş kağıt makas oyamak istiyorum. \nOyunun kuralları basit.. "
          "\nKağıt taşı sarar, Taş makası kırar, makas kağıdı keser.")

    while kontrol:
        while oyuncu_puan < 3 and pc_puan < 3:
            oyuncu_secimi = input("Seçim sırası sende. Taş, Kağıt, Makas ya da oynamak istemezsen "
                                  "çıkış yazabilirsin:").title()
            pc_secimi = random.choice(secim)

            if oyuncu_secimi not in secim + ["Çıkış"]:
                print("Yanlış komut girdiniz.")
                print("---------------------------")
                continue
            if oyuncu_secimi == "Çıkış":
                print("Korktun değil mi?")
                kontrol = False
                break
            if oyuncu_secimi == pc_secimi:
                tur_sayaci += 1
                print(f"İki oyuncu da {oyuncu_secimi} seçti. Berabere!!!")
                print(f"{oyun_sayaci}. oyun   {tur_sayaci}. tur")
                print(f"Bilgisayar:{pc_puan} Oyuncu: {oyuncu_puan}")
                print("---------------------------")
            elif oyuncu_secimi == "Taş":
                if pc_secimi == "Makas":
                    tur_sayaci += 1
                    oyuncu_puan += 1
                    win_puan_bildirme()
                else:
                    tur_sayaci += 1
                    pc_puan += 1
                    lose_puan_bildirme()
            elif oyuncu_secimi == "Kağıt":
                if pc_secimi == "Taş":
                    tur_sayaci += 1
                    oyuncu_puan += 1
                    win_puan_bildirme()
                else:
                    tur_sayaci += 1
                    pc_puan += 1
                    lose_puan_bildirme()
            elif oyuncu_secimi == "Makas":
                if pc_secimi == "Kağıt":
                    tur_sayaci += 1
                    oyuncu_puan += 1
                    win_puan_bildirme()
                else:
                    tur_sayaci += 1
                    pc_puan += 1
                    lose_puan_bildirme()
        if oyuncu_puan == 3:
            toplam_skor["oyuncu"] += 1
            print("Tebrikler! Oyunu kazandınız.")
        elif pc_puan == 3:
            toplam_skor["bilgisayar"] += 1
            print("Bilgisayar kazandı. Bir dahaki sefere belki de siz kazanırsınız!")

        print(f"Toplam Skor - Oyuncu: {toplam_skor['oyuncu']}, Bilgisayar: {toplam_skor['bilgisayar']}")
        while True:
            soru = input("Tekrar oynamak ister misiniz? (Evet/Hayır): ")
            if soru.title() == "Evet":
                if oyuncu_puan == 3:
                    print("Bu sefer seni alt edeceğim.")
                    print("---------------------------")
                    tur_sayaci = 0
                    oyun_sayaci += 1
                    pc_puan = 0
                    oyuncu_puan = 0
                    break
                else:
                    print("Yenilen pehlivan güreşe doymazmış. :DD")
                    print("---------------------------")
                    tur_sayaci = 0
                    oyun_sayaci += 1
                    pc_puan = 0
                    oyuncu_puan = 0
                    break
            elif soru.title() == "Hayır":
                print("Değerli zamanın için teşekkürler.")
                kontrol = False
                break
            else:
                print("Hatalı giriş yaptınız.")
                print("---------------------------")


tas_kagit_makas_yunusemretorunler_sudenazsali()
