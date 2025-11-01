# Menjumlahkan Data Dalam List
import os
list_nilai = []
while True:
    def maks():
            while True:
                print(f"Angka yang ingin dicari nilai maksimumnya : {list_nilai}")
                angka = int(input("Masukan angka: "))
                list_nilai.append(angka)
                ulang = input("Apakah ingin memasukan angka lagi? (Y/N)")
                if ulang.lower() == "y":
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                elif ulang.lower() == "n":
                    break
                else:
                    print("Pilih yang bener oi")
                    input("Tekan enter")
                    list_nilai.clear()
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                       
            maksimal = max(list_nilai)
            print(f"Total angka maksimum  yang anda input adalah : {maksimal}")
            while True:
                ulang1 = input("Apakah ingin mengulang pencarian angka maksimum lagi? (Y/N)")
                if ulang1.lower() == "y":
                    os.system("cls" if os.name == "nt" else "clear")
                    list_nilai.clear()
                    return maks()
                elif ulang1.lower() == "n":
                    print("Program selesai")
                    return
                else:
                    print("Pilih yang bener oi")
                    input("Tekan enter")
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                
    maks()
    break
                

            
