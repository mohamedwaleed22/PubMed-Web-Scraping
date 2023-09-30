
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
    print(emptyPages)

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

# https://pubmed.ncbi.nlm.nih.gov/?term=%28%28%22milk*%22%5BTitle%2FAbstract%5D+OR+%22blood*%22%5BTitle%2FAbstract%5D+OR+%22urine*%22%5BTitle%2FAbstract%5D+OR+%22saliva*%22%5BTitle%2FAbstract%5D+OR+%22salivary*%22%5BTitle%2FAbstract%5D+OR+%22body+fluid*%22%5BTitle%2FAbstract%5D+OR+%22body+fluids*%22%5BTitle%2FAbstract%5D+OR+%22physiological+fluid*%22%5BTitle%2FAbstract%5D+OR+%22physiological+fluids*%22%5BTitle%2FAbstract%5D%29+AND+%28%22exosomes*%22%5BTitle%2FAbstract%5D+OR+%22exosome*%22%5BTitle%2FAbstract%5D+OR+%22Extracellular+vesicles*%22%5BTitle%2FAbstract%5D+OR+%22EVs%22%5BTitle%2FAbstract%5D+OR+%22exosomal*%22%5BTitle%2FAbstract%5D+OR+%22Microvesicles*%22%5BTitle%2FAbstract%5D%29%29+AND+%28%22cancer*%22%5BTitle%2FAbstract%5D+OR+%22carcinoma*%22%5BTitle%2FAbstract%5D+OR+%22neoplasms*%22%5BTitle%2FAbstract%5D+OR+%22sarcoma*%22%5BTitle%2FAbstract%5D+OR+%22tumor*%22%5BTitle%2FAbstract%5D+OR+%22tumour*%22%5BTitle%2FAbstract%5D+OR+%22lymphoma*%22%5BTitle%2FAbstract%5D+OR+%22leukemia*%22%5BTitle%2FAbstract%5D+OR+%22leukeamia*%22%5BTitle%2FAbstract%5D+OR+%22malignant*%22%5BTitle%2FAbstract%5D%29&filter=lang.english&filter=years.2003-2024

if __name__ == '__main__':
    main()
