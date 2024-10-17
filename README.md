# eco395m-midterm-project


1. Scrape 15 works from Project Gutenberd. Run `code/scrape_literatures.py`, output text files in `text`. Each text is a work from an author. 5 works from pre-Shakespeare period and 5 works from post-Shakesoeare period.

2. Convert texts from the previous step to vectors of word frequency (BoW). Run `code/text_to_num.py`, output 15 csv files in `words_freq`. Each csv is the word frequency of a text.  

3. Reformat the code files via Black command.

4. Run `Vector.py`, Uses each column of dataframe as an array that is compared with cosine similarity. Table are created that make visualizations of scores easier.

5. Run `euclidian.py`. Does the same thing as vector above but calculates euclidian distance between columns. 

6. Run `flesch-kincaid` to get the data analyisis that goes to flesch-kincaid  directory. 

7. Run `sentiment` that uses outside package textblob
To do:  
Format the code eventually!
