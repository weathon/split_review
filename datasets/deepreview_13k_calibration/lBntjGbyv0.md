# BitStack: Fine-Grained Size Control for Compressed Large Language Models in Variable Memory Environments

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Large language models (LLMs) have revolutionized numerous applications, yet their deployment remains challenged by memory constraints on local devices. While scaling laws have enhanced LLM capabilities, the primary bottleneck has shifted from \textit{capability} to \textit{availability}, emphasizing the need for efficient memory management. Traditional compression methods, such as quantization, often require predefined compression ratios and separate compression processes for each setting, complicating deployment in variable memory environments. In this paper, we introduce \textbf{BitStack}, a novel, training-free weight compression approach that enables megabyte-level trade-offs between memory usage and model performance. By leveraging weight decomposition, BitStack can dynamically adjust the model size with minimal transmission between running memory and storage devices. Our approach iteratively decomposes weight matrices while considering the significance of each parameter, resulting in an approximately 1-bit per parameter residual block in each decomposition iteration. These blocks are sorted and stacked in storage as basic transmission units, with different quantities loaded based on current memory availability. Extensive experiments across a wide range of tasks demonstrate that, despite offering fine-grained size control, BitStack consistently matches or surpasses strong quantization baselines, particularly at extreme compression ratios. To the best of our knowledge, this is the first decomposition-based method that effectively bridges the gap to practical compression techniques like quantization.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Authors propose BitStack, a training-free weight compression method using weight decomposition. The method performs well on extreme compression ratio. The method also allows model of an arbitrary size for whichever the GPU memory allows.

### Strengths
1. Paper is clearly written and well-motivated.
2. A method that adapt models to different sizes dynamically should be very useful in practice.

### Weaknesses
See questions

### Questions
1. How long does it take to dynamically load/off-load a residual block? What is the strategy to achieve the best performance/latency tradeoff? Is more or less adjustment preferred during inference?
2. Based on the comparison between 8B and 70B, it seems that one should use llama-8B at FP16 instead of llama-70B at an extreme compression ratio. At least in this case, the extreme quantization does not seem to be needed. And I assume that the latency of a quantized larger model is also worse than the latency of a smaller model at FP16.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces BitStack, a novel training-free compression approach for Large Language Models (LLMs) that addresses the challenge of deploying models in environments with variable memory constraints. Unlike traditional compression methods such as quantization that require predefined compression ratios and separate compression processes for each setting, BitStack enables dynamic adjustment of model size at the megabyte level through an innovative weight decomposition technique. The method works by iteratively decomposing weight matrices based on parameter significance, creating approximately 1-bit per parameter residual blocks that are stored and can be loaded flexibly based on available memory. BitStack not only provides fine-grained control over the memory-performance trade-off but also matches or exceeds the performance of established quantization methods like GPTQ and AWQ, particularly at extreme compression ratios. This approach is particularly valuable for local deployment scenarios where available memory may fluctuate due to other applications running concurrently.

### Strengths
- Novel Problem Framing: The paper addresses a practical and important problem of deploying LLMs in variable memory environments
It identifies a gap in existing compression methods that typically require fixed compression ratios.
- Practical Utility: Enables dynamic trade-offs between memory usage and model performance eliminating the need for multiple compressed versions of the same model. This reduces storage burden by avoiding separate compression processes for different ratios
- A comprehensive set of experiments across different model scales with convincing results and good ablations to justify different design choices.

### Weaknesses
### Major
- This paper is motivated to work in variable memory environments where the amount of memory changes and a compression algorithm is provided. It would be great to have some results on how this compares in efficiency to other memory management techniques like paging. In what scenario is and how more effective is BitStack compared to a systems level optimization that allows to offload parts of the model not currently being used ? Specifically, the paper lacks a comparison against standard memory offloading techniques, which are commonly used in systems with limited memory. The core question is whether BitStack's compression and decompression overhead is less than the overhead of swapping model weights to and from slower storage. A detailed analysis of this trade-off is crucial for understanding the practical benefits of BitStack in real-world scenarios. Without this, it's difficult to ascertain if the proposed method is truly superior to existing memory management practices.

### Minor
- In Table 1, 2,3 it might be a good idea to make the best method's results in bold, to make it easier for the reader.
- Could you clarify what the multiple folders and smaller llama in figure 1a actually refer to ?
- In the abstract the paper references that the primary bottleneck for LLMs is capability and not availability. How does this factor in with other LLM problems like hallucination, knowledge cutoffs etc?

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces BitStack, an iterative weight decomposition method to compress the Large Language Models (LLMs). By adjusting the number of iterations, BitStack can compress LLMs with various compression ratio. Experimental results demonstrate that BitStack achieves comparable performance to quantization-based methods.

### Strengths
1.It is the first decomposition-based method that achieves comparable performance to quantization approaches.

2.The motivation of variable RAM on devices sounds is interesting.

3.The model compressed by BitStack is more scalable for deployment.

### Weaknesses
1.The evaluations should be enhanced. Both AWQ and GPTQ are no longer considered state-of-the-art quantization methods as of the current time. Even AWQ was submitted to arXiv over a year ago (June 2023).

2.Despite this, the performance gap between BitStack and AWQ is relatively small. For instance, the average accuracy scores of BitStack surpass those of AWQ-w2 by 1.4 points (30.8 vs. 29.4) across the LLaMA 3.1 8B model. Given that the full-precision model achieves an accuracy score of 74.1, this improvement is quite marginal.

3. When the compression ratio is below 70%, BitStack's performance tends to be weaker than AWQ on most benchmarks.

4. What is the real-world inference speed of BitStack? This is a crucial aspect for a compression method targeting large language models (LLMs), yet it is not addressed in the paper.

5. The font size in Figures 1, 2, 5, 6, and 7 is too small

### Questions
See weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents BitStack, a training-free weight compression method for large language models that adeptly navigates memory constraints on local devices. By utilizing weight decomposition and stacking blocks in storage as basic transmission units, BitStack enables dynamic adjustments to model size, offering megabyte-level trade-offs between memory usage and performance. The method achieves comparable or superior results to traditional quantization techniques.

### Strengths
- The paper addresses a crucial problem in memory allocation for large language models (LLMs) in edge computing scenarios with limited RAM.
- The research is backed by solid experimental evidence, enhancing its credibility.

### Weaknesses
 - The writing could be improved for clarity. The rationale for sorting SVD matrices is not well-explained, and the process of loading/offloading within and between layers needs better elucidation.
- The paper doesn't provide details about the caching process, which seems to be an integral part of the method. Discussion on cache size and caching strategy is missing.
- The impacts of SVD on model performance aren't discussed. The paper should elaborate on the effects of various decomposition parameters and distinguish the proposed SVD from those used in previous model compression techniques.
- The sorting algorithm and strategy need better description and justification. It's unclear how different matrices in LLMs should be decomposed and sorted using the proposed method.



### Questions
- Certain terms, like 'residual block', need to be defined more clearly as it seems to differ from its usage in the context of CNNs.
- The choice of "zeropoint quantization" as a baseline needs to be justified since simple zero point quantization is known to be ineffective in LLMs.

### Soundness
2

### Presentation
2

### Contribution
2
