Now I have a solid calibration. Let me write the final consolidated review.

**Round 1 bracket:** The paper sits between the weak anchors (~3) and strong anchors (~8), most plausibly in the 4.5–6.5 range.
**Round 2 narrowing:** Compared to similar-area papers at 5.25, 5.75, 6.00, and 6.25, this paper's theoretical novelty is above the 5.25 and 5.75 papers, but its empirical limitations hold it below the 6.25 paper. I place it at 5.5.

---

## Summary

This paper introduces *random set stability*, a novel extension of hypothesis set stability (Foster et al., 2019) that explicitly accounts for algorithmic randomness (e.g., SGD minibatch noise). Using this framework, the authors obtain expected worst-case generalization bounds that replace the intractable mutual information terms appearing in prior topological/fractal bounds (Simsekli et al., Birdal et al., Andreeva et al.) with a stability parameter \( \beta_n \). The key technical lemma (Lemma 3.4) bounds the expected worst-case generalization error by a Rademacher complexity term plus a stability-dependent term, and Theorem 4.4 provides the first mutual-information-free topological bounds. The framework elegantly recovers classical singleton stability bounds (\(J=1\)) and fixed-hypothesis-set bounds (\(J=n\)) as special cases.

## Strengths

- **Novel definition of random set stability (Assumption 3.1).** This is a principled extension of Foster et al.'s hypothesis set stability that accounts for algorithmic randomness \(U\), which prior worst-case bounds (e.g., Simsekli et al., Dupuis et al., Andreeva et al.) handled only through intractable mutual information terms. Lemma 3.2 shows that classical uniform argument stability (Definition 2.1) implies random set stability, establishing a clear path to verifying the assumption.

- **Lemma 3.4 (expected worst-case generalization bound).** Provides a clean bound \( \mathbb{E}[\sup_{w\in\mathcal{W}_{S,U}}(\mathcal{R}(w)-\hat{\mathcal{R}}_S(w))] \leq 2\mathbb{E}[\text{Rad}_{\tilde{S}_J}(\mathcal{W}_{S,U})] + 2J\beta_n \) that replaces the mutual information terms of prior work with the stability parameter. The decomposition into a Rademacher complexity term (capturing topological/geometric structure of the random set) and a stability term (capturing algorithmic sensitivity) is conceptually clean.

- **Theorem 4.4 (IT-free topological bounds).** Delivers generalization bounds using \(\alpha\)-weighted lifetime sums and positive magnitude *without* mutual information terms, directly fulfilling the paper's stated contribution of providing the first fully computable topological bounds. The result is nontrivial: it requires combining the random set stability assumption with Massart's lemma and a careful chaining argument.

- **Recovery of classical bounds (Corollaries 3.5 and 3.6).** Setting \(J=1\) recovers classical algorithmic stability bounds; setting \(J=n\) recovers standard Rademacher complexity bounds for fixed hypothesis sets. This demonstrates that the framework generalizes prior theory without contradiction and that \(J\) naturally interpolates between these two regimes.

- **Empirical estimation that goes beyond prior work.** The paper is the first to attempt full estimation of a worst-case topological bound, including \(\beta_n\), the topological complexity, and the optimization over \(J\). The bounds are within roughly one order of magnitude of the actual generalization gap in most settings, and the bound adapts meaningfully to hyperparameter changes.

## Weaknesses

### Major

- **Optimistic \(\beta_n\) estimation limits the "fully computable" claim.** The paper honestly acknowledges (Section 5) that the estimation of \(\beta_n\) uses a finite sample of \(M=500\) held-out points rather than a supremum over all \(z\in\mathcal{Z}\), producing an "optimistic estimation" that is a lower bound on the true \(\beta_n\). The degree of optimism is uncontrolled — the true stability parameter could be substantially larger, and since the empirical bounds already sit near (or above) the trivial value of 1 for some configurations (e.g., 104.43% for ViT), a larger \(\beta_n\) would push them well above 1. The claim of "fully computable" bounds is therefore partially true: the framework removes the *structural* intractability of mutual information, but replaces it with a quantity that can only be lower-bounded empirically with uncontrolled error. This is common in stability-based theory (even classical singleton stability bounds require estimation), but the paper overstates the significance of "fully computable" relative to this caveat.

- **Correlation experiments do not convincingly support Theorem 4.4.** The paper claims (Section 5.1, line 301) that "the sensitivity of \(\mathbf{E}^1(\mathcal{W}_{S,U})\) with respect to the generalization gap ... increases when \(n\) gets larger" and that this "strongly support[s] Theorem 4.4." However, the paper only reports Pearson correlation coefficients, not slopes, so the claimed increase in sensitivity is visually asserted rather than quantitatively demonstrated. Moreover, for GraphSage (Figure 3), the Pearson correlation drops from 0.92 (\(n=100\)) to 0.28 (\(n=10,000\)) — the *opposite* of the strengthening coupling the theory would predict. The speculative explanation ("reaching local minima is harder when \(n\) increases") is not supported by any evidence. This inconsistency weakens the empirical validation of the core theoretical result.

### Minor

- **Bound is vacuous for one configuration.** For ViT with \(\eta=10^{-4}\), \(b=64\), the estimated bound is 104.43% — strictly above the maximum possible value for 0-1 loss. The paper's phrasing ("in most experimental settings, the estimated bounds remain below 100% accuracy") is technically accurate but understates the problem: a framework whose bound can exceed the trivial worst case for plausible hyperparameter choices needs a clearer discussion of when it is non-vacuous.

- **Simplified Rademacher bound in experiments deviates from Theorem 4.4.** The empirical evaluation replaces the local Lipschitz constant \(L_{S,U}\) from Theorem 4.4 with Massart's lemma bound \(2\sqrt{2\log T/J} + 2J\beta_n\), discarding the Lipschitz dependence. While this is a practical simplification, it means the empirical bounds do not directly implement the theoretical bound of Theorem 4.4. The paper should discuss how this simplification affects tightness.

- **Limited experimental scope.** Only two models (ViT, GraphSage) and two datasets (CIFAR-100, MNISTSuperpixels) are tested. Adding simpler architectures (e.g., MLPs, CNNs on standard benchmarks) would strengthen the claim of broad applicability. The paper also does not compare against any baseline bound (e.g., a data-independent uniform convergence bound or a singleton stability bound for the last iterate) to contextualize the achieved tightness.

- **No confidence intervals for the bound itself.** The bound estimates in Table 1 are reported as point values without uncertainty quantification, despite the \(\beta_n\) estimates having non-negligible standard deviations and the topological complexity estimation involving subsampling.

### Trivial

- Table 1 reports the bound as \(10^2 \cdot \text{Bound}\) but should clarify the units more explicitly in the caption.

## Nice-to-Haves

- A theoretical upper bound on \(\beta_n\) for specific optimizers (e.g., SGD, Adam) under standard assumptions would restore the "fully computable" claim without qualification.
- Ablation varying the number of replacement samples in \(\beta_n\) estimation to characterize the optimistic bias empirically.
- Reporting the actual regression slopes from Figures 2 and 3 and testing whether they scale approximately as \(n^{1/3}\) under the assumption \(\beta_n \propto 1/n\).

## Removed Points

- *Criticism that the bound is "often near or above the trivial value of 1" and that the paper's claim is false*: The paper says "in most experimental settings, the estimated bounds remain below 100%" — this is accurate (6 of 8 settings are below 100%). The single case above 100% is a real limitation but the critic's claim that the paper's statement is "not true" is incorrect. The substance is kept as a Minor weakness above.
- *Criticism about the \(n^{-1/3}\) rate being slow with no comparison*: The paper acknowledges this trade-off explicitly (line 235) and mentions Neu et al. (2021) in the limitations section. The rate criticism is valid but overstated.
- *Request for theoretical proof of \(\beta_n\) for common optimizers*: Placed in Nice-to-Haves since it is a significant extension, not a flaw in the presented work.
- *Criticism about missing related works*: Not permissible to include; no external sources to verify.
- *Criticism about computational cost of \(\beta_n\) estimation*: Valid but moved to a brief mention; the paper focuses on feasibility, not computational efficiency.
- *Strength Finder's generic strengths about "addressing an important problem"*: Removed as superficial.
- *Formatting/style nitpicks*: Removed.

## Novel Insights

The most interesting observation emerging across the reviews is that the paper's framework exposes a fundamental tension between "fully computable" and "tight in practice." By replacing mutual information (which is structurally intractable but can be bounded theoretically) with a stability parameter \(\beta_n\) (which is conceptually simple but can only be lower-bounded empirically with uncontrolled error), the paper trades one form of intractability for another. The reviews collectively surface that this trade-off is not adequately discussed — and the empirical evidence suggests the cost may be high (the bound is sometimes vacuous, and the \(O(n^{-1/3})\) rate is slow). This suggests a broader question: whether stability-based approaches to removing information-theoretic terms in topological bounds can ever produce tight bounds for the practical regimes where these topological quantities are most informative.

## Suggestions

1. **Qualify the "fully computable" claim.** Explicitly state that the bound requires estimating \(\beta_n\) via a finite-sample approximation, and discuss the implications of this optimism for the bound's validity.
2. **Report slopes not just correlations** in the interplay experiments (Figures 2–3), and test whether they scale as the theory predicts. Provide error bars.
3. **Add a discussion of when the bound is provably non-vacuous.** For a simple setting (e.g., strongly convex loss, finite trajectories), analytically compute the bound's order and compare to the true worst-case error.
4. **Include a baseline comparison.** Add a data-independent Rademacher complexity bound and a singleton stability bound for the last iterate to Table 1.
5. **Expand model scope** to include at least one simple architecture (MLP or small CNN) on a standard dataset (e.g., MNIST, CIFAR-10) to demonstrate broad applicability.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| FAY6ORIvn5 (TDA generalization bounds) | 5.25 | R1 | Similar area (TDA + generalization) but narrower scope. This paper's theoretical contribution (random set stability) is more novel. |
| kuchZdMRMa (TDA descriptors expressivity) | 4.60 | R1 | More of a survey/analysis paper; this paper has stronger novelty. |
| FjZcwQJX8D (Scalable topological regularizers) | 7.00 | R1 | Stronger empirical validation with clear practical impact. This paper falls short of this. |
| RFMdtKbff5 (Algorithm tight bounds) | 5.00 | R2 | Weaker theoretical contribution; this paper is stronger. |
| lirR6Wfkd6 (QNN generalization bounds) | 6.00 | R2 | Rejected despite 6.0 — similar pattern of novel theory with limited experiments. Comparable. |
| 2GwMazl9ND (Stability for adversarial training) | 6.25 | R2 | Accepted — cleaner experiments, clearer practical implications. This paper is weaker empirically. |
| DZxU0q2S11 (Data geometry bounds on widths) | 5.75 | R2 | Strong theoretical results with applicability gap. Similar profile to this paper. |

**Initial bracket (Round 1):** 4.5–6.5  
**Narrowing (Round 2):** Comparison to anchors at 5.25, 5.75, 6.00, and 6.25 places the paper between the 5.75–6.00 cluster. The theoretical novelty is stronger than the 5.25 and 5.75 papers, but the empirics are notably weaker than the 6.25 paper.  
**Final score:** 5.5 — a borderline paper with a genuinely novel theoretical framework held back by significant empirical limitations and an overclaimed "fully computable" narrative.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>