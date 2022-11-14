from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import keys2
from twilio.rest import Client

client = Client(keys2.accountSID, keys2.authToken)

TwilioNumber = "+16293488273"
myCellphone = "'+12105606588"

url = 'https://cryptoslate.com/coins/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
		
req = Request(url,  headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

table_rows = soup.findAll("tr")

for row in table_rows[0:6]:
    td = row.findAll("td")
    if td:
        rank = td[0].text
        print(f'Rank:{rank}')

        name = td[1].text
        print(f'Name/Ticker:{name}')

        price = td[2].text.replace(",","")
        print(f'Price: {price}')

        pchange = td[3].text
        print(f'% Change: {pchange}')
    
        price = price.replace("$","").replace(",","")
        price = float(price)

        pchange = pchange.replace("%","").replace("+","")
        pchange = float(pchange)/100
        corresponding_price = round(price/(1+pchange),2)
        
        print(f'Before Price: ${corresponding_price}')
        print()
        print()

        if 'Bitcoin BTC' in name and price<40000:
            textmsg = client.messages.create(to=myCellphone, from_=TwilioNumber,body=
            'Bitcoin has dropped below $40,000!')
            
        if 'Ethereum ETH' in name and price<3000:
            textmsg = client.messages.create(to=myCellphone, from_=TwilioNumber,body=
            'Ethereum has dropped below $3,000!')
        
        input()

#if the value falls below $40,000 for BTC and $3,000 for ETH






