#class      CPSC 223p
#assignment 7
import yweather
import sys
import smtplib
from email.mime.text import MIMEText
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
    snset = weather['astronomy']  
    todaysforecast = weather['forecast'][0]
    forecaststring = '{} {} high: {}, low: {} {} sunset is at {}'.format( location, todaysforecast['date'], todaysforecast['high'],todaysforecast['low'], todaysforecast['text'], snset['sunset'])
    sendText(forecaststring, sys.argv[3]
    
    
if __name__== "__main__":
    main()

