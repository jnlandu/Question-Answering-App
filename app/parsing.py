# Importing the necessary libraries!
import json
import pandas as pd
from typing import List, Tuple

# Let's start by reading and inspecting the contents of the provided _Technical.txt file.
# File paths
technical_txt_file_path = '/home/prince/Dropbox/Question-Answering-System/dataset/Corpus/kwame-legal-LG-1680770745754_Technical.txt'
print("Reading and inspecting file contents...")
# Read the content of the _Technical.txt file
with open(technical_txt_file_path, 'r') as file:
    technical_txt_content = file.read()

# Display the first 500 characters to inspect the content
# print(technical_txt_content[:500])  # Let's now print a snippet of the file content for inspection
print("successfully read file contents")
# Let's now write a function to extract passages and metadata
def extract_passages_and_metadata(technical_txt: str, metadata_json: str) -> Tuple[List[str], str]:
    # Extracting passages within __paragraph__ markers
    paragraphs = technical_txt.split('__section__')[1:]  # Skip the first split as it will be empty
    extracted_passages = []
    for section in paragraphs:
        passages = section.split('__paragraph__')[1:]  # Skip the first split as it will be the section title
        extracted_passages.extend(passages)

    # Combining all extracted passages into 1 passage
    combined_passage = ' '.join([passage.strip() for passage in extracted_passages])

    # Splitting the combined passage into chunks of 5-sentences to form a passage each
    sentences = combined_passage.split('.')
    chunks_of_5_sentences = ['.'.join(sentences[i:i + 5]).strip() for i in range(0, len(sentences), 5)]

    # Removing empty strings if any
    chunks_of_5_sentences = [chunk for chunk in chunks_of_5_sentences if chunk]

    # Extracting metadata from the JSON file
    with open(metadata_json, 'r') as file:
        metadata = json.load(file)
    metadata_str = json.dumps(metadata)  # Converting metadata dict to string

    return chunks_of_5_sentences, metadata_str

# Specifying file paths for the metadata file
metadata_json_file_path = '/home/prince/Dropbox/Question-Answering-System/dataset/Corpus/kwame-legal-LG-1680770745754_Metadata.json'
# Extracting passages and metadata
passages, metadata = extract_passages_and_metadata(technical_txt_content, metadata_json_file_path)

# Displaying first 2 extracted passages and the corresponding metadata for inspection
# print(passages[:2], metadata) # Got the expected output
print("passage and metadata have been successfully extracted")

# Creating a DataFrame to hold the passages and metadata
passages_metadata_df = pd.DataFrame({
    'Passage': passages,
    'Metadata': [metadata] * len(passages)  # Replicating metadata for each passage
})
# Displaying the first few rows of the DataFrame for inspection
# print(passages_metadata_df.head()) # Intentionally commented this out after viewing the outputs though!

# Saving the DataFrame to a CSV file
csv_file_path = '/home/prince/Dropbox/Question-Answering-System/docs/passage_metadata.csv'
passages_metadata_df.to_csv(csv_file_path, index=False)
# Displaying the path to the generated CSV file
print("Passages with their corresponding metadata have been successfully extracted and paired. Check the file path below!")
print(csv_file_path)


