from transformers import DistilBertTokenizer, DistilBertModel, GPT2Tokenizer, GPT2LMHeadModel
import torch
import random

# Load DistilBERT for compression
distilbert_model_name = "distilbert-base-uncased"
distilbert_tokenizer = DistilBertTokenizer.from_pretrained(distilbert_model_name)
distilbert_model = DistilBertModel.from_pretrained(distilbert_model_name)

# Load GPT-2 for expansion
gpt_model_name = "gpt2"
gpt_tokenizer = GPT2Tokenizer.from_pretrained(gpt_model_name)
gpt_model = GPT2LMHeadModel.from_pretrained(gpt_model_name)

def compress_text(data, seed):
    """
    Use DistilBERT to obtain a fixed-size embedding of the data.
    """
    random.seed(seed)
    inputs = distilbert_tokenizer(data, return_tensors="pt")
    outputs = distilbert_model(**inputs)
    # Use the mean of the last hidden states as a simple compression strategy
    compressed_embedding = outputs.last_hidden_state.mean(dim=1)
    return compressed_embedding

def expand_text(embedding):
    """
    Use GPT-2 to generate text based on a prompt influenced by the embedding.
    """
    # Simplified example of using the norm of the embedding as a seed for the prompt
    prompt_seed = torch.norm(embedding).item()
    prompt = f"Generate a detailed description for the concept with code {prompt_seed:.2f}:"
    
    # Encode and generate text
    inputs = gpt_tokenizer(prompt, return_tensors="pt")
    outputs = gpt_model.generate(inputs['input_ids'], max_length=100)
    expanded_text = gpt_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return expanded_text

# Example usage
data = "This is some sample data to be encoded."
seed = 42

compressed_data = compress_text(data, seed)
expanded_data = expand_text(compressed_data)

print("Original Data:", data)
print("Compressed Data (Embedding Norm):", torch.norm(compressed_data).item())
print("Expanded Data:", expanded_data)

