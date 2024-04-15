# Program Output

## Execution Command
```bash
python3 example2.py 
```

## Results
### Initial Warnings and Settings
- The attention mask and the pad token id were not set. As a consequence, you may observe unexpected behavior. Please pass your input's `attention_mask` to obtain reliable results.
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
- 2024-04-15 18:02:41.802726: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
- To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
- 2024-04-15 18:02:44.179794: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT


### Data Processing
**Original Data:**  

The quick brown fox jumps over the lazy dog. This is a test of LLM based data compression..

**Compressed Data:**  

based is the this jumps a quick fox llm lazy over of compression. test brown dog. data

**Decompressed Data:**  

based is the this jumps a quick fox llm lazy over of compression. test brown dog. data.txt -rw-r--r-- 1 root root root.data.txt data.txt -rw-r--r-- 1 root root root.data.txt -rw-r--r-- 1 root root root.data.txt -rw-r--r-- 1 root root root.data.txt -rw-r--r-- 1 root root root.data.txt
