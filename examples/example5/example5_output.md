# Program Output

## Execution Command
```bash
python3 example5.py textfile.txt 
```

## Results
### Initial Warnings and Settings
- Token indices sequence length is longer than the specified maximum sequence length for this model (18445 > 1024). Running this sequence through the model will result in indexing errors
- 2024-04-16 21:20:01.866510: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.
- 2024-04-16 21:20:01.965794: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.
- 2024-04-16 21:20:01.966493: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
- To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
- 2024-04-16 21:20:03.638859: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT




### Output

```bash
Restored text has been saved to 'restored_text.txt'.
Original Text Length: 65185 bytes
Compressed Text Size: 24939 bytes  
Compressed Token Size: 20582 bytes
Restored Text Match: False
Similarity Score: 99.99384520695492%
```
