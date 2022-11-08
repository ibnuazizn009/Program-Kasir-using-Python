import os
import time
import main as m
import temp_data as td
import menu_after_login as mal
from pyfiglet import Figlet


# Fungsi untuk register
# ketika user memilih register pada menu awal
# maka fungsi ini dijalankan
def register():
    print("Masukkan ID dan Password Pengguna Baru")
    while True:
        try:
            td.user["id"] = input("Masukkan ID Pengguna berupa karakter bukan angka : ")
            td.user["pass"] = int(input("Masukkan Password berupa angka : "))
            if td.user["id"].isnumeric():
                print("Tolong input ID atau Password dengan benar")
                register()
                break
        except ValueError:
            print("Tolong input ID atau Password dengan benar")
        else:
            print()
            print("Berhasil Register")
            break
    kembali = input("Kembali ke menu awal? (y/n) = ")
    if kembali == "y":
        print("Waiting . . . .")
        time.sleep(2)
        os.system("clear")
        m.menu()
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
            m.menu()
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
        td.login["id"] = str(input("Masukkan ID Pengguna berupa karakter bukan angka : "))
        td.login["pass"] = int(input("Masukkan Password berupa angka : "))
        print(50*"=")
        if td.login["id"] == td.user["id"] and td.login["pass"] == td.user["pass"]:
            print("Login Successfull!!")
            print("Waiting . . . .")
            time.sleep(2)
            os.system("clear")
            print("Selamat Datang, ", td.user["id"], " ")
            mal.user_menu()
            try:
                td.login["id"] == td.user["id"] and td.login["pass"] == td.user["pass"]
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
        print("Kesempatan Anda untuk Login Telah Habis\nSilahkan Kembali Ke Menu Login")
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
        td.login["id"] = str(input("Masukkan ID Pengguna berupa karakter bukan angka : "))
        td.login["pass"] = str(input("Masukkan Password berupa angka : "))
   
        if td.login["id"] == td.user_tetap["id"] and td.login["pass"] == td.user_tetap["pass"]:
            print()
            print("Login Successfull!!")
            print("Waiting . . . .")
            time.sleep(2) # Delay time
            os.system("clear") # Clear Command
            print("Selamat Datang, ", td.user_tetap["id"], " ")
            mal.admin_menu()
            try:
                td.login["id"] == td.user_tetap["id"] and td.ogin["pass"] == td.user_tetap["pass"]
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
