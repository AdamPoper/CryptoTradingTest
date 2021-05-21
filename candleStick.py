class CandleStick:
    def __init__(self):
        self.open  = -1
        self.high  = -1
        self.low   = -1
        self.close = -1
        self.ma20  = -1
        self.ma50  = -1
        self.ma3   = -1
        self.ma5   = -1
    
    def supplyData(self, data):
        self.open  = float(data[1])
        self.high  = float(data[2])
        self.low   = float(data[3])
        self.close = float(data[4])
        
    def toString(self):
        return f'Open: {self.open}, High: {self.high}, Low: {self.low}, Close: {self.close}, MA3: {self.ma3}, MA5: {self.ma5}'