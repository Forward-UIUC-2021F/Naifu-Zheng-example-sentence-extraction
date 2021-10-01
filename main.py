#from fdl.keywords import getSentences
import os
import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from keywords import getSentences
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


stop_words = set(stopwords.words('english'))

print(stopwords.words('english'))


print("********************************START******************************\n*******************************************************************")
in_file_path = 'filtered_arxiv.json'
titleAbstractDict = {}
with open(in_file_path,'r') as in_json_file:
    json_obj_list = json.load(in_json_file)
    count = 0
    for json_obj in json_obj_list:
        if count > 10000:
            break
        titleAbstractDict[json_obj["title"]] = json_obj["abstract"]
        count += 1



trialKeyList = ["dynamic programming","classification","cloud computing","support vector machine","clustering"]
trialOutputList = []
for keyword in trialKeyList:
    print("KEYWORD : ", keyword)
    for title in titleAbstractDict:
        if keyword in titleAbstractDict[title]:
            sentenceList = getSentences(keyword, titleAbstractDict[title])
            for sentence in sentenceList:
                trialOutputList.append(sentence)
        if len(trialOutputList)>10:
            break
    print(trialOutputList)
    trialOutputList = []

