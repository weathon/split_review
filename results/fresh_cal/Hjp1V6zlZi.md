Now I have a complete picture. Let me compose the final consolidated review.

## Summary

This paper identifies and investigates **Extreme UniDA** — a regime where source-private classes substantially outnumber shared classes (SPCR > 1) — showing that existing partial domain alignment methods degrade because the noise from misweighted private samples exceeds the noise tolerance level. The paper proposes adding a self-supervised learning (SSL) loss on target-only data to preserve target feature structure and mitigate source-private bias. SSL is shown to reduce dimensional collapse in target representations and lower the noise rate of alignment weights. Experiments on four benchmarks (Office-31, Office-Home, VisDA, DomainNet) demonstrate consistent improvements when SSL is added to both adversarial-based and optimal-transport-based UniDA methods, with particularly large gains under high SPCR.

## Strengths

1. **Systematic characterization of Extreme UniDA via SPCR and failure analysis.** The paper introduces the Source-Private to Source-Common Ratio (SPCR) as a quantitative metric (Section 2) and provides a noise-tolerance analysis (Figure 3) showing that under high SPCR (e.g., 5) the noise rate of existing alignment weights exceeds the tolerance level, explaining why partial alignment fails. This directly supports the paper's central claim that existing methods struggle in extreme settings.

2. **Mechanistic explanation and evidence for source-private bias and SSL mitigation.** A toy experiment (Section 3.3, Figure 2) demonstrates that training with source-only loss distorts target feature structure while SSL preserves it. This is validated on real data via singular value spectrum analysis (Section 4.3, Figure 6), which shows dimensional collapse worsens with SPCR and that SSL reverses it. These findings directly support the paper's argument for why SSL helps in Extreme UniDA.

3. **Strong empirical gains in Extreme UniDA across multiple methods and datasets.** Tables 1 and 2 report substantial H-score improvements when SSL is added to adversarial methods (e.g., +17.8% on Office-Home, +20.4% on VisDA, +10.1% on Office, +7.5% on DomainNet) and consistent gains for OT-based methods (e.g., +11.2% on VisDA, +3.5% on Office). Figure 5 further shows improvements increase monotonically with SPCR.

4. **Ablation study confirming robustness to target-private classes.** Section 3.1 and Figure 4a compare applying SSL only on target common classes versus all target classes. The performance drop from including private classes is minor (<2% H-score), showing the method does not critically depend on perfect separation of target data.

5. **Demonstration that SSL reduces noise in partial domain alignment.** Figure 4b (Section 3.2) shows that adding SSL lowers the average noise rate of alignment weights by approximately 10 percentage points, providing concrete evidence for the proposed mechanism.

## Weaknesses

### Fatal
None.

### Major

1. **No error bars or multi-run statistics on any result.** The main results (Tables 1 and 2) and all ablation plots (Figures 4–6) report only point estimates. Without standard deviations or multiple seeds, the statistical reliability of reported gains — especially the smaller ones on OT methods in the general (non-extreme) setting — cannot be assessed. This is the most significant evidential gap. *Note: The paper reports gains of 1.7%–11.2% on OT methods in the extreme setting (with 11.2% on VisDA being non-trivial), so this weakness partially attenuates the strongest claims but remains important for the full set of results.*

### Minor

1. **Noise-tolerance experiment (Section 2.2) is procedurally underspecified.** The paper defines the noise rate (Eq. 3) and reports tolerance thresholds (Figure 3), but does not explain *how* noise is injected/controlled to produce the "misclassification rate under different noise levels" curves (Figures 3a, 3c). It is also unclear how the 0.5 threshold on continuous weighting functions is applied. This does not undermine the paper's main claims but limits reproducibility of the diagnostic analysis.

2. **No hyperparameter sensitivity analysis for the SSL weight α.** The unified objective (Eq. 5) introduces α as a weighted hyperparameter, but the paper reports no study of how results vary with α. Since the SSL loss is the paper's core novel component, understanding its sensitivity is important for practitioners.

3. **No discussion of computational overhead.** The paper claims the method is "lightweight" but does not report training time or additional memory costs relative to the baselines.

### Trivial
None.

## Nice-to-Haves

- Reporting results on more recent UniDA methods that focus on open-set classifiers (e.g., Lu et al. 2024) could further strengthen the paper's claim that open-set classification alone does not solve Extreme UniDA. The paper explicitly scopes these out ("Since these methods do not emphasize domain alignment, they are not covered"), which is a reasonable decision, but including at least one such comparison would be additive.
- A brief discussion of how the 0.5 threshold in the noise rate definition relates to the specific weighting schemes used in practice would improve clarity.

## Removed Points

These points were raised by reviewers but are removed or corrected after cross-checking against the paper:

- **"Modest/negligible gains on OT methods (0.4%–3.5%)" (Harsh Critic Point 3):** REMOVED. The critic conflated general setting gains with Extreme UniDA gains. The paper reports *extreme* setting OT gains of 1.7%–11.2% (including +11.2% on VisDA). The 0.4% and 0.5% figures refer to the *general* (non-extreme) setting, which is not the paper's focus. The critic's numerical claim is factually incorrect for the Extreme UniDA setting that is the paper's central contribution.

- **"Incomplete baseline coverage — missing recent methods" (Harsh Critic Point 2):** REMOVED. The paper's Related Work (Section 5) explicitly states: *"Another line of research…focuses on designing robust open-set classifiers…Since these methods do not emphasize domain alignment, they are not covered in our paper."* The paper's contribution is about improving domain alignment, and it reasonably scopes out methods that operate on a different principle. The chosen baselines (UAN, CMU, DANCE, UniOT) are the standard domain-alignment-based UniDA methods with open-source implementations, which is an appropriate criterion.

- **"Newer weighting mechanisms may already address high SPCR" (Harsh Critic, implied):** REMOVED. The paper's noise-tolerance analysis (Figure 3) explicitly measures the observed noise rates of *existing weighting mechanisms* (entropy, confidence, probability, ensemble) and shows they all exceed tolerance under high SPCR. This directly addresses the concern that newer weighting schemes might solve the problem — the analysis is about the fundamental limitation of weight-based partial alignment, not about specific implementations.

- **Suggestions from the Strength Finder that conflict with verified weaknesses:** All five strengths from the Strength Finder are concrete, specific to the paper, and grounded in evidence. None are dropped.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful feedback (error bars, reproducibility details) but do not contribute new analytical observations about the problem or method beyond what the paper already provides.

## Suggestions

1. **Report all main results with standard deviations over at least 3 random seeds.** This is the single most important improvement. It would address the main evidential concern and is standard practice for empirical deep learning papers.
2. **Detail the noise-injection procedure for Figure 3.** Specify how different noise levels are achieved (e.g., by artificially manipulating weights, adding random label flipping, or other mechanisms). Clarify how the 0.5 threshold is applied to continuous weighting functions from different methods (entropy, confidence, etc.).
3. **Add a hyperparameter sensitivity plot** for α (the SSL loss weight) over a range (e.g., {0.01, 0.05, 0.1, 0.5, 1.0}) on at least one dataset setting.
4. **Report training time** per epoch or per run compared to baselines to substantiate the "lightweight" claim.

## Score and Decision
MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>