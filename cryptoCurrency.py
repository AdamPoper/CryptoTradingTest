import requests
from candleStick import CandleStick

class CryptoCurrency:
    def __init__(self, ticker, label, url):
        super().__init__()
        self.ticker = ticker
        self.ticker_usd_label = label
        self.api_url = url
        self.candleSticks = []
        self.initPriceData()
        self.calculateMA3()
        self.calculateMA5()
        self.calculateMA20()
        self.calculateMA50()
    
    def initPriceData(self):
        response = requests.get(self.api_url)
        JSONdata = response.json()
        priceData = JSONdata['result'][self.ticker_usd_label]
        for i in priceData:
            cs = CandleStick()
            cs.supplyData(i)
            self.candleSticks.append(cs)  
    
    def calculateMA50(self):
        maLength = 50
        index = maLength
        while index < len(self.candleSticks):
            i = index - maLength
            ma50 = 0
            while i < index:
                ma50 += self.candleSticks[i].close
                i += 1
            ma50 /= maLength
            self.candleSticks[index].ma50 = round(ma50, 2)
            index += 1
            ma50 = 0
    
    def calculateMA20(self):
        maLength = 20
        index = maLength
        while index < len(self.candleSticks):
            i = index - maLength
            ma20 = 0
            while i < index:
                ma20 += self.candleSticks[i].close
                i += 1
            ma20 /= maLength
            self.candleSticks[index].ma20 = round(ma20, 2)
            index += 1
            ma20 = 0

    def calculateMA3(self):
        maLength = 3
        index = maLength
        while index < len(self.candleSticks):
            i = index - maLength
            ma3 = 0
            while i < index:
                ma3 += self.candleSticks[i].close
                i += 1
            ma3 /= maLength
            self.candleSticks[index].ma3 = round(ma3, 2)
            index += 1
            ma3 = 0
    
    def calculateMA5(self):
        maLength = 5
        index = maLength
        while index < len(self.candleSticks):
            i = index - maLength
            ma5 = 0
            while i < index:
                ma5 += float(self.candleSticks[i].close)
                i += 1
            ma5 /= maLength
            self.candleSticks[index].ma5 = round(ma5, 2)
            index += 1
            ma5 = 0

    def updateMA3(self):
        maLength = 3
        i = len(self.candleSticks) - 1
        ma3 = 0
        while i >= len(self.candleSticks) - maLength:
            ma3 += self.candleSticks[i].close
            i -= 1
        ma3 /= maLength
        self.candleSticks[-1].ma3 = round(ma3, 2)

    def updateMA5(self):
        maLength = 5
        i = len(self.candleSticks) - 1
        ma5 = 0
        while i >= len(self.candleSticks) - maLength:
            ma5 += self.candleSticks[i].close
            i -= 1
        ma5 /= maLength
        self.candleSticks[-1].ma5 = round(ma5, 2)

    def updateMA20(self):
        maLength = 20
        i = len(self.candleSticks) - 1
        ma20 = 0
        while i >= len(self.candleSticks) - maLength:
            ma20 += self.candleSticks[i].close
            i -= 1
        ma20 /= maLength
        self.candleSticks[-1].ma20 = round(ma20, 2)

    def updateMA50(self):
        maLength = 50
        i = len(self.candleSticks) - 1
        ma50 = 0
        while i >= len(self.candleSticks) - maLength:
            ma50 += self.candleSticks[i].close
            i -= 1
        ma50 /= maLength
        self.candleSticks[-1].ma50 = round(ma50, 2)

    def displayData(self):
        count = 1
        for i in self.candleSticks:
            print(f"{count}: ", i.toString())
            count += 1
