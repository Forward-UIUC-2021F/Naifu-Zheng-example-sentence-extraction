import json
import time
from re import match
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
    trialKey = []
    input_kw = input("Type the keyword:")
    trialKey.append(input_kw)
    candidateSentences = []
    SWords = set(STOPWORDS)
    start1 = time.time()
    for keyword in trialKey:
        print("KEYWORD : ", keyword)
        for title in titleAbstractDict:
            if keyword in titleAbstractDict[title]:
                sentenceList = getSentences(keyword, titleAbstractDict[title])
                for sentence in sentenceList:
                    candidateSentences.append(sentence)

    end1 = time.time()
    print("time used:", end1-start1)
    start2 = time.time()
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
        
    idealSentences.sort(key = lambda y : y[0])          #sort all the candidate sentences in an ascending order
    end2 = time.time()

    top20sentences = []
    for i in range(-1,-21,-1):
        top20sentences.append(idealSentences[i][2])
    print("time2 used:", end2-start2)
    print("TOP 20 ideal sentences:",top20sentences)#idealSentences[-20:])
    print("You got",len(idealSentences),"sentences containing the keyword")


    generate_wordcloud(SWords,all_matched_kw)



