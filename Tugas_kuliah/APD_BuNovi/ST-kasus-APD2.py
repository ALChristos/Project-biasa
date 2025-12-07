profile_mc = {"HP": 100, "Mana": 70}
profile_villain = {"HP": 150, "Mana": 100}
skill_mc = {
    "Light explosion": {"damage": 20, "mana": 10},
    "Light beam": {"damage": 50, "mana": 25},
    "Light healing": {"heal": 20, "mana":5},}
skill_villain = {
    "Shadow strike": {"damage": 15, "mana": 10},
    "Darkness wave": {"damage": 30, "mana": 20},
    "Shadow ruin": {"damage": 10, "mana": 5},}

while profile_mc["HP"] > 0 and profile_villain["HP"] > 0:
    # MC menyerang
    if profile_mc["Mana"] >= 25 and profile_mc["HP"] > 40:
        # Light beam
        profile_mc["Mana"] -= 25
        profile_villain["HP"] -= 50
        print("MC menggunakan Light beam! Villain terkena 50 damage.")
    elif profile_mc["Mana"] >= 10 and profile_mc["HP"] > 40:
        # Light explosion
        profile_mc["Mana"] -= 10
        profile_villain["HP"] -= 20
        print("MC menggunakan Light explosion! Villain terkena 20 damage.")
    elif profile_mc["Mana"] >= 5 and profile_mc["HP"] <= 40:
         # Healing
         profile_mc["Mana"] -= 5
         profile_mc["HP"] += 20
         print("MC menggunakan Light healing! HP MC bertambah 20.")
    else:
         # Isi ulang mana
         profile_mc["Mana"] += 10
         print("MC mengisi ulang mana.")

    # Villain menyerang
    if profile_villain["Mana"] >= 20:
        # Darkness wave
        profile_villain["Mana"] -= 20
        profile_mc["HP"] -= 30
        print("Villain menggunakan Darkness wave! MC terkena 30 damage.")
    elif profile_villain["Mana"] >= 10:
        # Shadow strike
        profile_villain["Mana"] -= 10
        profile_mc["HP"] -= 15
        print("Villain menggunakan Shadow strike! MC terkena 15 damage.")
    elif profile_villain["Mana"] >= 5:
        # Shadow ruin
        profile_villain["Mana"] -= 5
        profile_mc["HP"] -= 10
        print("Villain menggunakan Shadow ruin! MC terkena 10 damage.")
    else:
        # Isi ulang mana
        profile_villain["Mana"] += 10
        print("Villain mengisi ulang mana.")
    # Status HP dan Mana dari MC dan Villain
    print(f"Status: MC HP={profile_mc['HP']} Mana={profile_mc['Mana']} | Villain HP={profile_villain['HP']} Mana={profile_villain['Mana']}\n")
    
    # Hasil pertempuran
    if profile_villain["HP"] <= 0:
        print("Villain kalah! MC menang!")
   
