- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper introduces VoxCap, a voxel-captioning model that generates SMILES strings from voxelised pharmacophore-shape profiles (3D CNN encoder + LSTM decoder). The authors propose two workflows: (1) de-novo design, generating molecules with high pharmacophore-shape similarity to a query, and (2) fast library search, where generated molecules are mapped to 2D analogs in a database to approximate 3D similarity search at dramatically reduced cost. The core practical contribution is the fast search workflow, which reduces the number of expensive 3D overlay comparisons from full database size to O(n_g × n_a).

## Strengths

- **Practical fast-search workflow with clear efficiency gains.** The method reduces 3D comparisons from database size (e.g., 240k compounds) to ~500 ROCS evaluations per query—a >99.8% reduction—while still returning at least one hit per query molecule (Table 3, Section 4.2). The paper correctly identifies that this makes previously intractable searches (e.g., against Enamine Real's 60B compounds) feasible.

- **Well-defined benchmark for pharmacophore-conditioned generation.** The paper establishes a concrete task with clear hit criteria (TC ≥ 1.2, following Grebner et al.), multiple metrics (hits, unique scaffold hits, max TC, queries with hits), and uses two standard datasets (GEOM-drugs, ChEMBL/GuacaMol) with established splits (Section 4.1). This provides a reproducible evaluation framework.

- **Honest analysis of limitations.** The paper proactively identifies and analyzes why hits are lower than brute-force (low 2D similarity of generated molecules with median top-1 Morgan similarity 0.38, duplicate database mappings, early stopping issues) and suggests concrete future directions (Section 4.2). This transparency is valuable.

- **Justified voxel grid parameters.** Grid sizes (48³ for GEOM-drugs, 64³ for ChEMBL at 0.35 Å resolution) are chosen to cover >99.8% of atom positions (Section 4.1), providing a principled basis for the input representation.

## Weaknesses

### Fatal

None.

### Major

- **The PGMG comparison is misleading and overclaimed.** VoxCap receives both pharmacophore features (6 channels) and a shape channel (Gaussian densities at atomic positions), while PGMG conditions on a pharmacophore *point cloud* with *no shape information whatsoever*. The primary evaluation metric, Tanimoto Combo (TC), is a weighted combination of shape overlap and pharmacophore overlap—so shape contributes heavily to the score. The paper's headline claim that VoxCap "significantly outperforms" PGMG "by up to an order of magnitude" (abstract, Section 5) is therefore not a fair comparison. It demonstrates that *shape information helps on a shape-aware metric*, but the paper presents it as a method-level victory without acknowledging the input-modality mismatch. This undercuts the central de-novo performance claim. (See Section 3, lines 47-48 for VoxCap's shape channel; Section 4.1, line 112 for PGMG's pharmacophore-only point cloud input.)

### Minor

- **De-novo evaluation does not assess drug-discovery relevance.** The paper motivates the fast-search workflow by noting that library molecules are preferable because they are synthetically accessible and purchasable, while de-novo molecules are often not. Yet the de-novo evaluation measures only TC scores against the query—no assessment of synthetic accessibility, drug-likeness, or any property relevant to experimental follow-up is performed. This creates a gap between the stated motivation and the evidence provided for the de-novo workflow's utility (Section 4.1).

- **Fast search evaluation uses only 11 query molecules.** The fast search results (Table 3) are based on medians across 11 query molecules. With such a small sample, it is impossible to assess whether the reported values are stable or driven by outliers. No interquartile ranges or distributions are reported. This limits the statistical confidence in the fast search claims (Section 4.2, line 136).

- **Missing reproducibility details.** The paper does not report training hyperparameters (learning rate, batch size, optimizer, number of epochs to early stopping, GPU type, training time). The early stopping criterion is mentioned but not specified concretely ("a checkpoint after only a few epochs of training," line 142). These are standard experimental details needed for reproducibility.

- **No direct comparison against other voxel-based methods.** Skalic et al. (2019) is cited as a previous voxel-to-SMILES method but is not included as a baseline. While evaluation paradigms differ (Skalic et al. uses distributional metrics rather than per-query TC scores), the paper's claim that VoxCap improves over voxel-based approaches would be strengthened by acknowledging or addressing this gap (Related Work, Section 2.2).

- **No statistical confidence measures.** All results are reported as medians without standard deviations, interquartile ranges, or confidence intervals, making it difficult to assess the spread of performance across query molecules (Tables 1 and 3).

### Trivial

None.

## Nice-to-Haves

- A dedicated limitations section gathering the issues currently scattered across Section 4.2 (early stopping, low 2D similarity, duplicate mappings) would improve readability.
- Including SA Score or another simple synthesizability measure for a sample of generated hits would bridge the gap between the de-novo motivation and evaluation.
- The fast search evaluation could be extended to a larger query set (e.g., 100+ molecules) to verify that the 11-query results are representative.

## Removed Points

The following weaknesses from the input reviews are removed and should be treated with caution:

1. **"The table shows Medians of 848 vs. 11228, which are absolute hits, not hits in the top-500"** — The paper text (line 136) clearly states the comparison is with "the set of top 500 molecules by ROCS score from the brute force approach," not the full brute force. The numbers cited are consistent with hits found within that top-500 set. This appears to be a misreading of the paper's stated protocol.

2. **"PGMG is not a fair comparison at all" framed as fatal/invalidating** — While this is a real problem (retained as Major above), it does not invalidate the paper entirely. The fast-search workflow is independently evaluated against brute-force search on the same database—not against PGMG—and stands as a separate contribution. The PGMG comparison primarily affects the de-novo generation framing.

3. **Architecture criticism (3D CNN + LSTM is standard, no comparison to cross-attention)** — The paper does not claim architectural novelty; the contribution is in the workflow design and evaluation. Whether to use cross-attention vs. concatenation is a design choice, not a flaw in the presented method.

4. **Scaling issue attribution in introduction** — The paper lists both conformer generation and alignment/comparison as steps (lines 12-13), and correctly identifies alignment/comparison as the bottleneck *post-conformer generation*. There is no factual error here.

5. **Strength: "VoxCap outperforms prior pharmacophore-based generative models by a large margin"** — This conflicts with the verified weakness about the unfair PGMG comparison and is removed per the rule that when a strength and weakness disagree, the weakness wins.

6. **Generic strengths from Strength Finder** — General statements about the problem being "important" or the paper "addressing a relevant question" are removed as unspecific.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the familiar challenge of evaluating generative models in drug discovery—namely, that standard metrics (TC score) can conflate input representation advantages with genuine generative quality—but this observation is implicit in the paper's framing rather than a new insight from the reviews.

## Suggestions

1. **Re-frame the PGMG comparison transparently.** Acknowledge explicitly that PGMG conditions only on pharmacophore features (no shape) and that the TC metric rewards shape overlap. Position the comparison as demonstrating the *value of adding shape information* rather than as a method-level win. Alternatively, present PGMG as a "pharmacophore-only" baseline and add a separate comparison against a voxel-based baseline (e.g., Skalic et al.) on the same evaluation protocol.

2. **Add synthetic accessibility assessment to de-novo evaluation.** Even a simple SA Score or retrosynthetic feasibility analysis on a sample of generated hits would directly address the paper's stated motivation.

3. **Scale up the fast search evaluation.** Run on ≥100 query molecules and report distributions (e.g., box plots, IQRs) rather than only medians. This would substantially strengthen the statistical grounding of the main practical claim.

4. **Report training hyperparameters and the exact early stopping criterion.** These are essential for reproducibility and straightforward to provide.

5. **Add statistical confidence measures (standard deviations, percentiles) to all result tables.**

6. **Clarify Table 3 column definitions** so that the comparison (VoxCap hits vs. top-500 brute-force hits) is unambiguous.
