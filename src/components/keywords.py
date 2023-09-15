import requests 
from bs4 import BeautifulSoup





def affKeyword(page: str):

    pageTest = requests.get(page)
    src = pageTest.content
    soup = BeautifulSoup(src, 'lxml')


    ### Affilliations done, each author has (name, affiliation numbers, affiliation text )

    authorlist = soup.find_all("div", {'class': 'authors-list'})

    authorss = authorlist[0].find_all('span', class_='authors-list-item')

    affiliation_dict = {}
    for author in authorss:
        name = author.find('a', class_='full-name').text
        affiliation_texts = [text['title'] for text in author.find_all('a', class_='affiliation-link')]
        affiliation_dict[name] = affiliation_texts


    # keywords 
    keywords = soup.find_all("div", {'class': 'abstract'})

    keywords_tag = keywords[0].find_all('p')[-1].text.strip().split('\n')[-1].strip()
    keywords_text = keywords_tag.split(';')
    keywords_text = ','.join(keywords_text).replace(".", "")

    
    return affiliation_dict, keywords_text