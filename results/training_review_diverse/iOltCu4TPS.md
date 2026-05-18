Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper presents a systematic benchmark of 12 single-cell retrieval methods spanning three classes (non-ML, VAE-based, scFM-based) across cross-platform, cross-species, and cross-omics settings. It proposes both label-dependent metrics (Vote-Acc, Avg-Acc, BatchDiv, Recall) and label-free metrics (AvgOverlap, DE-gene consistency). Key findings include that top scFMs (UCE, scFoundation, SCimilarity) show overall advantage, traditional non-ML method CellFishing.jl remains competitive, and scFMs fail when the target species/omics are distant from the pre-training distribution.

## Strengths

- **First comprehensive side-by-side comparison of scFMs with VAE-based and non-ML baselines.** The paper benchmarks 12 methods in a unified framework across three distinct retrieval settings (cross-platform, cross-species, cross-omics), directly addressing the acknowledged gap that "there is no direct comparison between scFMs and other methods in existing works" (Section 1). Tables 1–3 provide the side-by-side results that support the main comparative claims.

- **Novel label-free evaluation metrics with empirical grounding.** The proposal of AvgOverlap (Jaccard similarity of retrieved cell sets across methods) and DE-gene consistency is practically motivated by the lack of ground-truth cell-pair annotations. Figure 2c demonstrates a strong correlation between AvgOverlap and Vote-Acc across four datasets, providing evidence that these metrics can serve as complementary evaluation tools when cell-type annotations are unavailable or inconsistent.

- **Identification of a strong non-ML baseline.** The finding that CellFishing.jl (a 2019 LSH-based method) remains competitive across multiple settings (Tables 1, 2) is a practically useful result that challenges the assumption that ML-based methods are always superior, and provides a concrete, lightweight baseline recommendation.

- **Empirical mapping of scFM failure modes.** The cross-omics evaluation (Section 4.3) cleanly shows that all scFMs perform poorly on mouse multi-omics datasets (Chen-2019, Ma-2020) while VAE-based methods (scVI, LDVAE, CellBlast) achieve best results. This directly supports the conclusion that scFMs are unreliable when both species and omics are far from the pre-training distribution — a nuanced and actionable finding.

## Weaknesses

### Fatal

None.

### Major

- **No uncertainty quantification or statistical significance in reported results.** All tables (1–3) report point estimates without any measure of variability. For a benchmark that aims to rank methods and draw conclusions about comparative performance, the absence of confidence intervals, standard deviations, or significance tests is a significant gap. Differences as small as 0.01 between methods (e.g., Table 1, K=50, UCE vs. scFoundation) cannot be assessed for reliability. While many of the core findings involve large gaps (e.g., 10%+ differences), the inability to distinguish signal from noise in closer comparisons weakens the precision of the paper's ranking claims. The authors should provide bootstrapped confidence intervals or replicate results across multiple random splits.

### Minor

- **VAE methods trained on the joint query+reference set while scFMs are used zero-shot — asymmetry not discussed.** Section 3.3.1 states that VAE-based methods are trained on the embeddings for both query and reference cells jointly, while scFMs are applied zero-shot. This asymmetry gives VAE methods an inherent advantage (access to the evaluation distribution), which actually makes the observed dominance of scFMs *more* striking rather than less. However, the paper does not acknowledge or discuss this design choice. Adding a brief discussion would improve transparency and prevent misinterpretation by readers.

- **Label-free metrics validated only via correlation on annotated data, not in a true label-free scenario.** Figure 2c shows a correlation between AvgOverlap and Vote-Acc across four datasets, which is positive evidence. However, the paper advocates that these metrics "can be employed in a broader scenario" (Abstract) when labels are unavailable, yet the validation is only shown on datasets where labels *are* available. The step from "correlates with accuracy when labels exist" to "functions as a reliable proxy when labels do not exist" would benefit from additional support — e.g., using AvgOverlap to rank methods on an unlabeled dataset and verifying against held-out labels or known biological relationships. The current evidence is suggestive but not yet conclusive for the claimed use case.

- **BatchDiv metric's validity is not independently demonstrated.** The BatchDiv metric computes entropy over batch labels of retrieved cells. As the reviewer correctly notes, a method that returns random cells would trivially achieve high BatchDiv. While the paper's results show that high-BatchDiv methods also tend to have high Vote-Acc (providing some face validity), no explicit analysis is provided to demonstrate that BatchDiv reflects meaningful cross-batch retrieval rather than simply diversity without regard to biological similarity. Showing correlation between BatchDiv and Vote-Acc across methods, or normalizing by the expected entropy of random retrieval, would strengthen this metric.

- **No discussion of potential pre-training data leakage.** Several scFMs are pre-trained on large public scRNA-seq datasets that may overlap with the evaluation data (e.g., human PBMC data is widely available in public repositories). If such overlap exists, the "zero-shot" evaluation is not truly zero-shot — the model may have been exposed to those cells during pre-training. The paper should check for and report any data leakage. This is a standard concern for zero-shot benchmarks using pre-trained models.

### Trivial

- **Minor inconsistency in method categorization and counts.** The paper states it benchmarks 2 non-ML, 3 VAE-based, and 7 scFM-based methods (totaling 12). Section 2.2 lists four methods (CellBlast, scmap, scVI, LDVAE) — though scmap is not strictly VAE-based, the count is unclear. Section 2.3 lists only six named scFMs. And scFind (Section 2.1) appears in the cross-species table but may be absent from other settings without explanation. These are small presentation inconsistencies that should be cleaned up.

## Nice-to-Haves

- **Computational efficiency comparison.** Retrieval time and memory usage are relevant for practical deployment. Including wall-clock time or embedding generation cost would strengthen the practical recommendations.
- **Sensitivity analysis for pre-processing choices.** Using each method's default pre-processing is a reasonable choice, but a small-scale robustness check (e.g., fixing a common pre-processing pipeline for a subset of methods) would help disentangle model quality from pre-processing effects.
- **Controlling BatchDiv for retrieval quality.** Normalizing BatchDiv by the expected entropy under random retrieval would make the metric more interpretable.

## Removed Points

The following points from the reviews were removed after verification against the paper:

- **"Unfair comparison between zero-shot scFMs and trained VAE methods" framed as a weakness that harms the paper's conclusions.** After verification, the asymmetry favors VAE baselines (trained on the joint set) over scFMs (zero-shot), making the scFM dominance *more* striking, not less. Per the rules, an asymmetry that favors the baseline does not count as a weakness against the paper. The point was moved to Minor (as a transparency/acknowledgment issue) rather than treated as a methodological flaw.
- **Generic/superficial strengths from the Strength Finder were dropped.** No such cases occurred — all four identified strengths are specific and evidence-backed.
- **The "pre-processing differences as a confound" point** was noted by the reviewer but is a standard design choice in benchmarking, not a genuine weakness. It is retained only as a Nice-to-Have.
- **"Retrieval time and memory not discussed"** — a fair wishlist item but not a weakness of the current paper's contribution scope. Moved to Nice-to-Haves.

## Novel Insights

The reviews collectively surface an interesting tension that the paper itself does not fully address: the zero-shot scFMs dominate the VAE methods despite the VAE methods having the advantage of being trained on the evaluation distribution (joint query+reference). This means scFMs are likely even more dominant than the tables suggest — the reported advantage is a lower bound. Conversely, the label-free metrics face the opposite structural issue: they are validated only in settings where labels exist, which is precisely the scenario where they are least needed. The paper's central methodological contribution (label-free evaluation) and its central empirical finding (scFM dominance) thus sit on opposite sides of the same validation gap. Bridging this — e.g., by demonstrating label-free ranking fidelity on a dataset where labels are then revealed — would tighten both contributions simultaneously.

## Suggestions

1. **Add confidence intervals or bootstrapped standard errors** to all main tables (1–3). This is the single highest-impact change. For a benchmark paper, readers need to know which differences are meaningful.
2. **Explicitly acknowledge the VAE vs. scFM training asymmetry** in Section 3.3.1 or the Limitation section, noting that this makes the scFM results conservative.
3. **Strengthen the label-free metric validation** by either: (a) simulating label-withholding on one of the existing datasets and showing that AvgOverlap-based rankings match the label-based rankings, or (b) adding a brief discussion that the current correlation evidence is supportive but preliminary.
4. **Check and report pre-training data overlap** for all scFMs, especially for the PBMC and pancreas datasets. Add a data leakage statement to the Limitation section.
5. **Clean up method counts and coverage.** Ensure the counts (2 non-ML, 3 VAE, 7 scFM) are consistent with the methods listed in Sections 2.1–2.3 and that each method's appearance across tables is explained.

## Score and Decision

The paper makes a solid empirical contribution — the benchmark scope is appropriate, the experimental design across three settings is well-conceived, and several findings (CellFishing.jl as a strong baseline, scFM failure on distant species+omics) are genuinely useful. The proposal of label-free metrics adds value to the benchmarking toolkit. However, the absence of any uncertainty quantification in what is explicitly a ranking-oriented benchmark is a structural gap that weakens the precision of the paper's core comparative claims. The other issues (asymmetry acknowledgment, data leakage, metric validation depth) are addressable. The paper is a useful contribution that would benefit from strengthening its statistical foundation before acceptance.

**MY FINAL SCORE:** <pineapple>6.5</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>