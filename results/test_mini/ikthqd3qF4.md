Now I have sufficient calibration context to produce the final review. Let me compile it.

**Bracket determination:** Round 1 bracketing placed the paper between weak anchors (~3.0) and middle anchors (~5.0-6.5). The strong anchors (8.0) are clearly too high — this paper has meaningful but non-fatal empirical gaps. The narrowest plausible range from round 1 is **4.5 to 6.5**.

**Round 2 narrowing:** I compared against specific anchors at 5.00 (Labelling Data with Unknown References), 5.33 (Theoretical Limitations of Embedding-Based Retrieval, accepted poster), 5.50 (USimUL), and 6.50 (PU Learning Benchmark, accepted poster). The current paper's theoretical contribution is stronger than the 5.00-5.50 anchors but its empirical gaps are wider than those of the 6.50 accepted paper. This places it in the **5.0–5.5** range.

**Final score: 5.5** — The paper sits between the 5.33 accepted poster (theory-heavy, some experimental concerns) and the 5.00/5.50 rejected papers, leaning toward a weak accept/weak reject borderline. The theoretical novelty is genuine, but the incomplete reporting of the real-data application (missing origination rate, size-2 restriction) prevents the empirical demonstration from being fully interpretable.

---

## Summary

This paper introduces a clever theoretical framework for deriving observable lower bounds on precision and recall in unsupervised record linkage, exploiting a structural constraint (e.g., each individual can originate at most one first-lien mortgage). Theorem 1 provides a bound precision ≥ 1 − Pr[Mult]/p² that depends only on observable quantities. The bound is validated in simulation, where it closely tracks the true precision. The method is then applied to 65.5M HMDA mortgage applications, reporting an estimated precision of 92.3% at the preferred specification. Corollaries extend the framework to relative recall and Fβ scores, enabling principled hyperparameter tuning without any labeled data.

## Strengths

1. **Genuinely novel theoretical bound using a structural constraint.** Theorem 1 derives an observable lower bound on precision that does not require any ground-truth labels. The insight — that a one-origination-per-individual constraint makes multiple-origination clusters informative about false positive rates — is both clever and broadly applicable beyond mortgage data (secured loans, insurance, college admissions, job offers). The bound depends only on the fraction of clusters with multiple originations (Pr[Mult]) and the overall origination rate (p), both estimable from the data.

2. **Simulation validates that the bound tracks true precision.** Section 3.1 shows a close match between the bound (Figure 4a) and the true precision (Figure 3a) across a range of ε values. The bound correctly ranks specifications (e.g., "with date" outperforming "without date") and identifies the same knee-point (ε = 0.06) as the true precision curve. This provides tangible evidence that the bound is useful in a controlled setting where ground truth is known.

3. **Extended bounds for recall and Fβ (Corollaries 1–2).** The framework extends beyond precision to relative recall and weighted summaries, enabling model selection without labels. This is a meaningful practical contribution — it turns the bound from a one-number diagnostic into a tool for tuning.

4. **Large-scale real-data demonstration on 65.5M applications.** The HMDA application demonstrates that the clustering algorithm scales to millions of records and that the bound can be computed at that scale. The precision-sample-size frontier (Figure 5) across 96 parameter combinations provides a clear, actionable trade-off visualization.

## Weaknesses

### Major

1. **Origination rate p̂ for the real HMDA data is not reported, making the headline 92.3% precision claim uninterpretable.** The bound's informativeness depends critically on p: precision ≥ 1 − Pr[Mult]/p². The simulation reports p̂ = 0.7917 (p² ≈ 0.63), but Section 4 does not report p̂ for the real data. If the real origination rate is 0.5, then p² = 0.25 and the bound could be substantially looser than the 92.3% reported. Without this number, a reader cannot evaluate whether the bound is meaningful or close to trivial. The final sentence of Section 4 says "We perform additional diagnostics to validate that the clusters truly correspond to cross-applicants in the Appendix" — but the appendix is not available for inspection. This is the single most important missing piece; it should be reported and discussed.

2. **Restriction to clusters of size exactly 2 is under-justified.** Footnote 4 states: "To keep the discussion as simple as possible, we drop all clusters with more than two applications in both our simulation results and our application that follows." This eliminates a potentially systematic subset of cross-applicants (those submitting 3+ applications). The paper neither reports how many larger clusters exist in the real data nor argues that the restriction does not bias the precision estimate. Since the theoretical derivation does not require size-2 clusters (the bound is general), this appears to be an implementation convenience that limits practical applicability.

### Minor

3. **Assumptions 1 and 2 are stated but not empirically examined.** Assumption 1 (independence of origination decisions across borrowers) and Assumption 2 (weakly increasing origination probability) are central to Lemma 1's bound on Pr[Mult|False]. The paper acknowledges these are "not very strong" but provides no sensitivity analysis. A simple diagnostic — e.g., testing for residual correlation in origination outcomes within partitions — would strengthen confidence.

4. **No comparison with alternative record linkage approaches.** The bounds are described as method-agnostic, but the paper does not demonstrate tuning of any alternative method (e.g., exact matching on categorical variables, probabilistic linkage, or a different clustering algorithm) using the same bounds. Showing that the bounds enable model selection across different model classes would significantly strengthen the contribution.

5. **The bound's dependence on p is not discussed as a limitation.** The paper should explicitly note that the bound becomes weak when p is small (p² → 0), and provide practical guidance on what range of p is required for the bound to be useful.

### Trivial

- The abstract and introduction describe "92.3% precision" without consistently qualifying it as a lower bound. The distinction between "estimated precision" and "lower bound on precision" could be sharper.

## Nice-to-Haves

- A small-scale manual validation of the bound on the real HMDA data (e.g., hand-inspecting 100–200 clusters) would provide ground-truth corroboration that the simulation alone cannot.
- Reporting how many clusters of size >2 exist in the real data and discussing whether dropping them biases the estimate.
- A simulation where origination probability p is varied to show the bound's behavior when p is low.

## Removed Points

- **"Lemma 1 proof is in appendix; can't inspect"** — The parser strips appendices from all papers. This is a known limitation, not an author error.
- **"Confusion about strict inequality vs. equality in Theorem 1"** — The paper's logic is clear: Lemma 1 (appendix) shows Pr[Mult|False] > p² for the general case, and the size-2 restriction makes exact equality a reasonable special case. No contradiction.
- **"Formatting/style nitpicks"** — These are parser artifacts, not author errors.
- **"Missing related works"** — Cannot verify without external sources.
- **"No external validation in real data"** — The paper claims there are "additional diagnostics" in the appendix (which is stripped). While unverifiable, the claim exists, and this point is subsumed by Weakness #1 (missing p̂).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report p̂ for the HMDA application immediately before or alongside the precision bound.** This single change would resolve the most significant concern with the empirical demonstration.
2. **Acknowledge and discuss the size-2 restriction transparently** — report the number and fraction of clusters of size >2 in the real data and explain why (or whether) they are excluded.
3. **Add a sensitivity analysis for Assumptions 1 and 2** — a simple simulation varying the degree of dependence in origination outcomes or lowering the per-application origination probability for cross-applicants would substantially increase confidence in the bound's robustness.
4. **Consistently use "lower bound on precision" rather than "estimated precision"** when referring to the 92.3% figure.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>