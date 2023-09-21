
from src.components.get_pages import get_pages
from src.components.get_research_url import get_research_urls
from src.components.get_research_dataframe import getResearchDataFrame

from pathlib import Path






def main():

    firstPage = str(input("Please provide the full URL for your search after applying neccessary filters here: "))
    
    print("Initializing first phase")
    print("="*35)
    all_pages = get_pages(first_page=firstPage)
    print("First phase is complete")
    print("="*35)
    print("Initializing second phase")
    print("="*35)
    all_urls = get_research_urls(all_pages)
    print("Second phase is complete")
    print("="*35)
    print("Initializing final phase")
    print("="*35)
    df, emptyPages = getResearchDataFrame(all_urls)
    print("Final phase is complete")
    print("="*35)

    print("There are {} empty pages in the research results".format(len(emptyPages)))
    print("="*35)

    answer = str(input("Do you want to save the results in a csv file format? Yes/No: ").strip()).lower()
    print("="*35)

    if answer == 'yes' or answer == 'y': 
        saveFile = str(input("Please provide the path of the file with .csv extension: "))

        filepath = Path(saveFile)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(filepath)
        
        print("Done")
        print("="*35)

    else:
        print("Sure, here is the top 5 rows of the result which you did not save")
        print(df.head(5))
        print("="*35)



## Example Input
# https://pubmed.ncbi.nlm.nih.gov/?term=(cancer*%20OR%20carcinoma*%20OR%20neoplasms*%20OR%20sarcoma*%20OR%20tumor*%20OR%20tumour*%20OR%20lymphoma*%20OR%20leukemia*%20OR%20leukaemia*%20OR%20malignan*)%20AND%20(caveolin*)&filter=simsearch1.fha&filter=years.2023-2023


if __name__ == '__main__':
    main()
