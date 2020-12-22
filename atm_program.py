print('Selamat Datang di ATM Progate!')

from customer import Customer
customer1 = Customer(400000078321540, 1234, int(10000))

menu_utama = -1

while menu_utama < 0 or menu_utama > 2:
    print('\n\t\tMenu Utama')
    print('1. Membuat rekening baru')
    print('2. Masuk ke rekening(log in)')
    print('0. Keluar')

    menu_utama = int(input('Silahkan pilih menu utama (0-2)? : '))

    if menu_utama == 1:
        name = input('Silahkan masukkan nama Anda ? : ')
        date = input('Silahkan masukkan tanggal lahir Anda (ddmmyyy) ? : ')
        mother = input('Silahkan masukkan nama Ibu kandung Anda ?: ')

        print('Kartu Anda telah selesai dibikin.')

        print(customer1.id_card())
        print(customer1.pin())

        menu_utama = -1

    elif menu_utama == 0:
        print('Terima kasih. Silahkan ambil Kartu Anda !')
        exit()

    elif menu_utama < 0 or menu_utama > 2:
        print("SALAH! pilihan menu tidak valid!")
        menu_utama = int(input('Silahkan pilih menu utama (0-2)? : '))

    else:
        print('Anda sukses masuk (log in)!')

        tries = 0
        while tries < 3:
            pin = int(input('Masukkan Pin Anda! '))

            if pin == customer1.custPin:
                menu_transaksi = 0
                while menu_transaksi <=0 or menu_transaksi > 7:
                    print('\n\t\tMenu Transaksi')
                    print('1. Periksa Pin')
                    print('2. Ganti Pin')
                    print('3. Cek Saldo')
                    print('4. Debet/Withdraw')
                    print('5. Simpan/Deposit')
                    print('6. Keluar')
                    print('7. Cetak Ringkasan Transaksi')

                    transaksi = int(input('Silahkan pilih menu transaksi (1-7)?: '))
                    saldo = int(10000)

                    if transaksi == 1:
                        print(customer1.pin())
                        menu_transaksi = 0

                    elif transaksi == 2:
                        print('Pin lama Anda : ' + str(customer1.custPin))
                        pin = int(input('Pin baru Anda ? : '))
                        menu_transaksi = 0

                    elif transaksi == 3:
                        print(customer1.balance())
                        menu_transaksi = 0

                    elif transaksi == 4:
                        print(customer1.balance())
                        nominal = int(input('Berapa uang yang akan diambil ?: Rp '))
                        debet = customer1.custBalance - nominal

                        if debet >= 0:
                            print(customer1.debet())
                            menu_transaksi = 0
                        else:
                            print('Saldo Anda tidak cukup')
                            menu_transaksi = 0

                    elif transaksi == 5:
                        simpan = customer1.custBalance + nominal
                        print(customer1.simpan())
                        menu_transaksi = 0

                    elif transaksi == 6:
                        tries = 3
                        break

                    elif transaksi == 7:
                        print(x.strftime("%A") + ', ' + x.strftime("%d") + ' ' + x.strftime("%B") + ' ' + x.strftime("%Y"))
                        print(customer1.balance())
                        print(customer1.debet())
                        print(customer1.simpan())
                        menu_transaksi = 0

                    else:
                        print('SALAH nomor menu transaksi!!')
                        menu_transaksi = 0

            elif tries == 2:
                print('Error. Silahkan ambil kartu Anda dan coba lagi..')
                exit()
            else:
                print('Pin Anda Salah! Silahkan Masukkan lagi Pin Anda! : ')
                tries += 1
