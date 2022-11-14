import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


random_chapter = random.randint(1,21)

random_chapter = str(random_chapter)


webpage = 'https://biblehub.com/asv/john/' + random_chapter + '.htm'



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

page_verses = soup.findAll('span', class_='reftext')

print(page_verses)

verse_list = []

for verse in page_verses:
    verse_list = verse.text.split(".")

print(verse_list)

#myverse = f'Chapter: {random_chapter} Verse: {random.choice(verse_list[:len(verse_list)-2])}'

#print(myverse)

import keys2
from twilio.rest import Client

client = Client(keys2.accountSID, keys2.authToken)

TwilioNumber = "+16293488273"
myCellphone = "'+12105606588"

#textmsg = client.messages.create(to=myCellphone, from_=TwilioNumber,body=myverse)