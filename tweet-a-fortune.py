#Assignment 6
#class      CPSC 223p

from twitter import *
import random


access_token = ''
token_secret = ''
consumerkey = ''
consumer_secret = ''

t = Twitter(auth=OAuth(access_token, token_secret, consumerkey, consumer_secret))
x = random.randrange(1,5)


t = Twitter(auth=OAuth(access_token, token_secret, consumerkey, consumer_secret))
x = random.randrange(1,5)

conn = sqlite3.connect('freebsd_fortunes_clean.sl3')
c = conn.cursor()
stmt2 = 'select aphorism from fortunes order by random() limit 1'

for row in c.execute(stmt2):
    if len(row[0]) < 140:
        b = (row[0])
    else:
        c.execute(stmt2)
t.statuses.update(status = b)
conn.close()
if x == 1:
    status = "PTT ★ Dragon"
    with open("9-dragons-wallpaper.jpg", "rb") as imagefile:
        params = {"media[]": imagefile.read(), "status": status}
        t.statuses.update_with_media(**params)
        
elif x == 2:
    status = "PTT ★ Phoenix"
    with open("Phoenix-Logo-Widescreen-Wallpaper.jpg", "rb") as imagefile:
        params = {"media[]": imagefile.read(), "status": status}
        t.statuses.update_with_media(**params)
             
elif x == 3:
    status = "PTT ★ Gryphon"
    with open("th.jpg", "rb") as imagefile:
        params = {"media[]": imagefile.read(), "status": status}
        t.statuses.update_with_media(**params)
        
elif x == 4:
    status = "PTT ★ Chimera"
    with open("chimera.jpg", "rb") as imagefile:
        params = {"media[]": imagefile.read(), "status": status}
        t.statuses.update_with_media(**params)
        
elif x ==5:
    status = "PTT ★ Hydra"
    with open("hydra.jpg", "rb") as imagefile:
        params = {"media[]": imagefile.read(), "status": status}
        t.statuses.update_with_media(**params)
