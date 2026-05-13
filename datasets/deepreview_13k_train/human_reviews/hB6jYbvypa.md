# MoE-Pruner: Pruning Mixture-of-Experts Large Language Model using the Hints from Its Router

- Decision: Reject
- Scores: 3, 5, 3, 6

## Abstract
Mixture-of-Experts (MoE) architectures face challenges such as high memory consumption and redundancy in experts. Pruning MoE can reduce network weights while maintaining model performance. Motivated by the recent observation of emergent large magnitude features in Large Language Models (LLM) and MoE routing policy, we propose MoE-Pruner, a method that prunes weights with the smallest magnitudes multiplied by the corresponding input activations and router weights, on each output neuron. Our pruning method is one-shot, requiring no retraining or weight updates. We evaluate our method on Mixtral-8x7B and Mixtral-8x22B across multiple language benchmarks. Experimental results show that our pruning method significantly outperforms state-of-the-art LLM pruning methods. Furthermore, our pruned MoE models can benefit from a pretrained teacher model through expert-wise knowledge distillation, improving performance post-pruning. Experimental results demonstrate that the Mixtral-8x7B model with 50\% sparsity maintains 99\% of the performance of the original model after the expert-wise knowledge distillation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a pruning method specifically designed for Mixture-of-Expert (MoE) models. It uses the Gate values from the MoE router to enhance weight importance evaluation during pruning. Additionally, it introduces an expert-wise approach for knowledge distillation to improve the performance of the pruned model.

### Strengths
1. New Insights: The paper provides valuable insights into how expert initialization methods influence final load balance and similarities between experts.

  2. Perplexity Performance Improvements: The proposed method leverages gate values in MoE to enhance the performance of pruned models, achieving perplexity improvements over previous methods designed for general transformer-based LLMs.

### Weaknesses
 1. Efficiency Evaluation: The paper lacks an evaluation of the proposed method’s efficiency improvements, such as wall-clock speedup or memory reduction.

  2. Limited Technical Contribution: Pruning weights in the least-activated expert appears intuitive, yet it’s unclear how the method addresses potential drawbacks. For instance, which specific capabilities are impacted by this pruning? Does the improved performance on tested tasks come at the cost of decreased performance on other rare but crucial tasks?

  3. Unclear Contribution of Gate Value Insights: While the paper discusses gate value differences between two MoE initialization methods, it doesn’t clarify how these insights inform the pruning method’s design. Additionally, a brief definition of sparse upcycling initialization in related work would be helpful, as it is repeatedly referenced in later discussions.

  4. Writing and Support for Claims: Some technical claims lack proper references or justification. For example, the statement “MoE mitigates catastrophic forgetting in continual learning” (Line 44, Introduction) is not supported by references. Similarly, the claim that “expert activation frequency is task-agnostic” (Line 161, Methodology) seems conclusive, yet the paper does not provide corresponding experimental or logical evidence.

### Questions
1. What is the runtime efficiency of the proposed method?

  2. What is the maximum sparsity that the proposed method can achieve without incurring significant perplexity loss? Could you provide performance comparisons under moderate losses, such as a 10% perplexity increase compared to the dense model? The perplexity loss at 50% density appears a bit high for both the proposed method and baselines.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a simple and effective pruning method for MoE models. Specifically, (1) the authors prune model weights based on the sensitivity criterion derived from the MoE gate outputs in each transformer block; (2) they further use a distillation method to recover task performance of the pruned model. Experimental results show that on zero-shot and language modeling datasets, the proposed method outperforms existing weight pruning methods in terms of algorithm performance.

### Strengths
1. The authors propose a simple yet effective MoE pruning method that can be easily applied to various existing MoE models, achieving notable performance improvements.
  2. The authors provide a detailed ablation study of each component and hyperparameter, clearly demonstrating the role of each component and the sensitivity to hyperparameters.

### Weaknesses
1. Equations lack detailed explanation.

    - For equations 7, 8, and 9, what do i and j stand for? Please describe in detail which dimension in each tensor corresponds to i and j. By the way, I also notice that in equation 9, the authors use S instead of S_{i,j} to represent the sensitivity metric. Is this a typo?

    - For equation 10, is cross entropy the global next token prediction loss or the local cross entropy loss for the MoE gate?

2. Algorithm 1 needs detailed explanation. In line 251, the authors mentioned that "Algorithm 1 presents the unstructured sparsity version of our MoE-Pruner algorithm". I don’t understand where "unstructured" is reflected. Is it that the weights of the experts are unstructured? Does the weight WWW represent all experts or just one expert? Also, which linear layer in SwiGLU does the weight WWW correspond to?

3. The experimental comparisons are not comprehensive. In the Introduction, the authors mention various issues with expert merging and expert pruning. However, in the experimental section, they do not compare their method with any expert merging or pruning methods [1,2,3]. The authors need to provide some comparative data and analysis to demonstrate whether their proposed method is truly SOTA.

[1] Liu et al., Efficient expert pruning for sparse mixture-of-experts language models: Enhancing performance and reducing inference costs

[2] Lu et al., Not All Experts are Equal: Efficient Expert Pruning and Skipping for Mixture-of-Experts Large Language Models

[3] Muzio et al., SEER-MoE: Sparse Expert Efficiency through Regularization for Mixture-of-Experts

### Questions
1. In line 154, the authors mentioned that upcycling initialization will lead to higher expert similarity in MoE models. Since the similarity between experts is relatively high, pruning experts should theoretically not result in a significant performance drop. Why do the authors reach the opposite conclusion?
  2. In line 158, the authors mentioned that train from stratch will show imbalanced expert activation frequency, indicating that least-used expert pruning could help compress model size and not bring performance degradation. However, I believe this may be task-dependent; these seemingly least-used experts could be very useful for specific tasks such as math or coding. Did the authors conduct any related validation?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work proposes MoE-Pruner, a pruning strategy for MoE based LLMs. MoE-Pruner uses the scores from the routers as signals to prune the experts and then performs an expert-wise distillation training to recover the performance. Experiments on Mixtral-8x7B and Mixtral-8x22B show that MoE-Pruner can outperform other pruning strategies for dense LLMs.

### Strengths
- Pruning MoE is an important and impactful research problem
- The proposed method is conceptually simple yet can achieve encouraging results

### Weaknesses
 - **Limited technical novelty and justification** - MoE-Pruner is to be a simple extension of Wanda's formulation without extending any of its analyses to MoE. Specifically, the paper does not provide a theoretical justification for how the router scores are incorporated into the pruning metric, nor does it analyze the impact of this modification on the pruning behavior. Similarly, the expert-wise knowledge distillation seems to be quite straightforward to extend from the standard knowledge distillation, lacking a detailed analysis of why this approach is optimal for MoE models, or how it compares to other distillation strategies. Therefore, I consider the technical contribution of this work to be limited.
- **Limited evaluation** - MoE-Pruner is only evaluated on Mixtral models, it would be helpful to test its robustness by considering other models such as DeepSeek-MoE or MiniCPM-MoE. The evaluation also lacks a comprehensive ablation study on the impact of different pruning ratios and distillation parameters, which would be crucial for understanding the method's sensitivity and generalizability.
- **Complexity analysis** - The paper does not provide a complexity analysis showing the pruning and inference speedup. It also does not analyze the memory overhead of storing the sparse masks, which is important for practical deployment.
- **Poor presentation** - The paper is poorly organized. Section 2 (Preliminaries) is too short while Sections 3.1 and 3.2 are essentially a literature review, serving the same purpose. Figure 1 does not clearly explain the method as the score S does not interact with other components in the figure.

### Questions
- What is pruning and inference speedup of MoE-Pruner compared to other baselines?
- How did the authors extend Wanda to MoE models, is it equivalent to setting $Gate_j = 1$ in MoE-Pruner?
- The method is poorly motivated (only from L232-237). A deeper analysis (for example, Section 3, Wanda) is preferred.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper focuses on the pruning of sparse mixture-of-experts (MoE) models. It introduces a method called MoE-Pruner, which selectively prunes weights based on the smallest magnitudes, factoring in both the corresponding input activations and router weights for each output neuron. Experiments are conducted on the Mixtral family models to evaluate the approach's effectiveness.

### Strengths
(1) The method is clearly explained.

(2) The proposed method is efficient and practical for real-world deployment.

### Weaknesses
(1) The evaluation is restricted to the Mixtral models, raising questions about the method's scalability to other architectures like Qwen and DeepSeek.  

(2) The distilled step shows only minor improvements, as seen in Table 4. What could be the underlying reason for this limited gain?

(3) This method builds incrementally on the baseline, Wanda, by incorporating gate weights within the MoE pruning framework.

### Questions
Some previous studies have focused on pruning entire experts, as seen in [1, 2, 3]. Could this method potentially be integrated with these approaches to enhance overall pruning effectiveness?    
[1] Lu, et al. "Not All Experts are Equal: Efficient Expert Pruning and Skipping for Mixture-of-Experts Large Language Models." ACL 2024.   
[2] Zhang, et al. "Diversifying the expert knowledge for task-agnostic pruning in sparse mixture-of-experts." arXiv preprint arXiv:2407.09590 (2024).   
[3] Lee, Jaeseong, et al. "STUN: Structured-Then-Unstructured Pruning for Scalable MoE Pruning." arXiv preprint arXiv:2409.06211 (2024).

### Soundness
3

### Presentation
3

### Contribution
2
