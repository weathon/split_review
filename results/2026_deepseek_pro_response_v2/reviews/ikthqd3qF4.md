Now I have a clear picture. Let me finalize the review.

**Calibration summary across all rounds:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Fréchet bounds for PWS | 5.50 | R1 | Closest topic; our paper has cleaner theory, better simulation validation → stronger |
| αMax-B-CUBED | 4.75 | R1 | Incremental metric; our paper clearly stronger |
| Deep clustering validation | 5.00 | R1 | Less novel; our paper stronger |
| SSME | 6.00 | R2 | Also evaluates without labels; our paper needs no labeled data at all, has cleaner theory → somewhat stronger |
| Can We Ignore Labels (OOD) | 6.33 | R2 | Novel theory + experiments; comparable quality; our paper has more practical application → comparable |
| Re-Evaluating SSL | 6.00 | R2 | Different topic; accepted at 6.0 |
| FairDen | 6.75 | R2 | Solid accepted paper; slightly more polished → our paper slightly weaker |
| DP Hierarchical Clustering | 6.67 | R2 | Different topic; accepted |
| M3C | 7.00 | R1 | Strong theory + extensive experiments → our paper weaker |
| Deep Temporal Graph Clustering | 7.33 | R2 | Strong accepted paper → our paper clearly weaker |

**Round 1 bracket:** 5.5–7.5
**Round 2 narrowing:** Our paper sits between SSME (6.00) and FairDen (6.75), comparable to Can We Ignore Labels (6.33). The paper's genuinely novel theoretical contribution and strong simulation validation push it above the borderline 6.0 papers, while the notation error and lack of HMDA validation keep it below the 7.0+ tier. **Final score: 6.5, Accept.**

---

## Summary
This paper derives observable lower bounds on precision and relative recall for unsupervised record linkage by exploiting a structural constraint — that an individual can have at most one positive outcome (e.g., originate at most one first-lien mortgage). The key insight is that clusters containing multiple originations are provably false positives, making the multi-origination rate informative about algorithm quality. The authors apply agglomerative clustering to 65.5M HMDA mortgage applications, using their bounds for hyperparameter selection without labeled data, and report 92.3% estimated precision on 314,344 identified cross-applicant clusters.

## Strengths
- **Novel theoretical contribution.** Theorem 1 provides a clean, observable upper bound on the false positive rate (Pr[False] ≤ Pr[Mult]/p²) using only the empirical origination rate and the fraction of clusters with multiple originations. The derivation via Remark 1 — exploiting the structural constraint that Pr[Mult | ¬False] = 0 — is elegant and requires only mild assumptions (independence of origination decisions across borrowers, and weakly increasing origination probability in number of applications). This is genuinely the first work to derive such bounds for unsupervised record linkage.

- **Method-agnostic and domain-agnostic framework.** The bounds depend only on predicted labels (lines 15-16), applying to any algorithm and any domain sharing the structural constraint. The paper provides concrete examples beyond mortgages: insurance policies, college admissions, and job offers (lines 13-14). The corollaries extend the framework to recall and Fβ-score, enabling full model comparison without ground-truth labels.

- **Strong simulation validation.** Section 3 provides ground-truth evaluation showing the bound closely tracks true performance: at ε=0.06 ("with date" specification), true precision is ~95% (Figure 3a) while the implied lower bound is ~93.7% (line 214), a gap of only ~1.3 percentage points. The simulation correctly recovers the relative ranking of specifications and demonstrates the bound is practically informative, not just theoretically valid.

- **Large-scale real-world application.** The method processes 65.5 million mortgage applications across 96 hyperparameter combinations (Section 4), identifying 314,344 cross-applicant clusters. The precision-sample-size frontier (Figure 5) provides a principled model selection approach, and the agglomerative clustering with complete linkage and nearest-neighbor chain algorithm (O(ℓ²) complexity, line 57) makes the computation feasible at scale.

- **Practical post-hoc filtering.** Dropping clusters with multiple originations (which are provably false positives under the structural constraint) yields an improved precision bound — a direct and practical refinement at negligible computational cost.

## Weaknesses

### Fatal
None.

### Major
- **Notation error in equations (1) and (2) contradicts the text and propagated usage.** The text on line 141 says equations (1)/(2) yield "a new lower bound on the precision of our algorithm," but the LHS of both equations is written as "Pr[False]" — the false positive rate. A lower bound on the false positive rate is an *upper* bound on precision (since Precision = 1 − Pr[False]), the opposite of what the text claims. The subsequent corollaries (lines 148-166) correctly treat α̂(θ) as a lower bound on *precision*, which is internally consistent with the claimed result but inconsistent with how α̂(θ) is defined in equation (2). This is not just a typo — it makes the central quantitative derivation impossible to verify from the main text as written. The authors must resolve whether the LHS of (1)/(2) should be "Precision" or some equivalent, and ensure all inequality directions are consistent with the corollaries. The simulation results (which use equation (2) to compute the implied precision bound) suggest the underlying derivation is correct and the error is in presentation, but this needs to be fixed.

- **HMDA precision claim lacks empirical validation beyond theoretical bounds.** The paper reports 92.3% precision as the preferred specification (line 240), but this is entirely a theoretical lower bound — there is no ground truth, no labeled subset, and no external validation for the HMDA application. The simulation (Section 3) provides evidence that the bound is tight when assumptions hold, but the real-world application operates under unknown assumption violations. The abstract and conclusion present this as an empirical finding (e.g., "successfully identified cross-applicants with 92.3% precision"), which overstates what has been demonstrated. The paper mentions additional validation diagnostics deferred to the Appendix (line 240), which are not available in the main text. At minimum, the authors should acknowledge that the 92.3% figure is a theoretical bound, not a verified measurement, and discuss what could cause the bound to be loose or anti-conservative in practice.

### Minor
- **Limited engagement with related literatures.** The paper claims to be "the first work to derive observable lower bounds on both precision and relative recall in unsupervised classification settings" (line 15) but does not discuss prior work from record linkage, entity resolution, internal cluster validation, or weak supervision — fields that have all grappled with evaluation without labels. The reference list (8 items) is drawn almost entirely from economics and the clustering software used. Positioning relative to at least the record linkage and unsupervised evaluation literatures would allow readers to assess the novelty claim and understand where this work fits.

- **Size-2 cluster restriction is not adequately discussed.** The paper restricts all analysis to clusters of size two (footnote 4, line 186), dropping larger clusters without reporting what fraction of clusters or applications are discarded, or discussing potential bias this introduces. Real cross-applicants may submit 3+ applications, and the method's coverage may be affected. The bound derivation does not inherently require this restriction — the paper imposes it for simplicity — so a discussion of the trade-off is warranted.

- **Key lemma deferred to appendix.** Lemma 1, which establishes the critical inequality Pr[Mult | False] > p² (the step that makes Theorem 1 a strict bound rather than an equality under independence), is stated only to exist in the Appendix (line 138). The main text provides some intuition (Remark 1 and the discussion of Assumptions 1-2 on lines 136-138) but a reader cannot reconstruct the proof from the body alone. A sketch of the reasoning behind Lemma 1 in the main text would strengthen the paper.

- **No sensitivity analysis for assumption violations.** The simulation generates data from exactly the same structural assumptions used in the theory, so it only validates that the bound is consistent, not that it remains informative under violations. The paper would be stronger with stress tests where Assumption 1 (independence) is violated (e.g., correlated origination within census tracts) or Assumption 2 is violated (e.g., adverse selection where rejected applicants submit more applications), showing whether the bound remains conservative or becomes anti-conservative.

### Trivial
- The LHS of equation (2) writes "Pr[F̂alse]" — the hat is on "False" rather than "Pr," which is nonstandard notation.
- No runtime or memory usage reported for the 65.5M-record processing, despite the claim of feasibility at scale (the O(ℓ²) complexity is stated but empirical cost would be informative).

## Nice-to-Haves
- Reporting confidence intervals for the estimated precision bound (rather than a point estimate), since both p̂ and P̂_m are estimated from finite samples.
- Discussion of what happens when the structural constraint is probabilistic rather than deterministic (e.g., rare cases where an individual originates two first-lien mortgages).
- A small manually labeled subset of HMDA clusters (even a few hundred) would provide some empirical grounding beyond the theoretical bound.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"The bound on Pr[Mult | False] is asserted, not demonstrated in the body... Remark 1 acknowledges that with size-2 clusters 'it may be reasonable to assume that Pr[Mult | False] = p²' — which would make the inequality an equality, collapsing the bound entirely."** → REMOVED. The Harsh Critic misreads the paper. The paper explicitly states on line 138: "Theorem 1 is more general (i.e., it does not impose Pr[Mult | False] = p²), but Lemma 1 in the Appendix shows that, under Assumptions 1 and 2, Pr[Mult | False] > p²." The paper does NOT claim the bound collapses; it says Lemma 1 prevents that collapse.

- **"Computation and reproducibility — no runtime, memory usage, or infrastructure details... confidential HMDA data makes application irreproducible."** → REMOVED. O(ℓ²) complexity is reported (line 57), which is the standard asymptotic reporting. The confidential data issue reflects data access constraints, not author error. The simulation is fully reproducible from the description in Section 3.

- **"The paper claims the method is feasible at scale but provides no evidence."** → REMOVED. Processing 65.5M records into 314,344 clusters across 96 hyperparameter combinations IS evidence of feasibility at scale.

- **"Equation (1)/(2) has a direction error that propagates to Corollaries making the entire quantitative apparatus unverifiable."** → Partially kept as the Major weakness about notation, but the claim that the error propagates to invalidate the corollaries is removed. The corollaries treat α̂(θ) as a precision bound, which is internally consistent; only the LHS label in (1)/(2) is wrong. The simulation results computed via equation (2) produce sensible numbers (93.7% implied precision closely matching ~95% true precision), confirming the intended interpretation is correct.

## Novel Insights
The core insight — that a structural constraint on positive outcomes (at most one per individual) can convert an observable signal (multiple positive outcomes in a cluster) into a bound on clustering precision — is genuinely novel and elegantly simple. The derivation through Remark 1 (Pr[False] = Pr[Mult] / Pr[Mult | False]) cleanly separates the observable (Pr[Mult]) from the unidentified (Pr[Mult | False]), and Theorem 1 shows that mild assumptions suffice to bound the latter. This framework should generalize beyond mortgages to any setting where a per-individual outcome cap exists, though the tightness of the bound will depend on domain-specific properties of Pr[Mult | False].

## Suggestions
- Fix the LHS of equations (1) and (2) to match the text: if these are precision bounds, the LHS should be "Precision" or "1 − Pr[False | ¬Mult]," not "Pr[False]." Verify all inequality directions are consistent from Theorem 1 through the corollaries.
- Add a brief sketch of the Lemma 1 proof in the main text to make the derivation self-contained.
- Include an explicit discussion of the size-2 cluster restriction: what fraction of clusters are discarded, and what bias this may introduce.
- Either construct a small labeled validation set for HMDA or significantly temper the language around the 92.3% figure (e.g., "theoretical lower bound of 92.3%" rather than "identified with 92.3% precision").
- Add stress-test simulations where assumptions are violated to characterize when the bound remains conservative vs. becomes anti-conservative or vacuous.
- Include a related work paragraph positioning against record linkage and unsupervised evaluation literatures.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>