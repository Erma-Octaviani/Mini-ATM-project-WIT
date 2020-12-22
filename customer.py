from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPin, custBalance):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def pin(self):
        return 'Nomor PIN Anda : ' + str(self.custPin)

    def balance(self):
        return 'Saldo Anda Saat ini : Rp' + str(self.custBalance)

    def id_card(self):
        return 'Nomor kartu Anda : ' + str(self.id)

    def debet(self):
        nominal = int(input('Berapa uang yang akan diambil ?: Rp '))
        debet = self.custBalance - nominal
        return 'Saldo Anda saat ini : Rp ' + str(debet)

    def simpan(self):
        nominal = int(input('Berapa uang yang akan disimpan ?: Rp '))
        simpan = self.custBalance + nominal
        return 'Saldo Anda saat ini : Rp ' + str(simpan)
