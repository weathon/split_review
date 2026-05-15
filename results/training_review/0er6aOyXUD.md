Now I have thoroughly verified all claims against the paper. Let me produce the final consolidated review.

## Summary

This paper introduces RewardMATH, a benchmark for evaluating reward model robustness in mathematical reasoning. It addresses two concrete flaws in the math subset of RewardBench: (1) a representation gap between human-written chosen solutions and machine-generated rejected solutions, and (2) reliance on a single one-to-one comparison. The paper validates RewardMATH by showing strong correlation between benchmark scores and Best-of-N accuracy improvement (r² > 0.8 for RewardMATH vs. ≤ 0.128 for RewardBench), and by demonstrating that models with higher RewardMATH scores exhibit less reward overoptimization.

## Strengths

- **Identifies and addresses well-motivated flaws in the existing benchmark.** The paper shows that RewardBench's math subset has a step-count distribution gap between chosen (human, few steps) and rejected (machine, many steps) solutions (Section 3.1, Figure 1a), and that a single pairwise comparison is insufficient. RewardMATH mitigates both issues: converting human solutions to step-by-step format with GPT-4 + manual verification, and using a 1:9 chosen-to-rejected comparison.

- **Demonstrates strong predictive validity for policy optimization.** The correlation analysis (Section 5.1, Figure 3) shows that RewardMATH scores achieve r² > 0.8 with Best-of-N accuracy gains on MATH500, while RewardBench scores yield r² ≤ 0.128. This stark difference across multiple reward model types (classifier-based, PRM) directly supports the claim that RewardMATH measures signals useful for policy learning.

- **Uncovers a hidden failure mode in generative reward models.** Table 1 shows that when ties are counted as correct (Acc w/ tie), many LLM-as-a-judge models improve dramatically, revealing that they assign identical scores to correct and incorrect solutions. This finding, enabled by RewardMATH's one-to-many design, would not be visible under RewardBench's binary evaluation.

- **Validates across multiple experimental settings.** The paper evaluates generative RMs, classifier-based RMs (6 from RewardBench leaderboard), and PRMs (4 variants), and validates with both BoN sampling (n up to 256) and PPO in the synthetic setup. The OOD test sets (Gaokao-math, SAT-math) partially mitigate concerns about dataset overlap. Code and data are publicly released.

## Weaknesses

### Fatal
None.

### Major

- **Circularity in the non-synthetic overoptimization setup.** Internlm2-7B-reward is used as the gold RM (defining "true reward") in the overoptimization analysis (Section 5.2, line 231), yet it is also one of the proxy RMs evaluated in the non-synthetic setup (Figure 6). Since the gold RM's own reward trajectory serves as the reference for "true reward," its own overoptimization curve is trivially perfect. This inflates the observed visual separation between high-scoring and low-scoring models and weakens the claim that RewardMATH generally predicts overoptimization for arbitrary reward models. The synthetic setup (freshly trained proxy RMs) is free of this issue, but the non-synthetic setup — which is the primary evidence linking *existing* RewardMATH scores to overoptimization — is not.

### Minor

- **No p-values, confidence intervals, or statistical tests for the main correlation.** The central claim that RewardMATH strongly correlates with BoN improvement (Figure 3, r² > 0.8) rests on ~11–15 data points with no reported confidence intervals, p-values, or residual diagnostics. While the stark magnitude of the effect (r² > 0.8 vs. ≤ 0.128) makes the qualitative conclusion plausible, the lack of statistical rigor means the "strong correlation" claim is not as precisely supported as it could be. The Spearman correlation analysis in Section 5.1 (Figure 4) partially addresses this for ablation studies but not for the main result.

- **Step-distribution gap reduction is not quantitatively validated.** The paper motivates RewardMATH by showing that RewardBench has a step-count gap between chosen and rejected solutions (Section 3.1, Figure 1a), and proposes converting human solutions to machine-step-by-step format to close this gap. However, no figures or statistics are presented showing the step distribution for RewardMATH's chosen vs. rejected solutions. Without this comparison, the claimed improvement in representation gap remains unverified, though the ablation in Figure 4 (where using RewardMATH chosen + RewardBench rejected improves correlation) provides indirect evidence.

- **Number of rejected solutions (9) is not ablated.** The paper uses 9 rejected solutions per problem (Section 3.2, line 128) but provides no sensitivity analysis varying this number (e.g., 3, 6, 12). It is unclear whether the 1:9 ratio is critical or whether a smaller set would suffice. This affects understanding of the benchmark's design trade-offs and resource requirements.

- **MRR scores are mentioned but not reported.** The paper defines Mean Reciprocal Rank as an alternative metric (Section 3.3, line 148) but only reports strict accuracy (chosen > all rejected) in the main results. Reporting MRR would clarify whether conclusions are sensitive to metric choice.

- **Figure 6 overoptimization analysis lacks quantitative correlation.** The paper states that "the higher the performance... the less reward collapse occurs" (Section 5.2, line 265) based on visual inspection of line colors. No numerical correlation coefficient (e.g., Spearman between RewardMATH score and overoptimization severity) is reported, making the claim qualitative rather than quantitative.

- **Non-synthetic overoptimization analysis uses only BoN.** The paper acknowledges (line 244) that PPO is not used in the non-synthetic setup due to instability concerns. While the synthetic setup includes PPO, the primary evidence linking existing open-source RMs' RewardMATH scores to overoptimization is BoN-only. BoN and PPO can behave differently with respect to reward overoptimization, so the generalization to online RL is partially inferred rather than directly shown.

- **Citation needed for the "20% error rate" claim.** Section 3.1 (line 116) states that "approximately 20% of the annotations in PRM800K are incorrect" without a specific citation. The surrounding citation (lightman2023verifystep) is the original PRM800K paper, not the source of this error-rate claim.

### Trivial

- Manual inspection of GPT-4 solutions (Section 3.2, line 135) is mentioned without inter-annotator agreement metrics or an error rate, slightly affecting reproducibility.
- No confidence intervals are reported for per-model scores in Table 2.
- Figure 3 (bar graph of r² values) could be complemented by a scatter plot with per-model labels, which would be more informative given the small N.

## Nice-to-Haves

- **Replace the gold RM in the non-synthetic setup** with an independent oracle (e.g., verified correctness on a held-out set) to eliminate the circularity concern entirely.
- **Add a PPO experiment for the non-synthetic setup** (with careful initialization to avoid instability) to directly connect RewardMATH scores to online RL overoptimization.
- **Ablate the number of rejected solutions** (e.g., 3, 6, 12) and recompute the correlation with BoN improvement to test whether 9 is strictly necessary.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Introduction lacks concrete evidence that the gap causes reward hacking"** — The paper provides evidence for this via the ablation in Section 5.1 (Figure 4), which shows that partially closing the gap improves correlation. The claim is not unsubstantiated.
- **"Table 1 confounded by training data" (generative RMs preferring human-written solutions)** — This is speculative and the paper's claim about failure to distinguish is robustly supported by the Acc (w/ tie) analysis. The paper tests both direct assessment and pairwise comparison, showing the issue persists across settings.
- **Various formatting/style nitpicks** — These reflect parser artifacts, not author errors.
- **Any criticism about missing appendix content, missing proofs, or absent references** — The parser strips appendix content; these are not author omissions.

## Novel Insights

Beyond the paper's own contributions, the most interesting finding is that the simple act of converting human-written solutions to machine-step-by-step format (thereby closing the representation gap) appears to be more impactful on correlation with downstream policy performance than the number of comparisons alone. The ablation in Figure 4 shows that using RewardMATH's chosen solution with RewardBench's rejected solution (partial gap closure, one-to-one) yields better Spearman correlation than using RewardBench's chosen with RewardMATH's 9 rejected solutions (gap still present, one-to-many). This suggests that representation alignment between chosen and rejected completions may be the more critical design principle — a point worth investigating in future benchmark design beyond the math domain.

## Suggestions

1. Add confidence intervals or bootstrap estimates for the r² values in Figure 3, and include a scatter plot with per-model labels to make the small-N regression more transparent.
2. Include a step-distribution comparison figure for RewardMATH (chosen vs. rejected) alongside the existing RewardBench distribution (Figure 1a) to directly validate that the representation gap is reduced.
3. Ablate the number of rejected solutions (e.g., 3, 6, 12) and report whether the correlation with BoN improvement holds with fewer comparisons.
4. Report MRR scores alongside accuracy to address metric sensitivity concerns.
5. Add a quantitative measure of overoptimization severity (e.g., KL at peak gold reward) and correlate it with RewardMATH scores numerically rather than relying on visual inspection.

## Score and Decision

The paper addresses an important and timely problem — reward model evaluation for mathematical reasoning — with a clearly motivated design and multiple forms of validation. The core finding (RewardMATH scores correlate with downstream policy improvement while RewardBench scores do not) is supported and practically significant. The weaknesses identified are about the *strength of evidence* (statistical rigor, one methodological concern about gold RM selection, missing ablations) rather than fundamental flaws. None invalidates the contribution, but collectively they mean the claims are somewhat stronger than the current evidence fully supports.

The gold RM circularity in the non-synthetic setup is the most significant concern, but it is partly mitigated by the independent synthetic experiments. The other weaknesses are addressable with additional analysis. This is a solid paper with a clear contribution that deserves publication with the caveat that the overoptimization claims should be slightly tempered or the gold RM issue addressed.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>