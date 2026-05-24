Now I have all the evidence I need. Let me write the consolidated review.

## Summary

This paper proposes a method to lower-bound precision and relative recall for unsupervised anonymous record linkage, exploiting a structural constraint (at most one positive outcome per individual, e.g., one originated mortgage). Theorem 1 bounds the false positive rate using only the observable origination rate and the fraction of clusters with multiple originations. The simulation shows the bound closely tracks ground-truth precision, and a large-scale application to 65.5 million HMDA mortgage records demonstrates feasibility at scale, with the preferred specification achieving a lower bound of 92.3% precision.

## Strengths

- **Novel theoretical contribution**: Theorem 1 and its corollaries provide the first observable lower bounds on precision and relative recall in unsupervised record linkage under the "at most one positive outcome" constraint. The derivation is clean and the bounding argument (Pr[Mult|¬False]=0 → Pr[False] ≤ Pr[Mult]/p²) is elegant and intuitive. (Section 2.2)

- **Simulation validates bound tightness**: In the simulation, the proxy precision computed from observable quantities (Figure 4a) closely matches the true precision computed with ground-truth individual IDs (Figure 3a). The paper states "We first note the close resemblance between Figures 3a and 4a," providing direct evidence that the bound is tight under realistic conditions. (Section 3.1)

- **Real-world deployment at massive scale**: The method is applied to 65.5 million confidential HMDA records, spanning 2018–2023. The preferred specification detects 314,344 cross-applicant clusters with an estimated lower bound of 92.3% precision. This demonstrates feasibility on a scale that few labeled-data approaches could achieve. (Section 4)

- **Practical bound refinement**: Dropping known-false-positive clusters (those with multiple originations) yields a tighter precision bound (Equation 1), turning a source of information that would be discarded into a method improvement. (Section 2.2)

- **Clean experimental framework**: The precision-sample-size frontier (Figure 5) provides an intuitive visualization for tuning ε, and Corollary 2 gives a principled basis for selecting the operating point via weighted precision-recall scores without any labeled data.

## Weaknesses

### Fatal

None.

### Major

- **Headline "92.3% precision" is presented as a point estimate rather than a lower bound.** The abstract states "identifies cross-applicants with 92.3% precision" and the conclusion says "achieving an estimated precision of 92.3%," both without the qualifier "at least." While the theoretical development (Section 2.2) correctly uses "lower bound" throughout, the paper's most prominent claims drop this qualifier. A reader could reasonably infer that 92.3% is the *actual* measured precision, whereas it is a lower bound that could be much looser in practice (the gap between bound and truth is unknown on real data since ground truth is unavailable). This is a framing issue that should be corrected consistently.

- **Claim of method-agnosticism is not empirically supported.** The paper asserts that the bounds are "method-agnostic" and "apply to any label-generating algorithm" (Introduction, Section 2.2, Conclusion), but the entire experimental evaluation — simulation and real data — uses only hierarchical agglomerative clustering. Showing that the bounds can tune or compare a different class of models (e.g., k-means, DBSCAN, or a simple threshold-based matcher) would substantiate this claim. Without it, the generality remains purely theoretical.

- **No comparison to baselines.** The paper compares only different configurations of its own algorithm (different ε values and distance functions). There is no baseline such as "treat every application as its own applicant" (trivial: zero recall on cross-applicants) or "treat all applications within a partition as the same person." Computing the bound for these baselines would demonstrate that the method can meaningfully distinguish good from poor models, which is a central selling point of the framework.

### Minor

- **Restriction to size-2 clusters is not adequately discussed.** The paper drops all clusters with more than two applications (footnote 4) in both simulation and application, but does not report how many larger clusters were formed or dropped, nor whether the bound results would change meaningfully if larger clusters were included (with appropriate multiplicity corrections). The theoretical bounds do not require size-2 clusters, so the restriction is a modeling choice that should be justified empirically.

### Trivial

- Figure 5's y-axis is labeled "implied precision" without explicitly stating in the label that it is a lower bound. This is consistent with the theoretical framing but could be clearer in the figure itself.

## Nice-to-Haves

- The simulation could report the quantitative gap (mean absolute error) between the bound and true precision across all ε values, giving readers a clearer sense of when the bound is tight versus loose.
- An external validation of detected cross-applicants on real data (e.g., comparison with credit bureau aggregates or manual record-checking) would substantially strengthen the application, though the current confidential-data constraints likely make this difficult.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"First work" claim is overselling (Harsh Critic).** The critic suggested the claim should be "first to derive such bounds under a *limited-outcomes constraint*." The paper already explicitly states the constraint it operates under and uses "to our knowledge" qualifiers. The claim is appropriately scoped.

2. **Assumption 1 independence concern (Harsh Critic).** The critic speculates about correlated origination decisions across borrowers (e.g., competing offers on the same property). This is a generic speculation about any statistical assumption, not a demonstrated violation. The paper clearly states the assumption and the bounds rely on it.

3. **Missing appendix content / proofs (Harsh Critic).** Per instructions: the parser strips appendix sections; they exist in the original submission.

4. **Reproducibility concern about confidential data (Harsh Critic).** Per instructions: criticisms about the availability/citation status of datasets and references cited in the paper are removed. The paper cites chMDA as a real dataset.

5. **Various presentation nitpicks / typos / formatting (both reviewers).** Per instructions: these are parser artifacts or minor presentation points that carry no weight in evaluation.

## Novel Insights

The harsh critic identifies a tension that is genuinely interesting beyond the paper's own claims: the bounding argument reliability is proven in simulation (where ground truth is available) and applied on real data (where it is not), but the gap between the bound and unknown truth on real data is itself unobservable. The paper would be materially stronger if it characterized this gap empirically — for example, by subsampling the simulation to see how the bound behaves when ground truth is withheld, or by showing that the bound's tightness depends on specific data properties (cluster size distribution, origination rate homogeneity) in predictable ways. The current narrative presents the simulation as validation and the real-data result as an application, but the connection between the two — exactly when and why the bound is informative — could be made more precise.

## Suggestions

1. Revise the abstract and conclusion to consistently say "precision of at least 92.3%" or "a lower bound of 92.3% on precision."
2. Add at least one alternative model (e.g., k-means with k=2 per partition, or a simple threshold matcher) to demonstrate method-agnosticism empirically.
3. Add a baseline comparison: compute the bound for trivial policies (no linking, full linking within partitions) to show that the bound meaningfully distinguishes good from poor models.
4. Report statistics on the number of dropped clusters with size >2 and discuss the sensitivity of results to this restriction.
5. Include a quantitative summary of the gap between bound and true precision in the simulation (e.g., mean absolute error across ε).

## Score and Decision

Calibration results across all rounds:

**Round 1 — Bracketing:** I searched for papers on unsupervised record linkage, theoretical bounds, and precision/recall without labels. Weak anchors in the 2.3–3.4 range (e.g., w5h443GIGo at 2.33, yNyDvFQNEm at 3.40) are substantially worse — they present niche clustering algorithms without the kind of rigorous theoretical contribution this paper makes. Strong anchors in the 7.6–8.0 range (e.g., Tzh6xAJSll at 7.60, A3YUPeJTNR at 8.00) have thorough empirical validation, multiple experiments, and polished presentation well beyond what this paper provides. The paper sits between these bands, in the 4–6 range.

**Round 2 — Narrowing:** I compared against several anchors in the 4.5–6.5 band:

- **Estimating Fréchet bounds for validating programmatic weak supervision** (f9RvYpXhFI, avg 5.50, Reject): Both papers provide performance bounds without labeled data. The Fréchet bounds paper has broader experiments (4 datasets) and asymptotic theory, but its bounds are often wide and sometimes violated. The paper under review has a cleaner, tighter bounding argument and a compelling large-scale application, but narrower evaluation (one algorithm, no baselines). **Comparable; this paper is slightly weaker empirically but has cleaner theory.**

- **Evaluating multiple models using labeled and unlabeled data** (HvkXPQhQvv, avg 6.00, Reject): Stronger empirical validation across 4 domains, but the method requires labeled data and multiple classifiers. The paper under review operates in a harder setting (entirely unsupervised). **Slightly worse than this anchor on empirical rigor.**

- **Towards Establishing Guaranteed Error for Learned Database Operations** (6tqgL8VluV, avg 6.00, Accept): Theoretical lower bounds for learned DB operations. Accepted despite limited experiments. **Comparable theoretical contribution, but the DB paper has broader scope and cleaner theoretical framing.**

- **αMax-B-CUBED** (oyFCgkkLUK, avg 4.75, Reject): A clustering evaluation metric with modest novelty. **This paper is stronger than this anchor.**

My initial bracket was 4.5–6.5. Round 2 narrowed this: the paper is clearly stronger than weak reject papers (3.x) but does not reach the empirical thoroughness of 6.0+ papers. It is most comparable to the Fréchet bounds paper at 5.50 and the SSME paper at 6.00, but with cleaner theory and weaker experiments. The framing issue with "92.3% precision" and narrow empirical validation prevent a higher score.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>