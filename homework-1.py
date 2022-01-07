from natsort import natsorted

"""Soru1: Bir metnin uzunluğunu hesaplamak için bir Python programı yazınız. ipucu Len fonksiyonu """


def soru1():
    metin = input("Metin Giriniz:")
    print(len(metin))


"""Soru2: Kullanıcı tarafından girilen bir metnin ilk iki ve son iki karakterini ekrana yazdıran Python programını 
yazınız. """


def soru2():
    metin = input("Metin Giriniz:")
    print('metin:' + metin)
    print('ilk iki karakter:' + metin[:2] + 'son iki karakter:' + metin[-2:])


"""Soru3: Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak girilen metin üzerinden değişikliği yapıp 
sonucu ekrana yazdıran Python programını yazınız. """


def soru3():
    metin = input('metin giriniz:')
    eski_harf = input('Değiştirmek istediğiniz harfi giriniz:')
    yeni_harf = input('Yeni harfi giriniz:')
    yeni_metin = metin.replace(eski_harf, yeni_harf)
    print(yeni_metin)


"""Soru4: Kullanıcı tarafından girilen bir kelimenin palindrom olup olmadığını karşılaştırma operatöründen faydalanarak 
print() fonksiyonu ile ekrana yazdırınız. """


def soru4():
    kelime = input('Bir kelime giriniz : ')
    ters = kelime[::-1]
    print('Girilen kelime = %s' % (kelime), '\n', 'Girilen kelimenin tersi = %s' % (ters))
    if ters == kelime:
        print('Girilen kelime palindrome.')
    else:
        print('Girilen kelime palindrome değil.')


"""Soru5: Girilen bir metnin son 2 karakterini 4 defa çoğaltarak ekrana yazan Python programını yazınız. * aritmetik 
operatöründen faydalanabilirsiniz. """


def soru5():
    metin = input('Bir metin giriniz:')
    a = metin[-2:]
    print(a * 4)


"""Soru6: 5 elemanlı bir liste oluşturunuz. Bu liste içerisindeki 2. elemanı 100 ile değiştiren python kodu 
yazınız. """


def soru6():
    liste = [1, 2, 3, 4, 5]
    liste[1] = 100
    print(liste)


"""Soru7: İki farklı listede tutulan verileri tek bir listede sırasıyla append,extend metodlarıyla ve "+" operatörü ile 
birleştiren python kodunu yazınız liste1 = [1,2,3] liste2 = [4,5,6] liste3 = ????? """


def soru7():
    liste1 = [1, 2, 3]
    liste2 = [4, 5, 6]
    liste3 = []

    # append
    for i in liste1:
        liste3.append(i)
    for i in liste2:
        liste3.append(i)
    print('append ile:', liste3)

    liste1 = [1, 2, 3]
    liste2 = [4, 5, 6]
    liste3 = []

    # extend
    liste3.extend(liste1)
    liste3.extend(liste2)
    print('extend ile:', liste3)

    liste1 = [1, 2, 3]
    liste2 = [4, 5, 6]
    liste3 = []

    # + ile
    liste3 = liste1 + liste2
    print('+ ile:', liste3)


"""Soru8: Oluşturduğunuz 3 elemanlı bir liste içerisine ilk sıraya "Elma" kelimesini ekleyiniz. """


def soru8():
    liste = ['kiraz', 'portakal', 'üzüm']
    liste.insert(0, 'elma')
    print(liste)


"""Soru9: liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23] yukarıdaki listeden ilk 3 sayısını silip ekrana yazdırınız. """


def soru9():
    liste = [1, 2, 3, 4, 5, 6, 7, 1, 3, 3, 3, 2, 2, 1, 23]
    del liste[:3]
    print(liste)


"""Soru10: liste1 = ["1",1,2,"3"] Yukarıdaki listenin bir kopyasını alarak 250 sayısını listenin sonuna ekleyiniz,
her iki listeyi ekrana yazdırınız. Beklenen Çıktı: ["1",1,2,"3"] => Liste1 Çıktısı ["1",1,2,"3",250] => Liste2 
Çıktısı """


def soru10():
    liste1 = ["1", 1, 2, "3"]
    liste2 = liste1.copy()
    liste2.append(250)
    print('Liste 1:', liste1, '\n', 'Liste 2:', liste2)


"""Soru11: Aşağıdaki üç farklı sözlüğü tek sözlükte birleştiren python kodunu yazınız dict1={1:10, 2:20} dict2={3:30, 
4:40} dict3={5:50,6:60} Beklenen Çıktı : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} """


def soru11():
    dict1 = {1: 10, 2: 20}
    dict2 = {3: 30, 4: 40}
    dict3 = {5: 50, 6: 60}
    d = {**dict1, **dict2, **dict3}
    print(d)


"""Soru12: sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} Sözlükteki en son elemanı silerek ekrana işlem sonucunu 
yazdırınız Beklenen Çıktı :(6,60) """


def soru12():
    sozluk = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    print(list(sozluk.items())[-1])
    sozluk.popitem()
    print(sozluk)


"""Soru13: dict1={1:10, 2:20} Yukarıdaki sözlüğe bir eleman ekleyiniz. Beklenen Çıktı :{1:10, 2:20, 3:30} """


def soru13():
    dict1 = {1: 10, 2: 20}
    dict1["3"] = "30"
    print(dict1)


"""Soru14: liste=[1,2,3,4,5] a.Yukarıdaki listeden faydalanarak bir sözlük oluşturun b.sözlüğün her alamanının karşılığına 
değer olarak anahtarda bulunan sayısal değerin 10 katını eşitleyin. Beklenen Çıktı : a. {1:0,2:0,3:0,4:0,
5:0} b. {1:10,2:20,3:30,4:40,5:50} """


def soru14():
    liste = [1, 2, 3, 4, 5]
    # a
    dictionary = dict((k, 0) for k in liste)
    print(dictionary)
    # b
    dictionary2 = dict((k, k * 10) for k in liste)
    print(dictionary2)


"""Soru15: sozluk={1:10,2:20,3:30,4:40,5:50} Sözlük içerisine 6 sayısını anahtar olarak değeri 60 olacak şekilde setdefault 
fonksiyonunu kullanarak ekleyiniz """


def soru15():
    sozluk = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    sozluk.setdefault(6, 60)
    print(sozluk)


"""Soru16: 8 sayısı girildiğinde yukarıdaki çıktıyı veren python programını 0 dan 9 a kadar olan sayılar için yazalım"""


def soru16():
    """liste = [126, 48, 109, 121, 51, 91, 95, 112, 127, 123]
    bin_list = []
    for num in liste:
        num = bin(num).replace("0b", "")
        num = num.zfill(8)
        bin_list.append(num)
    print(bin_list)"""

    for i in range(0, 10):
        x = str(i)
        n = 2
        l = lambda s: "".join(s) + "\n"
        h = lambda s: s.replace(*"! ") * ~-n + s.replace(*"!*")
        print(l(" " + "* "[c in "14"] * n + " " for c in x) + h(
            l("* "[c in "1237"] + n * "! "[c in "017"] + "* "[c in "56"] for c in x)) + h(
            l(" *"[c in "0268"] + n * "! "[c in "1479"] + "* "[c == "2"] for c in x)))


"""Soru17: Bir listeyi bir sözlükte sıralamak için bir Python programı yazın 
Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} """


def soru17():
    liste = ['n1', [2, 3, 1], 'n2', [5, 1, 2], 'n3', [3, 2, 4]]
    dictionary = {liste[i]: liste[i + 1] for i in range(0, len(liste), 2)}
    print(dictionary)


"""Soru18: sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen python kodu yazınız. """


def soru18():
    sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
    for kelime in sozluk.fromkeys(sozluk):
        temp = kelime.replace(" ", "")
        sozluk[temp] = sozluk.pop(kelime)
    print(sozluk)


"""Soru19: liste1=[1,2,3] liste2=[4,5,6,7,8] iki listeyi liste3 ile birleştiriniz? """


def soru19():
    liste1 = [1, 2, 3]
    liste2 = [4, 5, 6, 7, 8]

    liste3 = liste1 + liste2
    print(liste3)


"""Soru20: liste=[1,2,3,4,5,6] listesindeki 1. elemanı del komutu ile siliniz?"""


def soru20():
    liste = [1, 2, 3, 4, 5, 6]
    del liste[1]
    print(liste)


"""Soru21: liste=["elma" , "armut", "çilek"] listesine append komutu ile sona 3 elemanını ekleyiniz? """


def soru21():
    liste = ["elma", "armut", "çilek"]
    liste.append('3')
    print(liste)


"""Soru22: Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız"""


def soru22():
    i = 0
    num_list = []
    while i <= 10:
        a = input("10 tane sayı girin:")
        num_list.append(a)
        i += 1
    a = natsorted(num_list, reverse=True)
    print("En büyük 3 sayı:", a[:3])


"""Soru23: Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız."""


def soru23():
    metin = input("Metin Giriniz:")
    buyuk_harf_liste = []
    kucuk_harf_liste = []
    for harf in metin:
        if 'A' <= harf <= 'Z':
            buyuk_harf_liste.append(harf)
        else:
            kucuk_harf_liste.append(harf)
    print(' Büyük Harfler:', buyuk_harf_liste, '\n', 'Küçük Harfler:', kucuk_harf_liste)


"""Soru24: kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını ekrana yazdıran programı yazınız. """


def soru24():
    tek_count = 0
    cift_count = 0
    i = 0
    num_list = []
    while i <= 9:
        a = input("10 tane sayı girin:")
        num_list.append(a)
        i += 1
    print(num_list)

    for num in num_list:
        if int(num) % 2 == 0:
            cift_count += 1
        else:
            tek_count += 1

    print("Girilen 10 sayıdan", cift_count, "tanesi çifttir.")
    print("Girilen 10 sayıdan", tek_count, "tanesi tektir.")
