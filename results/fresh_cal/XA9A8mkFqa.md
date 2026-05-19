Now I have all the evidence needed. Let me construct the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

---

Here is the final consolidated review:

## Summary

This paper proposes Convolutional Signal Propagation (CSP), a non-parametric, parameter-free method for propagating signals on hypergraphs (equivalently, bipartite graphs). CSP averages node signals across hyperedges and back, with linear asymptotic complexity O(d(Σ_V + Σ_E)). The paper establishes theoretical connections to label propagation (showing CSP generalizes LP with α=1/2 to hypergraphs), Naive Bayes, and Hypergraph Convolutional Networks. Experiments on eight real-world datasets spanning citation networks, social media, and recommendation show CSP achieves competitive performance with baselines (Naive Bayes, NMF+classifiers) while being orders of magnitude faster than a simple HGCN.

## Strengths

1. **Provably efficient, implementable in a few lines of code.** The algorithm has asymptotic complexity O(d(Σ_V + Σ_E)) (Equation 5), linear in the number of nonzeros in the incidence matrix. Table 4 shows CSP executes in microseconds on small datasets and is roughly four orders of magnitude faster than the compared HGCN. The two-step procedure (Equations 1–2) avoids ever forming the dense product H D_e⁻¹ H^T, which the paper correctly identifies as critical for large-scale use.

2. **Clear theoretical grounding in established methods.** Section 4.3 shows CSP is a special case of Hyper-Conv with identity weight matrices. Section 4.4 rigorously proves CSP generalizes label propagation to hypergraphs (Equation 10 → Equation 7 with α=1/2). Section 4.5 provides an insightful qualitative comparison with Naive Bayes that correctly predicts when each method will perform better (classification vs. retrieval). These connections validate the design and situate CSP within a well-understood framework.

3. **Competitive performance achieved with zero learned parameters.** On 4 of 8 datasets (Cora, DBLP, PubMed, Corona) CSP achieves the best retrieval P@100 (Table 3), and on classification it is within 0.05 of the best on 5 of 8 datasets (Table 2). This is achieved without any training, hyperparameter tuning (beyond layer count), or GPU dependency, making the case for CSP as a practical first-line baseline.

4. **Transparent about limitations.** The paper explicitly acknowledges several limitations: NMF hyperparameters were not tuned for each dataset ("potentially impacting the performance of NMF-based baselines," line 225), NMF preprocessing time is excluded from runtime comparisons (Table 4 caption), extensions are left for future work (line 167), and HGCN was run with limited tuning. This candor allows readers to appropriately calibrate the claims.

## Weaknesses

### Fatal
None.

### Major

1. **No measures of variance or statistical significance in any result table.** Tables 2 and 3 report only averages over folds and classes, with no standard deviations, confidence intervals, or significance tests. The evaluation uses 10-fold cross-validation and multiple binary classes, so there is substantial room for variability. Without error bars, the reader cannot assess whether CSP's performance is reliably different from Naive Bayes or other baselines, or whether the "best" entries are within noise. This gap directly affects the paper's central claim that CSP is a "competitive baseline."

2. **Uneven comparison with NMF-based baselines.** Random Forest, Logistic Regression, and HGCN receive NMF-derived features with a fixed dimension of 60 and 10 iterations, with no tuning of these hyperparameters, while the classifiers themselves use default scikit-learn settings (Section 5.3). Naive Bayes (which operates on the raw incidence matrix) emerges as the strongest baseline in many settings, partly because it does not depend on the NMF preprocessing. The paper acknowledges this limitation, but the asymmetry remains: CSP natively uses the raw hypergraph structure while the NMF baselines rely on a preprocessing step whose quality is not optimized. A fairer comparison would at minimum vary the NMF dimension or also evaluate methods on raw features (e.g., sparse logistic regression on the incidence matrix).

### Minor

3. **NMF preprocessing time excluded from runtime comparison (Table 4).** The caption states "The non-negative matrix factorization was excluded from the execution time." The paper notes that LR and RF's short times on Corona and Movies are partly because "the most challenging part—extraction of structural information—is handled by nonnegative matrix factorization, which is not included in the reported times" (line 310). For a practitioner comparing end-to-end wall-clock time, this exclusion is misleading. Reporting total time (NMF + classification) would give a more honest comparison.

4. **Title's "Large-Scale" framing overstates the empirical evidence.** The largest dataset (MovieLens 25M) has ~62K nodes — moderately large but not large-scale by modern graph standards (e.g., ogbn-papers100M with 100M+ edges). While the asymptotic complexity is linear and promising, the paper does not demonstrate CSP on a dataset that would stress memory or runtime in a way that fully justifies the "large-scale" framing. This is a gap between the paper's rhetorical framing and its demonstrated evidence.

5. **Limited NLP evidence for the abstract's claim.** The abstract states CSP "achieves good results in tasks typically not associated with hypergraphs, such as natural language processing." This claim rests on a single dataset (Corona tweets with sentiment labels). A broader claim about NLP would require more diverse text tasks. This is a minor overclaim.

6. **Retrieval task's negative sampling introduces potential bias.** For methods that require negative examples (LR, RF, HGCN), negative training examples are randomly sampled from the unlabeled set, which may contain true positives (label noise, line 204). CSP does not require negatives. The paper dismisses this as acceptable because the negative class is dominant, but this asymmetric setup could systematically affect relative performance. The paper does not discuss whether this could advantage CSP.

7. **HGCN evaluation is limited and not a strong performance benchmark.** HGCN was run with a single layer, 15K epochs, default settings, and only 5 folds on some datasets (line 225). The paper states this is because HGCN is "numerically intensive," but the result is that the HGCN comparison serves primarily as a computational cost illustration rather than a meaningful performance comparison. The paper would benefit from acknowledging that stronger hypergraph methods (e.g., AllSet, HyperGCN) likely outperform CSP.

### Trivial

8. **Ambiguous phrasing about sparsity preservation.** Line 69 says "Equation 4 preserves the sparsity of H," but line 115 correctly notes that the explicit matrix product H D_e⁻¹ H^T "does not preserve the sparsity of H." The resolution (the two-step implementation avoids forming the dense product) is clear from context but the phrasing in line 69 could mislead a casual reader into thinking the dense matrix product itself is sparse.

## Nice-to-Haves

- **An ablation for the α extension (Section 4.6.2) on at least one small dataset** would demonstrate that CSP truly generalizes label propagation and that α has meaningful behavior. This would deepen the theoretical contribution without a large experimental campaign.
- **Including a brief discussion of how optimal layer count relates to graph properties** (e.g., sparsity, training set density) would help users choose the number of CSP layers in practice.
- **An inductive experiment** (e.g., hold out hyperedges rather than nodes) would strengthen the versatility claim made in Section 4.6.3, even on a single small dataset.

## Removed Points

These points were flagged by the reviewers but are removed from the main review with justification:

- **"Naive Bayes comparison is qualitative, not formal"** — The comparison in Section 4.5 is appropriately presented as an insightful analogy, not a formal equivalence proof. For a baseline paper, this level of analysis is entirely appropriate. Removed as not a genuine weakness.
- **"Single-layer un-tuned HGCN is not a strong baseline"** — The paper is transparent about this and states HGCN serves a computational cost comparison. The critic acknowledges this. Removed as duplicative of already-included weakness #7 (which is kept).
- **"Extensions not evaluated"** — The paper explicitly states "their comprehensive evaluation is left for future work" (line 167). This is a scope decision, not a weakness. Moved to Nice-to-Have.
- **"Sensitivity to number of layers not analyzed in depth"** — The paper already discusses oversmoothing (line 290) and notes optimal layers vary by dataset. A deeper analysis would be nice but is not required. Moved to Nice-to-Have.
- **"Missing hypergraph-specific baselines (AllSet, HyperGCN)"** — The paper's stated goal is to provide a simple baseline, not to compare with SOTA hypergraph methods. This is scope creep. Removed.
- **"No inductive evaluation"** — The paper clearly scopes this as future work. Removed and moved to Nice-to-Have.
- **"Isolated nodes degrade performance (honest acknowledgment)"** — The critic calls this an "honest acknowledgment," not a weakness. Removed.
- **Strengths removed from Strength Finder** — None were removed; all four were specific and evidence-grounded.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective on the paper that the paper itself does not present.

## Suggestions

1. Add standard deviations (over cross-validation folds) to all result tables. This is the single most impactful improvement — it directly supports the "competitive" claim and costs little to produce.
2. In Table 4, either include NMF preprocessing time in a separate column or add a footnote reporting it for each dataset, so practitioners can assess end-to-end cost.
3. Tone down the "large-scale" framing in the title or add at least one experiment on a dataset with >100K nodes to support it.
4. Add a brief α-ablation on Cora or PubMed to validate the generalization to label propagation.
5. Note in the abstract that the NLP claim is based on one text classification dataset, or broaden the experiments to include another text domain.

## Score and Decision

The paper presents a clean, well-motivated, and theoretically grounded method with practical value. The main weaknesses — absence of variance estimates and uneven baseline configuration — are real but not fatal; the method itself is sound and the core claims are likely correct. The paper's transparency about its limitations is commendable. With the addition of error bars and a fairer baseline calibration, the evaluation would fully support the claims. I recommend acceptance with minor revisions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>