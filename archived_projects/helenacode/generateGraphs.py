#-*- coding: utf-8 -*-
'''
Helena Gomez, 30/10/2017
This module generates the SI graph structure of a parsed file

python recorrerGrafos.py archivoEntrada
ejemplo: python recorrerGrafos.py ../grafosTest/ ../grafosAutores/ 
'''

import networkx as nx
from collections import defaultdict

def graph(ifile, lemma, frequency, pos, nopos):
    text = open(ifile, "r").readlines()
    G = nx.DiGraph()
    deprelationsDict={}
    wordsDict=defaultdict(lambda:[])
    
    for line in text:
        if (not line) or (line == ""):
            print "Error al leer documento"                                                         
            break;                                                                           
        line = line.rstrip()
        values = line.split(" ")
        
        DependencyType = values[0]
        initialValues = values[1].split("_")
        finalValues = values[2].split("_")
        initialPOS = initialValues[len(initialValues)-1]
        finalPOS = finalValues[len(finalValues)-1]
        
        #use lemma in the nodes
        if lemma:
            initialWord = initialValues[1].lower() #indicates the lemma
            finalWord = finalValues[1].lower()
        #use the word as is, but lowercase
        else:
            initialWord = initialValues[0].lower() #indicates the word
            finalWord = finalValues[0].lower()
        
        #use only pos in the nodes
        if pos:
            if initialPOS == '0':
                initialNode=initialWord+"_"+initialPOS
            else:
                initialNode= initialPOS
            finalNode = finalPOS
        #use only words
        elif nopos:
            if initialPOS == '0':
                initialNode=initialWord+"_"+initialPOS
            else:
                initialNode= initialWord
            finalNode = finalWord
        #use words_pos
        else: 
            initialNode= initialWord+"_"+initialPOS
            finalNode = finalWord +"_"+finalPOS
        
        wordsDict[initialNode+' '+finalNode].append(initialWord)
        wordsDict[initialNode+' '+finalNode].append(finalWord)
        
        #add frequency of the nodes pair + dependency tags
        if frequency:
            frequencyScore = int(values[3])
        else:
            frequencyScore = 1
            
        if initialWord !='' and finalWord != '':
            #storing dependency relations in a dict
            deprelationsDict[initialNode+' '+finalNode]= DependencyType
            
            #adding edges to the graph
            e=[(initialNode,finalNode,frequencyScore)]
            G.add_weighted_edges_from(e)
            G[initialNode][finalNode]['words']=wordsDict[initialNode+' '+finalNode]
            #print "palabras en nodo",initialNode, finalNode, G[initialNode][finalNode]['words']
            
    return G, deprelationsDict

def graphAuthor(files, lemma, frequency, pos, nopos):
    G = nx.DiGraph()
    deprelationsDict={}
    wordsDict=defaultdict(lambda:[])
    for authorfile in files:
        text = open(authorfile, "r").readlines()
        for line in text:
            if (not line) or (line == ""):
                print "Error al leer documento"                                                         
                break;                                                                           
            line = line.rstrip()
            values = line.split(" ")
            
            DependencyType = values[0]
            initialValues = values[1].split("_")
            finalValues = values[2].split("_")
            initialPOS = initialValues[len(initialValues)-1]
            finalPOS = finalValues[len(finalValues)-1]
            
            #use lemma in the nodes
            if lemma:
                initialWord = initialValues[1].lower() #indicates the lemma
                finalWord = finalValues[1].lower()
            #use the word as is, but lowercase
            else:
                initialWord = initialValues[0].lower() #indicates the word
                finalWord = finalValues[0].lower()
             
            #use only pos in the nodes
            if pos:
                if initialPOS == '0':
                    initialNode=initialWord+"_"+initialPOS
                else:
                    initialNode= initialPOS
                finalNode = finalPOS
            #use only words
            elif nopos:
                if initialPOS == '0':
                    initialNode=initialWord+"_"+initialPOS
                else:
                    initialNode= initialWord
                finalNode = finalWord
            #use words_pos
            else: 
                initialNode= initialWord+"_"+initialPOS
                finalNode = finalWord +"_"+finalPOS
                    
            wordsDict[initialNode+' '+finalNode].append(initialWord)
            wordsDict[initialNode+' '+finalNode].append(finalWord)
            
            #add frequency of the nodes pair + dependency tags
            if frequency:
                frequencyScore = int(values[3])
            else:
                frequencyScore = 1
                
            if initialWord !='' and finalWord != '':
                #storing dependency relations in a dict
                deprelationsDict[initialNode+' '+finalNode]= DependencyType                
                #adding edges to the graph
                e=[(initialNode,finalNode,frequencyScore)]
                G.add_weighted_edges_from(e)
                G[initialNode][finalNode]['words']=wordsDict[initialNode+' '+finalNode]
                #print "palabras en nodo",initialNode, finalNode, G[initialNode][finalNode]['words']
            
    return G, deprelationsDict


def graphMulti(ifile, lemma, frequency, pos, nopos):
    text = open(ifile, "r").readlines()
    G = nx.MultiDiGraph()
    deprelationsDict={}
    wordsDict=defaultdict(lambda:[])
    
    for line in text:
        if (not line) or (line == ""):
            print "Error al leer documento"                                                         
            break;                                                                           
        line = line.rstrip()
        values = line.split(" ")
        
        DependencyType = values[0]
        initialValues = values[1].split("_")
        finalValues = values[2].split("_")
        initialPOS = initialValues[len(initialValues)-1]
        finalPOS = finalValues[len(finalValues)-1]
        
        #use lemma in the nodes
        if lemma:
            initialWord = initialValues[1].lower() #indicates the lemma
            finalWord = finalValues[1].lower()
        #use the word as is, but lowercase
        else:
            initialWord = initialValues[0].lower() #indicates the word
            finalWord = finalValues[0].lower()
        
        #use only pos in the nodes
        if pos:
            if initialPOS == '0':
                initialNode=initialWord+"_"+initialPOS
            else:
                initialNode= initialPOS
            finalNode = finalPOS
        #use only words
        elif nopos:
            if initialPOS == '0':
                initialNode=initialWord+"_"+initialPOS
            else:
                initialNode= initialWord
            finalNode = finalWord
        #use words_pos
        else: 
            initialNode= initialWord+"_"+initialPOS
            finalNode = finalWord +"_"+finalPOS
        
        wordsDict[initialNode+' '+finalNode].append(initialWord)
        wordsDict[initialNode+' '+finalNode].append(finalWord)
        
        #add frequency of the nodes pair + dependency tags
        if frequency:
            frequencyScore = int(values[3])
        else:
            frequencyScore = 1
            
        if initialWord !='' and finalWord != '':
            #storing dependency relations in a dict
            deprelationsDict[initialNode+' '+finalNode]= DependencyType
            
            #adding edges to the graph
            e=[(initialNode,finalNode,frequencyScore)]
            G.add_weighted_edges_from(e)
            G[initialNode][finalNode]['words']=wordsDict[initialNode+' '+finalNode]
            G[initialNode][finalNode]['dep']=DependencyType
            #print "palabras en nodo",initialNode, finalNode, G[initialNode][finalNode]['words']
            
    return G, deprelationsDict

def graphAuthorMulti(files, lemma, frequency, pos, nopos):
    G = nx.MultiDiGraph()
    deprelationsDict={}
    wordsDict=defaultdict(lambda:[])
    for authorfile in files:
        text = open(authorfile, "r").readlines()
        for line in text:
            if (not line) or (line == ""):
                print "Error al leer documento"                                                         
                break;                                                                           
            line = line.rstrip()
            values = line.split(" ")
            
            DependencyType = values[0]
            initialValues = values[1].split("_")
            finalValues = values[2].split("_")
            initialPOS = initialValues[len(initialValues)-1]
            finalPOS = finalValues[len(finalValues)-1]
            
            #use lemma in the nodes
            if lemma:
                initialWord = initialValues[1].lower() #indicates the lemma
                finalWord = finalValues[1].lower()
            #use the word as is, but lowercase
            else:
                initialWord = initialValues[0].lower() #indicates the word
                finalWord = finalValues[0].lower()
                 
            #use only pos in the nodes
            if pos:
                if initialPOS == '0':
                    initialNode=initialWord+"_"+initialPOS
                else:
                    initialNode= initialPOS
                finalNode = finalPOS
            #use only words
            elif nopos:
                if initialPOS == '0':
                    initialNode=initialWord+"_"+initialPOS
                else:
                    initialNode= initialWord
                finalNode = finalWord
            #use words_pos
            else: 
                initialNode= initialWord+"_"+initialPOS
                finalNode = finalWord +"_"+finalPOS
                    
            wordsDict[initialNode+' '+finalNode].append(initialWord)
            wordsDict[initialNode+' '+finalNode].append(finalWord)
            
            #add frequency of the nodes pair + dependency tags
            if frequency:
                frequencyScore = int(values[3])
            else:
                frequencyScore = 1
                
            if initialWord !='' and finalWord != '':
                #storing dependency relations in a dict
                deprelationsDict[initialNode+' '+finalNode]= DependencyType                
                #adding edges to the graph
                e=[(initialNode,finalNode,frequencyScore)]
                G.add_weighted_edges_from(e)
                G[initialNode][finalNode]['words']=wordsDict[initialNode+' '+finalNode]
                #print "palabras en nodo",initialNode, finalNode, G[initialNode][finalNode]['words']
            
    return G, deprelationsDict