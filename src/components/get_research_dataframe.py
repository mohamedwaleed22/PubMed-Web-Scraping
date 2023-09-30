from tqdm import tqdm
from src.components.keywords import affKeyword
from src.components.cite_page import citePage
from src.components.cite_info import citeInfo
from src.components.num_citations import get_citations
import pandas as pd

# old 
# df = pd.DataFrame(
#             columns=["Title", "PMID", "Authors", "Citation", "First_Author", "Journal/Book"
#                      , "Publication_Year/Date","PMCID", "DOI", "Keywords", "Country", "N_Citations", "Authors/Affiliations"])

def getResearchDataFrame(pages: list):


    df = pd.DataFrame(
            columns=["Title", "PMID", "Authors", "Citation", "First_Author", "Journal/Book"
                     , "Publication_Year/Date","PMCID", "DOI", "Keywords", "Country", "N_Citations", "Authors/Affiliations"])
    emptyPages = []
    
    for page in tqdm(pages):

        pmid1 = page.split('/')[-2]
        
        keywords_text, country , affiliation_dict = affKeyword(page)
        cite_list = citePage(page)
        authors, title, journal, _, pmcid, firstAuth, citation, doi, pubDate = citeInfo(cite_list)
        num_cite = get_citations(pmid=pmid1)

        
        if authors == '':
            emptyPages.append(page)
            
        
        else:
            
            row = pd.Series({"Title": title, "PMID": pmid1, "Authors": authors, "Citation": citation, "First_Author": firstAuth
                              ,"Journal/Book": journal, "Publication_Year/Date": pubDate, "PMCID": pmcid, "DOI": doi, "Keywords": keywords_text
                              , "Country": country, "N_Citations": num_cite, "Authors/Affiliations": affiliation_dict})
            
            df = pd.concat([df, row.to_frame().T], ignore_index=True)
            

    return df, emptyPages
