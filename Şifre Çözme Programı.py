import os
import sys
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

from colorama import init
from colorama import Fore, Back, Style #Renk kütüphanemizdeki Fore , Back , Style komutlarını seçiyoruz.
init()

#The previous key of the key we set here must achieve the same success or the encryption will not work.

KEYFILE = "rimtay.key" #Burada Belirlediğimiz keyin önceki keyle aynı olmasına dikkat etmeliyiz yoksa şifreleme çalışmaz.

RUN = True #Hata raporlarının kodunu daha kısa tutmak için bir değişken belirliyoruz.


def decrypt(filename): #Yine fonksiyonumuzu kullanıyoruz.
    if (os.path.exists(filename) == True):
        new_name = filename.rstrip("_rimenc")
        os.rename(filename, new_name)
        file = open(new_name, "rb+")
        data = file.read() #Veri değişkenini yine belirliyoruzki içinde birşey olmayan dosyalarda hata dönütü verebilelim.
        file.close()
        # file.close()
        if (len(data) > 0): #Dosyaların içinde bir veri var ise şifrelemeye başlıyoruz.
            fernet = Fernet(key)
            try:
                decrypted = fernet.decrypt(data)
            except InvalidToken:
                print(Fore.RED) #Yazımızı kırmızı yapıyoruz #Articele color select red

                print("FAILED '" + filename + "' could not decrypted because key invalid")
                #Burada keyde hata varsa diye bir dönüt yazıyoruz.
                #Here we write a feedback saying that there is an error in the key.
                print("HATA '" + filename + "' belirttiğiniz key bulunamadı!")

                print(Fore.WHITE) #articel color select white
                os.rename(new_name, filename)
            except TypeError: #Stilde bir sorun varsa diye yine bir dönüt ekliyoruz.
                print(Fore.RED) #Yazı rengini kırmızı yapıyoruz
                print("FAILED '" + filename + "' could not decrypted because the data is not binary")
                print("HATA '" + filename + "' dosyaların ikili diziliminde bir sorun var.")
                print(Fore.WHITE)#Yazı rengini eski hale yani beyaz haline geri getiriyoruz.
                os.rename(new_name, filename)
            else:
                file = open(new_name, "wb")
                change = file.write(decrypted)
                file.close() #Dosyalarımızın işlemlerini bitiriyoruz
                print(Fore.GREEN)#Yazı rengimizi Yeşil yapıyoruz // Write color is green
                print("SUCCESS '" + filename + "' has decrypted and renamed as '" + new_name + "'")
                print("Başarılı '" + filename + "' şifre çözme işlemi başarılı '" + new_name + "'")
                print(Fore.WHITE)#Yazı rengimizi tekrardan beyaz yapıyoruz.
        else:
            print("WARNING '" + filename + "' could not decrypted because it's empty")


if os.path.exists(KEYFILE) == False:
    print("Encryption Key is not found! System will not work!") #Burada key bulunamassa diye bir hata raporu yazıyoruz.
    print("Şifreleme anahtarı bulunamadı! Sistem çalışmayı durdurdu!!") #Burada key bulunamassa diye bir hata raporu yazıyoruz.
    RUN = False #En başta belirlediğimiz run değişkenini kullanarak sistemi durduruyoruz
else:
    file = open(KEYFILE, "rb")
    key = file.read()
    print("Encryption Key File found on the system.") #burada ise anahtarın ne olduğunu tekrardan hatırlatıyoruz.
    file.close()
if (RUN):
    print("Encryption Key: " + str(key)) #Run değişkenimizi tekrardan kullanarak şifreleme anahtarını terminale yazıyoruz.
    print("Şifreleme anahtarı :" + str(key)) #run variable again, we write the encryption key to the terminal.

    for root, dirs, files in os.walk("."):
        for filename in files:
            # name,extension = os.path.splitext(filename)
            # extension = extension.lower()
            parts = filename.split("_")

            if (parts[-1] == "rimenc"):
                decrypt(filename)
            # print(filename)
    print("\n\nPress enter to exit!")
    wait = input()

    #By Alperen Türk