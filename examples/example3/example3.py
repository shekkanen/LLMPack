from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import random

model_name = "facebook/bart-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def encode(data, seed):
    """
    Simplified encoding that directly uses data.
    """
    random.seed(seed)
    prompt = f"ENCODE_DATA: {data} (SEED: {seed})"
    return prompt, seed

def decode(prompt, seed):
    """
    Attempt to directly extract data from the prompt.
    """
    random.seed(seed)
    print(f"Debug: Prompt for decoding - {prompt}")
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Use only max_length or max_new_tokens (remove one)
    # Choose the one that best suits your needs
    # Removed max_new_tokens as max_length is set explicitly
    output = model.generate(input_ids, max_length=100)  # Adjusted max_length

    decoded_data = tokenizer.decode(output[0], skip_special_tokens=True)
    print(f"Debug: Raw model output - {decoded_data}")
    return decoded_data

# Example usage
data = "This is some sample data to be encoded."
seed = 42

encoded_prompt, encoded_seed = encode(data, seed)
print(f"Encoded Prompt: {encoded_prompt}")
print(f"Encoded Seed: {encoded_seed}")

decoded_data = decode(encoded_prompt, encoded_seed)
print(f"Decoded Data: {decoded_data}")

if decoded_data.strip() == data:
    print("Decoding successful!")
else:
    print("Decoding failed!")

