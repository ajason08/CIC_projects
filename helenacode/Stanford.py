#-*- coding: utf-8 -*-
'''
Created on 30/10/2017
This module contains the methods for parsing files with the Stanford CoreNLP

python Stanford.py inputDir
example: python Stanford.py ../FilesDir
'''
import os, sys, codecs, glob, re
from pycorenlp import StanfordCoreNLP as CoreNLP
from collections import defaultdict

reload(sys)  

def get_files_all(path):    
    files  = []
    flag=0
    nelements = glob.glob(path+"/*.txt")
    if len(nelements) == 0:
        flag=1
        for item in os.listdir(path):
            aux = path+"/"+item            
            nelements = glob.glob(aux+"/*.txt")
            files.extend(nelements)
    else:
        files.extend(nelements)
    return files,flag

def clean_text( text ):
    re.sub('\x21', ' ', text);
    re.sub('\x22', ' ', text);
    re.sub('\x23', ' ', text);
    re.sub('\x24', ' ', text);
    re.sub('\x25', ' ', text);
    re.sub('\x26', ' ', text);
    re.sub('\x27', ' ', text);
    re.sub("\x40", " ", text);
    re.sub("\x5d", " ", text);
    re.sub("\x5f", " ", text);
    re.sub("\x60", " ", text);
    re.sub("\x7b", " ", text);
    re.sub("\x7c", " ", text);
    re.sub("\x7d", " ", text);
    re.sub("\x7e", " ", text);
    re.sub("\x0D", " ", text);
    re.sub("\x20", " ", text);
    
    return text

def parse_stanford(ifile, folder):   
    proc= CoreNLP('http://localhost:9000')
    
    fileName=ifile[ifile.rfind("/")+1:].lower()
       
    print "Parsing:"+ifile
    
    #create the graphs folder if not exists
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    out = codecs.open(folder+fileName+".ok","w",encoding="utf-8")
    try:
        tmp = open(ifile,"r")
    except IOError as e:
        print "Error: "+ifile+" I/O error({0}): {1}".format(e.errno, e.strerror)
        exit(1)
    #dictionary for counting occurences of terms and relations
    pairCount=defaultdict(lambda: 0)
    relations={}
    relationsCount=defaultdict(lambda: 0)
    for line in tmp.readlines(): 
                                                                                                  
        line = line.rstrip()
        line = clean_text(line)
        
        if line !='' and line !='\n': 
            data = proc.annotate(line, properties={
                                'annotators': 'tokenize,ssplit,pos,lemma,parse',#tokenize,ssplit,pos,depparse,parse
                                'outputFormat': 'json'})
            for sentence in data["sentences"]:
                words={}
                pos={}
                lemmas={}
                words[0] = "root"
                lemmas[0] = "root"
                pos[0] = "0"
                for tokens in list(sentence["tokens"]):
                    word=tokens["word"]
                    idx=tokens["index"]
                    words[idx] = word
                    pos[idx] = tokens["pos"]
                    lemmas[idx] = tokens["lemma"]
                if len(words.keys()) >= 2:
                    for tupla in sentence["basicDependencies"]:#basic-dependencies
                        governor=encodeMe(words[tupla["governor"]])+"_"+encodeMe(lemmas[tupla["governor"]])+"_"+pos[tupla["governor"]]
                        dependent=encodeMe(words[tupla["dependent"]])+"_"+encodeMe(lemmas[tupla["dependent"]])+"_"+pos[tupla["dependent"]]
                        deptag=tupla["dep"]
                        pairCount[governor+" "+dependent]+=1
                        relations[governor+" "+dependent]=deptag
                        relationsCount[deptag] +=1
                        #out.write(tupla["dep"]+" "+lemmas[tupla["governor"]].encode("UTF-8")+"_"+pos[tupla["governor"]]+" "+encodeMe(lemmas[tupla["dependent"]])+"_"+pos[tupla["dependent"]]+"\n")
                        
    for pair in pairCount:
        #if pairCount[pair] > 1:
        out.write(relations[pair] +" "+ pair +" "+ str(pairCount[pair] + relationsCount[relations[pair]]) +"\n")
        
    tmp.close()
    out.close()
    return(data)
##################################################
def encodeMe(st):
    try:
        st.decode("ascii")
        return st.enconde("UTF-8")
    except:
        return st
##################################################            
if __name__ == '__main__':
    # Ejemplo python Stanford.py ../authorshipAttribution/pan13-authorship-verification-test-corpus2/ Grafos/
    input=sys.argv[1]#"../pan12train/"#"../PythonGSI/"
    
    files,flag = get_files_all(input)
    
    print "Cant. Files:",len(files)
    for ifile in files:
        if flag==0:
            output=input+sys.argv[2]#"Grafos/"
        else:
            output=input+ifile[len(input):ifile.rfind('/')+1]+sys.argv[2]
        #perform parsing
        salida=parse_stanford(ifile,output)
         
    print "finish processing"
