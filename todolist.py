to_do_list=[]
 #kullanıcıda aldığımız verileri listeyen ekliyen fonksiyon 
def add_task(to_do_list):
     task=input("yapılacak görevi girin:")
     to_do_list.append(task)
     print("görev başarıyka eklendi.")
#listede bulunan görevleri gösteren fonksiyon
def show_tasks(to_do_list):
    print("yapılacak görevler:")
for tasks in to_do_list:
    print("-"+task)
#listeden görev silen fonksiyon 
def delete_task(to_do_list):
    print("silmek istediğiniz görevi girin:")
    if task in to_do_list:
        to_do_list.remove(task)
        print("görev başarıyla silindi.")
    else:
        print("görev bulunamadı.")
#Ana döngü
while True:
 print("\nTo-do list uygulaması")
 print("1.görev ekle")
 print("2.görevleri göster")
 print("3.görev sil ")
 print("4.çıkış")
 choice=input("seçiminizi yapınız(1/2/3/4):")
 
 if choice=="1":
     add_task(to_do_list)
 elif choice=="2":
     show_tasks(to_do_list)
 elif choice=="3":
     delete_task(to_do_list)
 elif choice=="4":
    print("uygulamadan çıkılıyor...")
    break
 else:
    print("Geçersiz seçim.Lütfen tekrar deneyin.")
    
    
    