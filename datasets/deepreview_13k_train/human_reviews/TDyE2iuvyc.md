# Efficient Model Editing with Task-Localized Sparse Fine-tuning

- Decision: Accept
- Scores: 5, 6, 5, 6

## Abstract
Pre-trained models are stepping stones for modern machine learning systems, but how to efficiently extract, reuse, and steer their knowledge for new tasks is an area of research with still several open questions. State-of-the-art Task Arithmetic solutions are strongly tied to model linearization which leads to computational bottlenecks during training and inference, and potentially neglect essential task dependencies. In this work, we focus on the fine-tuning stage that defines task vectors and propose TaLoS, a new approach based on sparse fine-tuning that strategically updates only parameters expected to provide functional task localization. This efficiently yields weight-disentangled models without the need for explicit linearization. We present a thorough experimental analysis showing how our approach significantly improves in training and inference efficiency while outperforming state-of-the-art approaches in task addition and task negation. Our work offers a principled solution to pre-trained model editing and paves the way to more cost-effective and scalable machine learning systems for real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a novel fine-tuning strategy based on sparsity that is designed explicitly to facilitate merging a posteriori. The proposed method first identifies a per-task parameter mask that actively promotes weight disentanglement and is used during fine-tuning to constraint the parameter updates only to those in the mask. The method includes vision and NLP benchmarks for task addition and negation as well as weight disentanglement plots which are common in the literature

### Strengths
1. The motivation of the paper is clear and the writing is easy to follow
2. The method is simple and intuitive.
3. The performance is superior compared to the closest baselines in both task addition and negation, highlighting the importance of sparsity for task localization and the effectiveness of the method.
4. The experiments on mask calibration are interesting, e.g. Figure 4. and showcase that the method clearly identifies a pattern in the weights of the model.

### Weaknesses
The paper has several flaws that, if addressed, can improve the paper significantly. Specifically:


1.  The applicability of the method is undermined by the fact that the user needs to redo the fine-tuning from scratch. This limits its practical use with the vast number of pre-trained models already available. The method does not allow for the use of existing fine-tuned checkpoints, requiring a complete retraining process.
2.  Mask construction part of the algorithm is not clear: L236 refers to $\mathbf{x}$ but it is not clear if the process involves a single batch or not. The reader needs to go to Algorithm 1 of the appendix to find that multiple “rounds” are used. Both the algorithm and the term “rounds” are never mentioned in the main text. Thus, the reader cannot understand the computational overhead of the method and the assumptions on task availability. The number of rounds and iterations within each round, which significantly impact the computational cost, are not discussed in the main text.
3.  The level of mask sparsity is not mentioned on the paper, while it is a major part of the algorithm, apart from the caption of figure 4. It is not clear if 90% is used throughout. Constraining the fine-tuning process too much will result in worse single-task performance (before merging), limiting the method’s applicability. This is an important hyperparameter of the method and it is not discussed/ablated. Moreover, the absolute fine-tuned results should also be given. This is especially important given that fine-tuning in the tangent space “may cause single task performance drop” (L118). The reader can only imply the difference in performance from Figure 3, where the proposed method achieves lower performance compared to some tasks such as SVHN, Cars and DTD. The paper should include a detailed analysis of the trade-off between sparsity and single-task performance.
4.  Logical jump in motivation. The paper includes a nice experiment for Figure 1, discussed in lines 208-226. However, this experiment focuses on the *zeroshot* and there is a logical jump on how and why this translates to the fine-tuned checkpoints. The paper would benefit from better explanation. The connection between the zero-shot sensitivity analysis and the fine-tuning process is not clearly established.
5.  Presentation of results is sometimes sloppy. For instance, T5-large Absolute: 77.31 > 76.20, making the +2.87 in the last row wrong. 
6.  Unfair comparison for task negation: all posthoc methods are designed for task addition, making the comparison unfair imo. this should be stated clearly. The paper should clarify that post-hoc methods are not designed for task negation and that this evaluation is an extension of their original purpose.
7.  Need rephrasing:
	1. “This inherent property of sparse finetuning increases the likelihood that the linearization condition will hold, effectively rendering explicit network linearization unnecessary.” This is not shown and should be framed as intuition rather than fact. The paper should provide empirical evidence or a more rigorous argument to support this claim.
	2. Contribution 1 needs to be rewritten and be more specific: the current version can be said for any model merging method.
8. Related work: apart from Fisher merging, the methods outlined in the model merging paragraph are proposed primarily for task addition and, therefore, should be merged with the task arithmetic paragraph. The authors should include a paragraph specific to fine-tuning specific for merging, as these are their baselines and most related works.

“Existing task arithmetic solutions are strongly tied to model linearization which leads to computational bottlenecks” → does this refer to tangent? task arithmetic/ties etc have no bottleneck

Minor comments:


1. L47: interference missing refs from ties and tall masks
2. L52: “is crucial for preventing interference” this does not seem like a correct characterization
3. L137-138: this is taken from [1], reference is missing. Moreover, equations 2 and 3 seem redundant
4. L194: fix notation of the subscript

### Questions
1. Can you explain the discrepancy in the normalized results in t5-small? TA is better at absolute compared to tall masks but much lower in normalized.
2. Table 3: why is non-linear ft forward-backward pass time so much more than the proposed method? Given that it does not have the masking of equation 7, shouldn't it be a lower bound to TaLoS? Also, where does the difference in peak memory usage come from? this would be the case if entire layers are excluded from the mask, saving space in optimizer states, but this is not explicitly mentioned.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a new approach for efficient model editing through Task Arithmetic, specifically using a method called Task-Localized Sparse Fine-Tuning (TaLoS). TaLoS differs from traditional linearization-based approaches by selectively updating only parameters with low gradients, reducing computational load while minimizing task interference. The proposed method enables precise task addition and removal across vision and NLP tasks and demonstrates high performance in experimental results. Additionally, TaLoS achieves a reduced memory footprint and runtime by avoiding explicit linearization, verified by extensive evaluations on computational cost.

### Strengths
- Novelty and Effectiveness: This work introduces a novel technique that improves computational efficiency by updating only parameters with low sensitivity while maintaining task separability. This approach significantly reduces the computational burden associated with linearization-based methods and is a valuable contribution in terms of efficiency.
- Empirical Performance: Experimental results demonstrate that TaLoS consistently outperforms baseline methods, including LoTA, across a range of tasks. As shown in Figure 4, TaLoS maintains high accuracy when adding tasks and minimizes the impact on target tasks when removing tasks, showcasing its robustness in task arithmetic.

### Weaknesses
 - Explanation of Task Interference: Regarding the sensitivity analysis in Figure 1, I understand that it evaluates the performance on other tasks when parameters with low gradients in a given task are pruned. However, could you provide a more detailed explanation on whether altering these selected parameters, rather than simply pruning them, would also have no impact on inference? For example, could you test whether applying extreme random changes to these parameters would still leave other tasks unaffected? This additional analysis would clarify the stability of these parameters across tasks.
- Key Concern: While intuitively, changing parameters with low sensitivity should not significantly affect the function for data drawn from task t , it is less clear why this would not affect other tasks post-finetuning. A detailed explanation of this phenomenon such as measuring the impact of these parameter changes on other tasks' performance or analyzing the overlap of low-sensitivity parameters across different tasks would strengthen the paper.

- Uniformity of Parameter Sensitivity
Regarding Figure 4, if the gradient norms are not uniform across layers, key parameters might differ across tasks. In this scenario, could the TaLoS approach risk inadvertently pruning important parameters? Could the authors provide further insights on this?

- Conditions for Task-Specific Parameter Pruning
Line 217 mentions that removing parameters deemed unimportant for a specific task does not degrade performance on other tasks. Could the authors clarify the specific conditions or limitations under which this holds? Insights into the effect of model size or architecture variations would also be beneficial.

- Pruning Criteria Unclarity
In Figure 1, the specific pruning criteria (e.g., values for bottom-k) were not readily apparent. Additional detail on this would enhance reproducibility.

### Questions
- Uniformity of Parameter Sensitivity
Regarding Figure 4, if the gradient norms are not uniform across layers, key parameters might differ across tasks. In this scenario, could the TaLoS approach risk inadvertently pruning important parameters? Could the authors provide further insights on this?

- Conditions for Task-Specific Parameter Pruning
Line 217 mentions that removing parameters deemed unimportant for a specific task does not degrade performance on other tasks. Could the authors clarify the specific conditions or limitations under which this holds? Insights into the effect of model size or architecture variations would also be beneficial.

- Pruning Criteria Unclarity
In Figure 1, the specific pruning criteria (e.g., values for bottom-k) were not readily apparent. Additional detail on this would enhance reproducibility.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes TaLoS, a novel sparse fine-tuning approach for efficient model editing in the task arithmetic framework. The key idea is to prevent interference between tasks by constraining updates to parameters that have low sensitivity across multiple tasks. By selectively fine-tuning only these parameters, the method aims to adapt models to new tasks while minimizing interference when performing task arithmetic operations.

### Strengths
- Novel approach combining sparse fine-tuning with task localization for improved task arithmetic

- Comprehensive empirical evaluation across vision and language tasks showing state-of-the-art performance

- Efficiency gains in both computation and memory usage compared to existing methods

- Detailed analysis of weight disentanglement and function localization properties

### Weaknesses
1. The caption for Figure 1 lacks clarity, particularly in explaining that "sensitivity" refers to gradient values. This makes the figure difficult to interpret without careful reading of the surrounding text.

2. The key algorithm and mechanism are not presented clearly. For example, there is a grammatical error in the sentence "To prevent interference between tasks and enable task arithmetic, prevents significant changes to the parameters that are highly sensitive to multiple tasks." This verbose phrasing obscures the core mechanism. Furthermore, the description in line 229, 'a procedure through which we constrain the parameters with the largest ∇θjf(x, θ0) to remain constant and update the only the ones where ∇θjf(x, θ0) ≈ 0.', is also unclear and needs further clarification.

3. The paper lacks theoretical analysis or proof of convergence for the proposed method. While empirical results are strong, a theoretical foundation would strengthen the work.

4. Equation 8 introduces parameter k as a significant factor in the upper bound, but there is insufficient discussion of its impact and optimal selection. A more comprehensive analysis of this parameter would be valuable. The results of the sparsity level search, which is a significant parameter in the setting, are also missing.

5. The direct relationship between gradient values and task interference is not thoroughly explored or justified theoretically. While intuitively reasonable, a more rigorous examination of this connection would bolster the method's foundation. The logic flow of this paper relies on the relationship between gradient values and task interference, and since this relationship has not been widely discussed, the logic is flawed.

### Questions
- Can the authors provide a clearer, more concise explanation of the core algorithm, perhaps with pseudocode?

- Is it possible to derive theoretical guarantees or convergence properties for the proposed method?

- How sensitive is the method to the choice of k, and are there principled ways to select its optimal value?

- Can the authors elaborate on the direct relationship between gradient magnitudes and task interference, ideally with theoretical justification?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Task-Localized Sparse Fine-Tuning (TaLoS), a novel approach to efficient model editing through sparse fine-tuning, aimed at enhancing task-specific performance in pre-trained models without explicit linearization. The method selectively updates parameters with minimal cross-task impact, achieving weight disentanglement and enabling efficient task arithmetic. Extensive experiments across vision and language domains demonstrate TaLoS's superiority over baseline methods in task addition/negation performance, computational cost, and memory efficiency.

### Strengths
+ The paper is well-written, with clear explanations of the motivation.
+ The empirical analyses offer valuable insights into the model’s behavior, which is interesting and well-reasoned.
+ The experiments are comprehensive.

### Weaknesses
 - Could the authors clarify further how TaLoS achieves linear behavior? The paper mentions that parameters unimportant for a given task are also generally unimportant for other tasks, which might imply a shared subset of parameters across tasks. It would be helpful if the authors provided experimental results showing parameter overlap across task vectors.
- It is unclear how the mask sparsity ratio is determined in practice. A sensitivity analysis of this hyperparameter might be valuable.
- I am curious about how this method might perform in combination with other model merging techniques, such as Ties-Merging or AdaMerging. Although such an investigation would require additional work, discussing this potential integration would be interesting.

### Questions
see weekness.

### Soundness
3

### Presentation
2

### Contribution
3
