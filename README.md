# example-sentence-extraction
Module: Finding example sentences for keywords
This module is responsible for fetching sentences containing the target user-inputed keyword, and by comparison with one another, select no more than 5 sentences which demonstrate the appropriate usage of the keyword.

## Functional Design:
External Package: MetaPy, NLTK
- driver function loading json file into a dictionary
![Image of load_json](https://github.com/Forward-UIUC-2021F/example-sentence-extraction/blob/main/load_json.png)

- getSentences takes the target keyword and a text segment(string type) and returns a list of sentences containing the keyword. 
![Image of getsentence](https://github.com/Forward-UIUC-2021F/example-sentence-extraction/blob/main/getsentence.png)
Note: Code above could be simplified using split()
- MetaPy filters used to evaluate the sample sentences.

## Algorithmic Design:
First fetch the texts from the Arxiv dataset (an ideal way is to import the Arxiv dataset into DB and fetch data from DB, so that there is no need for indexing).
Apply getSentences() to find the sentences which contain the target keyword and with appropriate length. Now we have a list of sentences containing the keyword.
Then by applying the metaPy package, we got the term frequencies of the sentences and got all the “important” words left. 
Finally, use the TF-IDF algorithm to compare the sentences and select the best ones.
![Image of flowchart](https://github.com/Forward-UIUC-2021F/example-sentence-extraction/blob/main/flowchart.png)
