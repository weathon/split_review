- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 3, 1, 3
Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

scKGOT proposes integrating a Ligand-Receptor-Pathway Knowledge Graph (LRP-KG) with optimal transport to infer intercellular signaling from scRNA-seq data. The method factorizes ligand-receptor prediction into a gene-importance score and a pathway-knowledge-discrepancy term, computes a Gromov-Wasserstein transport plan from expression-derived distance matrices, and derives pathway-level scores from the transport solution. The paper provides benchmarking against KGE methods and cell-cell communication tools, plus qualitative case studies in placenta, testis, and liver tissues.

---

## Strengths

- **High ranking precision for ligand-receptor pairs.** scKGOT consistently ranks target pairs within the top 1–5 positions across datasets, achieving percentile ranks frequently approaching 0.999 with minimal variance (Section 4.2). This directly supports the claim of superior prioritization over existing cell-cell communication methods.

- **Interpretable multi-level output.** The framework produces heatmaps and Sankey diagrams that trace ligand–receptor–pathway connections with connection thickness reflecting interaction strength (Section 4.3, Fig. 2c–d). This goes beyond black-box scoring and supports the interpretability claim.

- **Demonstrated robustness in ablation experiments.** Performance remains stable when up to 20% of KG facts, 30% of low-expression genes, or 70% of cells are removed (Section 4.5). This provides concrete evidence of resilience under data reduction, a practically useful property.

- **Principled probabilistic factorization.** Equation 2 decomposes the prediction into a gene-importance term and a pathway-knowledge-discrepancy term, which provides a clean mathematical framing for pathway-aware signaling inference (Section 2).

- **Biologically grounded case studies.** The method recovers known pathway activities (TGF-β in placenta, Wnt in testis, Notch signaling and ECM remodeling in tumor vs. non-tumor liver) in three distinct biological contexts (Section 4.4), demonstrating that its outputs align with established biology.

---

## Weaknesses

### Fatal
None.

### Major

1. **The integration of the knowledge graph into the optimal transport framework is not specified.**  
   The paper claims "Knowledge Graph Optimal Transport" and states that LRP-KG pathways provide "initial estimates that guide the search process" (Section 3). However, Equation 3 is the standard Gromov-Wasserstein distance with squared intra-cost differences — it contains no KG term, no pathway index, and no structural coupling between the knowledge graph and the OT loss. The text oscillates between describing a single global transport plan and "enumerating multiple pathways" / "a weighted average across signaling transportation problems" (Section 3), but the equations (Eq. 3–6) are pathway-agnostic. The reader cannot determine how the KG constrains, initializes, or regularizes the OT problem. For a method paper whose title centers on "Knowledge Graph Optimal Transport," this is a significant gap.

2. **The relationship between the global OT solution and per-pathway scoring is unclear.**  
   The formulas for s₁ (Eq. 4) and s₂ (Eq. 5) contain no dependence on the pathway index wₙ, yet the problem formulation (Eq. 2) sums over pathways wₙ with factors s₁(z,wₙ,D) and s₂(wₙ,D). The paper states that "γ* directly computes s₁ and s₂" but does not explain how a single transport plan decomposes into pathway-specific scores. If separate OT problems are solved per pathway (as hinted by "weighted average across signaling transportation problems"), this should be reflected in the equations and constraints. As written, the pathway decomposition in Eq. 2 and the OT solution in Eqs. 3–6 appear decoupled.

3. **Accuracy metric for cell-cell interaction comparison is undefined.**  
   For the comparison against NicheNet, CellPhoneDB, SingleCellSignalR, CellChat, and CellCall (Section 4.2), the paper reports "accuracy" and "percentile rank" but does not specify: (a) how predictions are binarized from scores, (b) what threshold is used, (c) whether all methods are compared on the same binary decision rule, or (d) what ground-truth labels are used. Without this, the claim of "accuracy levels comparable to these baselines" cannot be verified, and the percentile rank comparison lacks context about the candidate set against which ranks are computed. Standard metrics (e.g., precision-recall curves, AUPR) would also strengthen the evaluation.

### Minor

1. **KGE baseline comparison is not informative for the paper's core claim.** The paper compares scKGOT against TransE, DistMult, RotatE, and ComplEx — methods that use only the KG structure and do not incorporate scRNA-seq expression data (Section 4.1). scKGOT has access to strictly more information (expression + KG). Showing superior Mean Rank is expected and does not test whether the *integration* mechanism is effective. A comparison against KG-OT variants that ablate the KG component (data-driven GW only) would isolate the contribution.

2. **Percentile rank candidate set is not described.** The text claims scKGOT ranks "target ligand-receptor pairs within the top 1–5 positions out of hundreds or even thousands of potential candidates" (Section 4.2), but does not specify how the candidate set is constructed, how percentile rank is normalized, whether the same candidate set is used across methods, or whether trivial negatives inflate the metric. This makes the headline "0.999" figure difficult to assess.

3. **Eleven datasets are used but none are explicitly listed.** The paper mentions "6 human and 5 mouse scRNA-seq datasets" (Section 4.1) and provides three tissue examples in the case studies, but does not provide a table with dataset names, cell types, number of cells, number of known LR pairs, or download sources. This omission limits the reader's ability to assess the breadth of evaluation and reproduce the experiments.

4. **No limitations or failure-case discussion.** The paper lacks any limitations section. Potential issues — reliance on curated pathway coverage (missing novel pathways), sensitivity to gene set size for small pathways, assumption that signaling equates to transcript-level co-occurrence, scalability for datasets with many cell types — are not discussed, which is a notable omission for a method paper.

5. **Inequality constraints in the OT formulation are not justified.** Equation 3 uses γ𝟙 ≤ p, γᵀ𝟙 ≤ q (inequalities) rather than the standard equality constraints in optimal transport. The paper does not explain why inequality constraints are used or how they affect the solution (e.g., whether some mass is allowed to remain untransported).

### Trivial

- The introduction contains two near-identical paragraphs (lines 14–18 and lines 18–19), both starting with "Inspired by the remarkable performance of optimal transport…", evidently two draft versions that were not reconciled.
- "Correlation distance matrices" are referenced as the entries of C₁ and C₂ but the exact formula (1-Pearson? Spearman? other?) is not stated.

---

## Nice-to-Haves

- **Replace KGE baselines with more informative comparisons**, such as: (i) scKGOT without the KG (data-driven GW only), (ii) scKGOT without the OT (simple expression correlation within pathways), and (iii) existing methods using standardized metrics with error bars per dataset.
- **Report per-dataset tables** with standard deviations and ground-truth LR pair counts, rather than aggregate box plots.
- **Specify the OT solver** used (Sinkhorn iterations, proximal point, etc.) and report compute time and memory usage, especially given the 2M+ KG triples.
- **Provide formal justification for the inequality constraints** and the percentile-based normalization (1-Percentile) in Eq. 5.
- **Validate the percentile rank metric** by showing that the candidate sets are non-trivial and that ranks are not driven by obvious negatives.

---

## Removed Points

These points were flagged by the original reviewer but are removed here for the following reasons:

- **"No statistical tests"** — The paper explicitly states "permutation testing with 100 iterations" is used (Section 4.1, Metrics). The raw test results are not shown, but the claim of no testing at all is inaccurate. The point about not reporting permutation test p-values is reasonable, but the framing as absent statistical testing is wrong.
- **"Figure not rendered" / "Table 1 numbers not visible"** — These are PDF-to-text parsing artifacts. The figures and table exist in the original submission and are merely not transcribable from the extracted text.
- **"Missing appendix content"** — Appendices are stripped by the parsing pipeline; they exist in the original submission.
- **"If the candidate set contains many obvious negatives, a rank of 0.999 may be less impressive"** — Speculative about what the candidate set might contain, not a specific verified problem.
- **"No formal test (Shapiro-Wilk, Kolmogorov-Smirnov) for KDE distributions"** — Scope creep; demanding formal normality tests for an exploratory KDE visualization is not standard practice for a computational biology method paper.
- **"Could be improved by doing Y" framed as a fatal weakness** — Several of the "Strengthening" items are suggestions, not identified flaws, and are moved to Nice-to-Haves.

---

## Novel Insights

The cross-review synthesis reveals a pattern worth noting: the paper's stated contribution ("Knowledge Graph Optimal Transport") and its actual technical machinery (standard Gromov-Wasserstein + post-hoc pathway scoring) have a significant gap in the published description. However, the reviewers' divergent assessments — one focused on the methodological gap as disqualifying, the other on the empirical results as promising — suggest that the core idea (pathway-decomposed signaling inference via transport) may be salvageable if clearly specified. Most striking is that both the harsh critic and the strength finder agree on the core empirical finding: scKGOT achieves very high ranking precision for ligand-receptor pairs; they disagree only on whether the method is specified well enough to evaluate that claim. This tension between promising results and underspecified methodology is the central editorial judgment the review must resolve.

---

## Suggestions

1. **Clarify the KG-OT integration mechanism.** State explicitly: (a) whether a single global OT problem or separate per-pathway OT problems are solved, (b) how the KG constrains the distance matrices or the transport plan, and (c) what "initial estimates that guide the search process" means algorithmically (e.g., warm-start initialization, structured cost matrices, regularization). Without this, the method's name is aspirational rather than descriptive.

2. **Make the per-pathway scoring explicit in the equations.** Add a pathway index to γ*, C₁, C₂ if separate OT problems are solved per pathway. If a single global plan is used, explain how γ* is decomposed into pathway-specific components.

3. **Define accuracy computation for cell-cell method comparisons.** Specify thresholds, binarization, ground-truth labels, and candidate sets. Report precision/recall or AUPR alongside accuracy.

4. **List all 11 datasets** with names, cell-type pairs, number of cells/genes, and number of ground-truth LR pairs, so readers can assess the evaluation breadth.

5. **Replace or supplement the KGE comparison** with an ablation that removes KG information from scKGOT, isolating the contribution of the expression data versus the knowledge graph.

---
