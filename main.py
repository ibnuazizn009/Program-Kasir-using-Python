# Code dibawah adalah untuk memanggil package
# package disini adalah sebuah fungsi yg disediakan oleh python sendiri
# atau kita harus install terlebih dahulu packagenya
import os
import time # package untuk time diantaranya time.sleep untuk delay
import login_as as la
from pyfiglet import Figlet # package untuk style text

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
        la.register()
    elif pilih == "2":
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        la.Login()
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

# Main Fungsi
# berguna untuk mendefinisikan funsi mana yang akan
# di tampilkan ketika program di running/dijalankan
if __name__ == "__main__":
  while(True):
    menu()
            
   