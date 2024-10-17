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
To do:  
Format the code eventually!
