# Toko pakaian grand opening
harga_pakaian= int(input("Masukkan harga pakaian: "))
if harga_pakaian > 100000:
    diskon= harga_pakaian * 0.20
    total_bayar= harga_pakaian - diskon
    print(f"Total bayar setelah diskon 20% adalah:{total_bayar}")
elif harga_pakaian > 50000:
    diskon= harga_pakaian * 0.10
    total_bayar= harga_pakaian - diskon
    print(f"Total bayar setelah diskon 10% adalah:{total_bayar}")
else:
    print(f"Total bayar adalah:{harga_pakaian}")


# Tenary operator
harga_pakaian= int(input("Masukkan harga pakaian: "))
total_bayar= harga_pakaian - (harga_pakaian * 0.20) if harga_pakaian > 100000 else harga_pakaian - (harga_pakaian * 0.10) if harga_pakaian > 50000 else harga_pakaian
print(f"Total bayar adalah:{total_bayar}")
