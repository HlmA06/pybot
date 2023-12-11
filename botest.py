import sqlite3
import json
import os
import random
from datetime import datetime
import requests
from colorama import Fore, Style

# Veritabanı bağlantısı oluşturma
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Kullanıcı tablosunu oluşturma
cursor.execute('''
    CREATE TABLE IF NOT EXISTS kelimeler (
        kelime TEXT PRIMARY KEY,
        anlam TEXT
    )
''')
connection.commit()

print("Created By Hilmi")

# Espri verilerini saklamak için JSON dosyasını kontrol et
espri_json_yolu = "data2.json"
if not os.path.exists(espri_json_yolu):
    # Eğer dosya yoksa örnek espri ekleyelim
    espri_verileri = {"espriler": [
        "Data1",

        # İsterseniz daha fazla espri ekleyebilirsiniz.
    ]}
    with open(espri_json_yolu, "w") as espri_json_file:
        json.dump(espri_verileri, espri_json_file)

# JSON dosyasından espri verilerini okuma
with open(espri_json_yolu, "r") as espri_json_file:
    espri_verileri = json.load(espri_json_file)

espriler_listesi = espri_verileri["espriler"]

def kelime_ogren(kelime):
    cursor.execute('SELECT * FROM kelimeler WHERE kelime=?', (kelime.lower(),))
    result = cursor.fetchone()

    if result:
        return result[1]
    else:
        yeni_anlam = input(f"{kelime} Lütfen öğretin: ")
        cursor.execute('INSERT INTO kelimeler VALUES (?, ?)', (kelime.lower(), yeni_anlam))
        connection.commit()
        return f"{kelime} Anlam öğrenildi."

def kelime_listele():
    cursor.execute('SELECT kelime, anlam FROM kelimeler')
    kelimeler = cursor.fetchall()

    if kelimeler:
        print("Kelime Listesi:")
        for kelime, anlam in kelimeler:
            print(f"{kelime}: {anlam}")
    else:
        print("Veritabanında henüz kelime bulunmamaktadır.")

def kelime_duzenle(kelime):
    yeni_anlam = input(f"{kelime} Yeni anlamını yazın: ")
    cursor.execute('UPDATE kelimeler SET anlam=? WHERE kelime=?', (yeni_anlam, kelime.lower()))
    connection.commit()
    print(f"{kelime} Anlamı güncellendi.")

def kelime_sil(kelime):
    cursor.execute('DELETE FROM kelimeler WHERE kelime=?', (kelime.lower(),))
    connection.commit()
    print(f"{kelime} Kelimesi ve anlamı silindi.")

def espri_yap():
    if espriler_listesi:
        espri = random.choice(espriler_listesi)
        print(Fore.GREEN + f"Data: {espri}" + Style.RESET_ALL)
    else:
        print("Espri verisi bulunmamaktadır.")

def saat_sorgula():
    su_an = datetime.now()
    saat = su_an.strftime("%H:%M")
    print(Fore.CYAN + f"Şu anki saat: {saat}" + Style.RESET_ALL)

def hava_durumu_sorgula(sehir, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": sehir, "appid": api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            hava_durumu_bilgisi = data["weather"][0]["description"]
            return f"{sehir} hava durumu: {hava_durumu_bilgisi}"
        else:
            return "Hava durumu bilgisi alınamadı."
    except Exception as e:
        return f"Hata oluştu: {e}"

def hava_durumu_kontrol(api_key):
    sehir = input(Fore.CYAN + "Hangi şehirin hava durumunu öğrenmek istersiniz? " + Style.RESET_ALL).capitalize()
    hava_durumu_bilgisi = hava_durumu_sorgula(sehir, api_key)
    print(hava_durumu_bilgisi)

def hesap_makinesi():
    try:
        sayi1 = float(input("İlk sayıyı girin: "))
        operator = input("İşlemi girin (+, -, *, /): ")
        sayi2 = float(input("İkinci sayıyı girin: "))

        if operator == '+':
            sonuc = sayi1 + sayi2
        elif operator == '-':
            sonuc = sayi1 - sayi2
        elif operator == '*':
            sonuc = sayi1 * sayi2
        elif operator == '/':
            sonuc = sayi1 / sayi2
        else:
            print("Geçersiz operatör.")
            return

        print(Fore.MAGENTA + f"Sonuç: {sonuc}" + Style.RESET_ALL)
    except ValueError:
        print("Geçersiz sayı formatı.")
    except ZeroDivisionError:
        print("Sıfıra bölme hatası.")

# API anahtarını elle ekleyin
api_key = "b43c9d9893247c6dccfe5b4c9606cb00"

while True:
    giris = input("Bir şeyler yazın: ").lower()

    if giris == 'exit':
        break
    elif giris == '/list':
        kelime_listele()
    elif giris == 'help':
    	print("eklenecek")
    elif giris.startswith('/edit '):
        kelime_duzenle(giris[6:])
    elif giris.startswith('/delete '):
        kelime_sil(giris[8:])
    elif giris == 'data2':
        espri_yap()
    elif giris == 'saat':
        saat_sorgula()
    elif giris == 'hava durumu':
        hava_durumu_kontrol(api_key)
    elif giris == 'hesap':
        hesap_makinesi()
    else:
        cevap = kelime_ogren(giris)
        print(cevap)

# Veritabanı bağlantısını kapat
connection.close()