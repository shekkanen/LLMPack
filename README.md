# LLMPack
## AI-model based Stream Data Compression
![Your Diagram Title](/the_idea.png)

### Concept Overview

**Idea in a Nutshell:**
- **Data Compression with AI Models:** We utilize advanced AI models (e.g., diffusion models, large language models) to compress data. The data can be of any type, and the compressed output consists solely of sequences of prompt+seed strings, augmented with standard error correction techniques.
  
**Key Considerations:**
- **Technological Constraints:** Current technological limitations include high electricity and power demands, significant VRAM requirements, and the absence of a suitable model specifically designed for this purpose.
  
**Project Status:**
- **Research and Development:** This concept is currently in the exploratory phase. I have not conducted comprehensive research to determine if similar solutions already exist; this project represents a preliminary exploration of potential innovative applications.
- **Proof of Concept:** As of now, this repository does not contain fully functional code, but rather simple tests and demonstrations of the underlying principles.

**Disclaimer:**
- This project is a conceptual demonstration intended to spur further investigation and development within the community.



### Introduction
LLMPack is an open-source project that explores innovative data compression methods using AI-models. This project leverages the advanced generative capabilities of LLMs to encode substantial data volumes into concise prompts accompanied by seeds, facilitating significant data compression and efficient data transfer. The initiative aims to refine, develop, and standardize LLM-based data encoding and decoding, pushing beyond the limits of conventional data compression techniques.

### Concept
The principal concept of LLMPack is to utilize LLMs for encoding raw data into structured prompts that are decoded back to their original form or a close approximation thereof. This process relies on the sophisticated natural language processing capabilities of models such as GPT-3 or BERT, which are adept at generating and interpreting detailed text from minimal inputs.

### Workflow
The workflow of LLMPack includes several key stages:
1. **Data Preparation**: Conversion of raw data into a format amenable to prompt-based encoding.
2. **Prompt Engineering**: Creation of efficient prompts that encapsulate the essential data attributes.
3. **Seed Utilization**: Application of seeds to ensure the determinism of the data regeneration process.
4. **Encoding**: Transformation of data into optimized prompts for transmission.
5. **Transmission**: Delivery of encoded data through standard communication channels.
6. **Decoding**: Reconstruction of the original data from the prompts at the receiver’s end using a pre-trained LLM.

### Examples
#### Example 1: Summarization and Text Generation
This example demonstrates data compression followed by expansion using LLMs. It involves the use of a summarization pipeline to compress text into a summarized form, which is subsequently encoded into a hexadecimal format. The decompression process decodes this format back into text and employs a text-generation model to elaborate the summary into detailed form, illustrating the dual capabilities of LLMs for summarization and generation.

#### Example 2: Keyword Extraction and Data Regeneration
Demonstrating a practical text data compression approach, this example uses simple keyword extraction to create a compressed prompt, which is then expanded back into detailed text using GPT-2. This Python-scripted example underscores the utility of LLMs in processing and regenerating textual information.

#### Example 3: Advanced Summarization with BART
Building upon earlier concepts, this example uses BART—a transformer-based model known for efficient text summarization—to compress data into a summary. This summary is then expanded back into detailed text using sequence generation techniques, showcasing a complete cycle of data transformation.

#### Example 4: Embedding Compression and Expansion Using DistilBERT and GPT-2
This example highlights a hybrid approach where text is first compressed into neural network embeddings using DistilBERT, then expanded into detailed text using GPT-2. It demonstrates the sophisticated integration of multiple models to accomplish complex tasks like data regeneration from compressed representations.

#### Example 5: Text and Token Compression
This example demonstrates the compression of text and its tokens using the zlib library and Levenshtein distance for similarity scoring. Initially, text is read from a file, tokenized using GPT2Tokenizer, and then compressed both as raw text and as token bytes. The tokens are later decompressed and restored to text form, with performance metrics such as compression ratio and similarity score reported to assess the effectiveness of the compression method. The process highlights the utility of combining tokenization and traditional compression methods for effective data reduction.


### Related Studies
- D. Shin, "[Better Text Compression Using a Large Language Model](https://www.tdcommons.org/dpubs_series/6155)," *Technical Disclosure Commons*, August 2023.
- David Gili Fernández de Romarategui, "[Compressing Network Data with Deep Learning](https://upcommons.upc.edu/bitstream/handle/2117/406468/183323.pdf?sequence=2&isAllowed=y)," Master's Thesis, Facultat d'Informàtica de Barcelona (FIB), Universitat Politècnica de Catalunya (UPC) - BarcelonaTech, Thesis Supervisors: Pere Barlet Ros, José Suárez-Varela, Master's Degree in Data Science.

### Contributing
We welcome contributions from the open-source community. For more information on how to contribute, please refer to `CONTRIBUTING.md`.

### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

### Acknowledgements
- We extend our gratitude to all contributors and collaborators who have invested their time and effort into the success of this project.
- Special thanks to [Third-Party Library Name] for providing essential tools that facilitate this research.

### Contact
For inquiries or feedback, please contact us at [Your Email](mailto:your.email@example.com).
