import get_stock
import news_picker
import sms_sender
import os

STOCK_API_KEY = os.getenv("MY_STOCK_API_KEY")
NEWS_API_KEY = os.getenv("MY_NEWS_API_KEY")
TWILIO_NUMBER = "MY_TWILIO_NUMBER"
TWILIO_SID = os.getenv("MY_TWILIO_SID")
TWILIO_TOKEN = os.environ['MY_TWILIO_TOKEN']
RECIPIENT_NUMBER = os.environ['RECIPIENT_PHONE_NUMBER']

STOCK_END_POINT = "https://api.polygon.io/v2/aggs/ticker"
NEWS_END_POINT = "https://newsapi.org/v2/everything"
COMPANY_NAME = "NVIDIA"
STOCK_NAME = "NVD"

stock = get_stock.Stock(STOCK_END_POINT, STOCK_API_KEY, STOCK_NAME)
news = news_picker.News(NEWS_API_KEY, NEWS_END_POINT)
message_sender = sms_sender.Sender(TWILIO_SID, TWILIO_TOKEN)
dif_per = round(stock.difference_percentage)

stock_changes_icon = ""
if float(stock.close) > float(stock.open):
    stock_changes_icon = "📈"
elif float(stock.close) < float(stock.open):
    stock_changes_icon = "📉"
else:
    pass

stock_days_list = list(stock.stock_data.keys())
news_day = stock_days_list[0]

if dif_per > 1.0:
    news.get_news(COMPANY_NAME, news_day, "en")
    text_content = sms_sender.message_content(dif_per, stock_changes_icon, COMPANY_NAME, news.news_list)

    message_sender.send_sms(TWILIO_NUMBER, RECIPIENT_NUMBER, text_content)