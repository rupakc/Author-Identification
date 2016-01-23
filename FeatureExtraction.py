# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:31:16 2016
Defines the Feature Extraction  Util for the author Identification Task
TODO - Define the split up into k parts and seperate directories for train and test files
@author: Rupak Chakraborty
"""
import os
import time
from nltk.tokenize import sent_tokenize 
import TextProcessUtil

def featureExtractionPipeline(sentence_list):
    
    feature_list = []
    average_sentence_length = TextProcessUtil.getAverageSentenceLength(sentence_list)
    feature_list.append(average_sentence_length)
    feature_list.append(TextProcessUtil.getStopwordCount(sentence_list)/average_sentence_length)
    feature_list.append(TextProcessUtil.getBigramCounts(sentence_list)/average_sentence_length)
    feature_list.append(TextProcessUtil.getTrigramCounts(sentence_list)/average_sentence_length)
    feature_list.append(TextProcessUtil.getPunctuationCount(sentence_list)/average_sentence_length)
    noun,adj,verb = TextProcessUtil.getNounAdjVerbs(sentence_list)
    feature_list.append(noun/average_sentence_length)
    feature_list.append(adj/average_sentence_length)
    feature_list.append(verb/average_sentence_length)
    feature_list.append(TextProcessUtil.extractNERCounts(sentence_list)/average_sentence_length)
    
    return feature_list
    
    
main_dir = "Authors/"
author_list_filename = "author_list.txt"

f = open(main_dir+author_list_filename,"r")
author_names = f.read().split(",") 

start = time.time() 

for author in author_names:
    for i in range(8):
        f = open(main_dir+author+"/"+str(i+1)+".txt",'r')
        text = f.read()
        try:
            sentence_list = sent_tokenize(text)
        except:
            pass
        
        print featureExtractionPipeline(sentence_list)
        print i

end = time.time()

print "Total Time Taken for the feature extraction ", end-start

