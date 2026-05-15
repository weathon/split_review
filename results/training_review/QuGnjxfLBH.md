Now I have all the information needed. Let me compose the final consolidated review, carefully verifying each claim against the paper text.

---

## Summary

This paper proposes a benchmark process for constructing FL benchmarks on multi-semantic vision datasets where each sample contains multiple labels (e.g., scene graphs with objects, subjects, predicates). The process has two steps: (1) clustering data into semantic groups via K-means on a "category tensor" derived from the multi-label annotations, and (2) distributing data across clients with controllable heterogeneity using shard-based or Dirichlet-based partitioning on the resulting cluster labels. As a proof of concept, the authors construct the first FL benchmark for Panoptic Scene Graph Generation (PSG), evaluating four PSG models under six partition settings, varying client counts, participation rates, and one FL algorithm (FedAvgM).

## Strengths

- **Identifies a genuine gap in FL benchmarking.** The paper clearly demonstrates (Figure 1) that existing FL benchmarks overwhelmingly focus on single-label classification (one-hot labels), while many modern vision tasks involve multiple semantics per sample. The motivation for extending FL benchmarks to multi-semantic tasks is well-argued and timely.

- **Proposes a principled, task-agnostic benchmark process.** The two-step framework — semantic cluster discovery via K-means on category tensors (Section 4.1) followed by controllable data partitioning (Section 4.2) — is formalized mathematically and does not rely on pretrained models, making it applicable to a range of multi-semantic vision tasks beyond SGG/PSG.

- **Provides the first FL benchmark for PSG with reasonable breadth of evaluation.** The paper evaluates four PSG methods (IMP, MOTIFS, VCTree, GPS-Net) under six partition settings, varying client counts, participation rates, and FedAvgM. The results confirm that the benchmark imposes meaningful semantic heterogeneity: non-IID splits cause clear performance degradation relative to IID splits (average mR@20 drop of -0.77% for shard non-IID, -0.64% for Dirichlet), while random splitting produces near-IID behavior (gap ≤0.32%), validating that prior naive random splits do not capture heterogeneity.

- **Reveals a meaningful connection between long-tail robustness and FL heterogeneity robustness.** GPS-Net, designed for long-tailed PSG data, shows the smallest performance drop under semantic heterogeneity (e.g., minimal change in Table 2 with FedAvgM), while IMP, which struggles with long tails, shows the largest gap (-1.58% mR@20 from Dir(α=10) to Dir(α=0.2)). This insight is useful for the community.

- **Validates that standard FL techniques work on the benchmark.** FedAvgM consistently improves performance across methods (average +1.30% mR@100 in shard non-IID, Table 2), confirming the benchmark captures realistic FL challenges and behaves as expected.

## Weaknesses

### Fatal
None.

### Major

- **Centralized learning baseline is confounded with data quantity.** The paper equalizes cluster sizes via subsampling before FL partitioning (Section 4.2), discarding the majority of Cluster 2 (58%→5% share). The centralized learning (CL) baseline is described only as "with a centralized dataset without considering the FL settings" (Table 1 footnote) — it is not stated whether CL also uses the subsampled balanced dataset or the full original dataset. Since FL clients collectively see only ~25% of the original data after subsampling, the performance gap between CL and IID (averaging -2.45% to -2.71% mR@20) is confounded by dataset size and cannot be attributed solely to "decentralized training" or "limited data per client" as the paper does. This does **not** invalidate the benchmark's core contribution (the IID vs. Random vs. non-IID comparisons within FL are controlled), but it weakens the specific claim that "CL ≥ IID ≥ Random ≥ non-IID" is cleanly supported by the evidence.

- **No error bars or multiple seeds reported.** All results in Tables 1–4 are single-run with no variance estimates. FL is stochastic (client sampling, data partitioning seeds, model initialization), so single-run comparisons cannot be trusted for ranking algorithms or drawing fine-grained conclusions (e.g., the claim that MOTIFS shows "shaky behavior" at moderate non-IID is based on differences of ~0.2% mR@20 with no uncertainty quantification). For a paper proposing a *benchmark*, this is a significant gap in experimental rigor.

- **Validation on only one dataset and no comparison against alternative heterogeneity baselines.** The benchmark process is demonstrated solely on PSG. There is no application to another multi-semantic task (e.g., multi-label classification, visual relationship detection with different label spaces) to establish task-agnostic generality. Moreover, the clustering step is not compared against alternatives such as applying Dirichlet partitioning directly on raw predicate frequencies (without clustering) or using feature-space clustering with pretrained embeddings. Without such comparisons, it is unclear whether the category tensor clustering yields meaningfully different or more useful heterogeneity than simpler approaches.

### Minor

- **Cluster derivation lacks quantitative validation.** The choice of K=5 is not justified (no elbow method, silhouette score, or stability analysis), and the cluster descriptions (Section 4.3) are purely qualitative. Since the entire heterogeneity control depends on these clusters, the absence of validation metrics (coherence, separation, sensitivity to K) is a concern. Additionally, the paper does not specify how multiple triplets per image are aggregated into the category tensor (binary presence indicators? counts? normalized frequencies?) — this is a reproducibility gap.

- **Limited FL algorithm coverage.** Only FedAvg and FedAvgM are tested, while the paper itself cites FedProx, SCAFFOLD, and FedDyn as standard heterogeneity-handling algorithms (Section 2.1). A benchmark's utility depends partly on whether it can differentiate between algorithms; testing more FL methods would strengthen the contribution.

- **Some conclusions are speculative given the thin evidence.** The claim that "rather than increasing the number of participants in each round, the larger amount of data of each participant can expect greater performance improvement" (Section 5.4) is based on a single model (MOTIFS) showing this pattern, with no statistical testing. Similarly, the floor effect for GPS-Net in Table 2 (negligible FedAvgM improvement) may be because absolute performance is very low (~4.5% mR@20), not because GPS-Net is inherently robust to heterogeneity.

### Trivial

- Figure 3 (PCA visualization of clusters) is referenced but not described in terms of how PCA is applied to the category tensor; the axes are unlabeled.

- The paper uses "SSG" instead of "SGG" in one place (line 210: "SSG/PSG"), a minor inconsistency.

## Nice-to-Haves

- **Run CL on the subsampled balanced dataset** to provide a clean ablation that isolates the cost of decentralization from data reduction.
- **Report per-client or per-cluster performance** to analyze whether the global model performs uniformly across semantic contexts.
- **Plot training dynamics** (mR@K vs. communication round) to reveal convergence behavior differences across heterogeneity levels and algorithms.
- **Explore alternative mitigation for cluster imbalance** (e.g., weighted aggregation) instead of subsampling, which discards data.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Each round trains on only 5×16=80 images per round"** — Factually incorrect. The paper explicitly states "one epoch" (line 151), meaning each active client processes all of its ~114 local images per round, not one batch. With 5 active clients, each round processes ~570 images. The calculation ignores the "one epoch" specification.

- **Criticism about CL baseline being "uninterpretable"** — Overstated. The CL vs. IID comparison is confounded, but the IID vs. Random vs. non-IID comparisons within the FL setting are controlled and independently informative. The benchmark's core value does not hinge on the CL comparison.

- **"The paper overstates the novelty" and "the comparison with FedNLP is superficial"** — These are subjective opinions. The paper clearly articulates why extending existing FL benchmarks to multi-semantic tasks is non-trivial (Figure 1 and Section 1) and adequately contrasts with FedNLP (reliance on pretrained language models vs. the proposed task-agnostic tensor approach).

## Novel Insights

The most interesting finding that emerges from synthesizing the reviews and the paper is the interaction between the long-tailed problem inherent in SGG/PSG datasets and FL's semantic heterogeneity. The paper shows that GPS-Net, which uses components (DMP, NPS, ARM) designed to handle long-tailed predicate distributions, is also the most robust to semantic heterogeneity across clients. This suggests a deeper structural connection: both the long-tailed problem and FL semantic heterogeneity manifest as uneven per-class representation, and methods that address one may naturally help with the other. This insight is well-supported by the results and is valuable for guiding future FL algorithm design for structured prediction tasks. However, this insight would benefit from controlled experiments that separately vary long-tail severity and semantic heterogeneity.

## Suggestions

1. **Clarify the CL baseline.** State explicitly whether CL uses the full dataset or the subsampled balanced dataset. Ideally, include both baselines (CL-full and CL-subsampled) to allow clean decomposition of data quantity effects from decentralization effects.
2. **Add error bars.** Report means and standard deviations over at least 3 random data partition seeds for all major tables. This is essential for a benchmark paper.
3. **Validate clustering quantitatively.** Report silhouette scores or similar metrics for K=5, and show sensitivity analysis across K ∈ {3,4,5,6,7} to demonstrate that the benchmark's behavior is not brittle to this choice.
4. **Specify the tensor aggregation.** Clarify whether each cell of the category tensor is binary (presence of a (subject, object, predicate) combination), a count, or a normalized value. This affects reproducibility.
5. **Test at least one more FL algorithm.** Adding FedProx or SCAFFOLD would significantly strengthen the benchmark's utility as an evaluation platform.
6. **Apply to a second multi-semantic task.** Even a simple multi-label classification dataset (e.g., COCO multi-label) would help demonstrate task-agnostic generality.

## Score and Decision

The paper identifies a genuine gap in FL benchmarking and proposes a reasonable, principled process for filling it. The qualitative cluster analysis is intuitive, and the experimental results within the FL setting (IID vs. Random vs. non-IID) are consistent with expectations, validating that the benchmark imposes meaningful semantic heterogeneity. However, the experimental validation has notable gaps: the CL baseline is confounded with data size, no error bars are reported, only one dataset is tested, and the cluster derivation lacks quantitative validation. The core contribution — the benchmark process — is sound and useful, but the paper's evidence is not as strong as its claims. With the identified issues addressed (particularly error bars and the CL baseline clarification), this could become a solid contribution. In its current form, the contribution is worthwhile but the validation is preliminary.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>