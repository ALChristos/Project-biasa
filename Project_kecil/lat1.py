import os 

while True:
    os.system("cls")
    print("======"*10)
    print("PROGRAM KALKULATOR")
    print("======"*10)
    
    angka_1= float(input("Masukan Angka Pertama: "))
    perhitungan_user1= input("Masukan Perhitungan (+,-,*,/): ")
    angka_2= float(input("Masukan Angka Kedua: "))

    if perhitungan_user1 == "+":
        hasil= angka_1 + angka_2
        print(f"hasil dari {angka_1} + {angka_2} = {hasil}")
    elif perhitungan_user1 == "-":
        hasil= angka_1 - angka_2
        print(f"hasil dari {angka_1} - {angka_2} = {hasil}")
    elif perhitungan_user1 == "*":
        hasil= angka_1 * angka_2    
        print(f"hasil dari {angka_1} * {angka_2} = {hasil}")
    elif perhitungan_user1 == "/":
        hasil = angka_1 / angka_2
        print(f"hasil dari {angka_1} / {angka_2} = {hasil}")
    else:
        print("=========PROGRAM PERHITUNGAN TIDAK VALID!!!=========")
    input_penyelesaian= input("Apakah Mau Menghitung Lagi? (Y/N)")
    if input_penyelesaian.lower() in ("n","no","g","ga"):
        print("=========TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI==========")
        break