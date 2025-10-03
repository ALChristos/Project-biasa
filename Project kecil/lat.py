import os 

while True:
   os.system("cls")
   print("======"*10)
   print("PROGRAM PENILAIAN SISWA")
   print("======"*10)
   jumlah_siswa = int(input("Masukan Jumlah Siswa: "))
   for i in range(jumlah_siswa):
    print(f"jumlah siswa ke-{i+1}")
    nama_siswa = input("Masukan Nama Siswa: ")
    nilai_siswa = float(input("Masukan Nilai Siswa: "))
    if nilai_siswa >= 80:
     print(f"Siswa dengan nama {nama_siswa} mendapatkan nilai A")
    elif nilai_siswa >= 70:
        print(f"Siswa dengan nama {nama_siswa} mendapatkan nilai B")
    else:
        print(f"Siswa dengan nama {nama_siswa} mendapatkan nilai C")
        input_penyelesaian= input("Apakah Mau Menilai Lagi? (Y/N)")
        if input_penyelesaian.lower() in ("n","no","g","ga"):
            print("=========TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI==========")
            break