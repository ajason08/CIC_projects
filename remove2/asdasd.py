from nltk.corpus import wordnet as wn


    def get_wordnet_statistics_by_word(word="dog", pos="NN"):
        # mapper. If it starts with <chars from standar_tag_set> then is a <wordnet_tag>
        # NN => n           (NOUN)
        # V => v            (VERB)
        # JJ => a, s        (ADJECTIVE and ADJECTIVE SATELLITE)
        # RB => r           (ADVERB)
        sensesW = ""
        sensesW = wn.synsets(word)
        nro_senses = len(sensesW)
        #print("# senses of '", word, "':", nro_senses) # number of senses
        sum_lemmas_senseW = 0
        sum_hyponyms_senseW = 0
        sum_hyperonyms_senseW = 0

        for senseW in sensesW:
            # getting the lemmas. Lemmas are (in a practical use) the synonyms for a word given certain sense
            senseW = str(senseW)[8:-2]  # get the description for each sense
            sensesW_tag = senseW[-4:-3]
            undesiderable_sense1 = pos.startswith("NN") and not sensesW_tag == "n"
            undesiderable_sense2 = pos.startswith("V") and not sensesW_tag == "v"
            undesiderable_sense3 = pos.startswith("JJ") and not sensesW_tag == "a" and not sensesW_tag == "s"
            undesiderable_sense4 = pos.startswith("RB") and not sensesW_tag == "r"
            if undesiderable_sense1 or undesiderable_sense2 or undesiderable_sense3 or undesiderable_sense4:
                continue
            #print("with sense", senseW, ";")
            lemmas_senseW = wn.synset(senseW).lemma_names()
            #print(lemmas_senseW)
            nro_lemmas = len(lemmas_senseW)
            #print(nro_lemmas)
            sum_lemmas_senseW += nro_lemmas

        # getting hyponyms and hyperonyms by word
        hyponyms = wn.synset(senseW).hyponyms()
        hyperonyms = wn.synset(senseW).hypernyms()
        nro_hyponyms = len(hyponyms)
        nro_hyperonyms = len(hyperonyms)
        sum_hyponyms_senseW += nro_hyponyms
        sum_hyperonyms_senseW += nro_hyperonyms
        #print("there are", len(hyponyms), "hyponyms", "\n", hyponyms)
        #print("there are", len(hyperonyms), "hyperonyms", "\n", hyperonyms)

    print("+==============summary==============+")
    print("# senses of '", word, "':", nro_senses)  # number of senses
    print("sum of lemmas", sum_lemmas_senseW)
    print("sum of hyponyms", sum_hyponyms_senseW)
    print("sum of hyperonyms", sum_hyperonyms_senseW)

    return nro_senses, sum_lemmas_senseW, sum_hyponyms_senseW, sum_hyperonyms_senseW

#d = wn.synset('dog.n.01')
#print(d.hyponyms())
print(get_wordnet_statistics_by_word("dog","NN"))