Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

This paper systematically studies scaling properties of different LLM finetuning methods (full-model tuning, prompt tuning, LoRA) across multiple dimensions: LLM model size, pretraining data size, PET parameter size, and finetuning data size. Using bilingual LLMs (1B–16B) trained on two language pairs, the authors propose a multiplicative joint scaling law relating finetuning data to each other factor, finding that (1) LLM model scaling benefits finetuning more than pretraining data scaling, (2) scaling PET parameters is ineffective, and (3) the optimal finetuning method is highly task- and data-dependent.

## Strengths

- **Systematic multi-factor study of LLM finetuning scaling.** The paper covers three finetuning methods (FMT, prompt tuning, LoRA), two LLM families (En-De, En-Zh from 1B to 16B), three downstream tasks (two translation, one multilingual summarization), and four scaling factors — a broader scope than prior work (e.g., Hernandez et al. 2021, which focused on transfer vs. scratch training).

- **Empirically validated finding that PET parameter scaling is ineffective.** The paper shows that scaling prompt length or LoRA rank yields marginal or even negative gains ($|\alpha_t| \ll 1e-2$) across tasks and methods. This is a practically useful result with clear implications for practitioners deploying PET methods.

- **Identification of task- and data-dependent critical points for method selection.** Using the fitted joint scaling law, the paper shows that the crossover points between FMT, prompt tuning, and LoRA vary dramatically across tasks, demonstrating that no single finetuning method is universally optimal — an honest negative result that challenges naive heuristics.

- **Zero-shot generalization analysis.** The paper evaluates how finetuning affects generalization to related tasks, finding that PET methods (which freeze most LLM parameters) better preserve zero-shot capability, especially with larger base LLMs. This is a non-obvious insight relevant to deployment scenarios.

- **Large-scale, carefully designed experiments.** The study uses two bilingual LLM families pretrained from scratch, multiple held-out points per scaling dimension, and three random subsets to reduce noise — representing a substantial empirical effort.

## Weaknesses

### Fatal
None.

### Major

- **The comparison between LLM model scaling and pretraining data scaling is weakened by the use of intermediate checkpoints as proxies.** The paper (line 88) acknowledges using intermediate pretrained checkpoints for pretraining data scaling due to computational constraints. An intermediate checkpoint is not equivalent to a model trained on fewer tokens from scratch — training dynamics, data ordering, and learning rate schedule differ. While this is a pragmatic approximation commonly used in scaling law research (e.g., Kaplan et al. 2020), it introduces systematic uncertainty into the estimated exponent αₚ. Consequently, the headline claim that "LLM finetuning benefits more from LLM model scaling than pretraining data scaling" (αₘ > αₚ) is less reliable than the paper suggests. The paper's statement of this finding as a strong conclusion (abstract, Section 4, conclusion) should be qualified more explicitly, and the intermediate checkpoint proxy should be elevated from a brief acknowledgement to a primary caveat.

- **Evidence for the multiplicative joint scaling law over the additive alternative is mixed, and the claim of "generalization" is overstated.** Table 1 shows that the multiplicative form clearly outperforms the additive form for LLM model size (avg. 0.0048 vs. 0.0079 held-out error, a ~39% reduction) and moderately for PET parameters (0.004 vs. 0.005), but for pretraining data size the two forms are essentially tied (0.0068 vs. 0.0069). This comparison is reported only on one task (WMT En-De). The paper claims the law "generalizes to different settings" (abstract) but the supporting evidence spans only three tasks, two of which are from the same WMT machine translation family, and all are closed-form generation tasks. The generalizability to open-ended tasks (instruction following, dialogue, creative generation) remains untested, and the paper's own limitations section acknowledges this. A more circumspect characterization of the law's scope is warranted.

### Minor

- **No confidence intervals or uncertainty estimates on fitted scaling exponents.** The paper reports αₘ, αₚ, β, αₜ as point estimates without any error quantification (bootstrap or otherwise). Given that only 5 model sizes are available for fitting αₘ, and the paper itself acknowledges extrapolation mismatches at 16B (Section 4: "particularly for LoRA and Prompt on WMT19 En-Zh"), the statistical significance of differences like αₘ > αₚ cannot be assessed. This is a standard concern in empirical scaling law papers, but it limits confidence in the quantitative comparisons.

- **Critical point analysis extrapolates beyond observed data ranges.** For PET methods, finetuning data sizes range only up to 100K examples, yet the critical point analysis (Figure 6) estimates crossover points far beyond this range. The reliability of these extrapolated values is unclear, especially given the acknowledged fitting mismatches at extrapolation boundaries.

### Trivial
None.

## Nice-to-Haves

- Error bars or variance indicators on scaling plots (Figures 2–5) showing the spread across the three random subsets, which would help readers assess fit quality.
- A side-by-side visualization of additive vs. multiplicative fits for a representative setting so readers can visually judge which form better captures the data.
- Extending the study to at least one open-ended generation task (e.g., instruction following) to test generalizability beyond closed-form tasks, though the paper acknowledges this is beyond its current scope.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. *"The fitting procedure (first estimate β,E from two factors, then fix them and refit per factor) is ad hoc and not derived from any theoretical principle."* — This is a standard approach in scaling law fitting (see e.g., Kaplan et al. 2020, Hoffmann et al. 2022 for similar staged fitting). It is a reasonable engineering practice to reduce overfitting, not an "ad hoc" flaw.

2. *"Fitted separately for each factor X with different parameters A_X, α_X... The paper effectively fits a product of two power laws per factor, not a unified multi-factor law."* — The paper explicitly states that this is by design (Section 3: "treat finetuning data as the pivoting factor and perform joint scaling analysis between it and every other factor separately"), due to the computational cost of jointly modeling all factors. This is a scoping choice, not a flaw.

3. *Zero-shot result criticism about lack of significance tests* — The paper reports BLEURT scores averaged over multiple source languages; lack of formal significance tests is standard practice in large-scale empirical papers and does not invalidate the observed trends.

4. *"The paper does not report confidence intervals... making it impossible to judge whether observed differences are significant."* — This is a valid concern (retained as a Minor weakness above), but the critic's framing that it makes the core claims "not statistically robust" and thus unreliable is over-stated. Scaling law papers routinely report point estimates without confidence intervals, though confidence bands would strengthen the analysis.

5. *"Should include at least one open-ended generation task"* — Outside the paper's stated scope; the paper acknowledges this as a future direction.

6. *"Pretrain models from scratch at different data sizes"* — This would be ideal but is extremely expensive (the paper already pretrains LLMs from scratch for two language families at 5 sizes each). The paper uses a common approximation and acknowledges the limitation.

## Novel Insights

The reviews do not surface a genuinely novel insight beyond the paper's own contributions. The observation that scaling PET parameters (LoRA rank, prompt length) yields negligible gains is a useful practical finding that the reviews correctly highlight. The cross-task variability of "critical points" for method selection is another genuine contribution.

## Suggestions

1. **Elevate the intermediate checkpoint caveat.** The paper should clearly state in the abstract and conclusion that the comparison between model scaling and pretraining data scaling uses intermediate checkpoints as a proxy, and that the quantitative comparison (αₘ > αₚ) should be interpreted with this in mind.

2. **Add uncertainty quantification.** Report bootstrapped confidence intervals on all fitted exponents (αₘ, αₚ, β, αₜ), at least for the key comparisons. This would greatly strengthen the reliability of the quantitative claims.

3. **Present additive vs. multiplicative comparisons on more than one task.** Even a second task (e.g., MLSum) would substantially strengthen the case that the multiplicative form is broadly preferred.

4. **Tone down the "generalization" claim.** The joint scaling law is validated on closed-form generation tasks (translation and summarization). The paper should more precisely scope this claim rather than asserting it "generalizes to different settings."

5. **Add variance indicators to scaling plots.** Show run-to-run variability across the three random subsets in Figures 2–5 so readers can judge the noise level.

## Score and Decision

This paper tackles an important and underexplored question — scaling properties of LLM finetuning across multiple factors — and offers several useful empirical observations: the ineffectiveness of PET parameter scaling, the task-dependent nature of optimal method choice, and a multiplicative joint scaling law that fits the data well for model size and finetuning data. The experimental design is substantial and systematic. However, the headline comparison between model scaling and pretraining data scaling is weakened by the use of intermediate checkpoints as proxies (an acknowledged limitation), and the claim that the multiplicative law "generalizes" is overstated given the limited task diversity. The absence of uncertainty quantification on fitted exponents further limits confidence in quantitative comparisons. Despite these limitations, the core findings about PET scaling and task-dependence are solid, and the study fills a genuine gap in the literature. The paper would benefit from more circumspect framing of its strongest claims and additional uncertainty analysis.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>