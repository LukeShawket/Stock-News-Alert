import requests

class Stock:

    def __init__(self, end_point, apikey, symbol):
        stock_response = requests.get(f"{end_point}/{symbol}/prev?adjusted=true&apiKey={apikey}")
        stock_response.raise_for_status()
        self.stock_data = stock_response.json()
        self.close = self.stock_data['results'][0]["c"]
        self.open = self.stock_data['results'][0]["o"]
        stock_difference = abs(float(self.close) - float(self.open))
        stock_average = (float(self.close) + float(self.open)) / 2
        self.difference_percentage = (stock_difference / stock_average) * 100