# FlashDP: Memory-Efficient and High-Throughput DP-SGD Training for Large Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
As large language models (LLMs) increasingly underpin technological advancements, the privacy of their training data emerges as a critical concern. Differential Privacy (DP) serves as a rigorous mechanism to protect this data, yet its integration via Differentially Private Stochastic Gradient Descent (DP-SGD) introduces substantial challenges, primarily due to the complexities of per-sample gradient clipping. Current explicit methods, such as Opacus, necessitate extensive storage for per-sample gradients, significantly inflating memory requirements. Conversely, implicit methods like GhostClip reduce storage needs by recalculating gradients multiple times, which leads to inefficiencies due to redundant computations. This paper introduces FlashDP, an innovative cache-friendly method that consolidates necessary operations into a single task, calculating gradients only once in a fused manner. This approach not only diminishes memory movement by up to $\textbf{50}$% but also cuts down redundant computations by $\textbf{20}$%, compared to previous methods. Consequently, FlashDP does not increase memory demands and achieves a $\textbf{90}$% throughput compared to the Non-DP method on a four-A100 system during the pre-training of the Llama-13B model, while maintaining parity with standard DP-SGD in terms of precision. These advancements establish FlashDP as a pivotal development for efficient and privacy-preserving training of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies engineering approaches used to accelerate deep learning and improve the performance of DP-SGD. DP-SGD, the most widely used algorithm for training differentially private machine learning models, is known to cause performance degradation. Specifically, due to the need to clip gradients, initial implementations faced a large memory footprint because of the need to store per-sample gradients. Recent advances have almost solved this problem. A recent method called Ghost clipping eliminates the need to instantiate per-sample gradients, instead instantiating only per-sample norms. However, the throughput of this method is still far from that of non-private training. This paper attempts to resolve this gap by introducing FlashDP, which uses advanced caching techniques and performs gradient norm calculation and gradient calculation in a single task. This eliminates redundant calculations (by 20%, as claimed by the authors) of the activation gradient and improves throughput compared to Ghost clipping. FlashDP achieves a 90% throughput compared to the Non-DP method on a four-A100 system during the pre-training of the Llama-13B model.

### Strengths
- Improving the performance of DP-SGD is important for adoption of DP in machine learning community

- Matching the throughput and memory footprint of non-private training is impressive

### Weaknesses
 - Not much novelty, most techniques seem to be standard engineering techniques to accelerate deep learning

 - Figure 1 isn’t informative, how does eliminating the buffer help the throughput?

- What is subscript T in line 7 of algorithm 1?

- How do you exactly match the performance of DP-SGD? The added noise and sub-sampling creates a variance in the final model but that doesn't show in table 2.

- How do you perform poisson sub-sampling? In my experience, poisson sub-sampling itself can make training slower even without gradient clipping. 

- When you fix batch-size, does it mean that you are using sub-sampling rates that lead to that batch-size in expectation?

### Questions
- Figure 1 isn’t informative, how does eliminating the buffer help the throughput?

- What is subscript T in line 7 of algorithm 1?

- How do you exactly match the performance of DP-SGD? The added noise and sub-sampling creates a variance in the final model but that doesn't show in table 2.

- How do you perform poisson sub-sampling? In my experience, poisson sub-sampling itself can make training slower even without gradient clipping. 

- When you fix batch-size, does it mean that you are using sub-sampling rates that lead to that batch-size in expectation?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose FlashDP — an algorithm for efficient gradient computation in DP-SGD training. It is based on Hierarchical Reduction Architecture, which implements a multistage scheme, beginning with intra-block All-Reduce and then proceeding to inter-block reductions. To implement this block-wise All-Reduce, the authors used an adaptive kernel approach. The proposed method was empirically evaluated for both speed and memory efficiency using GPT-2, TinyLLaMA, and LLaMA models.

### Strengths
1. The differential private pre-training of large language models represents a significant research challenge, and this paper makes a valuable contribution toward advancing this direction.

2. The authors conducted comprehensive experimental evaluations, comparing their method against both non-private baselines and alternative DP-SGD implementations in different experimental setups.

### Weaknesses
Major weaknesses:

1. The main limitation of this work is the absence of complete implementation for the proposed algorithm (let alone the code for experiment reproduction) or at least detailed pseudocode. The description provided in Algorithm 1 is insufficient as it remains too high-level - for instance, it lacks crucial implementation details of the Block-wise All-Reduce operation, which, as the authors themselves acknowledge (line 356), represents a key technical challenge. For engineering-focused papers presenting complex algorithmic implementations, I consider the availability of source code to be essential, making this limitation particularly **crucial**.

2. A fundamental challenge in DP-SGD implementation, as I understand it, stems from the requirement to compute **the full gradient norm across all layers** for per-example clipping (for example, this issue is thoroughly discussed in Section 4 of the prior work [1]). This requirement has led previous algorithms to either compute gradients twice (first to calculate the gradient norm across all layers) or store gradients for all layers in a buffer (to enable clipping without recomputation once the total norm is determined). However, the current work notably lacks any discussion of this crucial aspect (the substring "layer" appears only in the supplementary material and in different contexts). Without addressing this fundamental consideration, it becomes challenging to understand how the proposed implementation achieves compliance with the DP-SGD algorithm while avoiding additional gradient recomputation and memory overhead.

Minor weaknesses:

1. The authors omitted the GhostClip method from Figure 4 and both GhostClip and BK methods from Figure 5, without providing any justification for these omissions. This appears particularly problematic given that these methods were substantially more competitive with FlashDP than the retained Opacus baseline (according to Table 3, GhostClip even outperformed FlashDP in terms of memory usage).

2. Lines 8-10 of the Algorithm 1 describe an All-Reduce operation between blocks for gradient norm computation. Such an All-Reduce operation necessitates the presence of multiple blocks that have computed values to reduce. However, according to the pseudocode in Algorithm 1, all *for* loops are executed sequentially. The authors should provide clarification regarding this algorithmic detail.

3. Since the official LLaMA release did not include a 3B-sized model, I assume that the authors used a custom LLaMA-like model with 3B parameters. If so, the authors should clearly state this and provide a complete description of this model's architecture.

### Questions
See Weaknesses.

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
1

### Summary
The vanilla DP-SGD has the memory and computational efficiency issue. Later-on methods try to improve this efficiency but still has additional cost in computations to save memory compared with non-private SGD. This paper proposes a method that encodes the per-sample clipping in the backward process. As evaluated in the experiment, when training with large language models, the proposed method matches the memory efficiency of  the non-private SGD and perform the best in terms of throughput compared with all implementations of DP-SGD.

### Strengths
1. The problem studied by this paper is important. The memory and computational cost introduced by DP-SGD is the bottleneck for applying it to large foundation models nowadays.
2. The empirical results on large language model look promising. The proposed method has a certain benefit over existing method: same memory cost as non-private SGD and 70-80% speed of non-private SGD.

### Weaknesses
 1. The intuition and the benefit of the proposed method are not straightforward to me, although it can be because I am not familiar with the low-level design in the GPU and CUDA (my confidence is 1). It seems that in the algorithm, per-sample gradients for all weights still need to be saved at the same time, before the block-wise synchronization block. Opacus also explicitly save per-sample gradients. Why is the proposed method more memory-efficient than Opacus?
2. The details of the proposed method are not clear to me. Does the Algorithm 1 only describe the MLP layer? What is the details of other computations in the transformer?
3. Some definitions are not well-introduced in the main paper; for example the abbreviation GEMM and HBM are directly mentioned in main paper without the full short phrase. Again, it is likely because i am not familiar with the area, but it would be better to have more description so the audience can be wider.


### Questions
Please check the weakness section. Moreover,
1. Can the proposed method be applied to other architecture such as convolutional neural network in computer vision?
2. Is it possible that the method can be implemented as a package s.t. it can be easily used for other variants of transformer?
3. What's the reason that the memory usage of ghostclip is even more efficient than NonDP?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper considers the problem of efficiently computing per-sample clipped gradients in DP training. Clipping causes DP training to be more expensive than non-private training because e.g. computing batch gradients might be more efficient than computing single gradients and averaging them, or because we might need to reload parts of the gradient into memory to rescale them. The authors propose FlashDP, which uses implicit fusion of a wider number of steps of the DP batch gradient computation than past work. e.g. compared to the popular GhostClip, which recomputes per-sample gradients after computing the clip norm, FlashDP combines the gradient computation / norm computation / rescaling operation into a single pass. The authors conduct experiments to demonstrate the improvements of FlashDP over past work. Their experiments show e.g. higher gradient throughput than the Opacus library's standard clipping operation while using less memory, and also much higher throughput than GhostClip while using slightly more memory.

### Strengths
The main strength is the empirical comparisons which are quite favorable - it seems based on the results in this paper that most PyTorch users who are training with DP would want to use FlashDP if it were made widely available. Beyond that, a lot of care is taken in the presentation, e.g. there are plenty of nice figures, comparisons to past works are broken down carefully, the main hardware algorithm is broken down line-by-line, and the paper includes explanations for DP experts who might not be as familiar with e.g. transformer architecture or hardware details of GPU training. The technical contributions also seem pretty significant - the question of how to do clipping while computing gradients in a blockwise manner is highly nontrivial, since a priori it seems one needs to do a 'multi-pass' algorithm to learn the norm before clipping.

### Weaknesses
I think the paper has limited weakness, with the main potential weakness being that the empirical comparisons to past methods seem to consider only PyTorch implementations. However, even e.g. the original Opacus paper shows (in e.g. Appendix E of https://arxiv.org/pdf/2109.12298) that e.g. JAX implementations of DP-SGD may be more scalable than Opacus (e.g. in their figure 4.d, JAX pays a large up-front compilation cost, its per-iteration runtime is much smaller than Opacus). It would be interesting to understand how FlashDP compares to JAX DP-SGD implementations / if the techniques in FlashDP are restricted to training with PyTorch. However, since PyTorch is quite popular for both private and non-private training, and it would likely be a large amount of work to ask the authors to investigate this, I think this weakness is limited. Anyway, the comparison of FlashDP to non-private PyTorch training is quite favorable and suggests FlashDP compares favorably to non-PyTorch methods as well.

### Questions
Are the losses in Table 2 exactly the same? i.e., does this table show that the input -> output function computed by FlashDP and other implementations are exactly the same given the same noise, or are there possibly some differences in later digits (e.g. due to slight algorithmic differences or numerical stability issues) that the authors view as insignificant compared to the efficiency benefits?

### Soundness
3

### Presentation
4

### Contribution
4
