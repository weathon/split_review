# Bilevel ZOFO: Bridging Parameter-Efficient and Zeroth-Order Techniques for Efficient LLM Fine-Tuning and Meta-Training

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Fine-tuning pre-trained Large Language Models (LLMs) for downstream tasks using First-Order (FO) optimizers presents significant computational challenges. Parameter-Efficient Fine-Tuning (PEFT) methods have been proposed to address these challenges by freezing most model parameters and training only a small subset. While PEFT is efficient, it may not outperform full fine-tuning when high task-specific performance is required.
Zeroth-Order (ZO) methods offer an alternative for fine-tuning the entire pre-trained model by approximating gradients using only the forward pass, thus eliminating the computational burden of back-propagation in first-order methods. However, when implementing ZO methods, it is crucial to ensure prompt-based text alignment, and relying on simple, fixed hard prompts may not be optimal. In this paper, we propose a bilevel optimization framework that complements ZO methods with PEFT to mitigate sensitivity to hard prompts while efficiently and effectively fine-tuning LLMs. Our Bilevel ZOFO (Zeroth-Order-First-Order) method employs a double-loop optimization strategy, where only the gradient of the PEFT model and the forward pass of the base model are required. We provide convergence guarantees for Bilevel ZOFO. Empirically, we demonstrate that Bilevel ZOFO outperforms both PEFT and ZO methods in single-task settings. Additionally, we show its strong potential for multitask learning. Compared to current first-order meta-training algorithms for multitask learning, our method has significantly lower computational demands while maintaining or improving performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper propose  Bilevel ZOFO, a framework combining PEFT and Zeroth-Order (ZO) optimization to improve fine-tuning and meta-training efficiency for large language models. Using a bilevel approach, it achieves better performance in single- and multi-task settings. 
It provides convergence guarantees for the optimization process.

### Strengths
Bilevel ZOFO effectively combines PEFT and ZO optimization to reduce computational and memory costs, making large model fine-tuning more efficient. 
Its bilevel structure allows for competitive performance in both single- and multi-task settings with theoretical convergence guarantees.

### Weaknesses
The experiments are limited to small- to medium-sized models in its experiments, raising concerns about scalability to larger models commonly used in practice and fair comparison.

Unlike MeZO that only require forward passes,  Bilevel ZOFO relies on First-Order gradient calculations, which can significantly increase computational and memory demands.
Minimax optimization often faces convergence problems due to saddle points, which can cause the training to stall and slow down overall progress.

### Questions
Q1 Could you provide quantitative evaluations for convergence, wall-clock time per step, memory profiling, and memory consumption, as seen in the MeZO paper?

Unlike MeZO that only require forward passes,  Bilevel ZOFO relies on First-Order gradient calculations, which can significantly increase computational and memory demands.
Minimax optimization often faces convergence problems due to saddle points, which can cause the training to stall and slow down overall progress. 


Q2 Could you provide the experimental results for larger models such as OPT13B.

ZO methods are particularly beneficial for reducing computational resources in large-scale model training. Thus, existing methods have generally evaluated models of at least moderate scale, such as models larger than OPT13B. The experiments in this paper, however, are limited to small- to medium-sized  models, up to 7B parameters.
To ensure a fair comparison with existing methods, it is essential to test on models of at least comparable size, such as OPT13B.
Effective hyperparameters may vary significantly based on model size.
However, MeZO tested in this paper may not necessarily be optimal for small-scale settings.
as existing methods are not designed with small-scale models.


Q3 Could you provide detailed experimental settings?
The MeZO paper provides detailed information on hyperparameters and computational environment, which is necessary for reproducibility and accurate comparison.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a bilevel optimization framework and combines zero-order finetuning with first-order PEFT to achieve higher performance on the downstream task. Experiments show that their proposed method outperformance both zero-order finetuning and PEFT only.

### Strengths
1. The proposed method is novel and interesting.
2. The experiment results look pretty strong compared to vanilla finetuning.

### Weaknesses
1. The motivation of this paper is unclear. The authors mention that with the bilevel optimization, the sensitivity of ZO to hard prompts can be mitigated. Are there any evidence for this claim? Or is the performance improvement simply comes from more tunable parameters?
2. Similar to point 1, have the authors done experiments with PEFT followed by a ZO finetuning?
3. The experiment section is a bit unclear, the MeZO baseline is not explained clearly.
4. For Tab. 3, it's not reasonable that the performance of stage 2 is much lower than the result from stage 1. The author should conduct basic hyperparameter tuning to make sure the result is reasonable or explain the counter-intuitive result.
5. Now I understand the MeZO baseline, but it seems the existence of MeZO weakens the novelty of this work.

### Questions
Please see the weaknesses above.

### Soundness
2

### Presentation
2

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
This paper realised two issues in current LLM tuning research. One is that parameter-efficient fine-tuning (PEFT) cannot sufficiently compete with full-model tuning, because only part of model parameters are tuned, which limits the model capacity. The second is that zeroth-order (ZO) optimization can tune full model parameters while relying on fixed non-optimal prompts. The authors propose to complement ZO with PEFT to mitigate the sensitivity to hard prompts through bi-level optimization. During formulation, they first transform the objective into single-level optimization problem and then use zeroth-order information to approximate gradient.

### Strengths
1. This paper presents a bi-level optimization method that is more suitable for tuning full pre-trained large language models, compared with parameter efficient tuning and zeroth-order tuning.
2. The proposed method can be extended to a lightweight meta-training process for multi-task learning.
3. The final results outperform both FO.and recent work MeZO.

### Weaknesses
1. I understand the motivation of complementing ZO with PEFT, but bi-level is known for its high computation cost, even after the zeroth-order approximation. In this sense, how is the tuning efficiency of the proposed method?
2.On line 201, you split data into two parts. Can the two-level optimization share the same tuning dataset?
3. From Eq.3 to Eq. 7, this process is following existing works. Any new technical contributions here? And have you demonstrated this transformation is better than others?
4. Efficiency comparision is lacked in experiments.
5. There are some improved LLM tuning works over MeZO. If this is not necessary to compare or even mention them, please provide the reasons.
6. Why not consider tuning soft prompts in this paper? As zeroth-order techniques are also explicitly used to tune prompts. [1]

### Questions
Please refer to Weaknesses.

The theoretical analysis presents the convergence of bi-level optimisation. It might be interesting for some readers but I doubt its significance in LLM tuning. For example, can you explain how will the convergence theory instruct the tuning process in real applications?

It would be better to draw a pipeline to show the optimization procedure, which can be left to appendix if not sufficient space.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a bilevel optimization method called Bilevel to efficiently finetune LLMs by combining PEFT and ZO optimization techniques. The motivation is to address the computational inefficiencies of traditional finetuning, which requires backpropagation and substantial memory. The primary research question centers on whether PEFT can enhance ZO fine-tuning for both single-task and multitask settings without requiring extensive computational resources. Bilevel ZOFO uses a two-level optimization framework that applies ZO for full model fine-tuning at the upper level and PEFT at the lower level to minimize computational cost while maintaining high performance. Experiments demonstrate that Bilevel ZOFO outperforms both individual ZO and PEFT methods on single tasks and achieves competitive results in multitask learning with reduced computational demand.

### Strengths
The paper has several major strengths:

1. Bilevel ZOFO is effectively extended to multitask learning scenarios, allowing models to handle multiple tasks simultaneously. This is beneficial in resource-limited environments where large, labeled datasets are scarce, such as in medical domains.

2. The paper provides theoretical guarantees for the convergence of the Bilevel ZOFO method.

3. Empirical results demonstrate that Bilevel ZOFO consistently outperforms both standalone ZO and PEFT approaches in single-task finetuning, and it is competitive with SOTA meta-learning methods for multitask scenarios.

### Weaknesses
The weaknesses of this paper are as follows:

1. The mathematical notations can be further improved to follow the convention. For example, when denoting a vector, usually bold font is preferred, such $\boldsymbol{\theta} \in \mathbb{R}^d$ instead of $\theta \in \mathbb{R}^d$. This helps the reader differentiate vectors from scalars and improves readability.

2. Typo at the end of line 269 "Sso" should be 'So'

3. In Eq. 2, I am not fully convinced why we need to train the PEFT module p and the base model parameter $\theta$ at the same time? Wouldn't avoiding training $\theta$ be the motivation for using PEFT modules?

4. The motivation for using ZO method in Algorithm 2 is not very clear to me. You may notice that as long as you need to do backpropagation, even if it is parameter efficient finetuning, the computational graph of all the network (from shallow to deep layers) should all be stored and thus, the memory consumption is still very high. Wouldn't this contradict the motivation for using ZO method? Why wouldn't the authors use ZO method throughout the algorithm, namely, use ZO method to calculate the gradient of the PEFT modules as well. 

5. As a follow-up question of 4, this paper does not report the efficiency comparison of any method. Specifically, the memory consumption, time consumption, and the convergence speed should be carefully measured and reported. I am afraid that the combination of ZO and PEFT in a way presented in this paper would harm the efficiency of both methods.

### Questions
Please see my questions in the weakness column.

### Soundness
3

### Presentation
3

### Contribution
3
