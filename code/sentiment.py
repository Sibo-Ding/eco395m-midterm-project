from textblob import TextBlob
import os
import csv


def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity


if __name__ == "__main__":
    INPUT_DIR = "text"
    OUTPUT_DIR = "sentiment_results"

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    OUTPUT_FILE = os.path.join(OUTPUT_DIR, "sentiment_results.csv")

    file_names = os.listdir(INPUT_DIR)

    with open(OUTPUT_FILE, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Text", "Polarity", "Subjectivity"])

        for file_name in file_names:
            input_path = os.path.join(INPUT_DIR, file_name)
            with open(input_path, 'r') as file:
                text = file.read()

            polarity, subjectivity = analyze_sentiment(text)
            csvwriter.writerow([file_name, polarity, subjectivity])
