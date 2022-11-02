import time
import os
import menu as mn
import main as m
from pyfiglet import Figlet
from colorama import Fore, Style

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
    0. Logout
    """)

    pilih = input("Pilihan : ")

    if pilih == "1":
        mn.tambah_menu() # Pemanggilan fungsi tambah menu yang sudah dibuat diatas
    elif pilih == "2":
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        mn.tampilkan_menu() # Pemanggilan fungsi tampilkan menu yang sudah dibuat diatas
    elif pilih == "3":
        mn.update_menu() # Pemanggilan fungsi tampilkan menu yang sudah dibuat diatas
    elif pilih == "4":
        mn.hapus_menu() # Pemanggilan fungsi hapus menu yang sudah dibuat diatas
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
        mn.tampilkan_menu() # Pemanggilan fungsi tambah menu yang sudah dibuat diatas
    elif pilih == "2":
        mn.do_pembelian() # Pemanggilan fungsi tampilkan menu yang sudah dibuat diatas
    elif pilih == "0":
        if mn.pembelian:
            print("Maaf anda tidak bisa Logout")
            print("Silahkan lakukan pembayaran terlebih dahulu")
            user_menu()
        else:
            print()
            print("Successfull Logout!")
            time.sleep(2) # Delay time
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