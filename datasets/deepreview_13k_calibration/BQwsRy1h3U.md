# MatryoshkaKV: Adaptive KV Compression via Trainable Orthogonal Projection

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
KV cache has become a \emph{de facto} technique for the inference of large language models (LLMs), where tensors of shape (layer number, head number, sequence length, feature dimension) are introduced to cache historical information for self-attention. 
As the size of the model and data grows, the KV cache can quickly become a bottleneck within the system in both storage and memory transfer.
To address this, prior studies usually focus on the first three axes of the cache tensors for compression.  
This paper supplements them, focusing on the feature dimension axis,  
by utilizing low-rank projection matrices to transform the cache features into spaces with reduced dimensions. 
We begin by investigating the canonical orthogonal projection method for data compression through principal component analysis (PCA). 
We observe the issue with PCA projection where significant performance degradation is observed at low compression rates.
To bridge the gap, we propose to directly tune the orthogonal projection matrices with a distillation objective using an elaborate Matryoshka training strategy.
After training, we adaptively search for the optimal compression rates for various layers and heads given varying compression budgets. 
Compared to previous works, our method can easily embrace pre-trained LLMs and hold a smooth tradeoff between performance and compression rate. 
We empirically witness the high data efficiency of our training procedure and find that our method can sustain over 90\% performance with an average KV cache compression rate of 60\% (and up to 75\% in certain extreme scenarios) for popular LLMs like LLaMA2-7B-base and Mistral-7B-v0.3-base.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces MatryoshkaKV, a method for compressing the Key-Value (KV) cache in large language models (LLMs) to reduce memory during inference. The method begins with PCA for initial dimensionality reduction but addresses PCA’s limitations by tuning projection matrices through knowledge distillation and applying Matryoshka training strategy to enable adaptive compression, allowing the model to balance performance and compression. Furthermore, this paper demonstrates effectiveness with high compression rates while maintaining relatively high accuracy across various LLMs on both CPT and SFT tasks.

### Strengths
1. The proposed Matryoshka training strategy effectively preserves hierarchical structures in orthogonal matrices inherited from PCA at various compression levels, ensuring robust performance across dimensions.

2. Greedy search algorithm effectively adapts to differing sparsity in each 
$𝑊_𝑘$ and $𝑊_𝑣$ matrix, showcasing flexibility in compression rates across layers.

3. There are comprehensive MKV evaluations across cache budgets, which reveals substantial improvements, particularly under extremely low cache budget.

### Weaknesses
1. Lack of Runtime Evaluation: The absence of runtime metrics makes it challenging to assess the practical benefits of this method fully (see Questions).

2. Missing State-of-the-Art Comparisons: Unusually, the paper doesn’t thoroughly compare to existing state-of-the-art methods. Although it mentioned the other methods may collapse under  60% cache budget (lines 126-131), a comparison with Eigen-Attention and HeadKV at different cache budgets and tasks in terms of both performance and runtime would strengthen the evaluation.

### Questions
1. Although the paper mentions it only needs processing 2 million training tokens (line 104), it does not clarify the runtime for each base model and task. Please provide the runtime details for the KV compression process, including PCA initialization, the greedy search for compression level selection, and fine-tuning in both CPT and SFT tasks. Notably, since both the greedy search and compression levels rely on outputs from the original model, this could potentially double the training and inference times.

2. How is $\Delta𝑟$ determined in the greedy search algorithm? And what values are used in the experiments? 

3. In Fig.4, MKV seems to work well with uniform compression rates. Does this always apply to all tasks? 

3. Line 96: k→r?

### Soundness
3

### Presentation
3

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
The authors study the problem of KV cache compression. While existing work focuses on compression along the layer number, the head number, and the sequence length, the authors work on the feature dimension. While PCA is the most intuitive approach, it does not provide good enough performance. Instead, the authors propose to directly tune the orthogonal projection matrices with a distillation objective using an elaborate Matryoshka training strategy.

### Strengths
1. The paper is easy to follow.
2. Much stronger performance than the PCA baseline when the compression ratio is low.

### Weaknesses
1. It is unclear whether the novelty of the paper is significant.
2. The paper does not compare with the methods that compress the other dimensions. Thus, it is unclear whether the proposed method is more effective. It is also unclear whether the proposed method can be combined with the others while maintaining its effectiveness.

### Questions
1. Can the author provide more insight so that the novelty is more than just the direct application of the Matryoshka training strategy proposed by the other paper?
2. Can the author compare with one to two baselines that compress the other dimensions to show compressing the feature dimension is more effective? Or can the author show that they can be combined together to further improve the performance?

### Soundness
3

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
This paper proposes MatryoshkaKV, a method to compress the key-value (KV) cache in large language models (LLMs) along the feature dimension using trainable orthogonal projection matrices. As LLMs grow in size, the KV cache can become a bottleneck in storage and memory transfer. Previous approaches have focused on compressing the cache along the layer, head, and sequence length dimensions. This work explores compressing along the feature dimension.

The authors first investigate using PCA to obtain orthogonal projection matrices for dimensionality reduction of the keys and values in each attention head. While this works well at moderate compression levels without needing training, performance degrades quickly at higher compression.

To improve on this, they propose MatryoshkaKV which tunes the orthogonal projection matrices end-to-end using a knowledge distillation objective and a special "Matryoshka" training strategy that enables adaptively searching for optimal compression rates per layer and head at inference time. The orthogonality of the projections is enforced using a Cayley parameterization.

### Strengths
The paper tackles the problem of KV cache compression in LLMs from a new angle by focusing on the feature dimension. While prior work has explored compressing along the layer, head, and sequence length dimensions, this work shows that significant compression gains can also be achieved along the feature axis. This opens up a promising new direction for efficient LLM inference.

The MatryoshkaKV method demonstrates impressive performance in experiments. It can compress KV caches by 60-75% on average while retaining over 90% of the full model's accuracy. This is a significant improvement over the PCA baseline, especially at high compression rates. The results hold across both continual pre-training and supervised fine-tuning settings, showing the approach is robust and widely applicable.

### Weaknesses
The paper lacks rigorous theoretical analysis of why their proposed MatryoshkaKV method works better than PCA-based approaches. While they provide some error analysis in Appendix A, it's relatively brief and doesn't fully explain the theoretical underpinnings of their method's superior performance. Specifically, the analysis does not delve into the nuances of how the trainable orthogonal projections capture the complex interactions between keys and values within the attention mechanism, nor does it provide a clear mathematical framework for understanding the observed performance gains. A more detailed analysis, perhaps drawing from established results in linear algebra or information theory, would be beneficial.

While the empirical results are promising, the limited evaluation on very long sequence tasks where KV cache compression would be most valuable is a significant concern. The experiments primarily focus on relatively short sequences, and it's unclear how well MatryoshkaKV would perform when dealing with the extremely long contexts that are increasingly relevant in modern LLM applications. The potential for error accumulation or instability in the compressed representations over very long sequences needs to be addressed with more comprehensive experimentation.

### Questions
Why does the Matryoshka training strategy work better than static compression ratios? What's the theoretical justification?

How sensitive is the method to the choice of sampling schedule for compression rates during training?

Why is PCA initialization critical for convergence? Could other initialization strategies work?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel method to efficiently compress Key-Value (KV) cache for large language models (LLMs) like LLaMA2-7B and Mistral-7B, which can be a bottleneck in terms of storage and memory transfer. The authors propose using low-rank orthogonal projection matrices, initialized with PCA and further fine-tuned with a distillation objective, to compress the feature dimension of the KV cache. The novel Matryoshka training strategy allows adaptive selection of compression levels for different layers and heads, balancing model performance and compression rate. Experiments demonstrate high data efficiency, with the method achieving over 90% performance while compressing the KV cache by 60% on average.

### Strengths
- The paper introduces a novel method to compress KV cache by focusing on the feature dimension. By employing low-rank projection matrices combined with orthogonality constraints, the authors efficiently reduce the KV cache size without requiring retraining from scratch, allowing the compression mechanism to be integrated directly into pre-trained models.

- The proposed training strategy to fine-tune orthogonal projection matrices effectively preserves model performance while allowing adaptive compression rates, providing a flexible approach to balance resource usage.

- The use of heterogeneous compression rates across different layers and heads is well-motivated and effectively demonstrated

### Weaknesses
 - Although the paper briefly mentions other KV cache compression methods, such as sharing KV headers across layers and merging redundant tokens, it lacks a detailed comparison to highlight the advantages of the feature-dimension based compression. Including experimental comparisons or a more thorough discussion of the advantages and disadvantages of each approach would strengthen the contribution and clarify the unique benefits of the proposed method.

- The justification for using predefined schedules for Matryoshka strategy and the heterogeneous compression rates with greedy search could be made stronger with more theoretical backing or detailed analysis. For example, are the results sensitive to different schedules? Is the greedy search algo. deterministic and with the grantee to converge, and how's the scalability? 

- The Figure 4 seems to indicate the Matryoshka strategy is much more important than greedy search (yellow and green lines are closed in right), and Orthogonal Constraint has less effect when Cache Utilization<0.5. More discussion and analysis on these findings are encouraged.

### Questions
see weakness

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a KV cache compression technique for efficient LLM inference through low-rank projections along the feature dimension.  Using principal component analysis (PCA) over key and value matrices to obtain low-rank counterparts leads to performance loss, especially at high compression ratios. To tackle this, the authors propose to tune the projection matrices for each layer and attention head with a distillation loss. Results are presented for Llama-2 (7b) and Mistral-v0.3 (7b) models.

### Strengths
1. This work targets KV cache compression, a crucial problem for efficient LLM inference at large sequence lengths. Results show extensive improvements over vanilla PCA for a variety of downstream tasks.

### Weaknesses
1. The training to obtain orthogonal projection matrices involves a KL divergence loss, which ensures that the KV compressed model performance stays close to the original model. However, this makes the strategy task-dependent by using a form of calibration dataset for the downstream task itself, leading to the necessity of training every time one needs a compressed KV cache for performing inference on certain task(s). Additionally, there is no clarification on the calibration dataset used for continual pretraining experiments in Section 5.1. The need to perform a greedy search for adaptive compression rates for each new task further exacerbates this issue, adding to the computational overhead.
2. For results in Section 5.2, the authors propose a 2-stage training pipeline: 1. LoRA (standard fine-tuning) 2. Updating projection matrices and LoRA parameters jointly. While the first stage is generally employed to improve the performance of LLMs on downstream tasks, the second stage is the associated overhead with this form of KV cache compression. Additionally, the joint update in this stage implies the need to compress the KV cache specifically for each downstream task. It would be ideal to have a task-agnostic KV cache compression scheme, or at least a method that minimizes task-specific tuning.
3. Comparisons with baselines are missing and/or somewhat ambiguous. Is the PCA baseline in Table 1 the same as Eigen Attention [1]? Another missing potential baseline is ASVD [2], which also involves training-free low-rank projection to reduce the KV cache footprint. The authors clarify that a variety of works compress the KV cache by targeting the sequence length or channel dimension, but don't demonstrate the possibility of using their approach concurrently with such techniques [3,4]. Furthermore, the lack of clarity on the specific implementation details of the PCA baseline makes it difficult to assess the true improvement of the proposed method.
4. Results on the more recent family of Llama models (Llama 3/3.1) are missing but crucial to establish the effectiveness of this approach. The absence of these results limits the generalizability of the findings, as the Llama 3 architecture incorporates modifications that could impact the performance of the proposed compression technique.

### Questions
1. Can the authors clarify how they achieve performance benefits with heterogeneous ranks across the head dimension? Different dimensions across the heads may require some form of padding before concatenating them during actual inference, so it would be great to see some hardware performance numbers as well.
2. Which calibration dataset was used for the results presented in Table 1? 
3. For the SFT setup described in Section 5.2, it would be interesting to see if the second stage of training can just be limited to projection tuning instead of the proposed joint tuning with LoRA parameters as well.

### Soundness
2

### Presentation
3

### Contribution
3
