# Rethinking Sparse Scaling through the Lens of Average Active Parameter Count

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Parameter pruning has emerged as a promising technique to address the growing computational demand of large language models (LLMs). While many studies focus on post-training pruning of LLMs, sparse pre-training offers a compelling alternative: sparsifying during pre-training reduces both training and inference costs. In this work, we conduct the first comprehensive study on optimal sparse pre-training configurations for LLMs, exploring various pruning schedules across different sparsity levels and training duration. We evaluate 80 unique configurations and find that a pruning schedule starting at 25% of total training compute and ending at 75% achieves near-optimal final evaluation loss. Our findings provide valuable insights for efficient and effective sparse pre-training of LLMs. Furthermore, we propose a new scaling law that modifies the Chinchilla scaling law to use the average number of active parameters during training. We present both empirical and theoretical evidence that this modification accurately models evaluation loss for both sparsely and densely pre-trained LLMs, thus offering a unified scaling law for dense and sparse model training. Our insights suggest that, while sparse pre-training yields similar model loss as dense pre-training for the same compute budget, it offers a clear advantage: the final model is smaller, resulting in significant potential computational savings during inference.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper conducts an overwhelming analysis of the effect of sparse pretraining on large language models (LLMs). Specifically, it proposes a new scaling law that is modified from the Chinchilla scaling law using a novel concept of the average number of active parameters during training, i.e., the averaged number of parameters that receive gradients in LLM pretraining among all training steps. The experimental results show that the proposed new scaling law sufficiently fits the evaluation loss prediction of LLM pretraining, while leveraging sparse pretraining could match the sparse, pruned model's evaluation loss to a larger, dense LLM.

### Strengths
- This paper extends the Chinchilla scaling law and adapts it to the scenario of sparse pretraining, where the modified scaling law uses the concept of averaged activate parameter number to sufficiently model the evaluation loss of LLMs.
- When design a pretraining pruning schedule using the scaling law proposed in this paper, one can pretrain an LLM with fewer parameters yet matching the evaluation performance of a dense model.
- The theoretical and empirical analysis in this paper demonstrates strong proof of the scaling law proposed in this paper.

### Weaknesses
 - The scale of models being used in this paper is limited, as the authors have addressed in the limitation section. Larger model experiments are definitely useful and could bring wider impact to this paper. Specifically, the paper would benefit from experiments that explore the scaling behavior of the proposed method with models that approach the size of state-of-the-art LLMs, as the current experiments may not fully capture the complexities of very large-scale pretraining.
- The only evaluation metric being used in this paper is the pretrained model's perplexity (or pretraining evaluation loss) without downstream task evaluations. As models could forget knowledge in pretraining because of pruning, a finer-grained analysis with task-specific evaluations could be beneficial. The paper should include evaluations on a diverse set of downstream tasks to assess the generalizability of the learned representations and to understand if the sparse pretraining approach leads to any degradation in performance on tasks that require specific knowledge or reasoning abilities.
- What is the exact pruning method being used in the iterative pruning phase? A detailed description of the pruning criteria could be helpful for the audience to understand (e.g., structured/unstructured pruning and how is the pruning decision being made). It is unclear if the pruning is applied to individual weights, groups of weights, or entire layers, and how this choice might affect the model's performance and the applicability of the proposed scaling law.
- $\bar{N}$ and $D$ are independent variables shown in equation (2), however, there seems no analysis in this paper showing that the effects of $\bar{N}$ and $D$ bring to the model's evaluation loss are independent. The paper assumes that the effects of average active parameters and dataset size on the loss are independent, but this assumption needs to be empirically validated, especially in the context of sparse pretraining, where the interaction between model capacity and data might be different from dense models.

### Questions
- What is the exact pruning method being used in the iterative pruning phase? A detailed description of the pruning criteria could be helpful for the audience to understand (e.g., structured/unstructured pruning and how is the pruning decision being made)
- $\bar{N}$ and $D$ are independent variables shown in equation (2), however, there seems no analysis in this paper showing that the effects of $\bar{N}$ and $D$ bring to the model's evaluation loss are independent.

### Soundness
4

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
This paper investigates sparse pre-training as an alternative to post-training pruning for large language models (LLMs) and proposes a modified scaling law based on the average active parameter count. Through extensive experimentation with over 80 configurations, the authors claim that sparse pre-training can yield models with similar performance to dense pre-training, offering a more efficient approach by beginning with dense training and progressively sparsifying. However, due to limitations in hardware and software, the paper lacks direct evidence of computational savings, which is a primary motivation for sparse pre-training.

### Strengths
+ Modifying the Chinchilla scaling law to consider average active parameters is a novel approach, bridging dense and sparse pre-training frameworks effectively
+ The study evaluates a wide array of configurations and sparsity schedules, providing a thorough analysis of optimal sparse pre-training practices

### Weaknesses
 - Despite the theoretical focus on efficiency, the paper lacks a demonstration of actual computational savings due to the current limitations in sparse matrix support in hardware/software, which could weaken the case for real-world applicability
- The study uses evaluation loss as the sole metric, without investigating the effects on real-world downstream tasks. This limits the ability to gauge the model’s practical effectiveness or generalization capabilities
- The framework’s reliance on finely tuned, phase-specific compute allocations (dense, pruning, recovery) introduces implementation complexity, which could be challenging to replicate or scale, particularly in resource-constrained environments

### Questions
See weakness

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
4

### Summary
The paper studies the scaling law for pretraining sparse language models. It argues that sparse pretraining reduces both pretraining and inference costs since the final model can be smaller and requires less computation during inference. The authors modify the Chinchilla scaling law for dense models to use the average number of active parameters (receiving gradients) in training. The modified scaling law unifies both sparse and dense models.  They also conduct extensive studies to search for optimal sparse pretraining configurations for LLMs. The key findings include pruning starting at 25% and ending at 75% obtains near optimal final eval loss, optimal learning rates, and batch sizes for sparse training match dense models under the same compute budget. The paper further provides both theoretical justifications and empirical validation for the scaling law and presents a simple recipe for sparsely pretrained models.

### Strengths
- The paper studies an interesting research problem, the scaling law for pretraining sparse models. It develops a modified scaling law that unifies both dense and sparse models. 
- The analysis and empirical validation are solid and convincing. The findings are supported by both theoretical justifications and experiments over 80 sparse pretraining configurations. The optimal settings for pretraining sparse models provide valuable practical lessons.
- The paper itself is well-written, clearly structured, and easy to follow.

### Weaknesses
 - One major concern is that the scaling law for dense models seems to have less impact, especially given that generally more data and compute resources are better to obtain better and more capable LLMs, LLaMA 2 and LLaMA 3 papers provide such evidence. How would unifying the scaling law for both dense and sparse models be useful under such a context?
- The paper mainly focuses on LLaMA style model architecture for sparse pretraining, any discussion on other sparse architectures like the mixture of experts (MoE)? Otherwise, it may be a bit overclamied. 
- The other concern is that previous scaling laws at least study model parameters with 1B scale, but this paper only discusses models under 500M parameters, making the claim of scaling law for LLM weaker. 
- While the paper acknowledges the limitation of evaluation loss, it would be very useful to report the performance numbers of downstream tasks, especially given the size of models is small. No compute limitation prohibits such evaluation.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
