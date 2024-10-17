import re
import os
import csv


def count_syllables(word):
    word = word.lower()
    word = re.sub(r"[^a-z]", "", word)
    vowels = "aeiouy"

    syllable_count = len(re.findall(r"[aeiouy]+", word))

    if word.endswith("e") and len(re.findall(r"[aeiouy]", word)) > 1:
        syllable_count -= 1

    if word.endswith("le") and len(word) > 2 and word[-3] not in vowels:
        syllable_count += 1

    return max(1, syllable_count)


def flesch_kincaid(text):
    words = re.findall(r"\b\w+\b", text)
    sentences = re.split(r"[.!?]", text)

    total_words = len(words)
    total_sentences = len([s for s in sentences if s.strip() != ""])
    total_syllables = sum(count_syllables(word) for word in words)

    flesch_reading_ease = (
        206.835
        - 1.015 * (total_words / total_sentences)
        - 84.6 * (total_syllables / total_words)
    )
    flesch_kincaid_grade = (
        0.39 * (total_words / total_sentences)
        + 11.8 * (total_syllables / total_words)
        - 15.59
    )

    return flesch_reading_ease, flesch_kincaid_grade


if __name__ == "__main__":
    INPUT_DIR = "../text"
    OUTPUT_DIR = "../flesch-kincaid_results"

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    readability_csv = os.path.join(OUTPUT_DIR, "readability_results.csv")
    grade_csv = os.path.join(OUTPUT_DIR, "grade_level_results.csv")

    with open(readability_csv, "w", newline="") as readability_file, open(
        grade_csv, "w", newline=""
    ) as grade_file:
        readability_writer = csv.writer(readability_file)
        grade_writer = csv.writer(grade_file)

        readability_writer.writerow(["Text", "Flesch-Kincaid reading ease"])
        grade_writer.writerow(["Text", "Flesch-Kincaid grade level"])

        file_names = os.listdir(INPUT_DIR)
        for file_name in file_names:
            input_path = os.path.join(INPUT_DIR, file_name)

            with open(input_path, "r") as file:
                text = file.read()

            flesch_reading_ease, flesch_kincaid_grade = flesch_kincaid(text)

            readability_writer.writerow([file_name, flesch_reading_ease])
            grade_writer.writerow([file_name, flesch_kincaid_grade])
