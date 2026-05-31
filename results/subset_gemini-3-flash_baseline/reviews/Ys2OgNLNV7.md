## Summary
The paper investigates the use of internal Query-Key (QK) alignment scores—the raw dot-product between attention query and key vectors—as a "white-box" signal for improving LLM reasoning. The authors demonstrate that a "think-first" phase (Chain-of-Thought) strengthens these internal signals, allowing for more accurate answer selection and verification directly from model activations rather than decoded tokens. The method is evaluated across multiple-choice (MMLU-Pro, HLE) and open-ended (MATH-500, GSM8K) tasks, showing significant gains in accuracy and permutation robustness compared to standard logit-based or greedy decoding baselines.

## Strengths
- **Novel Application of Internal Signals:** While prior work has used QK-scores for probing, this paper successfully applies them to the "think-first" (CoT) paradigm, showing that explicit reasoning steps actually improve the alignment of internal attention heads toward the correct answer.
- **Efficiency and Interpretability:** The method provides a computationally cheap decision rule (a single dot product) that avoids the need for expensive sampling (like self-consistency) or training external reward models/verifiers.
- **Robustness:** The use of Permutation Accuracy (PA) as a metric is a strong choice, as it demonstrates that QK-based selection is significantly less susceptible to the "positional bias" (e.g., preferring option 'A') that plagues standard LLM multiple-choice evaluation.
- **Strong Empirical Gains:** The results in Table 1 and 2 show substantial improvements (e.g., Qwen-14B on MMLU-Pro jumping from 17.7% to 44.4% accuracy) using the QK-score over the standard baseline.

## Weaknesses
### Fatal
None.

### Major
- **Head Selection Generalization:** The method relies on a calibration set to pick a "single best head." While Figure 2 shows a correlation between datasets, the paper lacks a rigorous analysis of how sensitive the performance is to the size or domain of the calibration set. If the "best head" shifts significantly between tasks, the "white-box" advantage is diminished by the need for task-specific supervision.
- **Comparison with Logit-based CoT:** In Table 1 and 2, the "MCQA with CoT Baseline" is compared to "MCQA with CoT QK-score." However, it is not entirely clear if the baseline is using the model's final generated token (the letter) or the logits of the options. If the model generates a long CoT and then concludes with "Therefore, the answer is (A)", the QK-score is essentially acting as a reranker. A more competitive baseline would be to compare QK-selection against a "Self-Consistency" baseline of the same computational budget (e.g., 8 samples).

### Minor
- **Threshold Calibration for Verification:** Section 4.4 mentions grid searching for an optimal threshold on 20 samples. This is a very small calibration set for verification, which might lead to over-fitting or high variance in the verification results.
- **Model Scope:** While the paper tests several models (LLaMA, Qwen, DeepSeek), they are mostly from the same architectural family (Dense Transformers). It is unclear if these "select-and-copy" heads are as prominent in MoE (Mixture-of-Experts) models or models trained with significantly different objectives.

### Trivial
- The paper mentions "Qwen3" in the tables, but Qwen2.5 is the current widely used version; this may be a naming convention or a specific internal version, but it doesn't affect the technical validity.

## Nice-to-Haves
- An analysis of *where* these heads are located (e.g., are they always in the middle/late layers?).
- A comparison of the QK-score against "Entropy" or "Softmax Attention weights" to prove that the raw dot-product is indeed the superior signal.

## Novel Insights
The most significant insight is that Chain-of-Thought (CoT) does not just help the model "calculate" the answer in the output space, but it actively "sharpens" the internal attention mechanism. By generating a reasoning trace, the model's internal query vectors become more strongly aligned with the key vectors of the correct option. This suggests that CoT acts as a latent state optimizer, making the model's internal "preference" for the correct answer much more distinct and readable via QK-alignment than it is through standard output logits.

## Suggestions
- Include a "Head Stability" analysis: show how often the same head is chosen as the "best" across different subsets of MMLU-Pro or between MATH and GSM8K.
- Provide a comparison with "Self-Consistency (SC) @ 5" or "SC @ 8" in Table 4 to better contextualize the Hypothesis Selection gains.

## Score and Decision
The paper presents a compelling and computationally efficient method to extract higher performance from LLMs by looking "under the hood" at attention alignments. The integration of CoT with internal QK-signals is a clever bridge between prompting and interpretability. While the reliance on a calibration set is a minor hurdle, the performance gains and the improvement in permutation robustness make this a valuable contribution to the community.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>