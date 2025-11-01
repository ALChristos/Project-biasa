# Menjumlahkan Data Dalam List
import os
list_angka = []
while True:
    def tambah():
            while True:
                print(f"Angka yang ingin anda jumlahkan : {list_angka}")
                angka = int(input("Masukan angka yang ingin di jumlahkan: "))
                list_angka.append(angka)
                ulang = input("Apakah ingin menambah angka lagi? (Y/N)")
                if ulang.lower() == "y":
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                elif ulang.lower() == "n":
                    break
                else:
                    print("Pilih yang bener oi")
                    input("Tekan enter")
                    list_angka.clear()
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                       
            total = sum(list_angka)
            print(f"Total jumlah angka yang anda input adalah : {total}")
            while True:
                ulang1 = input("Apakah ingin mengulang penjumlahan angka? (Y/N)")
                if ulang1.lower() == "y":
                    os.system("cls" if os.name == "nt" else "clear")
                    list_angka.clear()
                    return tambah()
                elif ulang1.lower() == "n":
                    print("Program selesai")
                    return
                else:
                    print("Pilih yang bener oi")
                    input("Tekan enter")
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                
    tambah()
    break
                

            
