# GatedMTL: Learning to Share, Specialize, and Prune Representations for Multi-task Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Jointly learning multiple tasks with a unified model can improve accuracy and data efficiency, but it faces the challenge of task interference, where optimizing one task objective may inadvertently compromise the performance of another.
A solution to mitigate this issue is to allocate task-specific parameters, free from interference, on top of shared features. However, manually designing such architectures is cumbersome, as practitioners need to balance between the overall performance across all tasks and the higher computational cost induced by the newly added parameters.
In this work, we propose \textbf{\methodname}, a novel MTL architecture designed to mitigate task interference while optimizing inference computational efficiency.
We employ a learnable gating mechanism to automatically balance the shared and task-specific representations while preserving the performance of all tasks.
Crucially, the patterns of parameter sharing and specialization dynamically learned during training, become fixed at inference, resulting in a static, optimized MTL architecture.
Through extensive empirical evaluations, we demonstrate SoTA results on three MTL benchmarks using convolutional as well as transformer-based backbones on CelebA, NYUD-v2, and PASCAL-Context.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The focus of this work is to address the problem of task interference in multitask learning (MTL), which manifests as the negative effect that learning a task may have on another one when trained together. To this end, the authors propose a new soft parameter-sharing framework coined GatedMTL, which effectively consists of an automatic mechanism by which a series of identical task-specific architectures learn to share a mixture of their features during training, while retaining task-specific parameters when needed. The authors also propose to use sparsity regularization to encourage sharing parameters and reduce compute. Finally, empirical results on convolutional and transformer based models show that the proposed architecture is able to successfully explore the performance vs. compute trade-off, outperforming the chosen baselines in that matter.

### Strengths
- The paper is well-written, and the proposed solution is super intuitive and easy to understand.
- The emphasis on performance vs. flops (or size) is rather refreshing to read.
- The number of experiments variety is impressive for what is usual in the field, and it is nice to see a discussion and empirical evaluation of negative transfer and backbone size.
- The authors propose GatedMTL for two fairly widespread architectures, and the empirical results are quite positive.

### Weaknesses
 
**Limitations**
- W1. The biggest problem I have with the manuscript is that it does not discuss or show the limitations of the proposed approach _at all_, which can really easily mislead the readers (and thus, the reviewers). For example, to my understanding, the proposed approach at training time is $T$ individual models that are trained altogether. However, this is a _huge_ setback as it scales poorly with $T$ in memory and time (for example, the usual CelebA setting in MTL is to do a 40-task binary classification, but the authors reduce it to 3 tasks). The authors should discuss it in the manuscript and show training times for each of the experiments. The claim that training time is comparable to other methods needs strong empirical support, especially when reducing the number of tasks so drastically compared to common benchmarks. The lack of a thorough analysis on how the method scales with the number of tasks is a major concern.
- W2. The hyperparameters $\tau_t$ are hardly intuitive, and the recommendation is to i) use the gap between STL and MTL models, and to ii) study the distribution of the gating patterns wrt the shared branch. The former requires tuning and training $T+1$ models, whereas the latter requires carefully looking into the model parameters. I am afraid that this can really hurt the adoption of the model by practitioners. The interpretation of $\tau$ as a 'target rate' is still not practical for users. It's unclear how this relates to the actual percentage of task-specific parameters, and the need to analyze activation distributions or train single-task models makes it even less intuitive. The parameter should have a direct and easily understandable meaning for practical tuning.

**Presentation**
- W3. Citations should properly use `\citet` and `\citep`. Even worse, the bibliography is a mess and I cannot comprehend how it happened (and I am going to assume, in good faith, that LLMs have nothing to do). The ones I spotted:
	- Kendall's citation is doubled (and with different years).
	- The citations **in the same paragraph of the manuscript** for DWA and MTAN (proposed in the same paper) are different. And again, different years. This is mind-blowing to me.
	- The paper by Maninis is also doubled.
	- The paper by Javaloy & Valera is from ICLR 2022, not 2021.
	- GradNorm is cited as arxiv 2017 when it is published at ICML 2018.
	- Adashare's paper has no venue.
	- Most urls point to semanticscholar instead of the official venue.

**Experiments**
- W3. I find $\Delta_{\text{MTL}}$ a brittle metric, as it is sensitive to low-magnitude metrics and task metrics are not comparable. I would add a more robust metric like the rank mean (see, e.g., [1]). 
- W4. The chosen baselines are inconsistent across experiments and mostly outdated. From the MTO side, DWA and Uncertainty are quite old and weak in comparison with other methods like PCGrad, CAGrad, or NashMTL. From the side of adaptive architectures, more modern approaches like Adashare should be included.

### Questions
- Q1. Do you use a different Lagrange multiplier for each task when using L1 regularization? Otherwise, I don't see how it is comparable to the hinge loss in Eq. 4.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript proposes a new Multi-Task Learning (MTL) framework called *GatedMTL* that learns the optimal balance between shared and task-specific representations for a given computational budget. It uses a gating mechanism to learn a combination of shared and task-specific features for each task in each layer. Unused features and weights are pruned during inference to improve sparsity and efficiency. The framework generalizes to convolutional backbone and transformer-based backbone. Experiments on CelebA, NYUD-v2, and PASCAL-Context datasets demonstrate the proposed method maintains a favorable balance between compute costs and multi-task performance across computational budgets.

### Strengths
*Originality*: This work introduces a multi-head gating mechanism into feature transformation, solving the challenge of multi-task learning with an emphasis on computational efficiency. 

*Quality*: The experiments are extensive. 

*Clarity*: The paper is written clearly, and the figures are easy to understand.

*Significance*: The problem that this work attempts to address is important. Given the computational budget, the performance improvement is obvious.

### Weaknesses
W1: No source code is provided. Although the experimental setup is detailed and the results are extensive, it is still necessary to provide the code for reference and reproducibility checking.

W2: Since a shared feature branch acts like a memory bank where task-specific features can communicate, a task-specific gate still learns features from other tasks, which can cause task interference.

W3: The reported performance in each table is based on a single run. The standard deviation based on multiple random runs is highly encouraged to be provided.

### Questions
Q1: What is the purpose of the "convolution block" in forming the shared feature map of the next layer (line 1, page 4)? 

Q2: A more detailed description of the changes made to the backbone is needed for the implementation of the gated MLT layer.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a GatedMTL framework for MTL.  GatedMTL aims to address the fundamental challenges of task interference and computational constraints in MTL. Specifically, a learnable gating mechanism is used to select and combine channels from its task-specific features and a shared memory bank of features. In addition, the gates are regularized to learn the optimal balance between allocating additional task-specific parameters and the model’s computational costs. The proposed method is evaluated on datasets and the experiment results also achieve comparable performance. However, the contribution of this GatedMTL seems marginal and the results are not very strong.

### Strengths
1) The proposed GatedMTL method to assign features to either a task-specific or shared branch, until reaching an adjustable target computational budget.
2) Experiment results demonstrate competitive performance.
3) Easy to understand.

### Weaknesses
1) The core idea of this paper is to find a parameter to control the ratio of task-specific features to task-shared features. The motivation of the gating design for MTL is not clear. The gating mechanism is not a new story in MTL. Specifically, the paper lacks a clear explanation of why a gating mechanism is superior to other methods for balancing task-specific and shared features, such as simple parameter sharing or adaptive weighting schemes. The novelty of the gating approach in this context is not well-justified, especially given the existing literature on gating mechanisms in other domains.
2) The gating module to balance task-specific features and the shared features in the decoder seems a bit more reasonable. Since the encoder is responsible for encoding out the shared features across all tasks, it doesn't seem to make sense to split out the task-specific features in the encoder. The paper does not adequately address why the encoder is the appropriate location for introducing task-specific gating, especially given that the encoder's primary function is to extract shared representations. This design choice raises questions about the potential for disrupting the shared feature space and whether a decoder-based gating mechanism might be more effective.
3) The proposed gating mechanism seems similar to a simplified variant of smooth Gating in DSelect-k[R1]. It is not possible to observe from Eqs. 2 and 6 that there is a point of novelty in the gating of this paper. The paper fails to clearly articulate the differences between the proposed gating mechanism and existing approaches, particularly in terms of the mathematical formulation and the practical implications for multi-task learning. A more detailed comparison is needed to highlight the unique aspects of the proposed method.
4) The authors are encouraged to show comparisons of feature changes before and after the addition of gating through visualization. In addition, how to show task-specific features and shared features. Can these two features be displayed through visualization? The paper lacks a qualitative analysis of the feature representations learned by the model. Visualizations of feature maps or embeddings could provide valuable insights into how the gating mechanism affects the learned representations and whether it effectively separates task-specific and shared features. Without such visualizations, it is difficult to assess the true impact of the proposed method.
5) The results in Table 1 were confusing to the reviewers, who could not see directly from the table how the five GatedMTLs are differentiated. The other tables have the same confusion. The presentation of results is unclear, making it difficult to understand the specific configurations and performance of the different GatedMTL variants. The paper needs to provide more detailed explanations of the experimental setup and the differences between the reported results.
6) Why are the results for Auto-λ not shown in Tables 3 and 4?

### Questions
1) The gating module to balance task-specific features and the shared features in the decoder seems a bit more reasonable. Since the encoder is responsible for encoding out the shared features across all tasks, it doesn't seem to make sense to split out the task-specific features in the encoder. Have the authors considered this?
2) Minor error:
$\Delta_{MTL}$ and $\Delta$ denote the same metric. The authors are encouraged to keep them consistent.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel multi-task learning (MTL) framework, GatedMTL, to address the fundamental challenges of task interference and computational constraints in MTL. GatedMTL learns the optimal balance between shared and specialized representations by leveraging a learnable gating mechanism to allow each task to select and combine channels from its task-specific features and a shared memory bank of features. Moreover, a regularization term is used to learn the optimal balance between allocating additional task-specific parameters and the model’s computational costs. Extensive empirical evaluations are conducted.

### Strengths
1. This paper proposes a novel multi-task learning (MTL) framework to address the fundamental challenges of task interference and computational constraints in MTL.
2. Extensive empirical evaluations are conducted.

### Weaknesses
1. The code is not provided.
2. The description of the proposed method in Section 3 and the overall framework in Figure 1 are confusing. If my understanding is correct, the proposed method is very similar to the existing MoE-base MTL methods. However, this paper does not discuss and compare with MoE-based MTL methods.
3. The proposed method uses the single-task weights for initialization, which means it needs to train $T$ single-task models before training the proposed method, and it is unfair to compare with the baselines which do not use the information from single-task models.

See the next Questions part for details.

### Questions
**Major Concerns**:
1. The description in Section 3 and Figure 1 are confusing. Is the encoder in Figure 1 shared among different tasks? Does $\Psi$ denote the shared encoder in Figure 1? If so, which part in Figure 1 is $\Phi_t$, and how can we obtain the shared and task-specific features at each layer? Are there $T+1$ encoders where one is $\Psi$ shared among different tasks and the others are task-specific $\Phi_t$? If so, what is the difference between the proposed GatedMTL and MoE-based MTL methods like [1, 2, 3, 4, 5]?
2. How to choose $\omega_t$ in Eq. (1)?
3. In the last paragraph of Section 4.1: "the task-specific branches are with their corresponding single-task weights". It means we need to train $T$ single-task models before training the proposed GatedMTL, which causes a huge computational cost in the training process. 
4. "for a given computational budget" in the abstract and "matching the desired target computational cost" in the second contribution. What is the "given computational budget" or "desired target computational cost"? Is it $\tau_t$ in Eq. (4)? However, $\tau_t$ represents neither parameter size nor flops. Besides, although both $\lambda_s$ and $\tau_t$ can control the trade-off between performance and computational cost, the sparsity regularization cannot be guaranteed to be optimized to $0$.
5. Why not report and compare the parameter size? It is very important in multi-task learning.
6. Many recent or important baselines are missing. For example, MoE-based MTL methods like [1, 2, 3, 4, 5] and MTO approaches like [6, 7, 8].


**Minor Concerns**:
1. $\odot$ in Eqs. (2), (3), (6), (7), and (8) is not defined.
2. Next line of Eq. (3): $R$ should be $\mathbb{R}$.
3. $\beta^l$ is a learnable parameter, but it does not appear in the overall training objective Eq. (5).
4. $(\tau_t)\_{t=1}^T$ should be $\\{\tau_t\\}\_{t=1}^T$. 
5. Some references appear twice, such as "Multi-task learning using uncertainty to weigh losses for scene geometry and semantics.", "End-to-end multi-task learning with attention.", "Auto-lambda: Disentangling
dynamic task relationships.", and "Attentive single-tasking of multiple tasks.".

----
[1] Modeling Task Relationships in Multi-task Learning with Multi-gate Mixture-of-Experts. KDD, 2018.

[2] Progressive Layered Extraction (PLE): A Novel Multi-Task Learning (MTL) Model for Personalized Recommendations. RecSys, 2020.

[3] DSelect-k: Differentiable Selection in the Mixture of Experts with Applications to Multi-Task Learning. NeurIPS, 2021.

[4] Deep Safe Multi-Task Learning. arXiv:2111.10601v2.

[5] MSSM: A Multiple-level Sparse Sharing Model for Efficient Multi-Task Learning. SIGIR, 2021.

[6] Multi-Task Learning as Multi-Objective Optimization. NeurIPS, 2018.

[7] Conflict-Averse Gradient Descent for Multi-task Learning. NeurIPS, 2021.

[8] Reasonable Effectiveness of Random Weighting: A Litmus Test for Multi-Task Learning. TMLR, 2022.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
