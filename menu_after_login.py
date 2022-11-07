import time
import os
import menu as mn
import main as m
from pyfiglet import Figlet
from colorama import Fore, Style

def admin_menu():
    print("""Pilih Menu :
    1. Tambah Menu
    2. Tampilkan Menu
    3. Update Menu
    4. Hapus Menu
    5. Melakukan Pembelian
    0. Logout
    """)

    pilih = input("Pilihan : ")

    if pilih == "1":
        mn.tambah_menu()
    elif pilih == "2":
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        mn.tampilkan_menu()
    elif pilih == "3":
        mn.update_menu() 
    elif pilih == "4":
        mn.hapus_menu() 
    elif pilih == "5":
        mn.do_pembelian()
    elif pilih == "0":
        print()
        print("Successfull Logout!")
        time.sleep(2)
        os.system("clear")
        m.menu()
    else:
        print("Menu Tidak Tersedia")
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        admin_menu()

def c_user_menu():
    print("""Pilih Menu :
    1. Tampilkan Menu
    2. Melakukan Pembelian
    0. Logout
    """)

    pilih = input("Pilihan : ")

    if pilih == "1":
        mn.tampilkan_menu()
    elif pilih == "2":
        mn.do_pembelian()
    elif pilih == "0":
        if mn.pembelian:
            print("Maaf anda tidak bisa Logout")
            print("Silahkan lakukan pembayaran terlebih dahulu")
            user_menu()
        else:
            print()
            print("Successfull Logout!")
            time.sleep(2)
            os.system("clear")
            m.menu()
    else:
        print("Menu Tidak Tersedia")
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        c_user_menu()

def user_menu():
    if mn.pembelian:
        print(f"{Fore.RED}[Anda belum melakukan pembayaran sebesar {sum(mn.pembelian)}] {Style.RESET_ALL}")
        print()
        c_user_menu()
    else:
        c_user_menu()