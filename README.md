# Question-Answering System

## Overview

This is a Question-Answering (QA) system designed to efficiently retrieve relevant passages from a corpus of documents in response to user queries. The system utilizes SentenceTransformers for embedding generation, Elasticsearch for data storage and retrieval, Flask for API development, and Streamlit for the user interface.

## Table of Contents

- [Features](#features)
- [System Requirements](#system-requirements)
- [Setup and Installation](#setup-and-instal) 
- [Usage](#usage)

## Features

- **Document Parsing:** Efficiently parsed and processed legal documents, extracting relevant passages and metadata.
- **Embedding Generation:** Uses SentenceTransformers to generate embeddings for efficient and accurate retrieval.
- **Elasticsearch Integration:** Indexed and retrieved embeddings using Elasticsearch for scalable and fast data handling.
- **Flask API:** A well-structured API for interacting with the QA system, including endpoints for querying and document uploading.
- **Streamlit Frontend:** A user-friendly interface for easy interaction with the QA system, built with Streamlit.

## Prerequisites and System Requirements

- Python 3.6 or higher
- SentenceTransformers
- Flask, Docker and Streamlit
- Docker and Docker Compose
- An internet connection for building Docker images

**Requirements File**
- A requirements.txt file that lists all the Python packages required to run the application is the docker directory. You can easily install these with the command:
    ```bash
    pip install -r requirements.txt
    ```
## Setup and Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/pmensah28/Question-Answering-System.git
    cd Question-Answering-System
    ```

2. **Build and Start the Docker Containers:**

    ```bash
    docker-compose up --build -d
    ```
    This command will build the Docker images and start the containers for the Flask API, Elasticsearch, and Streamlit in detached mode.
3. **Start Elasticsearch**
    ````bash
    sudo service elasticsearch start
   ````
   Starting Elasticsearch is a fundamental step in ensuring that the QA system is efficient, scalable, and capable of providing real-time, relevant answers to users’ questions.

## Usage

### Indexing Documents

Documents can be indexed by sending them to the Flask API’s upload endpoint. This can be done directly through a `curl` command or by using the Streamlit interface to upload documents.

### Querying the System

Use the Streamlit web interface to enter your questions. The system will return the top relevant passages from the indexed documents and generate a direct answer using a generative AI model.

Access the Streamlit interface at:

```bash
http://localhost:8501
````
Detailed design and implementation insights are in the `technical.pdf` in the `docs/` directory.
