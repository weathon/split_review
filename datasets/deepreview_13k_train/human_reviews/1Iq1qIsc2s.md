# Revisiting Positional Information in Transformers in the era of Fused Attention

- Decision: Reject
- Scores: 8, 5, 6

## Abstract
Imparting positional information has been a crucial component in Transformers due to attention's invariance to permutation. Methods that bias attention weights, like Relative Positional Bias (RPB), have been preferred choice in more recent transformer-based architectures for vision. In parallel, fused attention has become the standard implementation for attention, largely thanks to open source solutions such as Flash Attention and FMHA. However, it is not trivial to fuse explicit biasing or masking of attention weights into a fused attention kernel without affecting its performance. In this scenario, position embeddings present themselves as a viable replacement for attention weight biases. Position embeddings are applied to the tokens directly, decoupled from the attention mechanism, thereby sidestepping the problems that arise with attention weight biases in fused kernels. In this work, inspired by the booming LLM landscape, we analyze the applicability of Rotary Position Embeddings (RoPE) as a replacement for RPBs in vision models. Unlike RPB which explicitly biases attention weights, RoPE biases the dot product inputs (query and key) directly and ahead of the attention operation. We empirically show the prowess of RoPE over RPBs in terms of accuracy and speed. We study multiple implementations of RoPE and show that it is sufficient to use only a fraction of hidden dimensions for RoPE to achieve competitive performance. We also develop a fast implementation for Axial RoPE. Together with the most performant fused attention implementations, and our fast RoPE implementation, we observe  inference speedups compared to RPB with improved or similar accuracy.  We foresee RoPE as a replacement for RPBs, paving the way for the widespread adoption of fused attention in transformer-based vision models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes using RoPE embeddings, a popular and widely used method for LLMs for vision transformers motivated by imperial gains in accuracy and efficiency when applying to multiple models of various sizes. For this, they extend RoPE to fit image space and tackle the challenge of implementing it and studying multiple rotary positional embedding implementations.

### Strengths
- The expansion of RoPE to images is presented clearly and makes intuitive sense
- The paper does a great job of motivating and describing the CUDA implementation.
- It is deeply appreciated that they go deeper and explore multiple different Rotary Positional Embeddings and report the comparisons

### Weaknesses
 - While a lot of small improvements are introduced in the method (3.3.2) the support or estimation of impact is somewhat lacking in the results.
- While the impact of k is detailed and appreciated, the measurement of performance is limited to accuracy and makes it hard to understand the gains or sacrifices associated with the implementations.
- The paper claims "noteworthy gains" across models, however the gains in Table 2 seem relatively limited (0.1-0.2) in most cases.
- Limited novelty, while the expansion of RoPE makes sense, the novelty both in terms of method and results might be limited.

### Questions
- Could you expand on the justification for RoPE's superior performance compared to RPB, beyond the intuitive explanations provided?
- Would the gains in efficiency scale to larger model size and resolution combinations?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the use of Rotary Position Embeddings (RoPE) in vision transformer models and provides an analysis of the differences between Relative Positional Biases (RPE) and RoPE through empirical experiments. Additionally, it proposes a fused CUDA-based implementation to improve inference speed. The paper also presents various design choices for RoPE, supported by experimental results.

### Strengths
- The paper is well-written and easy to follow. The figures demonstrate the ideas clearly.

### Weaknesses
 - **Unclear Contribution:** The novelty of the paper is uncertain, as RoPE has been previously applied to vision transformers. Notably, Heo et al. (2024) and Chu et al. (2024) have already explored RoPE in this context, with 2D RoPE in particular resembling Heo et al.'s work. Further discussion is needed to clarify the differences between the current approach and previous implementations. A comparison in the experimental section is also recommended. Additionally, the authors should consider reorganizing the contribution sections, as the first two contributions appear unconvincing.

- **Inconclusive Results:** The paper lacks a definitive conclusion regarding the performance of 2D RoPE versus Axial RoPE. For instance, Table 4 shows that 2D RoPE outperforms Axial RoPE, warranting further discussion. The lack of a clear performance winner makes it difficult to assess the practical value of each approach. The paper should provide a more in-depth analysis of the trade-offs between these two methods, considering factors such as computational cost, memory usage, and performance across different model architectures.

- **Limited Generalization Testing:** The paper does not assess the generalization ability of Axial RoPE across downstream tasks (e.g., detection and segmentation). Additional experiments to showcase RoPE’s generalization potential are recommended. The current evaluation is limited to image classification, which may not fully capture the benefits or limitations of the proposed positional encoding methods. Testing on more complex tasks would provide a more robust evaluation.

### Questions
- In comparing Table 4 and Table 5, the shared angles consistently outperform the non-shared angles. Why, then, did the authors choose to use non-shared angles in Axial RoPE?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes Rotary Postional Embeddings as a replacement for relative positional bias in transformers. They shows that it is leads to better accuracy and faster implementation. The paper tries to tackle the issue of latency when RPB is used with modern attention implementations such as flash attention.

### Strengths
Instead of applying RPB which slows down the attention computation in flash attention modules, the paper devices a way to add positional embeddings before attention is computed.
Since RoPE implementation is not dependent on which attention module is used, it can be integrated with any of the modern fast modern attention implementation unlike RPB.
Developed an efficient CUDA implementation for RoPE with an easy-to-use Python wrapper.
Found that applying RoPE to a fraction of embedding is enough.

### Weaknesses
The fact that RoPE will improve performance in ViT is not a novel idea and has already been shown in 
P. Jeevan and A. Sethi, "Resource-efficient Hybrid X-formers for Vision," 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), Waikoloa, HI, USA, 2022, pp. 3555-3563, doi: 10.1109/WACV51458.2022.00361. This paper has not been cited.
The scope of this paper is limited to cases when fused attention kernel is used. When RPB is introduced in this case, it hampers the fast attention compute. 
Most of the paper is just a review of postional embeddings and biases. 
Table 3 shows best performance when there is no bias introduced. The paper does not explain why this is so and also why even RoPE is needed then.
The ablations and experiments needs to more elaborated.

### Questions
Explain in detail the actual contributions of this paper and what novel ideas where brought in?
Is Axial RoPE your contribution or has it been taken from another paper and you just did a lot of analysis on it?
Why do we even need RoPE if no bias gives best results?

### Soundness
4

### Presentation
4

### Contribution
2
