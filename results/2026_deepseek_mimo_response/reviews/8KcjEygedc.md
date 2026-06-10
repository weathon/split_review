Now I have enough calibration data. Let me write the final review.

**Round 1 bracket:** 5.5–8.0. The paper under review is clearly stronger than Firdoussi et al. (I9Dsq0cVo9, avg 5.50), which it extends with difficulty-based pruning, new theoretical results, and broader empirical validation including ImageNet and LLM reasoning connections.

**Round 2 narrowing:** Within the 6.0–7.5 range, comparing against:
- 93XT0lKOct (6.00, Data Pruning by Information Maximization) — more empirical/methodological, less theoretical novelty
- wFD16gwpze (7.33, Analyzing Neural Scaling Laws) — similarly rigorous theoretical framework for scaling laws, but narrower practical scope

The paper under review has stronger theoretical novelty and broader practical relevance than the 6.00 anchor, and comparable theoretical rigor with better practical connections than the 7.33 anchor. However, the unmeasured ρ in the LLM reasoning section (the most practically significant claim) is a real weakness. Final score: **7.0**.

---

## Summary
This paper develops a random matrix theory (RMT) framework for analyzing when data curation (pruning) improves generalization in high-dimensional binary classification. It derives exact closed-form scaling laws for test error under label-agnostic and label-aware curation rules, characterizes optimal pruning strategies as a function of generator quality (ρ), and connects the theory to recent empirical successes (LIMO, s1) in LLM reasoning and to model collapse prevention. Empirical validation is provided on synthetic data and ImageNet.

## Strengths
- **Exact closed-form scaling laws (Theorem 1, Eqns 9–11):** Derives precise analytical expressions for test error in the high-dimensional proportional limit, decomposing the effect of any pruning strategy into four interpretable scalar constants (p, γ, β, β̃ in Eqn 8). This provides exact predictions rather than order-wise bounds, going beyond prior empirical scaling-curve observations.
- **Sharp phase-transition characterization (Theorem 2):** Proves that the optimal pruning strategy flips depending on generator quality ρ: "keep hard" uniquely minimizes error when the generator is strong (ρ→1), while "keep easy" uniquely minimizes error when the generator is weak (ρ<1). This is a crisp structural result with direct practical implications.
- **Novel reconciliation of contradictory LLM reasoning findings (Section 4.2, Tables 1–2):** Provides a parsimonious explanation for why LIMO/s1 report "less is more" on average AIME while Sun et al. report "more is more" on hard AIME, mapping these to strong-generator and weak-generator regimes of Theorem 2.
- **Compelling empirical validation on ImageNet (Section 4.3, Figures 2–3):** Figure 2 demonstrates the predicted crossover between "keep easy" (small n, weak generator) and "keep hard" (large n, strong generator) on real ImageNet data. Figure 3 shows that strategic pruning stabilizes performance across multiple rounds of iterative pseudo-labeling while uncurated training degrades by ~20 percentage points.
- **Generality unifying prior special cases (Remark 1):** The label-aware curation rule (Eqn 6) subsumes Feng et al. (2025) and Firdoussi et al. (2024) as special cases, positioning this as a unifying contribution.
- **Clean geometric formalism (Eqn 7):** Quality constants ρ, ρ*, ρ_g are interpretable as cosines of angles between generator, oracle, and ground-truth vectors, making the theory's predictions transparent and the conditions for each regime easy to reason about.

## Weaknesses

### Fatal
None

### Major
- **ρ is never estimated in the LLM reasoning section (Section 4.2) —** The paper characterizes the base LLM as a "strong generator" for average AIME and a "weak generator" for hard AIME, but ρ is asserted based on qualitative reasoning (the base model gets 16.5% on average AIME and ~1% on hard AIME) rather than measured. Since the theoretical framework parameterizes generator quality precisely via E_test(w_g) = (1/π)arccos(ρ), the base model's accuracy on each difficulty slice could serve as a rough proxy. Without this, Section 4.2 functions as a plausibility argument rather than a quantitative test, and two of the four bullet-point contributions rest on this gap. This is the paper's most fixable high-leverage weakness.

- **Tables 1 and 2 aggregate results from different experimental setups —** Table 1 uses Pass@1 from LIMO/s1 papers while Table 2 uses Avg@8 from Sun et al., with different base models, curation pipelines, and evaluation metrics. The claim that the same framework explains both requires the assumption that only the difficulty slice differs, when many confounds exist across these reports. This further weakens the evidential support for the LLM reconciliation claim.

### Minor
- **Model collapse experiment presentation conflates two curation types —** Line 251 describes the stabilizing strategy as "applying the 'keep hard' strategy," but Figure 3 labels it "Training on hard valid examples" (i.e., label-aware curation from Theorem 3/Eqn 6, which also filters for correctness). The paper's own theory distinguishes sharply between label-agnostic and label-aware curation (Sections 3.1 vs 3.2). An ablation comparing "keep hard" (label-agnostic), "keep valid only" (label-aware, no difficulty filter), and "keep hard + valid" would clarify which component prevents collapse.

- **Abstract overclaims phase boundary precision —** The abstract promises "precise phase transition curves tied to data size and quality" but Theorem 2 characterizes results only in limiting regimes (ρ→1, ρ*→1) rather than deriving explicit phase boundary equations in the main text. The paper notes these exist in the appendix, but the main text does not preview them.

### Trivial
None

## Nice-to-Haves
- A brief note on computational cost of curation (oracle scoring every example) versus savings from training on less data.
- Preview of the analytical form of the phase boundary in the main text (e.g., "the crossover from 'less is more' to 'more is more' occurs at ρ = f(φ, p, ...)").

## Removed Points
These points are flagged to be removed, treat them with caution:
- Harsh critic's concern about missing discussion of computational cost of curation — scope creep; this is a theory paper, not a systems paper.
- Harsh critic's note about missing comparison to Dohmatob et al. (2024a) on model collapse in regression — the paper already references and positions against this work in the Related Work section.

## Novel Insights
The most novel observation from the reviews is the tension between the theory's precision and its empirical validation: the framework parameterizes generator quality via a precise geometric quantity (ρ = cos angle between w_g and w_*), but the LLM reasoning section — which anchors the paper's real-world significance — never measures ρ, instead asserting it from qualitative reasoning. Since E_test(w_g) = (1/π)arccos(ρ) directly links ρ to the base model's accuracy, even a rough estimate would transform this section from a narrative argument into a quantitative prediction. This is a high-leverage improvement that would substantially strengthen the paper's weakest link.

## Suggestions
- Estimate ρ for the LLM reasoning section: use the base model's accuracy on each difficulty slice as a proxy (ρ ≈ cos(π × error_rate)), transforming Section 4.2 from qualitative to quantitative.
- In Section 4.3, explicitly distinguish between the label-aware (correctness filtering) and difficulty-based components when discussing the model collapse experiment, and consider a brief ablation.
- Preview the phase boundary results in the main text with a sentence or equation summarizing the crossover condition.

## Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Weak Correlations / Linearization | 2NwHLAffZZ | 2.33 | 1 | Far below — lacks rigorous theory and empirical validation |
| Onset of memorization in diffusion | XeGSIr7z6u | 3.40 | 1 | Below — narrow setting, weaker theoretical contribution |
| Mesoscience model generalizability | lZRRfupxYn | 3.00 | 1 | Below — speculative, no rigorous theory |
| Simplicity Bias in Overparameterized ML | KNQJtoPZmz | 3.00 | 1 | Below — lacks concrete theoretical results |
| Severing Spurious Correlations with Data Pruning | Bk13Qfu8Ru | 7.00 | 1 | Comparable score but different focus (empirical pruning for fairness vs. RMT theory) |
| Distilling Knowledge in Data Pruning | 9ccZzuix2D | 5.33 | 1 | Below — more limited theoretical contribution |
| Effective pruning of web-scale datasets | CtOA9aN8fr | 5.25 | 1 | Below — purely empirical, no theory |
| Maximizing Potential of Synthetic Data (Firdoussi et al.) | I9Dsq0cVo9 | 5.50 | 1 | Clearly below — this paper extends that work substantially |
| Strong Model Collapse (Dohmatob et al.) | et5l9qPUhm | 8.00 | 1 | Above — more focused (collapse only), rejected despite perfect scores |
| Combatting Dimensional Collapse in LLM Data | f4gF6AIHRy | 8.00 | 1 | Above — more empirical, less theoretical novelty |
| Scaling Laws for Associative Memories | Tzh6xAJSll | 7.60 | 1 | Slightly above — similarly clean theoretical framework, more focused |
| Capturing Temporal Dependence of Training Data Influence | uHLgDEgiS5 | 8.00 | 1 | Above — different methodology (influence functions), accepted |
| Analyzing Neural Scaling Laws (Power-Law) | wFD16gwpze | 7.33 | 2 | Comparable — similarly rigorous theory, narrower practical scope |
| Bayesian Treatment of Empirical Kernel | O6znYvxC1U | 6.33 | 2 | Below — narrower scope, less practical relevance |
| Collective Variables of Neural Networks | S04xvGXjEs | 6.00 | 2 | Below — rejected despite mixed high scores, less complete contribution |
| No Free Lunch from Random Feature Ensembles | 7rzA6aEASo | 5.60 | 2 | Below — narrower scope |
| Data Pruning by Information Maximization | 93XT0lKOct | 6.00 | 2 | Below — more empirical method, less theoretical novelty |
| Exploring Learning Complexity for Dataset Pruning | FN7n7JRjsk | 6.67 | 2 | Below — practical method without deep theory |
| GIO: Gradient Information Optimization | 3NnfJnbJT2 | 7.00 | 2 | Comparable — empirical data selection method, less theoretical |
| Dynamic Data Pruning with Historical Sampling | ZQ9SF5eUHZ | 5.67 | 2 | Below — narrower contribution |

**Round 1 bracket:** 5.5–8.0
**Round 2 narrowed to:** 6.5–7.5
**Final score:** 7.0 — The paper is clearly stronger than the Firdoussi et al. anchor (5.50, same RMT framework, accepted) due to difficulty-based pruning, Theorem 2's sharp characterization, and broader empirical validation. It is comparable to or slightly below the "Analyzing Neural Scaling Laws" anchor (7.33), which has similarly rigorous theory but less practical relevance. The main drag is the unmeasured ρ in the LLM reasoning section, which prevents the strongest practical claim from being fully quantitative. Despite this, the theoretical contribution is substantial, the synthetic and ImageNet validations are compelling, and the unification of contradictory LLM findings is a genuine insight.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>