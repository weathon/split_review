# SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
The transformer architecture predominates across various models. As the heart of the transformer, attention has a computational complexity of $O(N^2)$, compared to $O(N)$ for linear transformations. When handling large sequence lengths, attention becomes the primary time-consuming component. Although quantization has proven to be an effective method for accelerating model inference, existing quantization methods primarily focus on optimizing the linear layer.
In response, we first analyze the feasibility of quantization in attention detailedly. Following that, we propose \our, a highly efficient and accurate quantization method for attention. The OPS (operations per second) of our approach outperforms FlashAttention2 and xformers by about \textbf{2.1x} and \textbf{2.7x}, respectively. \our also achieves superior accuracy performance over FlashAttention3. Comprehensive experiments confirm that our approach incurs almost \textbf{no end-to-end metrics loss across diverse models}—including those for large language processing, image generation, and video generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a new attention quantization method for speeding up transformer inference. To accelerate attention, the authors propose using INT8 quantization instead of FP8 for faster matrix multiplication on GPUs, along with a method for smoothing the K matrix to improve accuracy. Instead of quantizing the P and V matrices, they maintain them in FP16 and use a low-precision FP16 accumulator for faster multiplication without accuracy loss.  Finally, they offer different speed-accuracy trade-offs and a layer-wise selection method for optimal performance. Extensive experiments have been done on different transformer models for text, image and video generation tasks. The results show that the proposed SageAttention speeds up the FlashAttention2 and xformers by more than 2 times without losing any performance.

### Strengths
1. The contributions of this work are well motivated. 

2. The proposed method seems to be novel although I am not an expert in this field. 

3. The experiments are quite extensive, covering two different GPUs (RTX4090 and RTX3090), representative models for language, image, and video generation, and a wide range of datasets. 

4. The results are quite impressive, showing more than two times speedup without performance degradation.

### Weaknesses
1. Some design choices seem to be decided by the specific hardwares that are evaluated RTX4090 and 3090 (L271). Are those design choices also compatible with other GPUs like A100 and H100? Specifically, the use of INT8 quantization and the low-precision FP16 accumulator might be optimized for the specific architecture of the RTX series, and it's unclear if the same performance gains would be observed on GPUs with different tensor core implementations or memory hierarchies. The paper should provide a more detailed analysis of how these choices interact with different hardware architectures.

2. Table 7 shows that different model/task has different speedup. How is the speedup related to the specific transformer architecture, model size, and complexity of the task? The paper lacks a clear explanation of why the speedup varies across different models and tasks. It's important to understand if the speedup is consistent across different transformer architectures (e.g., encoder-only, decoder-only, encoder-decoder), model sizes (number of parameters), and task complexities (e.g., text generation vs. image generation). A more detailed analysis is needed to understand the factors that influence the observed speedup.

### Questions
I am not an expert in this field and do not have additional questions at this stage. I might have more questions at the discussion phase.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This papers conducts in depth analysis of viability to quantize LLMs/Diffusion models into INT8 frameworks. It also proposes smoothing methods to alleviate the outlier pains in the QKV projection process, demonstrating viable tradeoffs. Comparisons to relevant work is strong.

### Strengths
- Paper is well written.
- Experiments are thorough.
- Problem is challenging.

### Weaknesses
 - Full comparison to strong SOTA methods such as Flash attention 3, though slightly mentioned in the introduction and in Table 14, is not deeply explored.
- Only targeted 4090/3000 series GPUs - it would be recommended to be tested on stronger GPUs at server level that is facing the strongest limitations.
- It would be great to test across VLMs too.

### Questions
As above in weakness.

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
This paper presents SageAttention, an innovative quantization method designed to optimize the computational efficiency of attention mechanisms in transformer models by employing an 8-bit integer (INT8) quantization. It employs the FlashAttention-wise quantization and matrix smoothing with FP16 for Matmul. With all these proposed components,  the method demonstrates improved computational performance and maintains accuracy compared to existing solutions like FlashAttention2 and xformers.

### Strengths
+ The paper is well-written, with a logical structure and organization that facilitates understanding.

+ SageAttention shows competitive performance, outperforming FlashAttention2 and xformers by approximately 2.1x and 2.7x, respectively.

+ The method exhibits almost no end-to-end metrics loss across a variety of models, including large language models (LLMs), text-to-image (T2I), and text-to-video (T2V).

+ The discovery of channel-wise consistency, as illustrated in Figure 4, is particularly noteworthy and adds depth to the research.

### Weaknesses
 - The method relies heavily on FlashAttention, which may weaken its technical contribution and originality. What will the performance be if it does not employ the FlashAttention as the basis?

- The reported superiority over FlashAttention3 appears to be quite marginal, raising questions about the significance of the improvements.

- Another major weakness of this paper is that it does not compare SageAttention with other task-specific quantization methods, such as AWQ [1] for LLMs, Q-diffusion [2] for text-to-image, and ViDiT-Q [3] for text-to-video applications, which could provide a more comprehensive evaluation of its performance.

### Questions
Could the authors elaborate on the "Llama" column of Table 1? Specifically, why does the number remain stable even with quantization? Understanding this aspect could provide valuable insights into the robustness of the proposed method.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work explores post-training quantization of the attention mechanism. It claims that it's not well explored in the literature and the existing works focus either on quantized training or post-training quantization of non-attention layers (of course, among other attention acceleration methods, like linear attention, algorithmic accelerations, etc.). The work observed that the Keys matrix has similar values per-token, and proposed to smooth it by applying a per-token bias. It explores optimal quantization strategies and combines it with flash attention algorithmic techniques to obtain the best performance. SageAttention achieves very high reconstruction quality and does not seem to lose much performance on downstream metrics.

### Strengths
- The performance boosts seem to be impressive compared to 
- The work carries a valuable observation that the keys matrix has huge correlation per-token. It can be valuable even outside of 
- I find the evaluation section to be very thorough, including many domains (text2image, text2video, LLMs). I especially appreciate text2video (where the sequences are the longest) and performance exploration on second-tier GPUs (e.g. 3090), which are more suitable for production use cases.
- I am not an expert in quantization, but I checked some prior works and didn't find similar approaches. This makes me consider the paper as novel.
- The paper provides the source code: I have not tried running it but it is valuable.

### Weaknesses
 - I think that writing should be improved. A table I would like to see the most is the end-to-end model speed improvement and metrics degradation after integrating the proposed attention mechanism. First, for many models accelerating the attention op itself does not necessarily lead to much improved overall speed when the sequence length is short and it's MLPs who carry the main burden. Second, it's not entirely clear when looking at various tables which variant is being used at the end (and why there are so many of them throughout the paper instead of being just in some restricted ablation section). Finally, there are quite many typos and grammatical errors, e.g.:
    - L084: "matrice" => "matrices"
    - L138 (and elsewhere): "IO" => "I/O"
    - L144: "it compute" => "it computes"
    - L142=144: missing line or equation
    - L151: "The σ()" => "The" should be ommited or it should be "The function σ()".
    - L184: "First, We" => "First, we"
    - L264-L266: ~3 typos in 3 lines
    - etc.
- There are no qualitatives provided for image/video generation.

### Questions
- Is there a final attention variant among the proposed ones which performs the best uniformly across all tasks?
- L154: "The expression diag(l_i^j)^{-1}" would produce inf-s since l_i^j is initialized as 0. Or how is O_i^j initialized?
- L151: What is "online softmax" (i dont see it to be defined explicitly)? How does it differ from the standard softmax?

### Soundness
3

### Presentation
2

### Contribution
3
