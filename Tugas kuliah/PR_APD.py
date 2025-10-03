# Untuk menginport os agar bisa membersihkan layar
import os
# Perulangan
while True:
#  Setiap perulangan, layar akan dibersihkan
 os.system("cls")
# Menampilkan judul program dan opsi konversi suhu yang tersedia
 print("======"*10)
 print("PROGRAM PERHITUHNGAN SUHU")
 print("1. Melakukan konversi suhu Celcius ke Reamur, Farenheit, dan Kelvin")
 print("2. Melakukan konversi suhu Reamur ke Celcius, Farenheit, dan Kelvin")
 print("3. Melakukan konversi suhu Farenheit ke Celcius, Reamur, dan Kelvin")
 print("4. Melakukan konversi suhu Kelvin ke Celcius, Reamur, dan Farenheit")
 print("======"*10)
#  Masukkan opsi konversi suhu yang diinginkan
 input_pilihan= input("Masukan Opsi: ")
# Jika anda memilih opsi 1, maka program akan menjalankan konversi dari Celcius ke Reamur, Farenheit, dan Kelvin.
 if input_pilihan == "1":
     Suhu= float(input("Masukan Suhu dalam derajat Celcius: "))
    #  Rumus konversi suhu dari Celcius ke Reamur
     hitung_R= ((4/5)*Suhu)
    #  Menampilkan hasil konversi suhu Celcius ke Reamur
     print(f"Suhu Celcius ke Reamur = {hitung_R}")
    #  Rumus konversi suhu dari Celcius ke Farenheit
     hitung_F= (((9/5)*Suhu)+32)
    #  Menampilkan hasil konversi suhu Celcius ke Farenheit
     print(f"Suhu Celcius ke Farenheit  = {hitung_F}")
    #  Rumus konversi suhu dari Celcius ke Kelvin
     hitung_K= ((Suhu+273.15))
    #  Menampilkan hasil konversi suhu Celcius ke Kelvin
     print(f"Suhu Celcius ke Kelvin = {hitung_K}")

# Jika anda memilih opsi 2, maka program akan menjalankan konversi dari Reamur ke Celcius, Farenheit, dan Kelvin.
 elif input_pilihan == "2":
     Suhu= float(input("Masukan Suhu dalam derajat Reamur: "))
    #  Rumus konversi suhu dari Reamur ke Celcius
     hitung_C= ((5/4)*Suhu)
    #  Menampilkan konversi suhu dari Reamur ke Celcius 
     print(f"Suhu Reamur ke Celcius = {hitung_C}")
    #  Rumus konversi suhu dari Reamur ke Farenheit
     hitung_F= (((9/4)*Suhu)+32)
    #  Menampilkan hasil konversi suhu dari Reamur ke Farenheit
     print(f"Suhu Reamur ke Farenheit = {hitung_F}")
    #  Rumus konversi suhu dari Reamur ke Kelvin
     hitung_K= (((5/4)*Suhu)+273.15)
    #  Menampilkan hasil konversi suhu dari Reamur ke Kelvin
     print(f"Suhu Reamur ke Kelvin = {hitung_K}")

# Jika anda memilih opsi 3, maka program akan menjalankan konversi dari Farenheit ke Celcius, Reamur, dan Kelvin.
 elif input_pilihan == "3":
     Suhu= float(input("Masukan Suhu dalam derajat Farenheit: "))
    #  Rumus konversi suhu dari Farenheit ke Celcius
     hitung_C= ((5/9)*(Suhu-32))
    #  Menampilkan hasil konversi suhu dari Farenheit ke Celcius
     print(f"Suhu Farenheit ke Celcius = {hitung_C}")
    #  Rumus konversi suhu dari Farenheit ke Reamur
     hitung_R= ((4/9)*(Suhu-32))
    #  Menampilkan hasil konversi suhu dari Farenheit ke Reamur
     print(f"Suhu Farenheit ke Reamur = {hitung_R}")
    #  Rumus konversi suhu dari Farenheit ke Kelvin
     hitung_K= ((5/9)*(Suhu-32)+273.15)
    #  Menampilkan hasil konversi suhu dari Farenheit ke Kelvin
     print(f"Suhu Farenheit ke Kelvin = {hitung_K}")

# Jika anda memilih opsi 4, maka program akan menjalankan konversi dari Kelvin ke Celcius, Reamur, dan Farenheit.
 elif input_pilihan == "4":
     Suhu= float(input("Masukan Suhu dalam derajat Kelvin: "))
    #  Rumus konversi suhu dari Kelvin ke Celcius
     hitung_C= (Suhu-273.15)
    #  Menampilkan hasil konversi suhu dari Kelvin ke Celcius
     print(f"Suhu Kelvin ke Celcius = {hitung_C}")
    #  Rumus konversi suhu dari Kelvin ke Reamur
     hitung_R= ((4/5)*(Suhu-273.15))
    #  Menampilkan hasil konversi suhu dari Kelvin 
     print(f"Suhu Kelvin ke Reamur = {hitung_R}")
    #  Rumus konversi suhu dari Kelvin ke Farenheit
     hitung_F= ((9/5)*(Suhu-273.15)+32)
    #  Menampilkan hasil konversi suhu dari Kelvin ke Farenheit
     print(f"Suhu Kelvin ke Farenheit = {hitung_F}")

# Jika anda memilih opsi selain 1, 2, 3, atau 4, maka program akan menampilkan pesan bahwa program perhitungan suhu tidak ada.
 else:
     print("=========PROGRAM PERHITUNGAN SUHU TIDAK ADA!!!=========")

#  Menanyakan apakah user ingin melakukan perhitungan lagi
 Selesai = input("Apakah Mau Memilih Lagi? (y/n)")
#  Jika user memasukkan "y", "ya", atau "yes", maka program akan mengulangi perhitungan suhu.
 if Selesai.lower () in ("y","ya", "yes"):
    continue
 
#  Jika user memasukkan selain "y", "ya", atau "yes", maka program akan berhenti dan menampilkan pesan terima kasih.
 else:
    print("=========TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI==========")
    break


