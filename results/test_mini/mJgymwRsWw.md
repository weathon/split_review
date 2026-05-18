Now I have sufficient calibration data. Let me write the consolidated review.

## Summary

The paper proposes APDD (Active Probabilistic Drug Discovery), a three-stage pipeline for cost-effective virtual screening: (1) probabilistic clustering of molecules using Tanimoto similarity with the MPC algorithm, (2) selective docking of representative molecules from each cluster, and (3) active learning to iteratively query molecules for wet-lab experiments, updating binding probabilities within clusters. The method is evaluated on 90 targets from DUD-E and LIT-PCBA benchmarks plus a 1.4M-molecule simulated library, reporting average reductions of ~80% in docking and ~70% in wet experimental costs compared to full Vina enumeration.

## Strengths

- **Extensive multi-benchmark evaluation**: The paper evaluates on 90 targets across DUD-E (79 proteins) and LIT-PCBA (11 proteins) plus a 1.4M-molecule simulated library. This breadth of evaluation is a genuine effort that exceeds what many drug discovery papers attempt, and the method demonstrates consistent cost savings across diverse targets.

- **Quantified cost reductions are non-trivial**: The reported average reductions of 82%/75% on DUD-E and 85%/40% on LIT-PCBA (docking/wet experiments) are substantial figures. Even accounting for the weak baseline (discussed below), achieving the same recall as full enumeration with these reductions is practically meaningful for the specific scenario where the only alternative is exhaustive docking.

- **Scalability demonstration on million-size libraries**: Section 5.4 shows APDD operating on datasets augmented to 1.4M molecules, recovering the target number of actives with ~20% of the docking/wet-lab cost of Vina enumeration. This provides evidence that the method's cost advantages persist at scales relevant to industrial virtual screening.

- **Integration of multi-modal docking scores**: Section 4.2 provides a closed-form fusion rule (Equation 2) for combining probabilities from multiple docking methods under a conditional-independence assumption, adapted from MPC. This is a well-motivated design for combining complementary scoring functions without ad-hoc weighting.

## Weaknesses

### Fatal

None.

### Major

- **Only one baseline, and it is the most expensive one**: The paper compares APDD only against Vina Enumeration (VE), which docks *all* molecules and tests the top-scoring ones in wet experiments. This is the most computationally expensive possible strategy, making the reported 80-85% savings unsurprising. The paper does not compare against any cheaper alternative: (a) existing cluster-then-dock approaches (UMAP+centroid, fragment-based enumeration) that the paper itself discusses in Related Work (line 71-73), (b) standard active learning methods that operate without retraining (e.g., uncertainty sampling or expected improvement over a precomputed score), or (c) simpler strategies like random sampling from clusters. The paper's justification for excluding ML methods — "machine learning models cannot be retrained or fine-tuned due to the limited number of wet experiments" (line 177) — does not apply to methods that use a precomputed score (e.g., docking score itself) as the acquisition target. Without these comparisons, the claimed savings cannot be attributed to the probabilistic refinement machinery specifically. A large fraction of the savings likely comes from the simple strategy of clustering before docking, independent of the probabilistic apparatus.

- **The central "probability" model is an unsupported assumption**: Equation (1) defines P(e_ij=1) = Tanimoto similarity of Morgan fingerprints. The paper calls this "approximate" (line 79) but provides no calibration or validation of this mapping. Tanimoto similarity is bounded [0,1] but does not satisfy probability axioms; more importantly, there is no evidence that Tanimoto similarity between two molecules' fingerprints corresponds to the probability they both bind the same target. The paper mentions validation "using statistics from Lit-PCBA/DUD-E/PubChem datasets" (line 77) but presents none of this validation. Since the entire APDD pipeline — clustering, docking probability conversion, and active Bayesian refinement — rests on treating these Tanimoto scores as probabilities, this is a foundational issue. The method may still work as a heuristic pipeline, but the "active probabilistic learning" framing is unsupported.

- **No per-protein variance, statistical significance, or failure analysis**: Results are reported only as aggregate averages. The paper acknowledges failure cases where Vina scores are degenerate (MAPK1, KAT2A, PKM2) and APDD requires equal or more wet experiments, but these are neither quantified nor analyzed to understand when APDD works and when it does not. Without confidence intervals, error bars, or analysis of the conditions that cause failures, the reader cannot assess the reliability of the method across different protein targets.

### Minor

- **The query strategy derivation is heuristic rather than rigorous**: Equations (3)-(5) for expected recall improvement are stated without derivation. The cluster-based variant (E[Δn|i] = P(e_i=1)(1-P(e_i=1))|W|) is justified as "this formula approximates the difference" (line 139), which is a heuristic. The molecule-based variant assumes conditional independence of e_i, e_j, and e_ij (line 141) without justification. The active learning procedure may be sensible as a heuristic, but the paper's framing as a principled probabilistic method is undermined by these ad-hoc derivations.

- **Validation of the clustered-distribution assumption is self-referential**: Section 5.3 shows that active molecules concentrate in small clusters, but this analysis uses the same probabilistic clustering method (presumably MPC with Tanimoto) that APDD employs. This is a sanity check — it confirms the data has the property the method assumes — but it is not an independent validation. Comparing against alternative clustering methods (HDBSCAN, K-means on fingerprints) would strengthen the claim that the clustered-distribution property is a real feature of the data, not an artifact of the specific clustering algorithm.

- **No sensitivity analysis on key hyperparameters**: The paper fixes k-nearest neighbors to 50, the number of representatives per cluster to 2, and the maximum docking probability to 0.3 without any sensitivity study. The method's robustness to these choices is not established.

### Trivial

None.

## Nice-to-Haves

- Include simpler baselines such as random selection from clusters, UMAP+centroid docking, or uncertainty sampling over Vina scores. This would isolate what portion of savings comes from clustering vs. the active probabilistic refinement.
- Report per-protein results with error bars or confidence intervals and systematically analyze the conditions under which APDD requires as many or more experiments than VE.
- Validate the Tanimoto-to-probability mapping empirically (calibration curve on held-out binding data) or replace it with a properly calibrated probabilistic model.
- Add sensitivity analysis showing performance as a function of k-nearest neighbors, number of representatives, and maximum docking probability.
- State the target recall rate explicitly (the paper says "until the expected recall number meets our requirements" — what recall? what number?) and hold it constant across comparisons.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength from Strength Finder: "Empirical validation of the clustering assumption" (Table 3)** — This conflicts with the verified weakness (item 4 above) that the validation is self-referential. Removed per the rule that when strength and weakness disagree, the weakness wins.

- **Strength from Strength Finder: "Active learning tailored to probabilistic clusters"** — This conflicts with the verified weakness (item 3 above) that the query strategy derivation is heuristic and insufficiently justified. Removed per the same rule.

- **Criticism: "MPC cannot accept Tanimoto as valid input for probabilistic clustering"** — The paper states MPC "requires no prior knowledge to learn distance-probability mapping function automatically from multi-view distribution by consistency constraints" (line 75-76), indicating MPC can operate on similarity measures. This sub-claim is not supported against the paper's description, though the broader issue of equating Tanimoto to probability remains.

- **Criticism: "The paper provides no justification that Tanimoto similarity estimates a binding-related probability"** — The paper *does* claim validation exists (line 77: "further validated using statistics from Lit-PCBA/DUD-E/PubChem datasets") but does not present it. The criticism is softened to reflect that the paper claims validation exists but doesn't show it.

- **Strength from Strength Finder: "Principled fusion of multi-modal docking scores"** — This is retained as a genuine strength (included above). The fusion rule is a clean adaptation of MPC's method.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a recurring challenge in drug discovery papers: a method framed as "probabilistic" or "Bayesian" often reduces to heuristics when the core probability model is specified ad-hoc. This paper is a clear case where abandoning the probabilistic framing and presenting APDD as a heuristic clustering+active-learning pipeline would be more honest and likely better received by reviewers whose expectations are set by the "probabilistic" framing.

## Suggestions

1. Add at least 2-3 cheaper baselines: (a) random selection from MPC clusters (no active refinement), (b) UMAP+centroid docking, (c) greedy selection by Vina score without clustering. This is the single most important change to establish the method's value.
2. Remove the "probabilistic" framing unless Tanimoto similarity can be rigorously calibrated as a binding probability. Present APDD as a heuristic cluster-then-active-learn pipeline, which is what it actually is.
3. Report per-protein results with variance/confidence intervals and explicitly analyze failure cases.
4. Add sensitivity analysis for the three fixed hyperparameters (k=50, 2 representatives, max prob=0.3).
5. State the target recall rate explicitly and ensure it is held constant across all comparisons.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison to APDD |
|------|-----------|-------------------|
| `CaNp8ALCRT.md` (IB-MDP, Drug Discovery) | 3.0 | Similar: both propose ML methods for drug discovery with insufficient baselines and questionable methodological foundations. APDD evaluates on more targets but has a more fundamental issue with its probability model. |
| `An87ZnPbkT.md` (GNNAS-Dock) | 3.0 | Similar: both have single-baseline comparisons and insufficiently supported methodological choices. |
| `y2ch7iQSJu.md` (Survival AL) | 2.0 | Worse: fundamental flaws in problem formulation. APDD is clearly stronger. |
| `kYg04pmX7i.md` (COLT, Molecular AL) | 4.4 | Stronger: better experimental methodology, clear negative results, rigorous comparisons. APDD lacks the comparative rigor. |
| `bKAqK7Bh7n.md` (MF-LAL) | 5.2 | Stronger: more technically novel with better-supported claims, though also has evaluation concerns. |
| `S8gbnkCgxZ.md` (Bioactivity Prediction) | 7.0 | Much stronger: clear contribution (dataset + metrics), rigorous evaluation. APDD is far behind in experimental and methodological rigor. |

Based on the calibration: APDD sits firmly in the range of papers scoring ~3.0. It shares the core weakness of the mid-3 papers (insufficient baselines, questionable methodological foundation) without the redeeming experimental rigor or technical novelty of higher-scoring papers. Its evaluation breadth (90 targets) is a relative strength but does not compensate for the fact that the central claim rests on unsupported assumptions and a single, trivial baseline.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>