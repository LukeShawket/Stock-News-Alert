from twilio.rest import Client


def message_content(percentage, icon, name, news_list):
    text_content = f"{name} {percentage}% {icon}\n"
    for key in range(0, 3):
        text_content += (f"\n{key+1}.{news_list[key]['title']}\n"
                        f"Description: {news_list[key]['description']}\n"
                        f"Source: {news_list[key]['url']}")
    print("Message formed!")
    return text_content


class Sender:
    def __init__(self, twilio_sid, twilio_token):
        self.ACCOUNT_SID = twilio_sid
        self.AUTH_TOKEN = twilio_token


    def send_sms(self, twilio_number, recipient, content):
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)
        message = client.messages.create(
            body=content,
            from_=twilio_number,
            to=recipient,
        )
        print(message.status)

