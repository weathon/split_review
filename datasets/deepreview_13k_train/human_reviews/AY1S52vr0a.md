# Q-Mamba: Towards more efficient Mamba models via Post-Training Quantization

- Decision: Reject
- Scores: 8, 6, 3, 3

## Abstract
State Space Models (SSMs), such as Mamba, have recently demonstrated the potential to match or even surpass Transformers in language understanding tasks, making them a promising alternative for designing Large Language Models (LLMs). 
Concurrently, model quantization, especially Post-Training Quantization (PTQ), has been proven effective in reducing memory usage and inference latency in LLMs.
In this paper, we explore post-training quantization for Mamba (\textbf{Q-Mamba}) by turning both linear projections and state caches into low-bit integers for efficient inference. 
After a theoretical analysis of the causes of outliers in states, we propose \textbf{Decoupled Scale Quantization (DSQ)}, which mitigates outliers in both the state and channel dimensions by applying separate quantization scales.
To preserve the selective ability of quantized Mamba, we introduce \textbf{Efficient Selectivity Reconstruction (ESR)}, a block-wise reconstruction method that involves a novel quantization simulation scheme, enabling fast parallel scan algorithms with the non-linear quantization function.
We demonstrate the effectiveness of Q-Mamba across various quantization settings, model sizes, and both generation and zero-shot tasks. 
In particular, for Mamba2-2.7B with W8A8H4 quantization, Q-Mamba achieves a 50\% reduction in memory consumption with only a 2.13\% average accuracy degradation on zero-shot tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper explores post-training quantization (PTQ) for Mamba language models and introduces a new method called Q-Mamba. The authors identify that the bottlenecks in Mamba models arise from the large size of linear projections and state caches, which can be further optimized through model quantization. They observe that state caches contain outliers in both state and channel dimensions. Based on further analyses of this phenomenon, Q-Mamba proposes Decoupled Scale Quantization, utilizing independent scales for different dimensions. Additionally, Q-Mamba introduces a new quantization simulation approach called Efficient Selectivity Reconstruction to facilitate efficient layer-wise reconstruction using the original parallel scan algorithm. Experiments demonstrate the necessity of these methods for effective quantization of Mamba models, achieving W8A8H4 quantization for Mamba models for the first time. Experiments on memory consumption and latency are also presented.

### Strengths
1. The main contribution of this work is the first exploration of quantization for Mamba models. Mamba architecture has recently attracted significant attention in the research community, and this paper offers a fresh perspective on model compression. The authors identify that the bottlenecks in Mamba models stem from the large size of linear projections and state caches, highlighting the potential for further research in model compression for Mamba models.

2. Both the DSQ and ESR methods are well-motivated and specifically tailored for Mamba architectures. The DSQ method is based on the observation that states in SSMs contain outliers in both channel and state dimensions. After a theoretical analysis of this phenomenon, the paper proposes utilizing decoupled (independent) scales for these dimensions. This approach is compelling and demonstrates significant improvements compared to per-channel quantization. ESR is a novel quantization simulation method that approximates quantization noise in layer-wise reconstruction and is necessary when introducing quantization into the parallel scan algorithm. The authors also conduct empirical experiments to select fine-tuning parameters that enhance performance

3. Experiments demonstrate the effectiveness of these methods for quantization of Mamba models. Notably, this paper achieves W8A8H4 (8-bit linear projections and 4bit states) quantization for Mamba models for the first time. For example, Q-Mamba achieves a 50% reduction in memory consumption with only a 2.13% average accuracy degradation on zero-shot tasks for Mamba2-2.7B. Ablation studies also demonstrate the convenience of Q-Mamba, which requires only 128 samples and a few epochs. Experiments on memory consumption and latency are also presented.

4. This paper is clearly written, logically structured, and easy to understand.

### Weaknesses
1. The background section could be enhanced for clarity for readers who are not familiar with Mamba. It would be beneficial to include additional information about the differences between the Mamba-1 and Mamba-2 models.

2. Some ablation studies on hyperparameters, such as optimizer settings ( learning rate, and weight decay) should be provided to demonstrate the robustness of ESR. Specifically, the impact of these hyperparameters on the final quantized model performance should be analyzed, not just the intermediate reconstruction loss. The sensitivity of the method to different learning rates and weight decay values needs to be rigorously evaluated to ensure the reliability of the proposed approach.

3. Considering the need for fast deployment, the total time consumption for layer-wise construction should be included, particularly for the largest Mamba models. This should include a breakdown of the time spent on different stages of the ESR method, such as data loading, forward and backward passes, and parameter updates. Furthermore, the memory footprint during the layer-wise reconstruction process should also be reported, as this can be a limiting factor for large models.

### Questions
The appendix provides the results of the GPTQ[1] and SmoothQuant[2] methods on Mamba models. Could you provide more results for different quantization settings (e.g., W3A16, W4A4)? I am curious about the bit precision that can be achieved with Mamba model quantization.

[1] Xiao et al., SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models. ICML 2023.

[2] Frantar et al., OPTQ: Accurate Quantization for Generative Pre-trained Transformers. ICLR 2023.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces the first scheme for post-training quantization (PTQ) of Mamba models. In contrast to transformers, which are well studied in the context of PTQ, Mamba models have large state tensors that pose unique quantization challenges, as they can take a significant portion of memory, especially after quantizing weights.
They tackle this issue by focusing on the quantization of the states cache to low bits, down to 4 bits. They begin by examining the activation tensors and find that they have large outliers across both channel and state dimensions, making quantization difficult. They propose two methods to address this: 

1. Decoupled Scale Quantization (DSQ) that uses different scales and quantization schemes along the channel and state dimensions. This flattens outliers across both dimensions

2. Efficient Selective Reconstruction (ESG), which is a local fine-tuning technique for certain SSM parameters ($B$, $C$ and $\Delta$).  

By applying SmoothQuant to the rest of the linear layers of the network and ESG+DSQ to states the quantize the Mamba-2 models to W8A8H4. Specifically for Mamba2-2.7B they achieve 50% memory reduction with only 2.17% drop in accuracy degradation for zero-shot tasks

### Strengths
* The authors are the first to tackle the quantization of Mamba models and achieve impressive compression of the state tensors that can take a large proportion of memory. They also show the efficacy of their work by showing the memory reduction and latency improvement in Figure 6.

* The authors systematically study the state tensors and the presence of outliers to motivate Decoupled Scale Quantization with good visualization in Fig. 4 & Fig 8.

* The profiling of Mamba inference and memory requirements supported by figures (Fig, 2 & Fig. 8)

* An easy-to-read paper with good ablation studies

### Weaknesses
Unfortunately, the paper lacks innovation from a quantization perspective even if the application of PTQ is quite novel, recycling ideas that are already well established in existing quantization literature. I believe that this paper would make an excellent workshop paper but its contributions are not enough for an ICLR paper. In addition, there is a lot of crucial information missing to understand and reproduce both Decoupled Scale Quantization & Efficient Selective Reconstruction. 

## Decoupled Scale Quantization
According to the SMM equation in (1), the channels are independent from each other. I am not sure why then quantizing the values along the channel dimension would make any difference in the case of multiplication with $A$ & $C$. Per-state quantization of these matrices and of the states should lead to optimal quantization performance IF these matrix multiplications are in fact done in lower precision. Or the quantization scheme only for compression and matrix multiplications are done in higher precision. There are a lot of quantization details missing here that would explain the merits of the scheme.

## Efficient Selective Reconstruction
A lot of information missing here. Is this a local QAT scheme similar to OmniQuant for transformers? Are the learnt matrices just adjusted to the quantized states? Or they are also quantized using straight-through?

### Questions
* Many relevant references relate to LLM quantization in section 2.2, such as OPTQ, OmniQuant, OutlierSuppersion+, and etc.
* Figure 1: What exactly is learnable at block $N$ ? $\Delta$ is mentioned in the caption but is missing from the graph.
* Figure 2: is this the memory consumption during pre-fill or generation?
* Theorem 1 is very hard to follow. What does the split equation operator do? It’s never introduced. Where did the weight matrices ($W_x$ & $W_b$) come from? Please make this section more readable. 
* Figure 6, the legend hides the graph
* Figure 9, the caption does not explain what the different colours are.
* It would be very useful to add a graph of the Mamba block highlighting the final precision of each tensor and the precision of each compute. Look at Figure 6  of SmoothQuant.
## Section 5.2: 
  * you never introduce an equation of what block-wise reconstruction means. I understand from the references it is the $\ell_2$ loss between quantized and unquantized values but that's because I happen to know one of the cited papers well. 
 * What do you learn exactly? Where is the quantization? Do you use a straight-through estimator? Do you also learn the quantization scales?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces Q-Mamba, a post-training quantization (PTQ) approach aimed at improving the efficiency of Mamba models by converting linear projections and state caches into low-bit integers. The authors present two techniques: Decoupled Scale Quantization (DSQ), which addresses the outliers in both state and channel dimensions, and Efficient Selectivity Reconstruction (ESR) to preserve the model’s selectivity. They demonstrate Q-Mamba’s efficacy across various quantization settings and tasks, reporting a 50% reduction in memory with minimal accuracy degradation in some configurations.

### Strengths
1. **Relevance**: The paper addresses a key issue by optimizing Mamba’s memory and computational requirements, making it relevant to the field of efficient large language models (LLMs).

2. **Novel Quantization Scheme**: DSQ’s approach to outlier mitigation in both state and channel dimensions adds a unique element to quantization in SSMs.

3. **Practical Impac**: Q-MAMBA's claimed memory reduction is substantial, especially for real-world applications where memory efficiency is essential.

4. **Clarity in Methodology**: The authors provide a theoretical foundation for DSQ and clear motivation for ESR, contributing to understanding their method.

### Weaknesses
1- **Computation Overhead in Quantization**: The quantization and dequantization process requires computing an outer product of two vectors, which can be computationally expensive compared to other group quantization methods available in the field.

2- **Lack of Comprehensive Evaluation**: The experimental results lack sufficient diversity across tasks and model sizes. Evaluating Q-Mamba’s performance on additional Mamba family models would strengthen its claims of versatility.

3- **Limited Baseline Comparisons**: The paper could benefit from comparisons with related quantization methods like OmniQuant [1], OPTQ [2], AWQ [3], and Mamba-PTQ [4]. Assessing Q-Mamba against these methods would provide better insights into its performance, especially given that Mamba is composed largely of linear layers for which these quantization schemes have proven effective.

4- **Insufficient Analysis of Latency**: The paper does not sufficiently explore the impact of Q-Mamba on inference latency, which could be critical for real-world deployment. More timing results can enrich the experiments section further.

5- **Potential Misstep in DSQ Calculation**: In Equation 7, it appears that the mean of the absolute values of elements in $h$ should be used rather than the mean. If this is not an oversight, additional explanation would be valuable.

6- **Justification of ESR Design Choices**: ESR’s design choices, particularly which parameters are made learnable, lack sufficient exploration, and further analysis on this aspect would clarify ESR's effectiveness.

### Questions
1- **Comparison to Related Work**: How does Q-MAMBA compare to other quantization approaches such as Mamba-PTQ, OmniQuant, OPTQ, and AWQ in terms of performance and memory efficiency? The papers are cited in the weaknesses section.

2- **Impact on Latency**: What is Q-Mamba's effect on real-world latency, especially for larger batch sizes or latency-sensitive tasks? Additionally, what are the overheads of the outer products for the quantization and dequantizaiton of tensors?

3- **Scalability of DSQ**: Can DSQ be effectively scaled or applied to other architectures, or does it require specific adjustments for compatibility?

4- Clarification on DSQ Calculation: In Equation 7, should the mean of the absolute values of elements in $h$ be used instead of the mean? Further clarification on this point would be helpful.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors aim to investigate the unique challenges of quantizing state space models. Their investigation highlights the importance of outlier reduction, which motivates their proposal for fine-grained scaling factor selection (i.e., decoupled scale quantization) and block-wise reconstruction (i.e., efficient selectivity reconstruction).

### Strengths
The majority of quantization research on language models focus on the standard transformer architecture, namely Llama models, leaving state space models an under-explored model architecture within the space of post-training quantization. Given the importance of state space models, the topic is relevant and timely.

### Weaknesses
Outliers are a well-established challenge in neural network quantization, not just in language models but across neural architectures. It is unclear the unique challenges that SSMs pose over standard transformer architectures. While the authors claim this is the first paper to study SSM quantization, it is unclear where the unique challenges arise. Enough prior studies have investigated fine-grained scaling factors and block-wise reconstruction to warrant benchmarking against those techniques. Ultimately, it is unclear if existing techniques are already sufficient to solve the challenges the authors present. For example, many PTQ works have investigated groupwise quantization (e.g., GPTQ) to increase the granularity. This also establishes a grid of scaling factors similar to the decoupled scale quantization proposal. Finally, rotation-based quantization techniques have been studied in a handful of papers over the last year (e.g., QuIP, QuaRot, SpinQuant). There is no mention of any of these approaches in the paper, and it has been one of the most effective techniques to reducing outliers in language models.

It is unclear why BRECQ (or other existing block-wise reconstruction algorithms) can't be applied to SSMs. The analysis claims parallel training and layer selection are the challenges, but it is not clear if (or how) this is a restriction on the algorithm or some implementation of it. Can you please provide more detail?

The notation in Equation 1 confuses me. The matrix dimensions don't seem to line up. Should there be a transpose for $A_t h_{t-1}$ since $A_t$ is $N \times N$ and $h_{t -1}$ is $T \times N$? Also, I imagine $B_t x_t$ is an outer product and would also need to be transposed since $x_t$ is $T \times P$ and $B_t$ is $N \times 1$? If this understanding is correct, can you please explain where the $N \times P$ comes in?

### Questions
The notation in Equation 1 confuses me. The matrix dimensions don't seem to line up. Should there be a transpose for $A_t h_{t-1}$ since $A_t$ is $N \times N$ and $h_{t -1}$ is $T \times N$? Also, I imagine $B_t x_t$ is an outer product and would also need to be transposed since $x_t$ is $T \times P$ and $B_t$ is $N \times 1$? If this understanding is correct, can you please explain where the $N \times P$ comes in?

It is unclear why BRECQ (or other existing block-wise reconstruction algorithms) can't be applied to SSMs. The analysis claims parallel training and layer selection are the challenges, but it is not clear if (or how) this is a restriction on the algorithm or some implementation of it. Can you please provide more detail?

### Soundness
2

### Presentation
2

### Contribution
1
