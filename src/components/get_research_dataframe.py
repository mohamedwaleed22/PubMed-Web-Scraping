from tqdm import tqdm
from src.components.keywords import affKeyword
from src.components.cite_page import citePage
from src.components.cite_info import citeInfo
import pandas as pd



def getResearchDataFrame(pages: list):


    df = pd.DataFrame(
            columns=["Title", "PMID", "Authors", "Citation", "First_Author", "Journal/Book"
                     , "Publication_Year/Date","PMCID", "DOI", "Keywords", "Authors/Affiliations"])
    emptyPages = []
    
    for page in tqdm(pages):


        affiliation_dict, keywords_text = affKeyword(page)
        cite_list = citePage(page)
        authors, title, journal, doi, pmid, pmcid, firstAuth, citation, pubDate = citeInfo(cite_list)
        
        if authors == '':
            emptyPages.append(page)
            
        
        else:
            
            row = pd.Series({"Title": title, "PMID": pmid, "Authors": authors, "Citation": citation, "First_Author": firstAuth
                              ,"Journal/Book": journal, "Publication_Year/Date": pubDate, "PMCID": pmcid
                              ,"DOI": doi, "Keywords": keywords_text, "Authors/Affiliations": affiliation_dict})
            
            df = pd.concat([df, row.to_frame().T], ignore_index=True)
            

    return df, emptyPages
