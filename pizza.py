
# Online Python - IDE, Editor, Compiler, Interpreter

#Müşterinin pizza siparişi için aşağıdaki boyutlara göre ücretlendirilecektir:
#Küçük boy (S) pizza: 25 TL
#Orta boy (M) pizza: 30 TL
#Büyük boy (L) pizza: 35 TL
#Eğer müşteri pizzasında extra peynir isterse pizza boyutlarına göre aşağıdaki fiyatlar eklenecektir:
#Küçük boy (S) pizzaya +2 TL
#Büyük boy (L) ve orta boy (M) pizzaya +3 TL
#Kullanıcı yanına bir de içecek alacaksa
#Pizza boyutu fark etmeksizin +2 TL

print("HOŞGELDİNİZ")
pizza_boyutu=input("Hangi boyut pizza tercih edersiniz?(S/M/L):")
extra_peynir=input("Extra peynir ister misiniz?(E/H):")
içecek_tercihi=input("İçecek ister misiniz?(E/H):")

if pizza_boyutu=="S":
     ücret=25
elif pizza_boyutu=="M":
     ücret=30
elif pizza_boyutu=="L":
     ücret=35
 #extra peynir
if extra_peynir=="E" and pizza_boyutu=="S":
     ücret=27
elif extra_peynir=="E" and pizza_boyutu=="M":
     ücret=33
elif extra_peynir=="E" and pizza_boyutu=="L":
     ücret=38
 #içecek 
if içecek_tercihi=="E":
     ücret+=2
     #hesap sonu
print("Ödemeniz gereken hesap:{}".format(ücret))    
     
     
    
    