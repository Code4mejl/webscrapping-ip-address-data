import requests
from bs4 import BeautifulSoup
url ='https://myip.ms/browse/blacklist/Blacklist_IP_Blacklist_IP_Addresses_Live_Database_Real-time'
response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')
ipList = soup.select(".row_name")
with open('ip_output.csv', 'w') as f:
    for ips in ipList:
        f.write(ips.find('a').text + '\n')