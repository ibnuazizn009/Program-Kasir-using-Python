import os
import time 
import menu_after_login as mal
import temp_data as td
from pyfiglet import Figlet
from prettytable import PrettyTable

menu_menantea ={} 
pembelian = [] 

def tambah_menu():
    try:
        berapa = int(input("ingin menginputkan berapa banyak : "))
        t = PrettyTable(['No', 'Menu', 'Harga'])
        for idx in range(berapa):
            try:
                noMenu = int(input("Silahkan masukkan no menu : "))
                masukan = input("Silahkan masukkan nama menu : ")
                price = int(input("Harga menu : "))
                if noMenu == menu_menantea.keys():
                    print("No Menu sudah ada silahkan masukkan No lain")
                    time.sleep(1)
                    tambah_menu()
                else:
                    menu_menantea.update({noMenu:{masukan:price}})
            except ValueError:
                print('Input Salah!')
                break
            finally:
                print()
        for no, value in menu_menantea.items():
            for name, price in value.items():
                t.add_row([no, name, price])
        print()
        print("Menu yang ditambahkan")
        print(t)
        print()
        print("Data berhasil disimpan!")
        print("Waiting . . . .")
        time.sleep(9)
        os.system("clear")
        mal.admin_menu()
    except ValueError:
        print("Maaf inputan salah")
        print("Waiting . . . .")
        time.sleep(1)
        tambah_menu()
    finally:
        print()

def tampilkan_menu():
    print(40*"=")
    print("         Pilihan Menu            ")
    print(40*"=")
    if menu_menantea:
        t = PrettyTable(['No', 'Menu', 'Harga'])
        for no, value in menu_menantea.items():
            for name, price in value.items():
                t.add_row([no, name, price])
        print(t)
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

def update_menu():
    if menu_menantea:
        f_index = [index for index, itm in enumerate(menu_menantea, 1)] 
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

def hapus_menu():
    if menu_menantea:
        f_index = [*menu_menantea]
        berapa = int(input("Pilih nomor menu yang akan dihapus : "))
        try:
            if berapa == f_index.index(berapa) + 1:
                pilih = input("Apakah anda yakin menghapus menu ? (y/n): ")
                if pilih == "y":
                    del menu_menantea[berapa]
                    print("Menu deleted!!\n")
                    print("Waiting . . . .")
                    time.sleep(2)
                    os.system("clear")
                    mal.admin_menu()
                elif pilih == "n":
                    back = input("Back/No (0)/(1) : ")
                    if back == "0":
                        print("Waiting . . . .")
                        time.sleep(2)
                        os.system("clear")
                        if td.login["id"] == td.user["id"]:
                            mal.user_menu()
                        else:
                            mal.admin_menu()
                    elif back == '1':
                        hapus_menu()
                    return
        except ValueError:
            print("Maaf nomor menu yang anda masukkan tidak tersedia")
            print("Silahkan pilih nomor menu yang tersedia dan silahkan lihat menu terlebih dahulu")
            print("Waiting . . . .")
            time.sleep(1)
            hapus_menu()
    else:
        print("Maaf menu belum tersedia\n")
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        mal.admin_menu()

def do_pembelian():
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