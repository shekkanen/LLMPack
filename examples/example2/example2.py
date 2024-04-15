from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Ensure that the required model and tokenizer are loaded.
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
model.eval()  # Set the model to evaluation mode

def local_llm_encode(data):
    """
    Simulates a local LLM encoding process by converting data into a compressed form.
    This function will use simple techniques such as keyword extraction or summarization to create a compressed prompt.
    Args:
        data (str): The original data to be encoded.
    
    Returns:
        str: A compressed prompt representing the data.
    """
    # Example of encoding: extract keywords or use a summary. This is a placeholder.
    keywords = ' '.join(set(data.lower().split()))
    return keywords

def decode(prompt):
    """
    Decodes the given prompt using a pre-trained LLM to regenerate the original data.
    Args:
        prompt (str): The compressed prompt to be decoded.
    
    Returns:
        str: The regenerated data based on the prompt.
    """
    # Convert the prompt into tokens.
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    
    # Generate output using the model.
    with torch.no_grad():  # Disable gradient calculations for inference.
        outputs = model.generate(input_ids, max_length=100)
    
    # Decode the output tokens to a string.
    decoded_data = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded_data

# Example usage
original_data = "The quick brown fox jumps over the lazy dog. This is a test of LLM based data compression."
encoded_prompt = local_llm_encode(original_data)
decoded_data = decode(encoded_prompt)

print("Original Data:", original_data)
print("Encoded Prompt:", encoded_prompt)
print("Decoded Data:", decoded_data)
