Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes NMCLK, a noisy multi-view contrastive learning framework for top-K recommendation with knowledge graphs. It generates three complementary views (collaborative, semantic, structural), applies local- and global-level cross-view contrastive learning, injects noise into parameters and embeddings, and adds alignment/uniformity constraints. Experiments on MovieLens-100k and MovieLens-1M show improvements over nine baselines (BPR-MF through KGIN, 2009–2021). The core architecture is coherent, but the evaluation is insufficient to support the claimed state-of-the-art status, key components are under-specified, and the contribution is obscured by a missing ablation study.

## Strengths

- **Multi-view contrastive learning framework with consistent empirical gains**: NMCLK outperforms all nine baselines on both datasets across all four metrics (NDCG, MRR, Hit, Recall). On ML-100k, NDCG@20 reaches 0.3485 — an 8.9% improvement over the strongest baseline KGAT. On ML-1M, NDCG@20 is 0.2313, ~11.6% better than KGCN. These results are reported in Table 2 and represent a non-trivial margin.

- **Thoughtful integration of multiple views for KG-aware recommendation**: The framework separately models collaborative signals (user-item graph via LightGCN), semantic item-item relations (KNN over KG embeddings), and global structural information (attention-based aggregation over the full user-item-entity graph). This tripartite design is a reasonable approach to capturing different facets of the data.

- **Introduction of alignment/uniformity constraints into KG-aware recommendation**: Adapting these constraints (borrowed from CV/NLP) to the recommendation setting is a sensible direction. The motivation — pulling features from the same field closer while pushing features from different fields apart — is conceptually clear.

## Weaknesses

### Fatal

None. The paper's core approach is coherent and does not contain a methodological error that invalidates its central claims. The weaknesses below are major but addressable.

### Major

1. **Outdated baselines relative to the paper's SOTA claim.** The newest baseline is KGIN (2021). The paper claims state-of-the-art performance but does not compare against any contrastive-learning-based KG recommendation methods that postdate these baselines. It even cites SimGCL (line 110) in its own architecture description yet does not include it — or any method from the post-2021 wave of contrastive KG recommendation — in the experimental comparison. For a paper submitted in 2026, this five-year gap in the baseline set fundamentally undermines the central SOTA claim. The contribution may still be valuable, but the paper cannot demonstrate it is competitive with contemporary work.

2. **Missing ablation study for a multi-component framework.** The framework has at least five distinct design elements: (a) three separate view encoders, (b) local-level contrastive loss, (c) global-level contrastive loss, (d) alignment/uniformity constraints, and (e) noise injection. Table 2 reports only final combined results. Without ablations, the reader cannot determine which components drive performance, whether any are redundant, whether the gains could be achieved by a simpler subset, or whether the noise injection and alignment/uniformity constraints (presented as key contributions) are actually responsible for the improvement. This makes the paper's contribution claims unverifiable.

3. **Under-specified operationalization of the alignment/uniformity constraints.** The paper defines "field" (e.g., genre, director, actor) and "feature" ("a specific instance of user interaction with items"), then writes losses \(\mathcal{L}_a\) and \(\mathcal{L}_u\) over sets \(E_f\) and embeddings \(\mathbf{e}_i\). However, it never specifies:
   - How \(E_f\) is constructed from the MovieLens KG data (e.g., is each genre value a distinct "feature"? How are multiple genre labels per item handled?).
   - Whether \(\mathbf{e}_i\) in these losses is an item embedding, a user embedding, or some separate learned feature embedding.
   - How user embeddings participate in \(\mathcal{L}_a\) and \(\mathcal{L}_u\) (users do not have explicit field-organized attributes like genre).
   
   Since these constraints are listed as a core contribution, this gap directly impacts reproducibility and prevents the reader from fully understanding or implementing the method.

4. **Narrow evaluation on small, homogeneous datasets.** The main paper evaluates only on MovieLens-100k (100k interactions) and MovieLens-1M (1M interactions) — both from the same domain (movie ratings), both small by modern standards, and both used in recommendation research for over a decade. For a paper claiming SOTA, the lack of evaluation on larger, more diverse datasets (e.g., Amazon subsets, Yelp, LastFM) is a significant limitation. The paper mentions CTR results in supplementary material, but the main results rely entirely on two small MovieLens variants, so generalizability to other domains and scales is unestablished.

### Minor

- **Noise injection strategy is described at a high level.** The paper states it uses "a matrix-wise perturbation technique" introducing "varied uniform noises to distinct parameter matrices, contingent on the standard deviations of the parameters" (lines 91–92) and also adds noise to embeddings (line 110). No precise formula, distribution parameters, or per-module application details are given. While the reference to Noisytune provides some guidance, the paper should be self-contained for a named component.

- **No hyperparameter sensitivity analysis.** Five hyperparameters (\(\alpha,\beta,\gamma,\delta,\lambda\)) control the loss weighting, but they are reported as fixed values with no analysis of how varying them affects performance. The claim that they were "meticulously chosen to ensure balanced contributions" (line 252) is unsupported.

- **The two-level contrastive design is not justified.** Local-level contrasts collaborative vs. semantic views; global-level contrasts the structural vs. combined local view. It is not explained why this specific pairing is chosen over, e.g., contrasting all pairs of views directly, or why users are excluded from the semantic view.

- **The claim about low-frequency features (line 232) is unsupported.** The paper asserts that the alignment/uniformity constraints "help to alleviate the suboptimal representation issue for low-frequency features" but provides no analysis or experiment to substantiate this.

- **KG construction statistics are missing.** The paper does not report the number of entities, relations, or triples in the KG for each dataset, nor how the KG was obtained (e.g., via Microsoft Satori as in KGAT).

### Trivial

- None beyond parser artifacts that are not author errors.

## Nice-to-Haves

- Standard deviations over multiple random seeds would strengthen the reliability of results, given the method's stochastic components (noise, dropout, negative sampling).
- Reporting training time relative to baselines would help assess the framework's practical cost.
- A discussion of the negative sampling strategy used for contrastive losses (e.g., uniform vs. in-batch, number of negatives) would aid reproducibility.

## Removed Points

These points were raised by reviewers but are removed or modified per the review guidelines; they are provided here for reference transparency:

- **"Missing comparison to MCCLK, KGCL, KGSSL"** — Per guidelines, the reviewer should not demand comparisons to methods whose existence cannot be independently verified. However, the general point about outdated baselines is retained and rephrased above (Major #1).
- **"Model-agnostic design" strength** (from Strength Finder) — The paper states NMCLK is model-agnostic but provides no experiment demonstrating it with a different backbone. This claim is asserted, not evidenced.
- **Reproducibility concerns framed as "fatal"** — The harsh critic characterized the under-specified alignment/uniformity (Major #3) and noise injection (Minor) as fatal/non-reproducible. These are real specification gaps but are not fatal; they are addressable with additional detail and do not invalidate the method's core concept.
- **"Fatal flaw" label on alignment/uniformity operationalization** — The critic called this fatal. It is a major gap but not fatal: the concept is understandable even if the implementation mapping is missing. This is a common specification issue in first submissions.
- **"The paper does not discuss the method" framing** — Minor.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not contribute structural insights that go beyond what the paper describes itself.

## Suggestions

1. **Update the baseline set.** Include at least three contrastive-learning-based KG recommendation methods (or best-available published results on ML-1M) to substantiate the SOTA claim. The five-year gap is the single most damaging weakness.

2. **Add a full ablation study.** Isolate the contribution of: each view individually, the noise perturbation, \(\mathcal{L}_a\), \(\mathcal{L}_u\), and each contrastive level. This is essential for a multi-component framework.

3. **Specify the alignment/uniformity constraints concretely.** Provide the exact procedure for constructing \(E_f\) from MovieLens attribute data, clarify whether \(\mathbf{e}_i\) are item embeddings, user embeddings, or separate learned feature embeddings, and explain whether/how users participate in these losses.

4. **Give the noise injection formula.** Provide the precise distribution, scaling rule, and application schedule (e.g., per-batch or per-epoch, which modules, training only).

5. **Evaluate on at least one larger, non-movie dataset** (e.g., Amazon Books, Yelp) to demonstrate generalizability.

6. **Conduct and report a hyperparameter sensitivity study** for the key loss-weighting parameters.

## Score and Decision

**Originality**: Moderate. The combination of multi-view contrastive learning with alignment/uniformity constraints and noise injection for KG-aware recommendation is novel in its specific configuration, though each component individually draws heavily from prior work.

**Quality of research question**: Important — improving KG-aware recommendation with self-supervised learning is a well-motivated direction.

**Claims supported**: Partially. The results on the two MovieLens datasets are positive, but the outdated baselines, missing ablation, and under-specified components prevent the SOTA claim from being fully substantiated.

**Soundness of experiments**: Below the acceptance bar. Main concerns: (a) baselines are 5+ years old; (b) no ablation; (c) evaluation on only two small datasets from one domain.

**Clarity**: Adequate for the high-level architecture but insufficient at the implementation level (noise injection, alignment/uniformity).

**Value**: The core idea has merit, but in its current form the paper does not provide enough evidence to convince the reader that NMCLK is competitive with contemporary approaches or that its specific design choices are what drive performance.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>