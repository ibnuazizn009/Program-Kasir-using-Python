import os
import time
import login_as as la
from pyfiglet import Figlet 

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

if __name__ == "__main__":
  while(True):
    menu()
            
   