# Question-Answering System

## Overview

This is a Question-Answering (QA) system designed to efficiently retrieve relevant passages from a corpus of documents in response to user queries. The system utilizes SentenceTransformers for embedding generation, Elasticsearch for data storage and retrieval, Flask for API development, and Streamlit for the user interface.

## Table of Contents

- [Features](#features)
- [System Requirements](#system-requirements)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)

## Features

- **Document Parsing:** Efficiently parsed and processed legal documents, extracting relevant passages and metadata.
- **Embedding Generation:** Uses SentenceTransformers to generate embeddings for efficient and accurate retrieval.
- **Elasticsearch Integration:** Indexed and retrieved embeddings using Elasticsearch for scalable and fast data handling.
- **Flask API:** A well-structured API for interacting with the QA system, including endpoints for querying and document uploading.
- **Streamlit Frontend:** A user-friendly interface for easy interaction with the QA system, built with Streamlit.

## System Requirements

- Python 3.6 or higher (if you plan to run services outside of Docker)
- Docker and Docker Compose
- An internet connection (for downloading base Docker images and dependencies)

The necessary Python packages are listed in `docker/requirements.txt`. These are installed automatically when building the Docker images.

## Setup and Installation

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/pmensah28/Question-Answering-System.git
    cd Question-Answering-System
    ```

2.  **Build and Start the Docker Containers:**

    ```bash
    docker-compose up --build -d
    ```
    This command will build the Docker images and start the containers for the Flask API, Elasticsearch, and Streamlit in detached mode. Ensure Docker is running before executing this command.

## Usage

### Indexing Documents

Documents can be indexed by sending them to the Flask API’s upload endpoint. This can be done directly through a `curl` command or by using the Streamlit interface to upload documents.

### Querying the System

Use the Streamlit web interface to enter your questions. The system will return the top relevant passages from the indexed documents and generate a direct answer using a generative AI model.

Access the Streamlit interface at:

```
http://localhost:8501
```
Detailed design and implementation insights are in the `technical.pdf` in the `docs/` directory.


