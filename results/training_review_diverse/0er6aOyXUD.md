Now let me write the final consolidated review.

## Summary

This paper proposes RewardMATH, a benchmark for evaluating reward model robustness in mathematical reasoning. It identifies two flaws in the math subset of RewardBench: (1) a representation gap between chosen (human-written) and rejected (machine-generated) solutions that makes the benchmark vulnerable to reward hacking, and (2) reliance on one-to-one comparisons that fail to capture the diversity of incorrect solutions. RewardMATH addresses these by converting human solutions to machine-like step-by-step solutions and using one-to-many comparisons (1 correct vs. 9 incorrect solutions per problem). Extensive validation shows RewardMATH scores strongly correlate with policy optimization outcomes ($r^2 > 0.8$ on MATH500) and predict reward overoptimization, while RewardBench shows almost no correlation ($r^2 \leq 0.128$).

## Strengths

1. **Empirical demonstration that RewardBench fails to correlate with policy optimization while RewardMATH strongly correlates**: The paper shows the coefficient of determination between benchmark scores and $\Delta$acc from BoN sampling is at most 0.128 for RewardBench but exceeds 0.8 on MATH500 for RewardMATH (Figure 3 / lines 204–207). This directly validates the core claim that the proposed benchmark design better represents robustness.

2. **Comprehensive validation across multiple RM types and optimization setups**: The paper evaluates three categories of reward models (generative, classifier-based, process reward models) using both BoN sampling and PPO, in synthetic (dataset-size-controlled) and non-synthetic settings with open and closed models (Sections 4–5). This breadth strengthens the claim that RewardMATH reliably measures robustness across diverse RMs.

3. **Design choices are validated through ablation**: The paper explicitly validates each design element — reducing the representation gap (Figure 4, lines 210–213 shows that using RewardMATH's chosen solution with RewardBench's rejected solution improves correlation) and adopting one-to-many comparisons (Figure 4 shows one-to-one comparisons with single rejected solutions vary widely). This confirms that both design choices contribute to the benchmark's reliability.

4. **RewardMATH predicts reward overoptimization**: Models with higher RewardMATH scores exhibit less reward collapse as KL divergence increases (Figures 6–7 / lines 258–266). In the synthetic setup, increasing dataset size improves RewardMATH scores monotonically while RewardBench shows no such trend (Table 4 / lines 258–261). This goes beyond simple correlation and demonstrates that the benchmark measures practical robustness.

5. **Diagnostic insight into generative RM failures**: The paper computes accuracy "with ties" and observes large improvements (Table 1 / lines 172–174), revealing that most LLM-as-a-judge models fail by assigning equal scores rather than incorrect ranking — a finding not provided by RewardBench's binary comparison.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Unsubstantiated claim about PRM800K annotation errors**: In §3.1 (line 116), the paper states "it was recently revealed that approximately 20% of the annotations in PRM800K are incorrect, even though it is human-annotated" without providing a citation for this specific claim. While the PRM800K dataset citation (Lightman et al., 2023) is provided, it does not contain this 20% error claim. The claim is used to motivate the benchmark redesign, though the primary motivations (representation gap and one-to-many comparisons) are independently justified through step-count distributions and correlation experiments. The fix is straightforward: either add the correct citation, or remove/soften the claim.

2. **Undocumented manual correction process for correct solutions**: The paper states that human-written MATH500 solutions were converted to step-by-step machine-generated solutions using GPT-4, then "manually inspect[ed] the quality … and correct[ed] the errors that are found" (§3.2, line 135). No statistics are reported on how many solutions required correction, how many errors were found, whether multiple annotators were used, or inter-annotator agreement. Since the benchmark's "chosen" side depends on this conversion, providing basic quality metrics would increase trust. That said, for mathematical problems where correctness is objectively verifiable, manual inspection is a standard and reasonable practice.

3. **Missing confidence intervals or significance tests for correlation results**: Table 5 reports $r^2$ values but no p-values or confidence intervals. Given the relatively small number of models (~12), these would help assess the reliability of the reported correlations. This does not invalidate the clear qualitative trends (RewardMATH $r^2 > 0.8$ vs. RewardBench $r^2 \leq 0.128$) but would add rigor.

4. **The paper conflates two design changes simultaneously**: RewardMATH introduces both (a) reduced representation gap and (b) one-to-many comparisons at the same time. While Figure 4 partially disentangles these by testing intermediate configurations, a cleaner internal ablation (e.g., varying the number of rejected solutions from 1 to 9 within RewardMATH's own construction) would more directly attribute the gains to each factor. The existing evidence is sufficient to support the claim that both matter, but the relative contribution remains unclear.

### Trivial

1. **Random selection of rejected solutions without documented seed**: The paper states it "randomly select[s] 1 incorrect solution from each model" (§3.2, line 140) without specifying the random seed. Since the dataset is publicly released on HuggingFace (line 13), the final benchmark is deterministic for users. The concern about reproducibility is effectively addressed by the data release, but documenting the seed or selection procedure would be cleaner.

## Nice-to-Haves

- An ablation showing Spearman correlation vs. number of rejected solutions (a curve from 1 to 9) would strengthen the claim about one-to-many comparisons.
- Extending the benchmark design beyond mathematical reasoning (which the paper acknowledges as a limitation, line 273) would increase impact but is beyond the paper's stated scope.
- Releasing the exact list of problems excluded from MATH500 (only 483 of 500 are used) and the reason would improve transparency.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength Finder's claim that the PRM800K 20% error rate is "cited"**: The strength finder states the paper "addresses the known ~20% annotation error in PRM800K (cited)". This is factually incorrect — the paper does not provide a citation for this claim (line 116). The rest of the strength (about careful benchmark construction) is valid and retained above.

- **Harsh critic's concern about "random selection may hurt reproducibility"**: The critic suggests the random selection without a documented seed threatens reproducibility. However, the paper states it releases code and data publicly (§1, line 13). When the final benchmark is released as a fixed dataset, the exact selection is deterministic for users. This concern is addressed by the data release and is at most Trivial.

- **Harsh critic's suggestion to "disentangle the two design choices" via internal ablation**: The paper already partially disentangles them (Figure 4), showing that evaluation sets with reduced representation gap or multiple comparisons yield higher Spearman correlation. The critic's request for a cleaner ablation is reasonable but is a Nice-to-Have, not a weakness that threatens the claims.

## Novel Insights

None beyond the paper's own contributions. The key insight — that a reliable RM benchmark must minimize the representation gap between chosen/rejected solutions and use one-to-many comparisons — is cleanly motivated and validated. The reviews do not surface a novel perspective beyond what the paper itself argues.

## Suggestions

1. Add a citation for the "20% annotation errors in PRM800K" claim, or remove/soften it if a source cannot be found.
2. Report basic quality metrics for the manual correction process: number of solutions corrected, number of errors found, number of annotators, and agreement if multiple annotators were used.
3. Add confidence intervals or p-values for the correlation results ($r^2$) to strengthen statistical reporting.
4. Document the random seed used in the rejected-solution selection in the released code.

## Score and Decision

This paper makes a clear and substantive contribution. It identifies genuine flaws in an existing benchmark, constructs a new benchmark addressing them, and validates the new benchmark's scores strongly correlate with actual policy optimization outcomes — including reward overoptimization. The weaknesses are real but addressable and do not threaten the core claims. The benchmark is released publicly, the validation is thorough across multiple RM types and optimization methods, and the paper's findings have practical significance for the RLHF community.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>