import pandas as pd
from prettytable import PrettyTable

df = pd.read_csv("Data_Set/data_mahasiswa.csv")

print("\n" + "="*70)
print("         DATA MAHASISWA PER PRODI     ")
print("="*70 + "\n")

total_prodi = df.groupby("Prodi")["NIM"].count()
table1 = PrettyTable()
table1.title = "Total Mahasiswa per Prodi"
table1.field_names = ["Prodi", "Jumlah Mahasiswa"]
for prodi, total in total_prodi.items():
    table1.add_row([prodi, total])

print(table1, "\n")

for prodi in df["Prodi"].unique():
    print(f"\n===== PRODI: {prodi} =====")   
    df_prodi = df[df["Prodi"] == prodi]
    table_detail = PrettyTable()
    table_detail.title = f"Data Mahasiswa Prodi {prodi}"
    table_detail.field_names = ["NIM", "Nama", "Prodi", "Nilai", "Angkatan", "Jenis Kelamin"]
    for _, row in df_prodi.iterrows():
        table_detail.add_row([
            row["NIM"], row["Nama"], row["Prodi"], 
            row["IPK"], row["Angkatan"], row["JenisKelamin"]
        ])

    print(table_detail)

    total_angkatan = df_prodi.groupby("Angkatan")["NIM"].count()
    print("\nRekap Angkatan dalam Prodi:")
    for angkatan, total in total_angkatan.items():
        print(f"- Angkatan {angkatan}: {total} mahasiswa")

    ipk_angkatan = df_prodi.groupby("Angkatan")["IPK"].mean().round(2)
    table_ipk = PrettyTable()
    table_ipk.title = f"Rata-Rata IPK per Angkatan ({prodi})"
    table_ipk.field_names = ["Angkatan", "Rata-Rata IPK"]
    for angkatan, avg in ipk_angkatan.items():
        table_ipk.add_row([angkatan, avg])

    print("\n" + str(table_ipk) + "\n")

print("\n" + "="*70)
print("         DATA MAHASISWA BERDASARKAN ANGKATAN     ")
print("="*70 + "\n")
for angkatan in sorted(df["Angkatan"].unique()):
    print(f"\n===== ANGKATAN: {angkatan} =====")
    df_angkatan = df[df["Angkatan"] == angkatan]
    table_angkatan = PrettyTable()
    table_angkatan.title = f"Data Mahasiswa Angkatan {angkatan}"
    table_angkatan.field_names = ["NIM", "Nama", "Prodi", "IPK", "Angkatan", "Jenis Kelamin"]
    for _, row in df_angkatan.iterrows():
        table_angkatan.add_row([
            row["NIM"],
            row["Nama"],
            row["Prodi"],
            row["IPK"],
            row["Angkatan"],
            row["JenisKelamin"]
        ])

    print(table_angkatan)

