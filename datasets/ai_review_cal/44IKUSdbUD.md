- Decision: Reject
- Avg Score: 3.00
- Scores: 5, 3, 1
Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the consolidated review.

## Summary

This paper addresses the computational bottleneck of using large Transformer models for gene-gene interaction discovery on massive single-cell transcriptomic datasets. The authors propose CelluFormer, a permutation-invariant Transformer, and use its attention maps to infer gene-gene interactions. To reduce the cost of passing millions of cells through the model, they introduce a Weighted Diversified Sampling (WDS) algorithm that estimates each cell's minmax kernel density via 0-bit consistent weighted sampling (CWS) in two linear passes, then uses the inverse density as a sampling probability. Experiments on the SEA-AD Alzheimer's dataset across 8 neuronal cell-type datasets show that WDS at 1% sampling substantially outperforms uniform sampling and yields NES scores close to the full-dataset baseline.

## Strengths

1. **Efficient two-pass algorithm with theoretical grounding.** Algorithm 1 estimates the minmax density for every cell in O(n·nnz(X)) time with O(RB) memory independent of dataset size, avoiding the prohibitive O(n²·nnz(X)) pairwise computation. Theorem 1 proves the estimator is unbiased for the minmax kernel density, and the hash-based approach via 0-bit CWS is a principled application of known randomized methods to this domain.

2. **WDS consistently and substantially outperforms uniform sampling across all cell types and sample sizes.** In Table 4 (Sampling_Res), WDS at 1% achieves mean NES scores far closer to the full-dataset baseline than uniform sampling at any fraction up to 10%. For example, L6_CT: WDS at 1% NES=1.19 vs. uniform at 10% NES=0.91; L6b: WDS at 1% NES=1.17 vs. uniform at 10% NES=1.20. The MSE values for WDS are consistently lower by an order of magnitude or more. This provides clear evidence that diversity-aware sampling is significantly more data-efficient than naive uniform sampling for this task.

3. **Principled diversity formulation.** The paper formalizes cell diversity as inverse minmax kernel density (Definition 4), connects it to established randomized hashing methods (0-bit CWS), and provides an unbiased estimator (Theorem 1). This gives the sampling strategy a clear theoretical foundation rather than relying on ad-hoc heuristics.

4. **Reasonably broad evaluation across cell types and baselines.** The RQ1 experiments compare CelluFormer against three statistical baselines (Pearson, Spearman, CS-CORE), NID, and two foundation models (scGPT, scFoundation) across 8 datasets. CelluFormer wins on 4 of 8 datasets (ties or comes close on others), and Transformer-based methods generally outperform the statistical baselines.

## Weaknesses

### Fatal
None.

### Major

1. **The claim that 1% sampling achieves performance "comparable to" the full dataset is overstated for at least a subset of cell types.** Comparing Table 3 (full-dataset NES for CelluFormer) with Table 4 (1% WDS NES):
   - L5_ET: full = 1.15, 1% WDS = 0.95 (drop of 0.20)
   - Pax6: full = 1.25, 1% WDS = 1.08 (drop of 0.17)
   - L5_6_NP: full = 1.21, 1% WDS = 1.13 (drop of 0.08)
   
   These are non-trivial drops. While other cell types (L6_CT, L6b, L6_IT_Car3) indeed show near-identical scores, the paper's blanket assertion of "comparable performance" across the board is not uniformly supported. The claim should be qualified by cell type and accompanied by a principled criterion for "comparable" (e.g., within a confidence interval or effect size threshold).

2. **The decision to average attention maps across all layers and heads is stated without justification or analysis.** The paper simply takes "the average attention maps of all layers and all heads" (Section 2.3, page 5) without discussing whether different layers/heads capture different interaction patterns, whether averaging is appropriate, or whether the attention maps are stable across runs. Given that the entire downstream pipeline rests on the quality of these aggregated attention maps, some analysis of layer/head importance, variance across runs, or comparison to random attention would significantly strengthen the work.

3. **The WDS estimator involves a sampling-without-replacement procedure paired with importance weights designed for sampling with replacement, creating an unresolved technical inconsistency.** The text states "we perform sampling without replacement" (Definition 4) but Definition 5 uses an importance-weighted estimator $\tilde{Z}(v_i,v_j) = \frac{\sum_{x\in X_s} Z_x(v_i,v_j) \cdot \mathcal{I}(x)}{\sum_{x\in X_s} \mathcal{I}(x)}$ whose unbiasedness properties rely on sampling with replacement. The paper does not address how sampling without replacement interacts with the weighting scheme or whether the variance expression in Definition 5 remains valid.

### Minor

4. **The NES-based evaluation metric is described too tersely for the results to be fully interpretable.** The paper states: "we utilized the Kolmogorov-Smirnov test, which was facilitated by the GSEApy package. We select normalized enrichment score (NES) as our evaluation metric." It does not explain how a ranked list of *gene pairs* is mapped to GSEA's gene-set enrichment framework — e.g., what constitutes a "gene set" in this context, what the background ranking is, and how the BioGRID interaction pairs are mapped to the ranked list. While a knowledgeable reader can infer the setup, the paper should make this explicit for reproducibility.

5. **Table 4 reports only mean NES/MSE over five runs without any variability measure.** Five replicates is sufficient to report standard deviations, standard errors, or bootstrapped confidence intervals. Without these, the reader cannot assess whether the observed differences between WDS and uniform sampling, or between 1% and 2% WDS, are statistically meaningful.

6. **The fine-tuning procedure for foundation models (scGPT, scFoundation) is not specified.** The paper attributes foundation models' underperformance to "overfitting to pretrained knowledge" and "data distribution mismatch," but does not report what fine-tuning configuration was used (learning rate, epochs, data split, whether full fine-tuning or parameter-efficient). If the fine-tuning was suboptimal, the comparison may be unfair.

7. **The paper does not ablate components of the WDS algorithm.** It is unclear whether inverse density sampling is essential, or whether simpler diversity metrics (e.g., based on Euclidean distance, random centroids, or sampling proportional to density rather than inverse density) would perform similarly. Without such ablations, it is difficult to attribute the gains to the specific minmax+CWS formulation versus the general principle of diversity-aware sampling.

### Trivial
None of consequence.

## Nice-to-Haves

- Add a direct comparison table showing full-dataset NES alongside 1% WDS NES side-by-side for each cell type.
- Include an analysis or sanity check showing that attention maps from the disease classifier rank known AD-related gene pairs above random expectation (the NES values already provide this implicitly, but an explicit verification would strengthen confidence in the pipeline).
- Discuss the variance and concentration properties of the density estimator when R = O(log|X|) is small.

## Removed Points

These points from the input reviews are removed (with brief justification):

- **"The evaluation metric (NES) is used in a way that is not clearly explained, making the central results uninterpretable"** (Harsh Critic #1, fatal framing). Overstated. The description is brief but functional — the setup (ranked gene pairs against BioGRID/DisGenet ground truth via GSEApy) is standard and interpretable. The softened version is kept as Minor weakness #4 above.

- **"No discussion of why averaging across all layers and heads is appropriate"** was moved from fatal framing to Major weakness #2. It is a methodological gap but not "fatal" — the evaluation against ground truth provides indirect validation that the aggregated attention maps are meaningful.

- **"The Transformer-based gene-gene interaction discovery pipeline lacks validation"** (Harsh Critic #3, fatal framing). The entire RQ1 evaluation (Table 3) is a validation: CelluFormer's attention-based rankings achieve positive NES against BioGRID/DisGenet, establishing that the pipeline captures known AD-related interactions beyond chance. The stronger specific point about layer/head averaging (kept above) is the real weakness, not a lack of validation.

- **"Theorem 1 novelty is minimal"** (Harsh Critic, Section 3). The reviewer's substantive point is correct but framed as a weakness of a claimed contribution. The paper presents this as an efficient estimator, not a novel theoretical result. This is better treated as a scope observation than a weakness.

- **"The paper does not specify how foundation models were fine-tuned (learning rate, epochs)"** kept as Minor #6 rather than fatal.

- **"Model architecture details (layers, heads, embedding dimension) missing"** — these may reside in supplementary material (the paper references supplementary for Theorem 1's proof). The hard rules instruct removing criticisms about missing appendix content. Also softened since the architectural framing (permutation-invariant Transformer with padding mask) is described conceptually.

- **"Full-dataset NES values are not shown in Table 4"** — they are in Table 3. The side-by-side comparison would be convenient but the data is present and cross-referencing two tables is standard practice.

- **"Smaller samples sometimes outperforming larger samples undermines the core claim"** — The paper acknowledges this observation and provides a reasonable explanation (noise, limited interpretability). It does not undermine the core claim; rather, it honestly reports an interesting pattern.

- **All pure formatting/style nitpicks and grammar criticisms** removed per hard rules.

- **Several generic strengths from the Strength Finder** (e.g., "this paper addressed an important problem") removed as generic.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful suggestions for strengthening the evaluation but do not identify fundamentally new observations about the paper's approach or results that are absent from the paper itself.

## Suggestions

1. Add a direct comparison table showing full-dataset NES alongside the 1% and 2% WDS NES for each cell type, with a clear statement of which cell types support the "comparable performance" claim and which show meaningful degradation.
2. Reconcile the sampling-without-replacement statement with the importance-weighted estimator, or clarify that sampling is performed with replacement.
3. Add standard deviations (or confidence intervals) to Table 4.
4. Include a brief justification or ablation for the decision to average attention across all layers/heads — e.g., compare individual layers, or show that the aggregated ranking correlates better with ground truth than any single layer.
5. Report the fine-tuning configuration used for scGPT and scFoundation.
