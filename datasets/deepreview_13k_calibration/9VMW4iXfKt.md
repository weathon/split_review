# R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Large Language Models (LLMs), while demonstrating remarkable capabilities across various applications, present significant challenges during inference due to their substantial model size, especially when deployed on edge devices. Activation sparsity offers a promising solution to reduce computation and memory movement, enabling more efficient inference, particularly for small-batch on-device applications. However, current approaches face limitations with non-ReLU activation function, which are foundational to most advanced LLMs, or require heavy continual training. Additionally, the difficulty in predicting active channels and limited achievable sparsity ratios constrain the effectiveness of activation sparsity-based methods. In this paper, we introduce R-Sparse, a training-free activation sparsity approach capable of achieving high sparsity levels in advanced LLMs. We conducted two preliminary investigations into how different components contribute to the output within a single linear layer and found two key observations: (i) the non-sparse components of the input function can be regarded as a few bias terms, and (ii) The full computation can be effectively approximated by an appropriate combination of input channels and weight singular values. Building on this, we replace the linear layers in LLMs with a rank-aware sparse inference method that leverages the sparsity of input channels and singular value components, eliminating the need for active channel prediction like the output sparsity based approaches. Experiments on Llama-2/3 and Mistral models across ten diverse tasks demonstrate that R-Sparse achieves comparable performance at 50\% model-level sparsity, resulting in a significant 43\% end-to-end efficient improvements with customized kernels. Code will be made publicly available upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents R-Sparse, a training-free activation sparsity approach for large language models (LLMs). Current activation sparsity methods face limitations with non-ReLU activation functions and have difficulties in predicting active channels and achieving high sparsity ratios. R-Sparse overcomes these challenges by leveraging the sparsity of input channels and singular value components. The authors conduct investigations and find that non-sparse components can be regarded as bias terms and full computation can be approximated by a combination of input channels and weight singular values. R-Sparse is applied to both attention and MLP modules of LLMs and an evolutionary search algorithm is used to find optimal sparse component ratios. Experiments on Llama-2/3 and Mistral models across ten tasks show that R-Sparse achieves 50% model-level sparsity with comparable performance and up to 43% end-to-end speed improvement with a customized kernel.

### Strengths
* The training-free method does not require extensive pre-training, making it more efficient and easier to implement compared to methods that need continual training.
* R-Sparse achieves high sparsity levels (50% model-level sparsity) without sacrificing performance, leading to significant improvements in efficiency.
* R-Sparse is compatible with weight quantization for further efficiency gains and can be applied to different LLM families and a variety of tasks.

### Weaknesses
 * Table 1 is difficult to interpret. From the description of the authors, R-Sparse40% is compared with CATS22% and GRIFFIN33%, if my understanding is correct. Therefore, R-Sparse does not consistently outperform CATS across all tasks (e.g., PIQA 78.24 vs 79.00). The authors are suggested to refine the claim to avoid the misleading. Meanwhile, for certain cases, the performance increases with an even higher sparsity ratio (e.g., 79.49 vs 79.92 for R-Sparse40% and R-Sparse50%) on PIQA. Could the authors provide some insights into this phenomenon?
* The sensitivity analysis of hyperparameters should be added for a more thorough investigation of the effectiveness of R-Sparse.
* As [1] is discussed by the authors in the related works, why do the authors choose not to compare with [1] in the experiments?
* The authors are suggested to include the complexity analysis and running time comparison of R-Sparse, especially regarding the evolutionary search algorithm.
* The writing can be further improved. For example, the optimal sparse-rank $\alpha$ is not formally defined. From Algorithm 1, $\alpha$ seems to be fixed, how is it optimized?

### Questions
Please kindly refer to the Weaknesses.

### Soundness
3

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
2

### Summary
This paper uses the inherent sparsity and low-rank properties of input activations in LLMs to accelerate the inference of LLMs. It sparsifies the input activations to remove unnecessary activations, and interprets unnecessary activations as a bias term, using SVD to compensate for this bias. The proposed method achieves higher sparsity than the baseline while maintaining overall performance.

### Strengths
- This paper proposes a training-free activation sparsification method to speed up LLM inference. The proposed method can maintain performance at the same level as full parameters at sparsity of about 50%.
- This paper proposes to design different sparsity ratios for different layers to improve overall performance.
- This paper is very clearly written and the proposed method is easy to follow.

### Weaknesses
 - The analysis of "the contribution of each input channel and singular value component" in this paper is mainly focused on the C4 dataset (Figures 1 and 3). What are the similarities and differences between the analysis on other datasets and the C4 dataset? Especially on datasets that are very different from the C4 dataset. In addition, these analyses are mainly based on 16 randomly sampled training samples. When the number of samples increases or decreases, what changes will occur in the analysis results? It is crucial to understand if the observed patterns generalize across diverse data distributions and sample sizes, as this directly impacts the robustness of the proposed method.
- As shown in Figure 3, there is a clear difference in the importance of different linear layers (such as self_attn.k_proj vs. self_attn.up_proj), what this mainly stems from, the authors can give more comments on this. The underlying reasons for these variations in importance across different layers should be explored further. Specifically, how do the architectural differences and functional roles of these layers influence the observed sparsity patterns? A deeper analysis could reveal insights into the specific types of computations that benefit most from the proposed sparsification technique.
- What is the relationship between the sparsity ratio in the proposed R-Sparse and the final inference acceleration? For example, what is the corresponding acceleration for a certain sparsity ratio? The paper should provide a more detailed analysis of the practical speedup achieved with different sparsity levels, considering factors such as memory access patterns and computational overhead. This would help in understanding the trade-offs between sparsity and actual performance gains.
- In Figure 6, why under Dense, when the Generation Length becomes longer (1024->2048), the generation speed slows down, while when it is 128->256->512, the generation speed is accelerated. This behavior is counterintuitive and requires a more thorough explanation. The authors should analyze the different components of the inference process, such as prefilling, weight computation, and KV cache access, to pinpoint the factors that contribute to this non-monotonic trend in generation speed.

### Questions
See the Weaknesses section

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a novel training-free activation sparsity method called R-sparse. This method is applicable to non-ReLU-based large language models (LLMs) and eliminates the need for prediction by utilizing input activation sparsity. Furthermore, it is a method that can be applied not only to MLP modules but also to attention modules.

### Strengths
- The authors successfully identified existing challenges and, in connection to these, suggested a training-free, prediction-free activation sparsity method. Furthermore, their method is applicable to attention modules.
- Through various experiments, they demonstrated performance improvements.

### Weaknesses
 - difficult to read (clearity)
  - In introduction, how should Figure 1 be interpreted? It is difficult to understand the meaning of the figure until reviewing the explanation in Section 3.3.
  - In Section 3.2, what does the term "bias" mean? Is it interpreted as "bias" in the sense that performance is maintained even after replacing non-sparse values smaller than 0 with a constant? Does the term also include non-sparse components greater than 0? In Lines 183-185, why is it defined as "sparse", when $H_k \geq T_0$?

- the appropriateness of the title.
  - The proposed method appears to be "activation sparsity, then low-rank decomposition for non-important activations" rather than using both approaches simultaneously (rank-aware activation sparsity).


==== After Rebuttal ====
- I understand. However, the terms in Section 3.2 should be clarified more explicitly.
- It might be beneficial to add an explanation using examples, when $T_0 = 0$.
  - positive = sparse components = not pruned values
  - negative = non-sparse components = to be pruned values
- In fact, the most confusing term is "sparse components." It would be beneficial to clearly indicate, as suggested in the response, that it originates from prior research.

**[Q2 and Q6]**
- The authors said that "the sparsity is defined as the ratios of $x < T_{0}$", in Q6.
  - However, within this range, $x$ actually takes on the nearest discrete value rather than 0 in order to maintain the original functionality. Is it correct to define this as "sparsity"?
  - As requested in the original question, please provide an example to explain the situation. I understand the case where the minimum of $x$'s input is -2.
- Futhermore, the authors said that "all the **non-sparse** components where $H_{k} < T_{0}$", in Q2.
  - Is not this expression contradictory to the definition provided above?

### Questions
- (Writing) Please switch the positions between mlp.up_proj and mlp.gate_proj of layer 0 in Figure 3.
- Recommended reference
  - Alizadeh, Keivan, et al. "Llm in a flash: Efficient large language model inference with limited memory."
- Definition of multi-phase ReLU.
  - Is the multi-phase ReLU expressed on line 170 correctly defined? Where is sparsity defined? Shouldn't there be a definition for when x $< T_{L}$? Moreover, the output should get closer to zero as it becomes more negative, but it is defined in the opposite direction.
  - For instance, $T_0 = 0, T_1=-1, T_2=-2$, please explain it.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a rank-aware activation sparsity, including applying input sparsification and weight decomposition. Experiments show that the proposed R-Sparse improves end-to-end efficiency while maintaining comparable sparsity.

### Strengths
1. The proposed methods are easy to understand.
2. The experimental results are good.

### Weaknesses
1. The connections between motivations and the proposed methods are weak. For example, the first motivation claims that the outputs for the non-sparse inputs can be regarded as biases. However, it is not sure which part of the proposed methods is motivated by this. Please explicitly explain how the observation about non-sparse inputs being treated as biases directly informs specific components of their R-Sparse method.

2. The contributions are incremental, which only directly apply existing techniques, such as CATS for sparsity, SVD for weight decomposition, and genetic algorithm for hyperparameters searching. Please more clearly articulate the novelty of your approach. Is there any specific design in SVD?

3. The paper claims that existing non-ReLU activations such as SiLU and GELU introduce less sparsity. However, the experiments lack generality as Llama 2/3 and Mistral all adopt SiLU as activation functions. For example, adding results of models using GELU activation functions such as Gemma would be helpful.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
2
