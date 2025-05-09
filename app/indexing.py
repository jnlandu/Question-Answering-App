# Import libraries
from elasticsearch import Elasticsearch, helpers
import pandas as pd
import json

# Connect to the ElasticSearch cluster
es = Elasticsearch(["http://localhost:9200"])
# Verify that the connection is established
if es.ping():
    print("Connected to ElasticSearch.")
else:
    print("Could not connect to ElasticSearch.")
    exit()

# Load the data from the CSV file
csv_file = '/home/prince/Dropbox/Question-Answering-System/docs/passage_metadata_emb.csv'
df = pd.read_csv(csv_file)

# Prepare the data for bulk indexing
actions = [
    {
        "_index": "passages",
        "_source": {
            "passage": row['Passage'],
            "metadata": json.loads(row['Metadata']),
            "embedding": row['Embedding'][1:-1].split(', ')
        }
    }
    for _, row in df.iterrows()
]

# Create an index
es.indices.create(index="passages", ignore=400)

# Now let's perform bulk indexing
helpers.bulk(es, actions)

print("Data indexed successfully.")
