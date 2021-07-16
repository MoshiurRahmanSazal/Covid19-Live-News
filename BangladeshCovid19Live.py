from collections import namedtuple
import requests
from lxml import html

covid_data = namedtuple("covid_data", "cases deaths recovered")
def covid_stats (url: str = "https://www.worldometers.info/coronavirus/country/bangladesh/") \
    -> covid_data:
    xpath_str = '//div[@class = "maincounter-number"]/span/text()'
    return covid_data(*html.fromstring(requests.get(url).content).xpath(xpath_str))


fmt = """ 
In Bangladesh:
\nTotal COVID-19 Positive: {}
Total Deaths: {}
Total Recovered: {}"""
print(fmt.format(*covid_stats()))