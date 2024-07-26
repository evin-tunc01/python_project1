def topla(x,y):
    return x+y
def çıkar(x,y):
    return x-y
def çarp(x,y):
    return x*y
def böl (x,y):
    return x/y
    
print("Lütfen yapmak istediğiniz işlemi seçiniz.")
print("1.Toplama")
print("2.çıkarma")
print("3.çarpma")
print("4.bölme")

secim=input("seçiminiz (1/2/3/4):")

sayi1=float(input("ilk sayıyı giriniz:"))
sayi2=float(input("ikinci sayıyı giriniz:"))

if secim=="1":
    print(sayi1,"+",sayi2,"=",topla(sayi1,sayi2))
elif secim=="2":
    print(sayi1,"-",sayi2,"=",çıkar(sayi1,sayi2))
elif secim=="3":
    print(sayi1,"*",sayi2,"=",çarp(sayi1,sayi2))
elif secim=="4":
    if sayi2==0:
        print("bir sayı sıfıra bölünmez")
    else:
        print(sayi1,"/",sayi2,"=",çarp(sayi1,sayi2))
else:
    print("GEÇERSİZ SEÇİM")
    