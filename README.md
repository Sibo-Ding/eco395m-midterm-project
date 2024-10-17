# eco395m-midterm-project

1. Scrape 15 works from Gutenberd. Run `code/scrape_literatures.py`, output text files in `text`. Each text is a work from an author.  
2. Convert texts from the previous step to vectors of word frequency (BoW). Run `code/text_to_num.py`, output 15 csv files in `words_freq`. Each csv is the word frequency of a text.  
3. Reformat the code files via Black command.
4. Run flesch_kincaid.py: outputs two csv files in flesch-kincaid_results directory with flesch-kincaid analysis for each text, scoring the text by grade level and general readability
5. Run sentiment.py: uses TextBlob library to analyze the sentiment of each text, scoring each by positive/negative sentiment and subjective/objective focus and outputting to a csv file in sentiment_results directory.

To do:  
Format the code eventually!
