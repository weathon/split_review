Now I have all the information needed to write the consolidated review.

## Summary

The paper generalizes Minimum Bayes' Risk (MBR) decoding to incorporate weight uncertainty by replacing the single-model distribution with an expectation over a posterior over model parameters. This yields principled sequence-level and token-level decoding methods that effectively ensemble multiple models during generation. The paper provides extensive experiments across machine translation, summarization, data-to-text, and scoring tasks using finetuned, from-scratch-trained, and zero-shot prompted LLMs, showing consistent improvements over single-model MBR baselines and analyzing the roles of diversity, selective prediction, and scaling behavior.

## Strengths

1. **Principled Bayesian grounding for ensembling in MBR**: The paper modifies MBR's expected risk to incorporate the predictive posterior (Eq. 5, Section 3.1), connecting model combination during decoding to Bayesian decision theory rather than relying on ad-hoc ensembling. This provides theoretical justification that prior ensembling approaches (Kobayashi, 2018; Farinhas et al., 2023) lacked, and the paper explicitly acknowledges and distinguishes itself from this prior work (Section 3.2 Discussion).

2. **Practical decoding methods with clear computational trade-offs**: The paper introduces two sequence-level estimators (Eqs. 9, 10) and a token-level estimator (Eq. 13), each with explicit computational costs: Eq. (9) costs \((|\mathcal{M}|\cdot|\mathcal{H}_\theta|)^2\) utility computations, Eq. (10) costs \(|\mathcal{M}|\cdot|\mathcal{H}_\theta|^2\), and token-level costs \(|\mathcal{H}|^2\). This enables practitioners to choose based on available compute and API access.

3. **Consistent empirical improvements across diverse settings**: Tables 1, 2, and 3 show uncertainty-aware MBR improves BLEU, chrF, COMET, LaBSE, ROUGE, and RMSE over single-model MBR baselines across finetuned Gemma-2B, Transformer models trained from scratch, and zero-shot prompted LLMs (Llama-3, Mistral, Gemma-2, Qwen-2). On IWSLT17, COMET improvements correspond to a >85% chance of human preference (Section 4.2, citing Kocmi et al. 2024).

4. **"For-free" improvements from unimodal posteriors**: Table 1 demonstrates that unimodal IVON posteriors (requiring no extra training overhead beyond standard optimization and the same decoding compute budget) yield consistent gains. This is practically appealing because it requires no additional training runs.

5. **Scaling and diversity analysis**: Section 4.5 (Fig. 3) systematically studies scaling with ensemble size and hypothesis set size, showing that token-level combination benefits from larger ensembles under ancestral sampling and that sequence-level combination is better for small hypothesis sets. Section 4.3 connects performance to prediction diversity, validated via temperature-adjusted sampling and snapshot ensembles.

## Weaknesses

### Fatal
None.

### Major

1. **Missing critical baselines for selective prediction**: Section 4.4 compares different variants of the paper's own expected utility criteria but does not compare against standard selective prediction baselines such as model confidence (likelihood), entropy-based methods (Ren et al., 2023), or semantic entropy (Kuhn et al., 2023), despite citing these works for background. Without these comparisons, the claim that expected Bayes' risk is a *good* criterion for abstention is unsupported—the paper only shows it works better than some alternatives within its own framework.

2. **No ablation of the additive union vs. set union**: The paper distinguishes itself from Kobayashi (2018, Alg. 1) by using an additive union (multi-set) that preserves sample counts rather than a set union, claiming this provides an unbiased estimate of Eq. (7). However, no experiment compares the multi-set approach against a simple set union to verify that this design choice matters empirically. Since this is one of the explicitly claimed differentiators from prior work, the lack of empirical validation is a notable gap.

### Minor

1. **No statistical significance testing or confidence intervals**: None of the reported improvements in Tables 1–3 are accompanied by confidence intervals, bootstrap estimates, or paired significance tests. Many improvements are modest (e.g., +0.2–0.6 BLEU), and without measures of variability the reader cannot assess whether these are reliable or within the noise of the evaluation.

2. **Diversity analysis lacks quantitative rigor**: Figure 1 presents a scatter plot with a trend line but reports no correlation coefficient, p-value, or goodness-of-fit measure. The claim that "performance correlates with diversity" remains qualitative. A more rigorous analysis (e.g., pairwise KL divergence, Pearson/Spearman correlation with significance) would strengthen the conclusions.

3. **No explicit limitations section**: The paper lacks a discussion of important limitations, including: (a) IVON's unimodal Gaussian posterior may underrepresent true parameter uncertainty; (b) the assumption that finetuning only LoRA parameters captures weight uncertainty in a restricted subspace; (c) increased storage and inference cost from maintaining multiple models; (d) token-level combination's reliance on token probabilities, unavailable from many black-box APIs; (e) evaluation focuses on relatively constrained generation tasks (MT, summarization) — generalizability to open-ended generation is unclear.

4. **Selective prediction evaluation limited to one dataset**: The analysis in Section 4.4 (Fig. 2) uses only IWSLT14. Generalizability of the findings to other tasks, domains, or model scales is unknown.

5. **No comparison to non-Bayesian ensemble baselines**: The paper compares IVON (Bayesian posterior) to single-model MBR and Deep Ensembles, but does not compare against simple ensembles formed by training the same architecture with different random seeds via standard (non-Bayesian) optimization. Such a comparison would help isolate whether the benefits come from the Bayesian posterior specifically or from ensembling multiple models generally.

### Trivial
None.

## Nice-to-Haves

- Report results under both matched-comparisons and matched-hypothesis-set-size conditions to disentangle potential confounds in the compute-matching strategy.
- Report wall-clock time or FLOPs in addition to matched MBR comparisons, as parallelization and communication overhead differ across methods.
- Include an ablation comparing additive union (multi-set) against a plain set union (Kobayashi, 2018) to validate the claimed differentiator.
- Release code and trained posterior models to facilitate reproducibility and adoption.

## Removed Points

Points from the reviews that are flagged to be removed; treat them with caution:

- **"Paper overstates lack of methods that consider uncertainty during decoding"**: The paper cites multiple works on uncertainty (Ren et al., 2023; Xiao & Wang, 2021; Fadeeva et al., 2024) and correctly notes that few methods *react to* or *adjust for* uncertainty during decoding — a claim supported by the cited literature. This is an accurate characterization, not an overstatement.
- **"The LoRA limitation should be discussed"**: The paper already discusses this (Section 4.2: "We hypothesize that this difference can be attributed to the use of LoRA for finetuning—which explores a smaller subspace of potential posterior parameters and may therefore pose a comparably easier learning problem"). The reviewer's concern is already addressed.
- **"Novelty is insufficient for a top venue"**: The paper transparently acknowledges prior work (Kobayashi, 2018; Farinhas et al., 2023) and clearly distinguishes its contribution (Bayesian decision-theoretic framing, additive union for unbiased estimation, comprehensive evaluation framework). This is an opinion about bar, not a verified weakness, and the paper's contributions are substantive.
- **"The paper should report results with both matched comparisons and matched hypothesis set size"**: This is a methodological suggestion, not a flaw in what is reported. The paper's chosen matching strategy is defensible and transparently described (App. A.4).
- **Figure readability complaints** ("small markers, many lines"): Formatting/style nitpick — parser and rendering artifacts, not author errors.
- **"The paper does not mention whether code will be released"**: The hard rules instruct removing criticisms that question the release status of artifacts. Code release is standard practice but not required for evaluation of the scientific contribution, and the paper is under review rather than camera-ready.

## Novel Insights

The most useful insight from the reviews is that the paper's contributions would be significantly strengthened by directly comparing the proposed framework against the specific prior methods it claims to improve upon (Kobayashi's set-union approach for the ablation, and Ren/Kuhn-style selective prediction methods for the abstention analysis). The reviews also surface a tension: the paper is simultaneously praised for its principled Bayesian framing and criticized for essentially being ensembling — but the reviews do not adequately grapple with the fact that the paper's value lies precisely in providing a *theoretical justification* for what was previously done ad-hoc, which is a real form of scientific contribution even if the mechanics resemble existing practice.

## Suggestions

1. **Add a direct comparison to Kobayashi (2018)'s set-union approach** as an ablation in the main experiments — this would validate the additive union as a meaningful design choice and directly address the most prominent prior work.
2. **Add standard selective prediction baselines** (entropy-based abstention, model confidence thresholds) to Section 4.4 to substantiate the claim that expected Bayes' risk is a useful criterion for abstention.
3. **Report confidence intervals or bootstrap estimates** for the main results (Tables 1–3) to allow readers to assess the reliability of modest improvements.
4. **Add a limitations section** explicitly discussing the caveats of the unimodal posterior approximation, LoRA-only uncertainty, storage costs, and the scope of evaluated tasks.
5. **Quantify the diversity correlation** in Section 4.3 with a correlation coefficient (Pearson or Spearman) and associated significance test.

## Score and Decision

The paper proposes a well-motivated extension to MBR decoding with a principled Bayesian foundation, extensive experiments, and consistent empirical gains. The weaknesses are real but addressable — missing baselines for selective prediction, no ablation of the additive union, lack of statistical rigor, and missing limitations discussion. None of these invalidate the core contribution (that incorporating weight uncertainty improves MBR decoding), and most could be addressed with additional experiments (selective prediction baselines, additive union ablation, confidence intervals) rather than requiring a fundamentally new approach. The paper represents a solid contribution with incremental but meaningful novelty, and the experiments are fairly comprehensive in scope. The weaknesses lower confidence but do not undermine the core findings.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>