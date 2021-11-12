import json
import time
from re import match
import pandas as pd
from keywords import getSentences,generate_wordcloud
import nltk
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from utils import construct_trie,construct_re,get_matches,get_matches_overlap


stop_words = set(stopwords.words('english'))


print("********************************START******************************\n*******************************************************************")
in_file_path = 'filtered_arxiv.json'
titleAbstractDict = {}
start = time.time()
with open(in_file_path,'r') as in_json_file:
    json_obj_list = json.load(in_json_file)
    count = 0
    for json_obj in json_obj_list:
        if count > 30000:
            break
        titleAbstractDict[json_obj["title"]] = json_obj["abstract"]
        count += 1
end = time.time()
print(end-start)

with open('Keywords-Springer-83K.csv', 'r',encoding='utf-8') as inp:
    reader = csv.reader(inp)
    keywordList = []
    for rows in reader:
        if rows[1]== 'frequency':
            continue
        if int(rows[1]) < 200:
            break
        keywordList.append(rows[0])


if __name__ == "__main__":
    trialKeyList = ["dynamic programming","classification","support vector machine","clustering","query execution","cloud computing","sift","virtual machine"]
    trialKey = []
    input_kw = input("Type the keyword:")
    trialKey.append(input_kw)
    candidateSentences = []
    SWords = set(STOPWORDS)
    for keyword in trialKey:
        print("KEYWORD : ", keyword)
        for title in titleAbstractDict:
            if keyword in titleAbstractDict[title]:
                sentenceList = getSentences(keyword, titleAbstractDict[title])
                for sentence in sentenceList:
                    candidateSentences.append(sentence)
            if len(candidateSentences)>20:
                break
        #print(candidateSentences)
    #print(len(candidateSentences))
    kw_trie = construct_trie(keywordList)
    reg = construct_re(kw_trie)
    idealSentences = []
    all_matched_kw = []
    for sentence in candidateSentences:
        sentenceLength = len(sentence)
        matches = get_matches(sentence, reg)
        for keyword in matches:
            if keyword == trialKey[0]:
                continue
            else:
                all_matched_kw.append(keyword)
        if sentenceLength >300 or sentenceLength<50:
            continue
        idealSentences.append((len(matches)*100.0/sentenceLength,len(matches),sentence))
        
        #print(matches)
    idealSentences.sort(key = lambda y : y[0])
    print(idealSentences)
    print(len(idealSentences))
    print(all_matched_kw)
    #generate_wordcloud(SWords,all_matched_kw)



