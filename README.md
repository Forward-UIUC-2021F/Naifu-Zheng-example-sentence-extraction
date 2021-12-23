# example-sentence-extraction
Module: Finding example sentences for keywords
This module is responsible for fetching sentences containing the target user-inputed keyword, and by comparison with one another, select sentences which demonstrate the appropriate usage of the keyword. 

## Demo video
[![Watch the video](https://img.youtube.com/vi/GjHNIrJioOk/maxresdefault.jpg)](https://www.youtube.com/watch?v=GjHNIrJioOk)


## Setup and Dependencies
- run the commands below to install packages
```
pip3 install nltk
pip3 install wordcloud
```
- All the sample sentences are from the pruned Arxiv dataset(original dataset is in the reference at the bottom of the page). The filtered Arxiv dataset contains only papers about computer science topics, work is done by Forward Data Lab. Need to download the filtered Arxiv dataset first.

- Need to download the csv file of the computer science keywords. Can be downloaded [here](https://drive.google.com/drive/folders/1wD9t3BQbLktgOqzU0z8Xmnds1At6bZn5)
```
naifu-zheng-example-sentence-extraction/
    - keywords.py
    - main.py
    - __init__.py
    - trie/
        -- __init__.py
        -- Trie.py
        -- utils.py
    - filtered_arxiv.json
    - Keywords-Springer-83K.csv
```

## Functional Design:
External Package: MetaPy, NLTK
- driver function loading json file into a dictionary where the keys are titles of articles and values are abstracts of the articles.
```
with open(arxiv,'r') as in_json_file:
    json_obj_list = json.load(in_json_file)
    for json_obj in json_obj_list:
        titleAbstractDict[json_obj["title"]] = json_obj["abstract"]
```
- driver function loading keywords csv file into a list- keywordList
```
with open('Keywords-Springer-83K.csv', 'r',encoding='utf-8') as inp:
    reader = csv.reader(inp)
    keywordList = []
    for rows in reader:
        keywordList.append(rows[0])
```

- getSentences takes the target keyword and a text segment(string type) and returns a list of sentences containing the keyword. 
```
def getSentences(keyword, text):
    return keywordSentences
```
- generate_wordcloud takes a collection of stopwords and a list of keywords, outputs the wordcloud of the keywords
```
def generate_wordcloud(StopWords,wordcloudlist):
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()
```
- MetaPy filters used to evaluate the sample sentences.

## Algorithmic Design:
First fetch the texts from the Arxiv dataset (an ideal way is to import the Arxiv dataset into DB and fetch data from DB, so that there is no need for indexing).
Apply getSentences() to find the sentences which contain the target keyword and with appropriate length. Now we have a list of sentences containing the keyword.
Then by applying the metaPy package, we got the term frequencies of the sentences and got all the “important” words left. 

- Determination of the quality of a sentence: number of other CS keywords appeared in the sentence/length of the sentence
![Image of flowchart](https://github.com/Forward-UIUC-2021F/example-sentence-extraction/blob/main/flowchart.png)

## Potential Improvement
- Some edge cases of splitting sentences are unconsidered. Probably can be improved using NLTK tokenizer.
- There are a few sentences in test runs such that they are a list of keywords, which should be removed.
- Wordcloud stemmization and lemmatization

## Reference:
Dataset: https://www.kaggle.com/Cornell-University/arxiv
