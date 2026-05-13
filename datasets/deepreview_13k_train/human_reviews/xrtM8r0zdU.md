# Sparse Gradient Compression for Fine-Tuning Large Language Models

- Decision: Reject
- Scores: 5, 5, 5, 5, 5

## Abstract
Fine-tuning large language models (LLMs) for downstream tasks has become increasingly crucial due to their widespread use and the growing availability of open-source models. However, the high memory costs associated with fine-tuning remain a significant challenge, especially as models increase in size. To address this, parameter efficient fine-tuning (PEFT) methods have been proposed to minimize the number of parameters required for fine-tuning LLMs. However, these approaches often tie the number of optimizer states to dimensions of model parameters, limiting flexibility and control during fine-tuning. In this paper, we propose sparse gradient compression (SGC), a training regime designed to address these limitations. Our approach leverages inherent sparsity in gradients to compress optimizer states by projecting them onto a low-dimensonal subspace, with dimensionality independent of the original model's parameters. By enabling optimizer state updates in an arbitrary low-dimensional subspace, SGC offers a flexible tradeoff between memory efficiency and performance. We demonstrate through experiments that SGC can decrease memory usage in optimizer states more effectively than exising PEFT methods. Furthermore, by fine-tuning LLaMA models on various downstream tasks, we show that SGC can deliver superior performance while substantially lowering optimizer state memory requirements, particularly in both data-limited and memory-limited settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents a Sparse Gradient Compression (SGC) algorithm to flexibly and granularly control the number of trainable parameters during fine-tuning. By projecting the optimizer states into a subspace, SGC updates and stores these states in a low-dimensional space. Numerical experiments demonstrate that the performance of SGC is comparable to existing parameter-efficient fine-tuning (PEFT) algorithms to some extent.

### Strengths
1.The paper introduces two algorithms, MESGC and CESGC, for effectively reducing the memory and computational complexity, respectively.
2.It presents a well-reasoned approach for determining the hyperparameters of the SGC algorithm in Section 5.2.

### Weaknesses
1.The novelty of the proposed approach is limited. The concept of projecting optimizer states into a subspace with a dimension independent of the original model size has been previously discussed in the top-k compressor as shown in [1] and [2]. The paper fails to adequately distinguish its approach from these existing methods, particularly concerning the specific application to fine-tuning large language models (LLMs). While the authors use a random projection matrix, the core idea of reducing dimensionality before applying sparsification is not sufficiently novel.

2.The paper lacks a theoretical analysis of the relationship between the choice of k and the model’s convergence, a detail that has been explored in [1] and [2]. The absence of such analysis makes it difficult to understand the impact of the chosen subspace dimension on the convergence behavior of the proposed method. Specifically, it is unclear how the chunk size and sparsity parameters interact with the convergence rate, and how these parameters should be chosen in practice.

3.The idea behind SGC lacks novelty, as both algorithms are quite similar to GaLore. Additionally, MESGC appears to be time-consuming, particularly regarding the practical adjustments outlined in Algorithm 4, and the numerical results in Table 2 do not consistently demonstrate CESGC’s superiority over GaLore. The paper does not provide a clear explanation of the trade-offs between the different algorithms, and the practical benefits of MESGC, given its computational overhead, are not clearly demonstrated.

### Questions
1.In Section 4.4, the gradient is chunked during computation. If c is not large, the size of the projection matrix remains significant, leading to high memory consumption. Conversely, if c is large, it introduces c times the matrix multiplications, which may be time-consuming. What is the result of the runtime comparison between MESGC and existing PEFT methods?
2.What is the performance of MESGC on small datasets, as discussed in Section 5.3?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Based on gradient sparsity, this paper proposes a flexible gradient compression method to reduce memory usage during training LLMs. By sparsifying and projecting the gradient onto a low-dimensional subspace, the optimizer state is updated, and then, when updating parameters, it is mapped back to the high-dimensional space using the orthogonal matching pursuit (OMP) algorithm.

### Strengths
1. SGC is more flexible compared to previous methods like LoRA and GaLore, allowing more granular control over the dimensionality of the compressed optimizer state.
2. On commonsense benchmarks, SGC achieves a comparable average accuracy to both GaLore and LoRA while using fewer optimizer state parameters.

### Weaknesses
1. Although SGC is more flexible, this advantage is somewhat marginal, as LoRA and GaLore are already quite flexible.
2. The paper lacks throughput experiments and runtime analysis of OMP.
3. It does not include empirical experiments comparing memory usage of SGC and baseline methods to validate the theoretical analysis.
4. There is no information on the error magnitude after gradient compression.
5. Mischaracterization in lines 350-352 and 368-369, where it mentions GaLore as a type of PEFT method; GaLore is not a PEFT method.

### Questions
What is the practical benefit of increased flexibility and granular control, given that memory usage is primarily dominated by parameters rather than optimizer states in methods like PEFT or GaLore?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new optimizer, Sparse Gradient Compression (SGC), designed to enhance fine-tuning efficiency for large language models (LLMs). The main innovation of SGC lies in compressing the optimizer states, providing a more flexible and granular tradeoff between memory usage and performance compared to other Parameter Efficient Fine-Tuning (PEFT) methods. The compression leverages the inherent sparsity in gradients, with the recovery of compressed states performed through a greedy algorithm called Orthogonal Matching Pursuit (OMP). Experimental results on LLaMA models demonstrate that SGC achieves performance comparable to or even better than existing PEFT methods on some tasks, while reducing memory requirements for optimizer states.

### Strengths
1. The writing is clear and well-structured, with an appropriate balance of detail, making it easy to understand. Most technical choices are well-motivated and thoroughly explained.
2. The motivation behind the proposed SGC method is intuitive, making the approach conceptually accessible and logical given the challenges in fine-tuning large language models.
3. The experiments and comparative analyses effectively demonstrate that SGC offers memory savings while maintaining comparable performance, validating the practical advantages of the approach.

### Weaknesses
1. **Limited Applicability**: While the paper claims that SGC offers a more flexible, fine-grained tradeoff, PEFT methods typically target compute-constrained scenarios, where such granular control may require extra tuning that reduces practicality. It would be beneficial to include a plot with sparsity on the x-axis and performance on the y-axis to directly compare the flexibility of SGC with LoRA. This visualization could more intuitively demonstrate whether SGC’s fine-grained control offers practical performance benefits at different sparsity levels.
2. **Questionable Memory Advantage**: The memory usage for first-order optimization methods largely comes from the model parameters, gradients, activations, and optimizer states. Even with Adam’s two states, optimizer memory costs are typically less than half. SGC, based on Adam, can’t reduce memory below that of simple SGD without momentum, and since it still calculates full gradients, its GPU memory consumption may surpass LoRA, which doesn’t require full gradient computations.
3. **Subpar Performance**: As seen in Table 2, SGC shows no clear performance advantage over methods like LoRA and GaLore, raising questions about its efficacy as a fine-tuning method.
4. **Lack of Related Work Comparison**: The paper omits discussion and comparison with relevant optimizers like Adafactor[1] and CAME[2], which also focus on compressing optimizer states. These omissions reduce the context for understanding SGC’s place among similar methods. Including a comparison on task performance, memory efficiency and convergence speed would better contextualize SGC's advantages and place among similar methods.

### Questions
1. In Equation (6), $\boldsymbol{A}$ is initialized randomly as stated in the appendix. How does this randomness affect the model's final performance? Are there significant differences observed across different random seeds?
2. What are the actual comparisons of wall-clock time per iteration and GPU memory usage when training with SGC compared to LoRA and full Adam fine-tuning? Providing this data for LLaMa-7b in a table or plot format would help clarify SGC's efficiency across contexts.
3. Does SGC offer any advantages over Adafactor and CAME in terms of performance or efficiency? If so, could you elaborate on these advantages?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Sparse Gradient Compression (SGC), a method aimed at reducing memory requirements when fine-tuning LLMs. SGC leverages gradient sparsity to update optimizer states within a low-dimensional subspace, effectively reducing memory usage while preserving performance. Experimental results demonstrate that SGC outperforms traditional parameter-efficient fine-tuning methods, especially in memory-limited settings.

### Strengths
1. The paper presents a novel approach that addresses memory efficiency in large-scale fine-tuning tasks. The proposed approach enables more flexible and granular control over the number of parameters to train during finetuning.
2. Experimental evaluation shows that SGC competes well with and often outperforms existing methods (e.g., LoRA, GaLore) in terms of memory efficiency and accuracy.

### Weaknesses
1. The author highlights limitations in the flexibility and granularity of LoRA due to the dependency on model dimensions. However, in practical applications, these constraints may not significantly impact performance. Many real-world tasks do not require extreme reductions in trainable parameters, and the existing flexibility of LoRA is often sufficient. For instance, as shown in Table 2, LoRA fine-tunes only 0.2% of the parameters, meaning the LoRA weights and optimizer states are not the bottleneck—the base model weights and activations are. Reducing this further to 0.08% would likely not yield significant benefits.

### Questions
1. Can you justify in what scenarios is fine-grained control over the training parameters necessary?
2. If fine-grained control of training parameters is required, are there simpler methods to achieve similar results, such as using different ranks in different transformer layers?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The main contribution of the paper is the introduction of the Sparse Gradient Compression (SGC) method for memory-efficient fine-tuning of large language models (LLMs). SGC leverages inherent sparsity in gradients to compress optimizer states by projecting them onto a lower-dimensional subspace, independent of the model's original parameter dimensions. This approach offers a trade-off between memory efficiency and performance.

### Strengths
- The presentation is clear and easy to follow, with only a few minor typos.
- The proposed sparse gradient method is straightforward and supported by reasonable theoretical foundations.

### Weaknesses
 - **Dataset Limitation**: The authors only use a single dataset (Commonsense) in the experimental sections. I strongly recommend adding at least one more dataset to demonstrate the generalizability of the algorithm across different data domains.

- **Comparison to LoRA in Speed**: While SGC effectively reduces optimizer memory costs similar to LoRA, LoRA offers additional advantages by significantly speeding up the fine-tuning process. Through low-rank adapters and fewer trainable parameters, LoRA can accelerate fine-tuning by 12–16 times compared to full fine-tuning. Since SGC performs full forward and backward propagation, it does not offer the same speed benefit and is likely to be significantly slower than LoRA. I suggest the authors include a training time profile for SGC to clarify this difference. The lack of speedup compared to LoRA is a significant drawback, especially considering the computational cost of large language model training. The authors should clarify if the backward pass is truly full or if it is limited to the target layers, as this has a large impact on the computational cost.

- **Comparison to LoRA in optimizer Memory**: LoRA also has the advantage of substantially reducing optimizer memory costs. For example, in LLaMA-2-7B full fine-tuning, the optimizer memory cost for a batch size of 128 can reach up to 40GB. With low-rank adapters, this can be reduced to under 1GB. Since SGC performs full forward and backward propagation, it does not reduce optimizer memory cost and is expected to be comparable to full fine-tuning. I recommend the authors discuss SGC's optimizer memory usage in more detail. The authors should provide a more detailed analysis of memory usage, including a breakdown of the memory footprint for optimizer states, gradients, and activations. This is crucial for understanding the practical limitations of the method.

- **Base Model Limitations**: Although the authors utilize LLaMA-2-7B, LLaMA-2-13B, and LLaMA-3-8B, I recommend including more state-of-the-art models, such as LLaMA-3.1. Additionally, incorporating models outside the LLaMA family, like Phi-2/Phi-3 or Mistral, could further demonstrate SGC's generalizability across different model architectures. The current selection of models is somewhat limited and does not fully demonstrate the robustness of the proposed method across different architectures and parameter scales.


### Questions
- Please refer to some questions I listed in the weakness section.
- Here are a few typos and minor improvements I found in the paper:
1. Abstract: “dimensionality independent of the original model’s parameters” - it might be clearer to specify “independent of the dimensionality of the original model’s parameters.”
2. Introduction (line 23): "exising PEFT methods" should be "existing PEFT methods."
3. Section 2 (line 127): "Adapter-based methods... However, these approaches can introduce latency during inference." - The phrase "these approaches can introduce latency" might read more smoothly as "these methods may increase latency."
4. Equation in Section 3: Ensure consistency with spaces around equations and symbols, especially around parentheses and operators.
5. Section 4.1 (line 217): "sparisfys(·)" should be "sparsifys(·)."
6. Section 4.3 (line 265): "compressed from pt and qt" should read more clearly as "compressed forms, pt and qt."
7. Section 5.3: "boolQ" should consistently be capitalized as "BoolQ" to match standard dataset naming conventions.
8. Section 5.4: "As indicated in 3" should be "As indicated in Equation 3."

- **Time Profiling**: SGC introduces additional computational overhead and extra time costs compared to full fine-tuning. Could the authors provide further discussion on the complexity of this additional computation, along with some time profiling results to illustrate the impact?


I would like to discuss the questions I raised regarding the weaknesses and concerns with the authors. If my concerns are adequately addressed, I would be willing to reconsider my rating.

### Soundness
2

### Presentation
3

### Contribution
2
