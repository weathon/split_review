- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

GraphProp proposes a two-phase method for training Graph Foundation Models (GFMs) for graph-level classification. Phase 1 trains a structural GFM by supervised regression of 15 polynomial-time graph properties (e.g., fractional chromatic number, Lovász number) from an invertible positional encoding of the adjacency matrix. Phase 2 uses the structural GFM's representations as positional encodings to augment in-context learning with LLM-derived node features, yielding a comprehensive GFM. The central thesis is that graph structures carry more cross-domain consistent information than node features, so explicitly learning structural representations via property prediction enables better cross-domain generalization — particularly on graphs without node features.

## Strengths

- **Clear and substantial empirical gains on graphs without node features (Section 5.2, Table 3, Figure 3a).** On the G₂ group (COLLAB, IMDB-B, DD, REDDIT-B, REDDIT-M5K), GraphProp outperforms OFA by ~10–15% average improvement. This directly supports the claim that the structural GFM captures transferable topological information independent of node features, and it is the paper's strongest piece of evidence.

- **Principled two-phase design that decouples structural and feature generalization (Sections 3.2–3.3).** Training a structural GFM via property prediction (using only the adjacency matrix) and then injecting its representations as positional encodings into an in-context learning pipeline is a clean conceptual framework. It cleanly separates the structural and node-feature learning objectives.

- **Invertible positional encoding insight (Definition 2.1, Section 3.2).** The paper identifies that common spectral embeddings (eigenvectors of the Laplacian) are non-invertible and therefore lose information needed for property prediction, and proposes the invertible encoding **B** = **U****Λ**^(1/2). This is a concrete technical contribution that distinguishes GraphProp from prior graph transformers.

- **Leveraging graph theory for GFM training (Section 2.2, Section 3.4).** Using a diverse set of 15 graph properties from established graph theory (including fractional chromatic number and Lovász number) is a novel way to supervise structural learning, and the ability to train on unlabeled and synthetic graphs (because properties can be computed algorithmically) addresses a real data-scarcity bottleneck.

## Weaknesses

### Fatal
None.

### Major

- **The central motivational claim (cross-domain correlations are higher for structure than for features) rests on visual inspection of heatmaps without any numerical summary or statistical test (Section 3.1, Figure 1).** The paper states "We observed that the cross-domain correlation of **C** is higher than that of **Ē**" but provides no mean cross-domain correlation coefficients, no standard deviations, and no significance test. Figure 1's color maps are not explained in the caption (readers cannot tell what light vs. dark means), and the eight datasets used are not listed. Given that this claim is presented as the paper's key motivation ("the importance of focusing on graph structures in GFM training"), the lack of quantitative support weakens the paper's foundation. The authors should report numeric values (e.g., average off-diagonal block correlation for each matrix) and a simple statistical test. This is fixable but currently under-evidenced.

### Minor

- **The contribution of the structural GFM over simply using pre-computed property values as fixed features is not isolated in the main text.** A natural baseline would be: skip the structural GFM, compute the 15 graph properties directly, and feed them as features (concatenated with LLM representations) into the comprehensive GFM. The paper references an ablation study in the appendix (Section 5.4), but this specific comparison — learned structural representations vs. raw property values — is the critical test of whether the structural GFM training adds value beyond using properties as input features. Including this comparison in the main text would substantially strengthen the paper.

- **The baseline set is somewhat narrow for a cross-domain GFM paper.** The main comparisons are against OFA (the core baseline) and basic GNNs (GCN, Graph Transformer). The paper would be stronger by including at least one additional competitive baseline: (a) handcrafted structural features (e.g., degree statistics, clustering coefficients, spectral embeddings) fed directly into a classifier on G₂, and (b) a contrastive pre-training method (e.g., InfoGraph), which the paper mentions comparing in the appendix but does not report in the main tables. The results against OFA are convincing for G₂ but more baselines would solidify the claim.

- **The evaluation metric is not stated in the main results tables (Tables 2, 3).** The tables have captions like "Results ..." without specifying accuracy, AUROC, F1, or any other metric. The reader must infer it from context. This should be corrected.

### Trivial

- The list of 15 graph properties used (referenced as Table 4) is not reproduced in the main paper body, making it harder for a reader to understand what the structural GFM predicts without searching the appendix.
- The data augmentation method (mixup of adjacency matrices) is described in Section 3.2 but never evaluated in the main experiments; the paper references appendix experiments, but the main text gives no summary of whether augmentation helps.

## Nice-to-Haves

- Empirically compare invertible vs. non-invertible positional encodings (e.g., spectral embedding vs. **B** = **U****Λ**^(1/2)) for property prediction accuracy. The paper gives a theoretical argument but no experiment.
- Justify the concatenation fusion (**x̂**ᵢ = **e**ᵢ ⊕ **z**ᵢ) over alternatives (sum, cross-attention).
- Report variability (error bars or confidence intervals) in the few-shot learning plots (Figure 3b, 3c) rather than averages only.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Criticism that the appendix is stripped and the paper cannot be fully evaluated.** Per the review guidelines, appendix content is stripped by the PDF parser; the original submission contains it. The paper references ablation studies, InfoGraph comparisons, and augmentation experiments in the appendix, and these should be assumed to exist.

2. **Suggestion to benchmark GraphQA-style reasoning models.** GraphQA is designed for graph question-answering, not graph classification — the paper's task. This comparison would be a new task setting, not a missing baseline for the paper's claimed contribution.

3. **Complaint that data augmentation (mixup, synthetic graphs) is not used in main experiments.** The paper refers to augmentation experiments in the appendix (Section 5.4, item 3). Since the appendix is stripped, the presence or absence of these experiments cannot be verified from the text available.

4. **Strength claiming the correlation analysis is "quantitative motivation."** This strength (from the Strength Finder) conflicts with the verified weakness that the analysis lacks numerical summary statistics and statistical tests. Per the merging rules, when a strength and weakness conflict, the weakness wins. The correlation analysis is qualitatively suggestive but not quantitatively rigorous as presented.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a succinct numerical summary to Section 3.1: report mean off-diagonal block correlation for **C** vs. **Ē** (with standard errors) and a simple statistical test (e.g., paired t-test or permutation test). This directly validates the paper's central motivation and is inexpensive to add.

2. Include a main-text ablation that compares GraphProp against a variant that uses pre-computed graph properties as fixed input features (skipping the structural GFM). This isolates whether the structural GFM training provides additional benefit beyond using properties as raw features. Even a one-paragraph summary with one table row would substantially strengthen the contribution claim.

3. Add error bars or confidence bands to the few-shot learning plots (Figure 3b, 3c) to show variability across the 10 runs mentioned in Section 5.3.

4. Clearly state the evaluation metric (accuracy, AUROC, or F1) in every table caption.

The paper presents a well-motivated method with clean empirical evidence for its main claim (structural generalization helps, especially without node features). The core weaknesses are in the rigor of the motivational evidence and the isolation of the key design choice (learned vs. raw property representations). Both are addressable without changing the method.
