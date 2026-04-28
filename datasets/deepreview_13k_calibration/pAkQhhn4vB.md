# Revisit Micro-batch Clipping: Adaptive Data Pruning via Gradient Manipulation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Micro-batch clipping, a gradient clipping method, has recently shown potential in enhancing auto-speech recognition (ASR) model performance.
However, the underlying mechanism behind this improvement remains mysterious, particularly the observation that only certain micro-batch sizes are beneficial.
In this paper, we make the first attempt to explain this phenomenon.
Inspired by recent data pruning research, we assume that specific training samples may impede model convergence during certain training phases.
Under this assumption, the convergence analysis shows that micro-batch clipping can improve the convergence rate asymptotically at the cost of an additional constant bias that does not diminish with more training iterations.
The bias is dependent on a few factors and can be minimized at specific micro-batch size, thereby elucidating the existence of the sweet-spot micro-batch size observed previously.
We also verify the effectiveness of micro-batch clipping beyond speech models on vision and language models, and show promising performance gains in these domains.
An exploration of potential limitations shows that micro-batch clipping is less effective when training data originates from multiple distinct domains.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper revisits micro-batch clipping, an optimization technique initially proposed for memory efficiency in differentially private stochastic gradient descent. The paper conceptualizes micro-batch clipping as a form of data pruning, proposing that certain "dragger" gradients impede model convergence. Through convergence analysis and empirical evaluation, the paper demonstrates that micro-batch clipping can asymptotically accelerate convergence but introduces a constant bias term. This bias term explains the existence of an optimal micro-batch size. The paper further validates the effectiveness of micro-batch clipping beyond speech models, showing promising results on vision and language tasks. However, limitations are identified when training data originates from multiple distinct domains.

### Strengths
1. Novel Conceptualization: The paper innovatively frames micro-batch clipping as a data pruning technique, introducing the concept of "dragger" gradients to explain its mechanism. This provides new insights into why and when micro-batch clipping works.
2. Comprehensive Analysis: The paper conducts both theoretical convergence analysis and extensive empirical evaluation to support its hypotheses. The results demonstrate the effectiveness of micro-batch clipping across different model architectures and datasets.

### Weaknesses
1. Lack of interpretability or robustness. This paper does not discuss the potential impact of micro-batch clipping on the interpretability or robustness of the trained models, which are important considerations in many real-world applications. Specifically, the paper lacks any analysis of how micro-batch clipping might affect adversarial robustness or the sensitivity of the model to input perturbations. Furthermore, the paper does not explore whether the pruning effect of micro-batch clipping leads to models that are more or less interpretable, for example, by examining feature importance or saliency maps.
2. Limited scope of experiments: The experiments are primarily conducted on speech recognition models and limited vision and language tasks. The generalizability of the findings to a broader range of models and datasets is unclear. More extensive experimentation across different domains and model architectures would strengthen the conclusions. For example, the paper should consider evaluating the method on more diverse datasets with varying levels of noise and complexity, as well as on models with different architectural characteristics, such as transformers or graph neural networks. The current selection of tasks and models is not sufficient to establish the broad applicability of micro-batch clipping.
3. Concern of memory overhead: While the paper mentions that data sharding with a micro-batch size equal to the per-core batch size can mitigate memory overhead, this may not be feasible for larger models. The growing size of modern models necessitates alternative solutions to ensure computational efficiency. The paper does not address the potential memory overhead when the micro-batch size is not equal to the per-core batch size, which could be a practical limitation in many scenarios. Additionally, the paper does not consider the impact of micro-batch clipping on the communication overhead in distributed training environments, which is a critical factor for large-scale model training.
4. Rigorous relationship between micro-batch size and performance: The paper suggests that there exists an optimal micro-batch size that minimizes the constant bias term in the convergence analysis. However, the relationship between the micro-batch size b and the factor c is not rigorously established. A tighter convergence bound and a more accurate relationship between b and c could better guide the choice of micro-batch sizes in practice. The paper provides no clear guidance on how to select the optimal micro-batch size for a given task or model, leaving this as a hyperparameter that requires extensive tuning.

### Questions
See Weaknesses.

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
Micro-batch clipping has recently demonstrated potential in improving model performance in automatic speech recognition (ASR). This paper seeks to uncover the mechanism driving this enhancement. The authors assume that certain data samples ("draggers") may impede model convergence. Through theoretical analysis, they find that micro-batch clipping can accelerate convergence by diminishing the impact of these draggers, albeit introducing a constant bias dependent on micro-batch size. This insight further explains the observed phenomenon where improvements occur only at specific micro-batch sizes. Additional empirical experiments are conducted beyond ASR to investigate the effectiveness of micro-batch clipping.

### Strengths
- Uncovering the mechanism behind the performance improvements brought by micro-batch clipping is both interesting and valuable.
- The paper provides a series of theoretical foundation to analyze this mechanism and support its conclusions.
- The theoretical findings in this paper can explain empirical results, such as the performance gains achieved through micro-batch clipping and why these improvements occur only at specific micro-batch sizes.
- Extensive experiments are conducted to explore the benefits of micro-batch clipping beyond ASR.

### Weaknesses
 - The Appendix of this paper is somewhat lost, and the full proofs of the theorems are thus invisible, requiring further verification.
- Assumption 4.4 posits that dragger gradients are orthogonal to the benign gradient subspace, which may be a restrictive assumption and not entirely realistic in practical scenarios. This orthogonality assumption, while simplifying the analysis, may not hold true in many real-world scenarios where dragger gradients could have components within the benign subspace. The impact of these non-orthogonal components on the convergence behavior is not addressed, potentially limiting the applicability of the theoretical results.
- In Sec.1, the authors claim that micro-batch clipping can adaptively suppress samples that hinder convergence. However, it remains somewhat unclear in the theorem whether the effectiveness of micro-batch clipping directly stems from suppressing these draggers. The theoretical analysis primarily focuses on the convergence rate bound, and it is not explicitly shown how the clipping operation directly reduces the influence of dragger gradients on the overall optimization process. The connection between the clipping operation and the suppression of draggers needs to be more clearly established.
- It appears that as $\epsilon$ decreases, approaching zero and indicating a lower likelihood of draggers, the convergence rate bound in Thm 4.2 actually increases, which seems counterintuitive. This behavior of the bound with respect to $\epsilon$ raises concerns about the practical implications of the theoretical results. A more detailed discussion on the limitations of the bound and its interpretation in the context of varying dragger probabilities is needed.

### Questions
Please refer to the weakness section.

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
4

### Summary
This paper presents a theoretical analysis of why the micro-batch clipping method, which has been shown to improve performance in automatic speech recognition (ASR) tasks, is only effective for specific micro-batch sizes. The authors first categorize mini-batch samples into benign samples and dragger samples, followed by a convergence analysis. This analysis provides an explanation of the sweet spot for micro-batch size. Finally, the paper demonstrates that micro-batch clipping is also effective in both vision and language tasks.

### Strengths
- The topic of theoretically analyzing the batch-size dependency issue of micro-batch clipping in training ASR models, which has shown empirical success, is both meaningful and interesting.

- Despite the mathematical rigor throughout the paper, the overall writing is easy to read and follow; in particular, both the content and proof of Theorem 4.1 are easy to understand.

- In the case of the ASR task, the paper presents promising empirical results that align well with the theoretical analysis.

### Weaknesses
 
**Methodology**
- Section 4.3 is significantly underdeveloped and requires more extensive elaboration. Expanding on this section with a detailed explanation of the method would improve clarity and depth.
  - In line 279, the paper states, “The proof can be found in ??,” but the proof is missing, and there is no supplementary material to refer to.
  - The proofs for Lemma 4.3 and Lemma 4.4 are also missing. Furthermore, in line 304, "The proof is provided in Appendix ??." mentions that the proof is in the appendix, but no appendix is provided in the paper.
  -  I suggest that the authors include these proofs in an appendix or supplementary material and ensure that all references to proofs are properly linked.

-  The samples that slow down convergence, termed "draggers," seem to refer not to those with gradients perpendicular to the benign samples, but rather those with gradients in the opposite direction (i.e., cosine similarity around -1); in Figure 1, there appear to be cases where benign samples have negative cosine similarity. Are there no samples with reverse gradient directions?

- As noted in the paper's limitations, determining the exact micro-batch size $b$ that achieves the "sweet spot" is a challenging task. This poses a significant empirical limitation, and even within the paper, the optimal micro-batch size changes due to various factors:
  - The best micro-batch size varies by modality; for example, the authors use a size of 4 for the speech task, 32 for the vision task, and 16 for the language task.
  - Additionally, memory constraints may impede the selection of the optimal micro-batch size. For the vision task, a micro-batch size of 32 was used per core, but such size may be difficult to adjust due to memory limitations.
  - I suggest the authors discuss potential strategies or heuristics for selecting micro-batch sizes in practice, considering the observed 
variability and memory constraints.

- Along with batch size, one of the most critical hyperparameters in training neural networks is the learning rate. Prior research has explored the relationship between batch size and learning rate [1].

- Is micro-batch clipping independent of mini-batch size, as opposed to micro-batch size? Further investigation into this relationship could be beneficial.

- While this paper analyzes micro-batch clipping in the context of SGD, in practice, SGD is rarely used for training neural networks. It is important to determine whether a similar theoretical analysis holds for modern optimizers like Adam.

- In Section 5.1, to fine-tune the model, the LibriSpeech dataset and handcrafted canaries were synthetically used as benign and dragger samples, respectively. However, this setup seems artificial. In a more realistic scenario where only the LibriSpeech dataset is used, how would dragger samples be detected in practice?  Including practical strategies for detecting draggers would add relevance to the findings.

**Experiments**
- In Tables 2 and 3, experiments were conducted with only batch sizes of 1, 4, and 512, which is insufficient. The authors should have included batch sizes such as 1, 4, 16, 64, 256, and 1024 to provide a more comprehensive evaluation. If these additional results are not feasible, explaining the rationale behind the specific batch sizes chosen would help clarify this decision.

- The analysis related to $|| \mu || \le C || g||$ is completely missing in Section 5.2. I suggest the authors include this analysis in the section or provide an explanation if it was intentionally omitted. 

- How does micro-batch clipping perform when training from scratch instead of fine-tuning? This could offer valuable insights into its effectiveness in different training scenarios.

- When conducting the language task experiments, reporting validation performance is inappropriate. It would have been better to test on a separate dataset. Additionally, the paper states that validation set information was not used at all, so how was hyperparameter optimization carried out? Clarifying this would improve transparency.

- The experimental results shown in Table 5 reveal little to no improvement in performance. It would be helpful to discuss possible reasons for this outcome and consider further refinements or additional evaluation metrics.

**Typo**
- The term "nominator" in line 395 should be corrected to "numerator."

- The equation $ C = \sqrt{\frac{2(1-\epsilon)\eta - (1 - \epsilon^2) L \eta^2}{2 \epsilon^2 L \eta^2}}$ in line 219 should be updated to $ C = \sqrt{\frac{2(1-\epsilon)\eta - (1 - \epsilon)^2 L \eta^2}{2 \epsilon^2 L \eta^2}}. $

- Additionally, the expression $ \frac{2(1-\epsilon)\sigma^2}{LB} $ in line 232 should be updated to $ \frac{(1-\epsilon)\sigma^2}{2LB}. $

### Questions
- How are micro-batches grouped within a mini-batch? Is this process conducted randomly?

- Around line 114, the text states that mini-batch gradients are "summed," but isn't it more accurate to describe this as "averaged" or "aggregated," given that the mean is typically computed?

### Soundness
3

### Presentation
2

### Contribution
2
