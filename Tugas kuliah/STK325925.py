nilai=input(int("Masukkan nilai akhir: "))
kelas=input("Masukkan kelas (A/B/C): ")
if nilai >= 80 and kelas == "A":
    print("Selamat, Anda lulus dengan predikat A")
elif nilai >= 70 and kelas == "B":
    print("Selamat, Anda lulus dengan predikat B")
elif nilai >= 60 and kelas == "C":
    print("Selamat, Anda lulus dengan predikat C")
else:
    print("Maaf, Anda tidak lulus/anda tidak terdaftar di kelas manapun")