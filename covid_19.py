import requests
import  pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from twilio.rest import Client

"""Sending request to the webpage.
"""
URL = "https://www.worldometers.info/coronavirus/#countries"
html_page = requests.get(URL).text
#print(html_page)

"""Extracting the table data using beautifulsoup.
1.Convert webpage sourcecode into xml data.
2.Then extract data from page step by step.
"""
soup = BeautifulSoup(html_page,'lxml')
get_table = soup.find("table",id="main_table_countries_today")
get_table_data = get_table.tbody.find_all("tr")
#print(get_table_data)

dic = {}
count = 0
for i in range(len(get_table_data)):
        count+=1;
        key  = get_table_data[i].find_all("td")[0].string
        value = get_table_data[i].find_all("td")[1].string
        if key == "India":
            print(key,value)
            print('HEY,MESSAGE HAS BEEN SENT!')
            client = Client('AC05649b9ed3ed42bbf4962a51c08df923', '073aef34c5d4d174182745551d40831b')
            client.messages.create(to = '+918210467848', from_ = '+12098854949', body = 'Updated Covid cases in India:, '+value+' link for more: '+URL)
