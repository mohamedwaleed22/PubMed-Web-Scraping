import requests 
from bs4 import BeautifulSoup
from tqdm import tqdm





## input is the seconed page after the search and filters to return a list of all pages 

def get_pages(first_page: str):
    page = requests.get(first_page)
    src = page.content
    soup = BeautifulSoup(src, 'lxml')

    ## number of pages for the loop 

    number = soup.find_all("div", {'class': 'page-number-wrapper'})

    input_tag = number[0].find('input', class_='page-number')
    max_value = int(input_tag['max'])
    
    all_pages = []
    for i in tqdm(range(1, max_value+1)):
        
        if '&page=' in first_page:
            
            pages = first_page.split('page')[0]
            pages_counter = pages + "page={}".format(i)
            all_pages.append(pages_counter)
            
        else:
            
            pages = first_page
            pages_counter = pages + "&page={}".format(i)
            all_pages.append(pages_counter)

    return all_pages