from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import pandas as pd

# Load the model and tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Load the previously retrieved passages and questions
df = pd.read_csv('/home/prince/Dropbox/Question-Answering-System/docs/evaluation.csv')

# Function to generate an answer using the generative model
def generate_answer(question, passages):
    # Create a prompt using the question and passages
    prompt = question + " " + " ".join(passages)

    # Encode the prompt to tensor
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Generate answer
    with torch.no_grad():
        output = model.generate(input_ids, max_length=150, num_return_sequences=1,
                                temperature=0.7, top_k=50, top_p=0.95)

    answer = tokenizer.decode(output[0], skip_special_tokens=True)

    return answer

# Generate direct answers for each question and add them to the DataFrame
df['Generative AI Answer'] = df.apply(
    lambda x: generate_answer(x['Question'], [x['Passage 1'], x['Passage 2'], x['Passage 3']]), axis=1
)
# Save the updated DataFrame to a new CSV file
df.to_csv('/home/prince/Dropbox/question_answering/docs/questions_answers_gen.csv', index=False)
print("Results with generative AI answers saved to questions_answers_gen.csv.")
