# Sihir pemurnian merupakan sihir yang dapat mengidentifikasi letak Aethermark dan memurnikan kegelapan Abyss
letak_Aethermark = ("Dahi", 
                    "Telapak tangan kanan",
                    "Tulang selangka kiri", 
                    "Punggung tangan kiri", 
                    "Punggung leher") #letak Aethermark
tokoh_utama = (["Dada kiri"],)  

for i in letak_Aethermark:
    if i != tokoh_utama[0]:
        if i == "Dahi":
            print(f"Aethermark terletak di {i}, merupakan ras Celestial")
        elif i == "Telapak tangan kanan":
            print(f"Aethermark terletak di {i}, merupakan ras Archon")
        elif i == "Tulang selangka kiri":
            print(f"Aethermark terletak di {i}, merupakan ras Heiros")
        elif i == "Punggung tangan kiri":
            print(f"Aethermark terletak di {i}, merupakan ras Manusia")
        elif i == "Punggung leher":
            print(f"Aethermark terletak di {i}, merupakan ras Abyss\n")
        
else:
 print("Aethermark tokoh utama terletak di dada kiri dan ras tidak diketahui")
 print("Sihir pemurnian mendeteksi letak Aethermark baru dan menambahkan ke dalam list letak Aethermark\n")
letak_Aethermark_baru = list(letak_Aethermark)
letak_Aethermark_baru.append(tokoh_utama[0])
print(f"Letak Aethermark baru terdeteksi, menjadi\n {letak_Aethermark_baru}\n tetapi ras tokoh utama masih tidak diketahui") 
