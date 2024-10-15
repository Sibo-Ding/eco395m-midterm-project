import requests
import os

# List of plain text URLs for the selected works
plain_text_urls = [
    "https://www.gutenberg.org/cache/epub/23042/pg23042.txt",
    "https://www.gutenberg.org/cache/epub/1532/pg1532.txt",
    "https://www.gutenberg.org/cache/epub/43440/pg43440.txt",
    "https://www.gutenberg.org/cache/epub/1539/pg1539.txt",
    "https://www.gutenberg.org/cache/epub/1524/pg1524.txt"
]

# Titles corresponding to the URLs
titles = [
    "THE TEMPEST.",
    "JULIUS CAESAR.",
    "ARDEN OF FEVERSHAM.",
    "KING LEAR.",
    "HAMLET, PRINCE OF DENMARK."
]

# Define the relative path for the directory
output_dir = 'shakespeare_works'

# Ensure the current working directory is valid
current_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_dir, output_dir)

# Create a directory to save the works
os.makedirs(output_path, exist_ok=True)

# Initialize a variable to hold all texts
all_texts = ""

# Function to get the text from a plain text URL
def get_text_from_url(url, title):
    response = requests.get(url)
    if response.status_code == 200:
        text = response.text
        start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
        end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"
        start_index = text.rfind(start_marker)  # Find the last occurrence of the title
        end_index = text.find(end_marker)
        if start_index != -1 and end_index != -1:
            return text[start_index + len(start_marker):end_index].strip()
        else:
            print(f"Markers not found in {url}")
            return None
    else:
        print(f"Failed to retrieve the text from {url}. Status code: {response.status_code}")
        return None

# Loop through the URLs and titles, get the text, and append to all_texts
for title, url in zip(titles, plain_text_urls):
    print(f"Fetching text for {title} from {url}")
    text = get_text_from_url(url, title)
    if text:
        all_texts += f"Title: {title}\n\n{text}\n\n{'='*80}\n\n"
        print(f"Extracted text for {title}")

# Save all texts to a single file
output_file = os.path.join(output_path, 'shakespeare_works.txt')
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(all_texts)
print(f"Saved all texts to {output_file}")