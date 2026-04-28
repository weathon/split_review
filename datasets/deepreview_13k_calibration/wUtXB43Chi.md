# FlashMask: Efficient and Rich Mask Extension of FlashAttention

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
The computational and memory demands of vanilla attention scale quadratically with the sequence length $N$, posing significant challenges for processing long sequences in Transformer models. FlashAttention alleviates these challenges by eliminating the $\mathcal{O}(N^2)$ memory dependency and reducing attention latency through IO-aware memory optimizations. However, its native support for certain attention mask types is limited, and it does not inherently accommodate more complex masking requirements. Previous approaches resort to using dense masks with $\mathcal{O}(N^2)$ memory complexity, leading to inefficiencies. In this paper, we propose \ours{}, an extension of FlashAttention that introduces a column-wise sparse representation of attention masks. This approach efficiently represents a wide range of mask types and facilitates the development of optimized kernel implementations. By adopting this novel representation, \ours{} achieves linear memory complexity $\mathcal{O}(N)$, making it suitable for modeling long-context sequences. Moreover, this representation enables kernel optimizations that eliminate unnecessary computations by leveraging sparsity in the attention mask, without sacrificing computational accuracy, resulting in higher computational efficiency. We evaluate \ours{}'s performance in fine-tuning and alignment training of LLMs such as SFT, LoRA, DPO, and RM. \ours{} achieves significant throughput improvements, with end-to-end speedups ranging from 1.65x to 3.22x compared to existing FlashAttention dense method. Additionally, our kernel-level comparisons demonstrate that \ours{} surpasses the latest counterpart, FlexAttention, by 12.1\% to 60.7\% in terms of kernel TFLOPs/s, achieving 37.8\% to 62.3\% of the theoretical maximum FLOPs/s on the A100 GPU.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel compression scheme for the attention mask where only the boundary indices of the masks are stored for every column. For a specific set of attention masks, it is sufficient to store two sets of boundary indices for every column to represent the attention mask. This reduces the memory complexity of attention masks from quadratic on sequence length to linear on sequence length, enabling handling of longer context lengths. The column-wise sparse representation is also used to skip fully masked blocks increasing the overall compute efficiency of the attention mechanism. This technique is augmented with FlashAttention algorithm for efficient computation of the attention mechanism and the modified algorithm for both forward pass and backward pass are presented. The experiments section shows that FlashMask is faster than FlashAttention dense method by up to 3.22x and can achieve up to 60.23% more throughput than FlexAttention. The proposed method also doesn’t alter the convergence during training.

### Strengths
The paper is well-written and easy to understand. The results section is elaborate with a wide range of benchmarks to demonstrate the advantages of the proposed methods. The appendix section and the analysis with synthetic data to corroborate the claims are very insightful. The compute and memory utilization advantages of FlashMask are well demonstrated. The proposed sparse representation scheme is novel and should be adopted wherever applicable for its memory efficiency and ability to support longer context lengths.

### Weaknesses
While the results section shows that FlashMask achieves higher computational efficiency, I’m not sure if it’s attributable to the proposed columns-wise sparse representation.
The computational efficiency of FlashMask comes from skipping computation on entirely masked blocks as discussed in section 4.3. However, this technique is also used in Block-Sparse FlashAttention and FlexAttention. The advantages of FlashMask over Block-Sparse FlashAttention and FlexAttention in terms of computational efficiency is not clear. Specifically, the paper doesn't provide a detailed breakdown of where the performance gains are coming from, making it difficult to isolate the impact of the column-wise sparse representation versus the block skipping optimization. It's also unclear if the performance gains are consistent across different hardware architectures or mask densities. 
Also as mentioned in the paper, the idea of column-wise sparse representation used in FlashMask is limited to specific attention patterns. Any other pattern can’t be handled even naively. This severely restricts the applicability of the proposed method in real-world scenarios where attention patterns can be more complex and less structured. The paper should also discuss the overhead associated with maintaining the boundary indices, which could become significant for very long sequences or very sparse masks.

### Questions
You mentioned FlexAttention can also exploit sparsity by skipping computation on fully masked blocks. If that’s the case where’s compute throughput advantage of FlashMask coming from?
Would the Block-Sparse FlashAttention be able to handle the mask types described in Fig 1(a)? If yes, that should be used instead of the DenseMask variant for the throughput comparisons across the paper. If not, please mention why.
In Fig 4b, why is the FlexAttention’s memory utilization lower than that of FlashMask for sequence length lower than 16K?

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
5

### Summary
The paper proposes an efficient sparse mask representation by using composition of LT and RT range for expressing complex patterns. The proposed mask is compatible with FlashAttention-2 and can bring speed-up when applied.

### Strengths
1. The paper open-sourced a rather general sparse self-attention representation framework, which could facilitate many research and production attempts in the field.
2. The implementation is practical, shown wall-clock speed-up over FlashAttention-2.

### Weaknesses
1. It seems the implementation is limited to Paddle. It would be good to see if it can also be made more general so that the Torch/Megatron community can also leverage the framework.
2. Inference support is missing. It would make more sense to discuss how such sparse mask can be put into actual inference/serving. 
3. [1] was published earlier, and also provide a general sparse self-attention training & serving framework. It would be ideal to also cite [1].

### Questions
1. What would be the block size supported by Flashmask? Namely, what would be the granularity of mask/unmask chunks?
2. How does different block/chunk size affect the speed-up, in different mask types?
3. When tiling, it seems some mask may lead to different workload among thread blocks, which could hurt the overall performance. Is there any mitigation to this?
4. Can we have a comparison between the theoretical FLOPs reduction wrt wall-clock speed-up for different mask types?
5. How does tensor parallel and pipeline parallel affect the speed-up?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces an extension for SDPA that supports different types of masks in an easy-to-understand way. The method is novel due to its sparse representation. Experiments show FlashMask outperforms FlexAttention by a significant gap.

### Strengths
Although this representation might be similar to COO/CSR/CSC, this is the first time I have ever seen these techniques used in attention, one of the most important operators in LLMs.

### Weaknesses
This paper lacks two baselines:
1.  Flashinfer with dense masks;
2.  Flashinfer sparse mask (https://docs.flashinfer.ai/api/python/sparse.html);

Although Flashinfer does not support backward, I believe it is an important baseline for SOTA attention implementation. If this comparison is presented, I will raise my score.

### Questions
1. How can this technique be integrated with page attention?
2. Can tree-based speculative decoding benefit from this customized attention?
3. Can you report evaluation results on machines such as P100, V100, A10G, and H100? (other than A100)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The article presents Flash Mask - a method to incorporate a wide class of attention masks into flash attention. Algorithmically, this means that the  non trivial structuring of the mask is incorporated into the online calculation of the softmax operation involved in self attention without materializing the full mask and paying quadratic in sequence length memory. Furthermore, this algorithm is implemented in a hardware aware fashion, much like flash attention to minimize memory access and data movement while exploiting the thread group level parallelism in GPUs. Empirically, this method is benchmarked against the dense mask of flash attention 2 and also against flex attention - an alternative state of the art method to incorporate structured masks in efficient attention computations and the method presented shows noticeable gains both in inference and in training.

### Strengths
The strengths of this paper are in the novelty of the incorporation of a class of structured masks into the online softmax calculation involved in memory efficient attention and further into the hardware aware version of the algorithm which is flash attention, and in the  comprehensive validation of the superior efficiency of the algorithm when benchmarked against dense masking in conventional flash attention 2 and in flex attention. 
The algorithm for the forward and backward pass are presented clearly and the empirical results are presented clearly.

### Weaknesses
As admitted by the authors, this method cannot handle irregular masking patterns within a column of the mask, or completely arbitrary masking patterns.

### Questions
Following up on the limitations, I would like the know whether the authors think that arbitrary masking patterns can be incorporated in a GPU friendly manner or if memory efficient implementations of such masking patterns would require alternative hardware architectures (such as those developed by Cerebras).

### Soundness
3

### Presentation
3

### Contribution
3
