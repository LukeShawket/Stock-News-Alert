import requests

class News:

    def __init__(self, api_key, end_point):
        self.NEWS_END_PONT = end_point
        self.NEWS_API_KEY = api_key
        self.news_list = []


    def get_news(self, q, day, lan):
        news_params = {
            "qInTitle": q,
            "from": day,
            "sortBy": "popularity",
            "language": lan,
            "apikey": self.NEWS_API_KEY
        }
        news_response = requests.get(self.NEWS_END_PONT, params=news_params)
        news_data = news_response.json()

        self.news_list = [news_data['articles'][i] for i in range(1, 4)]

