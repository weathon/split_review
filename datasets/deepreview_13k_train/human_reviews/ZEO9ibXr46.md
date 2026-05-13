# MLAE: Masked LoRA Experts for Visual Parameter-Efficient Fine-Tuning

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
In response to the challenges posed by the extensive parameter updates required for full fine-tuning of large-scale pre-trained models, parameter-efficient fine-tuning (PEFT) methods, exemplified by Low-Rank Adaptation (LoRA), have emerged. LoRA simplifies the fine-tuning process but may still struggle with a certain level of redundancy in low-rank matrices and limited effectiveness from merely increasing their rank. To address these issues, a natural idea is to enhance the independence and diversity of the learning process for the low-rank matrices. Therefore, we propose \textbf{M}asked \textbf{L}oR\textbf{A} \textbf{E}xperts (MLAE), an innovative approach that applies the concept of masking to visual PEFT. Our method incorporates a cellular decomposition strategy that transforms a low-rank matrix into independent rank-1 submatrices, or ``experts'', thus enhancing independence. Additionally, we introduce a binary mask matrix that selectively activates these experts during training to promote more diverse and anisotropic learning, based on expert-level dropout strategies. Our investigations reveal that this selective activation not only enhances performance but also fosters a more diverse acquisition of knowledge with a marked decrease in parameter similarity among MLAE, significantly boosting the quality of the model. Remarkably, MLAE achieves new state-of-the-art (SOTA) performance with an average accuracy score of 78.8\% on the VTAB-1k benchmark and 90.9\% on the FGVC benchmark, surpassing the previous SOTA result by an average of 0.8\% on both benchmarks with approximately half parameters. %This achievement highlights its superior capability in visual Parameter-Efficient Fine-Tuning (PEFT).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper discusses an improvement to Low-Rank Adaptation (LoRA), called Masked LoRA Experts (MLAE). The key idea is to randomly drop submatrices within the low-rank matrix during fine-tuning. The authors claim that such a strategy can enhance learning diversity and parameter quality. Moreover, they conduct multiple experiments on visual recognition, including VTAB-1k and FGVC, to demonstrate the effectiveness of MLAE.

### Strengths
1.	This paper is clearly presented and well-organized. The authors also provide a detailed discussion of related works and variants.
2.	MLAE compares multiple masking strategies, including fixed, random, and mixed masking, and presents detailed experimental results for reference.
3.	MLAE shows commendable performance across multiple datasets, surpassing GLoRA on most datasets involved.

### Weaknesses
1.	Two main components, the mix of LoRA experts and MoE dropout, have been discussed in previous studies [1,2], thereby limiting the novelty and technical contribution of MLAE. The specific implementation of masking in MLAE, while presented as a key contribution, appears to be a straightforward application of dropout at the submatrix level. The paper lacks a detailed analysis of why this particular masking strategy is superior to other potential masking techniques, such as structured dropout or more sophisticated methods based on parameter importance.
2.	Since MLAE shares some similarities with recent related competitive baselines, both the differences and performance should be compared between MLAE and these works (e.g., IncreLoRA). The paper does not adequately explore the specific advantages of MLAE over methods that dynamically adjust the rank of the low-rank matrices, such as IncreLoRA or AdaLoRA. A more detailed comparison, including computational cost and parameter efficiency, is needed to justify the proposed approach.
3.	Given that this article proposes a task-independent LoRA improvement, it would be better to perform comparisons with existing LoRA-based methods on fine-tuning LLMs, the main benchmark of PEFT methods. The current evaluation is primarily focused on visual recognition tasks. To demonstrate the general applicability of MLAE, it is crucial to evaluate its performance on large language models, which are the primary focus of parameter-efficient fine-tuning research.

### Questions
1.	In Section 3.3 Adaptive Coefficients, I know that \lambda is set as a learnable parameter, but the paper does not explicitly state this. Suggest clarification.
2.	The ablation experiment in Table 5 seems to indicate that the effect of adaptive coefficients is minimal, e.g., only a 0.2% improvement on average. Why introduce this?
3.	Table 10 indicates that each dataset requires searching for appropriate hyperparameters. How sensitive is the model to different parameters?
4.	Why is lora+dropout not more effective than MLAE?

### Soundness
4

### Presentation
4

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
The paper addresses the redundancy and limited diversity in LoRA's low-rank matrices. The authors introduce Masked LoRA Experts (MLAE), which decomposes low-rank matrices into rank-1 "experts" and applies masking techniques to selectively activate these experts during training. The method involves Cellular Decomposition to divide low-rank matrices into independent rank-1 submatrices or experts, followed by masking. Meanwhile, adaptive coefficients for each expert are determined to control their contribution based on their importance. Experiments conducted on the VTAB-1k and FGVC benchmarks demonstrate that MLAE surpasses previous parameter-efficient fine-tuning baselines.

### Strengths
+ While the LoRA framework has been used within the mixture of experts (MoE) before, the use of masking at the expert level sounds novel. The authors demonstrate how the adaptive dropout technique combined with cellular decomposition effectively addresses redundancy.
+ The authors provide extensive experiments across 24 tasks covering both general vision tasks and fine-grained classification.
+ The paper is well-organized and easy to follow.

### Weaknesses
 - Regarding Masking Configurations: While stochastic masking performed best, the analysis could be expanded by exploring additional dropout probabilities or scheduling strategies to better understand how different levels of sparsity affect each dataset type (e.g., specialized vs. structured). Specifically, the paper lacks a detailed exploration of how varying dropout rates within stochastic masking impact performance across different dataset categories. It would be beneficial to see a more granular analysis, perhaps by testing a range of dropout probabilities (e.g., 0.1, 0.3, 0.5, 0.7, 0.9) for each dataset type to identify optimal sparsity levels. Furthermore, the paper should investigate dynamic dropout scheduling, where the dropout probability changes during training, which could potentially lead to better performance.

- Computational Costs: The authors briefly mention longer training times for MLAE due to the introduction of dropout but do not fully explore how significant this increase is. Adding a thorough analysis of training time vs. performance trade-offs could improve the practical usability of MLAE. The paper should include a detailed comparison of training times between LoRA and MLAE, not just a qualitative statement about increased time. This comparison should be done across all datasets, or at least representative datasets from each category (Natural, Specialized, Structured), to understand the practical implications of the increased training time. Furthermore, the analysis should include a discussion of the trade-off between training time and performance gains, which would help practitioners decide whether the performance improvement justifies the additional computational cost.

### Questions
- In the experiments, stochastic masking is found to perform best. Have different dropout probabilities or dynamic dropout scheduling been considered within each masking type?
- Could the authors provide more insight into why cellular decomposition (rank-1 expert decomposition) specifically benefits generalization? Is there a theoretical foundation for why smaller, rank-1 updates lead to better performance in PEFT, or is it primarily an empirical observation?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a novel approach to LoRA adapters by treating each rank as an independent expert, incorporating a rank-wise dropout mechanism to enhance diversity and independence among these experts. They also introduce a learnable weight for each rank, allowing adaptive emphasis on different ranks during training. This method, validated on VTAB-1K and FGVC datasets, demonstrates its effectiveness by achieving state-of-the-art performance with greater parameter efficiency.

### Strengths
1.The paper introduces a dropout mechanism specifically for LoRA adapters, applying rank-wise dropout to improve model generalizability.
2.The concept of treating each rank in the LoRA adapter as an independent expert is innovative, providing a fresh perspective on parameter-efficient fine-tuning.
3.The paper is well-structured and easy to follow, making the proposed methodology accessible and clear.

### Weaknesses
1.The claims regarding the use of cellular decomposition to impose independence and diversity constraints (lines 18-21, 161) lack clarity. Specifically, there is no explicit mention of how independence among the 8$\times$rank-1 LoRA matrices is achieved or how it is better than a rank-8 LoRA. Additionally, it’s not evident how using 8$\times$rank-1 LoRAs differs from a single Rank-8 LoRA, as rank 8 LoRA can be viewed as concatenate row and column vectors of the 8 rank-1 LoRAs. This raises questions about whether the observed differences in Table 6 results are significant or coincidental, and further analysis or confidence intervals would strengthen this claim. The authors should clarify whether the observed performance gains are due to the rank-wise dropout, or simply the increased number of parameters when using multiple rank-1 matrices. A more rigorous analysis, possibly including a comparison with a rank-8 LoRA with an equivalent number of parameters, is needed to validate the effectiveness of the proposed decomposition strategy.

2.Apart from the rank-wise dropout, the advantage of adding adaptive weights to each rank in the LoRA adapter appears limited, suggesting that its contribution to performance may be minor. The paper lacks a detailed ablation study to quantify the isolated impact of these adaptive weights. It is unclear if the performance gains are statistically significant, or if they are simply due to random fluctuations during training. The authors should provide a more thorough analysis to justify the inclusion of this component.

3.The paper does not provide sufficient configuration details for the VTAB-1K experiment, making reproducibility challenging. Specifically, the masking schedule, initialization coefficients, and other hyperparameters used in the VTAB-1k experiments are not clearly specified. This lack of detail makes it difficult for other researchers to replicate the results and validate the claims made in the paper.

4.The core idea shares similarities with recent papers, including "LoRA Dropout as a Sparsity Regularizer for Overfitting Control" (Lin et al., 2024) and "LoRA Meets Dropout under a Unified Framework" (Wang et al., 2024). Highlighting the distinctions more clearly would strengthen the paper's originality. The paper should provide a more detailed comparison of the proposed method with these existing approaches, emphasizing the specific differences in the dropout application and the overall methodology. A more thorough discussion of how the proposed method builds upon or differs from these works is needed to establish its novelty.

5.(minor)In Table 1, the source for certain numbers should be specified, particularly those taken from previous publications, like the GLoRA paper.

### Questions
Need either analysis on the claim for preferring 8$\times$Rank-1 LoRA against Rank-8 LoRA without the proposed dropout, or the p-value of Tab.6.
Also please provide the experiment settings, especially the configuration of the proposed method, for the VTAB-1k experiment, including which hyperparameter you choose and also the masking schedule you use to reproduce the results.

### Soundness
3

### Presentation
3

### Contribution
2
