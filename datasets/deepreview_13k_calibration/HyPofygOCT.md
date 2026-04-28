# ASVD: Activation-aware Singular Value Decomposition for Compressing Large Language Models

- Decision: Reject
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
In this paper, we introduce a new post-training compression paradigm for Large Language Models (LLMs) to facilitate their wider adoption. We delve into LLM weight low-rank decomposition, and find that the challenges of this task stem from ❶ the distribution variance in the LLM activations and ❷ the sensitivity difference among various kinds of layers. To address these issues, we propose a training-free approach called Activation-aware Singular Value Decomposition (ASVD). Specif- ically, ❶ ASVD manages activation outliers by transforming the weight matrix based on the activation distribution. This transformation allows the outliers in the activation matrix to be absorbed into the transformed weight matrix, thereby enhancing decomposition accuracy. ❷ Additionally, we propose an efficient iter- ative calibration process to optimize layer-specific decomposition by addressing the varying sensitivity of different LLM layers. In this way, ASVD can compress a network by 10%-30%. Based on the success of the low-rank decomposition of projection matrices in the self-attention module, we further introduce ASVD to compress the KV cache. By reducing the channel dimension of KV activations, memory requirements for KV cache can be largely reduced. ASVD can further achieve 50% KV cache reductions without performance drop in a training-free manner.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes Activation-aware Singular Value Decomposition (ASVD) to prune the weights of LLMs in a training-free manner. In particular, the technical contributions include a data whitening trick with activation magnitude or Cholesky decomposition as well as a layer-wise rank search method. The empirical studies are extensive.

### Strengths
- The paper is well written, with extensive empirical results support the arguments. 

- The combination with quantization approaches is desirable.

### Weaknesses
 - One major issue is the close relationship and similar results with SVD-LLM. In particular, the paper offers a choice of using activation magnitude to construct the whitening matrix while SVD-LLM advocates the Cholesky decomposition of the activation covariance. As shown in Table 2, the latter is consistently superior (corresponding to ASVD+). In this sense, the original contribution of this paper is minor. The searching method of layer-wise rank with a calibration set is relatively novel compared to SVD-LLM, but it is still widely used in training-free LLM compression (see [1, 2]).

- The rationale of KV cache compression is not clear enough. In particular, the positional embedding is not considered when developing the low-rank projections. In my practice, this cannot decrease peak running memory for the whole system, while slightly reducing the storing memory. Besides, comparing your compressed states with those in EigenAttn [3], which one is better? In my opinion, EigenAttn does not consider the weight matrix when constructing the low-rank projections but your method considers that weight. What will this lead to?

- When the Param ratio is relatively low (e.g., less than 0.7), the compression is more promising, but the method is worse than SVD-LLM. Besides, metrics like MMLU should be reported in each scenario because it is of more concern in practice. And other task-specific metrics should also be included like accuracies on gsm, wino, etc.

### Questions
See above

### Soundness
3

### Presentation
3

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
This article introduces a novel, training-free, low-rank pruning method for reducing the memory and computational demands of large language models (LLMs). ASVD addresses the challenges of distribution variance in activations and sensitivity differences across layers.

### Strengths
### Strengths:
- ASVD introduces a pioneering approach in SVD pruning by accounting for the influence of activation distribution, inspiring subsequent works like SVD-LLM and Palu.
- ASVD innovates with a sensitivity-based truncation rank search, enabling dynamic allocation of non-uniform ranks across layers.

### Weaknesses
### Weaknesses:
- This type of activation-based pruning is not novel in the pruning field, particularly within LLM pruning, as demonstrated by methods like Wanda [1], RIA [2], and others. While ASVD uses the matrix product of weights and activations, other methods also leverage activation information for pruning decisions, making the core concept of activation-aware pruning not entirely new. The novelty is further diminished by the fact that many pruning methods, including those cited, already consider the magnitude of weights and activations in some form.
- The memory compression rate of ASVD is lower than that of other methods, such as quantization and unstructured/semi-structured pruning, which may limit its applicability. However, exploring memory compression techniques beyond quantization and pruning is also valuable. ASVD’s contribution to SVD pruning may have the potential for future advancements in-memory compression. The practical impact of this lower compression rate is significant, as it directly affects the feasibility of deploying large models on resource-constrained devices. The paper should acknowledge that the current compression rate is a limitation for real-world applications.
- The sensitivity-based truncation rank search involves calculating PPL for each layer at varying truncation ratios, which may be time-consuming for large models. This process is computationally expensive and may not scale well to extremely large models, making it impractical for real-world deployment scenarios. The paper should provide a more detailed analysis of the computational cost and scalability of this search method.
- The paper lacks experiments on actual memory footprint or computation speedup. This absence of empirical data makes it difficult to assess the practical benefits of the proposed method. Without concrete numbers on memory savings and speedup, the claims of efficiency remain unsubstantiated.

### Questions
### Questions:
- Several other unstructured pruning methods use non-uniform layerwise sparsity, such as OWL [3]. Could the authors compare sensitivity-based truncation rank search with these non-uniform sparsity approaches?
- Could you test the actual memory footprint and computation speedup of ASVD?

---

[3] Yin, Lu, et al. "Outlier Weighted Layerwise Sparsity (OWL): A Missing Secret Sauce for Pruning LLMs to High Sparsity." *Forty-first International Conference on Machine Learning.*

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
ASVD is a method for the compression of LLMs. SVD is applied not to the original weight matrix, but to the transformed one. The transformation is computed using samples from the dataset.

### Strengths
The main idea is clear, and the paper is well-written. There are enough experiments to convincingly demonstrate that the algorithm performs better than pure SVD. The possibility of quantization and KV-cache compression is also highlighted.

### Weaknesses
The only solid dataset is MMLU, and the only LLM family is LLAMA-2.

### Questions
* Am I correct in assuming that the matrix $S^{-1}$ is also counted in the total number of parameters? Does it make sense to set $S = L$, where $L$ is the Cholesky factor, in terms of the parameters stored?
* Would it be possible to include plots of the normalized singular values for different layers, as seen in "Reduced-Order Modeling of Deep Neural Networks" by Gusak et al.?

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
5

### Summary
The paper introduces the Activation-aware Singular Value Decomposition (ASVD), a training-free method for compressing large language models (LLMs). It targets compression challenges like activation distribution variances and layer sensitivity. ASVD achieves compression by transforming weight matrices based on activation distribution and adjusting for layer sensitivity through an iterative calibration.

### Strengths
1. The method proposes a train-free method for model compression of LLMs, and it uses activation values to rescale the weight matrix so that weight vectors with larger activation norms are more important.
2. It further reduces the KV cache due to SVD, but one may need to recompute the KV using the low-rank KV at the next prediction step.
3.  Its performance is better than SVD and FWSVD.

### Weaknesses
1. The methodology framework of this paper is mostly based on weighted SVD, where you use a diagonal matrix to reweight the weight vector. The difference between this paper and FWSVD is that this paper puts the activation magnitude in the diagonal, and FWSVD puts the fisher information into the diagonal matrix.
2. One of the problems of SVD is that the full-rank model actually has twice the size of the original model. As a result, if you prune the model to 90% parameters of the original model, you remove 55% of ranks on average. A better way for SVD is to look at layers where they are not connected by activation functions (non-linearity), where you can get 50% parameter reduction for 50% rank reduction, examples are the value matrix and output transformation matrix like in [1].
3. Missing results regarding zero-shot performance beyond MMLU. In SVD-LLM, they tested their results on other tasks, like MathQA, PIQA, etc.
4. Missing related works on compressing language models with SVD [2]. In [2], the method can find the number of ranks per weight matrices in a learning process which is very relevant to section 3.4 of this paper.

### Questions
Please refer to weakness.

### Soundness
3

### Presentation
3

### Contribution
2
