import requests
import os

def get_text_from_url(url):
    """For a Gutenberg work, input a URL, output the text."""

    response = requests.get(url)
    if response.status_code == 200:  # If successfully load the webpage
        text = response.text
        start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
        end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"
        start_index = text.rfind(start_marker)  # Find the last occurrence of the title
        end_index = text.find(end_marker)
        if start_index != -1 and end_index != -1:  # If both markers exist
            return text[start_index + len(start_marker):end_index].strip()
        else:
            print(f"Markers not found in {url}")
            return None
    else:
        print(f"Failed to retrieve the text from {url}. Status code: {response.status_code}")
        return None


if __name__ == "__main__":
    ### When changing to other authors, modify urls, authors
    # List of URLs for the selected works
    urls = [
        "https://www.gutenberg.org/cache/epub/23042/pg23042.txt",
        "https://www.gutenberg.org/cache/epub/1532/pg1532.txt",
        "https://www.gutenberg.org/cache/epub/43440/pg43440.txt",
        "https://www.gutenberg.org/cache/epub/1539/pg1539.txt",
        "https://www.gutenberg.org/cache/epub/1524/pg1524.txt"
    ]

    # Authors corresponding to the URLs
    authors = [
        'Shakespeare1',
        'Shakespeare2',
        'Shakespeare3',
        'Shakespeare4',
        'Shakespeare5'
    ]

    # Change working directory to the current .py file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    
    # Create a directory to save the works
    output_dir = 'text'
    os.makedirs(output_dir, exist_ok=True)

    # Loop through the URLs and authors, get the text
    for author, url in zip(authors, urls):
        text = get_text_from_url(url)

        # Save each author's work as a text file
        output_file = os.path.join(output_dir, f"{author}.txt")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Saved text by {author}")
