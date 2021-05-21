import requests
import json
from clock import Clock
from candleStick import CandleStick
from currency import Currency
from cryptoCurrency import CryptoCurrency

def realTimeTradingAlgortithm():
    eth_data_url = 'https://api.kraken.com/0/public/OHLC?pair=ETHUSD&interval=1'
    eth_usd_label = 'XETHZUSD'
    etherium = CryptoCurrency('ETH', eth_usd_label, eth_data_url)
    realtime_url = 'https://api.kraken.com/0/public/Ticker?pair=ETHUSD'  
    tickClock = Clock()
    currencyClock = Clock()
    cs = CandleStick()
    originalInvestAmount = 1000
    money = originalInvestAmount
    investAmount = originalInvestAmount
    coinsOwned = 0       
    tradingAbove5ma = False
    totalOrders = 0
    while True:
        if tickClock.getElapsedTime() >= 1:
            resp = requests.get(realtime_url)
            JSONdata = resp.json()
            cs.close = float(JSONdata['result'][etherium.ticker_usd_label]['a'][0])             
            candleStickOps(cs, cs.close)            
            #print(f'Etherium: {cs.toString()}')
            tickClock.restart()  
        if currencyClock.getElapsedTime() >= 60:
            etherium.candleSticks.append(cs)
            etherium.updateMA3()
            etherium.updateMA5()            
            if etherium.candleSticks[-1].ma3 > etherium.candleSticks[-1].ma5 and not tradingAbove5ma:
                tradingAbove5ma = True
                coinsOwned = investAmount / cs.close
                money -= cs.close * coinsOwned
                print(f'Buy: {cs.close}, Money: {money}')
                totalOrders += 1
            elif etherium.candleSticks[-1].ma3 < etherium.candleSticks[-1].ma5 and tradingAbove5ma:
                tradingAbove5ma = False
                money += coinsOwned * cs.close
                print(f'Sell: {cs.close}, Money: {money}')
                totalOrders += 1
            print(f'Total Orders: {totalOrders}')
            #etherium.displayData()
            cs = CandleStick()
            currencyClock.restart()
             
def candleStickOps(cs, currentPrice):
    # handle minute open conditions
    if cs.open == -1:
        cs.open = currentPrice       
    if cs.low == -1:
        cs.low = currentPrice        
    if cs.high == -1:
        cs.high = currentPrice
    # adjust highs and lows
    if currentPrice > cs.high:
        cs.high = currentPrice
    if currentPrice < cs.low:
        cs.low = currentPrice

def tradeEtherium():
    eth_url = 'https://api.kraken.com/0/public/OHLC?pair=ETHUSD&interval=1'
    eth_usd_label = 'XETHZUSD'
    etherium = Currency('ETH', eth_usd_label, eth_url)
    #etherium.tradingAlgorithm3ma50ma()
    etherium.tradingAlgorithm3ma5ma()
    #etherium.tradingAlgorithm20ma50ma()
    #etherium.tradingAlgorithm3ma20ma()

def tradeDoge():
    doge_url = 'https://api.kraken.com/0/public/OHLC?pair=DOGEUSD&interval=1'
    doge_usd_label = 'XDGUSD'
    doge_coin = Currency('DOGE', doge_usd_label, doge_url)
    #doge_coin.tradingAlgorithm20ma50ma()
    doge_coin.tradingAlgorithm3ma5ma()
    #doge_coin.tradingAlgorithm3ma50ma()

def tradeBitcoin():
    btc_url = 'https://api.kraken.com/0/public/OHLC?pair=BTCUSD&interval=1'
    btc_usd_label = 'XXBTZUSD'
    bitcoin = Currency('BTC', btc_usd_label, btc_url)
    bitcoin.tradingAlgorithm3ma5ma()
    #bitcoin.tradingAlgorithm20ma50ma()


#tradeEtherium()
#tradeDoge()
#tradeBitcoin()
realTimeTradingAlgortithm()