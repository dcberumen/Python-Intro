#class      CPSC 223p
#assignment 7
import yweather
import sys
import smtplib
import time
from twilio.rest import TwilioRestClient

def sendText(text, phone)
    account_sid = ''
    auth_token = ''
    client2 = TwilioRestClient(account_sid, auth_token)
    client2.messages.create(body = text,to = '+' + phone, from_ = "")
    

def main()
    client = yweather.Client( )
    woeid = client.fetch_woeid(sys.argv[1])

    while True:
        weather = client.fetch_weather(woeid, metric = False)
        timesethour = int(weather['astronomy']['sunset'][0:1])
        timesetmin = int(weather['astronomy']['sunset'][2:4])
        if weather['astronomy']['sunset'][5:7] == 'pm':
             timesethour += 12
        awakentime = timesethour*60*60+timesetmin*60 - 300
        sleeptillsunset = time.localtime().tm_hour*60*60 + time.localtime().tm_min*60
        if sleeptillsunset > awakentime:
            sleeptillsunset = 0
            time.sleep(86400-sleeptillsunset + 10800)
        else:
            time.sleep(awakentime - sleeptillsunset)
            sentText('Sunset is in 5 minutes', sys.argv[3])
            time.sleep(60)
            
if __name__== "__main__":
    main()

        
