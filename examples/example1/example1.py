from transformers import pipeline

# Initialize summarization and text generation pipelines
summarizer = pipeline("summarization")
generator = pipeline("text-generation", model="gpt2")

def compress_data(data):
    """
    Compress data by summarizing it and then encoding the summary into a compressed form.
    Args:
        data (str): The original text data to compress.
    
    Returns:
        str: A compressed form of the original text.
    """
    summary = summarizer(data, max_length=50, min_length=25, do_sample=False)[0]['summary_text']
    compressed_data = ''.join([f"{ord(char):x}" for char in summary])  # Simple hexadecimal encoding of summary
    return compressed_data

def decompress_data(compressed_data):
    """
    Decompress data by decoding the compressed form back into text and expanding it.
    Args:
        compressed_data (str): The compressed text data.
    
    Returns:
        str: The decompressed text, an approximation of the original data.
    """
    decoded_summary = ''.join([chr(int(compressed_data[i:i+2], 16)) for i in range(0, len(compressed_data), 2)])
    expanded_data = generator(f"Expand this summary into a detailed text: {decoded_summary}", max_length=200)[0]['generated_text']
    return expanded_data

# Example usage
original_data = "This is a long text that needs to be compressed using an innovative method utilizing LLMs. The process involves summarizing the text, encoding it, and then expanding it back to its original form or something close to it."
compressed_data = compress_data(original_data)
decompressed_data = decompress_data(compressed_data)

print("Original Data:", original_data)
print("Compressed Data:", compressed_data)
print("Decompressed Data:", decompressed_data)
