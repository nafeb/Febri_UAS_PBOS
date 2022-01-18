kalkulator = []

def tambah_angka() :
    x = int(input("Angka 1 : "))
    y = int(input("Angka 2 : "))
    tambah = x + y
    print(tambah)

def kurang_angka() :
    x = int(input("Angka 1 : "))
    y = int(input("Angka 2 :"))
    kurang = x - y
    print(kurang)

def kali_angka():
    x = int(input("Angka 1 : "))
    y = int(input("Angka 2 :"))
    kali = x * y
    print(kali)

def bagi_angka():
    x = int(input("Angka 1 : "))
    y = int(input("Angka 2 : "))
    bagi = x / y
    print(bagi)

def hitungan_menu():
    print("\n")
    print("[1] tambah")
    print("[2] kurang")
    print("[3] kali")
    print("[4] bagi")
    menu = input("Pilih perhitungan> ")
    print("\n")
    if menu == "1" :
        tambah_angka()
    elif menu == "2" :
        kurang_angka()
    elif menu == "3" :
        kali_angka()
    elif menu == "4":
        bagi_angka()
    else:
        exit()

if _name== "main_":
    while(True) :
        hitungan_menu()