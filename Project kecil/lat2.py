import inquirer

data = {
    "nama" : [],
    "NIM" : [],
    "kelas" : []
}

def tambah_data():
    tanya = [   
        inquirer.Text("nama", message = "input nama"),
        inquirer.Text("NIM", message = "input NIM" ),
        inquirer.Text("kelas", message = "input kelas")
    ]  
    jawab = inquirer.prompt(tanya)
    data['nama'].append(jawab['nama'])
    data['NIM'].append(jawab['NIM'])
    data['kelas'].append(jawab['kelas'])
    
tambah_data()
for i,a in data.items():
    print(i,a)
    
if inquirer.text("nama",message="input nama") in "123456789":
    print("error")