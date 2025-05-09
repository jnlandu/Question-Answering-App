from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import pandas as pd

# Initialize ElasticSearch client
es = Elasticsearch(["http://localhost:9200"])

# Initialize the SentenceTransformers model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Load the user queries
with open('/home/prince/Dropbox/Question-Answering-System/dataset/user_queries.txt', 'r') as file:
    queries = file.readlines()

# Stripping off newline characters
queries = [query.strip() for query in queries if query.strip()]

# Displaying the first few queries for verification
print(queries[:5])  # Displaying the first 5 queries for verification

# Create a DataFrame to hold the evaluation data
evaluation_data = []

# Search for relevant passages for each query
for query in queries:
    query = query.strip()
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Search in ElasticSearch
    search_results = es.search(index='passage_index', body={
        'size': 3,
        'query': {
            'script_score': {
                'query': {'match_all': {}},
                'script': {
                    'source': "cosineSimilarity(params.query_vector, doc['embedding']) + 1.0",
                    'params': {'query_vector': query_embedding.tolist()[0]}
                }
            }
        }
    })

    passages = [hit['_source']['passage'] for hit in search_results['hits']['hits']]
    metadata = [hit['_source']['metadata'] for hit in search_results['hits']['hits']]
    scores = [hit['_score'] for hit in search_results['hits']['hits']]

    evaluation_data.append([
        query,
        passages[0], scores[0], metadata[0], '',  # Empty string for manual rating
        passages[1], scores[1], metadata[1], '',
        passages[2], scores[2], metadata[2], ''
    ])

# Create a DataFrame and save to CSV
columns = [
    'Question',
    'Passage 1', 'Relevance Score 1', 'Passage 1 Metadata', 'Is Passage 1 Relevant?',
    'Passage 2', 'Relevance Score 2', 'Passage 2 Metadata', 'Is Passage 2 Relevant?',
    'Passage 3', 'Relevance Score 3', 'Passage 3 Metadata', 'Is Passage 3 Relevant?'
]
evaluation_df = pd.DataFrame(evaluation_data, columns=columns)
evaluation_df.to_csv('/home/prince/Dropbox/Question-Answering-System/docs/evaluation.csv', index=False)

# Now let's Load the rated evaluation data
rated_df = pd.read_csv('/home/prince/Dropbox/Question-Answering-System/docs/evaluation.csv')

# Compute the top-1 and top-3 accuracies
top_1_accuracy = rated_df['Is Passage 1 Relevant?'].value_counts(normalize=True)['Yes'] * 100
top_3_accuracy = rated_df[['Is Passage 1 Relevant?', 'Is Passage 2 Relevant?', 'Is Passage 3 Relevant?']].apply(
    lambda x: 'Yes' in x.values, axis=1
).value_counts(normalize=True)[True] * 100

# Print the accuracies
print(f'Top-1 Accuracy: {top_1_accuracy}%')
print(f'Top-3 Accuracy: {top_3_accuracy}%')

# Save the accuracy results to a CSV file
accuracy_df = pd.DataFrame({
    'Top 1 Accuracy': [top_1_accuracy],
    'Top 3 Accuracy': [top_3_accuracy]
})
accuracy_df.to_csv('/home/prince/Dropbox/Question-Answering-System/docs/performance.csv', index=False)


