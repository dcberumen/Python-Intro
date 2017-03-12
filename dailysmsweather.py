#class      CPSC 223p
#assignment 7
import yweather
import sys
import smtplib
import time
from twilio.rest import TwilioRestClient

    
def sendText(text, phone):
    account_sid = ''
    auth_token = ''
    client2 = TwilioRestClient(account_sid, auth_token)
    client2.messages.create(body = text,to = '+' + phone, from_ = "")
    


def main():
    client = yweather.Client( )
    woeid = client.fetch_woeid(sys.argv[1])
    weather = client.fetch_weather(woeid, metric = False)
    location = '{}, {}'.format(weather['location']['city'], weather['location']['region'])
    todaysforecast = weather['forecast'][0]
    forecaststring = '{} {} high: {}, low: {} {}'.format( location, todaysforecast['date'], todaysforecast['high'],todaysforecast['low'], todaysforecast['text'])
    while True:
        if time.strftime("%H") == "12" and time.strftime("%M") == "00":
            sendText(forecaststring,sys.argv[3])
            time.sleep(86400)
if __name__== "__main__":
    main()

