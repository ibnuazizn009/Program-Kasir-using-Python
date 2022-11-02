import os
import time # package untuk time diantaranya time.sleep untuk delay
import menu_after_login as mal
import temp_data as td
from pyfiglet import Figlet # package untuk style text
from prettytable import PrettyTable

menu_menantea = [] # Global variabel, variabel ini digunakan untuk menyimpan data menu yg di tambahkan pada 
pembelian = [] # Global variabel, variabel ini digunakan untuk menyimpan data pembelian

# Fungsi untuk Tambah Menu
# ketika user memilih tambah menu pada menu awal
# maka fungsi ini dijalankan
def tambah_menu():
    try:
        berapa = int(input("ingin menginputkan berapa banyak : "))
        t = PrettyTable(['No', 'Menu'])
        for idx in range(berapa):
            masukan = input("silahkan masukkan nama menu : ")
            menu_menantea.append(masukan)
        # for idx, itm in enumerate (menu_menantea, 1) :
        #     print()
        #     print("Menu yang ditambahkan")
        #     t.add_row([idx, itm])
        # print(t)
        print()
        print("Data berhasil disimpan!")
        print("Waiting . . . .")
        time.sleep(3)
        os.system("clear")
        mal.admin_menu()
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
            if td.login["id"] == td.user["id"]:
                mal.user_menu()
            else:
                mal.admin_menu()
        return
    else:
        print("Maaf menu belum tersedia")
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        if td.login["id"] == td.user["id"]:
            mal.user_menu()
        else:
            mal.admin_menu()
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
                mal.admin_menu()
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
        mal.admin_menu()

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
                    mal.admin_menu()
                elif pilih == "n":
                    print("Waiting . . . .")
                    time.sleep(1)
                    mal.admin_menu()
            
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
        mal.admin_menu()

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
                    pilih = input("Apakah anda ingin memesan lagi ? (y/n): ")
                    if pilih == "y":
                        print("Waiting . . . .")
                        time.sleep(3)
                        do_pembelian()
                    else:
                        # print("Total Pembayaran : ", [ beli ])
                        print()
                        print("Silahkan melakukan pembayaran di kasir")
                        print("Waiting . . . .")
                        time.sleep(5)
                        os.system("clear")
                        if td.login["id"] == td.user["id"]:
                            mal.user_menu()
                        else:
                            mal.admin_menu()
                    return
            except ValueError:
                print("Maaf no menu tidak terdaftar, silahkan cek menunya")
                print("Waiting . . . .")
                time.sleep(3)
                os.system("clear")
                if td.login["id"] == td.user["id"]:
                    mal.user_menu()
                else:
                    mal.admin_menu()
                return
            finally:
                print()
    else:
        print("Maaf menu belum tersedia\n")
        print("Waiting . . . .")
        time.sleep(3)
        os.system("clear")
        if td.login["id"] == td.user["id"]:
            mal.user_menu()
        else:
            mal.admin_menu()
        return