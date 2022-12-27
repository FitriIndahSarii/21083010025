total = []
def welcome():
    print(' ')
    print('===================================')
    print('=== SELAMAT DATANG DI OYEN CARE ===')
    print('===================================')
    print('\n')
    print("Silahkan Login Sebagai Admin!")
    usrnm = "fitriindh"
    pw = "fitriindh"
    for i in range(3) :
        try :
            username = input("Masukkan username : ")
            password = input("Masukkan password : ")
            if len(password) < 8 :
                raise NameError
            else :
                if username == "fitriindh" and password == "fitriindh" :
                    print("Anda Berhasil Login!")
                    break
                elif password != pw :
                    print("Username atau password salah!")
        except NameError :
            print("Password minimal 8!")
            print("")
    menu()

def menu():
    print('\n===========================')
    print('[1]Produk Oyen Care')
    print('[2]Ketentuan diskon')
    print('[3]Check Out')
    print('[0]Keluar dari Oyen Care')
    print('===========================')
    pilih = input('Masukkan Nomor Pilihan Anda : ')
    if pilih == '1':
        produk()
    elif pilih == '2':
        ketentuan_diskon()
    elif pilih == '3':
        checkout()
    elif pilih == '0':
        keluar()
    else:
        print('\nAngka yang Anda masukan tidak dikenal\nAnda kami kembalikan ke menu utama\n')
        menu()

def produk():
    print('\n=====\t     PRODUK OYEN CARE^^\t       =====')
    print('1. Makanan\t\t\t: Rp. 30000')
    print('2. Kandang\t\t\t: Rp. 100000')
    print('3. Tempat makan dan minum\t: Rp. 30000')
    print('4. Litter box dan serokan\t: Rp. 20000')
    print('5. Pasir kucing\t\t\t: Rp. 15000')
    print('6. Sisir bulu\t\t\t: Rp. 5000')
    print('7. Lint rolling\t\t\t: Rp. 10000')
    print('8. Shampoo\t\t\t: Rp. 20000')
    print('============================================')
    back_to_menu()

def ketentuan_diskon():
    print('\n====   !! Ketentuan Diskon Oyen Care !!   ====')
    print('1. Diskon 10% jika membeli minimal Rp. 100000')
    print('2. Diskon 15% jika membeli minimal Rp. 200000')
    print('3. Diskon 25% jika membeli minimal Rp. 300000')
    print('4. Diskon 50% jika membeli minimal Rp. 500000')
    print('==============================================')
    back_to_menu()

def checkout():
    print('\nBarang apa yang ingin anda beli?')
    print('1. Makanan')
    print('2. Kandang')
    print('3. Tempat makan dan minum')
    print('4. Litter box dan serokan')
    print('5. Pasir kucing')
    print('6. Sisir bulu')
    print('7. Lint rolling')
    print('8. Shampoo')
    print('\n')
    kode = input("Masukkan nomor barang : ")
    if kode == '1':
        jumlah1=int(input("Masukkan jumlah barang : "))
        total1=30000*jumlah1
        total.append(total1)
        tanya()
    elif kode == '2':
        jumlah2=int(input("Masukkan jumlah barang : "))
        total2=100000*jumlah2
        total.append(total2)
        tanya()
    elif kode == '3':
        jumlah3=int(input("Masukkan jumlah barang : "))
        total3=30000*jumlah3
        total.append(total3)
        tanya()
    elif kode == '4':
        jumlah4=int(input("Masukkan jumlah barang : "))
        total4=20000*jumlah4
        total.append(total4)
        tanya()
    elif kode == '5':
        jumlah5=int(input("Masukkan jumlah barang : "))
        total5=15000*jumlah5
        total.append(total5)
        tanya()
    elif kode == '6':
        jumlah6=int(input("Masukkan jumlah barang : "))
        total6=5000*jumlah6
        total.append(total6)
        tanya()
    elif kode == '7':
        jumlah7=int(input("Masukkan jumlah barang : "))
        total7=10000*jumlah7
        total.append(total7)
        tanya()
    elif kode == '8':
        jumlah8=int(input("Masukkan jumlah barang : "))
        total8=20000*jumlah8
        total.append(total8)
        tanya()
    return

def tanya():
    print("\n")
    tanya = input("Ingin tambah barang? [y/t] : ")
    if(tanya=="y"):
        checkout()
    elif(tanya=="t"):
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")
    
def akhir():
    for harga in total:
        diskon=0
        a=sum(total)
        if(a>=500000):
            diskon=a*50/100
        elif(a>=300000):
            diskon=a*25/100
        elif(a>=200000):
            diskon=a*15/100
        elif(a>=100000):
            diskon=a*10/100
        else:
            diskon=0
        totalakhir=a-diskon
    
    print("\n==============================================")
    print("                  KWITANSI                  ")
    print("==============================================")
    print("Harga sebelum diskon\t : Rp. ",sum(total))
    print("Total diskon\t\t : Rp. ",diskon)
    print("Harga yang harus dibayar : Rp. ",totalakhir)
    print("==============================================")
    print(" Terima Kasih Sudah Berbelanja di Oyen Care>< ")
    print("==============================================")
    print(" ")
    exit = input('Apakah Anda ingin berbelanja lagi? (y/n) : ')
    if exit == 'y':
        welcome()
    elif exit == 'n':
        keluar()
    else:
        keluar()

def back_to_menu():
    pilih = input('Apakah Anda ingin kembali ke menu utama? (y/n) : ')
    if pilih == 'y':
        menu()
    elif pilih == 'n':
        print('Anda keluar dari Oyen Care huhu')
        keluar()
    else:
        print('Anda memasukkan nilai yang salah! Harap masukkan kembali')
        back_to_menu()

def keluar():
    exit()

welcome()