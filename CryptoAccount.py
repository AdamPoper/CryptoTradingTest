from cryptoCurrency import CryptoCurrency

class CryptoAccount:
    def __init__(self, money):
        super().__init__()
        self.funds = money
        self.currency = CryptoCurrency()
        