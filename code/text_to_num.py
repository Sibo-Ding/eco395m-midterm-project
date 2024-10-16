import csv
import os
import re

def load_stopwords():
    """Load the stopwords from the file and return a set of the cleaned stopwords."""

    stopwords = set()

    with open(STOPWORDS_PATH, 'r') as file:
        for line in file:
            cleaned_line = re.sub('[^A-Za-z\s]', '', line.strip().lower())
            cleaned_line = re.sub("\s+", " ", cleaned_line)
            stopwords.add(cleaned_line)
    return stopwords


def load_all_lines():
    "Loads every line in the dataset as a list of strings."

    with open(input_path, 'r') as file:
        all_lines = file.readlines()

    return all_lines


def get_words(all_lines):
    """Takes the lines and makes a list of lowercase words."""

    combined_text = " ".join(all_lines)

    clean_text = re.sub('[^A-Za-z\s]', '', combined_text.lower())
    text_with_only_spaces = re.sub("\s+", " ", clean_text)

    words = text_with_only_spaces.split()

    return words


def count_words(words, stopwords):
    """Counts the words that are not stopwords.
    returns a dictionary with words as keys and values."""

    word_counts = dict()
    for word in words:
        if word not in stopwords: 
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    return word_counts


def sort_word_counts(word_counts):
    """Takes a dictionary or word counts.
    Returns a list of (word, count) tuples that are sorted by word in lexicographical order."""
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[0])

    return sorted_word_counts


def write_word_counts(sorted_word_counts, path):
    """Takes a list of (word, count) tuples and writes them to a CSV."""

    column = ["word", "count"]
    with open (output_path, "w") as file:
        write =  csv.writer(file)
        write.writerow(column)
        write.writerows(sorted_word_counts)


if __name__ == "__main__":
    # Change working directory to current .py file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_directory)
    # Change working directory to the repo
    os.chdir('..')

    INPUT_DIR = "text"
    STOPWORDS_PATH = "stopwords.txt"
    OUTPUT_DIR = "words_freq"
    
    file_names = os.listdir(INPUT_DIR)
    
    # Print the file names
    for file_name in file_names:
        input_path = os.path.join(INPUT_DIR, file_name)
        output_path = os.path.join(OUTPUT_DIR, f"{file_name[:-4]}.csv")

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        stopwords = load_stopwords()
    
        all_lines = load_all_lines()
        
        words = get_words(all_lines)

        word_counts = count_words(words, stopwords)
        word_counts_sorted = sort_word_counts(word_counts)

        write_word_counts(word_counts_sorted, output_path)
