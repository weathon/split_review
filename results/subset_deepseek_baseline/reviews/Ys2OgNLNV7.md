## Summary

This paper proposes using raw query-key (QK) dot-product scores from transformer attention heads as an internal signal for answer selection and correctness verification in LLMs. The authors evaluate this approach across multiple settings: multiple-choice QA with and without chain-of-thought reasoning, verification of reasoning chains, and candidate selection among self-generated hypotheses, demonstrating that QK-score-based selection can match or exceed standard decoding-based baselines on benchmarks including MMLU-Pro, MATH-500, GSM8K, and a variant of Humanity's Last Exam.

## Strengths

- **Novel application of internal attention signals**: The paper extends prior work on QK-score probing (Tulchinskii et al., 2024, 2025) to practical reasoning tasks, showing that raw attention alignment can serve as a white-box decision rule without additional training or external verifiers.
- **Comprehensive experimental scope**: The authors evaluate three distinct use cases (MCQA selection, verification, hypothesis selection) across multiple model families (LLaMA-3.1, Qwen, Qwen3, DeepSeek-R1-Distill) and scales (1.5B to 32B), providing a broad empirical characterization.
- **Permutation accuracy metric**: The inclusion of Permutation Accuracy (PA) from Gupta et al. (2024) is a strong methodological choice that addresses the known issue of position bias in MCQA, lending credibility to the reported improvements.
- **Reproducibility focus**: The paper commits to releasing code, prompts, calibration splits, and evaluation scripts, which is valuable for the community.

## Weaknesses

### Major

1. **Insufficient baseline comparisons and missing standard methods**: The paper compares QK-score selection primarily against a simple "baseline" (decoded token selection) and self-consistency. However, it does not compare against established internal probing methods such as Contrast-Consistent Search (CCS, Burns et al., 2022), DoLa (Chuang et al., 2024), or other decoding-time control methods that are cited in the related work. Without these comparisons, it is unclear whether QK-score offers advantages over existing white-box or decoding-time approaches.

2. **Lack of statistical significance and variance reporting**: The paper reports single accuracy numbers without confidence intervals, standard deviations, or multiple runs. Given that head selection is performed on a calibration set and evaluation on a disjoint set, the results could be sensitive to the specific calibration split. The absence of error bars or significance tests makes it difficult to assess whether the reported improvements (e.g., 22% gains) are robust.

3. **Unclear calibration procedure and potential overfitting**: The head selection procedure picks the single best head on a calibration set of 500 samples. With hundreds of attention heads (e.g., 32 layers × 32 heads = 1024 heads in LLaMA-3.1-8B), selecting the best head on 500 samples risks overfitting to the calibration set. The paper does not discuss this risk, report calibration set performance, or validate that the selected head generalizes across different calibration splits.

4. **Verification task evaluation is problematic**: In Table 3, the "baseline" accuracy for HLE-¼ is reported as 0% for most models, meaning the models never produce a correct verdict. The QK-score then achieves 69-90% accuracy. This dramatic improvement suggests either (a) the baseline is trivially poor (e.g., always predicting "false" or random guessing), or (b) the QK-score threshold is exploiting a trivial signal (e.g., all solutions are incorrect, so always predicting "incorrect" yields high accuracy). The paper does not clarify the baseline definition or report precision/recall/F1, making these results uninterpretable.

5. **Hypothesis selection results are weak and potentially misleading**: In Table 4, the QK-score with calibration on MATH-500 achieves 53.8% on MATH-500 but only 31.6% on HLE-¼ (essentially baseline). The out-of-domain calibration (HLE → MATH) yields 40.2%, which is only 8.2% above baseline. The paper claims "result accuracy is not worse than that of the baseline," but the improvements are modest and inconsistent across domains, undermining the claim of general applicability.

### Minor

- The paper claims "performance gains of up to ≈22% across various benchmarks and models" in the abstract, but the actual gains vary widely (from -3% to +90% depending on task and metric), and the 22% figure is not clearly tied to a specific experiment.
- The HLE-¼ dataset construction (using LLMs to generate incorrect options) introduces potential biases that are not discussed.
- The verification threshold calibration uses only 20 sampled solutions, which is very small for reliable threshold estimation.

### Trivial

- Figure 2 (correlation scatter plot) is referenced but the image is not rendered in the text; the caption describes it but the actual plot is missing from the provided content.

## Nice-to-Haves

- Comparison with CCS, DoLa, or other internal signal methods would significantly strengthen the paper.
- Reporting results with confidence intervals (e.g., bootstrap) across multiple calibration splits.
- Ablation study on calibration set size and its effect on head selection stability.
- Precision/recall/F1 for the verification task to complement accuracy.

## Novel Insights

The paper's core insight—that raw QK alignment scores from a single attention head can serve as a practical selection and verification signal—is interesting but not entirely novel, as it builds directly on prior QK-score probing work (Tulchinskii et al., 2024, 2025). The main novelty lies in extending this signal to CoT-augmented settings and hypothesis selection, and in demonstrating that a "think-first" phase can improve QK-based selection. However, the empirical support is uneven, and the lack of comparison to existing methods limits the strength of the claimed contributions.

## Suggestions

1. Add comparisons to CCS, DoLa, and other internal/decoding-time control methods to establish the relative merits of QK-score selection.
2. Report results with confidence intervals (e.g., bootstrap over 10 different calibration splits) to demonstrate robustness.
3. Clarify the verification baseline: what exactly does the model output, and what is the chance-level accuracy? Report precision, recall, and F1.
4. For hypothesis selection, include a comparison with self-consistency using the same number of samples (k=8) and report results with variance.
5. Discuss the risk of overfitting in head selection and provide evidence (e.g., calibration vs. evaluation accuracy) that the selected head generalizes.

## Score and Decision

The paper addresses an interesting question and provides a broad experimental evaluation, but the weaknesses are significant: missing comparisons to established methods, lack of statistical rigor, problematic verification evaluation, and modest/inconsistent hypothesis selection results. The core claims are not fully supported by the evidence presented.

**Score: 4.0** (borderline reject)

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>