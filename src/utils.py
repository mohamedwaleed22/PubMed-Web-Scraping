import spacy

nlp = spacy.load('en_core_web_sm')

def extract_country_names(text):

    country_names = []
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == 'GPE':
            country_names.append(ent.text)
    if country_names:
        
        return (country_names[-1])
    else:
        return 0


def getCountry(arr):

    set1 = set(arr)
    curr = maxi = 0
    arrdict = {}
    for i in set1:
        curr = arr.count(i)
        arrdict[i] = curr
        maxi = max(maxi, curr)
    country = [k for k, v in arrdict.items() if v == maxi]
    return country[0]

    