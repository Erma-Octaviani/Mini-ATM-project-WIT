class ATMCard:
    def __init__(self, pin, saldo):
        self.pin = defaultPin
        self.saldo = defaultBalance

    def pin(self):
        return 'Nomor PIN Anda : ' + self.pin

    def balance(self):
        return 'Saldo Anda Saat ini : Rp' + str(self.saldo)
