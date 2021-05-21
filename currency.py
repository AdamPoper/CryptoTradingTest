import requests
from candleStick import CandleStick

class Currency:
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

    def tradingAlgorithm20ma50ma(self):
        money = 1000
        investAmount = money
        coinsOwned = 0       
        tradingAbove50ma = False
        for stick in self.candleSticks:
            if stick.ma20 > stick.ma50 and not tradingAbove50ma:
                tradingAbove50ma = True   
                coinsOwned = investAmount / stick.close           
                money -= stick.close * coinsOwned             
                print(f'Buy: {stick.close}, Money: {money}')
            elif stick.ma20 < stick.ma50 and tradingAbove50ma:
                tradingAbove50ma = False
                money += coinsOwned * stick.close 
                print(f'Sell: {stick.close}, Money: {money}') 

    def tradingAlgorithm3ma5ma(self):
        originalInvestAmount = 1000
        money = originalInvestAmount
        investAmount = originalInvestAmount
        coinsOwned = 0       
        tradingAbove5ma = False
        totalOrders = 0
        previousBuyPrice = 0
        for stick in self.candleSticks:
            if money < originalInvestAmount:
                investAmount = money
            else:
                investAmount = originalInvestAmount
            if stick.ma3 > stick.ma5 and not tradingAbove5ma:
                tradingAbove5ma = True   
                coinsOwned = investAmount / stick.close           
                money -= stick.close * coinsOwned             
                print(f'Buy: {stick.close}, Money: {money}')
                totalOrders += 1 
                previousBuyPrice = stick.close
            elif (stick.ma3 < stick.ma5 and tradingAbove5ma):
                tradingAbove5ma = False
                money += coinsOwned * stick.close 
                print(f'Sell: {stick.close}, Money: {money}') 
                totalOrders += 1
        print(f'Total Orders: {totalOrders}')

    def tradingAlgorithm3ma20ma(self):
        originalInvestAmount = 1000
        money = originalInvestAmount
        investAmount = originalInvestAmount
        coinsOwned = 0       
        tradingAbove20ma = False
        totalOrders = 0
        previousBuyPrice = 0
        for stick in self.candleSticks:
            if money < originalInvestAmount:
                investAmount = money
            else:
                investAmount = originalInvestAmount
            if stick.ma3 > stick.ma20 and not tradingAbove20ma:
                tradingAbove20ma = True   
                coinsOwned = investAmount / stick.close           
                money -= stick.close * coinsOwned             
                print(f'Buy: {stick.close}, Money: {money}')
                totalOrders += 1 
                previousBuyPrice = stick.close
            elif (stick.ma3 < stick.ma20 and tradingAbove20ma):
                tradingAbove20ma = False
                money += coinsOwned * stick.close 
                print(f'Sell: {stick.close}, Money: {money}') 
                totalOrders += 1
        print(f'Total Orders: {totalOrders}')

    def tradingAlgorithm3ma50ma(self):
        money = 1000
        totalOrders = 0
        investAmount = money
        coinsOwned = 0       
        tradingAbove50ma = False
        for stick in self.candleSticks:
            if stick.ma3 > stick.ma50 and not tradingAbove50ma:
                tradingAbove50ma = True   
                coinsOwned = investAmount / stick.close           
                money -= stick.close * coinsOwned             
                print(f'Buy: {stick.close}, Money: {money}')
                totalOrders += 1
            elif stick.ma3 < stick.ma50 and tradingAbove50ma:
                tradingAbove50ma = False
                money += coinsOwned * stick.close 
                print(f'Sell: {stick.close}, Money: {money}')
                totalOrders += 1
        print(f'Total Orders: {totalOrders}')

    def displayData(self):
        count = 1
        for i in self.candleSticks:
            print(f"{count}: ", i.toString())
            count += 1