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
import nltk

stopword_list = set(stopwords.words("english")) 
punctuation_list = list(string.punctuation)

"""
Given a list of finds the average sentence length of the set of sentences

Params:
--------
sentence_list: List of sentences whose average length has to be calculated

Returns:
--------
Floating point number representing the average sentence length
"""
def getAverageSentenceLength(sentence_list):
    
    word_count = 0.0;
    sentence_count = len(sentence_list) + 1.0
    
    for sentence in sentence_list:
        words = word_tokenize(sentence)  
        word_count = word_count + len(words)
    
    return ((word_count)/(sentence_count+1))

"""
Given a list of sentences returns the stopword count of it i.e. number of stopwords in them

Params:
-------
sentence_list: List of sentences whose stopword count has to be calculated

Returns:
--------
Integer containing the count of stopwords in the given list of sentences
"""
def getStopwordCount(sentence_list):
    
    stopword_count = 0.0; 
    
    for sentence in sentence_list:
        for word in word_tokenize(sentence):
            if word in stopword_list:
                stopword_count = stopword_count + 1.0 
                
    return stopword_count 
    
"""
Given a sentence list of sentences calculates the punctuation count of the sentence list

Params:
---------
sentence_list: List of sentences whose punctuation count has to be calculated

Returns:
---------
Integer representing the punctuation count
"""
def getPunctuationCount(sentence_list): 
    
    punctuation_count = 0.0; 
    
    for sentence in sentence_list:
        for word in word_tokenize(sentence):
            if word in punctuation_list:
                punctuation_count = punctuation_count + 1.0
    
    return punctuation_count

"""
Returns the number of nouns,adjectives and verbs for a given sentence list

Params:
--------
sentence_list: The list of sentences whose count of nouns,adj and verbs have to be calculated

Returns:
---------
Integers containing the count of nouns,adjectives and verbs
"""
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
                nouns = nouns + 1.0
            elif k == "JJ" or k == "JJR" or k == "JJS":
                adj = adj + 1.0
            elif k == "VB" or k == "VBD" or k == "VBG" or k == "VBN" or k == "VBP" or k == "VBZ":
                verbs = verbs + 1.0 
                
    return nouns,adj,verbs

"""
Returns the count of bigrams for a given sentence list

Params:
--------
sentence_list: List of sentences whose bigram count has to be calculated

Returns:
----------
Count of bigrams in a given sentence list
"""
def getBigramCounts(sentence_list):
    
    bigram_count = 0.0
    for sentence in sentence_list:
        words = word_tokenize(sentence)
        k = len(list(nltk.bigrams(words)))
        bigram_count = bigram_count + k
    
    return bigram_count;

"""
Given a list of sentences returns the trigram count of the sentence list

Params:
--------
sentence_list: List of sentences whose trigram count has to be calculated

Returns:
---------
Integer containing the trigram count of the sentence list
"""    
def getTrigramCounts(sentence_list):
    
    trigram_count = 0.0
    for sentence in sentence_list:
        words = word_tokenize(sentence)
        k = len(list(nltk.trigrams(words)))
        trigram_count = trigram_count + k
    
    return trigram_count;

"""
Given a list of sentences returns the count of NER in the sentence list

Params:
--------
sentence_list: List of sentences whose NER count has to be calculated

Returns:
---------
Integer containing the count of the NERs in the given sentence list
"""
def extractNERCounts(sentence_list): 
    
    count_ner = 0.0
    for sent in sentence_list:
        try:
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
               if hasattr(chunk, 'node'):
                  count_ner = count_ner + len(list(chunk.leaves()))
        except:
            pass
              
    return count_ner

def is_ascii(s):
    return all(ord(c) < 128 for c in s)
