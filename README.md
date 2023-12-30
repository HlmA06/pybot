# Basit Sohbet Botu

Bu, kullanıcının girdiği metinlere tepki verebilen, öğrenme yeteneğine sahip basit bir sohbet botu uygulamasıdır.

## Kurulum

1. Projeyi bilgisayarınıza klonlayın:

    ```bash
    git clone https://github.com/HlmA06/pybot.git
    cd pybot
    ```

2. Gerekli Python kütüphanelerini yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

## Başlarken

1. `botest.py` dosyasını çalıştırarak sohbet botunu başlatın.
2. Bot, size karşılık verecektir ve öğrenme özelliği kullanıma hazır olacaktır.

## Temel Kullanım

- **Konuşma:** Bot, kullanıcının girdiği metinlere ne cevap vereceğini öğrenir ve kaydeder.

  ```plaintext
  Kullanıcı: Nasılsın?
  Bot: Nasılsın dediğinizde ne cevap vermemi istersiniz?
  Kullanıcı: İyiyim.
  Kullanıcı: Nasılsın?
  Bot: İyiyim.
  ```

- **Kelime Listeleme:** Öğrenilen kelimeleri ve anlamlarını listeleyin.

  ```plaintext
  Kullanıcı: /list
  ```

- **Kelime Düzenleme:** Öğrenilen bir kelimenin anlamını düzenleyin.

  ```plaintext
  Kullanıcı: /edit kelime
  ```

- **Kelime Silme:** Öğrenilen bir kelimeyi veritabanından silin.

  ```plaintext
  Kullanıcı: /delete kelime
  ```

- **Espri Yapma:** Bot, önceden tanımlı espri listesinden rastgele bir espri yapar. Bu dosyaya istediğiniz bilgiyi ekleyebilirsiniz.

  ```plaintext
  Kullanıcı: data2
  ```

- **Saat Sorgulama:** Bot, şu anki saat bilgisini verir.

  ```plaintext
  Kullanıcı: saat
  ```

- **Hava Durumu Sorgulama:** Bot, bir şehirin hava durumunu sorgular.

  ```plaintext
  Kullanıcı: hava durumu
  ```

- **Hesap Makinesi:** Basit bir hesap makinesi ile matematik işlemlerini yapın.

  ```plaintext
  Kullanıcı: hesap
  ```
