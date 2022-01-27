import sys
import json
import time
from re import match
from keywords import getSentences # ,generate_wordcloud
import nltk
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from wordcloud import WordCloud, STOPWORDS
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
from utils import construct_trie,construct_re,get_matches,get_matches_overlap

import os
from dotenv import load_dotenv
load_dotenv()

stop_words = set(stopwords.words('english'))

CS_KEYWORDS_FILE = f"{os.getenv('DATA_DIR')}/Keywords-Springer-83K.csv"

# print("********************************START******************************\n*******************************************************************")
in_file_path = f"{os.getenv('DATA_DIR')}/filtered_arxiv.json"
titleAbstractDict = {}
start = time.time()
with open(in_file_path,'r') as in_json_file:
    json_obj_list = json.load(in_json_file)
    count = 0
    for json_obj in json_obj_list:
        titleAbstractDict[json_obj["title"]] = json_obj["abstract"]
        count += 1
end = time.time()
# print(end-start)


with open(CS_KEYWORDS_FILE, 'r',encoding='utf-8') as inp:
    reader = csv.reader(inp)
    keywordList = []
    for rows in reader:
        if rows[1]== 'frequency':
            continue
        if int(rows[1]) < 200:
            break
        keywordList.append(rows[0])


def get_ranked_sentences(cmd_line_inp):
    inps = cmd_line_inp.split()
    
    input_kw = inps[0].replace('+', ' ')
    num_requested = int(inps[1])


    trialKey = []
    # input_kw = input("Type the keyword:")
    trialKey.append(input_kw)
    candidateSentences = []
    SWords = set(STOPWORDS)
    start1 = time.time()
    for keyword in trialKey:
        # print("KEYWORD : ", keyword)
        for title in titleAbstractDict:
            if keyword in titleAbstractDict[title]:
                sentenceList = getSentences(keyword, titleAbstractDict[title])
                for sentence in sentenceList:
                    candidateSentences.append(sentence)

    end1 = time.time()
    # print("time used:", end1-start1)
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
    # print(f"Num top: {len(idealSentences)}", file=sys.stderr)
    for i in range(-1,-21,-1):
        try:
            top20sentences.append(idealSentences[i][2])
        except Exception as e:
            print(e, file=sys.stderr)
            continue

    # print("time2 used:", end2-start2)
    # print("TOP 20 ideal sentences:",top20sentences)#idealSentences[-20:])
    # print("You got",len(idealSentences),"sentences containing the keyword") 

    # generate_wordcloud(SWords,all_matched_kw)

    return top20sentences


if __name__ == "__main__":
    # https://stackoverflow.com/questions/7091413/how-do-you-read-from-stdin-in-python-from-a-pipe-which-has-no-ending
    # print("Ready")
    try:
        buff = ''
        while True:
            buff += sys.stdin.read(1)
            if buff.endswith('\n'):
                res = get_ranked_sentences(buff[:-1])
                res = [{
                    'sentence': s
                } for s in res]
                print(json.dumps(res))
                sys.stdout.flush()
                buff = ''

    except KeyboardInterrupt:
        sys.stdout.flush()
        pass



