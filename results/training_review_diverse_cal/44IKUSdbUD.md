I have thoroughly verified each reviewer claim against the paper. Here is my consolidated review.

---

## Summary

This paper tackles gene-gene interaction discovery from single-cell transcriptomic data using a Transformer model (CelluFormer) whose attention maps serve as indicators of gene-pair interactions. The main methodological contribution is a weighted diversified sampling (WDS) algorithm that, in two linear passes over the dataset, estimates the minmax kernel density of each cell via 0-bit consistent weighted hashing and uses its inverse as a sampling probability to select diverse, representative subsets. Experiments on the SEA-AD Alzheimer's dataset show that WDS at 1% sampling achieves notably higher NES scores than uniform sampling across multiple cell types, though the claim of "comparable" performance to the full dataset is only partially supported.

## Strengths

- **Novel two-pass minmax density estimation algorithm.** Algorithm 1 is a clean, theoretically grounded method for computing diversity scores without pairwise comparisons. It runs in O(n·nnz(X)) time with O(RB) memory (constant w.r.t. dataset size), making it genuinely scalable. The connection to 0-bit CWS hashing and the informal Theorem 1 provide a principled foundation.

- **WDS substantially outperforms uniform sampling at low sample rates.** Across 24 of 28 comparisons in Table 2, WDS achieves higher mean NES and lower MSE than uniform sampling. At 1% sampling, WDS closes the gap to the full-dataset NES to within 0.08 or less on 4 of 6 cell types, while uniform sampling lags by 0.20–0.36 points. This is a clear and practically meaningful improvement.

- **Evaluation on a large, realistic Alzheimer's dataset.** The SEA-AD dataset (1.24M cells, 36K genes) is a challenging real-world testbed. Results are reported across 7 distinct neuronal cell types plus the combined data, giving reasonable coverage.

- **The paper correctly identifies and formalizes an important bottleneck.** The data-ingestion challenge for attention-based interaction discovery (Section 3.1) is well articulated, and the WDS approach is a principled response grounded in locality-sensitive hashing and kernel density estimation.

## Weaknesses

### Fatal
None.

### Major

1. **The claim that 1% sampling achieves "performance comparable to that of utilizing the entire dataset" is overstated for several cell types.** The gaps between WDS at 1% and the full-dataset NES (from Table 1) are: L5_ET (0.95 vs 1.15, Δ=0.20), Pax6 (1.08 vs 1.25, Δ=0.17), L5_6_NP (1.13 vs 1.21, Δ=0.08), L6_IT_Car3 (1.20 vs 1.22, Δ=0.02), L6b (1.17 vs 1.13, Δ=-0.04), L6_CT (1.19 vs 1.18, Δ=-0.01). On a scale where most full NES values are 1.13–1.25, a Δ of 0.17–0.20 represents a ~14–16% relative shortfall — not "comparable" by a strict reading. The paper provides no statistical test or principled criterion for what "comparable" means, and does not report confidence intervals. The claim should be softened to reflect that WDS at 1% substantially outperforms uniform sampling but does not fully match the full dataset in all cases.

2. **"Since CelluFormer consistently outperformed other baselines" (line 281) is contradicted by the paper's own Table 1.** Table 1 shows that on individual cell types, at least one baseline achieves a higher NES than CelluFormer in 4 out of 7 cases: L5_ET (scGPT 1.23 > 1.15), L6_CT (NID 1.54 > 1.18), L5_6_NP (scGPT 1.50 > 1.21), L6b (scGPT 1.23 > 1.13). CelluFormer does win on the combined "All neuron data" row (1.17 vs next best 1.06), but the blanket claim of consistent outperformance is inaccurate. This undermines trust in the paper's rhetorical framing and is easily fixable by more precise language.

### Minor

3. **The evaluation metric pipeline is underspecified.** The paper states that it produces a ranking of *gene-gene pairs* from the accumulated attention maps, and uses NES from the GSEApy package with BioGRID (filtered to AD-relevant genes) as ground truth. However, NES traditionally operates on a ranked list of *genes* against a gene set. The paper never explicitly states whether (a) pair-level rankings are converted to gene-level ranks (e.g., by scoring each gene based on its incident interaction scores), or (b) GSEA is applied directly to the ranked list of gene pairs with BioGRID as a set of known-interacting pairs. While option (b) is a valid and natural extension, the paper should clarify the exact procedure so the results are fully reproducible.

4. **Missing combined multi-cell-type sampling experiment.** The paper's motivation (Section 2.3) emphasizes that Transformers benefit from training on diverse cell types, and the "All neuron data" row in Table 1 shows the full-pipeline performance on the combined dataset. Yet the sampling experiments in Table 2 test WDS only on individual cell types (using each cell type's own data as the full reference). The operational scenario of interest — subsampling from the combined multi-cell-type dataset — is not evaluated. Adding this would directly support the stated use case. (The individual cell-type experiments are still informative as controlled tests, but they do not fully address the claimed setting.)

5. **No comparison against other subset selection methods.** WDS is compared only against uniform sampling. While the paper states that "none of them requires preprocessing time exponential to the dataset size," there exist other efficient methods such as stratified sampling, coreset selection (e.g., k-center greedy, herding), or influence-function-based sampling that would provide a more informative baseline. Even a simple comparison against random sampling stratified by cell type would help isolate whether the gains come from diversity weighting specifically.

6. **Table 2 reports only mean NES and MSE across five repeats, without standard deviations or raw values.** Some MSE values are extremely small (e.g., 4.30e-05), which combined with NES values around 1.2 suggests near-zero variance — suspicious without more detail. Reporting standard deviations or showing the distribution of NES across repeats would clarify this.

7. **The self-similarity term in the minmax density estimator is not discussed.** In Algorithm 1, the first pass counts every cell in each hash bucket including the query cell itself. Thus w_q = 1 + Σ_{y≠q}(minmax(q,y)+o(1)) in expectation. The additive constant of 1 compresses the dynamic range of 1/w_q in the softmax sampling probability. For large datasets (millions of cells) this is negligible, but for smaller cell types it merits at least a note. The paper should either acknowledge this or analyze the effect.

### Trivial

- The paper defers model architecture details (layers, heads, embedding dimension, learning rate) to the supplementary, which appears to have been stripped by the PDF extraction. These should be in the main text or at minimum referenced clearly.

## Nice-to-Haves

- A rank-overlap analysis (e.g., Jaccard index of top-k gene pairs between the WDS-subset and full-dataset rankings) would directly quantify how well the subset recovers the full ranking, complementing the NES-based evaluation.
- A statistical test (e.g., permutation test on rank overlap) for the "comparable" claim would give a principled basis for accepting it.
- The self-similarity offset could be trivially corrected by subtracting 1 from w_x before computing 1/w_x, which the authors may wish to note.

## Removed Points

The following criticisms from the original reviews were removed after verification:

- **"The evaluation metric is inadequately described, making the experimental results uninterpretable."** — Removed as overstatement. The paper describes ranking gene-gene pairs and using NES with BioGRID as ground truth. The specific concern about "gene-level conversion" assumes NES requires gene-level rankings, which is incorrect; GSEA can operate on any ranked list against a reference set of matching items. The evaluation is interpretable, though the description could be more explicit.
- **"Theorem 1 informal version should note the o(1) factor bias."** — Removed: the theorem already includes the o(1) term explicitly ("minmax(x,q)+o(1)"). The critic misread.
- **"CelluFormer architecture description is sparse (no layers/heads/embedding dim)."** — Removed per hard rule: these details were in the supplementary material, which was stripped by the PDF parser.
- **"Time complexity should be clarified."** — Removed: the paper states O(n·nnz(X)) which is correct and standard for hash-based methods; the critic accepts it is "plausible."
- **Missing related works.** — Removed per hard rule: I cannot verify existence of missing citations without external sources.

## Novel Insights

The reviewers' comments surface an interesting tension: the WDS algorithm is genuinely elegant and its gains over uniform sampling are clear, yet the paper's presentation makes the core result (1% achieving "comparable" performance) seem stronger than the data warrant. This is a framing problem, not a methodological one. The paper would be substantially strengthened by (a) walking back the "comparable" language to a more precise claim about WDS being far better than uniform sampling and approaching full-dataset performance, (b) adding the combined-dataset experiment, and (c) clarifying the metric pipeline. The minmax hashing approach to diversity-guided sampling is a genuinely useful idea that deserves a clean presentation.

## Suggestions

1. **Clarify the evaluation metric.** Explicitly state: "We rank all ordered gene pairs (i,j) by their normalized attention score Z_{ij}/M_{ij}. We then use GSEApy to compute the NES of this ranked list against the reference set of known-interacting gene pairs from BioGRID (filtered to AD-relevant genes from DisGeNET)."

2. **Add the combined multi-cell-type sampling experiment.** Run the same WDS vs. uniform sampling comparison (1%, 2%, 5%, 10%) on the "all neuron data" and report NES against the full-dataset ground truth from the "All neuron data" row of Table 1. This directly tests the claimed use case.

3. **Softening of claims.** Replace "comparable to that of utilizing the entire dataset" with "approaching the performance of the full dataset while using only 1% of cells" or similar. Replace "CelluFormer consistently outperformed other baselines" with "CelluFormer achieved the best or near-best NES on most datasets, particularly on the combined all-neuron data."

4. **Add standard deviations to Table 2** or visualize the five repeat NES values to help assess variability and support the very low MSE values reported.

5. **Acknowledge the self-similarity term** in Algorithm 1 briefly and explain why it is negligible for the dataset sizes used (or propose a correction if it is not).

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>