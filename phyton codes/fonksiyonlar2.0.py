import  random 
import string
from math import pow
from math import pi
class zam():
 def zamyap(self,deger):
        return deger+((deger*20)/100)

newword= "levent elçiçek"

# substring fonksiyonu
#-----------------------
secondword= newword[5:10]
#-----------------------

print(str(secondword))

# uzunluk fonksiyonu(lenght)
#------------------
print(str(len(newword)))
#-------------------

# tuple list değeri değiştirilemez değerler için kullanılır 
#-----------------------
tupleListe =(6,57,55,"elçiçek",("l",7))
#---------------------- 

liste=[1,7,8,"leben",[1,2]]
liste[0]="melek"
print(tupleListe[2:2])
print(liste[2:2])


# dictionary kullanımı
#--------------------------
sözlük={"book": "kitap","pancel":"kalem"}
sözlük["book"]= ["defter"]
sözlük["name"]=["isim"]
print(sözlük["name"])

#--------------------------

#replace ( değiştirme fonksiyonu)
#-----------------
isim="elçiçek"
isim=isim.replace("e","i")
print(str(isim))
#--------------------

# split( bölme fonksiyonu)
#-----------------
isim2= "levent elçiçek 76543 gunduzA"
isim2= isim2.split(" ")
print(isim2)
#----------------

#strip(baş ve sondaki boşlukları kaldırma metodu)
#--------------------
isim3="    levent   ".strip()
print(str(isim3))
#-------------------

#Apped(diziye eleman ekleme metodu)ve remove ("  " silme metodu)
#----------------
dizi=["levent","melek","ali","levent"]
dizi.append("metin")
dizi.remove("levent")
print(dizi)
#---------------

# insert(istenilen indexe eleman ekleme metodu)
#-------------
dizi4=["melek","aysel","selma"]
dizi4.insert(2,"alican")
print(dizi4)
#-------------

# count (istenilen elemandan kaçtane olduğunu döndüren fonksiyon)
#-----------------
dizi2=[1,4,9,2,5,9,9,4,2,81,64,]
print(dizi2.count(9))
#----------------

# pop (istenilen indexteki değeri silen fonksiyon)
#-----------------
dizi3=["saffet","zeynel","sevgi"]
dizi3.pop(1)
print(dizi3)
#-----------------

#reverse (ters çevirme metodu)(metod önce uygulanır ,sonra print edilir)
#----------------
dizi5=["ali","veli","deli"]
dizi5.reverse()
print(dizi5)
#---------------

# extend(2 diziyi birbirine ekleme metodu)
#-------------------
dizi6=["a","b","c"]
dizi7=["d","e","f"]
dizi6.extend(dizi7)
print(dizi6)
#------------------

# random sayı üretme metodu
#----------------
rastgele=random.randint(1,3)
#----------------

# del(diziden index silme metodu)
#-------------------
sayılar=[1,2,3,4,5,6]
del sayılar[2]
print(sayılar)
#-------------------

# Dosya oluşturma ,açma ,kapama işlemleri
#----------------------
file1= open("levent.txt","a")
dosyasayısı=89
file1.write("phyton dosyaları"+"\n")
file1.write(str(dosyasayısı)+"\n"+str(sayılar))
file1.close()
#---------------------

# bir dizinn içini for döngüsüyle doldurma olayı
#--------------------------
file1=open("levent.txt","w")
isimler=["levent","melek","saffet","zeynel","metin"]
sayılar=[random.randint(10,100) for i in range(5)]
for k in range(5):
 file1.write(isimler[k]+"-"+str(sayılar[k])+"\n")
file1.close()
#--------------------------

# sep anahtar sözcüğü 
#-------------------
print("a","b","c",sep='\t',end="\n -----123----\n")
#---------------------

#stringlerin karar yapısıyla kartşılaştırılmasında
#hangi harf alfabede daha sonra geliyor ise o daha büyüktür
#aynı harften küçük(lower case)olan,
#büyük olandan(upper case) den ascıı tablo gereği daha büyüktür
#--------------------------
levent="levent"
Levent="Levent"

if levent>Levent:
 print(str("Levent  >  elçiçek"))
else:
 print(str(" tam tersi"))
#---------------------------

# map fonksiyonu bir listenin 
# tüm elemanları üzerinde işlem yapılacaksa kullanılır
#---------------------------
zamlımaas= zam()
maas=[100,200,300,400,500]
yenimaas=list(map(zamlımaas.zamyap,maas))
print(yenimaas)
#---------------------------

# zip fonksiyonu 2 listenin elemanlarını karşılıklı olarak
#sıraile birleştirmeyi sağlar
#----------------------------
personeller=["levent","saffet","zeynel","melek","alican"]
sonuclistesi=list(zip(personeller,maas))
print(sonuclistesi)

yarıcap=int (input("alan giriniz"))
sonuc=0
if yarıcap>=0:
 sonuc= pi*pow(yarıcap,2) 
print (str(sonuc))

#sum(liste elemanmları toplamı) fonksiyonu
#---------------------
sayılistesi=[10,20,30,40,50]
listetopamı= sum( sayılistesi)
print(str(listetopamı))
#---------------------

# abs(mutlak değer) fonksiyonu
#------------------------
negative= -67
print(int(abs(negative)))
#-------------------------

#for döngüsü kullanmadan " * " operatoru ile isim yazdırma
#---------------------
isim=input("isim giriniz")
print((isim+"\n")*10)
#---------------------




