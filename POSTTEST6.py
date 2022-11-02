# Code dibawah adalah untuk memanggil package
# package disini adalah sebuah fungsi yg disediakan oleh python sendiri
# atau kita harus install terlebih dahulu packagenya
import os
import time # package untuk time diantaranya time.sleep untuk delay
from pyfiglet import Figlet # package untuk style text
from prettytable import PrettyTable

# user, login dan user_tetap disini
# bisa dibilang sebagai temporary database untuk proses register dan login
user = {
    "id" : "",
    "pass" : "",
}
login = {
  "id" : "",
  "pass" : "",
}
user_tetap = {
    "id" : "admin",
    "pass" : "0987",
}

menu_awal = True # Global variabel
menu_menantea = [] # Global variabel, variabel ini digunakan untuk menyimpan data menu yg di tambahkan pada 
pembelian = [] # Global variabel, variabel ini digunakan untuk menyimpan data pembelian

# Fungsi untuk register
# ketika user memilih register pada menu awal
# maka fungsi ini dijalankan
def register():
    print("Masukkan ID dan Password Pengguna Baru")
    while True:
        try:
            user["id"] = str(input("Masukkan ID Pengguna berupa karakter bukan angka : "))
            user["pass"] = str(input("Masukkan Password berupa angka : "))
        except ValueError:
            print("Tolong input ID atau Password dengan benar")
        else:
            print("Berhasil Register")
            break
    kembali = input("Kembali ke menu awal? (y/n) = ")
    if kembali == "y":
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        menu()
    else:
        register()
    print(50*"=")

# Fungsi untuk Login
# ketika user memilih login pada menu awal
# maka fungsi ini dijalankan
def Login():
    ulang = False
    coba = 1
    while ulang == False and coba <=3:
        f = Figlet(font="digital", width=200) # Style Font menggunakan Figlet package
        print(f.renderText('LOGIN AS'))
        print("""Pilih Menu :
        1. User
        2. Admin
        0. Back
        """)
        pilih = input("Pilihan : ")
        print(50*"=")
        if pilih == "1":
            login_as_user()
        elif pilih == "2":
            login_as_admin()
        elif pilih == "0":
            print("Waiting . . . .")
            time.sleep(2)
            os.system("clear")
            menu()
        else:
            print("Menu Tidak Tersedia")
            print("Waiting . . . .")
            time.sleep(2)
            os.system("clear")
            Login()

# Fungsi untuk Login as user
# ketika user memilih user pada menu Login AS
# maka fungsi ini dijalankan
def login_as_user():
    ulang = False
    coba = 1
    while ulang == False and coba <= 3:
        print("Masukkan ID dan Password pengguna yang telah dibuat")
        login["id"] = str(input("Masukkan ID Pengguna berupa karakter bukan angka : "))
        login["pass"] = str(input("Masukkan Password berupa angka : "))
        print(50*"=")
        print()
        if login["id"] == user["id"] and login["pass"] == user["pass"]:
            print("Waiting . . . .")
            time.sleep(2)
            os.system("clear")
            print("Selamat Datang, ", user["id"], " ")
            user_menu()
            try:
                login["id"] == user["id"] and login["pass"] == user["pass"]
            except:
                print("Tolong input ID atau Password dengan benar")
                break
            break
        else:
            print("ID atau Password salah,Pastikan ID atau Password yang anda masukkan benar !")
            print("Pastikan bahwa akun anda sudah ter-registrasi terlebih dahulu")
            print(50  *"=")
            coba += 1
    if coba >=3 :
        print("Kesempatan Anda untuk LOgin Telah Habis\nSilahkan Kembali Ke Menu Login")
        time.sleep(2)
        os.system("clear")
        Login()
    
# Fungsi untuk Login as admin
# ketika user memilih admin pada menu Login AS
# maka fungsi ini dijalankan
def login_as_admin():
    ulang = False
    coba = 1
    while ulang == False and coba <= 3:
        print("Masukkan ID dan Password pengguna yang telah dibuat")
        login["id"] = str(input("Masukkan ID Pengguna berupa karakter bukan angka : "))
        login["pass"] = str(input("Masukkan Password berupa angka : "))
   
        if login["id"] == user_tetap["id"] and login["pass"] == user_tetap["pass"]:
            print("Waiting . . . .")
            time.sleep(2) # Delay time
            os.system("clear") # Clear Command
            print("Selamat Datang, ", user_tetap["id"], " ")
            admin_menu()
            try:
                login["id"] == user_tetap["id"] and login["pass"] == user_tetap["pass"]
            except:
                print("Tolong input ID atau Password dengan benar")
                break
            break
        else:
            print("ID atau Password salah,Pastikan ID atau Password yang anda masukkan benar !\n")
            print(50  *"=")
            coba += 1
    if coba >=3 :
        print("Kesempatan Anda untuk LOgin Telah Habis\nSilahkan Kembali Ke Menu Login")
        time.sleep(2)
        os.system("clear")
        Login()
# Fungsi untuk Tambah Menu
# ketika user memilih tambah menu pada menu awal
# maka fungsi ini dijalankan
def tambah_menu():
    try:
        berapa = int(input("ingin menginputkan berapa banyak : "))
        for idx in range(berapa):
            masukan = input("silahkan masukkan nama menu : ")
            menu_menantea.append(masukan)
        for idx, itm in enumerate (menu_menantea, 1) :
            print(f"{idx}.{itm}")
        print("Data berhasil disimpan!\n")
        print("Waiting . . . .")
        time.sleep(3)
        os.system("clear")
        admin_menu()
    except ValueError:
        print("Maaf inputan salah")
        print("Waiting . . . .")
        time.sleep(1)
        tambah_menu()
    finally:
        print()

# Fungsi untuk Tampilkan Menu
# ketika user memilih tampilkan menu pada menu awal
# maka fungsi ini dijalankan
def tampilkan_menu():
    print(40*"=")
    print("         Pilihan Menu            ")
    print(40*"=")
    # cek terlebih dahulu apakah data yang ada pada
    # globaL variabel menu_menantea diatas datanya ada atau tidak
    if menu_menantea:
        t = PrettyTable(['No', 'Menu'])
        for idx, itm in enumerate (menu_menantea, 1) :
            t.add_row([idx, itm])
        print(t)
            # print(f"{idx}.{itm}")
        print()
        back = input("Back (0) : ")
        if back == "0":
            print("Waiting . . . .")
            time.sleep(2)
            os.system("clear")
            if login["id"] == user["id"]:
                user_menu()
            else:
                admin_menu()
        return
    else:
        print("Maaf menu belum tersedia")
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        if login["id"] == user["id"]:
            user_menu()
        else:
            admin_menu()
        return

# Fungsi untuk Update Menu
# ketika user memilih update menu pada menu awal
# maka fungsi ini dijalankan
def update_menu():
    # cek terlebih dahulu apakah data yang ada pada
    # globaL variabel menu_menantea diatas datanya ada atau tidak
    if menu_menantea:
        # for x in range(len(menu_menantea + 1)):
        f_index = [index for index, itm in enumerate(menu_menantea, 1)] # digunakan untuk menemukan index menu_menante
        berapa = int(input("Pilih nomor menu yang akan dihapus : "))
        try:
            if berapa == f_index.index(berapa) + 1:
                menuGanti = input("Nama menu menjadi ?: ")
                menu_menantea[berapa-1] = menuGanti
                print("Menu updated!\n")
                print("Waiting . . . .")
                time.sleep(2)
                os.system("clear")
                admin_menu()
        except ValueError:
            print("Maaf nomor menu yang anda masukkan tidak tersedia")
            print("Silahkan pilih nomor menu yang tersedia")
            print("Waiting . . . .")
            time.sleep(1)
            update_menu()
    else:
        print("Maaf menu belum tersedia\n")
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        admin_menu()

# Fungsi untuk Update Menu
# ketika user memilih update menu pada menu awal
# maka fungsi ini dijalankan
def hapus_menu():
    # cek terlebih dahulu apakah data yang ada pada
    # globaL variabel menu_menantea diatas datanya ada atau tidak
    if menu_menantea:
        # for x in range(len(menu_menantea)):
        f_index = [index for index, itm in enumerate(menu_menantea, 1)]
        berapa = int(input("Pilih nomor menu yang akan dihapus : "))
        try:
            if berapa == f_index.index(berapa) + 1:
                pilih = input("Apakah anda yakin ? (y/n): ")
                if pilih == "y":
                    del menu_menantea[berapa-1]
                    print("Menu deleted!!\n")
                    print("Waiting . . . .")
                    time.sleep(2)
                    os.system("clear")
                    admin_menu()
                elif pilih == "n":
                    print("Waiting . . . .")
                    time.sleep(1)
                    admin_menu()
            
        except ValueError:
            print("Maaf nomor menu yang anda masukkan tidak tersedia")
            print("Silahkan pilih nomor menu yang tersedia")
            print("Waiting . . . .")
            time.sleep(1)
            hapus_menu()
    else:
        print("Maaf menu belum tersedia\n")
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        admin_menu()

# Fungsi untuk Melakukan Pembelian
# ketika user memilih melakukan pembelian pada menu awal
# maka fungsi ini dijalankan
def do_pembelian():
    # cek terlebih dahulu apakah data yang ada pada
    # globaL variabel menu_menantea diatas datanya ada atau tidak
    beli = sum(pembelian)
    if menu_menantea:
        print()
        print("Current harga yg harus di bayar", [ beli ] ,"\n")
        banyak_menu = int(input("Berapa Banyak = "))
        if banyak_menu <= 0:
            print("Pesanan tidak boleh 0 atau < 0")
            time.sleep(1)
            do_pembelian()
        else:
            try:
                t_menu = int(input("Silahkan masukkan no menu: "))
                f_index = [index for index, itm in enumerate(menu_menantea, 1)]
                if t_menu == f_index.index(t_menu) + 1:
                    harga = int(input("Harga = "))
                    print("Anda memesan", menu_menantea[t_menu-1], "sebanyak", banyak_menu, "menu" ) 
                    total_harga = int(banyak_menu) * harga
                    print("Total harga yang harus anda bayar: ", total_harga ,"\n")
                    pembelian[:0] = [total_harga]
                    pilih = input("Apakah anda ingin memesan lagi ?: (y/n)\n")
                    if pilih == "y":
                        print("Waiting . . . .")
                        time.sleep(3)
                        do_pembelian()
                    else:
                        print("Total Pembayaran : ", [ beli ])
                        print()
                        print("Silahkan melakukan pembayaran di kasir")
                        print("Waiting . . . .")
                        time.sleep(5)
                        os.system("clear")
                        if login["id"] == user["id"]:
                            user_menu()
                        else:
                            admin_menu()
                    return
            except ValueError:
                print("Maaf no menu tidak terdaftar, silahkan cek menunya")
                print("Waiting . . . .")
                time.sleep(3)
                os.system("clear")
                if login["id"] == user["id"]:
                    user_menu()
                else:
                    admin_menu()
                return
            finally:
                print()
    else:
        print("Maaf menu belum tersedia\n")
        print("Waiting . . . .")
        time.sleep(3)
        os.system("clear")
        if login["id"] == user["id"]:
            user_menu()
        else:
            admin_menu()
        return

# Fungsi Menu Login and Register
def menu():
    f = Figlet(font="small", width=200)
    print(f.renderText('PROGRAM KASIR TOKO MENANTEA'))
    print("""Pilih Menu :
    1. Register
    2. Login
    0. Exit
    """)
    pilih = input("Pilihan : ")
    print(50*"=")
    if pilih == "1":
        register()
    elif pilih == "2":
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        Login()
    elif pilih == "0":
        print(50*"_")
        print("                 Terima Kasih !!!                ")
        print()
        time.sleep(2)
        exit() 
    else:
        print("Menu Tidak Tersedia")
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        menu()

# Fungsi untuk menampilkan menu pada awal
# program di running
# untuk membuat fungsi di python menggunakan def(spasi)(namanya()) seperti di bawah
def admin_menu():
    print("""Pilih Menu :
    1. Tambah Menu
    2. Tampilkan Menu
    3. Update Menu
    4. Hapus Menu
    5. Melakukan Pembelian
    6. Logout
    """)

    pilih = input("Pilihan : ")

    if pilih == "1":
        tambah_menu() # Pemanggilan fungsi tambah menu yang sudah dibuat diatas
    elif pilih == "2":
        tampilkan_menu() # Pemanggilan fungsi tampilkan menu yang sudah dibuat diatas
    elif pilih == "3":
        update_menu() # Pemanggilan fungsi tampilkan menu yang sudah dibuat diatas
    elif pilih == "4":
        hapus_menu() # Pemanggilan fungsi hapus menu yang sudah dibuat diatas
    elif pilih == "5":
        do_pembelian()
    elif pilih == "6":
        print()
        print("Successfull Logout!")
        time.sleep(3)
        os.system("clear")
        menu()
    else:
        print("Menu Tidak Tersedia")
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        admin_menu()

def user_menu():
    print("""Pilih Menu :
    1. Tampilkan Menu
    2. Melakukan Pembelian
    3. Logout
    """)

    pilih = input("Pilihan : ")

    if pilih == "1":
        tampilkan_menu() # Pemanggilan fungsi tambah menu yang sudah dibuat diatas
    elif pilih == "2":
        do_pembelian() # Pemanggilan fungsi tampilkan menu yang sudah dibuat diatas
    elif pilih == "3":
        print()
        print("Successfull Logout!")
        time.sleep(3) # Delay time
        os.system("clear")
        menu()
    else:
        print("Menu Tidak Tersedia")
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        user_menu()

# Main Fungsi
# berguna untuk mendefinisikan funsi mana yang akan
# di tampilkan ketika program di running/dijalankan
if __name__ == "__main__":
  while(True):
    menu()
            
   