import numpy as np
import seaborn as sns
from InquirerPy import inquirer
import pandas as pd
import matplotlib.pyplot as plt
import os

plt.style.use("seaborn-v0_8")

def bersih():
    os.system("cls" if os.name == "nt" else "clear")


def load_data():
    print("\n=== LOADING BMW DATASET ===")
    df = pd.read_csv("Data_Set/BMW_Sales.csv")
    print(f"Total data: {len(df)}")
    return df


def harga_per_tahun(df):
    plt.figure(figsize=(12, 6))

    harga_rata2 = df.groupby("Year")["Price_USD"].mean()

    plt.plot(harga_rata2.index, harga_rata2.values, marker='o')
    plt.title("Rata-rata Harga Mobil BMW per Tahun", fontsize = 20)
    plt.xlabel("Tahun", fontsize = 20)
    plt.ylabel("Harga Rata-rata (USD)", fontsize = 20)
    plt.grid(True, linestyle = '--', alpha=0.6)

    for x, y in zip(harga_rata2.index, harga_rata2.values):
        plt.text(x, y, f"{int(y)}$", fontsize = 11, ha = "center", va = "bottom")

    plt.tight_layout()
    plt.show()


def total_penjualan_unit(df):
    plt.figure(figsize = (12, 6))
    penjualan_tahun = df.groupby("Year")["Model"].count()
    
    plt.plot(penjualan_tahun.index, penjualan_tahun.values, marker = "o")
    plt.title("Data Unit BMW Yang Terjual Tiap Tahun", fontsize = 20)
    plt.xlabel("Tahun", fontsize = 20)
    plt.ylabel("Unit Terjual", fontsize = 20)
    plt.grid(True, linestyle = "--", alpha = 0.6)
    
    for i, o in zip(penjualan_tahun.index, penjualan_tahun.values):
        plt.text(i, o, f"{o}Unit", fontsize = 11, ha = "center", va = "bottom")
        
    plt.tight_layout()
    plt.show()
    

def total_penjualan_unit_benua(df):
    plt.figure(figsize = (12, 6))
    
    penjualan_benua = df.groupby("Region")["Model"].count()
    plt.plot(penjualan_benua.index, penjualan_benua.values, marker = "o")
    plt.title("Data Penjualan BMW 2014-2024 DiBerbagai Benua", fontsize = 20)
    plt.xlabel("Benua", fontsize = 20)
    plt.ylabel("Unit Terjual", fontsize = 20)
    plt.grid(True, linestyle = "--", alpha = 0.6)
    
    for x, y in zip(penjualan_benua.index, penjualan_benua.values):
        plt.text(x, y, f"{y}Unit", fontsize = 11, ha = "center", va = "bottom")
        
    plt.tight_layout()
    plt.show()
    
    
def bahan_bakar(df):
    plt.figure(figsize = (12, 6))

    tipe_fuel = df.groupby("Fuel_Type")['Fuel_Type'].count()

    plt.bar(tipe_fuel.index, tipe_fuel.values)
    plt.title("Jumlah Penjualan Berdasarkan Fuel Type", fontsize = 20)
    plt.xlabel("Fuel Type", fontsize = 20)
    plt.ylabel("Jumlah Unit", fontsize = 20)
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    for i, v in enumerate(tipe_fuel.values):
        plt.text(i, v, f"{v}Unit", fontsize = 11, ha='center', va='bottom')

    plt.tight_layout()
    plt.show()


def bahan_bakar_benua(df):
    plt.figure(figsize = (14, 8))
    
    grup = df.groupby(["Region", "Fuel_Type"]).size().unstack()
    benua = grup.index
    tipe_fuel = grup.columns

    for i, region in enumerate(benua, start=1):
        plt.subplot(2, 3, i)  

        jumlah = grup.loc[region]
        plt.bar(tipe_fuel, jumlah.values)

        plt.title(f"Pengguna Fuel BMW Di {region}", fontsize = 14)
        plt.xlabel("Tipe Bahan Bakar", fontsize = 12)
        plt.ylabel("Jumlah Unit", fontsize = 12)
        plt.grid(axis='y', linestyle='--', alpha=0.6)

        for idx, val in enumerate(jumlah.values):
            plt.text(idx, val, f"{val}Unit", ha='center', va='bottom')

    plt.tight_layout()
    plt.show()
    
    
def transmisi(df):
    plt.figure(figsize = (12, 8))

    jenis_transmisi = df['Transmission'].value_counts()

    plt.bar(jenis_transmisi.index, jenis_transmisi.values)
    plt.title("Perbandingan Mobil Otomatis vs Manual")
    plt.xlabel("Transmission")
    plt.ylabel("Jumlah Unit")
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    for idx, val in enumerate(jenis_transmisi.values):
        plt.text(idx, val, f"{val}Unit", ha='center', va='bottom')

    plt.tight_layout()
    plt.show()
    
def transmisi_benua(df):
    plt.figure(figsize = (14, 8))
    
    grup = df.groupby(["Region", "Transmission"]).size().unstack()
    benua = grup.index
    jenis_transmisi = grup.columns
    
    for idx, region in enumerate(benua, start = 1):
        plt.subplot(2, 3 , idx)
        data_benua = grup.loc[region]
        
        plt.bar(jenis_transmisi, data_benua.values)
        plt.title(f"Data Transmisi BMW {region}", fontsize = 14)
        plt.xlabel("Transmisi Mobil", fontsize = 12)
        plt.ylabel("Jumlah Unit")
        plt.grid(axis = "y", linestyle = "--", alpha = 0.6)
        
        for x, y in enumerate(data_benua.values):
            plt.text(x, y, f"{y}Unit", ha = "center", va = "bottom")
            
    plt.tight_layout()        
    plt.show()
    
    
def plot_mileage_vs_price(df):
    bins = np.arange(0, df["Mileage_KM"].max()+10000, 10000)
    df["mileage_bin"] = pd.cut(df["Mileage_KM"], bins=bins)

    grouped = df.groupby("mileage_bin", observed = False)["Price_USD"].mean().reset_index()

    grouped["mid_mileage"] = grouped["mileage_bin"].apply(
        lambda b: int(b.left + (b.right - b.left)/2)
    )
    plt.figure(figsize=(12,6))
    plt.plot(grouped["mid_mileage"], grouped["Price_USD"], marker="o", linewidth=2)

    plt.title("Harga Mobil Berdasarkan Mileage")
    plt.xlabel("Mileage (KM)")
    plt.ylabel("Harga Rata-rata (USD)")
    plt.grid(True, linestyle = '--', alpha = 0.5)
    
    for x, y in zip(grouped["mid_mileage"], grouped["Price_USD"]):
        plt.text(x, y, f"{int(y)}$", fontsize = 11, ha='center', va='bottom')

    plt.tight_layout()
    plt.show()


def menu(df):
    while True:
        pilihan = inquirer.select(
            message="Pilih visualisasi:",
            choices=[
                "1. Rata-rata Harga BMW per Tahun",
                "2. Total Unit BMW Penjualan PerTahun Global",
                "3. Total Unit BMW Terjual Per Benua",
                "4. Perbandingan Tipe Bahan Bakar Global",
                "5. Perbandingan Tipe Bahan Bakar Per Benua",
                "6. Perbandingan Transmisi Global",
                "7. Perbandingan Transmisi Per Benua",
                "8. Korelasi Jarak Tempuh Dengan Harga Mobil",
                "Keluar",
            ],
            pointer = "➣"
        ).execute()

        if pilihan.startswith("1"):
            bersih()
            harga_per_tahun(df)
            
        elif pilihan.startswith("2"):
            bersih()
            total_penjualan_unit(df)
        
        elif pilihan.startswith("3"):
            bersih()
            total_penjualan_unit_benua(df)
            
        elif pilihan.startswith("4"):
            bersih()
            bahan_bakar(df)
            
        elif pilihan.startswith("5"):
            bersih()
            bahan_bakar_benua(df)
            
        elif pilihan.startswith("6"):
            bersih()
            transmisi(df)
            
        elif pilihan.startswith("7"):
            bersih()
            transmisi_benua(df)
            
        elif pilihan.startswith("8"):
            bersih()
            plot_mileage_vs_price(df)
      
        else:
            bersih()
            print("\nTerima kasih! Program selesai.")
            break


if __name__ == "__main__":
    bersih()
    df = load_data()
    menu(df)
