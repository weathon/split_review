Now I have a thorough understanding of the paper and all the review arguments. Let me construct the consolidated review.

---

## Summary

This paper proposes NMCLK, a noisy multi-view contrastive learning framework for knowledge-aware top-K recommendation. The framework generates three complementary graph views (collaborative via LightGCN, semantic via KNN item-item graph from the KG, and structural via attention-based KG aggregation), applies noise perturbations to embeddings, and enforces feature alignment and field uniformity constraints alongside contrastive learning between views. Experiments on MovieLens-100k and MovieLens-1M report improvements over nine pre-2022 baselines.

## Strengths

- **Novel multi-view generation combining three complementary graph perspectives.** The paper explicitly designs a collaborative view (user-item graph with LightGCN), a semantic view (k-NN item-item graph with relation-aware aggregation), and a structural view (attention-based KG aggregation with neighborhood aggregator). This three-view design is a clear conceptual advance over prior work that typically uses one or two views, and the equations for each encoder are provided in Sections 4.1.1–4.1.3.

- **Substantial reported improvements over the compared baselines.** On ML-100k, NMCLK achieves NDCG@20=0.3456 (8.9% over KGAT's 0.3172); on ML-1M, NDCG@20=0.2313 (11.6% over KGCN's 0.2073). These gains appear consistently across NDCG, MRR, Hit, and Recall in Table 2.

- **Multi-task learning objective is explicitly specified with hyperparameters.** The final loss (Eq. 15) combines BPR, local/global contrastive losses, alignment loss, and field uniformity loss with specific weighting (α=0.2, β=0.1, λ=0.01, γ=0.5, δ=0.05), enabling reproducibility of the training setup.

- **The core motivation—using self-supervised contrastive learning to exploit multi-view KG information—is timely and well-grounded.** The paper identifies a genuine limitation of prior KG-aware methods (reliance on sparse supervised signals) and proposes contrastive learning across views as a reasonable remedy.

## Weaknesses

### Fatal
None.

### Major

1. **The "state-of-the-art" claim is unsubstantiated due to outdated baselines.** The paper compares against methods from 2009–2021 (BPR-MF, CKE, RippleNet, MKR, KTUP, KGCN, KGNN-LS, KGAT, KGIN). Multiple strong KG-aware contrastive recommendation methods from 2022–2025 (e.g., KGCL, SimGCL, SGL, NCL) are absent. Since the paper's central claim is "superior performance compared to state-of-the-art methods" (abstract) and the method itself is a contrastive learning approach, the omission of contemporary contrastive KG recommenders means the SOTA claim is unsupported. The comparison establishes superiority over older methods but cannot be said to represent the current frontier.

2. **No ablation study of any kind.** The framework combines contrastive loss (local + global), feature alignment, field uniformity, noise injection, and three separate view encoders. Without any ablation experiment, it is impossible to determine which components drive the reported improvements. The gains could stem from hyperparameter tuning on small datasets, the multi-view design, the noise, the alignment/uniformity constraints, or any combination thereof. This is the most critical empirical gap.

3. **Statistical significance and variance are completely absent.** All results in Table 2 are single-point estimates with no standard deviations, confidence intervals, or significance tests. On small datasets (ML-100k: 943 users, 1682 items after filtering), random seed and data split variance can be substantial. Without variance reporting, the claimed 8.9% and 11.6% improvements cannot be evaluated for statistical reliability.

4. **The noise injection mechanism is critically underspecified.** The paper states "we adopt a matrix-wise perturbation technique" and "addition of random noise to the generated user and item embeddings" (Sections 4.1, 4.1.1), citing SimGCL and NoisyTune. However, it never defines: (a) the noise distribution (uniform? Gaussian?), (b) the noise scale or how it is set, (c) whether noise is applied to parameters, embeddings, or both, or (d) whether it is applied per-layer or globally. A reader cannot replicate or evaluate this component, despite it being a headline contribution ("noisy" appears in the paper's title and abstract).

5. **The "field" concept for alignment and uniformity constraints is defined on metadata that does not exist for these datasets.** The paper defines fields as "genre, director, or actor in datasets like MovieLens" (Section 4.3). However, MovieLens-100k and 1M contain only genre information — no director or actor metadata. The alignment loss therefore pairs all movies sharing a genre as "positive," ignoring multi-genre assignments and the coarseness of genre as a signal. The uniformity loss pushes apart movies of different genres, which is arbitrary for recommendation. The paper presents no analysis of whether these constraints actually benefit representation quality.

### Minor

1. **Only two datasets, both MovieLens (small-scale).** ML-100k and ML-1M are the only evaluation datasets. Both are small, from the same domain (movies), and filtered via 10-core. This limits generalizability claims. Results on at least one larger, non-movie dataset (e.g., Amazon Books, Yelp) would strengthen the evaluation.

2. **Only K=20 is reported.** Results for K=5, 10, 50 are not provided, making it unclear whether NMCLK's advantage holds across different recommendation list lengths.

3. **The k value for the semantic view's k-NN graph is not specified.** Section 4.1.2 introduces "a k-Nearest-Neighbor item-item semantic graph" but never states the value of k used in experiments.

4. **Conclusion introduces "textual and visual aspects" never described in the method.** Section 6 states "the framework utilizes a contrastive learning module to merge item representations from multiple views, including textual and visual aspects," but the method section (Section 4) contains no textual or visual modality processing. This appears to be a writing error where conclusion language exceeds the actual scope.

5. **The structural view encoder (Section 4.1.3) uses GAT-style attention on entity nodes but does not explicitly model relation types in the KG.** Despite the KG motivation emphasizing heterogeneous relations, the structural encoder aggregates neighbors without distinguishing edge types, which is inconsistent with the paper's stated goal of leveraging KG relational information.

6. **The claim that "low-frequency and high-frequency features have equal chances" in alignment/uniformity constraints (Section 4.3.2) is stated without any supporting analysis.** No frequency analysis, ablation, or evidence is provided.

### Trivial
None.

## Nice-to-Haves

- Results on large-scale datasets (Amazon Books, Yelp2018) would strengthen generalizability claims.
- Ablation of the noise mechanism with varying noise levels and analysis of robustness under test-time perturbation.
- t-SNE/UMAP visualizations of learned embeddings to illustrate the effect of the alignment and uniformity constraints.
- Convergence curves of the different loss components to show training stability.
- Reporting results at K=5, 10, 50 in addition to K=20.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Reference [32] is not in the visible text"** — The paper cites existing work (projection/rotation operators) which is standard practice. This is not a weakness.
- **"KGAT mischaracterized as supervised learning"** — KGAT's primary loss is BPR (a supervised ranking loss); the characterization is not incorrect.
- **"Notation sloppiness (sim in Eq. 12)"** — This is a formatting/parser artifact, not an author error.
- **"Baselines may be undertuned"** — Using hyperparameters from original papers is standard practice; speculating about undertuning without evidence is not a valid criticism.
- **"CTR experiments not in main paper"** — The paper states these are in supplementary material, which is acceptable.
- **"Missing appendix/proofs/references"** — These may be in the original submission but stripped by the parser.

## Novel Insights

None beyond the paper's own contributions. The reviews identify genuine empirical gaps but do not contribute new analytical insights about the method or problem beyond what the paper already articulates.

## Suggestions

1. **Add contemporary baselines** — At minimum, include KGCL (2022), SimGCL (2022), SGL (2021), and one 2023–2024 method to support the SOTA claim.
2. **Perform ablations** — Systematically remove each view, remove noise, remove alignment/uniformity constraints, and replace the contrastive loss to isolate the source of improvements.
3. **Specify the noise mechanism precisely** — Provide equations for the noise distribution, scale parameter, and exact application point (embeddings vs. parameters, per-layer vs. global).
4. **Report standard deviations over multiple random seeds** (at least 5 runs) to establish statistical significance.
5. **Clarify the field definition** — Acknowledge that only genre metadata is available for MovieLens, justify why genre-level alignment/uniformity is meaningful, or adapt the method to use available metadata.
6. **Add results on at least one larger, non-movie dataset** to demonstrate generalizability.

## Score and Decision

The paper presents a reasonable high-level architecture (three-view contrastive learning for KG-aware recommendation) and reports strong gains on familiar benchmarks. However, the evaluation has critical gaps: the SOTA claim rests on outdated baselines, no ablation isolates the contribution of any component, statistical reliability is unexamined, and the headline "noisy" mechanism is left underspecified to the point of irreproducibility. The core conceptual contribution (multi-view contrastive learning with alignment/uniformity) is interesting, but the empirical demonstration is insufficient to support the paper's claims in its current form. A major revision addressing these weaknesses would be needed before the contribution can be properly evaluated.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>