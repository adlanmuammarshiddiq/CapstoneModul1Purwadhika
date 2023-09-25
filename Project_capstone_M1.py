import os

# ID dan Password Admin
adminID = {"admin": "12345"}


# Data Stok Gudang yang berisi key dan value
# Code merupakan KEY
# List yang berada dalam Dictionary merupakan value
# Format code_barang : [kategori,nama,jumlah,harga]
stok = {
    "B001": ["Rokok", "Sampoerna", 4, 250000],
    "B002": ["Sembako", "Minyak", 11, 240000],
    "B003": ["Sembako", "Beras", 8, 100000],
    "B004": ["Minuman", "Coca-Cola", 15, 40000],
    "B005": ["Makanan", "Kue", 10, 100000],
}


# Function yang memfilter agar user dapat melihat barang berdasakan kategori
def filter_read_kategori():
    print("=" * 50)
    print("||", " " * 14, "Daftar Kategori", " " * 13, "||")
    print("=" * 50)
    print("Daftar Kategori:")
    # Memunculkan kategori yang berada dalam stok
    kategori = set(data[0] for data in stok.values())
    for k in kategori:
        print("-", k)
    while True:
        # User input by kategori
        input_kategori = input("Masukkan kategori yang ingin Anda lihat: ").title()
        # Mengecek apakah code yang di masukkan user berupa huruf jika tidak maka akan mengeluarkan
        # Kategori harus berupa huruf. Coba lagi.
        if not input_kategori.isalpha():
            print("Kategori harus berupa huruf. Coba lagi.")
            print()
            continue
        else:
            found = False
            for kode, data in stok.items():
                # Memunculkan output sesuai dengan kategori yang dipilih
                if data[0].lower() == input_kategori.lower():
                    found = True
                    os.system("cls")
                    print("=" * 63)
                    print(
                        "||",
                        " " * 11,
                        "Tabel Stok Sesuai Kategori Barang",
                        " " * 11,
                        "||",
                    )
                    print("=" * 63)
                    tabelstok(input_kategori)
                    userback3 = input("Kembali (Y/N) : ").upper()
                    while True:
                        if userback3 == "Y":
                            # Memanggil function filter_read
                            os.system("cls")
                            filter_read()
                        elif userback3 == "N":
                            print("Thank you for visiting our warehouse")
                            exit()
                        else:
                            print("Masukkan (Y/N)")
        if not found:
            print("Kategori tidak ditemukan. Coba lagi.")
            print()
            continue


# Function filter_read akan merupaka function READ pada aplikasi ini
def filter_read():
    while True:
        print("=" * 50)
        print("||", " " * 15, "Stok Gudang", " " * 16, "||")
        print("=" * 50)
        print("1. Lihat semua table")
        print("2. Lihat tabel sesuai code barang")
        print("3. Lihat tabel sesuai kategori")
        print("4. Kembali ke Menu")
        print("=" * 50)

        # User input untuk memilih menu 1,2,3,4
        userInput = input("Masukkan pilihan anda [1-3] : ")

        if userInput == "1":
            # Tampilkan seluruh tabel stok
            os.system("cls")
            tabelstok()
            while True:
                userback1 = input("Kembali (Y/N) : ").upper()
                # Kembali ke pilihan menu utama filter_read
                if userback1 == "Y":
                    os.system("cls")
                    filter_read()
                elif userback1 == "N":
                    print("Thank you for visiting our warehouse")
                    exit()
                else:
                    print("Masukkan (Y/N)")
                    print()
        elif userInput == "2":
            while True:
                # User input untuk memunculkan tabel sesuai dengan code barang
                # Apabila user ingin menginputkan lebih dari 2 barang maka harus dipisahkan dengan koma
                code_barang_input = input(
                    "Masukkan code barang (B00..) dipisahkan koma: "
                )
                # Mengsplit code barang dengan koma
                code_barang_list = [
                    code.strip().upper() for code in code_barang_input.split(",")
                ]
                # User tidak boleh menginputkan code barang duplikat
                if len(code_barang_list) != len(set(code_barang_list)):
                    print("Code barang tidak boleh ada yang duplikat atau sama!!")
                    print()
                    continue
                # Mengecek apakah code yang diinputkan oleh user berada dalam list atau tidak
                valid_codes = []
                invalid_codes = []
                for code_barang in code_barang_list:
                    if code_barang in stok:
                        valid_codes.append(code_barang)
                    else:
                        invalid_codes.append(code_barang)
                # Jika code barang tidak berada dalam list maka akan memunculkan
                # Code barang x tidak ada dalam stok dan system akan kembali melooping
                if invalid_codes:
                    print()
                    # Mengecek apakah code yang diberikan oleh user duplikat atau sama
                    print(
                        f"Code barang {', '.join(invalid_codes)} tidak ada dalam stok !!!"
                    )
                # Memunculkan output sesuai code_barang yang telah diinputkan oleh user
                if valid_codes:
                    os.system("cls")
                    print("=" * 63)
                    print(
                        "||", " " * 13, "Tabel Stok Sesuai Code Barang", " " * 13, "||"
                    )
                    print("=" * 63)
                    print(
                        "+--------+---------------+-------------+-----------+----------+"
                    )
                    print(
                        "|  Kode  |    Kategori   |     Nama    |   Jumlah  |   Price  |"
                    )
                    print(
                        "+--------+---------------+-------------+-----------+----------+"
                    )
                    for code_barang in valid_codes:
                        kategori, nama, jumlah, harga = stok[code_barang]
                        print(
                            "| {:<6} | {:<13} | {:<11} | {:<9} | {:8} |".format(
                                code_barang, kategori, nama, jumlah, harga
                            )
                        )
                    print(
                        "+--------+---------------+-------------+-----------+----------+"
                    )
                    print()
                    userback1 = input("Kembali (Y/N) : ").upper()
                    while True:
                        if userback1 == "Y":
                            os.system("cls")
                            filter_read()
                        elif userback1 == "N":
                            print("Thank you for visiting our warehouse")
                            exit()
                        else:
                            print("Masukkan (Y/N)")
                else:
                    print("Tidak ada code barang yang valid dalam stok.")
                print()
        # Menu menampilkan filter read berdasarkan kategori
        elif userInput == "3":
            os.system("cls")
            # Memanggil functio filter_read_kategori
            filter_read_kategori()
            while True:
                userback = input("Kembali (Y/N) : ").upper()
                if userback == "Y":
                    os.system("cls")
                    filter_read()
                    break
                elif userback == "N":
                    print("Thank you for visiting our warehouse")
                    exit()
                else:
                    print("Masukkan input (Y/N) !!! ")
        # Kembali ke dashboardAdmin
        elif userInput == "4":
            while True:
                userback = input("Kembali ke Dashboard Admin (Y/N) : ").upper()
                if userback == "Y":
                    os.system("cls")
                    # Memanggil function dashboardAdmin
                    dashboardAdmin()
                    break
                elif userback == "N":
                    print("Thank you for visiting our warehouse")
                    exit()
                else:
                    print("Masukkan input (Y/N) !!! ")
        else:
            print("Masukkan pilihan [1-3] !!! ")


# Function untuk memanggil tabel pada stok
def tabelstok(input_kategori=None):
    print()
    print("+--------+---------------+-------------+-----------+----------+")
    print("|  Kode  |    Kategori   |     Nama    |   Jumlah  |   Price  |")
    print("+--------+---------------+-------------+-----------+----------+")
    # Memberikan output data sesuai dengan format yang berada pada stok
    for kode, data in stok.items():
        kategori, nama, jumlah, harga = data

        if input_kategori is None or kategori.lower() == input_kategori.lower():
            print(
                "| {:<6} | {:<13} | {:<11} | {:<9} | {:8} |".format(
                    kode, kategori, nama, jumlah, harga
                )
            )

    print("+--------+---------------+-------------+-----------+----------+")
    print()


# Function untuk menyimpan ID Admin
def is_valid_username(username):
    return username.isalpha()


# Function untuk menyimpan password Admin
def is_valid_password(password):
    return password.isdigit()


# Function untuk memberikan dashboard adminLogin
# Sebelum masuk ke dashboard Admin
def adminLogin():
    print("=" * 50)
    print("||", " " * 16, "Admin Login", " " * 15, "||")
    print("=" * 50)
    # Untuk menyimpan value Failedlogin yang diinputkan oleh user
    failedLogin = 0

    while failedLogin <= 2:
        username = input("Masukkan ID anda : ").lower()

        if not is_valid_username(username):
            print("ID hanya boleh berisi huruf. Coba lagi.")
            print()
            continue

        while True:  # Melakukan loop untuk input kata sandi
            password = input("Masukkan kata sandi anda : ").lower()

            # Mengecek apakah kata sandi yang diinputkan berupa angka
            if not is_valid_password(password):
                print("Kata sandi hanya boleh berisi angka. Coba lagi.")
                print()
                continue

            # Keluar dari fungsi adminLogin() setelah login berhasil
            if username in adminID and adminID[username] == password:
                os.system("cls")
                dashboardAdmin()
                return

            # Menambahkan value failed login + 1 jika user menginputkan ID dan Password yang salah
            else:
                print("ID atau Password yang anda masukkan salah!!")
                print()
                failedLogin += 1
                break

        # Jika user melakukan failed login sebanyak 4 kali maka akan dikembalikan ke mainMenu()
        if failedLogin == 3:
            print("Anda telah melebihi batas percobaan login yang diperbolehkan.")
            os.system("cls")
            # Memanggil function main menu
            mainMenu()


# Funtion untuk memanggil belanjaan user
def shoppingCart():
    cart = {}  # Dictionary untuk menyimpan barang yang akan dibeli
    total_harga = 0  # Total harga belanjaan
    uang = 0  # Jumlah uang yang dimasukkan oleh user
    ppn = 0  # PPN
    kembalian = 0  # Kembalian
    os.system("cls")

    while True:
        print("=" * 65)
        print("||", " " * 22, "Shopping Cart", " " * 22, "||")
        print("=" * 65)
        print("| No. |    Jenis    |       Nama       |  Jumlah  |    Harga    |")
        print("=" * 65)

        for no, (kode, data) in enumerate(stok.items(), start=1):
            jenis, nama, jumlah, harga = data
            print(f"| {no:2}  | {jenis:11} | {nama:16} | {jumlah:8} | {harga:11} |")

        print("=" * 65)

        while True:
            shoppingInput = input(
                f"Masukkan nomor barang yang ingin dibeli [1-{no}][Y/N] untuk kembali : "
            )
            if shoppingInput.isalpha():
                if shoppingInput == "y" or shoppingInput == "Y":
                    os.system("cls")
                    mainMenu()
                elif shoppingInput == "N" or shoppingInput == "n":
                    print("Thanks for visiting our warehouse")
                    exit()
                else:
                    continue

            if shoppingInput.isdigit():  # Memastikan input adalah angka
                shoppingInput = int(shoppingInput)

                if (
                    1 <= shoppingInput <= 5
                ):  # Memastikan input berada dalam rentang [1-5]
                    kode_barang = list(stok.keys())[
                        shoppingInput - 1
                    ]  # Mendapatkan kode barang dari input

                    if kode_barang in cart:
                        if (
                            cart[kode_barang] < stok[kode_barang][2]
                        ):  # Memeriksa apakah jumlah dalam keranjang kurang dari stok
                            while True:
                                jumlah_input = input(
                                    f"Masukkan jumlah {stok[kode_barang][1]} yang ingin dibeli: "
                                )
                                if jumlah_input.isdigit():
                                    jumlah_input = int(jumlah_input)
                                    if (
                                        1 <= jumlah_input <= stok[kode_barang][2] and jumlah_input != 0 
                                    ):  # Memeriksa apakah jumlah yang diminta tidak melebihi stok atau 0
                                        cart[kode_barang] += jumlah_input
                                        total_harga += (
                                            jumlah_input * stok[kode_barang][3]
                                        )
                                        print(
                                            f"{jumlah_input} {stok[kode_barang][1]} berhasil dimasukkan ke keranjang."
                                        )
                                        break
                                    else:
                                        print(
                                            "Jumlah yang diminta melebihi stok yang tersedia atau 0"
                                        )
                                else:
                                    print("Masukkan angka yang valid untuk jumlah.")
                        else:
                            print(f"Stok {stok[kode_barang][1]} sudah habis.")
                    else:
                        while True:
                            jumlah_input = input(
                                f"Masukkan jumlah {stok[kode_barang][1]} yang ingin dibeli: "
                            )
                            if jumlah_input.isdigit():
                                jumlah_input = int(jumlah_input)
                                if (
                                    1 <= jumlah_input <= stok[kode_barang][2]
                                ):  # Memeriksa apakah jumlah yang diminta tidak melebihi stok
                                    cart[kode_barang] = jumlah_input
                                    total_harga += jumlah_input * stok[kode_barang][3]
                                    print(
                                        f"{jumlah_input} {stok[kode_barang][1]} berhasil dimasukkan ke keranjang."
                                    )
                                    break
                                else:
                                    print(
                                        "Jumlah yang diminta melebihi stok yang tersedia atau 0"
                                    )
                                    print()
                            else:
                                print("Masukkan angka yang valid untuk jumlah.")
                else:
                    print("Nomor harus berada dalam tabel. Coba lagi.")
            else:
                print("Masukkan angka yang valid!!")

            if not cart:
                print("Keranjang belanja kosong.")
                break
            os.system("cls")
            print("=" * 51)
            print("||", " " * 15, "Shopping Cart", " " * 15, "||")
            print("=" * 51)
            print("| No. |       Nama       |  Jumlah  |    Harga    |")
            print("=" * 51)

            for no, (kode, jumlah) in enumerate(cart.items(), start=1):
                jenis, nama, stok_tersedia, harga = stok[kode]
                print(f"| {no:2}  | {nama:16} | {jumlah:8} | {jumlah * harga:11} |")

            print("=" * 51)
            print(f"Total Harga: {total_harga}")
            print("=" * 51)

            while True:
                uang_input = input("Masukkan jumlah uang yang Anda bayarkan: ")
                if uang_input.isdigit():
                    uang_input = int(uang_input)
                    if uang_input < total_harga:
                        print("Jumlah uang tidak mencukupi!!")
                    else:
                        uang = uang_input
                        break
                else:
                    print("Masukkan angka yang valid untuk uang.")

            while True:
                checkout = input("Apakah anda ingin checkout (Y/N)? ").strip().lower()
                if checkout == "y":
                    ppn = total_harga * 0.1
                    ppn = int(ppn)
                    kembalian = uang - total_harga - ppn
                    for kode, jumlah in cart.items():
                        stok[kode][
                            2
                        ] -= jumlah  # Mengurangi stok sesuai dengan jumlah yang dibeli
                    while True:
                        cetakStruk = input(
                            "Apakah anda ingin mencetak struk belanja (Y/N) :"
                        ).upper()
                        if cetakStruk == "Y":
                            os.system("cls")
                            print("+", "-" * 26, "+")
                            print("|                            |")
                            print("|", " " * 5, "GUDANG BAROKAH  ", " " * 3, "|")
                            print("|                            |")
                            print("+", "-" * 26, "+")
                            print("|", f"Nama Barang : {nama}    |")
                            print("|", f"Jumlah Barang : {jumlah}          |")
                            print("|", f"Total Harga : {total_harga}       |")
                            print("|", f"PPN 10%                    |")
                            print("|", f"Kembalian : {kembalian}       |")
                            print("+", "-" * 26, "+")
                            print()
                            kembali = input("Back to Shopping Cart (Y/N) : ").upper()
                            if kembali == "Y":
                                os.system("cls")
                                shoppingCart()
                            elif kembali == "N":
                                print("Thank you for visiting our warehouse")
                                exit()
                            else:
                                print("Masukkan (Y/N)")
                                print()
                            break
                        elif cetakStruk == "N":
                            print()
                            print("Terima kasih telah berbelanja!")
                            print("PPN 10%")
                            print(f"Kembalian Anda: {kembalian}")
                            print()
                            kembali = input("Back to Shopping Cart (Y/N) : ").upper()
                            if kembali == "Y":
                                os.system("cls")
                                shoppingCart()
                            elif kembali == "N":
                                print("Thank you for visiting our warehouse")
                                exit()
                            else:
                                print("Masukkan (Y/N)")
                                print()
                            break
                        else:
                            print("Masukkan (Y/N)")
                            print()
                elif checkout == "n":
                    cart.clear()
                    total_harga = 0
                    os.system('cls')
                    shoppingCart()
                    break
                else:
                    print("Masukkan Y atau N.")
                    print()
                    continue

        kembali = input("Back to Shopping Cart (Y/N) : ").upper()
        if kembali == "Y":
            os.system("cls")
            shoppingCart()
        elif kembali == "N":
            print("Thank you for visiting our warehouse")
            exit()
        else:
            print("Masukkan (Y/N)")
            print()


# Funtrion Dashboard Admin
def dashboardAdmin():
    print("=" * 50)
    print("||", " " * 14, "Dashboard Admin", " " * 13, "||")
    print("=" * 50)
    print("1.Menampilkan Stok Gudang")
    print("2.Menambah Stok Gudang")
    print("3.Mengupdate Stok Gudang")
    print("4.Menghapus Stok Gudang")
    print("5.Kembali ke menu utama")
    print("6.Keluar Program")
    print("=" * 50) 
    while True:
        adminInput = input("Masukkan pilihan anda : ")
        if len(stok.items()) == 0:
            print('Tidak ada barang dalam stok')
            if adminInput == "5":
                os.system("cls")
                mainMenu()
                break
            elif adminInput == "6":
                print("Thank you for visiting our warehouse")
                exit()
            else:
                continue
        # Memanggil function filter_read
        if adminInput == "1":
            os.system("cls")
            filter_read()
            break
        # Memanggil function menambahStokGudang
        elif adminInput == "2":
            os.system("cls")
            menambahStokGudang()
            break
        # Memanggil function mengupdateStokGudang
        elif adminInput == "3":
            os.system("cls")
            mengupdateStokGudang()
            break
        # Memanggil function menghapusStokGudang
        elif adminInput == "4":
            os.system("cls")
            menghapusStokGudang()
            break
        # Kembali ke main menu
        elif adminInput == "5":
            os.system("cls")
            mainMenu()
            break
        # End Program
        elif adminInput == "6":
            print("Thank you for visiting our warehouse")
            exit()
        else:
            print("Please Input [1-6]")
            print()
            continue
            


# Function untuk menambah stok pada gudang / CREATE
def menambahStokGudang():
    print("=" * 60)
    print("||", " " * 17, "Tambah Stok Barang", " " * 17, "||")
    print("=" * 60)

    while True:
        kode_barang = input("Masukkan Kode Barang (B00...): ").capitalize()
        # Mengecek apakah code barang berawalan dari B00
        if not kode_barang.startswith("B00"):
            print("Kode barang harus berawalan dengan huruf (B00..)")
            continue
        # Mengecek apakah code barang memiliki 2 digit angka setelah B00
        elif (
            not kode_barang[3:].isdigit()
            or len(kode_barang) < 4
            or len(kode_barang) > 5
        ):
            print("Kode barang harus memiliki 1/2 digit angka setelah 'B00'")
            print()
            continue
        # Mengecek apakah code barang berada dalam stok
        elif kode_barang in stok:
            os.system("cls")
            tabelstok()
            print("Kode barang sudah ada dalam stok, silahkan masukkan kode yang lain.")
            continue
        # Menu untuk menambah stok barang
        else:
            while True:
                nama_barang = input("Masukkan Nama Barang: ").title()
                # Mengecek nama barang apakah sudah berupa huruf
                if not nama_barang.isalpha():
                    print("Nama barang harus berupa huruf.")
                    print()
                    continue
                # Nama barang tidak boleh sama dengan nama kategori yang berada dalam stok
                elif any(nama_barang == data[0] for data in stok.values()):
                    print("Nama barang tidak boleh sama dengan nama kategori!!")
                    print()
                    continue
                # Nama barang tidak boleh duplikat dengan nama barang yang sudah ada dalam stok
                elif any(nama_barang == data[1] for data in stok.values()):
                    print(
                        "Nama barang sudah ada dalam stok, silahkan masukkan nama yang berbeda."
                    )
                    print()
                    continue
                else:
                    break

            while True:
                kategori = input("Masukkan Kategori Barang: ").title()
                # Mengecek apakah kategori yang diinputkan oleh user berupa huruf
                if not kategori.isalpha():
                    print("Kategori barang harus berupa huruf.")
                    print()
                    continue
                # Nama kategori tidak boleh sama dengan nama barang pada stok
                elif any(nama_barang == data[1] for data in stok.values()):
                    print("Nama kategori tidak boleh sama dengan nama barang")
                else:
                    break

            while True:
                jumlah_str = input("Masukkan Jumlah Barang: ")
                # Mengecek apakah jumlah barang sudah berupa angka
                if not jumlah_str.isdigit():
                    print("Jumlah barang harus berupa angka.")
                    print()
                    continue
                # Merubah type data string ke integer agar sesuai dengan jumlah pada stok
                jumlah = int(jumlah_str)
                break

            while True:
                harga_str = input("Masukkan Harga Barang : ")
                # Mengecek apakah harga barang sudah berupa angka
                if not harga_str.isdigit():
                    print("Harga barang harus berupa angka.")
                    print()
                    continue
                # Merubah type data string to integer
                harga = int(harga_str)
                break

            # Menampilkan data yang diinputkan atau ditambahkan oleh user
            os.system("cls")
            print("+--------+---------------+-------------+-----------+----------+")
            print("|  Kode  |    Kategori   |     Nama    |   Jumlah  |   Price  |")
            print("+--------+---------------+-------------+-----------+----------+")
            print(
                f"|{kode_barang:^8}|{kategori:^15}|{nama_barang:^13}|{jumlah:^11}|{harga:^10}|"
            )
            print("+--------+---------------+-------------+-----------+----------+")
            print()
            menambahStok = input("Apakah anda ingin menambahkan stok di atas (Y/N) :").upper()
            while True : 
                # Jika user menekan Y maka data yang diinputkan akan ditambahkan ke dalam stok
                if menambahStok == "Y" :
                    stok[kode_barang] = [kategori, nama_barang, jumlah, harga]
                    os.system("cls")
                    tabelstok()
                    print("Barang telah ditambahkan ke dalam stok!!")
                    break
                elif menambahStok == 'N' : 
                    print('Barang tidak jadi ditambahkan')
                    break
                else : 
                    print('Masukkan (Y/N)')

        # Kembali ke dashboard admin
        userInput = input("Kembali ke Dashboard Admin (Y/N) : ").upper()
        if userInput == "Y":
            os.system("cls")
            dashboardAdmin()
        # Exit Program
        elif userInput == "N":
            print("Terima kasih telah mengunjungi gudang kami.")
            exit()
        else:
            print("Masukkan (Y/N)")
            print()


# Function untuk mengupadate stok pada gudang / UPDATE
def mengupdateStokGudang():
    print("=" * 65)
    print("||", " " * 19, "Update Stok Gudang", " " * 20, "||")
    print("=" * 65)
    print()
    tabelstok()
    print("=" * 65)
    while True:
        updateStok = input(
            "Masukkan Code barang yang ingin anda ganti (B00..) : "
        ).upper()
        # Mengecek apakah code barang yang diinputkan oleh user berada dalam tabel stok
        if updateStok not in stok:
            print("Kode barang harus berada pada tabel")
            print()
            continue
        # Menu untuk memilih update berdasarkan kategori atau semua
        elif updateStok in stok:
            os.system("cls")
            print("=" * 65)
            print("||", " " * 19, "Update Stok Gudang", " " * 20, "||")
            print("=" * 65)
            print("1.Update Kategori Barang ")
            print("2.Update Nama Barang ")
            print("3.Update Jumlah Barang ")
            print("4.Update Jumlah,Nama,Kategori Barang ")
            print("5.Kembali ke Dashboard Admin ")
            print("=" * 65)
            userInput = input("Stok yang ingin diganti [1-5] : ")
            while True:
                # Menu untuk menggatin Kategori barang sesuai dengan yang user inputkan
                if userInput == "1":
                    while True:
                        new_kategori = input(
                            "Masukkan Kategori Barang yang baru: "
                        ).title()
                        # Mengecek apakah inputan user hanya berupa huruf
                        if new_kategori.isalpha():
                            # Mengecek apakah nama kategori sama seperti sebelumnya
                            if any(new_kategori == data[1] for data in stok.values()):
                                print(
                                    "Nama kategori tidak boleh sama dengan nama yang pada stok"
                                )
                                print()
                                continue
                            # Mengganti kategori baru dengan yang user inputkan
                            stok[updateStok][0] = new_kategori
                            print("Kategori Barang telah diupdate.")
                            break
                        else:
                            print("Kategori harus berupa huruf")
                            print()
                            continue
                    break
                elif userInput == "2":
                    while True:
                        new_nama = input("Masukkan Nama Barang yang baru: ").title()
                        # Mengecek apakah inputan user hanya berupa huruf
                        if new_nama.isalpha():
                            # Mengecek apakah nama barang sama dengan nama yang sudah ada pada stok
                            if any(new_nama == data[1] for data in stok.values()):
                                print("Nama barang tidak boleh sama yang ada pada stok")
                                continue
                            # Mengecek apakah nama barang != nama kategori yang ada pada stok
                            elif any(new_nama == data[0] for data in stok.values()):
                                print(
                                    "Nama barang tidak boleh sama dengan nama kategori"
                                )
                                continue
                            # Mengganti nama barang sesuai dengan nama yang diinputkan oleh user
                            stok[updateStok][1] = new_nama
                            print("Nama Barang telah diupdate.")
                            break
                        else:
                            print("Kategori harus berupa huruf")
                            print()
                            continue
                    break
                elif userInput == "3":
                    while True:
                        new_jumlah = input("Masukkan Jumlah Barang yang baru: ")
                        # Mengecek apakah jumlah barang berupa huruf
                        if new_jumlah.isdigit():
                            new_jumlah = int(new_jumlah)
                            stok[updateStok][2] = new_jumlah
                            print("Jumlah Barang telah diupdate.")
                            break
                        else:
                            print("Jumlah barang harus berupa angka")
                            print()
                            continue
                    break
                elif userInput == "4":
                    while True:
                        new_kategori = input(
                            "Masukkan Kategori Barang yang baru: "
                        ).title()
                        # Mengecek apakah inputan user hanya berupa huruf
                        if new_kategori.isalpha():
                            if any(new_kategori == data[1] for data in stok.values()):
                                print(
                                    "Nama kategori tidak boleh sama dengan nama barang pada stok"
                                )
                                print()
                                continue
                            stok[updateStok][0] = new_kategori
                            print("Kategori Barang telah diupdate.")
                        else:
                            print("Kategori harus berupa huruf")
                            print()
                            continue
                        new_nama = input("Masukkan Nama Barang yang baru: ").title()
                        if new_nama.isalpha():
                            if any(new_kategori == data[1] for data in stok.values()):
                                stok[updateStok][1] = new_nama
                                print("Nama Barang telah diupdate.")
                                break
                        else:
                            print("Kategori harus berupa huruf")
                            continue
                        new_jumlah = int(input("Masukkan Jumlah Barang yang baru: "))
                        if new_jumlah.isdigit():
                            new_jumlah = int(new_jumlah)
                            stok[updateStok][2] = new_jumlah
                            print("Jumlah Barang telah diupdate.")
                            break
                        else:
                            print("Jumlah barang harus berupa angka")

                    stok[updateStok] = [new_kategori, new_nama, new_jumlah]
                    print("Kategori, Nama, dan Jumlah Barang telah diupdate.")
                    print()
                    tabelstok()
                    break
                elif userInput == "5":
                    os.system("cls")
                    dashboardAdmin()
                else:
                    print("Masukkan angka antara [1-4] !!!")
                    break
        else:
            print("Masukkan Code Barang yang berada dalam Tabel!!!")
            print()
            continue

        kembali = input("Kembali ke Dashboard Admin (Y/N) : ").upper()
        if kembali == "Y":
            os.system("cls")
            dashboardAdmin()
        elif kembali == "N":
            dashboardAdmin()
        else:
            print("Masukkan (Y/N)")


# Function untuk menghapus stok pada gudang berdasarkan Kategori
def filter_delete_kategori():
    os.system("cls")
    print("=" * 50)
    print("||", " " * 14, "Daftar Kategori", " " * 13, "||")
    print("=" * 50)
    print("Daftar Kategori:")
    # Menampilkan kategori yang ada pada stok
    kategori = set(data[0] for data in stok.values())
    for k in kategori:
        print("-", k)
    while True:
        kategori = input("Masukkan Kategori Barang yang akan dihapus: ").title()
        found_items = []
        # Mengecek apakah kategori barang yang diinputkan oleh user ada pada stok
        for kode, data in stok.items():
            if data[0].title() == kategori:
                found_items.append((kode, data))

        # Melooping jika user memasukkan kategori yang tidak ada pada stok
        if not found_items:
            print("Kategori barang tidak ditemukan dalam stok!!")
            print()
            continue
        # Menampilkan data sesuai dengan kategori yang ada pada stok
        else:
            os.system("cls")
            print()
            print("+--------+---------------+-------------+-----------+----------+")
            print("|  Kode  |    Kategori   |     Nama    |   Jumlah  |   Price  |")
            print("+--------+---------------+-------------+-----------+----------+")
            for kode, data in found_items:
                kategori, nama, jumlah, harga = data
                print(
                    "| {:<6} | {:<13} | {:<11} | {:<9} | {:8} |".format(
                        kode, kategori, nama, jumlah, harga
                    )
                )
            print("+--------+---------------+-------------+-----------+----------+")
            print()
            # Memastikan apakah user ingin menghapus barang
            while True:
                delBarang1 = input("Apakah anda ingin menghapus data (Y/N) : ").upper()
                if delBarang1 == "Y":
                    for kode, _ in found_items:
                        del stok[kode]
                    os.system("cls")
                    # Menampilkan tabel setelah penghapusan
                    tabelstok()
                    print(f"Barang dengan kategori {kategori} telah dihapus dari stok.")
                elif delBarang1 == "N":
                    print("Penghapusan data dibatalkan.")
                    break
                else:
                    print("Masukkan (Y/N)")
                    print()
                    continue

        # Kembali ke pilihan menu utama
        userback1 = input("Kembali (Y/N) : ").upper()
        if userback1 == "Y":
            os.system("cls")
            menghapusStokGudang()
        else:
            print("Thank you for visiting our warehouse")
            exit()


# Function untuk menghaspus stok pada gudang /DELETE
def menghapusStokGudang():
    print("=" * 50)
    print("||", " " * 12, "Delete Stok Gudang", " " * 12, "||")
    print("=" * 50)
    print("1. Hapus Seluruh data")
    print("2. Hapus Data berdasarkan ID")
    print("3. Hapus Data berdasarkan Kategori")
    print("4. Back to Dashboard Admin")
    print("=" * 50)

    while True:
        menudelBarang = input("Masukkan Pilihan [1-4] : ")
        # Menu untuk menghapus seluruh barang yang ada pada stok
        # Mengosongkan tabel pada stok
        if menudelBarang == "1":
            os.system("cls")
            tabelstok()
            delBarang1 = input("Apakah anda ingin menghapus data (Y/N) : ").upper()
            if delBarang1 == "Y":
                stok.clear()
                os.system("cls")
                tabelstok()
                print("Seluruh data barang telah dihapus dari stok.")
                break
            else:
                # Stok akan dibatalkan penghapusan apa bila user memilih N
                print("Penghapusan data dibatalkan.")
                break
            # Kembali ke pilihan menu diatas
        elif menudelBarang == "2":
            # Menu untuk mendelete baran berdasarkan code_barang
            while True:
                os.system("cls")
                print("=" * 50)
                print("||", " " * 12, "Delete Stok Gudang", " " * 12, "||")
                print("=" * 50)
                print()
                delBarang_input = input(
                    "Masukkan Kode Barang (B00...) yang akan dihapus, dipisahkan oleh koma (,): "
                )
                # Memastikan code yang diinput jika lebih dari 2 code barang yang diinputkan harus dipisahkan oleh (,)
                delBarang_list = [
                    code.strip().upper() for code in delBarang_input.split(",")
                ]

                # Memastikan code barang tidak boleh ada yang duplikat
                if len(delBarang_list) != len(set(delBarang_list)):
                    print("Code barang tidak boleh ada yang duplikat atau sama!!")
                    print()
                    continue

                # Mengecek inputan yang diinputkan oleh user
                valid_codes = []
                invalid_codes = []
                for delBarang in delBarang_list:
                    if delBarang in stok:
                        valid_codes.append(delBarang)
                    else:
                        invalid_codes.append(delBarang)
                # Mengeluarkan output jika barang yang diinputkan oleh user tidak ada dalam stok
                if invalid_codes:
                    os.system("cls")
                    print(
                        f"Kode barang {', '.join(invalid_codes)} tidak ada dalam stok !!!"
                    )
                # Menampilkan data barang sesuai dengan code_barang yang diinputkan oleh user
                if valid_codes:
                    os.system("cls")
                    print()
                    print(
                        "+--------+---------------+-------------+-----------+----------+"
                    )
                    print(
                        "|  Kode  |    Kategori   |     Nama    |   Jumlah  |   Price  |"
                    )
                    print(
                        "+--------+---------------+-------------+-----------+----------+"
                    )
                    for delBarang in valid_codes:
                        kategori, nama, jumlah, harga = stok[delBarang]
                        print(
                            "| {:<6} | {:<13} | {:<11} | {:<9} | {:8} |".format(
                                delBarang, kategori, nama, jumlah, harga
                            )
                        )
                    print(
                        "+--------+---------------+-------------+-----------+----------+"
                    )
                    print()
                    delBarang1 = input(
                        "Apakah anda ingin menghapus data (Y/N) : "
                    ).upper()

                    # Mendelete barang apa bila user memilih menu Y
                    if delBarang1 == "Y":
                        for delBarang in valid_codes:
                            del stok[delBarang]
                        os.system("cls")
                        tabelstok()
                        print(
                            f"Barang dengan kode {', '.join(valid_codes)} telah dihapus dari stok."
                        )
                    else:
                        # Menghapus data akan dibatalkan jika user menginputkan N
                        print("Penghapusan data dibatalkan.")
                    break
                # Option jika barang yang diinputkan oleh user tidak berada dalam stok
                else:
                    print("Tidak ada kode barang yang valid dalam stok.")
                    print()
                    continue
        elif menudelBarang == "3":
            filter_delete_kategori()

            # UserInput kembali ke dashboard admin
            userInput = input("Kembali ke Dashboard Admin (Y/N) : ").upper()
            if userInput == "Y":
                os.system("cls")
                dashboardAdmin()
                break
            else:
                print("Thank you for visiting our warehouse")
                exit()
        elif menudelBarang == "4":
            os.system("cls")
            dashboardAdmin()
            break
        else:
            print("Masukkan angka 1-4 !!")
            print()
            continue
    # Kembali ke pilihan menu awal ketika user telah selesai
    userback1 = input("Kembali (Y/N) : ").upper()
    if userback1 == "Y":
        os.system("cls")
        dashboardAdmin()
    else:
        print("Thank you for visiting our warehouse")
        exit()


# Funtion menu utama sebelum user masuk
# Dashboard Admin
# Shopping cart
def mainMenu():
    print("=" * 50)
    print("||", " " * 14, "Gudang Barokah", " " * 14, "||")
    print("=" * 50)
    print("1.Admin Login  ")
    print("2.Shopping Cart  ")
    print("3.Exit Program  ")
    while True:
        inputMenuUtama = input("Masukkan pilihan anda [1-3]: ")
        # Memasukkan user ke dashboard admin
        if inputMenuUtama == "1":
            os.system("cls")
            adminLogin()
            break
        # Memasukkan user ke Shopping Cart
        elif inputMenuUtama == "2":
            os.system("cls")
            shoppingCart()
            break
        # End Program
        elif inputMenuUtama == "3":
            print("Thank you for visiting our warehouse")
            break
        else:
            print("Please input enter number 1-3")
            print()


mainMenu()
