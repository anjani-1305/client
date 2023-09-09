class StockDataProcessor:
    def __init__(self, stock_A_data, stock_B_data):
        self.stock_A_data = stock_A_data
        self.stock_B_data = stock_B_data

    def getDataPoint(self, stock_data):
        stock_name = stock_data['name']
        bid_price = stock_data['bid_price']
        ask_price = stock_data['ask_price']
        price = (bid_price + ask_price) / 2
        return (stock_name, bid_price, ask_price, price)

    def getRatio(self):
        stock_A_price = self.getDataPoint(self.stock_A_data)[-1]
        stock_B_price = self.getDataPoint(self.stock_B_data)[-1]

        if stock_B_price == 0:
            return "Undefined (division by zero)"
        else:
            return stock_A_price / stock_B_price


