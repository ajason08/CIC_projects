#-*- coding: utf-8 -*-
'''
Helena Gomez, 30/10/2017
This module traverse the SI graphs, count the features and calculated the similarity

python traverseGraphsOld.py inputFile
example: python traverseGraphsOld.py ../grafosTest/ ../grafosTrain/ 
'''

from __future__ import division
from time import time
import sys, glob, os, math, getopt, re
import networkx as nx
from collections import defaultdict
import generateGraphs

def calcular_caracteristicas(GT):
    vector=[]
    
    values = nx.in_degree_centrality(GT)
    vector.append(sum(values.values())/len(values.values()))
    
    
    values = nx.out_degree_centrality(GT)
    vector.append(sum(values.values())/len(values.values()))
    
    #values = nx.eigenvector_centrality(GT,max_iter=500)
    #vector.append(sum(values.values())/len(values.values()))
    #values = nx.katz_centrality(GT,max_iter=)
    vector.append(sum(values.values())/len(values.values()))
    
    values = nx.closeness_centrality(GT)
    vector.append(sum(values.values())/len(values.values()))
    #values = nx.current_flow_closeness_centrality(GT)
    #vector.append(sum(values.values())/len(values.values()))
    values = nx.betweenness_centrality(GT)
    vector.append(sum(values.values())/len(values.values()))
    values = nx.edge_betweenness_centrality(GT)
    vector.append(sum(values.values())/len(values.values()))
    #values = nx.current_flow_betweenness_centrality(GT)
    #vector.append(sum(values.values())/len(values.values()))
    #values = nx.edge_current_flow_betweenness_centrality(GT)
    #vector.append(sum(values.values())/len(values.values()))
    
    values = nx.pagerank(GT)
    vector.append(sum(values.values())/len(values.values()))
    h,a = nx.hits(GT,max_iter=1000)    
    vector.append(sum(h.values())/len(h.values()))
    vector.append(sum(a.values())/len(a.values()))
    
    for id,item in enumerate(vector):
        vector[id]=item*1000
    
    return vector

def calc_cosenoList(vec1, vec2):
    #intersection = set(vec1.keys()) & set(vec2.keys())
    #print "len:",len(intersection)
    #print "Vector 1"
    #print vec1
    #print "Vector 2"
    #print vec2
    numerator = sum([vec1[id] * vec2[id] for id,item in enumerate(vec1)])
    sum1 = sum([x**2 for x in vec1])
    sum2 = sum([x**2 for x in vec2])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator 

def calc_coseno(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    #print "len:",len(intersection)
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator  

                        
def readFiles(path, doctype):    
    files  = defaultdict(lambda:[])
    nelements = glob.glob(path+"/"+doctype+"*.ok")
    if len(nelements) == 0:
        for item in os.listdir(path):
            aux = path+"/"+item+"/Grafos"+"/"+doctype       
            nelements = glob.glob(aux+"*.ok")
            files[aux].extend(nelements)
    else:
        files[aux].extend(nelements)
    return files

def get_argv(argv_value):
    trainpath = ''
    outPath = ''
    lemma = False # if true use the lemma in the nodes, else use the word as apears in the text
    freq = False # if true include the frequency counts on the edges
    pos = False # if true generate the graphs only with pos in the nodes
    nopos=False # if true generate the graphs only with words in the nodes
    profile = False # if true evaluates the similarities on the concatenation of the documents, else evaluates on each training document individually
    try:
        opts, args = getopt.getopt(argv_value,"ht:o:lfpnr",["trainPath=","out=","lemma","freq","onlypos","nopos","profile"])
        if len(opts)<=1 and ('h' not in opts[0][0]):
            print 'USO: graphsVerification.py -t <trainPath> -o <outPath> [-l (lemma) -f (use frequency) -p (only pos) -n (nopos) -r (profile)]' 
            sys.exit(2)
    except getopt.GetoptError:
        print 'Error: traverseGraphsOld.py -t <trainPath> -T <testPath> -o <outPath> [-l (lemma) -f (use frequency) -p (only pos) -n (nopos) -r (profile)]'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Help: traverseGraphsOld.py -t <trainPath> -T <testPath> -o <outPath> [-l (lemma) -f (use frequency) -p (only pos) -n (nopos) -r (profile)]'
            sys.exit()
        elif opt in ("-t", "--trainPath"):
            trainpath = arg
        # for boolean parameters, it is necessary to convert to boolean because the input is str()
        elif opt in ("-l", "--lemma"):
            lemma = True
        elif opt in ("-f", "--freq"):
            freq = True
        elif opt in ("-p", "--onlypos"):
            pos = True
        elif opt in ("-n", "--nopos"):
            nopos = True
        elif opt in ("-r", "--profile"):
            profile = True
        elif opt in ("-o", "--out"):
            outPath = arg
    return trainpath, outPath, lemma, freq, pos, nopos, profile
   
def main(argv):
    #reading arguments
    train_path, out_path, lemma, freq, pos, nopos, profile= get_argv(argv)
            
    f_out=open(out_path, "w+")
    #reading files
    #train_files = readFiles(train_path, '')
    #test_files = readFiles(train_path, '')
    
    #Test Features dictionary
    testFeatures = defaultdict(lambda: {})
    #test_filesList= sum([test_files[t] for t in test_files], [])
    #print "Traversing Test Graphs", len(test_filesList)
    test_filesList = [my_test+"/10306newsml.txt.ok"]
    for testFile in test_filesList:
        Gt, relationsTest=generateGraphs.graph(testFile, lemma, freq, pos, nopos)
        #Puedes probar esta funcion que define un grafo dirigido multietiquetado
        #Gt, relationsTest=generateGraphs.graphMulti(testFile, lemma, freq, pos, nopos)
        #calculate test graph features here
        testFeatures[testFile]=calcular_caracteristicas(Gt)
                
    #Train Features dictionary
    trainFeatures = defaultdict(lambda: {})
    if not profile:
        #train_files= sum([train_files[t] for t in train_files], [])
        print "Traversing Train Graphs"#,len(train_files)
    else:
        print "Traversing Train Graphs, profiles"#,len(train_files)
    train_files = [my_training+"/10306newsml.txt.ok", my_training+"/16167newsml.txt.ok"]
    for trainFile in train_files:
        #defined in the parameters, if the training graphs will include all texts written by the author or only one sample
        if profile:
            Ga, relationsTrain = generateGraphs.graphAuthor(train_files[trainFile], lemma, freq, pos, nopos)
            #Puedes probar esta funcion que define un grafo dirigido multietiquetado
            #Ga, relationsTrain=generateGraphs.graphMultiAuthor(trainFile, lemma, freq, pos, nopos)
        else:
            Ga, relationsTrain = generateGraphs.graph(trainFile, lemma, freq, pos, nopos)
            #Puedes probar esta funcion que define un grafo dirigido multietiquetado
            #Ga, relationsTrain=generateGraphs.graphMulti(trainFile, lemma, freq, pos, nopos)
        #calculate train graph features here
        trainFeatures[trainFile]=calcular_caracteristicas(Ga)
        

    print "Calculating Cosine Similarity", len(testFeatures), len(trainFeatures)
    #calculating similarity
    for testFile in testFeatures:
        #extracting name of the file for output
        testName=re.sub(train_path+'/','',testFile)
        testName=re.sub('Grafos/','',testName)
        for trainFile in trainFeatures:
            #extracting name of the file for output
            trainName=re.sub(train_path+'/','',trainFile)            
            trainName=re.sub('Grafos/','',trainName)
            coseno = calc_cosenoList(testFeatures[testFile], trainFeatures[trainFile])
            f_out.write(testName+'|'+trainName+'|'+str(coseno)+'\n')


if __name__ == '__main__': 
    start_time = time()
    
    #main(sys.argv[1:])
    my_training = "C:/From_windowsCIC/CIC_projects/helenacode/prueba2/Alan/Grafos"
    my_test     = "C:/From_windowsCIC/CIC_projects/helenacode/prueba1/Alan/Grafos"
    out      = "C:/From_windowsCIC/CIC_projects/helenacode/salida"

    main(["-t",my_training, "-o", out,"-l"])
    elapsed_time = time() - start_time
    print("Elapsed time: %.10f seconds." % elapsed_time)
    
    print "Finished"
#"T","mytest",