- Decision: Reject
- Avg Score: 5.40
- Scores: 6, 5, 6, 5, 5
Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper identifies concrete flaws in RewardBench's math subset — namely, a distribution mismatch between human-written chosen solutions and machine-generated rejected solutions, and reliance on single pairwise comparisons — and proposes a new benchmark, RewardMATH, designed to be resistant to reward hacking. The benchmark uses machine-style correct solutions and a one-to-many evaluation setup (1 correct vs. 9 incorrect solutions per problem). The paper's core validation demonstrates that RewardMATH scores strongly correlate with downstream policy optimization performance (R² > 0.8 on MATH500 vs. at most 0.128 for RewardBench) and can detect reward overoptimization, whereas RewardBench cannot.

## Strengths

- **Strong predictive validity for downstream performance**: Section 5.1 shows RewardMATH scores achieve R² > 0.8 with best-of-n policy accuracy improvements on MATH500, while RewardBench's maximum R² is 0.128. This is the paper's most compelling evidence that the benchmark measures what matters — the reward model's ability to guide policy learning.

- **RewardMATH detects reward overoptimization where RewardBench does not**: Section 5.2 (non-synthetic BoN experiments) demonstrates a clear relationship: models with higher RewardMATH scores show less reward collapse as KL divergence increases, while top RewardBench models (e.g., Oasst-rm-2.1-pythia-1.4b) overoptimize rapidly. This directly supports the claim that RewardMATH captures robustness.

- **Principled construction to address known failure modes**: The conversion of human-written solutions to step-by-step machine-style solutions (Section 3.2) directly mitigates the representation gap documented in Figure 1 (step-count distribution). The use of 9 incorrect solutions from 14 diverse models avoids the "isolated case" problem of single-pair comparisons.

- **RewardMATH scores improve monotonically with training data size**: Table 3 shows that as synthetic training data grows from 5K to 65K samples, RewardMATH accuracy rises from 13.46→38.30, while RewardBench fluctuates (70.28→73.39→70.16). This matches the known property that more data yields more robust reward models, confirming RewardMATH captures a meaningful signal.

## Weaknesses

### Fatal
None.

### Minor
- **Gold RM selection in synthetic experiments has some circularity**: Section 5.2 (line 231) selects Internlm2-7B-reward as the gold RM because it "performs well on both RewardBench and RewardMATH," then uses it to generate preference data for the synthetic overoptimization experiments that partially validate the benchmark design. This is a mild circularity. However, this does not threaten the paper's core claims because (a) the non-synthetic experiments (which provide the strongest evidence) do not use any gold RM, (b) the paper also evaluates via oracle reward (pass@1) which is independent of the gold RM, and (c) the synthetic experiments follow established methodology (Gao et al. 2023, Coste et al. 2023). The paper would benefit from acknowledging this limitation more explicitly.

- **Generative RMs are evaluated on RewardMATH but excluded from the core validation experiments**: The BoN correlation analysis (Section 5.1) and non-synthetic overoptimization analysis (Section 5.2) only include classifier-based RMs and PRMs. Generative RMs (GPT-4, Claude, etc.) appear in Tables 1–2 but are not tested in the downstream validation pipeline. The paper's title and claims refer to "reward models" broadly, but the empirical support for predictive validity is limited to non-generative RMs. The paper should either scope its claims more precisely or justify why generative RMs would follow the same pattern.

### Trivial
- **Uncited claim about PRM800K annotation quality**: Section 3.1 (line 116) states that "approximately 20% of the annotations in PRM800K are incorrect" without a visible citation in the extracted text. While likely a well-known finding in the community, this consequential claim should have a clear reference.

## Nice-to-Haves

- **Report confidence intervals or statistical significance for the overoptimization trends in Figure 5/6**: The visual pattern (darker lines → less collapse) is compelling but lacks numerical quantification. Spearman correlations or confidence intervals would strengthen the claim.
- **Quantify the reliability of the manual correction process** for step-by-step solution conversion (Section 3.2): reporting inter-annotator agreement or the fraction requiring correction would help readers assess data quality.
- **Per-problem difficulty analysis** for RewardMATH: understanding whether the benchmark is dominated by a small set of very hard problems would help users interpret results.

## Removed Points

- **Circularity as a "critical" or "fatal" issue**: The harsh critic's point about gold RM circularity is downgraded from a "Critical Issue" to a Minor weakness above. The non-synthetic experiments do not rely on this assumption, and the oracle reward (pass@1) provides independent validation. The paper follows standard methodology from the overoptimization literature. The weakness is real but does not threaten the core claims.
- **"The paper does not discuss [the attenuation] for out-of-distribution datasets"**: The paper reports OOD results (Gaokao, SAT) with R² values. Discussing attenuation in more depth would be nice, but this is a scope choice, not a flaw. Moved to nice-to-have.
- **"No analysis of per-problem difficulty"**: Moved to nice-to-have. Not a weakness of the current paper, just an additional analysis that could be done.
- **"The PRM aggregation function choice is reasonable but not compared to alternatives"**: This is a minor ablation that would strengthen the paper but is not a weakness in the current work. The paper explicitly justifies its choice (geometric mean to remove step bias).
- **Strength Finder's strengths**: All verified as concrete and specific to the paper. None removed.

## Novel Insights

The reviews converge on the key insight that this paper makes a useful methodological contribution by identifying concrete failure modes in existing reward model benchmarks (distribution mismatch in solution style, single-pair evaluations) and validating a fix whose predictive validity is demonstrated through downstream policy experiments. The harsh critic's skepticism about the gold RM circularity and generative RM exclusion is reasonable but does not undermine the paper's strongest evidence (the non-supervised BoN experiments showing R² > 0.8 vs. 0.128). The most interesting observation across the reviews is that the paper's empirical strategy — validating a benchmark by testing whether it predicts actual downstream behavior rather than just measuring agreement with other benchmarks — sets a higher standard for benchmark design that future work should follow.

## Suggestions

1. Scope the paper's claims more precisely to reflect that predictive validity is demonstrated for classifier-based RMs and PRMs, not generative RMs.
2. Add an explicit limitations paragraph about the gold RM selection in synthetic experiments, noting that this follows established methodology but introduces mild circularity.
3. Add a citation for the PRM800K annotation quality claim, or soften it.
4. Consider adding confidence intervals or correlation statistics for the overoptimization trends in the non-synthetic BoN experiments.
