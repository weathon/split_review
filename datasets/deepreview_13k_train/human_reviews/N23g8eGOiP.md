# NeuZip: Memory-Efficient Training and Inference with Dynamic Compression of Neural Networks

- Decision: Reject
- Scores: 3, 8, 3

## Abstract
The performance of neural networks improves when more parameters are used. However, the model sizes are constrained by the available on-device memory during training and inference. Although applying techniques like quantization can alleviate the constraint, they suffer from performance degradation. In this work, we introduce \name, a new weight compression scheme based on the entropy of floating-point numbers in neural networks. With \name, we are able to achieve memory-efficient training and inference without sacrificing performance. Notably, we significantly reduce the memory footprint of training a Llama-3 8B model from 31GB to less than 16GB, while keeping the training dynamics fully unchanged. In inference, our method can reduce memory usage by more than half while maintaining near-lossless performance. Our code is publicly available

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper presents a entropy based quantization method to reduce the memory footprint in training. It is claimed that this method could reduce around half of the memory without losing accuracy.

### Strengths
The paper made relatively extensive experiments on the modern LLMs, and showed its advantage in reducing memory footprint.

### Weaknesses
1. The motivation is unclear. It's not clear that where the entropy for the sign bit (Figure 1) comes from. The author did not mention in details, where the pre-trained model weight is obtained and whether it is an empirical value or theoretical value, making the analysis not persuasive enough.

2. The compression algorithm is not clearly presented.

3. Codes are not released, otherwise we can make clear what the methodology is by checking the implementation.

### Questions
Are the experiments of pre-trained being ran for a full epoch? How many A6000s are used and how long it took?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This is an interesting work that uses small entropy in the exponent bit to compress neural networks in two settings: lossless and lossy. In the lossless setting the memory consumption and inference speed are both improved. The authors try their models on LLMs with <70B parameters but the method is general and can be used to compress LLMs of larger size. The paper is properly structured, well-written, and easy to follow.

### Strengths
The paper addresses the important problem of increased size of LLMs with lack of resources for training and inference. The algorithm can be built on top of other compression methods. The authors also show that their lossy compression falls on the Pareto frontier and therefore a good compression candidate overall.

### Weaknesses
The paper motivates on linear layer, and their compression requires activations to be saved. This is a restriction specially when small values like GELU type activations are generated in the network. I wonder if the paper suits partial linear activations like ReLU better. Discussion on convutional models, and RNNs will strengthen the paper further.

### Questions
- Transformer-type language models such as BERT-type are getting implemented on edge devices such as cell phones. Do you see a potential that this compression helps the edge implementation of LLMs?
- Do you see a potential for Transformer-alternative architectures such as MAMBA, xLSTMs, JAMBA, etc?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents NeuZip a compression technique for reducing the memory requirements of neural networks for training and inference. NeuZip contains both a lossless and a lossy operating mode, where either only the exponent bits are (losslessly) compressed, or additionally a truncation of the mantissa bits is performed. The performance is tested on various models from the Natural Language Processing community.

### Strengths
- The paper is well structured, the experiments are well described and the figures and tables are informative.
- The developed method in the paper is well explained and clear to understand.
- The experiment settings and presentation of results are well chosen to show the effect of proposed method.

### Weaknesses
 - The novelty of the _NeuZip_ method seems poor.  Lossless NeuZip consists of the direct application of a very widely used compression method (ANS) to (parts of) the weight vector. The lossy compression part is a truncation of mantissa bits, which is a well-known method in data compression (f.e. used in the GRIB2 format). Moreover, the paper fails to mention that this truncation itself is equivalent to quantisation to a non-uniform grid (f.e. float32 with 0 mantissa bits corresponds to quantization with the grid {$\pm 2^{-127}, \pm2^{-126}, \dots \pm2^{128}$}). Quantization with non-uniform grids is a widely used idea (f.e. in "Data Free Network Quantization", Chikin et al. 2022, or NF4 from QLoRA, Dettmers et al. 2023).
- The methods that the paper compares lossless _NeuZip_ to are not fairly chosen, and this is not immediately made obvious in the experimental descriptions. In Table 2, the quantisation methods that _NeuZip_ compares to contain no entropy coding, while _NeuZip_ contains entropy-coding in the exponent bits (which will be especially significant as the ratio of exponent bits to mantissa bits increases). Including entropy coding into the compared quantisation methods would reduce the speed by a small bit, but increase the compression performance at no perplexity cost (which are the metrics the methods are compared on). Again, as the proposed method is equivalent to non-uniform grid quantisation, I would expect most of the gains that are reported in this table to have come from the included entropy coding.
- A large part of the memory efficiency gains of lossless _NeuZip_ come from the established LOMO method (see Table 1). Adding _NeuZip_ on top often reduces the execution speed by a large margin.

### Questions
- I wonder how the reported speeds for the quantization methods such as Quant INT8 in Table 2 came to be. Especially for large models, inference speed-ups should be expected, see Dettmers et al. 2023 (LLM.int8(), https://arxiv.org/abs/2208.07339), appendix D, p.17ff, where LLM.int8 reports increased inference speed for all models that have more than 13B parameters). 
- Similarly, for QLoRA, which has been shown to make networks more memory efficient in the original work, this paper seems to report contrary results, decreasing or barely reducing the memory efficiency compared to vanilla networks as well as suffering a large performance hit (f.e. T5 1B). A discussion of why this happens could be beneficial to the paper, and if it turns out that QLoRA is not suitable for networks this small, other state-of-the-art methods should rather be used to compare _NeuZip_ with.

### Soundness
2

### Presentation
2

### Contribution
1
