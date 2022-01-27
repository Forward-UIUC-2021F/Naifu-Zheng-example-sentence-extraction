import json
import nltk
import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
# from wordcloud import WordCloud , STOPWORDS
from Trie import Trie
import re
from utils import construct_trie,construct_re,get_matches,get_matches_overlap
'''********************
getSentences function
PARAMETERS:  KEYWORD -- word to search for; TEXT -- string made of sentence(s)
RETURN: a list of strings, each is a sentence containing the keyword
************************'''

def getSentences(keyword, text):
    keywordSentences = []
    candSentences = text.split('. ')
    for sentence in candSentences:
        if keyword.lower() in sentence.lower():
            sentence = sentence.replace('\n',' ')
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


def generate_wordcloud(SWords,wordcloudlist):
    comment_words = ''
    # for sentence in wordcloudlist:
    #     tokens = sentence.split()
    for i in range(len(wordcloudlist)):
        wordcloudlist[i] = wordcloudlist[i].lower()
    comment_words += " ".join(wordcloudlist)+" "
    #print("CCCC:",comment_words)
    #comment_words = "apple apple banana apple pear pear"
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    stopwords = SWords,
                    min_font_size = 10).generate(comment_words)

    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()


