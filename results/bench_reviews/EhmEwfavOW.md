## Summary

This paper introduces HoloNets, a framework that extends spectral convolutional networks to directed graphs by replacing the graph Fourier transform with the holomorphic functional calculus (Cauchy integral formula). The key insight is that spectral filters need not rely on self-adjoint operators or a complete eigen-decompositions — any sufficiently regular function of a linear operator can be defined via contour integration. Two architectural instantiations are proposed: FaberNet (for node classification using polynomial filters) and Dir-ResolvNet (for graph-level tasks, using resolvent-based filters with provable scale-insensitivity). Experiments on five heterophilic directed datasets and the QM7 molecular regression task demonstrate competitive or superior performance relative to baselines.

## Strengths

1. **Fundamental theoretical advance**: The holomorphic functional calculus provides a principled and rigorous way to define spectral convolutions on any linear operator, eliminating the traditional requirement of self-adjointness and the graph Fourier transform. The paper correctly identifies this as a conceptual shift (Section 3.1), backing it with the Cauchy integral formula (Eq. 2) and the Jordan-Chevalley frequency response decomposition (Eq. 3), which is genuinely novel for the GNN literature.

2. **Formal stability guarantees for directed scale-insensitivity**: Theorems 3–5 (resolvent convergence, filter stability, graph-level stability) provide rigorous mathematical guarantees that Dir-ResolvNet is provably stable under resolution-scale perturbations on directed graphs. This extends the undirected ResolvNet theory to directed graphs using the notion of reaches to generalize undirected connected components — a non-trivial generalization.

3. **Consistent empirical improvements across heterophilic node classification**: FaberNet achieves the best mean accuracy on all five directed heterophilic datasets tested (Table 1), outperforming both undirected heterophily-specialized models (Gradient Gating, FSGNN) and directed methods (DirGNN, MagNet). The margins over DirGNN are 1–5%, and the improvement on Snap-patents and Roman-Empire is clear even accounting for variance.

4. **Frequency-response interpretation for directed filters**: Equation (3) provides a clean spectral-domain understanding of what directed filters do — the derivative terms \(g^{(n)}(\lambda)/n!\) — and the path-graph example (Section 3.2) illustrates concretely how this differs from undirected spectral GNNs. This provides genuine design guidance for future work.

5. **Complex-to-real reduction theorem**: Theorem 1 formally shows that any HoloNet with complex weights can be simulated by a double-width network with real parameters, giving practitioners a clear trade-off without losing expressivity.

## Weaknesses

### Major

1. **Theory-experiment gap in the scale-insensitivity evaluation (Kirchhoff condition)**. The resolvent convergence theorems (Theorems 3–5) assume a critical Kirchhoff condition: equal in- and out-degrees within the high-weight subgraph \(G_{\text{high}}\). The QM7 experiment modifies edge weights to induce directionality via "partial shielding" of heavy atoms, but the paper never verifies whether the Kirchhoff condition holds for the resulting graphs. The weight modification is described heuristically (lines 628–634), and the connection to the theory's assumptions is not established. While the empirical convergence of Dir-ResolvNet features (Fig. 2) is interesting, whether it reflects the theorem's mechanism or other properties of the architecture is unclear. The paper should at minimum discuss this gap quantitatively.

2. **Coarse-grained QM7 experiment conflates distribution-shift robustness with scale-insensitivity**. The paper reports that Dir-ResolvNet outperforms baselines by "a factor of up to 240" on coarse-grained QM7 graphs (Table 3). However, the baselines were evaluated using "previously trained networks" (line 715) from the normal QM7 task — they were not retrained or even fine-tuned on the coarse-grained data. This tests robustness to an out-of-distribution shift that the baselines were never designed or tuned for, rather than a controlled comparison of stability properties. Dir-ResolvNet's own MAE increases from 17.12 to 27.34 (a 60% relative increase), which is itself non-negligible. The framing of a "240× improvement" is misleading without acknowledging that the baseline methods were evaluated under protocol conditions that disadvantage them.

3. **No ablation studies isolating the core innovation**. The paper claims that the holomorphic functional calculus drives performance, yet provides no ablation that separates this from other architectural choices. Specifically: (a) there is no baseline that replaces the holomorphic filter with a simple polynomial in the same operator (monomial vs. Faber basis not compared experimentally), (b) there is no ablation removing backward filters or setting \(\alpha = 0/1\) to quantify the benefit of bidirectional filtering, and (c) there is no comparison against a symmetrized (undirected) version of the same operator to test whether directionality itself is being leveraged. Without these controls, the claim that the spectral approach *per se* causes improvement over spatial methods is unsupported.

### Minor

4. **Node classification gains are marginal on several datasets**. On Chameleon, FaberNet (80.33 ± 1.19) vs. DirGNN (79.74 ± 1.40) — the gap is within one standard deviation. Similarly on Arxiv-year (64.62 ± 1.01 vs. 63.97 ± 0.30). Without significance testing, the claim of "new state of the art" is technically accurate for means but may not reflect a reliable improvement. The paper would benefit from statistical significance reporting.

5. **Faber polynomial motivation is undercut by the practical implementation**. Section 3.3.1 correctly notes that without explicit spectral information, the minimal domain is a disk of radius \(\|T\|\), for which Faber polynomials reduce to monomials. This means the actual implementation uses monomial bases — the same as simple polynomial filters. The paper acknowledges this (lines 320–324) but does not discuss whether monomial bases may be ill-conditioned for higher degrees or whether the optimality claims of Faber approximation carry meaningful practical consequences. The theoretical justification for Faber polynomials is thus somewhat disconnected from what is actually implemented.

6. **Complex weights claim is not supported by controlled comparison**. The paper states that complex parameters performed best on Squirrel and Chameleon (lines 615–618) but provides no real-only vs. complex comparison under identical hyperparameters. Theorem 1 (complex-to-real reduction with doubled width) suggests a concrete trade-off, but the experiments do not test it. Without this, the observation that "complex helps" could reflect poor tuning of the real variant.

### Trivial

7. The introduction of the Kirchhoff condition (line 415) appears abruptly in Section 3.3.2 without a formal statement earlier in the main text — the paper states "we here assume equal in- and out-degrees" within a parenthetical footnote, but this condition is central to the theory and deserves more prominent treatment.

8. The concept of "reaches" is defined only in Section 2 (line 132) and then used without further elaboration when defining limit graphs in Section 3.3.2. A brief recap when it first appears in the theoretical development would improve readability.

## Nice-to-Haves

- Validation of the Kirchhoff condition on the modified QM7 graphs, or an analysis of how sensitive Dir-ResolvNet is to violations.
- An ablation replacing holomorphic filters with monomial polynomial bases on the same characteristic operator.
- Fine-tuning or at least reporting baseline training protocol for the coarse-grained QM7 task before drawing stability conclusions.
- A comparison against undirected versions of FaberNet/Dir-ResolvNet using a symmetrized operator.
- Significance tests (e.g., paired t-tests) for the node classification results where standard deviations overlap.

## Removed Points

- *"The concept of 'Kirchhoff condition' is introduced only briefly in a footnote in Section 3 without formal statement until the appendix (stripped) likely contains it."* — The Kirchhoff condition is stated in the main text (line 415), not only in a footnote. The appendix reference is a parser-stripping artifact that exists in the original submission; per instructions, such criticisms about missing appendix content are removed.
- *"The paper currently lacks any mention of implementation" / "Provide code and precomputed filter matrices"* — These are reproducibility nitpicks about artifacts that are impractical for a submission.
- *"No homophilic directed dataset tested (e.g., Cora-ML, CiteSeer with directed edges)"* — The paper explicitly scopes itself to heterophilic graphs, and the method's motivation (Section 4, line 512) targets heterophily. This is scope creep.
- *"The derivative/frequency response discussion abruptly ends"* — The paper does elaborate on guidance for scale-insensitive filters in the subsequent sections on resolvents; the connection is present, if not exhaustive.
- *Strength Finder claims that conflict with verified weaknesses* — e.g., "dramatic robustness gap with factor up to 240× better" is moved here because the underlying experiment is confounded (Weakness #2).

## Novel Insights

Beyond the paper's own contributions, one observation emerges from reading the reviews: the core methodological gap the paper identifies — that spectral GNNs have been artificially restricted to undirected graphs — is a genuinely important conceptual point that recursive application of the Cauchy integral formula cleanly resolves. However, the reviews collectively suggest that translating this theoretical advance into practical architectures requires considerably more careful experimental design than provided here. The same difficulty (connecting abstract operator theory to concrete graph learning experiments) plagued the precursor ResolvNet paper and remains unresolved. A productive direction would be to construct small-scale synthetic directed graphs where the spectral properties (e.g., eigenvalue locations, Jordan block structure) can be fully characterized, and then test whether the holomorphic calculus provides measurable benefits over spatial methods in that controlled setting.

## Suggestions

1. Most importantly: run a controlled ablation where the holomorphic filter (Faber polynomial or resolvent expansion) is replaced by a simple monomial polynomial of the same operator, under the same hyperparameter tuning protocol. This would isolate whether the functional calculus itself drives performance.
2. For the scale-insensitivity experiment, retrain baselines on the coarse-grained QM7 data (or at least fine-tune) before comparing to Dir-ResolvNet. Report both the distribution-shift scenario (current setup) and the retrained scenario separately.
3. Verify the Kirchhoff condition on the directed QM7 graphs, or discuss why violations might not affect the qualitative behavior.
4. Add significance testing (paired t-tests or confidence intervals via bootstrapping) for the node classification results where standard deviations overlap.
5. Report the real-only vs. complex parameter comparison under identical settings for at least one dataset.

## Score and Decision

**Calibration anchors** (from batch retrieval):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/P7KIGdgW8S.md` | 8.00 | Hölder Stability — cleaner theory-experiment link, stronger empirical validation. This paper matches it in theoretical depth but falls short experimentally. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/XWBE90OYlH.md` | 7.00 | Edge Signals — well-designed experiments with ablations. Current paper has deeper theory but weaker empirical methodology. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/yrgQdA5NkI.md` | 6.33 | Matrix Functions — similar use of resolvent calculus; experiments on established benchmarks (ZINC, TU). Current paper's experiments on directed heterophilic graphs are more novel but less thorough. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/s4Wm71LFK4.md` | 6.40 | Directed Positional Encodings — cleaner experiments, clearer baselines. Current paper has stronger theory but more confounded experiments. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vEgLnT9avP.md` | 5.50 | ResolvNet (undirected precursor) — similar theory-experiment gap; the current paper extends this to directed graphs but inherits the same experimental limitations. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/oKGDfMrD4A.md` | 5.75 | Adversarial Robustness (directed) — has some interesting ideas but limited scope; current paper has stronger theoretical contribution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/AxYTFpdlvj.md` | 2.00 | Graph Decoding — fundamentally flawed; current paper is much stronger in both theory and experiments. |

The paper's theoretical contribution (holomorphic functional calculus for directed spectral GNNs) is genuine and well-executed. However, the experimental validation has significant weaknesses: the theory-experiment gap in the scale-insensitivity evaluation (unverified Kirchhoff condition), the confounded coarse-grained QM7 protocol that inflates the "factor 240" claim, and the absence of any ablation studies. The node classification results are consistently positive but often within noise margins. Relative to the calibration anchors, this paper sits between ResolvNet (5.5) and Matrix Functions (6.33) — its theory is stronger than ResolvNet's, but its experiments are not yet at the level required for top-tier venues.

**Score: 5.5**

**Decision: Reject** (borderline — the theoretical contribution is real, but the experimental validation is too weak to carry the empirical claims made in the paper. A major revision with proper ablations, controlled baselines for the QM7 experiments, and Kirchhoff condition verification could make this a strong paper.)

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>