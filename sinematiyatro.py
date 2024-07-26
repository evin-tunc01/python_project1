#kullanıcıya sinema ya da tiyatro tercihi sorulsun.Sinema izlemek için #15 TL,tiyatro için 10 TL ödenmesi gerekmektedir.
#Öğrencilere ½50 indirim yapıldığı düşünülerek öğrenci ise indirim yapılan;
#öğrenci değil ise indirimsiz tutarı hesaplayarak ekrana yazdıran kodu yazınız.
tercih=input("sinema için (1),tiyatro için (2) yi tercih ediniz:")
öğrenci=input("öğrenci misiniz e/h")
ücret=0

if tercih=="1" and öğrenci=="h":
    print("ücret=15")
elif tercih=="1" and öğrenci=="e":
    print("ücret=7.5")
elif tercih=="2" and öğrenci=="h":
    print("ücret=10")
else:
    print("ücret=5")