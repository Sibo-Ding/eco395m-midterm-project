# eco395m-midterm-project


1. Scrape 15 works from Project Gutenberd. Run `code/scrape_literatures.py`, output text files in `text`. Each text is a work from an author. 5 works from pre-Shakespeare period and 5 works from post-Shakesoeare period.

2. Convert texts from the previous step to vectors of word frequency (BoW). Run `code/text_to_num.py`, output 15 csv files in `words_freq`. Each csv is the word frequency of a text.  

3. Reformat the code files via Black command.
4. Run flesch_kincaid.py: outputs two csv files in flesch-kincaid_results directory with flesch-kincaid analysis for each text, scoring the text by grade level and general readability
5. Run sentiment.py: uses TextBlob library to analyze the sentiment of each text, scoring each by positive/negative sentiment and subjective/objective focus and outputting to a csv file in sentiment_results directory.

4. Run `Vector.py`, Uses each column of dataframe as an array that is compared with cosine similarity. Table are created that make visualizations of scores easier.

5. Run `euclidian.py`. Does the same thing as vector above but calculates euclidian distance between columns. 

6. Run `flesch-kincaid` to get the data analyisis that goes to flesch-kincaid  directory. 

7. Run `sentiment` that uses outside package textblob

  The objective of this report was to quantitate differences between English authors and Shakespeare  in different periods of time. 5 authors combined or unique work were chosen from 1500 and 1650, and another group of 5 works were chosen from 1750-1800. The first group included contemporaries of Shakespeare. One of the ideas was to see if Shakespeare was more similar to his own time, or if the influence Shakespeare had made future works similar to his own style. 5 works of Shakespeare were also included. 
	The works were scrapped from the Guttenberg project and each word was separated and a data frame was created for each work with the unique word and the times it appears in the text. Stop words were removed since they are very common. 
	These data frames were then converted into a data frame that had the frequency of each word in each work. The rows were the word, and the column was the work. These were merged with outer join and all null values were converted to 0. Each column was then transformed into an array. And the Euclidian and cosine similarity between works and between groups (Early, Late and Shakespeare) as well as between works and periods were calculated and a confusion matrix was created. 
	There seemed to be big differences between authors, and little noticeable differences between the values of Shakespeare vs the two periods. However, the data was limited to very few authors and the pool of writers could be considered not representative of the eras. 
Readability scores were also run on the works. These are common metrics used in education to give an idea of difficulty of understanding text. Older works on average had higher grade level scores and lower reading ease scores, than early works. 

Sentiment scores were calculated using textblob library, works were analyzed by polarity which is the emotional tone measured by values of -1 and 1. Shakespeare was balanced and later works where happier 
	
### Limitations of the data
1. The number of texts is limited. We only scrape 15 works.
2. We only control the time that works were published. Further research can focus on other aspects (e.g. genres).

### Limitations of the analysis
1. We only use term frequency (Bag-of-Words) to convert textual data to numerical data.  
