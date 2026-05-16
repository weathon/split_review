Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper studies the value of noisy data for training diffusion models by systematically varying the mixture of clean and noisy training samples across three datasets (CIFAR-10, CelebA-HQ, ImageNet) with over 80 trained models. The central empirical finding is that a model trained on a mixture of a small fraction (e.g., 10%) of clean data and a large fraction (90%) of highly noisy data (σ=0.2) achieves FID close to the clean-data baseline (ImageNet: 1.68 vs. 1.41), dramatically outperforming training on either the small clean set alone (10.57) or the full noisy set alone (5.32). The paper also develops minimax-optimal estimation rates for Gaussian Mixture Models with heterogeneous noise levels as a theoretical parallel.

## Strengths

- **Clear and well-supported core empirical finding.** Table 1 and Table 2 provide systematic evidence across all three datasets that adding a small fraction of clean data to a large noisy pool recovers nearly all the performance of clean-only training. The result is consistent across corruption levels (σ∈{0.05, 0.1, 0.2}) and across dataset sizes spanning two orders of magnitude (30K to 1.3M). The extreme-case experiments (1% clean + 99% noisy; σ=0.4) further strengthen the claim.

- **Large-scale systematic study.** Training over 80 models with controlled variation along three axes (dataset, noise level, mixture ratio) establishes scaling trends rather than cherry-picked anecdotes. The inclusion of standard deviations from multiple runs adds credibility.

- **Novel theoretical contribution on its own terms.** The minimax estimation rates for heterogeneous-variance GMMs (Theorem 1 and matching lower bound) are technically interesting. The key qualitative insight — that noisy samples are downweighted only polynomially for dimensionality reduction but exponentially (in the number of components) for fine-grained estimation — is clean and intuitive. The algorithmic improvement over prior work (improving the failure-probability dependence from √log (1/δ) to (log (1/δ))^{1/(4k−2)}) is a genuine technical refinement.

- **Practical training recipe.** Algorithm 1 combines standard DSM and Ambient DSM losses with no extra computational overhead from consistency losses, making the approach directly usable in realistic data-curation pipelines.

## Weaknesses

### Fatal

None.

### Major

None. The core empirical finding is robust and the experimental design is sound. The weaknesses below are non-fatal issues of framing, precision, and exposition.

### Minor

- **Overstated connection between theory and experiments.** The paper describes the GMM analysis as "theoretical evidence" (abstract) and "a theoretical explanation" (contributions) for the empirical findings on diffusion models. This overstates the link. The theory studies a k-atomic distribution convolved with sample-dependent Gaussian noise, estimated via moment methods; the experiments train diffusion models on natural images using score matching. The gap is acknowledged in the limitations section ("might not capture all the intricacies of real distributions"), but the abstract and contributions present a stronger claim. The theory provides an insightful *analogy* and qualitative intuition (exponential gap in utility between noisy and clean samples), but does not constitute direct evidence for the observed scaling behavior in diffusion models. The paper would be more accurate by framing the theory as a parallel, independent contribution whose qualitative insights align with the experiments, rather than as evidence or explanation.

- **The data-pricing analysis (Section 4.4) overstates its precision.** The bounds (e.g., 1.5 ≤ 1/c₀.₂ ≤ 1.75) are derived from a small number of pairwise inequality constraints, and their narrowness largely reflects the sparsity of the comparison grid rather than an empirically validated sharp relationship. The claim that "narrow ranges lend credibility" is not fully justified — with few constraints, the bounds are mechanically tight regardless of whether the underlying relationship is clean. The paper should present these as rough qualitative estimates (noisier samples are worth less; larger datasets dilute the penalty) rather than as precise exchange rates.

- **The condition in Theorem 1 (bounded `max_i 1/σ_i⁴`) is not discussed in relation to the experiments.** The paper explains the condition's formal role (ensuring sufficient effective samples) but does not discuss whether it is satisfied in the experimental setup, or how mild or restrictive it is for the two-noise-level setting studied. Since the theory is presented as supporting the experiments, clarifying this connection would help readers assess the theory's relevance.

- **The "pushing performance" ablation (Section 5.3) does not test whether the same tuning benefits the clean baseline.** The sequence of improvements (more training → adjusted sampling → consistency → weight decay) brings the mixture model from FID 1.68 to 1.55, leaving a gap of 0.14 to the clean baseline of 1.41. It is possible that the same tuning interventions would also improve the clean baseline, potentially widening (rather than narrowing) the gap. Acknowledging this caveat would make the comparison more balanced.

### Trivial

- The paper reports standard deviations for FID scores but does not explicitly state over how many random seeds/runs these were computed (e.g., "mean ± std over 3 seeds").

## Nice-to-Haves

- Test whether the same tuning interventions used in Section 5.3 (more steps, adjusted sampling, consistency fine-tuning, weight decay) improve the clean-data baseline. This would clarify whether the remaining gap is truly shrinking or simply being masked by undertuned baselines.
- A finer-grained grid of noise levels (beyond the three discrete values) to better characterize the transition where noisy samples cease to be useful.
- A rough back-of-the-envelope calculation using the GMM theory: estimate an effective "k" for each dataset and compute how many purely noisy samples the theory suggests would be needed to match a given clean-only performance — even as a speculative extrapolation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The wording 'impossible... to match the performance' could be read as a universal impossibility."** The abstract explicitly says "at these sample sizes," and the introduction clarifies "without a significant hit (that is exponential...)." The paper already contains the qualification the reviewer requests. *(Removed: point already addressed by the paper.)*

- **"Why no mixture experiments for CIFAR-10 at p=90% noisy?"** The full grid is presented in Table 2. For CIFAR-10, the row corresponding to "p% clean" at p=10% (i.e., 90% noisy) is reported for all three noise levels. The reviewer appears to have misread the table. *(Removed: factually incorrect.)*

- **"Missing appendix content / inaccessible appendix."** The appendix is present in the original submission; it was stripped by the PDF parser. The rule instructs removing criticisms about missing appendix content. *(Removed: parser artifact.)*

- **"Low-frequency vs. high-frequency intuition is not experimentally tested."** The paper presents this as "intuition" (line 149), not as a tested claim. Labeling an explicitly marked intuition as untested is not a valid criticism. *(Removed: not a claimed contribution.)*

- **Strength: "Quantitative data-pricing bounds... validates the theoretical prediction."** This strength conflicts with the verified weakness that the pricing analysis is underdetermined and may give a false sense of precision (weakness wins per rules). The pricing framework is a creative tool, but its precision claims are not validated at the level the strength implies. *(Downgraded from strength: moved here due to conflict with verified weakness.)*

## Novel Insights

The most interesting observation emerging across the reviews — beyond the paper's own contributions — is the asymmetry in how reviewers evaluated the theory-practice connection. The harsh critic correctly identifies that the theory does not constitute direct evidence for the diffusion experiments, yet the core qualitative insight from the theory (exponential gap in utility between clean and noisy samples) is directionally consistent with all experimental results. This suggests the paper could be strengthened by more carefully delineating what "theoretical evidence" means in an empirical paper: the theory provides a *mechanism* (heterogeneous-variance GMMs) in a simplified setting that qualitatively reproduces the same pattern, which is useful for intuition but not for quantitative prediction. Few empirical papers with theoretical components manage this distinction well, and this paper's framing would benefit from treating that boundary more explicitly.

## Suggestions

1. Reframe the theory section as a complementary conceptual analysis rather than "evidence" or "explanation" for the diffusion experiments. The experiments are the primary contribution; the theory provides an independent result whose qualitative trends align.

2. Add a brief discussion of whether the condition in Theorem 1 (bounded max_i 1/σ_i⁴) is mild or restrictive in the two-noise-level experimental setting.

3. Explicitly state the number of random seeds used for the FID standard deviations.

4. Add a caveat that the "pushing performance" gains may partially reflect undertuned default hyperparameters and that the same interventions were not tested on the clean baseline.

## Score and Decision

The paper makes a clear, well-supported empirical contribution with practical implications for dataset curation. The experiments are thorough (80+ models, three datasets, multiple noise levels), and the core finding is robust and actionable. The theoretical results are technically interesting on their own terms, though their connection to the experiments is somewhat overstated. The weaknesses are all addressable and do not undermine the central contribution. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>