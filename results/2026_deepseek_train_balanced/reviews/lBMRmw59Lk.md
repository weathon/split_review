## Summary

This paper proposes a feature-centric geometric framework for understanding GNN phenomena. The core idea is to treat class-conditional features through their centroids, whose convex hull forms a "feature centroid simplex." Using coarse geometry (quasi-isometry), the paper compares this simplex to ideal shapes (regular vs. degenerate) and argues that simplex shape—rather than graph topology or homophily ratio alone—determines how well GNN aggregation can work. The framework yields explanations for heterophily, oversmoothing, and dataset difficulty, and motivates simple practical tricks (adding same-class edges, very early stopping).

---

## Strengths

- **Genuinely graph-independent, feature-centric perspective.** Most prior GNN theory (oversmoothing via graph spectra, heterophily via rewiring) is graph-topology-dependent. This paper builds its framework entirely from class centroids and coarse geometry (Definitions 2–3, Section 2), treating the graph only as an aggregation mechanism. The paper explicitly states this contrast (lines 14–15: "We regard node features as an intrinsic property, which is model-agnostic and does not change if the graph is modified").

- **Targeted empirical test of a specific theoretical prediction via feature re-shuffling.** The degenerate simplex theory (Corollary 1, Section 3.3) predicts that if Δₑ is degenerate, swapping features between classes should not harm performance. The paper designs and executes precisely this experiment (Table 1, lines 228–238) on five datasets. The qualitative pattern aligns: re-shuffling does not harm on degenerate-simplex datasets (Chameleon, Squirrel, Actor) but significantly changes outcomes on regular-simplex ones (Cora, Citeseer). This is a clean, model-agnostic test.

- **Unified geometric explanation that distinguishes heterophilic datasets.** Prior work treats heterophily as the primary obstacle. This paper shows that Texas (heterophilic but with a more regular Δₑ) is amenable to GNN improvement (~60%→~90%), while Actor (heterophilic with degenerate Δₑ) resists improvement (Figure 1). This insight—that simplex shape, not just homophily ratio, explains dataset difficulty—is genuinely new and not available from graph-centric approaches.

- **Oversmoothing analysis via simplex volume shrinkage with numerical verification.** The derivation of oversmoothing as convergence of Δₑ⁽ᵗ⁾ to a single point via the stochastic matrix M (Lemma 4, Section 4) provides an intuitive geometric complement to spectral analyses. Numerical verification (Cora: volume ~1.7% after 4 layers; Texas: ~2.6% after 7 layers, line 226) supports the theory.

---

## Weaknesses

### Fatal

None.

### Major

1. **Theoretical analysis conducted on a strongly simplified model, with unsubstantiated claims of broader applicability.** Section 3 explicitly considers "a 1-layer model without ReLU" and states "a 1-layer model is only slightly worse than a 2-layer model" (line 121) **without any evidence or citation**. Discarding the ReLU nonlinearity removes the central mechanism enabling non-linear decision boundaries in multi-layer models. The definition of "eventual GCN type" models (lines 123–125) attempts to extend the framework to attention, rewiring, and diffusion models, but this extension is purely conceptual—no theorems are proved for any non-GCN model, and the discussion does not establish that the simplified analysis carries over.

2. **Theoretical bounds are existential, not quantitative; key parameters are never instantiated on real data.** The theorems (Theorem 1, Theorem 2, Corollary 1) involve uninstantiated constants K and δ, with the convention (line 70) that "we will refer to the same K and δ in Lemma 2 without further mentioning." The quasi-isometry parameter ε is never estimated from feature data for any dataset. The central prediction—that simplex regularity determines hardness—remains qualitative: the paper does not compute a quantitative regularity measure (e.g., ratio of min to max centroid distance) and correlate it with achievable accuracy across datasets. Without such instantiation, the theory provides conceptual insight but not a falsifiable quantitative prediction that could be checked against the homophily ratio or other difficulty measures.

3. **Experimental reporting lacks essential rigor.** The experimental section does not report: (a) number of random seeds or runs, (b) standard deviations for any result, (c) data split percentages, (d) hyperparameter ranges for η and ℰ, or (e) the specific statistical test used to compute the claimed p-values. The results tables are embedded as images (parser artifact), so numerical values cannot be inspected. These omissions prevent independent verification and assessment of result stability.

### Minor

4. **No comparison with the homophily ratio as an alternative difficulty measure.** The paper's central claim is that simplex regularity captures dataset difficulty for GNNs. The homophily ratio is the standard difficulty measure in the literature. A direct comparison (e.g., showing that simplex regularity predicts accuracy better than homophily across a range of datasets, or that it explains the Texas vs. Actor discrepancy that homophily alone cannot) would substantially strengthen the paper's thesis but is absent.

5. **Normalization trick under-developed as a contribution.** The feature normalization trick (rescaling features to unit norm, lines 261–262) is potentially the most interesting practical finding, as it directly operates on the feature simplex. However, it is introduced late, tested only briefly in Table 3, and not integrated into the core theoretical framework. Its relationship to the quasi-isometry analysis is asserted but not developed.

6. **Re-shuffling interpretation not fully reconciled with non-trivial accuracy on degenerate datasets.** The paper shows that re-shuffling features between classes does not harm accuracy on degenerate-simplex datasets, yet these same datasets achieve above-random accuracy (as shown in Table 2). The paper does not fully explain how models distinguish classes when centroids are near-degenerate—whether through graph structure, higher-order feature moments, or other mechanisms. A more complete discussion would strengthen the framework.

### Trivial

7. The "mean-field type assumption" (line 216) in the oversmoothing analysis is stated without justification or verification, yet it is critical to the derivation of the matrix M.
8. Lemma 1 (convex position of features) is claimed to have been verified for all datasets used (line 51), but no verification details whatsoever are provided—no numbers, no test description.

---

## Nice-to-Haves

- A figure or table quantifying simplex regularity (e.g., ratio of min-to-max centroid distance, condition number of the Gram matrix of centroid vectors) across all benchmark datasets, correlated with achievable accuracy.
- Ablation study separating the contribution of each proposed trick (edge-adding vs. early stopping).
- Comparison of the "very early stopping" trick against standard validation-based early stopping to show whether the theoretical criterion yields different results.
- Discussion of how the theory applies to datasets with low feature dimensionality (since Lemma 1 depends on high-dimensional stochastic separation).

---

## Removed Points

- **"Feature re-shuffling undermines the paper's own claims about dataset difficulty" (Harsh Critic §2)**: Removed because it misunderstands the paper's claim. The paper does not assert that degenerate-centroid datasets have zero classification accuracy, only that centroid-level class distinctions are weak. Models can still achieve non-trivial accuracy using graph structure, higher-order feature moments, or distinctions among other class pairs. The observation that accuracy is unchanged after swapping is consistent with the paper's theory and does not create a contradiction.

- **"Unfair comparison: baselines may not have access to label-enhanced graph" (Harsh Critic, §4)**: Removed because the comparison is within-model (base model M vs. M-AE with tricks applied to the same model), not across models with different information. The paper's claim is that adding these tricks improves M, not that M-AE beats some other model.

- **"Missing appendix content or proofs"**: Removed per instructions (parser strips appendices from all papers).

- **Various generic formatting/style nitpicks and reproduction-related nitpicks about undisclosed hyperparameters**: Removed per instructions.

- **"Strengthening the Paper on Its Own Terms" section**: These are already covered in Minor weaknesses and Nice-to-Haves above.

---

## Novel Insights

Beyond the paper's own contributions, the most striking observation from the reviewer interactions is the asymmetry in evidentiary standards that the paper exposes. The paper makes a genuinely novel conceptual claim—that feature centroid simplex shape, not graph homophily, is the fundamental determinant of GNN success—but validates it almost exclusively with qualitative pattern-matching (Texas vs. Actor, re-shuffling on 5 datasets). This creates an uncomfortable gap: the framework is too elegant to dismiss and too weakly validated to fully accept. The paper would be substantially stronger if it treated "degree of simplex regularity" as a quantifiable variable and correlated it with performance—a straightforward analysis that would either strongly support or refute its central thesis. That the authors did not perform this analysis, despite having all the tools to do so, suggests either an oversight or a tacit recognition that the correlation may be weaker than claimed.

---

## Suggestions

1. **Quantify simplex regularity.** Compute for each dataset the ratio of the smallest to largest pairwise centroid distance in Δ_g, or the condition number of the Gram matrix of centroid vectors. Show that this measure correlates with achievable accuracy across datasets, and compare this correlation with that of the homophily ratio.

2. **Ablate the proposed tricks.** Report results with each trick applied separately to isolate their individual contributions.

3. **Add standard experimental rigor.** Report results over multiple random splits/seeds with standard deviations, specify data splits clearly, and describe hyperparameter selection methodology.

4. **Estimate ε on real data.** Compute the quasi-isometry parameter ε by finding the best approximating regular simplex for Δ_g for each dataset, and discuss whether the obtained ε values align with the framework's predictions.

5. **Address the 1-layer/no-ReLU simplification.** Either provide evidence that the simplified model's predictions hold for standard multi-layer GCNs with ReLU, or restrict the theoretical claims accordingly.

---

## Score and Decision

**Score**: 4.0 — The paper presents a genuinely novel conceptual framework with an interesting geometric perspective on GNN phenomena and includes a clever empirical test (feature re-shuffling). However, the theoretical analysis is conducted on an overly simplified model (1-layer, no ReLU) without justification that the results extend to standard GNNs, the theoretical bounds are qualitative rather than quantitative (uninstantiated constants, ε never estimated), and the experimental evaluation lacks standard rigor (no standard deviations, data splits, or ablations). These weaknesses collectively prevent the paper from meeting the evidentiary standards expected at ICLR.

**Decision**: Reject

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>