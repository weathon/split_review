Now I have all the information needed. Let me write the consolidated review.

## Summary

The paper presents a systematic empirical study of activation sparsity in decoder-only Transformer LLMs. It proposes PPL-\(p\%\) sparsity, a performance-aware metric that adaptively sets layer-wise sparsity thresholds based on a target PPL increase, and then uses it to characterize how activation sparsity scales with training data, activation function (ReLU vs. SiLU), width-depth ratio, and model scale (0.1B–1.2B). Key findings include: (1) opposite training-time sparsity trends for ReLU (sparsity increasing with data) vs. SiLU (sparsity decreasing with data), (2) a monotonic relationship between activation ratio and width-depth ratio below a bottleneck, and (3) weak dependence of limit sparsity on parameter scale at similar width-depth ratios.

## Strengths

- **Novel performance-aware sparsity metric (PPL-\(p\%\)).** The paper improves over prior CETT-based metrics by directly tying sparsity to a target PPL degradation, making it both versatile (applicable to any activation function) and practically interpretable. Figure 3 demonstrates it achieves a better PPL-sparsity trade-off than Straightforward ReLU, Top-k, and FAT-\(\epsilon\) baselines across model scales.

- **First quantitative scaling laws for activation sparsity in decoder-only LLMs.** The paper identifies and fits mathematically explicit forms — a logspace power-law for ReLU (Eq. 4) and a vanilla power-law for SiLU (Eq. 5) — relating activation ratio to training data. These go beyond prior qualitative observations and enable training-time prediction of sparsity.

- **Useful finding: ReLU yields higher sparsity with opposite data trend vs. SiLU.** ReLU consistently achieves higher sparsity than SiLU at matched scales, and its sparsity *improves* with more training data (while SiLU's degrades). This gives actionable architectural guidance if comparable performance can be confirmed.

- **Width-depth analysis provides practical architecture guidance.** Figure 5 shows activation ratio increases linearly with width-depth ratio below a bottleneck (~114 for 0.1B), implying deeper models are sparser. Combined with the loss curve (Figure 6), the paper identifies a concrete interval for optimal width-depth ratio, offering actionable design guidance.

- **Scale-insensitivity of limit activation sparsity is supported by mechanistic evidence.** Beyond the limit estimates (Figure 7), the paper provides complementary analyses of activation frequency distributions across datasets (Figure 9) and token-wise activation ratios (Figure 10), showing that activation patterns are similar across scales — strengthening the claim beyond curve fitting alone.

## Weaknesses

### Fatal
None.

### Major

1. **Claim of "comparable performance" between ReLU and SiLU is unsubstantiated by direct evidence.** The paper repeatedly asserts that ReLU and SiLU achieve comparable performance (abstract, Section 1 bullet 2, Section 4.2), yet it provides no dedicated comparison — no table of validation loss, no downstream task scores (commonsense reasoning, reading comprehension) contrasting the two activation functions at matched scales and token counts. Figure 3 compares PPL curves, which offers partial support, but the paper's central practical recommendation ("replace SiLU with ReLU") requires explicit performance verification. *Why it matters*: This is a key practical implication; if SiLU models actually outperform ReLU at matched sparsity levels, the recommendation is misleading. The gap is addressable but currently limits the strength of the paper's core narrative.

### Minor

2. **Single-run scaling curves without uncertainty quantification.** Each configuration (scale × activation function) appears to be trained once. Scaling-law claims about fitted parameters \(A_0, c, \alpha\) and especially about the estimated *limits* (Figures 7–8) have unknown reliability without multiple seeds or bootstrap-based intervals. *Why it matters*: The paper's most novel claims are quantitative laws; the absence of any variance estimate makes it impossible to assess whether observed cross-scale or cross-activation differences are meaningful. However, this concern is partially mitigated by community practice — most scaling-law papers (e.g., Kaplan et al., Hoffmann et al.) use single runs — so it is not a fatal flaw but weakens the empirical rigor.

3. **Narrow scale range for the scale-insensitivity claim (0.1B–1.2B, <1 order of magnitude).** The paper reports only ~2–3% variation in limit activation ratio across five scales, but this range is modest compared to typical scaling-law work spanning 2–4+ orders of magnitude. The observed "insensitivity" could break down at larger scales (e.g., 7B+). *Why it matters*: The claim of scale insensitivity is central but the supporting data is confined to a small window. The activation-pattern analyses (Figures 9–10) help, but the conclusion is extrapolative.

4. **Width-depth ratio analysis limited to one setting (0.1B, ReLU only).** The bottleneck point (~114) and the linear trend are derived from a single model family. It is unclear whether the pattern holds for SiLU or at other parameter scales. The paper's own language is appropriately cautious ("for 0.1B"), but the takeaway in the Discussion (Section 5) treats the bottleneck as general guidance. *Why it matters*: An architectural recommendation to prefer deeper models rests on a pattern observed in only one configuration.

5. **The combinatorial explanation for faster convergence of smaller models (Eq. 6) is speculative.** The paper labels this a "Deduction," but it is an untested hypothesis — it counts possible neuron-grouping assignments but does not model optimization dynamics, training time, or convergence rate. The equation does not constitute evidence. *Why it matters*: While clearly identified as an explanatory hypothesis, it is presented alongside the empirical results without a disclaimer about its tentative nature.

### Trivial

6. **Inconsistent threshold for training data sufficiency.** Section 3.2 states "no less than 80 times the scale of non-embedding parameters," but the caption of Figure 4 states "no less than 190 times." The discrepancy is unexplained.

7. **No comparison with alternative functional forms for the fits.** The chosen forms (logspace power-law, vanilla power-law) are justified only as "after careful attempts" with no residual analysis or comparison to alternatives (e.g., saturating linear, log-log polynomial).

## Nice-to-Haves

- A discussion of whether the PPL-\(p\%\) metric's thresholds are stable across different choices of validation data would increase confidence in the metric's robustness.
- The width-depth analysis would be considerably strengthened by checking at least one additional model scale (e.g., 0.4B) or activation function (SiLU) to test generalization.
- Reporting the specific width-depth ratio values used (the 9 sampled configurations) would aid reproducibility.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that Figure 3 and Table 1 validation uses only 0.1B/0.2B models.** The paper explicitly states "models of different scales" for Figure 3, and Table 1 covers 0.1B–1.2B. This criticism is not supported by the paper text.
- **Criticism about MoE being mentioned only once.** MoE appears only as motivation in the introduction to contrast with intrinsic sparsity — this is appropriate scoping, not a weakness.
- **Criticism about missing discussion of computational overhead of binary search.** This is a minor implementation detail, not a structural flaw.
- **Critique about the "80 times parameter scale" threshold being arbitrary.** While the reviewer questions the justification, this is a reasonable design choice for ensuring sufficient training; no alternative threshold is standard in the literature. The inconsistency with "190 times" (trivial point #6 above) is noted separately.

## Novel Insights

The most interesting insight from the review process is that the paper's core claims can be stratified by evidential strength. The discovery of *opposite* sparsity-data trends for ReLU vs. SiLU (increasing vs. decreasing) is well-supported by clear empirical curves across 5 scales. However, the derivative claims built on this — that ReLU and SiLU have "comparable performance" and that the width-depth bottleneck is general — are inferences that outrun the current evidence. The paper is strongest as a descriptive empirical study of sparsity dynamics and weakest in its prescriptive architectural recommendations. A reader should appreciate the former while treating the latter as suggestive rather than conclusive.

## Suggestions

1. **Add a dedicated ReLU vs. SiLU performance table.** Show validation loss and downstream task scores (commonsense reasoning, reading comprehension) for both activation functions at 2–3 matched scales and training token counts. This single addition would directly address the most significant evidential gap.
2. **Run at least 2–3 seeds for a representative subset of configurations** (e.g., 0.1B and 0.4B for both activations) to provide error estimates on the fitted scaling-law parameters.
3. **Extend the width-depth analysis to at least one additional scale** (e.g., 0.4B SiLU) to test whether the bottleneck point and linear trend generalize.
4. **Reframe the scale-insensitivity claim** with explicit caveats about the range (0.1B–1.2B) and note that the observed weak variation (~2-3%) may be within the fitting noise given single-run data.
5. **Label the combinatorial argument (Eq. 6) more clearly as a conjecture** rather than a deduction, and consider removing it or placing it in a "possible explanation" paragraph separate from the empirical results.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>