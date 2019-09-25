from math import log2


class NgramAnalyzer:
    
    gram_dict = {}    
    total_unigrams = 0
    total_bigrams = 0
    total_trigrams = 0
        
    def __init__(self, file_url):
        self.file_url = file_url
    
    def ngram_creator(self, wordlist,n):            
            ngrams = []
            for i in range(len(wordlist)):        
                ngram = wordlist[i:i+n]
                if len(ngram) == n:
                    ngrams.append(ngram)
            return ngrams
    
    def run(self):        
        wordlist = []
        with open(self.file_url) as myfile: 
            # reading line by line avoid out-of-memory issues when working with large files.
            for line in myfile:

                # capturing last words for get n-grams between lines
                try: last_word = wordlist[-1:] 
                except: last_word = []

                try: last2_words = wordlist[-2:]
                except: last2_word = []        

                # collecting ngrams by calling n_gram_creator
                wordlist = line.split()          
                unigrams = self.ngram_creator(wordlist, 1)
                bigrams = self.ngram_creator(last_word + wordlist, 2)
                trigrams = self.ngram_creator(last2_words + wordlist, 3)
                ngrams = unigrams + bigrams + trigrams                
                
                self.total_unigrams += len(unigrams)
                self.total_bigrams += len(bigrams)
                self.total_trigrams += len(trigrams)

                # save/storing at dictionary
                for gram in ngrams:            
                    gram = " ".join(gram)
                    try: self.gram_dict[gram] += 1
                    except: self.gram_dict[gram] = 1

    def run_pmi(self,ocurrences_threshold, score_threshold=0):        
        # ocurrences_threshold: minimum number of occurrences a n-gram should have in each of its word to be considered
        # score_threshold: minimum pm_score a n-gram should have to be considered
        
        # controlling whether ngram information is available
        try:
            assert len(self.gram_dict)>0, "it is empty, you first should to call run method"
        except:
            print ("******* internally it called run method")
            self.run()
        
        bigrams_scores = {}
        trigrams_scores = {}
        for gram in self.gram_dict:
            
            # filter out unigrams and ngrams do not overcome the ocurrences_threshold
            gram_list = gram.split()
            if len(gram_list)<2: continue
            if not all([self.gram_dict[word]>ocurrences_threshold for word in gram_list]): continue                        
            
            # compute probabilities
            total_ngrams= self.total_bigrams if len(gram_list)==2 else self.total_trigrams
            gram_count = self.gram_dict[gram]/total_ngrams
            gram_list_counts = [self.gram_dict[word]/self.total_unigrams for word in gram_list]
            
            # compute pmi score e.g. pmi_sc = P(w1,w2,w3)/P(w1)P(w2)P(w3)
            mult_ind_words= 1
            for word_count in gram_list_counts:
                mult_ind_words = mult_ind_words*word_count            
            coocurrence_score=log2(gram_count/mult_ind_words)
            
            # filter n-grams based on pmi_score
            if coocurrence_score < score_threshold: continue
            
            # reporting results in different dictionaries
            if len(gram_list)==2: bigrams_scores[gram] = coocurrence_score
            if len(gram_list)==3: trigrams_scores[gram] = coocurrence_score
        return bigrams_scores, trigrams_scores
