# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 13:59:37 2016
Defines a set of utility functions for feature Extraction from text
@author: Rupak Chakraborty
"""

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import pos_tag_sents
from nltk import ne_chunk_sents
from nltk.corpus import stopwords
import string 

stopword_list = set(stopwords.words("english")) 
punctuation_list = list(string.punctuation)

def getAverageSentenceLength(sentence_list):
    
    word_count = 0.0;
    sentence_count = len(sentence_list) + 1
    
    for sentence in sentence_list:
        words = word_tokenize(sentence)  
        word_count = word_count + len(words)
    
    return ((word_count)/(sentence_count+1))

def getStopwordCount(sentence_list):
    
    stopword_count = 0.0; 
    
    for sentence in sentence_list:
        for word in word_tokenize(sentence):
            if word in stopword_list:
                stopword_count = stopword_count + 1 
                
    return stopword_count

def getPunctuationCount(sentence_list): 
    
    punctuation_count = 0.0; 
    
    for sentence in sentence_list:
        for word in word_tokenize(sentence):
            if word in punctuation_list:
                punctuation_count = punctuation_count + 1

def getNounAdjVerbs(sentence_list): 
    
    nouns = 0
    verbs = 0
    adj = 0 
    
    for text in sentence_list: 
        
        words = word_tokenize(text)
        
        try:
            pos_tags = nltk.pos_tag(words)
        except:
            pass
        
        for token in pos_tags: 
            k = token[1]
            if k == "NN" or k == "NNP" or k == "NNS" or k == "NNPS":
                nouns = nouns + 1
            elif k == "JJ" or k == "JJR" or k == "JJS":
                adj = adj + 1
            elif k == "VB" or k == "VBD" or k == "VBG" or k == "VBN" or k == "VBP" or k == "VBZ":
                verbs = verbs + 1 
                
    return nouns,adj,verbs

def getBigramCounts(sentence_list):
    
    bigram_count = 0.0
    for sentence in sentence_list:
        words = word_tokenize(sentence)
        k = len(list(nltk.bigrams(words)))
        bigram_count = bigram_count + k
    
    return bigram_count;
    
def getTrigramCounts(sentence_list):
    
    trigram_count = 0.0
    for sentence in sentence_list:
        words = word_tokenize(sentence)
        k = len(list(nltk.trigrams(words)))
        trigram_count = trigram_count + k
    
    return trigram_count;

def extractNERCounts(sentence_list): 
    
    count_ner = 0.0
     for sent in sentence_list:
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
           if hasattr(chunk, 'node'):
              count_ner = count_ner + len(list(chunk.leaves()))
