from MyLib import *

def main():
    while True:
        print("=======================")
        print(" ")
        print("    SELAMAT DATANG     ")
        print("SILAHKAN MASUKKAN UANG")
        print("        10000")
        print(" ")
        print("=======================")
        
        n = int(input("masukkan uangmu : "))
        masukan_uang(n)
        print(" ")
        print("==========================================")
        print("   SILAHKAN PILIH MENU YANG ADA DI SINI")
        print("==========================================")
        print("| ┌─────────────────────────────────────┐|")
        print("| |_____________________________________||")
        print("| |coca cola| fanta  | sprite | frestea ||")
        print("| |   1     |    2   |   3    |    4    ||")
        print("| |         |        |        |         ||")
        print("| |_____________________________________||")
        p = int(input())
        pesan(p)
        break

if __name__ == "__main__": 
    main()