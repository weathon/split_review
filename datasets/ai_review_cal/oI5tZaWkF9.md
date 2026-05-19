- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8
Now I have all the information needed to write a consolidated review. Let me synthesize.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
List only evidence-backed, concrete strengths.

## Weaknesses
Carefully filtered per the rules.

Let me write the final review now.

---

## Summary

The paper proposes IMP-Loss and DIMP-Loss, two weighted-loss functions for training text classifiers on LLM-generated synthetic data. The methods use a small real-world dataset to build a "quality checker" (probability of the data under the real distribution) and a "diversity checker" (inverse probability under either the synthetic data distribution or the current model), assigning higher weights to high-quality, diverse examples. Experiments on three text-classification benchmarks with GPT-3.5-turbo-generated data show consistent improvements over CE-Loss, Focal-Loss, and a meta-learning baseline.

## Strengths

- **Principled distribution-alignment motivation via importance sampling.** IMP-Loss is derived from a Monte Carlo importance-sampling perspective (Eq. 4–6, lines 82–95), providing a clear theoretical rationale for weighting synthetic data to match the real-world distribution.
- **Consistent and substantial empirical gains.** On all three benchmarks with GPT-3.5-generated data, both IMP-Loss and DIMP-Loss outperform CE-Loss, Focal-Loss, and DML by meaningful margins (e.g., Financial: CE-Loss 77.39 Acc → IMP-Loss 82.09 → DIMP-Loss 82.67; Tweet Irony: CE-Loss 76.91 → IMP-Loss 81.89; MRPC: CE-Loss 72.00 → IMP-Loss 75.83). Table 1 (lines 194–199) documents the full results.
- **Computational efficiency of DIMP-Loss.** Section 4.4 (lines 171–174) explicitly characterizes the overhead: DIMP-Loss requires only one additional training pass on the small real-world set and one forward pass on the synthetic set, making it far cheaper than meta-learning approaches like DML.
- **Robustness to smaller/reduced quality checkers.** Table 3 (lines 254–268) shows DIMP-Loss with a BERT-base quality checker still achieves top accuracy (83.25 on Financial) when training a BERT-large classifier. Figure 2 (line 270) further shows that even 10% of the real-world data suffices for the quality checker.
- **Stable training dynamics.** Figure 1 (lines 232–248) shows IMP-Loss and DIMP-Loss converge to higher accuracy with lower variance across epochs compared to CE-Loss and Focal-Loss.

## Weaknesses

### Fatal
None.

### Major

- **No filtering baseline despite motivating against it in the introduction.** The paper explicitly contrasts its weighting approach with data filtering: "filtering strategies abandoned the potential of the filtered data that may contribute to the final performance" (line 13). Yet no filtering method (e.g., confidence-thresholding, CACTUS-style selection, self-instruct filtering) is included in any experiment. Without this comparison, the core claim that weighting is preferable to filtering for LLM-generated data remains unsubstantiated. This is the most significant empirical gap.

- **Limited evaluation scope relative to the generality of claims.** The experiments cover only three text-classification datasets, one LLM generator (GPT-3.5-turbo), and one model architecture (BERT). The paper frames the methods as broadly applicable to "leveraging synthetic data from any suitable data generator" (abstract), but does not test across different LLMs (e.g., LLaMA, GPT-4), task types (e.g., sequence labeling, QA, generation), or data regimes beyond the three tested. While the paper's title scopes to text classification, the claims in the abstract and conclusion are more expansive than the evidence supports.

### Minor

- **DIMP-Loss derivation from the online batch-selection objective is heuristic.** The transition from Eq. 6 (the online selection objective) to Eq. 7 (the ratio of two conditional probabilities) is presented as following from Bayes' rule, but the steps are not shown and the reasoning is not obvious. More importantly, the paper then approximates \(\hat{P}(y|\mathbf{x}; \theta_t, D_{P'})\) with \(\hat{P'}(y|\mathbf{x})\) — a separately trained static model. This severs the connection to the dynamic, one-step-ahead selection motivation. The paper cites prior work (bayesian_data_selection) for this approximation and is transparent about it, but the claimed theoretical grounding is weaker than presented. The method may still be effective, but the motivation is heuristic rather than rigorously derived.

- **DML baseline results are anomalously poor, raising questions about comparison fairness.** On LLM-generated data, DML (71.7 Acc on Financial, 71.42 on Tweet Irony) underperforms even simple CE-Loss (77.39 and 76.91, respectively). On large real-world data, DML scores 60.33 Acc on Tweet Irony versus CE-Loss's 68.75 — an 8-point drop. The paper states it used the authors' official code (line 215, footnote), but does not report whether hyperparameter search was performed for DML. These numbers are far below what one would expect from a reasonable implementation, which weakens the paper's claim that "our methods outperformed all baselines" — since one baseline may not have been properly tuned.

- **No confidence intervals or statistical significance on main results.** Table 1 reports only point estimates. Figure 2 does show variance across seeds for accuracy curves, but the main results table lacks any quantification of uncertainty (standard deviations or confidence intervals), making it impossible to assess whether observed improvements are statistically reliable.

- **Hyperparameter values not reported.** The focusing parameter \(\gamma\) for Focal Loss is mentioned but never specified. Any DML-specific hyperparameters are also absent. While these may be in the stripped appendix, their omission from the main text makes the experimental setup harder to evaluate.

- **The importance-sampling derivation assumes \(Q(\mathbf{x}) \approx P(\mathbf{x})\) without supporting analysis.** This assumption (Section 3, lines 72–73) is critical for the IMP-Loss weight derivation (lines 89–95), but the paper provides no empirical analysis (e.g., input distribution similarity) to validate it. Additionally, importance weights of the form \(P(y|\mathbf{x})/Q(y|\mathbf{x})\) are known to have high variance in high dimensions; the paper does not discuss truncation, normalization, or any variance-reduction strategy.

### Trivial

- **Table 1 caption formatting is non-standard.** "Bold entries denote the performance within 0.5% comparing to the best performance of each training source" leads to multiple bolded entries per column, diluting the visual signal. Standard practice would bold only the single best result per column (or per training source + metric combination).
- **Section 3.2 dataset reference is ambiguous.** The information-theoretic metrics are reported for "a Financial benchmark scenario" without clarifying whether this is the Financial Phrasebank dataset used elsewhere or a different dataset.

## Nice-to-Haves
- An analysis of the weight distribution (e.g., what kinds of synthetic examples receive high vs. low weights, with qualitative examples or t-SNE visualization) would strengthen the story.
- Experiments with additional LLM generators (e.g., LLaMA, GPT-4) would demonstrate generality.
- A small wall-time comparison would substantiate the claimed computational advantage.
- A filtering baseline (e.g., keep examples where \(\hat{P'}(y|x) > \tau\)) would directly test the paper's argument against filtering.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Missing noisy-data experiment (Harsh Critic point 1).** The paper references a noisy-data condition (Sec.~\ref{sec:training_on_noisydata}) in both the introduction (line 16) and experiments (line 212). The parser strips appendix sections; this experiment exists in the full submission. Per the removal rules for missing appendix content, this criticism is removed.

- **Section 4.2 bound derivation missing (Harsh Critic).** The inequality bounding DIMP-Loss is presented without derivation steps shown in the main text. The reproducibility statement (line 312) references appendix sections for theoretical results, including the lower bound. Per the removal rules, this is removed.

- **Missing appendix/prompts/hyperparameters.** The paper explicitly states these are in the appendix (lines 310–312). Removed per rules.

- **Formatting/style nitpicks** (unusual caption formatting is kept as Trivial above since it has substantive content about result interpretation).

- **Section 3.2 dataset unclear → "Financial benchmark scenario."** In context (lines 69–70), this clearly refers to the Financial Phrasebank dataset — the only "Financial" dataset used in the paper. Removed as factually incorrect.

- **Table 2 IMP-Loss inconsistency (Harsh Critic).** The paper already acknowledges "IMP-Loss showed inconsistent performance when using a smaller Diversity Checker" (line 277). The criticism restates what the paper itself says and is thus removed.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- **Add a filtering baseline.** The simplest approach — keep synthetic examples where the quality checker probability exceeds a threshold, discard the rest — would directly address the paper's motivating contrast with filtering and substantially strengthen the evaluation.
- **Validate the DML implementation.** Either verify that DML achieves reasonable performance on a standard benchmark (to rule out implementation bugs), or replace it with a more reliable meta-learning baseline. Report whether hyperparameter search was performed.
- **Add confidence intervals or standard deviations to Table 1.** This is standard practice and would allow readers to assess the reliability of the reported gains.
- **Clarify the DIMP-Loss derivation.** Even if the connection to the online selection objective is heuristic, the paper should be explicit about which approximations are being made and cite the prior work more carefully.
- **Report key hyperparameters** (γ for Focal Loss, DML settings) in the main text.
