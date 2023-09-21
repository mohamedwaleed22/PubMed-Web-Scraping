
import requests 
from bs4 import BeautifulSoup


def get_citations(pmid):

    page = 'https://pubmed.ncbi.nlm.nih.gov/?linkname=pubmed_pubmed_citedin&from_uid={}&filter=simsearch1.fha'.format(pmid)

    pageTest = requests.get(page)
    src = pageTest.content
    soup = BeautifulSoup(src, 'lxml')

    num = soup.find_all("div", {'class': 'results-amount'})
    if num:

        num = num[0].find("span", {'class': 'value'})
        num = int(num.text) - 1
        return num
    else:
        return 0