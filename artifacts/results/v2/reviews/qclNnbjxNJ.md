Now I have a thorough understanding of the paper and the calibration landscape. Let me produce the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper addresses the underappreciated problem of post-treatment selection in interventional causal discovery, where samples are selectively included after interventions. It introduces a formal framework with an augmented DAG model that explicitly represents selection, defines a finer-grained equivalence class ($\mathcal{FI}$-Markov equivalence) and a new graphical representation ($\mathcal{F}$-PAG) that can distinguish causal relations from selection-induced patterns that standard PAGs collapse. The paper proposes an algorithm ($\mathcal{F}$-FCI) to recover this equivalence class and provides empirical evidence showing improved performance over existing methods on synthetic data with post-treatment selection.

## Strengths

- **Well-motivated and clearly scoped problem.** The paper identifies a genuine gap in interventional causal discovery — post-treatment selection — that existing frameworks cannot handle because it produces the same invariant/variant patterns as true causal relations (Section 2.2, Figure 1). The motivation from biological studies (gene perturbation quality control) makes the problem concrete and relevant.

- **Novel formal framework ($\mathcal{FI}$-Markov equivalence and $\mathcal{F}$-PAG).** Definitions 2 and 5 introduce a finer equivalence class than standard interventional Markov equivalence, supported by the theoretical characterization in Lemmas 1-4 and Theorem 2. The $\mathcal{F}$-PAG representation with its four mark types (tail, arrowhead, square, circle) and eight edge types formally captures structural distinctions that PAGs cannot, as illustrated in Figure 5.

- **Clear identification of distinguishing CI patterns.** Figure 4(i) and the surrounding discussion in Section 3.2 concretely show how symmetric vs. asymmetric CI patterns involving intervention indicators ($\psi$) can separate causation from selection, and how interventions on a third variable (Type I inducing node) can resolve remaining ambiguities. This provides the core insight that the algorithm builds on.

- **Empirical improvement over multiple baselines.** On synthetic data with latent confounders and post-treatment selection, $\mathcal{F}$-FCI achieves higher DAG precision and lower SHD than six baselines (GIES, IGSP, UT-IGSP, JCI-GSP, FCI-interven, CDIS) across varying sample sizes (n=500-2000) and variable counts (d=10-25) in Figure 6, including both hard and soft intervention settings.

## Weaknesses

### Major

- **Missing ablation study that isolates the method's specific contribution.** The experimental comparison shows that $\mathcal{F}$-FCI outperforms baselines, but all baselines are methods that were not designed for post-treatment selection. The critical control is absent: a version of $\mathcal{F}$-FCI that uses the same augmentation (intervention indicators + selection node) and the same CI tests but applies only standard interventional FCI orientation rules (without the Type I inducing node detection and $\mathcal{F}$-PAG-specific steps). Without this ablation, the performance gain cannot be attributed to the novel identification machinery (Type I detection, $\mathcal{F}$-PAG orientation) rather than to the more general benefit of using interventional data in a selection-augmented model. The comparison against FCI-interven partially addresses this concern but does not isolate the novel steps.

- **Algorithm description has critical gaps that prevent full understanding or reproduction.** Two specific issues:
  1. **AllPaths is undefined.** Step 2.1 conditions on $C \subseteq \{X_n : X_n \in \text{AllPaths}(\mathcal{G}_p^{(0)}, X_{\mathcal{I}^{(i)}}, X_{\mathcal{I}^{(j)}})\}$. The function $\text{AllPaths}$ is never defined — it is unclear whether it returns all nodes on all paths, only nodes on some paths, or paths of a specific type. This makes the conditioning set search space ambiguous and prevents assessment of computational feasibility.
  2. **Type I inducing node detection is not operationalized from data.** Definition 6 defines inducing nodes in terms of $\mathcal{F}$-PAG marks ("incoming arrowhead into a square (Type I) or adjacent two squares (Type II)"), but the $\mathcal{F}$-PAG is the *output* of the algorithm. While Step 2.3 describes CI tests ($\psi_n \perp\!\!\!\perp X_{\mathcal{I}^{(i)}}$) that would detect them, the paper never specifies how candidate Type I inducing nodes are identified *before* the $\mathcal{F}$-PAG is constructed. The algorithm appears to require iterating over possible non-endpoint nodes on inducing paths, but how these candidate nodes/paths are enumerated is not described. This creates a circularity between the definition and the detection procedure.

- **Real-data validation lacks quantitative evaluation.** The real-world experiment on the Norman et al. (2019) gene perturbation dataset is described only qualitatively: "We report both the regulatory (causal) links and the spurious dependencies induced by post-treatment selection, as identified by $\mathcal{F}$-FCI in Figure 13" (Section 5.2). No quantitative metrics (precision/recall against a known gold standard or curated database) are reported in the main text. The evaluation via Enrichr is mentioned but without numerical results. This substantially weakens the real-data support for the method.

### Minor

- **No proof sketches for key theoretical claims in the main text.** Lemmas 2-4 and Theorems 1-4 are stated without proof or proof sketch. While full proofs are in the appendix (inaccessible due to parser stripping), at least a brief sketch of the reasoning behind Lemma 3 (tail condition from marginal invariance) and Theorem 2 (graphical criteria equivalence) would give the reader confidence in the theoretical framework and is standard practice for papers that claim soundness/completeness.

- **Limited scope of the completeness result.** Theorem 4 states completeness only for "substructures represented by tail, arrowhead, square, $\blacktriangleleft$, and $\blacktriangleright$ between a pair of intervened nodes." The overall $\mathcal{F}$-PAG for all variables (including non-intervened ones) is not guaranteed to be fully identified. This honest limitation should be more prominently discussed in the main text rather than only appearing in the theorem statement.

- **Scalability and complexity are not discussed.** The algorithm as described appears to examine all subsets of variables along paths between every pair of intervened nodes, which could be exponential in the number of variables along those paths. There is no worst-case complexity analysis or discussion of practical heuristics in the main text (scalability results are deferred to the inaccessible Appendix, Figure 11).

### Trivial

- The CI pattern table in Figure 4(i) uses column numbers 1-6 without clear mapping to the subfigures (a)-(h), making it hard to parse quickly.

## Nice-to-Haves

- An ablation study comparing $\mathcal{F}$-FCI against a version that uses the same interventional CI tests but applies only standard PAG orientation rules (from Kocaoglu et al. 2019) would cleanly isolate the benefit of the $\mathcal{F}$-PAG-specific steps.
- A discussion of the statistical reliability of CI tests involving $\psi$ (a binary variable that can be highly imbalanced) would be valuable, along with sensitivity analysis for different sample sizes and effect sizes.
- Quantitative results on the real-world dataset (e.g., precision/recall against a curated gene interaction database) would substantially strengthen the empirical contribution.

## Removed Points

These points were flagged for removal but are preserved here for reference:

- **Pseudocode formatting (all CI conditions identical).** The harsh critic noted that all `if CIs == (⊥,⊥,⊥,⊥)` blocks have identical conditions in Algorithm 1. This is a parser formatting artifact — the original submission would show distinct CI patterns. The conceptual mapping is described in the text and Figure 4(i).

- **Appendices/Proofs missing.** Criticisms about missing proofs, appendix content, or supplementary materials. These are stripped by the parser; the original submission contains them.

- **Code repository not shown.** The paper states a Python implementation is available but the URL is omitted for double-blind review. This is standard practice.

- **Equation (1) factorization concern.** The harsh critic questioned whether $p(X | S=1)$ factorizes as shown. In the augmented DAG framework where $S$ is explicitly included as a node, this factorization is correct: each conditional factor conditions on $S=1$ where $S$ is a parent. This is conceptually sound for the model.

## Novel Insights

The key insight that emerges from the reviews but is not fully articulated in the paper is that post-treatment selection creates a specific type of identifiability problem that lies *between* the standard causal and latent confounder cases: selection-induced dependencies are structurally symmetric (both endpoints show the same mark type) whereas causal relations are asymmetric, but existing PAG representations cannot capture this distinction because they only encode tails and arrowheads. The paper's proposal to add a square mark to denote selection-specific inducing paths is the natural graphical extension, and the reliance on Type I inducing nodes (intervened intermediate variables) to break the symmetry is clever. However, the practical limitation — that the method only fully resolves structures when such Type I nodes exist — is more severe than the paper emphasizes: in sparse perturbation experiments where only a few variables are intervened on, the method may not have access to the intermediate nodes needed to disambiguate the most interesting edges.

## Suggestions

1. **Add an ablation study.** Compare $\mathcal{F}$-FCI against a version that uses the same CI tests and the same augmented skeleton, but applies only standard PAG orientation rules from the interventional MAG literature (e.g., Kocaoglu et al. 2019) without the Type I inducing node detection and $\mathcal{F}$-PAG-specific orientation steps. This would directly quantify the value of the novel machinery.

2. **Define AllPaths and operationalize Type I detection.** Either define $\text{AllPaths}(\mathcal{G}, X_i, X_j)$ formally (all vertices on any path between $X_i$ and $X_j$ in graph $\mathcal{G}$) and discuss computational considerations, or replace it with a more efficient neighborhood-based search strategy. For Type I inducing nodes, provide a clear operational criterion: e.g., "a candidate inducing node $X_n$ is any non-endpoint node on an inducing path between $X_i$ and $X_j$ such that $X_n$ is an ancestor of $S$ or of one of the endpoints." Then specify how candidate paths are enumerated.

3. **Provide proof sketches.** Even one sketch in the main text — e.g., the reasoning behind Lemma 3 (why a tail at $X_i$ corresponds to every inducing path beginning with a tail in the augmented DAG) — would substantially increase confidence in the theoretical claims.

4. **Add quantitative real-data results.** Report precision/recall or enrichment scores against known regulatory interactions for the Norman dataset, at least for the regulatory edges identified by $\mathcal{F}$-FCI.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round/Bucket | Comparison |
|--------|-----------|-------------|-----------|
| `xByvdb3DCm` (When Selection meets Intervention) | 8.00 | R1-topic-high | Topically very similar (pre-treatment selection), much cleaner algorithm description and stronger theory presentation. Our paper is substantially weaker. |
| `G5KbDVAlI6` (Gene Regulatory Network Inference with Selection) | 4.00 | R1-topic-mid | Shares similar issues: unclear definitions, small-scale experiments, missing baselines. Our paper has stronger problem motivation and more novel contributions. |
| `Bp0HBaMNRl` (Differentiable Causal Discovery) | 6.75 | R1-topic-mid | Strong theory paper with clear algorithm. Our paper is less complete and less well-specified. |
| `qe1CsfnN1W` (Causal Effect Estimation with Latent Confounders) | 6.25 | R1-topic-mid | Cleaner theoretical framework. Our paper has comparable motivation but weaker execution. |
| `ZXs3pkmrRG` (Test-Time Learning of Causal Structure) | 5.50 | R2-narrow | Rejected paper with split reviews (8,3,6,5). Algorithm description had gaps. Our paper is comparable in quality. |
| `x2rZGCbRRd` (Extracting Post-Treatment Covariates) | 5.50 | R2-narrow | Different topic (effect estimation, not discovery). Clearer experiments. |
| `Lxst78Rrwj` (Causal Graph Learning via Distributional Invariance) | 5.00 | R2-narrow | Had presentation gaps and unclear definitions, but extensive experiments. Our paper has stronger novelty but weaker experiments. |
| `2pEqXce0um` (Root Cause Analysis) | 4.50 | R2-narrow | Had unclear definitions and missing details. Comparable presentation quality to our paper. |

**Round 1 bracket:** Based on the topic-anchored queries, the paper sits in the middle-to-low band — weaker than the 8.0 anchor on the same topic, stronger than the 4.0 GRN paper. **Initial bracket: 4.0 – 5.5.**

**Round 2 narrowing:** Comparing against papers scoring 4.5-5.5, the paper under review has stronger novelty and problem motivation than the 4.5-5.0 papers but shares their presentation gaps (undefined terms, missing ablations). The paper is somewhat stronger than the 4.5 Root Cause Analysis paper but clearly weaker than the 5.5 Test-Time Learning paper (which at least had a fully specified algorithm). **Narrowed bracket: 4.5 – 5.0.**

The low-band anchors (4.0-4.5) typically fail on: unclear/undefined key concepts, missing experimental controls, weak real-data validation, and algorithm descriptions that leave critical gaps. The paper under review shares *all* of these failure modes to varying degrees. The score must reflect that.

**Final score: 4.5**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>