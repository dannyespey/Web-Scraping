from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url = 'https://www.webull.com/quote/us/gainers'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
		
req = Request(url,  headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

#print(title.text)

tablecells = soup.findAll("div", attrs={"class":"table-cell"})

#print(f'{tablecells[0].text} {tablecells[1].text} \nPercent Change: {tablecells[3].text} \nLast Price: {tablecells[4].text}')

#or

#for cell in tablecells[:7]:
    #print(cell.text)

counter = 1

for x in range(5):
    name = tablecells[counter].text
    change = tablecells[counter+2].text
    high = float(tablecells[counter+4].text)
    low = float(tablecells[counter+5].text)

    calc_change = round(((high - low)/low)*100,2)

    print(name)
    print(f'% Change on Webpage: {change}')
    print(f'High: {high}')
    print(f'Low: {low}')
    print(f'Calculated Change %: {calc_change}%')
    print()
    print()
    counter+=11

#print(((float(tablecells[5].text)-float(tablecells[6].text))/float(tablecells[6].text))*100)

#print(((float(tablecells[16].text)-float(tablecells[17].text))/float(tablecells[17].text))*100)

#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

