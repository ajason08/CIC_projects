import nltk
d = nltk.corpus.cmudict.dict()
def nsyl(word):
    return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]


print nsyl("rebel-held")
