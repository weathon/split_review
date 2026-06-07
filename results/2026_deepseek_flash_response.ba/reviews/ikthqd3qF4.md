I now have sufficient calibration anchors. Let me write the final review.

## Summary

This paper proposes a method for evaluating unsupervised record linkage without labeled data by exploiting a structural constraint: an individual can originate at most one first-lien mortgage. The authors derive observable lower bounds on precision (Theorem 1) and relative recall (Corollaries 1–2) that depend only on the fraction of clusters with multiple originations and the unconditional origination probability — both estimable from unlabeled data. They instantiate the method with hierarchical clustering on 65.5M HMDA mortgage applications, reporting 92.3% precision at the preferred specification.

## Strengths

- **Theorem 1 is a genuinely novel theoretical contribution.** The bound $\Pr[\text{False}] \leq \Pr[\text{Mult}] / p^2$ turns an unobservable quantity (false positive rate) into a function of two directly estimable observables. This is clean, elegant, and not something I have seen before in the record linkage literature. The proof is conceptually straightforward once explained, but the insight is non-trivial.

- **Corollaries 1–2 extend the same logic to relative recall and weighted metrics.** Bounding recall in unsupervised settings is typically harder than bounding precision, so the derivation of a rank-equivalent observable quantity $\hat{\alpha}(\theta)N^+(\theta)$ for relative recall is practically useful and theoretically notable.

- **The framework is genuinely method-agnostic.** The bounds depend only on predicted labels, not on the clustering algorithm that produced them (Section 1, line 15). This is a real departure from prior work that tied evaluation bounds to specific linkage procedures, and it opens the door to principled model comparison — even if the paper itself does not fully walk through that door.

- **The simulation demonstrates that the bound is practically tight.** At $\varepsilon=0.06$, the bound reaches 93.7% against a true precision above 95% (Section 3, Figures 3–4). This shows the bound is not just theoretically valid but tight enough for tuning.

- **Real-world application at genuine scale.** The method is applied to 65.5 million mortgage applications — a real, consequential dataset where ground-truth labels genuinely do not exist. The computational implementation using the nearest-neighbor-chain complete-linkage algorithm (Müllner, 2011) with $O(\ell^2)$ worst-case complexity is appropriate for this scale.

## Weaknesses

### Major

1. **No comparison to alternative linkage methods, despite claiming cross-model comparison.** The paper evaluates 96 combinations of distance functions and $\varepsilon$ — all variants of the *same* agglomerative clustering approach. The paper explicitly claims the method enables "cross-model comparisons" and "hyper-parameter tuning and model comparison without ground-truth labels" (Section 1, line 15; Conclusion). Yet the empirical section never demonstrates this: there is no comparison to exact matching, rule-based linkers, DBSCAN, canonical Fellegi–Sunter-style record linkage, or any other fundamentally different approach. The 92.3% precision figure is an isolated number — we cannot tell whether a trivial rule (e.g., link applications sharing identical census tract, income rounded to nearest $1000, and date within 1 day) would achieve similar or better precision. This is a significant gap because the paper's value proposition is that the bound enables principled model comparison, but it only tunes one model.

2. **Restriction to size-2 clusters substantially limits practical applicability.** The paper drops all clusters with more than two applications (footnote 4: "To keep the discussion as simple as possible"). The simulation generates applicants with expected 1.25 applications, meaning a non-trivial fraction have $\ge 3$ applications — precisely the most prolific cross-applicants (potentially the most informative for downstream fairness or shopping-behavior analyses in Section 5). The bound itself does not require size-2 clusters (it generalizes), so the paper's restriction of the entire empirical evaluation to pairs is an unmotivated limitation. The paper should at minimum quantify what fraction of cross-applicants are lost by this restriction.

3. **Simulation validates only under ideal conditions where assumptions hold by construction.** The data-generating process satisfies Assumptions 1–2 by design, so the close match between Figures 3a and 4a is a consistency check, not a robustness test. The paper would be substantially stronger with a misspecified simulation (e.g., correlated origination outcomes across $\varepsilon$-identical applicants, or violations of the monotonicity assumption) to show whether the bound degrades gracefully or fails entirely.

4. **No uncertainty quantification.** The precision lower bound is reported as a point estimate (92.3%, Section 4), but both $\hat{p}$ and $\hat{p}_m$ are estimated from finite samples of 65.5M applications. Bootstrap confidence intervals or some quantification of sampling variability are needed to assess the precision of the bound itself.

### Minor

1. **No absolute recall estimate in the real application.** In simulation, recall is reported at 92% (Section 3). In the HMDA application, recall is described only as "minimal loss in relative recall" — no number is given. The recall bound from Corollary 1 is proportional to $\hat{\alpha}(\theta)N^+(\theta)$, but converting this to absolute recall requires $P_{tot}$, which is unknown. This asymmetry (precisely estimated precision but unquantified recall in practice) limits what the method tells practitioners.

2. **Selection bias inherent in the method is not discussed.** Detected cross-applicants are those who submit $\varepsilon$-identical applications. Applicants who vary their reported characteristics across lenders (different loan amounts, different reported income) are systematically excluded. The paper acknowledges this only in a footnote (footnote 5) for the partitioning variables but never discusses its implications for the downstream fairness and shopping-behavior analyses proposed in Section 5.

3. **Sensitivity of the preferred specification to the choice of $\lambda$ is not explored.** The "knee" of the frontier is chosen via the weighted score $W(\theta)$, but $\lambda$ (or equivalently, the location of the knee) is a subjective choice. A slightly different weighting could shift the preferred specification and the reported precision.

### Trivial

None.

## Nice-to-Haves

- Bootstrap confidence intervals for the bound estimates.
- A misspecified simulation scenario where Assumptions 1–2 are partially violated.
- Quantification of the fraction of cross-applicants discarded by the size-2 restriction.
- Brief discussion of computational runtime / wall-clock time for the 65.5M records.

## Removed Points

These were flagged by the reviewers but are excluded from the main evaluation:

- **"Bound becomes uninformative when algorithm is poor" / circularity claim**: The critic argues the bound is most useful when the algorithm is already good, creating circularity. This conflates a diagnostic with a training signal. A bound that says "this algorithm is bad" (by returning precision ≈ 0) is still informative — it tells the practitioner not to use that configuration. This is a property of any honest bound, not a flaw.

- **"Could go the other way" (negative correlation in false-positive clusters)**: The critic speculates that $\Pr[\text{Mult}|\text{False}]$ could be $< p^2$ if the clustering algorithm selects pairs with complementary origination probabilities. The paper uses complete-linkage clustering, which produces homogeneous clusters; positive correlation is the natural direction, and under that direction the bound is *conservative*. This speculation is unsupported and not a genuine weakness.

- **Structural constraint examples not perfect analogs (insurance, job offers)**: The paper's core analysis is on mortgages; the other examples are illustrative. Criticizing their imperfect mapping is scope creep.

- **Partitioning variables exclude some cross-applicants**: Acknowledged as a modeling choice in footnote 5. Every linkage method makes such choices.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add 2–3 fundamentally different linkage methods** (exact matching, a simple rule-based linker, DBSCAN) and show that the bound correctly ranks them, validated in simulation where ground truth is known. This would transform the paper from "a clever bound applied to one algorithm" to "a general evaluation framework."

2. **Include a misspecified simulation** where origination outcomes are correlated within $\varepsilon$-similar applicants, testing whether the bound remains conservative or fails.

3. **Quantify and discuss the implications of the size-2 restriction**: what fraction of cross-applicants are missed, and what biases does this introduce for the downstream applications (fairness, shopping behavior) proposed in Section 5?

4. **Add bootstrap standard errors** to the precision lower bound estimate.

---

### Calibration Report

**Round 1 — Bracketing:**
- Low band (score < 3.5): Papers about unsupervised evaluation with weak empirical support (avg 2.0–3.4). Our paper is clearly stronger — it has a real theoretical contribution and large-scale application.
- Middle band (3.5–7.5): Most relevant papers here included the Fréchet bounds paper (avg 5.50, Reject) and SSME (avg 6.00, Reject), both about evaluating models without labels.
- High band (>7.5): Strong papers with comprehensive theory + experiments (avg 7.6–8.0). Our paper does not meet this standard empirically.

**Round 2 — Narrowing:**
- Fréchet bounds paper (avg 5.50): Closest in contribution type (bounds for evaluation without labels). Our paper has a cleaner, more elegant theoretical contribution (Theorem 1) and a more compelling real-world application at genuine scale (65.5M records vs. standard ML benchmark datasets). However, our paper shares similar gaps: strong assumptions, and our paper is actually *worse* on baseline comparisons (the Fréchet bounds paper at least compared across label models). Overall, slightly stronger than this anchor.
- SSME (avg 6.00): More thorough empirical evaluation across 4 domains with baselines, but less novel theoretically (mixture model + EM). Our paper and this one are roughly comparable — each has different strengths.
- OOD detection paper (avg 6.33, Accept): Strong theory (label blindness theorem) + new benchmark + experiments with baselines. Accepted. Our paper has comparable theoretical novelty but weaker empirical validation.
- M3C (avg 7.00, Accept): Strong theory + experiments with baseline comparisons in graph matching. Our paper's empirical component is significantly weaker.

**Final placement:** The paper sits above the Fréchet bounds paper (5.50) but below the OOD detection paper (6.33). The core theoretical insight is genuinely novel and well-executed, but the empirical evaluation has significant gaps—most critically, no baseline comparisons despite claiming cross-model comparison as a key benefit. At a top venue, the empirical component needs substantial strengthening.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>