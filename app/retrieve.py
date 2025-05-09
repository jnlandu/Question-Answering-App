from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Function to retrieve relevant passages
def retrieve_passages(question: str, model, es, index_name, top_n=3):
    # Generate embedding for the question
    question_embedding = model.encode([question], convert_to_tensor=True)

    # Elasticsearch query to retrieve relevant passages
    query = {
        "size": top_n,
        "query": {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                    "params": {"query_vector": question_embedding[0].tolist()}
                }
            }
        }
    }

    # Execute the query
    results = es.search(index=index_name, body=query)

    # Extract passages and scores
    passages = [
        {
            "passage": hit["_source"]["passage"],
            "score": hit["_score"],
            "metadata": hit["_source"]["metadata"]
        }
        for hit in results["hits"]["hits"]
    ]

    return passages

# Initialize the Elasticsearch client
es = Elasticsearch(["http://localhost:9200"])

# Load SentenceTransformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Specify the index name
index_name = "passages"

# Example questions
questions = ["What is a valid offer?", "What case defines what an offer is?"] # Just randomly chose two question from the Example excel file provided in the drive folder

# Retrieve relevant passages and save to CSV
data = []
for question in questions:
    passages = retrieve_passages(question, model, es, index_name)
    row = {
        "Question": question,
        **{
            f"Passage {i+1}": passages[i]["passage"],
            f"Relevance Score {i+1}": passages[i]["score"],
            f"Passage {i+1} Metadata": passages[i]["metadata"]
            for i in range(len(passages))
        }
    }
    data.append(row)

# Create a DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("/home/prince/Dropbox/Question-Answering-System/docs/questions_answers.csv", index=False)
print("Successfully implemented elasticsearch integration and document retrieval")
print("Results saved to questions_answers.csv.")
