import requests 
from bs4 import BeautifulSoup
import json


def citePage(page: str):

    # Page + citations/
    citationlink = page + 'citations/'

    citeTest = requests.get(citationlink)
    src2 = citeTest.content

    soup2 = BeautifulSoup(src2, 'html.parser')
    data = soup2.text
    parsed_data = json.loads(data)
    format_text = parsed_data['nlm']['format']

    cite_list = format_text.split(". ")
    
    return cite_list