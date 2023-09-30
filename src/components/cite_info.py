from datetime import datetime
import re





## Takes a list of citations 

def citeInfo(citations: list):
    
    cite_list = citations
    
    authors = ''
    title = ''
    journal = ''
    pmid = ''
    pmcid = ''
    firstAuth = ''
    citation = ''

    if len(cite_list) >= 6:

        if "Epub" in cite_list[5] or "Erratum" in cite_list[5]:
            cite_list.pop(5)
        

        if "Epub" in cite_list[5] or "Erratum" in cite_list[5]:
            cite_list.pop(5)

        if "Retraction in:" in cite_list[5]:
            cite_list.pop(5)

        if "Update in:" in cite_list[5]:
            cite_list.pop(5)
        

        if len(cite_list) == 7:



            authors = cite_list[0]
            title = '. '.join(cite_list[1:3])
            journal = cite_list[3]
            pub_year = cite_list[4].split(';')[0].split(' ')[0]

            doi = ''
            if 'doi:' in cite_list[5]:
                doi = cite_list[5].split('doi: ')[1]
            else: 
                doi = ''

            pmid = re.findall("PMID: (\d*)", cite_list[6])
            pmid = pmid.pop().removesuffix('.')

            pmcid = ''
            if 'PMCID' in cite_list[6]:

                pmcid = re.findall("PMCID: (\S*)", cite_list[6])
                pmcid = pmcid.pop().removesuffix('.')
            else:
                pmcid = ''

            pubDate = pub_year

            if len(cite_list[4].split(';')[0]) > 9:

                dateObj = cite_list[4].split(";")[0]
                createdDate = datetime.strptime(str(dateObj), "%Y %b %d")
                dateObj = dateObj.split(':')[0]
                createdDate = createdDate.strftime("%m/%d/%Y")

                pubDate = pubDate + ', ' + createdDate
            else:
                pubDate = pubDate

            firstAuth = cite_list[0].split(",")[0]
            citation = '. '.join(cite_list[3:-1])

            
        elif len(cite_list) == 6:

            authors = cite_list[0]
            title = cite_list[1]
            journal = cite_list[2]
            pub_year = cite_list[3].split(';')[0].split(' ')[0]

            doi = ''
            if 'doi:' in cite_list[4]:
                doi = cite_list[4].split('doi: ')[1]
            else: 
                doi = ''

            pmid = re.findall("PMID: (\d*)", cite_list[5])
            pmid = pmid.pop().removesuffix('.')

            pmcid = ''
            if 'PMCID' in cite_list[5]:

                pmcid = re.findall("PMCID: (\S*)", cite_list[5])
                pmcid = pmcid.pop().removesuffix('.')
            else:
                pmcid = ''

            pubDate = pub_year

            if len(cite_list[3].split(';')[0]) > 9:

                dateObj = cite_list[3].split(";")[0]
                dateObj = dateObj.split(':')[0]
                createdDate = datetime.strptime(str(dateObj), "%Y %b %d")
                createdDate = createdDate.strftime("%m/%d/%Y")

                pubDate = pubDate + ', ' + createdDate
            else:
                pubDate = pubDate

            firstAuth = cite_list[0].split(",")[0]
            citation = '. '.join(cite_list[2:-1])


    elif len(cite_list) == 5:
        
        authors = cite_list[0]
        title = cite_list[1]
        journal = cite_list[2]
        pub_year = cite_list[3].split(';')[0].split(' ')[0]

        pmid = re.findall("PMID: (\d*)", cite_list[4])
        pmid = pmid.pop().removesuffix('.')
        
        doi = ''
        
        pmcid = ''
        if 'PMCID' in cite_list[4]:

            pmcid = re.findall("PMCID: (\S*)", cite_list[4])
            pmcid = pmcid.pop().removesuffix('.')
            
        else:
            pmcid = ''

        pubDate = pub_year

        if len(cite_list[3].split(';')[0]) > 9:

            dateObj = cite_list[3].split(";")[0]
            dateObj = dateObj.split(':')[0]
            createdDate = datetime.strptime(str(dateObj), "%Y %b %d")
            createdDate = createdDate.strftime("%m/%d/%Y")

            pubDate = pubDate + ', ' + createdDate
        else:
            pubDate = pubDate

        firstAuth = cite_list[0].split(",")[0]
        citation = '. '.join(cite_list[2:-1])
    
    
    elif len(cite_list) == 4:
        authors = cite_list[0]
        title = cite_list[1]

        pmcid = ''
        journal = ''

        pmid = re.findall("PMID: (\d*)", cite_list[3])
        pmid = pmid.pop().removesuffix('.')
        citation = '. '.join(cite_list[1:-1])
        doi = ''
        pub_year = ''
        pubDate = pub_year

        firstAuth = cite_list[0].split(",")[0]

    return authors, title, journal, pmid, pmcid, firstAuth, citation, doi, pubDate

