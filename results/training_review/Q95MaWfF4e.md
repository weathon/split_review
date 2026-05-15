Here is my consolidated meta-review.

---

## Summary

This paper identifies a flaw in standard Concept Activation Vector (CAV) computation: linear classifier weights (filter-CAVs) optimize class-separability rather than the true concept signal direction, picking up distractor components. The authors introduce pattern-CAVs, computed as the covariance between latent activations and concept labels (a closed-form, hyperparameter-free estimator drawn from neuroimaging literature). Controlled experiments with ground-truth concept directions show pattern-CAVs achieve significantly higher alignment, and downstream applications (TCAV and ClArC model correction) benefit from the improved direction estimate across multiple architectures and datasets.

## Strengths

- **Identifies a genuine, practically important limitation of filter-based CAVs.** The paper provides a clear mathematical decomposition showing that filter-CAVs (ridge, SVM, etc.) optimize separability and thus capture distractor components (Eq. 1), while the signal pattern is something different. The connection to the neuroimaging filter/pattern dichotomy (Haufe et al., 2014) is insightful and well-positioned.

- **Introduces a simple, principled, and immediately usable alternative.** Pattern-CAVs (Eq. 3) require no hyperparameter tuning, no regularization selection, and are computationally cheaper than training linear classifiers. This makes them directly applicable in any existing CAV pipeline.

- **Controlled experiments with ground-truth directions convincingly demonstrate superior alignment.** Using three datasets (ISIC2019, Bone Age, FunnyBirds) and three architectures (VGG16, ResNet18, EfficientNet-B0), Fig. 3 shows pattern-CAVs achieve consistently higher cosine similarity with ground-truth concept directions across all convolutional layers, with standard errors reported. The invariance to feature pre-processing (Fig. 4) is a practical bonus.

- **Downstream impact demonstrated on two major CAV applications.** Pattern-CAVs improve TCAV scores (Fig. 5) and model correction via ClArC (Table 1, Fig. 7-8). The qualitative heatmaps (Fig. 6, 8) visually confirm that pattern-CAVs localize concepts more precisely and lead to more effective artifact removal.

- **Honest discussion of limitations.** Section 4.5 acknowledges that for applications prioritizing class-separability (e.g., post-hoc concept bottleneck models), filter-CAVs may be preferable, demonstrating nuanced understanding of the trade-off.

## Weaknesses

### Fatal
None.

### Major
- **Overclaim that pattern-CAVs focus "solely" on concept signals (Abstract, line 7; Conclusion, line 397).** The pattern-CAV is computed as cov[A, t], which captures *everything* that covaries with the concept label. If a distractor is partially correlated with the concept — a common real-world scenario — it will be included in the pattern-CAV just as it influences filter-CAVs. The toy experiments and controlled datasets carefully construct settings where distractors are uncorrelated with the concept, so the method works ideally there, but the paper never tests the correlated-distractor case. The strong language ("solely focussing on concept signals," "disregarding distractors") overstates the method's theoretical guarantees. The Limitations section does not address this. This does not invalidate the core contribution (pattern-CAVs are still better aligned than filter-CAVs in the uncorrelated setting, and even with correlated distractors they remain the correct signal estimate), but the phrasing should be softened and the limitation acknowledged.

### Minor
- **Missing statistical significance for the core ClArC results (Table 1).** While the alignment plots (Fig. 3) report standard errors, the downstream application table that drives the headline contribution reports only point estimates. For VGG16 Bone Age, pattern-CAV achieves 0.755 biased accuracy versus ridge regression at 0.743 — a small difference that could be within noise. Without multiple runs or confidence intervals, the reader cannot evaluate whether pattern-CAV is reliably better for these particular numbers. The evidence remains suggestive rather than conclusive for individual table entries (though the consistent pattern across models, layers, and datasets in Fig. 7 mitigates this concern).

- **Unsupported claim about filter-CAV sensitivity in low-data scenarios (Section 3.3, line 155).** The claim that "filter-based CAVs face further challenges, including sensitivity to regularization strength and random seeds, particularly in low data scenarios" is plausible but never tested. No experiment in the paper examines this. This should be either supported or removed.

- **Missing analysis of ResNet18 FunnyBirds results.** The paper notes that "all CAV variants achieve a perfect score for ResNet18" (line 292) but offers no explanation. Understanding why — whether ResNet's features are less noisy, the concept is more easily separable, or some other factor — would strengthen the analysis.

- **Correlated-distractor scenario not tested.** As noted above under Major, the paper never tests the case where distractors are partially correlated with the concept label. Adding such an experiment (even in the 2D toy setting) would clarify the method's actual limitations and prevent users from assuming the method is robust to all forms of confounding.

### Trivial
None.

## Nice-to-Haves

- Adding error bars or multiple-seed results to Table 1 would significantly strengthen the empirical case.
- A low-data regime experiment (varying the number of CAV training samples) would support the claim in Section 3.3 about filter-CAV instability.
- Showing the pattern-CAV's top neurons for real artifacts (band-aid, ruler, skin marker) analogous to Fig. 2 for timestamps would further strengthen qualitative evidence.

## Removed Points

- **"Weakness about unfair comparison":** Not applicable; no such criticism was raised.
- **"Reproducibility nitpicks (undisclosed hyperparameters, trivial implementation details):** Not applicable; no such criticism was raised.
- **"Missing related works":** Removed per instructions — cannot confirm existence of missing references.
- **"Formatting/style nitpicks" and "typos/grammar":** Removed per instructions — these are parser artifacts, not author errors.
- **Some generic strengths from Strength Finder** (e.g., "this paper addressed an important problem") — dropped. The retained strengths are substantive and supported by specific evidence.
- **The harsh critic's request for "multiple random seeds for ClArC"** — moved to Nice-to-Haves. While valuable, single-run evaluation is standard practice for large-scale model correction experiments, and the pattern of improvement across multiple models/layers/datasets (Fig. 7) provides sufficient evidence.

## Novel Insights

Beyond the paper's own contributions, the reviews surfaced an important nuance: the neuroimaging filter/pattern decomposition (which the paper imports) was designed for settings where signal and noise are statistically independent by construction. The paper's transposition to CAVs inherits this assumption implicitly, but real-world concept supervision often involves partially confounded signals. The key insight is that while pattern-CAVs are provably better than filter-CAVs in the uncorrelated setting and remain the *correct* signal estimate in theory, the practical gap between the two methods may narrow under confounding — and neither method is truly "distractor-free" when distractors correlate with the concept. This is a worthwhile caveat for practitioners and a natural direction for future work (which the paper already flags: "disentanglement of correlated concept directions" in the conclusion).

## Suggestions

1. **Soften the language** in the Abstract and Conclusion: replace "solely focussing on concept signals" with "more precisely estimating the concept signal direction" and add an explicit caveat about correlated distractors in the Limitations section.
2. **Add error bars or multiple-seed results** to Table 1, or at minimum acknowledge the lack of statistical significance as a limitation.
3. **Either provide supporting evidence or remove** the claim about filter-CAV instability in low-data scenarios (line 155).
4. **Add a brief discussion** of why ResNet18 achieves perfect ΔTCAV for all methods on FunnyBirds, even if speculative.
5. **Consider adding a correlated-distractor experiment** (even a simple 2D extension) to demonstrate the method's behavior under confounding and clarify its actual guarantees.

## Score and Decision

**Originality:** 7/10 — The filter/pattern decomposition is borrowed from neuroimaging, but the identification of directional divergence in CAVs and the application of this decomposition to the concept direction estimation problem is novel and useful.

**Importance of research question:** 8/10 — CAVs are widely used in XAI, and their accuracy directly impacts downstream applications; improving them has broad practical value.

**Claims well-supported:** 7/10 — Core alignment claims are well-supported. Downstream application claims are suggestive but lack error bars. The "solely" language overreaches.

**Soundness of experiments:** 7/10 — Controlled experiments are well-designed with ground truth. Some missing analyses (ResNet18, correlated distractors) and missing error bars for Table 1 weaken the empirical case slightly but do not undermine the overall conclusion.

**Clarity of writing:** 8/10 — Clear motivation, well-structured, with helpful visualizations.

**Value to research community:** 8/10 — The method is simple, ready-to-use, and improves a widely used tool. Practitioners can adopt it immediately.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>