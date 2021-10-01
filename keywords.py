import os
import json
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


#print(os.path.abspath("arxiv-metadata-oai-snapshot.json"))
'''********************
getSentences function
PARAMETERS:  KEYWORD -- word to search for; TEXT -- string made of sentence(s)
RETURN: a list of strings, each is a sentence containing the keyword
************************'''
# def getSentences(keyword, text):
#     sentences = []
#     startIdx = 0
#     for charIdx in range(len(text)):
#         if text[charIdx]=='.' and charIdx<len(text)-1:
#             if keyword.lower() in text[startIdx:charIdx].lower():
#                 if len(text[startIdx:charIdx]) > 100:
#                     if startIdx == 0:
#                         sentences.append(text[startIdx:charIdx+1])
#                     else:
#                         sentences.append(text[startIdx+2:charIdx+1])
#             startIdx = charIdx
#     return sentences

def getSentences(keyword, text):
    keywordSentences = []
    candSentences = text.split('.')
    for sentence in candSentences:
        if keyword.lower() in sentence.lower():
            keywordSentences.append(sentence)
    return keywordSentences
 
'''
eval_sentence function
PARAMETER: a list of strings, each is a sentence containing target keyword
            a list of stopwords in nltk
RETURN: a list of sentences which satisfy the criterias
'''
def eval_sentence(extractedSentences,stop_words):
    scoreSentenceTuple = []
    for sentence in extractedSentences:
        word_tokens = word_tokenize(sentence)
        filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
        score = len(filtered_sentence)/len(word_tokens)
        scoreSentenceTuple.append((sentence,score))
    return scoreSentenceTuple

stop_words = set(stopwords.words('english'))
a = [' The first method is based on tabling and\nwe modified the proof theory to table calls and answers on states (practically,\nequivalent to dynamic programming)', 'We experimentally compare the\noutcomes of MR with those of the optimal "full search" dynamic programming\nsolution and of classical merge and split approaches']
print(eval_sentence(a,stop_words))

