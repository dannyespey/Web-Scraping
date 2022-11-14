# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from dataclasses import replace
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url,  headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')


table_rows = soup.findAll("tr")


deathrate=0
lowdeathrate=100
lowdeathratestate = ''
deathratestate=''

testrate=0
lowtestrate=10000
lowtestratestate=''
testratestate=''



for row in table_rows[2:51]:
    td = row.findAll("td")

    statename = td[1].text
    deaths = int(td[4].text.replace(",",""))
    cases = int(td[2].text.replace(",",""))
    tests = int(td[10].text.replace(",",""))
    population = int(td[12].text.replace(",",""))

    
    newdeathrate = round(((deaths/cases)*100),2)
    if newdeathrate>deathrate:
        deathrate = newdeathrate
        deathratestate = statename

    if newdeathrate<lowdeathrate:
        lowdeathrate = newdeathrate
        lowdeathratestate = statename

    newtestrate = round(((tests/population)*100),2)
    if newtestrate>testrate:
        testrate = newtestrate
        testratestate = statename

    if newtestrate<lowtestrate:
        lowtestrate = newtestrate
        lowtestratestate = statename

    print(f'Highest Death Rate State: {deathratestate}')
    print(f'Highest Death Rate: {deathrate}%')
    print()
    print(f'Lowest Death Rate State: {lowdeathratestate}')
    print(f'Lowest Death Rate: {lowdeathrate}%')
    print()
    print(f'Highest Test Rate State: {testratestate}')
    print(f'Highest Test Rate: {testrate}%')
    print()
    print(f'Lowest Test Rate State: {lowtestratestate}')
    print(f'Lowest Test Rate: {lowtestrate}%')
    print()
    print()
    input()






#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

