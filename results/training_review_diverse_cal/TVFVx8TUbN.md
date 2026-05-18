Now I have all the verification I need. Let me compose the final review.

## Summary

This paper introduces MHPP (Mostly Hard Python Problems), a manually curated benchmark of 210 Python programming problems designed to evaluate LLMs beyond the saturated capabilities tested by HumanEval and MBPP. The benchmark targets seven distinct challenge categories (Distraction, Redefinition, Shortcut, Commonsense, Cornercase, Complexity, Codesense) derived from error analysis on existing benchmarks. Experiments across 26 models reveal that MHPP exposes performance gaps that HumanEval obscures—most notably, open-source models that approach GPT-4o on HumanEval fall significantly short on MHPP.

## Strengths

- **MHPP is a genuinely harder benchmark that reveals meaningful performance differentiation.** On HumanEval, many open-source models approach GPT-4o; on MHPP, GPT-4o achieves 49.2 pass@1 vs. DeepSeek-V2.5 at 42.1 and Llama 3.1 405B considerably lower (Table 1). This gap is the paper's central empirical contribution and is well-supported by the 26-model evaluation.

- **The dataset construction process is rigorous.** The 0% contamination rate (Section 3.2) is achieved through internet searches plus a contamination detector, with a two-phase quality assurance process using three meta-annotators per problem. The challenge-specific annotation guidelines (Section 3.1) are concrete and measurable (e.g., Distraction problems require >200 words, Complexity problems require >3 reasoning hops), which provides a principled basis for problem difficulty rather than ad-hoc curation.

- **The seven-category taxonomy yields useful descriptive granularity.** The paper shows that different models fail on different categories (e.g., GPT-4-turbo has 60% error on Shortcut vs. ~40% on other categories in Figure 3), and these patterns are more informative than a single aggregate pass rate. This granularity is a genuine improvement over existing benchmarks.

- **The paper evaluates a broad and representative set of 26 models**, including both open-source (DeepSeek, Llama 3.1, Gemma, Mixtral, Phi) and proprietary (GPT-4o, GPT-4-turbo, GPT-3.5-turbo) families, enabling informative cross-family comparisons.

## Weaknesses

### Major

1. **The claimed correlation with HumanEval is not quantified.** Section 4.4 and Figure 4 assert that MHPP is "closely correlated" and "largely correlated" with HumanEval, but no correlation coefficient (Spearman's ρ, Pearson's r) is reported. Visual inspection of the scatter plot shows substantial scatter: models with similar HumanEval scores (e.g., ~80–85 pass@1) span a wide range on MHPP (approximately 10–40 pass@1). Without a quantitative measure, claims about correlation strength are unsupported, and the subsequent argument that MHPP "more accurately assesses performance in complex scenarios" lacks the grounding it needs. The authors should report rank correlation with confidence intervals across the 26 models.

2. **The confidence interval analysis does not address benchmark reliability.** Section 5.1 computes CIs by subsampling generated outputs (50 of 100 samples per round) from the *same* 210 problems. This tells us that pass@k estimates are stable under repeated sampling of a model's own outputs—but it says nothing about how scores would vary if a different set of 210 problems were drawn. The paper frames this as validating the "robustness" and "reliability" of MHPP (lines 212–213), which overclaims what the analysis supports. The relevant analysis would be problem-level bootstrapping: resampling the 210 problems with replacement to estimate uncertainty intervals on model rankings. Given the modest benchmark size, these intervals might be non-trivial. This is the paper's most significant methodological gap.

3. **The seven challenge categories are validated only through two case studies.** The categories are derived from error analysis of three models (GPT-4, GPT-3.5, DeepSeekCoder) on HumanEval (Section 2.2), then used as fixed templates for the 30 problems each in MHPP. Section 5.2 reviews only *two* problems (one Commonsense, one Complex) to confirm that the intended challenge caused the model's error. This is thin evidence that the categories actually correspond to the failure modes experienced by other models on MHPP. A systematic failure attribution—e.g., having annotators label model failures with the most responsible challenge category across a representative set of models—would substantially strengthen the claim that MHPP measures the seven intended dimensions. The paper's current evidence supports the categories as design principles, not as validated measurement dimensions.

### Minor

4. **Per-category sample size (30 problems) limits within-category conclusions.** With 30 problems per category, a single anomalous problem can shift a category's pass rate by ~3 percentage points. The paper draws conclusions about relative model strengths across categories (e.g., "GPT-4-turbo performed poorly in every MHPP category, with a 60% error rate in shortcut challenges") without reporting per-problem variance. Reporting the standard deviation of per-problem pass rates would allow readers to assess whether category averages reflect consistent behavior or are driven by a few outlier problems.

5. **No representative examples from each category are provided.** The paper shows one general example in Figure 1 and two case studies in Section 5.2, but a table with one representative problem per challenge type (with docstring and key test) would help readers understand what each category means in practice. This is a presentation gap that hurts interpretability.

6. **The correlation figure (Figure 4) would benefit from a trend line or regression annotation.** Adding this would improve the visual interpretability of the relationship between the two benchmarks.

### Trivial

None beyond the minor points above.

## Nice-to-Haves

- Several model-level comparisons are noted but not explored (e.g., why DeepSeek-V2.5 outperforms GPT-3.5-turbo on MHPP but not HumanEval). A brief qualitative analysis of which problem types tip these comparisons would be informative.
- Reporting per-category pass rates alongside bootstrap CIs (problem-level) would make the benchmark's stability at the category level more transparent.
- The MBPP contamination analysis (Section 2.1) is interesting but somewhat tangential to the core contribution and could be condensed.

## Removed Points

- **"The paper does not release the MHPP dataset or code for evaluation within the manuscript"** — Removed per guidelines: the paper describes an API-based access mechanism, and the hard rules prohibit questioning the release status/availability of cited resources.
- **Strength: "Comprehensive statistical validation through confidence intervals"** — Removed because it conflicts with verified Weakness #2: the CI analysis addresses output sampling variance, not the benchmark reliability it claims to support.
- **Criticism about missing appendix content / stripped sections** — Removed per guidelines: parser-stripped content (appendix, proofs, references) exists in the original submission.
- **Generic/superficial strengths from Strength Finder** — Filtered out; the strengths above are the concrete, specific ones that survive cross-checking against the paper.

## Novel Insights

The reviews surface a pattern not fully articulated in the paper: MHPP is most valuable as a *discriminative stress test* (it separates models that HumanEval lumps together), but the paper's empirical apparatus for supporting *why* it separates them (the category taxonomy, the correlation with HumanEval, the CI-based reliability argument) is weaker than the core contribution warrants. The paper's strongest evidence is the raw ranking data in Table 1; its weakest is the post-hoc interpretation of what those rankings mean. This suggests the paper would benefit from doubling down on the descriptive value of the rankings themselves and softening the causal/validity claims about the taxonomy.

## Suggestions

1. **Add problem-level bootstrap CIs** for model pass@1 scores across all 26 models. This directly addresses the reliability concern and requires no new data collection.
2. **Report Spearman's rank correlation** (with bootstrap CI) between MHPP and HumanEval pass@1 scores, and discuss what the resulting value means for whether MHPP adds information beyond HumanEval.
3. **Conduct or add a systematic failure attribution study** (or acknowledge the limitation more prominently if the authors cannot). Even a small-scale annotation of model failures across 3–4 representative models would substantially strengthen the category validity claim.
4. **Reframe the CI section** to clearly state it addresses output-level estimation variance, and add problem-level bootstrapping if possible. If problem-level bootstrapping is not feasible, the limitation should be acknowledged explicitly.
5. **Add a table of representative problems** — one per category with docstring snippet and the key challenge — to help readers understand the taxonomy concretely.

## Score and Decision

The paper's core contribution — a well-constructed, manually curated benchmark with strong quality control — is solid and addresses a genuine need. The 26-model evaluation revealing real performance gaps that HumanEval misses is a useful result for the community. However, the paper systematically overclaims on three fronts: the correlation with HumanEval is asserted without quantification, the confidence interval section is misaligned with its conclusions, and the seven-category taxonomy lacks systematic validation. These gaps are addressable (they require re-analysis of existing data, not new collection), but as presented, the evidence does not fully support the strength of the claims made.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>