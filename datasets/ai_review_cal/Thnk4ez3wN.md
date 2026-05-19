- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5
Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper addresses tabular dataset distillation, an understudied area relative to image distillation. It proposes TDColER, a pipeline that learns column embeddings and an encoder–decoder to map heterogeneous tabular rows into a compact latent space, applies off-the-shelf distillation methods (k-means, agglomerative, KIP, GM) in that latent space, then decodes back. The paper also introduces TDBench, a large-scale benchmark evaluating 3 encoder architectures, 4 distillation schemes, 7 downstream classifiers, and 10 distillation sizes across 23 datasets, resulting in 226,200 distilled datasets and 541,980 model trainings. The results show that distilling in the learned latent space consistently improves downstream performance over vanilla distillation.

## Strengths

1. **Well-motivated approach adapted to tabular data's unique challenges.** The paper correctly identifies two key obstacles that prevent direct transfer of image distillation methods: feature heterogeneity (tabular features have diverse semantics, unlike homogeneous pixels) and model agnosticism (tabular downstream models are often non-differentiable). TDColER's latent-space distillation pipeline directly addresses both, and the results (Figures 3, 5) convincingly show that this pipeline boosts performance across diverse classifiers and distillation schemes.

2. **Exceptionally large-scale and systematic evaluation.** The benchmark spans 23 datasets, 7 model classes (including non-differentiable ones like XGBoost and KNN), 4 distillation schemes, and 10 IPC values — 226,200 distilled datasets and 541,980 model trainings. This breadth substantially exceeds prior distillation benchmarks (e.g., Cui et al. 2022) and provides strong empirical grounding for the reported findings.

3. **Concrete practical insights.** The paper goes beyond aggregate metrics to identify specific findings useful to practitioners: (i) k-means with TF\* (supervised fine-tuned transformer) is the strongest combination (Table 3, Figure 5); (ii) GNN encoders offer competitive performance with far fewer parameters (Figure 4); (iii) distilled data reaches 98.37% of full-data HPO performance at 21.84% of the runtime (Figure 6); (iv) clustering-based methods are particularly robust to class imbalance (Figure 7).

4. **Method-agnostic and modular framework.** The TDColER pipeline separates representation learning from distillation and downstream training, meaning it can incorporate future distillation methods without modification. The two-output design (latent-space or decoded original-space distilled data) gives users flexibility for privacy vs. interpretability.

## Weaknesses

### Fatal

None. The core claims (distilling in a learned latent space improves tabular data distillation) are supported by the evidence presented. No verifiable fatal error was identified.

### Major

1. **Ambiguous headline improvement statistic.** The abstract and Figure 2b state TDColER "boost[s] the distilled data quality ... by 0.5–143%" and a "performance increase from 0.5% to as large as 143%." The paper does not specify whether this is (a) absolute or relative improvement, and (b) improvement in balanced accuracy, relative regret, or some other quantity. Since the paper's main metric is relative regret (lower = better), the phrase "increase from 0.5% to 143%" is unclear. The specific improvements reported later (e.g., "44.96–108.79% improvement at IPC=10" for KNN, line 139) are described in context of relative regret comparisons, but the headline number in the abstract lacks this context. This makes the paper's central quantitative claim uninterpretable without digging into the details. The authors should explicitly define the metric, state whether the improvement is relative or absolute, and provide distributional statistics (median, quartiles, fraction of positive improvements).

2. **Missing ablation isolating the column-embedding contribution.** The paper argues that column embeddings are a key ingredient, but all encoder architectures (FFN, Transformer, GNN) operate on column embeddings. There is no comparison against a simpler baseline: a standard autoencoder trained on the raw preprocessed feature vectors (without column embeddings), followed by latent-space distillation. Without this control, the observed gains cannot be cleanly attributed to column embeddings specifically — they could come from any form of autoencoding (dimensionality reduction, denoising, or a better-structured latent space). Since the paper's framing emphasizes column embeddings as the mechanism, this ablation is important to validate the central motivation. (Verifiable from Section 2.1: all encoders receive column embedding matrices as input; no baseline without column embeddings is tested.)

### Minor

1. **Train/test split not explicitly described.** The evaluation metric (line 128) separately references "the full training set" and "the same test set," implying a standard train/test split exists. However, the paper never states the split ratio, the splitting strategy (e.g., stratified by class), or explicitly confirms that the test set is held out from *all* stages (autoencoder training, fine-tuning, distillation, and downstream model training). The equations (1) and (2) are written over the whole set *S*, and line 82 says "the whole original dataset." While standard practice strongly implies proper separation, the ambiguity should be resolved with an explicit statement. This does not invalidate the results but is a clarity gap.

2. **Results do not specify which k-means/agglomerative variant was used.** Section 3 describes both a synthetic variant (Euclidean cluster center) and a real-point variant (nearest real point) for k-means and agglomerative clustering. The results in Section 4 do not specify which variant was deployed in the reported experiments. Since the synthetic vs. real-point distinction has different implications (coreset selection vs. generative distillation), this should be clarified.

3. **Brief discussion section with no limitations.** Section 5 (lines 238–243) is a three-sentence summary. The paper does not discuss failure cases, datasets where TDColER underperforms vanilla distillation, sensitivity to hyperparameters, or computational overhead of the representation learning step. Adding a limitations paragraph would strengthen the paper's scientific rigor.

4. **GNN encoder architecture details not provided in main text.** The paper describes GNN at a high level (bipartite graph, message passing) but does not specify the number of layers, hidden dimensions, or activation functions. These may appear in the appendix (which was stripped by the parser), but the main text's claims about parameter efficiency (Figure 4) would benefit from minimal architectural details.

### Trivial

- The phrase "33.93.96.38%" on line 139 appears to contain a formatting error (likely "33.93–96.38%").
- Some figure references (e.g., to Figures 8, 9, 11, 12) point to appendix content that is not included in the main text, making some descriptions hard to follow without the full paper.

## Nice-to-Haves

- Per-dataset summary tables (e.g., relative regret for each dataset at IPC=10, averaged over classifiers) would help readers assess consistency across datasets, beyond the aggregate ranks and medians already reported.
- A systematic runtime breakdown (representation learning time + distillation time + downstream training time vs. full-data training time) would contextualize the computational trade-offs, which the paper cites as a core motivation.
- Confidence intervals or standard errors for the main relative regret comparisons would strengthen the statistical rigor, though the Wilcoxon signed-rank tests (Figure 5) already provide pairwise significance testing.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Data leakage as a "structural/fatal" issue.** The harsh critic claimed the paper "never states how the data is split" and that results could be invalid due to data leakage. However, the evaluation metric (line 128) clearly distinguishes "full training set" and "same test set," confirming a split exists. The equations (1) and (2) operating on *S* are standard notation for the training set. While the split ratio is not specified (a minor clarity gap), characterizing this as a potential fatal leakage is not supported by the paper as written. → *Downgraded to Minor (item 1 above).*

- **Hyperparameter α not discussed.** The critic notes α is not discussed, but the paper explicitly states "4.2 discusses this procedure in more detail" (line 78). This section was likely stripped by the PDF parser. → *Removed (addressed in stripped appendix).*

- **Multi-class and regression experiments missing.** The paper explicitly scopes to binary classification to study imbalance (line 95) and notes that the pipeline is "natively applicable to multi-class" (line 95). Requesting these experiments is scope creep. → *Removed.*

- **Open-source release / reproducibility concerns about code availability.** The paper does not provide a code link, but this is not a stated contribution (the paper presents the benchmark conceptually). The "open-source" criticism is speculative and reflects a reviewer expectation, not a paper flaw. → *Removed.*

- **All generic "strengths" about the problem being important.** The Strength Finder's claim that "this paper addressed an important problem" is generic and not specific to this paper's contribution. → *Removed from Strengths.*

## Novel Insights

Beyond the paper's own contributions, the most notable emergent insight from the reviews is a structural tension: the paper frames "column embeddings + autoencoding" as the specific innovation, yet does not run the straightforward ablation (autoencoder without column embeddings) that would validate this framing. This gap means the paper's strongest empirical finding — that latent-space distillation helps — is robust, but the attribution of *why* (column embeddings specifically) is not fully proven. The massive scale of the benchmark partially compensates for this, but the core attribution remains underdetermined without the ablation.

## Suggestions

1. **Define the 0.5–143% claim precisely.** State whether it is relative or absolute improvement, in which metric (balanced accuracy or relative regret), and report the median and interquartile range to contextualize the wide endpoints. A paired comparison showing the fraction of dataset×classifier pairs with positive improvement would be more informative than the range alone.

2. **Add the column-embedding ablation.** Include a baseline where a standard autoencoder (without column embeddings) is trained on the raw preprocessed feature vectors, then used for latent-space distillation. This directly tests whether column embeddings are the cause of improvement or if any autoencoding suffices.

3. **Explicitly state the train/test split protocol** — the split ratio, stratification strategy, and a confirmation that the test set is untouched until final evaluation.

4. **Specify which k-means variant was used** (synthetic cluster center vs. nearest real point) in the results section, and briefly justify the choice.

5. **Add a limitations paragraph** to Section 5 discussing failure cases, sensitivity to the reconstruction/classification trade-off (α), and the computational overhead of representation learning.
