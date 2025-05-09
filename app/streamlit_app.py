import streamlit as st
import requests

# Function to get answers for a question
def get_answers(question):
    # Replace with the actual URL of your Flask API
    url = 'http://localhost:4000/ask'
    response = requests.post(url, json={'question': question})
    if response.status_code == 200:
        return response.json()['answers']
    else:
        st.write("Error:", response.text)
        return None

# Function to upload documents for indexing
def upload_documents(file):
    # Replace with the actual URL of your Flask API
    url = 'http://localhost:4000/upload'
    response = requests.post(url, files={'file': file})
    return response.status_code == 200

# Streamlit app
st.title('Question-Answering System')

# Upload documents
st.header('Upload Documents')
uploaded_file = st.file_uploader("Choose a file", type=['txt', 'json'])
if uploaded_file is not None:
    if upload_documents(uploaded_file):
        st.success("File uploaded successfully!")
    else:
        st.error("Failed to upload file.")

# Ask questions
st.header('Ask a Question')
question = st.text_input("Enter your question here:")
if st.button('Get Answers'):
    answers = get_answers(question)
    if answers:
        for i, answer in enumerate(answers, start=1):
            st.subheader(f'Passage {i}')
            st.write("Passage:", answer['passage'])
            st.write("Relevance Score:", answer['score'])
            st.write("Metadata:", answer['metadata'])
        st.subheader('Generative AI Answer')
        # You should replace the line below with the actual generative AI answer
        st.write("This is a sample generative AI answer.")
