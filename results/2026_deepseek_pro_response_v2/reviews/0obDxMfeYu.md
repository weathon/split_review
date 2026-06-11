Now I have all the calibration data I need. Let me synthesize the final review.

**Anchor comparisons for calibration:**
- SAL (Du et al. 2024a): avg 6.50 (Round 1) — most directly comparable paper; same problem setting, two-stage framework, theoretical guarantees. Medix is clearly stronger: better empirical results, novel median approach, relaxed assumptions.
- "Gradient norm as OOD proxy": avg 5.50 (Round 1) — rejected; gradient-based OOD but different setup and had novelty concerns. Medix is substantially stronger.
- "Out-Of-Domain Unlabeled Data Improves Generalization": avg 7.00 (Round 2) — DRO + unlabeled data, theoretical bounds on Gaussian mixtures. Had restrictive model and unclear contributions. Medix is comparable or stronger.
- DOS: Diverse Outlier Sampling: avg 7.33 (Round 2) — simple, effective OOD detection method; praised for clarity but lacking theory. Medix has stronger theory and novelty but weaker presentation precision. Roughly comparable.
- "Negative Label OOD with VLMs": avg 7.50 (Round 2) — different approach (VLMs), clean method with theory.
- "Deep Orthogonal Hypersphere Compression": avg 8.00 (Round 1) — different area.

**Narrowed bracket: 6.5–7.5.** Medix sits above SAL (6.50) with stronger theory and empirics, roughly at or slightly below DOS (7.33) given theoretical presentation gaps but compensating with stronger novelty and theoretical contribution. Final score: **7.0**.

---

## Summary
Medix introduces a two-stage OOD detection framework that separates outliers from unlabeled wild data using element-wise median (EWM) of per-sample gradients, then trains a binary OOD detector on the InD data plus filtered outliers. The paper provides theoretical bounds (Theorems 4.1, 4.2) decomposing misclassification rates into contamination, concentration, and separation effects, and demonstrates strong empirical results on CIFAR-10/100 across 20 baselines and five OOD test sets.

## Strengths
- **Strong and consistent empirical results (Tables 1, 2):** Medix achieves an average FPR95 of 0.80% on CIFAR-10 (vs. 3.40% for WOODS, the next-best wild-data method) and 5.42% on CIFAR-100 (vs. 6.74% for WOODS), with improvements across all five OOD test sets and tight error bars across five runs (±0.09 on CIFAR-10 average). The gains over KNN+ (best InD-only method) are 9.50 and 40.98 percentage points respectively.
- **Clean empirical motivation (Figure 1):** The paper incrementally adds SVHN OOD samples to CIFAR-10 wild data and demonstrates a monotonic increase in L2 distance between the InD mean gradient and the EWM of wild-data gradients. This directly motivates the optimization objective in Eq. 4 and is a genuinely novel empirical observation.
- **Synthetic validation of filtering (Figure 2):** On 2D Gaussian mixtures with known ground truth, Medix flags 87.5% of actual OOD samples while retaining only 12.5% InD contamination. This controlled experiment isolates the filtering stage and corroborates the theoretical claims in a visually verifiable setting.
- **Interpretable theoretical framework:** Theorems 4.1 and 4.2 decompose misclassification into contamination (bounded for π < 0.5), concentration (vanishing as O(1/√m)), and separation (exponential in distributional gap Δ) effects. This is one of few works providing formal theory for the unlabeled wild-data OOD setting, alongside Du et al. (2024a).
- **Practical relaxation of batch-level mixing:** Unlike WOODS and SAL, which require batch-level mixing with fixed InD/OOD ratios, Medix operates on the entire wild dataset at once (Algorithm 1), broadening applicability to large outsourced datasets where structured mixing is unavailable.
- **Comprehensive baseline coverage spanning 20 methods:** The evaluation includes classic scoring (MSP, ODIN, Mahalanobis, Energy), post-hoc methods (ReAct, DICE, ASH, KNN), contrastive approaches (CSI, KNN+), and wild-data methods (OE, Energy w/OE, WOODS), plus recent baselines CONJ and DRL.

## Weaknesses

### Fatal
None.

### Major
- **Theoretical statements are imprecisely presented in the main text.** Theorem 4.1 references `m_in` and `m_min` without defining them; Theorem 4.2 references `m_out` without definition. The "EWM filtering rule" that the theorems bound is never formalized mathematically — what threshold or decision procedure does it use? ERR_in and ERR_out are named but not formally defined. Additionally, Theorem 4.1 defines ε = σ√(2 log(2d m_min)) but this ε is never used in the bound. These gaps make contribution C2 (theoretical guarantees) difficult to fully evaluate from the main text alone. The full definitions and proofs are presumably in the stripped appendix, but the main-text presentation is incomplete as a standalone.

### Minor
- **The sub-Gaussian assumption on gradient coordinates is strong.** The core results (Theorems 4.1, 4.2) require each gradient coordinate to be sub-Gaussian. Remark 4.3 provides empirical evidence (histogram and Q-Q plot) and Theorem C.3 (appendix) relaxes this to bounded second moments with degraded rates, but the clean exponential/concentration guarantees require sub-Gaussianity, which may not hold for all architectures and datasets.
- **The separation condition in Theorem 4.2 is not empirically validated.** The bound requires ||μ_out - ∇̄_in||₂ ≥ Δ√d, but the paper provides no evidence that this holds for the CIFAR/OOD dataset pairs used. This makes the practical relevance of the OOD misclassification bound unclear.
- **Computational cost of Algorithm 1 is high.** Each iteration computes EWM after removing each sample (leave-one-out), yielding O(|S|² · d) per iteration where d is the parameter/gradient dimension. The paper defers computational analysis to Appendix A.6, but this is a practical concern. Using only penultimate-layer gradients helps, but the quadratic scaling with |S| remains.
- **Limited experimental scope.** Only CIFAR-10/100 are used as InD datasets; only Wide ResNet-40-2 architecture is tested. The wild mixing is fixed at π = 0.5 with no sensitivity analysis in the main text. No ImageNet-scale experiments are provided.

### Trivial
- Algorithm 1, line 2: the while condition uses "or" where "and" appears intended. With "t ≤ T or |δ_max| > ε", the loop continues if either condition holds, meaning convergence (|δ_max| ≤ ε) does not stop the loop while t ≤ T. The intended behavior (stop upon convergence within max iterations) requires "and."
- Algorithm 1, line 10: δ_max is computed as max over δ_i for i ∈ S, but δ_i values were computed in lines 5-7 using the pre-removal S. After line 9 modifies S, line 10's δ_max is computed over the updated S using stale δ_i values.

## Nice-to-Haves
- Sensitivity analysis across different contamination ratios π (beyond the fixed π = 0.5), which would directly validate the theoretical contamination bounds.
- Evaluation on larger-scale datasets (e.g., ImageNet) and additional architectures to demonstrate generality.
- Empirical validation that the separation condition (||μ_out - ∇̄_in||₂ ≥ Δ√d) holds for the real datasets used.
- Brief computational cost analysis in the main text (not only in the appendix).

## Removed Points
These points are flagged to be removed, treat them with caution.
None from the Harsh Critic — the Harsh Critic input was truncated and contained no substantive weaknesses to evaluate. The Strength Finder's points were all cross-checked and found to be valid, concrete, and grounded in the paper content, so none were removed.

## Novel Insights
The gradient-deviation experiment (Figure 1) provides a genuinely novel empirical observation: the L2 distance between the InD mean gradient and the element-wise median of wild-data gradients increases monotonically with OOD contamination. This is not an obvious consequence of known theory and directly motivates the optimization objective. The two-sided theoretical decomposition into contamination, concentration, and separation effects — while building on standard concentration tools — provides an interpretable framework for understanding when median-based filtering succeeds that was previously absent from the wild-data OOD literature.

## Suggestions
- Define all quantities (m_in, m_min, m_out, ERR_in, ERR_out) explicitly in the theorem statements; do not rely on the appendix for these definitions.
- Formalize the "EWM filtering rule" mathematically in the main text — specify the decision threshold and connect it to the optimization in Eq. 4.
- Either remove the unused ε from the Theorem 4.1 statement or explain its role in the bound.
- Fix the while condition in Algorithm 1 (change "or" to "and") and correct the δ_max computation (compute δ_i values after updating S, or use the indices selected in line 8).
- Include a brief computational cost discussion in the main text, not only in Appendix A.6.

---

**Calibration anchor summary:**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| jlEjB8MVGa (SAL, Du et al. 2024a) | 6.50 | R1 | Most directly comparable; same problem setting. Medix stronger empirically and methodologically. |
| bcWwhF8cTZ (Gradient norm OOD) | 5.50 | R1 | Gradient-based OOD, different setup, novelty concerns. Medix substantially stronger. |
| eN0RyRVbSm (Double Descent OOD) | 6.50 | R1 | Theoretical OOD work, different focus. Medix more applied and empirically stronger. |
| Bo6GpQ3B9a (Out-of-Domain Unlabeled) | 7.00 | R2 | Uses unlabeled data with DRO, restrictive Gaussian model, unclear contributions. Medix comparable or stronger. |
| iriEqxFB4y (DOS) | 7.33 | R2 | Simple, clean OOD method without theory. Medix has stronger theory/novelty but weaker presentation precision. |
| xUO1HXz4an (NegLabel) | 7.50 | R2 | OOD with VLMs, different approach. Medix is in a different sub-area. |

**Bracket:** 6.5–7.5 from Round 1. Round 2 narrowed to 7.0: Medix is clearly above SAL (6.50) with stronger theory and empirical results, roughly comparable to DOS (7.33) — stronger on theoretical contribution and novelty, slightly weaker on presentation polish — placing it at **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>