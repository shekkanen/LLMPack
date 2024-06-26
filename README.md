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

### Theoretical Foundation

#### Video Data Compression and Transmission using SVD

Singular Value Decomposition (SVD) has already demonstrated its potential in the realm of data compression, particularly with video. SVD can effectively reduce a video into a series of principal components, which can be seen as an early conceptual model for what we now envision as prompt+seed sequences.

**Key Insights:**
- **Proof of Concept:** Experiments with SVD show that from a series of prompt+seed sequences, a few seconds of video can be generated. When these sequences are transmitted from one user to another and input into an equivalent system (such as another SVD-based decoder), the exact same video segment can be reproduced.
  
- **Potential Applications:** This proof of concept lays the groundwork for developing AI models that could automate the conversion of existing movie files into prompt+seed sequences. Such a breakthrough could revolutionize how we store, transmit, and consume video content, offering significantly reduced data sizes while maintaining quality.

- **Future Directions:** Looking ahead, the film and media production industries might evolve to incorporate AI-driven tools not only in the compression of existing content but also in the creation of new content. AI could enable more dynamic and adaptable content generation, tailored to user preferences and viewing conditions.

**Challenges and Considerations:**
- **Model Development:** The current challenge lies in creating an AI model that can efficiently convert full-length movies into optimized prompt+seed sequences without losing the essence of the content.
- **Technological Barriers:** As highlighted earlier, the requirements for electricity, computing power, and VRAM are significant and need to be addressed as we develop these advanced AI models.

This section introduces the foundational technologies and highlights the potential of this innovative approach to data compression and content generation. It serves as a call to the research and development community to explore these possibilities further.


### Introduction
LLMPack is an open-source project that explores innovative methods of data compression using AI models. This project leverages the advanced generative capabilities of these models to encode substantial data volumes into concise prompts accompanied by seeds, facilitating significant data compression and efficient data transfer. The initiative aims to refine, develop, and standardize AI-model-based data encoding and decoding, pushing beyond the limits of conventional data compression techniques.


### Concept
The principal concept of LLMPack is to utilize AI-models for encoding raw data into structured prompts that are decoded back to their original form or a close approximation thereof. 

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
I welcome contributions from the open-source community. For more information on how to contribute, please refer to `CONTRIBUTING.md`.

### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

### Contact
For inquiries or feedback, please contact me at [sami.hekkanen@gmail.com](mailto:sami.hekkanen@gmail.com).

