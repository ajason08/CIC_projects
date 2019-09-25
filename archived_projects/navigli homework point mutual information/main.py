from ngram_analyzer_class import NgramAnalyzer
from pandas import DataFrame as df


def gram_dataframe(ngram_dictionary):
    ngrams_keys = list(ngram_dictionary.keys())
    ngrams_values = list(ngram_dictionary.values())
    data = {"ngram":ngrams_keys, "pmi_score": ngrams_values}
    sorted_df = df.from_dict(data).sort_values(by='pmi_score', ascending=False)
    return sorted_df


# FIRST PART: Read file, extract n-grams (from unigrams to trigrams) and save them in a dictionary variable of an object
url = "peter_norvig_file.txt"
my_ngram_analyzer = NgramAnalyzer(url)
my_ngram_analyzer.run()

# demo: dictionary of n-grams frequencies
dictionary = my_ngram_analyzer.gram_dict
print("demo: dictionary of n-grams frequencies")
for i, gram in enumerate(dictionary):
    print(gram, dictionary[gram])
    if i == 10: break
print ("... \nA total of", len(dictionary), "different n-grams where found.")


# SECOND PART: extract ngrams (bigrams and trigrams) based on occurences_threshold and pmi_score_threshold
occurences_threshold = 100
score_threshold = 5
bigram_pmi_scores, trigram_pmi_scores = my_ngram_analyzer.run_pmi(occurences_threshold, score_threshold)

# demo: bigram and trigrams pmi_scores
print("demo: bigrams and trigrams pmi_scores.")
print(gram_dataframe(bigram_pmi_scores))
print("-------------------------------")
print(gram_dataframe(trigram_pmi_scores))


# Some comments about
analysis = """
Analysis:
- A min_ocurrence_threshold = 100 seems to work pretty well for extract collocation of bigrams.
- However at extracting collocation of trigrams a min_ocurrence_threshold = 360 leads to better results.
- Posterior data cleaning like (case converter, remove punctuation, POS filtering, etc) should improve results for collocation and keywords identification.
"""
print(analysis)
