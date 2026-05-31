## Summary
The paper introduces the Query-Key (QK) score—the raw dot-product within a transformer's attention heads—as a white-box decision rule for selecting and verifying answers in LLM reasoning tasks. The key finding is that performing a "think-first" phase via Chain-of-Thought (CoT) prompting systematically strengthens this internal signal, making it more reliable than standard logit-based decoding. The authors demonstrate that QK-score selection is significantly more robust to option-ordering bias (Permutation Accuracy) and outperforms standard self-verification prompts on challenging reasoning benchmarks like HLE and MATH-500.

## Strengths
- **Significant Robustness to Position Bias**: The paper provides strong evidence that internal QK signals are more robust to answer-order effects than output logits. For example, on MMLU-PRO (Table 1), LLaMA-3.1-8B shows a jump from 10.6% Permutation Accuracy (baseline) to 21.4% using the QK-score rule.
- **Enhanced Verification Performance**: The method achieves impressive results in correctness verification, particularly on the difficult HLE benchmark. While standard self-judging baselines struggle (0-1% accuracy), the QK-score thresholding reaches up to 90% accuracy for certain models (Table 3), demonstrating a latent ability to recognize correctness that is not surfaced through text generation.
- **Novel Empirical Paradigm**: The transition from evaluating the model's *generative* output (CoT) to using that generation to strengthen its *internal* selection mechanism (QK-alignment) is a compelling and well-supported contribution.
- **Generalizable Head Identification**: The authors show (Figure 2) that heads identified via calibration on one task (MATH-500) correlate strongly with performance on another (HLE), suggesting these "select-and-copy" heads are general reasoning components rather than task-specific artifacts.

## Weaknesses

### Fatal
None.

### Major
- **Suspiciously Weak Verification Baseline**: The reported "Baseline" accuracy for self-verification on HLE-1/4 is 0-1% for several competitive models (Table 3). This suggests an evaluation protocol or prompt for the baseline judge that is failing at a trivial level (e.g., unable to follow "true/false" formatting). While the QK-score's high accuracy is notable, the lack of a strong baseline (like mean log-probs or optimized self-correction prompts) makes it difficult to assess the true relative gain.
- **Methodological Gaps in Head Localization**: The paper identifies the existence of "best heads" for QK-scoring but provides little detail on *where* these heads are located (layer/index) or how many such heads exist per model. Given that prior work (Tulchinskii et al., 2024) is cited, a more thorough comparison or confirmation of head stability across different reasoning architectures would be expected for a paper claiming a "white-box" contribution.

### Minor
- **Sensitivity to Formatting and Delimiters**: The method relies on choosing specific tokens (e.g., end-of-line tokens) to represent the premise and response. As acknowledged in the limitations, this makes the method sensitive to prompt formatting and tokenizer specifics, but the paper lacks an ablation on how different choices (e.g., average pooling vs. last token) affect the stability of the QK-score.
- **Calibration Set Requirements**: The method requires a calibration phase to select the optimal head and verify thresholds. The paper does not analyze the sensitivity of the results to the size of this set (e.g., how the performance scales with 10 vs. 500 samples), which is crucial for determining the practical "cost" of deploying this rule on new tasks.

### Trivial
- **Variance and Significance**: Results in Table 4 (Hypothesis Selection) are reported on relatively small subsets (N=182, 259) without variance reporting or significance testing, which would be standard for improvements of this magnitude (e.g., 32% to 53%).

## Nice-to-Haves
- Comparison against standard white-box baselines such as mean log-probability of the reasoning chain for the verification and hypothesis selection tasks.
- Visualization of the standard "location" of these heads across layers (e.g., middle layers vs. late layers) for the various models tested.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *Criticism regarding the 0% baseline being "broken" because it cannot identify its own correct answer*: While the AC agrees the baseline is weak, the reviewer's phrasing that "LLM-as-a-judge is completely failing... or unable to follow the true/false formatting" is a valid observation about the paper's reported experiment, though it was demoted to Major from Fatal because the 90% accuracy of the QK signal is still an interesting intrinsic result.
- *Reproducibility of cited models*: Concerns about the existence of "Qwen3" or "HLE" are removed as per hard rules (they are assumed to exist).

## Novel Insights
The core novel insight is the synergistic relationship between **generative reasoning** (CoT) and **internal activation-based selection**. Traditional work treats CoT as a way to improve the final token. This work shows that the process of generating a CoT reasoning trace actually "primes" or "configures" the internal attention heads, creating a high-fidelity alignment signal that is natively more robust to permutation bias than the model's final output distribution. This suggests that LLM errors like position bias may be introduced during the final unembedding/projection phase rather than being fundamental to the model's "internal understanding" of the prompt.

## Suggestions
- Include a log-probability baseline for Tables 3 and 4 to prove the QK signal is not a redundant proxy for sequence likelihood.
- Provide a summary table of the "best head" indices (layer and head number) for the main models (LLaMA-3.1, Qwen) to assist with independent verification and interpretability.
- Conduct a sensitivity study on the calibration set size to show how much "supervision" is truly required for a new dataset.

## Score and Decision

Calibration anchored against:
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/A0W7VCSQev.md (Avg Score 4.75): This anchor explores QK-scores for MCQA but lacks the "think-first" CoT integration and the extensive free-form verification/hypothesis selection experiments present in the current paper. The current paper is significantly more comprehensive.
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Tigr1kMDZy.md (Avg Score 7.33): This paper looks at "overthinking" and "induction heads" for few-shot learning. The current paper is similar in depth and mechanistic focus but covers a broader range of practical reasoning tasks (HLE, MATH-500).
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/EytBpUGB1Z.md (Avg Score 8.00): This anchor provides a more rigorous "mechanistic" explanation (Retrieval Heads). The current paper is slightly less mechanistically rigorous (e.g., lacks head localization detail) but offers higher practical utility for test-time scaling and verification.

Round-1 bracket was [5.0, 7.5]. Round 2 narrowing and comparison against *A0W7VCSQev* (which it clearly surpasses) and *Tigr1kMDZy* (which it is comparable to in level of insight) suggests a score in the mid-to-high 6s or low 7s. While the zeroed-out baselines are a concern, the PA robustness gains are a very strong, verified empirical result.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>