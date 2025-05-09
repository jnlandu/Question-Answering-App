# Importing libraries
from sentence_transformers import SentenceTransformer
import pandas as pd

# Loading the the CSV file
csv_file = '/home/prince/Dropbox/Question-Answering-System/docs/passage_metadata.csv'
df = pd.read_csv(csv_file)

# Load the SentenceTransformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Generate embeddings for each passages
embeddings = model.encode(df['Passage'].tolist(), convert_to_tensor=True)
# # Displaying the first 2 embeddings for inspection
print(embeddings[:2])
# Convert embeddings tensor to list
embeddings_list = embeddings.tolist()
# Add the embeddings to the DataFrame
df['Embedding'] = embeddings_list

# Save the updated DataFrame with embeddings to a new CSV file
df.to_csv('/home/prince/Dropbox/Question-Answering-System/docs/passage_metadata_emb.csv', index=False)

print("Embeddings generated, added to the dataframe and saved to passage_metadata_emb.csv.")