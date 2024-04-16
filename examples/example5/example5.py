import zlib
import argparse
from transformers import GPT2Tokenizer
import Levenshtein as lev

def compress_text(text, level=9):
    """ Compress text using zlib with a specified compression level. """
    return zlib.compress(text.encode('utf-8'), level=level)

def decompress_text(compressed_text):
    """ Decompress text using zlib. """
    return zlib.decompress(compressed_text).decode('utf-8')

def similarity_score(original, restored):
    """ Calculate similarity score using Levenshtein distance. """
    return 100 - lev.distance(original, restored) * 100 / max(len(original), len(restored))

def compression_ratio(original_size, compressed_size):
    """ Calculate the compression ratio as a percentage of reduction. """
    if compressed_size >= original_size:
        return 0  # Indicates no reduction, or increase in size.
    return 100 * (1 - compressed_size / original_size)

def main(input_file):
    # Read input text from a file
    with open(input_file, 'r', encoding='utf-8') as file:
        original_text = file.read()

    # Initialize tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    
    # Tokenize text
    tokens = tokenizer.encode(original_text, add_special_tokens=True)
    
    # Convert token IDs to bytes
    token_bytes = bytearray()
    for token in tokens:
        token_bytes.extend(token.to_bytes(2, 'big'))
    
    # Compress original text and tokens
    compressed_text = compress_text(original_text)
    compressed_tokens = zlib.compress(token_bytes)
    
    # Save compressed data to files
    with open('compressed_text.zlib', 'wb') as file:
        file.write(compressed_text)
    with open('compressed_tokens.zlib', 'wb') as file:
        file.write(compressed_tokens)

    # Decompress tokens and convert back to text
    decompressed_token_bytes = zlib.decompress(compressed_tokens)
    decompressed_tokens = [int.from_bytes(decompressed_token_bytes[i:i+2], 'big') for i in range(0, len(decompressed_token_bytes), 2)]
    restored_text = tokenizer.decode(decompressed_tokens)

    # Save the restored text to a file
    with open('restored_text.txt', 'w', encoding='utf-8') as file:
        file.write(restored_text)
        print("Restored text has been saved to 'restored_text.txt'.")

    # Similarity and compression efficiencies
    similarity = similarity_score(original_text, restored_text)
    original_text_length = len(original_text.encode('utf-8'))
    text_compression_ratio = compression_ratio(original_text_length, len(compressed_text))
    token_compression_ratio = compression_ratio(len(token_bytes), len(compressed_tokens))

    # Print results
    print(f"Original Text Length: {original_text_length} bytes")
    print(f"Compressed Text Size: {len(compressed_text)} bytes")
    print(f"Compressed Token Size: {len(compressed_tokens)} bytes")
    print(f"Restored Text Match: {original_text == restored_text}")
    print(f"Similarity Score: {similarity}%")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Text and Token Compression Tool')
    parser.add_argument('input_file', type=str, help='File containing text to compress')
    args = parser.parse_args()
    main(args.input_file)
