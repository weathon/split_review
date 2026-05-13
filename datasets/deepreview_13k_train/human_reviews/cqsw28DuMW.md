# TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Causal language models have demonstrated remarkable capabilities, but their size poses significant challenges for deployment in resource-constrained environments. Knowledge distillation, a widely-used technique for transferring knowledge from a large teacher model to a small student model, presents a promising approach for model compression.
A significant remaining issue lies in the major differences between teacher and student models, namely the substantial capacity gap, mode averaging, and mode collapse, which pose barriers during distillation.
To address these issues, we introduce $\textit{Temporally Adaptive Interpolated Distillation (TAID)}$, a novel knowledge distillation approach that dynamically interpolates student and teacher distributions through an adaptive intermediate distribution, gradually shifting from the student's initial distribution towards the teacher's distribution. We provide a theoretical analysis demonstrating TAID's ability to prevent mode collapse and empirically show its effectiveness in addressing the capacity gap while balancing mode averaging and mode collapse.
Our comprehensive experiments demonstrate TAID's superior performance across various model sizes and architectures in both instruction tuning and pre-training scenarios. Furthermore, we showcase TAID's practical impact by developing two state-of-the-art compact foundation models: $\texttt{TAID-LLM-1.5B}$ for language tasks and $\texttt{TAID-VLM-2B}$ for vision-language tasks.
These results demonstrate TAID's effectiveness in creating high-performing and efficient models, advancing the development of more accessible AI technologies.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes TAID, introducing a temporally adaptive interpolation between the student and teacher distributions. The interpolation is upon relative change in the objective function. Numerical experiments over instruction tuning and pretraining stage well demonstrated the efficacy of TAID.

### Strengths
- The paper is well motivated, written well and easy to follow.

- The numerical experiments are comprehensive to well show the effectiveness of TAID.

### Weaknesses
 - The technical contribution feels somewhat limited, primarily focusing on the difference between TAID and Skew KLD through the proposed temporal adaptive interpolation mechanism. This design choice, however, appears heuristic in nature. Given that multiple adaptive mechanisms could potentially meet the provided criteria, it would be helpful for the authors to elaborate on why this particular format was chosen for the adaptive mechanism. Providing additional rationale or theoretical support would strengthen the justification for this approach and enhance the perceived novelty of the contribution.


### Questions
See the weakness.

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
5

### Summary
The paper focuses on improving the distillation procedure for LLMs and VLMs. It discusses the student-teacher distribution mismatch in standard distillation and identifies two crucial problems: the capacity gap and mode averaging/collapse. A novel approach based on time-dependent corrections to intermediate teacher distributions is proposed.
The method is compared to other techniques in the LLM setting, showing superior results. Finally, the paper presents results for distillation in both LLMs and VLMs.

### Strengths
- The problem formulation is well done. The paper discusses issues with current KD, identifies two specific problems, and addresses them effectively, creating a compelling narrative.
- The paper addresses both LLM and VLM distillation.
- The approach is straightforward, which is a strength. It requires adjusting only a single hyperparameter.
- The resulting models demonstrate state-of-the-art (SOTA) performance compared to models in the literature, as shown in Tables 4 and 5.

### Weaknesses
1. The results in Table 2 show that TAID performs very similarly to standard KL. They also indicate that other techniques underperform compared to KL. It is unclear if this is due to implementation or if it highlights a limitation of the method in the pre-training scenario. The paper should provide a more detailed analysis of why other methods underperform in this setting, especially given that standard KL is a strong baseline.
2. The authors discuss the capacity gap and mode collapse in standard distillation. Is there any experimental evidence of this for LLM and VLM cases? Specifically, the paper should include quantitative analysis of the student's probability distribution, showing how it differs from the teacher's and how TAID mitigates these issues. For example, visualizations of the probability mass distribution or entropy analysis could be beneficial.
3. The paper claims to outperform all other distillation techniques. An analysis comparing the differences in loss functions between methods would be important to support this claim and to explain why the proposed approach is superior. This analysis should include a mathematical comparison of the gradients and how they affect the optimization process, not just a comparison of final performance.
4. For Tables 4 and 5, it is important to assess improvements by comparing them to standard cross-entropy (CE) loss training. This comparison is crucial to understand the actual benefit of the proposed distillation method over simply training the student model from scratch.

### Questions
1. It is known that top-k logit distillation aids knowledge distillation (KD). Did the authors conduct experiments involving this? By top-k, I mean applying KD only on the top 100/1000 neurons to reduce the capacity gap.
2. The approach potentially bears similarities to linearly increasing the loss weight during distillation via t. Any thoughts on this?
3. What does m represent in line 199?
4. Were the results in Table 1 computed by the authors using the same data and settings?
5. How would this approach compare to adjusting the learning rate during the distillation process? Could it have a similar effect?
6. Will the code be open-sourced?
7. Is it beneficial to combine this with cross-entropy (CE) loss? If so, what should the ratio be?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This method addresses key challenges such as the capacity gap between teacher and student models and issues like mode averaging and mode collapse during distillation. The core idea behind TAID is the introduction of an intermediate, dynamic distribution that gradually shifts from the student model’s distribution to the teacher’s, enabling a smoother and more effective transfer of knowledge. The authors provide both theoretical and empirical analysis, showing that TAID prevents mode collapse, enhances performance across different model sizes, and results in more efficient and high-performing LLMs.

### Strengths
1. **Adaptive Approach**: The use of a dynamic, time-dependent intermediate teacher distribution addresses the capacity gap effectively, making it easier to transfer knowledge between models of different sizes.

2. **Versatility**: TAID is effective across a variety of model sizes and tasks, including language-only and vision-language models, making it broadly applicable.

3. **Theoretical Perspective**: TAID’s approach is supported by solid theoretical analysis, proving its ability to prevent mode collapse and balance between mode averaging and collapse, which traditional KD methods often struggle with. However, I didn't check the detailed proof for the theorem.

### Weaknesses
1. Despite the basic concept of the objective function being very similar to Skew KL in DistiLLM, there is limited comparison between Skew KL and TAID. I am wondering if there is a reasonable analysis of the main differences between the Skew KL and TAID functions.


### Questions
1. Does TAID also hold for reverse KL divergence? Are there any results regarding this?

### Soundness
3

### Presentation
3

### Contribution
2
