Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper introduces Fast-DetectGPT, a zero-shot detector for machine-generated text that replaces the expensive perturbation step of DetectGPT with efficient conditional independent sampling. The method achieves a 340× speedup over DetectGPT while also improving detection accuracy by a relative ~75% (gap-closing metric) in both white-box and black-box settings, reaching 0.9887 AUROC across five source models and strong results on ChatGPT (0.9615) and GPT-4 (0.9061) generations.

## Strengths

- **Significant practical improvement over DetectGPT with 340× speedup**: Fast-DetectGPT reduces inference time from ~22 hours to ~4 minutes on the same hardware while simultaneously improving detection accuracy. The 0.9887 white-box AUROC (vs. 0.9554 for DetectGPT) and the 340× speed factor are well-documented in Table 1 and Section 3.1, representing a clear engineering advance.

- **Empirically validated discriminative feature**: Figure 1 shows that the conditional probability curvature cleanly separates human-written text (curvature near 0) from machine-generated text (curvature near 3) across four source models on XSum. This distributional gap directly supports the paper's central claim that the statistic is informative.

- **Black-box performance that exceeds DetectGPT's white-box**: Fast-DetectGPT (GPT-J/Neo-2.7) in the black-box setting (0.9677 avg.) outperforms DetectGPT (T5-3B/*) in the white-box setting (0.9554 avg.), a relative 27.6% improvement. This is a strong result showing the curvature feature is more discriminative even with limited model access.

- **Robust performance on ChatGPT and GPT-4 generations**: Table 3 shows Fast-DetectGPT achieving 0.9615 (ChatGPT) and 0.9061 (GPT-4) AUROC, substantially outperforming both zero-shot baselines (Likelihood, LogRank, LRR) and supervised detectors (RoBERTa, GPTZero) averaged across datasets.

- **Interpretable connection to likelihood and entropy**: Section 2.3 shows that when the scoring and sampling models are identical, the curvature numerator decomposes into Likelihood + Entropy, providing a clear theoretical link to established baselines and explaining why the method works.

- **Ablation study confirms key design choices**: The ablation demonstrates that model selection for sampling contributes ~27% relative improvement and the normalization term (σ) contributes ~10%, empirically justifying the design of the curvature estimator.

## Weaknesses

### Fatal

None.

### Major

None. The core claims are well-supported by the experiments.

### Minor

- **Uncontrolled comparison between DetectGPT and Fast-DetectGPT for model size**: In Table 2 (main results), Fast-DetectGPT uses the source model itself (which can be as large as GPT-J-6B or NeoX) for sampling in the white-box setting, while DetectGPT uses T5-3B for perturbation. In the black-box setting, Fast-DetectGPT uses GPT-J-6B while DetectGPT uses T5-3B. The sampling/perturbation model sizes differ, making it unclear how much of the gain is due to the method vs. model capacity. This concern is partially mitigated by Table 3, where DetectGPT uses T5-11B (larger than GPT-J-6B) yet Fast-DetectGPT still outperforms it substantially, suggesting the method itself is the primary driver. However, a fully controlled comparison would strengthen the paper.

- **Numerical discrepancy in the "80% recall" claim**: The introduction (line 42) states "it aptly flags 80% of ChatGPT-crafted content, while only misidentifying 1% of human compositions," but the Usability Analysis (line 255) reports "a recall of 87% for machine-generated texts with only 1% misclassification" for the same condition (ChatGPT, 1% FPR). These numbers (80% vs. 87%) do not match, and the introduction does not specify the dataset or condition under which this result holds. This creates an inconsistency and overgeneralizes a specific operating point.

- **Missing evaluation on paraphrasing attacks**: The paper mentions "Robustness under Paraphrasing Attack" as a subsection header (line 279) but contains no actual content — it is an empty placeholder. Paraphrasing is a well-known evasion technique for machine-generated text detectors, and its absence (whether due to omission or a parser artifact) is a notable gap in the evaluation. Future work should address this.

- **No exploration of the sample count (N=10,000) sensitivity**: The paper fixes N=10,000 samples without examining how performance and speed trade off at smaller or larger sample counts. A sensitivity analysis (varying N from, say, 100 to 100,000) would provide practical guidance for deployment and clarify whether the reported speedup is achievable at lower sample counts.

### Trivial

- **Slightly overstated novelty of the "new hypothesis"**: The paper claims "we posit a **new hypothesis**" about humans vs. machines picking different tokens (line 39), but the basic observation that machine text has higher average probability is the same insight underlying likelihood-based detectors (Gehrmann et al., 2019; Solaiman et al., 2019). The paper does acknowledge this connection (line 85), so the issue is only that the "new" framing is imprecise — the novelty is in the *curvature formulation* and its efficient estimation, not in the observation itself. The paper would benefit from clearer language distinguishing the two.

- **"Conditional probability function" terminology**: Equation 3 defines $p_\theta(\tilde{x}|x) = \prod_j p_\theta(\tilde{x}_j|x_{<j})$ with independent per-token draws given the original context. While the paper transparently states "the tokens $\Tilde{x}_j$ are independently predicted given $x$" (line 92) and "independent sampling of alternative tokens is the key to the efficiency" (line 129), naming this quantity a "conditional probability function" without consistent qualification could mislead readers into thinking it represents the model's autoregressive generation distribution. This is a minor presentation issue that could be addressed by qualifying the name (e.g., "independent conditional probability function") when first introduced.

## Nice-to-Haves

- Adding a baseline that directly combines Likelihood + Entropy (without the variance normalization) would clarify the marginal value of the z-score component and the curvature formulation beyond the simple sum.
- Providing error bars or variance estimates across random seeds for the main AUROC results, given the modest sample sizes (150–500 per condition).
- A theoretical intuition for why the statistic works, e.g., connecting to concentration of measure or typicality, would elevate the paper from purely empirical to having explanatory power.

## Removed Points

These points were flagged by reviewers but filtered upon verification against the paper:

- **Harsh Critic Point 1 (conditional probability function not a proper distribution)**: The Harsh Critic claimed this quantity "has no direct probabilistic interpretation as a conditional probability over texts." This is incorrect — the product of per-position independent conditionals *is* a valid distribution over the product space of token sequences of length |x|. The paper transparently states the independence assumption (line 92, lines 127–130). The concern is reduced to a trivial terminology preference above.

- **Harsh Critic Point 2 (relative improvement metric inflates gains)**: The paper explicitly defines the metric in the Table 1 caption as "(new − old)/(1.0 − old)" and explains it represents "how much improvement has been made relative to the maximum possible improvement." The absolute AUROC numbers (0.9554 vs. 0.9887) are displayed directly in the same table. The abstract points to this table. There is no deception — the metric and absolute numbers are presented together transparently.

- **Harsh Critic's claim about "the paper reports that the normalization (σ) improves performance by 10%" being under-explored**: The ablation study explicitly quantifies this. A brief mention in a results section is appropriate for what it is — an ablation finding, not a core claim. The request for "a more thorough investigation" across datasets is scope creep beyond what the paper's length and focus reasonably support.

- **Strength Finder's strengths about generic importance**: Filtered through — the retained strengths above are specific and well-evidenced.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an angle or interpretation that the paper itself does not already articulate.

## Suggestions

- Resolve the numerical inconsistency between the 80% (intro) and 87% (Section 3.3) recall-at-1%-FPR figures for ChatGPT, and qualify the operating-point claim in the introduction with the specific dataset and condition.
- Add a controlled comparison in which DetectGPT uses a perturbation model of comparable capacity to Fast-DetectGPT's sampling model (e.g., T5-11B for all conditions, not just ChatGPT/GPT-4) to bound the model-size confound.
- Include a sensitivity analysis of the sample count N (e.g., 100–100,000) showing the accuracy–speed trade-off.
- Rename or consistently qualify the "conditional probability function" (e.g., "independent conditional probability function") when first introduced to avoid confusion with autoregressive generation.
- Add evaluation on paraphrased/rewritten texts, or clearly acknowledge this as a limitation.

## Score and Decision

**Overall assessment**: The paper makes a clear, practical contribution to machine-generated text detection. The 340× speedup over DetectGPT with simultaneous accuracy improvement is a strong result. The empirical evaluation is thorough across multiple datasets, models (open-source and proprietary), and settings. The weaknesses are minor and mostly concern presentation and experimental control — none threaten the core claims. This is a solid conference paper.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>