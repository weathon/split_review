# Structured Mixture-of-Experts LLMs Compression  via Singular Value Decomposition

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6

## Abstract
Mixture of Experts (MoE) architecture has emerged as a powerful paradigm in the development of Large Language Models (LLMs), offering superior scaling capabilities and reduced computational costs. However, the increased parameter budgets and memory overhead associated with MoE LLMs pose significant challenges to their efficiency and widespread deployment. In this paper, we present MoE-SVD, the first decomposition-based compression framework tailored for MoE LLMs without any extra training. By harnessing the power of Singular Value Decomposition (SVD), MoE-SVD addresses the critical issues of decomposition collapse and matrix redundancy in MoE architectures.   Specifically, we first decompose experts into compact low-rank matrices, resulting in accelerated inference and memory optimization. In particular, we propose selective decomposition strategy by measuring sensitivity metrics based on weight singular values and activation statistics to automatically identify decomposable expert layers. Then, we share a single V-matrix across all experts and employ a top-k selection for U-matrices. This low-rank matrix sharing and trimming scheme allows for significant parameter reduction while preserving diversity among experts.  Comprehensive experiments conducted on Mixtral-8×7B|22B, Phi-3.5-MoE and DeepSeekMoE across multiple datasets reveal that MoE-SVD consistently outperforms existing compression methods in terms of performance-efficiency tradeoffs. Notably, we achieve a remarkable 60\% compression ratio on Mixtral-7x8B and Phi-3.5-MoE, resulting in a 1.5$\times$ inference acceleration with minimal performance degradation. Codes are available in the supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces MoE-SVD, a novel framework leveraging SVD for compressing Mixture-of-Experts architectures in large language models. MoE-SVD addresses key challenges of decomposition collapse and parameter redundancy in MoE models, utilizing techniques such as selective decomposition, matrix sharing, and matrix trimming. Experiments conducted on Mixtral-8x7B, Phi-3.5-MoE, and DeepSeekMoE demonstrate its ability and inference acceleration. Further evaluations with LoRA fine-tuning and quantization suggest MoE-SVD’s adaptability across different MoE backbones.

### Strengths
- The paper thoroughly evaluates the proposed method across various MoE architectures, including Mixtral-8x7B, Phi-3.5-MoE, and DeepSeekMoE.
- Additional experiments with LoRA fine-tuning and quantization validate the efficacy of MoE-SVD.
- MoE-SVD introduces a unique method for MoE compression. The matrix-sharing techniques can be interesting.

### Weaknesses
 - The paper does not include comparisons with structured compression methods directly applicable to MoE models, such as those presented in [1, 2, 3]. Additionally, it overlooks methods that specifically target expert layer compression or simultaneously address both expert layer and expert number compression, as found in [4, 5, 6]. These comparisons are crucial for a comprehensive evaluation of MoE-SVD's performance.
- Key metrics such as model size reduction, TFLOPS, and runtime are missing. These metrics are critical for assessing the practical efficiency of the proposed method. While the paper mentions some speedup, a detailed breakdown of TFLOPS and model size at different compression ratios is needed for a thorough analysis.
-  MoE-SVD shows a notable decline in performance even with a 20% parameter reduction, indicating possible limitations in maintaining model quality during compression. Furthermore, the absence of significance testing for performance claims weakens the robustness of the results. It is unclear if the observed performance differences are statistically significant or due to random variations.
- The representation and decomposition process of the expert matrix is ambiguous. In the expert decomposition subsection, the paper describes the expert matrix as $\mathbb{R}^{m \times n}$, but experts are typically two- or three-layer neural networks. It is unclear whether the matrix is decomposed individually for each layer or concatenated before decomposition, and if so, how the concatenation is done. Clarifying these points is important for the reader's understanding. The paper should specify if SVD is applied to each weight matrix within the expert or to a combined matrix, and if combined, how the dimensions are handled.
- The calculation of the sensitivity score in the selective decomposition strategy lacks clarity. It is unclear how activations are computed, how the dataset for expert frequency calculation is chosen, and whether the frequency values obtained from one dataset can be generalized to others. Providing pseudo-code would enhance comprehensibility. The paper needs to detail the activation calculation process, including whether it uses the input or output of the expert layers, and how the dataset for frequency calculation is selected and its impact on the results.
- The reasoning behind sharing the V-matrix to maintain performance is insufficiently explained. Further elaboration on the properties that enable the effective shared use of this matrix would be beneficial. The paper should explain why the V-matrix can be shared across experts without significant performance degradation, and what properties of the V-matrix allow for this.
-  The rationale for each expert storing information from two other experts, as indicated in equation (8), requires clearer justification. Specifically, an explanation is needed on why each expert needs information from other experts and how this contributes to enhancing the model’s overall performance. Although the paper mentions diversity as a factor, it is unclear why simply combining the U-matrix suffices can work, especially in the context of zero-shot MoE-LLMs.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed MoE-SVD, which is a training-free decomposition-based compression framework. Specifically, they first decompose experts into low-rank matrices via SVD. In particular, they selectively decompose the expert layers based on sensitivity metrics. Then, they share a single V-matrix across all experts and use a top-k selection for U-matrices for parameter reduction.

### Strengths
1. This paper explores SVD-based methods for MoE LLMs and identifies key factors that degrade performance: certain layers are sensitive to decomposition, and activation patterns differ in MoE, revealing expert redundancy. 
2. the authors propose a selective decomposition strategy along with low-rank matrix sharing and trimming, which are well-justified approaches. 
3. Overall, the paper is clear and easy to follow.

### Weaknesses
1. In line 53, could you elaborate on "Hardware Dependency" in the context of semi-structured sparse methods?

2. In Eq. (4),  $r_i$ represents the rank, but I believe the matrix should be of full rank, so the purpose of using $r_i$ here is unclear. Additionally, what does $f_i$ represent? Is it related to sampling frequency?

3. Figure 4 is unclear to interpret. It appears that the green grid denotes the decomposed experts, but could you clarify what the compression ratios, also shown on the y-axis, represent? While the overall motivation, that the approach seeks to identify layers with varying decomposition sensitivity, is understandable, the details require further clarification.

4. For the experiments, including Qwen in the experiments could strengthen the results.

### Questions
Please clarify more on Section 3.2

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
This paper proposes a compression framework called MoE-SVD, which uses a low-rank matrix decomposition of experts and a selective decomposition strategy based on weight singular values and activation statistics to identify the factorable expert layer, while sharing the V-matrix and implementing top-k selection in the U-matrix to reduce the number of parameters while maintaining the diversity among experts. The experimental results show that MoE-SVD performs better than existing compression methods on multiple datasets in terms of performance and efficiency tradeoff.

### Strengths
1. The method seems technically sound and straightforward in principle.
2. Good written and easy to follow.

### Weaknesses
1. The accuracy degradation of the compressed model is too obvious. With a 20% compression ratio, the average accuracy is generally reduced by 5%-10%. Even with the LoRA fine-tuning, the compression model cannot be improved to lossless, which greatly limits the practicability of the method.
2. Once it comes to fine-tuning, the author needs to compare it with some fine-tuning compression methods, such as MC-SMoE [1], which also uses low-rank decomposition + sparse technique.
3. For matrix multiplication, Rank(AB) ≤ min(Rank(A), Rank(B)), which also means that for an MLP layer, the rank of its output y is often less than W and x. Maybe using AFM [2] instead of SVD here is better, i.e., perform SVD decomposition of MLP output y, and then merge UV into the MLP weight. According to paper [2], AFM seems to be consistently superior to SVD.
4. The authors only test the throughput in Mixtral-8x7B and Phi-3.5-MoE, lacking speed on DeepSeekMoE. This is a little strange, because some MoE LLMs (such as DeepSeekMoE and Qwen2-57B-A14B) have a very heavy share-expert, which is a key bottleneck in LLM inference. Can the author discuss the actual speed performance of MOE-SVD on this type of model?
5. For current LLM inference, to achieve higher throughput, tensor parallelism is generally adopted. However, low-rank decomposition will split one MLP layer into two layers, which may result in relatively large communication overhead when combined with tensor parallelism. At present, the throughput measurement has only been done on an H100 GPU. Can authors further discuss the tensor parallelism (like TP4) inference with  MoE-SVD in detail?

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
2
