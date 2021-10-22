# example-sentence-extraction
Module: Finding example sentences for keywords
This module is responsible for fetching sentences containing the target user-inputed keyword, and by comparison with one another, select no more than 5 sentences which demonstrate the appropriate usage of the keyword.

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
Finally, use the TF-IDF algorithm to compare the sentences and select the best ones.
![Image of flowchart](https://github.com/Forward-UIUC-2021F/example-sentence-extraction/blob/main/flowchart.png)
