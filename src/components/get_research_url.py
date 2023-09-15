import requests 
from bs4 import BeautifulSoup
from tqdm import tqdm




## takes a list of all pages of the search and returns a list of all the research in each page

def get_research_urls(pages_list: list):
    all_urls = []
    for page in tqdm(pages_list):
        pages = requests.get(page)
        src = pages.content
        soup = BeautifulSoup(src, 'lxml')
        
        ## get every hyperlink in the page
        links = soup.find_all("a", {'class': 'docsum-title'})
        for link in links:
            id2 = link['data-article-id']
            urls = "https://pubmed.ncbi.nlm.nih.gov/{}/".format(id2)
            all_urls.append(urls)
    return all_urls