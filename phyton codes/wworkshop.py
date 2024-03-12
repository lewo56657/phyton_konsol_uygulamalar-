import random
import string
 
isimler =["levent","zeynel","saffet"]
hediyeler =["leptop","tablet","telefon"]

eşleşme1=random.choice(hediyeler)
print(f"{isimler[0]} :{eşleşme1} kazandı")
hediyeler.remove(eşleşme1)

eşleşme2=random.choice(hediyeler)
print(f"{isimler[1]} :{eşleşme2} kazandı")

hediyeler.remove(eşleşme2)

eşleşme3=random.choice(hediyeler)
print(f"{isimler[2]} :{eşleşme3} kazandı")

hediyeler.remove(eşleşme3)

#-----------------------------

starcount=int(input("yıldız sayısını giriniz"))

for i in range(starcount):
     print(" "*((starcount-1)-i), end="")
     for j in range(i*2+1):

        print("*",end="")
     print()

#----------------------------------

sayılar=string.digits
karakterler=string.punctuation
buyuk_harfler=string.ascii_uppercase
kucuk_harfler= string.ascii_lowercase
sifre=""
degerler=[sayılar,karakterler,buyuk_harfler,kucuk_harfler]
for i in range(4):
  for j in range(2):
    sifre= sifre+degerler[i][random.randint(0,9)]

yeni_sifre= ""

sifre=list(sifre)

random.shuffle(sifre)

for k in sifre:
    yeni_sifre=yeni_sifre+k

print(yeni_sifre)    
#-----------------------
file3= open("file3.txt","w")
   
for i in range(50):
  file3.write(str(random.randrange(0,48))+"-"+str(random.randint(0,15)) +"\n")
 
file3.close()
try:
 file3= open("file3.txt","r")
   
 for i in file3:
    yeni1=i.strip()
    yeni1= yeni1.split("-")
    print( " pay :",str(yeni1[0])," payda :",str(yeni1[1]))   
    print(" bolüm sonuxcu",int(yeni1[0])/int(yeni1[1]))  
     
 file3.close()
except FileNotFoundError  as  x:
 print(x)
except IndexError as y:
   print(str(y))
except ValueError as z:
   print(str(z))
except ZeroDivisionError as j :
   print("0 a bolme hatası")
   #------------------------

try:
  isimler= ["levent","saffet","zeynel Abidin"]
  soyisimler= ["elçiçek","demir"," erbek"]
  kilolar=[71,99,65]
  kişiler=[isimler,soyisimler,kilolar]


  for i in range(len(kişiler)):
    for j in range(len(kişiler)):
        if  j==2:
          print("kilosu : ",(str(kişiler[j][i])))
        else:
          print(str(kişiler[j][i]), " ",end ="")
  print()
except IndexError as x:
   print(str(x))








