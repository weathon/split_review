- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5
Now I have all the information needed to cross-reference every reviewer claim against the paper. Let me produce the final consolidated review.

---

## Summary

This paper argues that if a model truly understands a mathematical problem, it should perform robustly across diverse tasks and variants of that problem. To operationalize this, the authors introduce **MathCheck**, a 4×4 checklist evaluation framework (four tasks × four robustness variants), along with an LLM-driven pipeline for automatic generation. They produce two datasets — MathCheck-GSM (3,096 samples from 129 GSM8k seeds) and MathCheck-GEO (1,440 samples from 60 geometry seeds) — and evaluate 43 models. The key evidence is that MathCheck-GSM correlates more strongly with independent proxies of genuine mathematical ability (private data GSM1k, and BPC-loss on math arXiv papers) than the vanilla GSM8k benchmark does.

## Strengths

1. **Novel and well-motivated checklist design.** The 4×4 matrix — Problem Solving, Answerable Judging, Outcome Judging, Process Judging crossed with Original, Problem Understanding, Irrelevant Disturbance, Scenario Understanding — is clearly described and directly follows from the paper's core thesis (if a model really understands a problem, it should work across tasks and variants). This structure is a genuine methodological contribution that goes beyond single-task evaluation.

2. **Strong comparative correlation evidence.** The paper directly compares MathCheck-GSM against GSM8k on two independent proxies of true reasoning ability. The Pearson coefficients (MathCheck-GSM: \(p=-0.915\) vs. GSM8k: \(p=-0.822\) with BPC-loss; and a higher correlation with private GSM1k) provide concrete evidence that the checklist better aligns with measures less susceptible to contamination and overfitting. This is a head-to-head benchmark comparison, not an indirect one.

3. **Comprehensive evaluation with diagnostic value.** Evaluating 26 LLMs and 17 MLLMs across the checklist dimensions produces fine-grained breakdowns (Tables 1 and 2) that allow the paper to surface non-obvious patterns — e.g., that math-specialized models (DeepSeek-Math, MetaMath) improve sharply on problem solving but show limited or negative transfer to other tasks, and that models like Qwen1.5-72B-Chat exhibit large performance gaps across task types. These diagnostics are precisely what a single-accuracy-number benchmark cannot reveal.

4. **Automatic generation pipeline mitigates data contamination concerns.** The framework can dynamically generate evaluation data from any seed benchmark, reducing the risk of memorization and contamination that plagues static open-source benchmarks. The 84% pass rate with manual verification by three graduate students provides reasonable confidence in data quality.

## Weaknesses

### Fatal

None.

### Major

1. **Dataset scale limits reliability of fine-grained comparisons and correlations.** MathCheck-GSM has only 129 seed problems (3,096 samples total, spread across 16 cells); MathCheck-GEO has 60 seeds (1,440 samples). The paper reports Pearson correlations and model rankings (e.g., O1-preview 93.2 vs. GPT-4o 92.0) without any confidence intervals, bootstrapping, or significance tests. With this many models and this few independent seeds, some of the differences the paper discusses may fall within noise. The correlation coefficients with GSM1k and BPC-loss are visually impressive, but their stability is unquantified. This is the paper's most significant limitation — the evidence is directionally convincing but lacks the statistical rigor expected for a benchmark that claims to measure "true reasoning ability."

2. **The "linear representation of intelligence" claim is overstated relative to the evidence.** The paper states that MathCheck "represents mathematical intelligence more linearly" (Section 3.4 title) but never tests whether the relationship is actually more linear (vs. e.g., a nonlinear fit that would tighten or loosen the difference). What the evidence actually shows is a higher Pearson correlation, which measures strength of *linear* association — not "linearity" as a property distinct from correlation strength. The surrogates (GSM1k and BPC-loss) are themselves reasonable proxies but are not independently validated as measures of "mathematical intelligence"; the paper inherits this framing from prior work without critical discussion. The core finding (MathCheck correlates better) is solid and sufficient; the "more linear" framing adds unnecessary vulnerability.

### Minor

1. **Inter-annotator reliability is unreported.** The paper mentions "three graduate students who underwent training" for manual validation and an average pass rate of 84%, but it does not report any inter-annotator agreement scores (e.g., Cohen's \(\kappa\)). Without this, the claim that validation is "rigorous" is unverifiable. An 84% overall pass rate is also not broken down by task type or robustness variant, making it impossible to assess where the generation pipeline is weakest.

2. **Reasoning consistency analysis is qualitative.** The behavior analysis (Section 4) identifies models with inconsistent performance (e.g., Qwen1.5-72B-Chat: PS=71.1 vs. OJ=31.9) through visual inspection of tables. While the patterns are visible and interesting, the paper does not quantify inconsistency (e.g., variance or range across checklist cells) or test whether observed inconsistency correlates with proxy-based measures of overfitting. Formalizing these observations would strengthen the "excessive decoration" argument.

3. **Extension to other reasoning domains is too thin.** Section 5 discusses adapting MathCheck to date understanding and code generation with one paragraph and no data or evaluation results. This reads as a teaser for future work rather than a contribution of the current paper. Including even small-scale results for one additional domain would have been more useful.

4. **No full checklist group example is shown.** The paper would benefit from showing one complete 4×4 checklist matrix (a single seed problem expanded into all 16 cells) so readers can directly assess the quality and diversity of the generated data. Currently, only Figure 1 gives a schematic overview.

### Trivial

None.

## Nice-to-Haves

- Report bootstrapped confidence intervals for the Pearson correlations with GSM1k and BPC-loss (even a simple percentile bootstrap with the available model points would be informative).
- Show the full 4×4 matrix results for at least 2–3 representative models to demonstrate the diagnostic utility more concretely than aggregated row/column means.
- Ablate the generation model (e.g., compare data from GPT-4-Turbo vs. a weaker model) to understand sensitivity of the pipeline.
- Include a failure analysis: what kinds of errors do models make on different checklist cells?

## Removed Points

The following points from the harsh critic were considered but are excluded or demoted:

1. **"No direct head-to-head comparison with existing multi-task benchmarks like MathVista, GSM-Symbolic, or MathAttack"** — The paper's primary claim is about superiority over *single-task* benchmarks (GSM8k, Geometry3K), and it provides direct comparative evidence via correlation with surrogates. Comparing against MathVista (multi-modal collection) would be scope mismatch. Comparing against GSM-Symbolic or MathAttack (robustness-only benchmarks) would be useful but not essential; the absence does not weaken the core claim. These belong in Nice-to-Haves at most.

2. **"The claim about overfitting risk is asserted without evidence"** — The paper introduces this claim in the introduction and then supports it empirically in Section 3.4 (the correlation analyses showing inflated GSM8k scores for models like DeepSeek-Math-7B-RL). This is standard paper structure, not an unsupported assertion.

3. **"The data and code are claimed to be at a URL, but the link is not verified"** — Removed per hard rules: the paper cites its repository, which is assumed to exist.

4. **Strength Finder claim about "extensibility demonstrated"** — Removed. The extension section contains no data or results; a one-paragraph description without evaluation does not constitute demonstration.

## Novel Insights

None beyond the paper's own contributions. The two synthesized insights that emerge most clearly from combining the reviews are: (1) the checklist's diagnostic value is real but would benefit from quantification rather than visual inspection, and (2) the correlation evidence is directionally strong but would be substantially more convincing with even basic uncertainty quantification.

## Suggestions

1. Add bootstrapped 95% confidence intervals to the Pearson correlation figures (Figs. 4 and 5). With ~26 data points, a simple percentile bootstrap would clarify whether the gap between MathCheck and GSM8k correlation is stable.
2. Report inter-annotator agreement (Cohen's \(\kappa\) or percent agreement) for the manual validation process, and break down the 84% pass rate by task type and robustness variant.
3. Show at least one complete 4×4 checklist example for a representative seed problem in the appendix.
4. Quantify reasoning inconsistency using a simple metric (e.g., coefficient of variation across the 16 cells) and correlate it with overfitting indicators (e.g., gap between GSM8k and GSM1k performance).
5. Tone down the "more linearly" framing — the paper's evidence supports "correlates more strongly with proxies of genuine ability," which is already a strong and sufficient claim.
