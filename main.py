import os

# Kelas Node untuk merepresentasikan node pada Binary Search Tree (BST)
class Node:
    def __init__(self, value):
        self.value = value      # Menyimpan data barang dalam bentuk dictionary
        self.right = None       # Node anak kanan
        self.left = None        # Node anak kiri

# Kelas BinarySearchTree untuk mengelola data stok barang menggunakan BST
class BinarySearchTree:
    def __init__(self):
        self.root = None        # Root dari BST

    # Fungsi untuk menambahkan barang baru ke dalam BST
    def insertBarang(self, value):
        newNode = Node(value)
        if self.root is None:   # Jika BST masih kosong, jadikan node baru sebagai root
            self.root = newNode
            return True
        temp = self.root
        while(True):
            # Jika SKU sudah ada, tidak bisa menambah barang yang sama
            if newNode.value["no.SKU"] == temp.value["no.SKU"]:
                return False
            # Jika SKU lebih kecil, bergerak ke kiri
            if newNode.value["no.SKU"] < temp.value["no.SKU"]: 
                if temp.left is None:
                    temp.left = newNode
                    return True
                temp = temp.left
            # Jika SKU lebih besar, bergerak ke kanan
            else:
                if temp.right is None:
                    temp.right = newNode
                    return True
                temp = temp.right

    # Fungsi untuk mencari barang berdasarkan SKU pada BST
    def containsInputBarang(self, value):
        temp = self.root
        while (temp is not None):
            if value["no.SKU"] < temp.value["no.SKU"]:
                temp = temp.left
            elif value["no.SKU"] > temp.value["no.SKU"]:
                temp = temp.right
            else:
                return temp      # Mengembalikan node jika ditemukan
        return None             # Jika tidak ditemukan

# Inisialisasi objek BST untuk stok barang
stok = BinarySearchTree()
# List untuk menyimpan data transaksi konsumen
databaseTransaksi = []

# Fungsi untuk mengurutkan data transaksi berdasarkan subtotal secara descending
def urutanSubtotal(database):
    for i in range(len(database)-1):
        index = i
        for j in range(i+1, len(database)):
            if database[j][3] > database[index][3]:
                index = j
        if i != index:
            temp = database[i]
            database[i] = database[index]
            database[index] = temp
    return database

# Fungsi utama untuk menampilkan menu dan mengelola seluruh proses aplikasi
def gudangBelanja():
    while (True):
        os.system("cls")    # Membersihkan layar terminal
        print("|==========================================|")
        print("|======== Pilih Menu Yang Tersedia ========|")
        print("|==========================================|")
        print("|          1. Kelola Stok Barang           |")
        print("|       2. Kelola Transaksi Konsumen       |")
        print("|                 0. Exit                  |")
        print("|==========================================|")

        pilihMenu = input("Pilih Menu yang akan anda gunakan: ")
        if pilihMenu == "1":
            # Menu untuk mengelola stok barang
            while(True):
                os.system("cls")
                print("|==========================================|")
                print("|=========== Menu Kelola Barang ===========|")
                print("|==========================================|")
                print("|          1.1. Input Stok Barang          |")
                print("|          1.2. Update Stok Barang         |")
                print("|          0. Kembali ke menu utama        |")
                print("|==========================================|")

                pilihMenu = input("Pilih menu untuk mengelola stok barang: ")

                if pilihMenu == "1.1":
                    # Menu untuk input barang baru ke gudang
                    while (True):
                        print("|==========================================|")
                        print("|========== Inputkan Data Barang ==========|")
                        print("|==========================================|")
                        try:
                            NoSKU = int(input("Inputkan Nomer SKU Dari Barang: "))
                            nowStock = stok.containsInputBarang({"no.SKU" : NoSKU})
                            # Validasi SKU harus 4 digit
                            if NoSKU < 1000 or NoSKU > 9999:
                                print("Harap isi ulang kembali, inputkan nomer SKU 4 digit")
                                continue
                            # Cek apakah SKU sudah ada di BST
                            elif nowStock:
                                print("Maaf barang dengan No.SKU ini sudah tersedia!")
                                continue
                            else:
                                print("Barang dengan No.SKU ini belum tersedia, anda bisa menambahkannya dalam gudang!")
                        except ValueError:
                            print("Masukan dengan Angka yang benar untuk No.SKU")
                            continue

                        # Input nama barang, validasi tidak boleh kosong
                        NamaBarang = str(input("Inputkan Nama Dari Barang: "))
                        if NamaBarang == "":
                            print("Nama barang tidak boleh kosong")
                            continue
                        try:    
                            # Input harga satuan dan jumlah stok, validasi harus angka
                            HargaSatuan = int(input("Inputkan Harga Satuan Dari Barang: "))
                            JumlahStok = int(input("Inputkan Jumlah Stok Dari Barang: "))
                        except ValueError:
                            print("Inputkan harga yang benar untuk Harga dan Jumlah")
                            continue
                        
                        # Membuat dictionary data barang
                        database = {
                            "no.SKU": NoSKU,
                            "NamaBarang" : NamaBarang,
                            "HargaSatuan" : HargaSatuan,
                            "JumlahStok" : JumlahStok
                        }
                        # Menambahkan barang ke BST
                        if stok.insertBarang(database):
                            print("Barang berhasil ditambahkan!")
                        else:
                            print("Maaf, barang ini tidak bisa ditambahkan! Barang ini masih ada")
                        os.system("pause")
                        break

                elif pilihMenu == "1.2":
                    # Menu untuk menambah stok barang yang sudah ada
                    while(True):
                        print("|==========================================|")
                        print("|========== Restok Jumlah Barang ==========|")
                        print("|==========================================|")
                        try:
                            NoSKU = int(input("Inputkan Nomer SKU Dari Barang: "))
                            # Validasi SKU harus 4 digit
                            if NoSKU < 1000 or NoSKU > 9999:
                                print("Harap isi ulang kembali, inputkan nomer SKU 4 digit")
                                continue
                        except ValueError:
                            print("Masukan dengan Angka yang benar untuk No.SKU")
                            continue            
                        # Mencari barang berdasarkan SKU
                        # Jika barang tidak ditemukan, tampilkan pesan
                        stockBarang = stok.containsInputBarang({"no.SKU" : NoSKU})
                        if stockBarang is None:
                            print("Maaf barang tidak ditemukan, silahkan inputkan barang ini terlebih dahulu!")
                        else:
                            try:
                                # Input jumlah stok yang ingin ditambahkan
                                tambahStok = int(input("Inputkan jumlah stok: "))
                                # Menambah jumlah stok pada barang yang ditemukan
                                stockBarang.value["JumlahStok"] += tambahStok
                                print(f"Stok barang pada No.SKU : {NoSKU} berhasil ditambah\ntotal barang saat ini: { stockBarang.value['JumlahStok']}")
                            # Validasi input harus angka
                            except:
                                print("Masukan jumlah stok dengan Angka yang benar")
                                continue
                        os.system("pause")
                        break
                elif pilihMenu == "0":
                    break

        elif pilihMenu == "2":
            # Menu untuk mengelola transaksi konsumen
            while(True):
                os.system("cls")
                print("|======================================================|")
                print("|=========== Menu Kelola Transaksi Konsumen ===========|")
                print("|======================================================|")
                print("|            2.1. Input Data Transaksi Baru            |")
                print("|         2.2. Lihat Seluruh Transaksi Konsumen        |")
                print("|    2.3. Lihat Data Transaksi Berdasarkan Subtotal    |")
                print("|              0. Kembali ke menu utama                |")
                print("|======================================================|")

                pilihMenu = input("Pilih menu untuk mengelola transaksi: ")

                if pilihMenu == "2.1":
                    # Menu untuk input transaksi baru
                    while(True):
                        print("|==========================================|")
                        print("|=======Inputkan Transaksi Konsumen========|")
                        print("|==========================================|")
                        while (True):
                            NamaUser = str(input("Inputkan Nama Dari Kosumen: "))
                            if NamaUser == "":
                                print("Nama konsumen tidak boleh kosong")
                                continue
                            else:
                                break

                        while(True):
                            try:
                                NoSKU = int(input("Inputkan Nomer SKU Dari Barang: "))
                                stockBarang = stok.containsInputBarang({"no.SKU" : NoSKU})
                                # Validasi SKU harus 4 digit dan barang harus ada
                                if NoSKU < 1000 or NoSKU > 9999:
                                    print("Harap isi ulang kembali, inputkan nomer SKU 4 digit")
                                    continue
                                elif stockBarang is None:
                                    print("Maaf barang tidak ditemukan!!")
                                    lanjutKan = input("Kembali Input lagi?(y/n)").lower()
                                    if lanjutKan == "y":
                                        continue
                                    else:
                                        break #Jika user memilih 'n'akan kembali ke menu kelola transaksi
                                else:
                                    break #Jika barang ditemukan, lanjutkan ke input harga satuan dan jumlah stok
                            # Jika input tidak valid, tampilkan pesan kesalahan
                            except ValueError:
                                print("Masukan dengan Angka yang benar untuk harga satuan atau jumlah stok")
                                continue  
                        # Kondisi ini untuk memasitakan jika user memilih 'n' pada input SKU dan barang tidak ditemukan
                        # Kondisi ini untuk mencegah input jumlah barang jika SKU tidak ditemukan
                        if stockBarang is None:
                            os.system("pause")  
                            break
                            
                        while(True):
                            jumlahBelibarang = int(input("Masukan Jumlah barang yang akan dibeli: "))
                            try:
                                # Cek apakah stok cukup
                                if stockBarang.value["JumlahStok"] >= jumlahBelibarang:
                                    # Kurangi stok barang
                                    stockBarang.value["JumlahStok"] -= jumlahBelibarang
                                    # Hitung subtotal transaksi
                                    subTotal = stockBarang.value["HargaSatuan"]*jumlahBelibarang
                                    # Simpan data transaksi ke list
                                    dataPembelian = [NamaUser, NoSKU, jumlahBelibarang, subTotal]
                                    databaseTransaksi.insert(0, dataPembelian)
                                    print(f"Transaksi Berhasi total belanja anda adalah Rp{subTotal}\nStok Barang saat ini dalam gudang yaitu {stockBarang.value['JumlahStok']}")
                                    break
                                else:
                                    print("Stok barang tidak cukup!!!")
                                    lanjutKan = input("Kembali Input lagi?(y/n)").lower()
                                    if lanjutKan != "y":
                                            break
                            except ValueError:
                                print("Masukan jumlah yang akan dibeli dengan benar!!!")
                                continue
                        if stockBarang:
                            print("Data transaksi sudah tersimpan!!")
                        else:
                            break
                        lanjutKan = input("Kembali Transaksi lagi?(y/n)").lower()
                        if lanjutKan != "y":
                            os.system("pause")
                            break

                elif pilihMenu == "2.2":
                    # Menu untuk menampilkan seluruh data transaksi
                    while(True):
                        os.system("cls")
                        print("|==========================================|")
                        print("|========Daftar Transaksi Konsumen=========|")
                        print("|==========================================|")
                        for data in  databaseTransaksi:
                            print(f"Nama = {data[0]}, No.SKU = {data[1]}, Jumlah barang yang dibeli = {data[2]}, Subtotal belanjaan = {data[3]}")
                        os.system("pause")
                        break

                elif pilihMenu == "2.3":
                    # Menu untuk menampilkan data transaksi yang sudah diurutkan berdasarkan subtotal
                    while (True):
                        os.system("cls")
                        print("|==========================================|")
                        print("|========Daftar Subtotal Transaksi=========|")
                        print("|==========================================|")
                        urutanSubtotal(databaseTransaksi)
                        for data in  databaseTransaksi:
                            print(f"Nama = {data[0]}, No.SKU = {data[1]}, Jumlah barang yang dibeli = {data[2]}, Subtotal belanjaan = {data[3]}")
                        os.system("pause")
                        break
                elif pilihMenu == "0":
                    break
        elif pilihMenu == "0":
            # Keluar dari aplikasi
            print("Terimakasih dan sampai jumpa!")
            os.system("pause")
            break

# Memanggil fungsi utama untuk menjalankan aplikasi
gudangBelanja()