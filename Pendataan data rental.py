import time
import os
from termcolor import colored

def proses_animasi(pesan):
    for i in range(10):
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        titik = '.' * (i % 4)
        print(f"{pesan}{titik}")

def tambah_data_rental(rental_data):
    while True:
        nama = input("Masukkan Nama Penyewa: ")
        mobil = input("Masukkan Tipe Mobil: ")

        durasi = input("Masukkan Durasi Sewa (hari): ")
        while not durasi.isdigit():
            print("Durasi harus berupa angka. Silakan coba lagi")
            durasi = input("Masukkan Durasi Sewa (hari): ")
        durasi = int(durasi)

        harga = input("Masukkan Harga Sewa per Hari: ")
        while not harga.isdigit():
            print("Harga harus berupa angka. Silakan coba lagi")
            harga = input("Masukkan Harga Sewa per Hari: ")
        harga = int(harga)

        rental_data.append([nama, mobil, durasi, harga])
        proses_animasi("Menambahkan data rental")

        pilihan = input("Apakah Anda ingin menambahkan data lagi? (y/n): ")
        if pilihan.lower() != 'y':
            break

def simpan_ke_file(rental_data):
    with open("data_rental.txt", "w") as file:
        for data in rental_data:
            file.write(f"{data[0]},{data[1]},{data[2]},{data[3]}\n")
    proses_animasi(f"Menyimpan data ke data_rental.txt")

def baca_dari_file():
    rental_data = []
    try:
        with open("data_rental.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                rental_data.append(data)
        proses_animasi(f"Membaca data dari data_rental.txt")
    except FileNotFoundError:
        print(f"File data_rental.txt tidak ditemukan")
    
    return rental_data

def tampilkan_menu():
    print(colored("         Menu", "light_blue"))
    print(colored("="*25, "light_blue"))
    print("1. Tambah Data Rental")
    print("2. Tampilkan Data Rental")
    print("3. Simpan Data ke File")
    print("4. Baca Data dari File")
    print(colored("5. Keluar", "red"))
    print(colored("="*25, "light_blue"))

def tampilkan_data_rental(rental_data):
    if rental_data:
        print(colored("                              Data Rental Mobil Natia                 ", "red"))
        print(colored("="*80, "cyan"))
        print(f"{'No':<5} {'Nama':<20} {'Mobil':<18} {'Durasi (hari)':<18} {'Harga per hari':<15}")
        print(colored("="*80, "cyan"))

        for i, data in enumerate(rental_data):
            print(f"{i + 1:<5} {data[0]:<20} {data[1]:<18} {data[2]:<18} {data[3]:<15}")
    else:
        print(colored("Tidak ada data rental yang tersedia.", "red"))

def login():
    username = "natia"
    password = "sukses123"

    print(colored("Silakan login terlebih dahulu", "yellow"))
    input_username = input("Username: ")
    input_password = input("Password: ")

    if input_username == username and input_password == password:
        print(colored("Login berhasil!", "green"))
        return True
    else:
        print(colored("Username atau password salah.", "red"))
        return False

def main():
    if not login():
        return
    
    rental_data = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == '1':
            tambah_data_rental(rental_data)
        elif pilihan == '2':
            tampilkan_data_rental(rental_data)
        elif pilihan == '3':
            simpan_ke_file(rental_data)
        elif pilihan == '4':
            rental_data = baca_dari_file()
            tampilkan_data_rental(rental_data)  
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program rental mobil")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi 1-5!")

main()
