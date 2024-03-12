import random
import itertools
şifre_dosyası=open("şifre_dosyası.txt","w")

dizi=["a","y","z","x","l","m","f","n"]
boş_liste1=[]
boş_list2=[]

boş_string2=" "
sayac=1

boş_liste1=list(itertools.permutations(dizi,6))
for k in boş_liste1: 
  for m in k:
     boş_string2=boş_string2 +m
  şifre_dosyası.write(str(boş_string2)+"\n") 
  boş_string2=" "

şifre_dosyası.close()
     

   





     
