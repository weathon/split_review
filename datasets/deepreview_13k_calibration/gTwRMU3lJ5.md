# LoRA-Pro: Are Low-Rank Adapters Properly Optimized?

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
Low-rank adaptation, also known as LoRA, has emerged as a prominent method for parameter-efficient fine-tuning of foundation models.
Despite its computational efficiency, LoRA still yields inferior performance compared to full fine-tuning.
In this paper, we first uncover a fundamental connection between the optimization processes of LoRA and full fine-tuning: using LoRA for optimization is mathematically equivalent to full fine-tuning using a low-rank gradient for parameter updates.
And this low-rank gradient can be expressed in terms of the gradients of the two low-rank matrices in LoRA.
Leveraging this insight, we introduce LoRA-Pro, a method that enhances LoRA's performance by strategically adjusting the gradients of these low-rank matrices.
This adjustment allows the low-rank gradient to more accurately approximate the full fine-tuning gradient, thereby narrowing the performance gap between LoRA and full fine-tuning.
Furthermore, we theoretically derive the optimal solutions for adjusting the gradients of the low-rank matrices, applying them during fine-tuning in LoRA-Pro.
We conduct extensive experiments across natural language understanding, dialogue generation, mathematical reasoning, code generation, and image classification tasks, demonstrating that LoRA-Pro substantially improves LoRA's performance, effectively narrowing the gap with full fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
LoRA reduces the parameters required during training by introducing a low-rank matrix, thereby reducing computational requirements and memory footprint while maintaining model performance. This paper introduces LoRA-Pro to enhance LoRA’s performance by strategically adjusting the gradients of the two low-rank matrices, allowing the low-rank gradient to more accurately approximate the full fine-tuning gradient.

### Strengths
In this paper, the optimal solution of adjusting the gradient of low rank matrix is deduced theoretically and applied to the fine tuning process of LORA-PRO, which narrows the performance gap between LoRA and full fine tuning. Extensive experiments in multiple tasks have been carried out to prove that LORA-Pro greatly improves the performance of LoRA.

### Weaknesses
1. The method is not applied to the latest LLMs.
2. LoRA-Pro brings in extra memory cost and computation cost in the training.
3. It is not clear why the optimal gradients for the low-rank matrices do not explicitly depend on the full fine-tuning gradient.

### Questions
•	Please explain why LoRA-Pro is much better than Full FT in Table 3. Is there overfitting phenomenon that gives LoRA-Pro an advantage on these specific tasks?
•	Please explain why the training speed of LoRA-Pro is slightly worse than LoRA and much better than Full FT in Table 5. It will be better to provide a breakdown of the additional operations required by LoRA-Pro compared to standard LoRA, and to quantify the overhead in terms of FLOPs
•	Please provide more choices of X in Table 4.   For example, the analytical solution of X can be calculated in Theorem 2.1. 
•	LoRA-GA[1] has the same purpose as the work in this paper. Please discuss how LoRA-Pro differs conceptually or methodologically from LoRA-GA and supplement the results of LoRA-GA in Table 3 and Table 5.
•	If available, please add discrepancy curves between the low-rank equivalent gradient and the full fine-tuning gradient. Please supplement the training loss curves to illustrate the convergence rate of the proposed method.

[1]Wang S, Yu L, Li J. LoRA-GA: Low-Rank Adaptation with Gradient Approximation[J]. arXiv preprint arXiv:2407.05000, 2024.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors show that demonstrating that optimizing with LoRA is mathematically equivalent to performing full fine-tuning using a low-rank gradient for updates. They introduce a novel parameter-efficient fine-tuning (PEFT) method named LoRA-Pro, which minimizes the divergence between the true gradient and the low-rank gradient by adjusting the gradients of matrices A and B. The authors provide theoretical proof of the optimal gradients and detail the optimization process utilizing these gradients. They conduct extensive experiments across various tasks, including natural language understanding, dialogue generation, mathematical reasoning, code generation, and image classification, showcasing the effectiveness of their proposed method.

### Strengths
- The motivation is clearly articulated, and the paper is well-written with well-explained ideas.

- The proposed method enhances LoRA, a highly relevant technique for fine-tuning, in a straightforward manner, supported by both theoretical proofs and experimental evidence.

- The experiments and ablation studies are thorough, demonstrating the effectiveness of the proposed method across diverse settings.

### Weaknesses
 - The authors conducted all experiments for the different methods (for a given task) using the same learning rates. However, this approach may not provide a fair representation of optimal conditions, as the selected learning rate could work well for one method but not for others. To strengthen their findings, it would be beneficial for the authors to perform a learning rate sweep for each method. If this is too resource-intensive for all datasets, they might consider limiting the sweep to a single task, which would further increase confidence in the effectiveness of their proposed method.

- It would be interesting to explore how the equivalent gradients differ from the low-rank gradients in LoRA. A quantitative analysis could provide valuable insights into this relationship. For instance, how does the difference between these gradients vary across different models, deeper layers, and various types of weights? Conducting such a study could yield interesting findings, and further strengthen the motivation behind the gradient adjustment.

Minor:

- Please provide metrics for the datasets used in Table 1. I believe not all metrics used are “Accuracy”. For instance, CoLA typically usually uses Matthews Correlation Coefficient - kindly specify for all datasets.
- How exactly is the *efficient* mode less stable than the *full* mode? To clarify, all the results in the main paper are derived using the *efficient* mode, is that correct?

### Questions
- It would be interesting to explore how the equivalent gradients differ from the low-rank gradients in LoRA. A quantitative analysis could provide valuable insights into this relationship. For instance, how does the difference between these gradients vary across different models, deeper layers, and various types of weights? Conducting such a study could yield interesting findings, and further strengthen the motivation behind the gradient adjustment.

Minor:

- Please provide metrics for the datasets used in Table 1. I believe not all metrics used are “Accuracy”. For instance, CoLA typically usually uses Matthews Correlation Coefficient - kindly specify for all datasets.
- How exactly is the *efficient* mode less stable than the *full* mode? To clarify, all the results in the main paper are derived using the *efficient* mode, is that correct?

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
The paper introduces LoRA-Pro, a novel method aimed at improving the performance of LoRA in fine-tuning foundation models. LoRA-Pro enhances LoRA by adjusting the gradients of low-rank matrices to better approximate the full fine-tuning gradient. The paper establishes a mathematical equivalence between LoRA and full fine-tuning, and uses this insight to optimize LoRA's performance. Extensive experiments across various tasks demonstrate that LoRA-Pro substantially narrows the performance gap between LoRA and full fine-tuning.

### Strengths
- The paper presents a novel approach by mathematically linking LoRA with full fine-tuning through gradient adjustments.
- The theoretical foundation is robust, with clear derivations and optimal solutions provided for gradient adjustments. The experiments are comprehensive, covering multiple domains such as language understanding, dialogue generation, mathematical reasoning, and image classification.
- The paper is well-organized.

### Weaknesses
 - It will be better to test LoRA-Pro in real large models (e.g., 70B).


### Questions
- Do LoRA-Pro have some failure cases? (e.g., potential limitations or edge cases where LoRA-Pro might not perform as well)

### Soundness
4

### Presentation
3

### Contribution
4
