## Summary

The paper proposes a method to detect poisoned examples in instruction fine-tuning datasets using influence functions combined with a semantic transformation (e.g., sentiment inversion). By comparing influence score distributions before and after transformation, the method flags “critical poisons”—examples with strong influence that remain unchanged. The authors demonstrate on sentiment classification (T5-small) and math reasoning (deepseek-coder-1.3b) that removing a small fraction of detected examples (≈1%) restores model performance to near-clean levels, and claim the method requires no prior knowledge of the attack.

## Strengths

- **Important problem**: Detecting instruction fine-tuning attacks without prior knowledge of triggers or attack strategies is a timely and challenging problem for safe LLM deployment.
- **Novel idea**: Using influence functions under a semantic transformation to distinguish poisoned from clean examples is a creative and principled approach.
- **Computational feasibility**: The use of EK-FAC approximation (Kronfluence) makes influence computation practical for moderate-sized models and datasets (50k examples in 2 hours on a single A100).
- **Two-task demonstration**: The method is tested on both sentiment classification and math reasoning, showing some degree of generalization across tasks and model architectures.

## Weaknesses

### Fatal

- **Extremely low true positive rate undermines the core claim**: For the sentiment classification experiment, only 23 out of 653 detected “critical poisons” are actual poisons (TPR ≈ 3.5%). This means the method flags mostly clean examples. The paper does not compare against random removal of the same number of examples, so the observed performance recovery cannot be attributed to poison removal—it may simply be an artifact of removing 1% of the training data. Without such a baseline, the claim that the method “detects critical poisons” is not supported.

### Major

- **Task-specific transformation limits generality**: The method requires designing a transformation that inverts the task’s output (e.g., sentiment flip for sentiment classification, “What is the opposite of” for math reasoning). This is prior knowledge about the *task*, not the attack. The paper does not provide guidance on how to choose such a transformation for arbitrary tasks, which severely limits the claimed “no prior knowledge” advantage.
- **Weak evaluation metrics and missing baselines**: The sentiment experiment uses “POS ratio” (fraction of positive predictions) rather than standard accuracy or attack success rate. The attack’s effect on POS ratio is small and inconsistent across tasks. No comparison is made with simple baselines such as random removal, loss-based filtering, or clustering methods under the same experimental setup. The math reasoning experiment lacks a random-removal baseline as well.
- **Detection performance is too low for practical use**: Even in the math reasoning experiment, the TPR for the top-100 detected examples is only 15%. Removing 100 examples (more than the number of true poisons) drops the target output rate to zero, but again without a random-removal control it is unclear whether the detected examples are responsible. The method appears to require removing many clean examples to achieve any effect.

### Minor

- **The paper does not define “strong influence” or the selection criterion for critical poisons quantitatively** (e.g., threshold or top-k). The description is vague.
- **The ablation study is limited**: Only a few alternative prefixes are tested, and the results are described qualitatively (“almost no impact”). No quantitative comparison of detection rates or recovery is provided.
- **The comparison with existing methods is superficial**: High-loss removal is dismissed with a single sentence and no experimental details. Spectral signatures and activation clustering are mentioned but not evaluated under the same attack setup.

### Trivial

- The paper states “We show that this method work on sentiment classification task” (grammar).
- Table 2 reports accuracy that is identical across conditions (56.52%), which is suspicious and not discussed.

## Nice-to-Haves

- Compare against random removal of the same number of examples to demonstrate that the detected examples are indeed more harmful.
- Provide precision-recall curves or ROC curves for the detection method across different thresholds.
- Test on a larger model (e.g., 7B) to show scalability.
- Include a more thorough ablation of transformation choices, including cases where the transformation is not perfectly aligned with the task.

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

- Add a random-removal baseline for both tasks to show that the detected examples are more effective at recovering performance than random data removal.
- Report standard metrics such as attack success rate (e.g., fraction of trigger-containing test inputs classified as positive) and accuracy, not just POS ratio.
- Provide a clear, quantitative definition of “critical poison” (e.g., top-k by a combined score of influence magnitude and invariance).
- Discuss how to design the semantic transformation for a new task without prior knowledge of the attack, or acknowledge this as a limitation.

## Score and Decision

**Score**: 3  
**Decision**: Reject

The paper addresses an important problem and introduces a creative idea, but the experimental validation is insufficient to support the claims. The detection method achieves a very low true positive rate, and the performance recovery results are not convincingly attributed to poison removal due to the lack of a random-removal baseline. The method also requires task-specific transformation design, which limits its generality. Major revisions and stronger evidence are needed before the paper can be considered for acceptance.

MY FINAL SCORE: <score>3</score>  
MY FINAL DECISION: <decision>Reject</decision>