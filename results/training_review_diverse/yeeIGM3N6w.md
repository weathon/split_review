Now I have a thorough understanding of the paper and can verify each claim. Here is my consolidated review.

---

## Summary

This paper proposes HC-SMoE, a retraining-free, task-agnostic framework for reducing the number of experts in sparse Mixture-of-Experts (SMoE) language models. The method uses hierarchical clustering (average linkage) on averaged expert outputs as the similarity metric to group functionally similar experts, then merges experts within each cluster. The paper evaluates on two model families (Qwen: 60→30 experts, Mixtral: 8→4 experts) across eight zero-shot language tasks, consistently outperforming pruning baselines (O-prune, S-prune, F-prune) and the M-SMoE merging baseline.

## Strengths

- **Expert outputs convincingly outperform alternative similarity metrics.** The ablation in Table~4 (tab:ab-hc) shows that clustering with expert-outputs under average linkage achieves 0.5459 average, while router-logits yield 0.3153 and weights yield 0.5234 on Qwen 45x2.7B. This three-way comparison, repeated across models and reduction rates, provides strong evidence that output-based similarity captures functional expertise better than prior metrics.

- **Hierarchical clustering demonstrates clear advantages over K-means and single-shot grouping.** Table~5 (tab:ab-kmeans) shows HC-SMoE achieves 0.5426 average vs. the best K-means variant at 0.5415 on Qwen 45x2.7B, with K-means exhibiting high sensitivity to initialization (12.96% drop from fixed to random initialization with weights). Table~6 (tab:ab-one-shot-mixtral) shows HC-SMoE outperforms single-shot grouping by 1.98% (Mixtral 6x7B) and 1.67% (Mixtral 4x7B). The consistency across model scales substantiates the claim that iterative clustering matters more than the merging method.

- **Strong empirical results across two model families and eight tasks.** On Qwen 30x2.7B (50% reduction), HC-SMoE averages 0.5223, outperforming the best baseline F-prune (0.4528) by 6.95% absolute. On Mixtral 4x7B, HC-SMoE achieves 0.5729, competitive with O-prune (0.5728) while dramatically outperforming S-prune (0.4062). Performance degrades gracefully — within 3% of the original model at 25% reduction and 7.43% at 50% reduction.

- **Comprehensive ablation study isolating design choices.** Tables 4–7 systematically ablate linkage methods (single/complete/average), similarity metrics (router-logits/weights/expert-outputs), clustering algorithms (hierarchical/K-means/single-shot), and merging strategies (frequency/average/fixed-dominant). The finding that merging strategy has little impact when clustering is good (Table 7: all three strategies score within 0.001 of each other on Qwen 45x2.7B) cleanly isolates clustering quality as the driver of performance.

- **Practical retraining-free pipeline.** Uses only 32 sequences of 2,048 tokens from C4 as calibration data, requiring no fine-tuning or task-specific data.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The distance metric for expert output vectors is not specified.** The paper discusses linkage methods (single, complete, average) but never states the underlying distance function applied to the averaged expert output vectors before hierarchical clustering. The method repeatedly refers to "pairwise distance" and "cluster distance" (Section 3.2.2) without specifying whether cosine similarity, Euclidean distance, or another measure is used. This is a genuine reproducibility gap — the distance metric is a free parameter of the algorithm, and the paper's own Table 4 shows that different metrics (router-logits vs. weights vs. expert-outputs) produce dramatically different results, so the distance function for expert outputs matters. The paper clearly implemented *something*; it needs to be stated explicitly.

- **The scalability claim is imprecisely supported.** The paper claims the method "scales efficiently with the number of experts" (contributions list), but provides no runtime measurements, no complexity analysis, and demonstrates only on models with 8 and 60 experts per layer. Average-linkage hierarchical clustering has O(n²) time and memory complexity in the number of experts. For 60 experts this is negligible, but the claim as stated implies a generality that is not demonstrated. The paper's own "scalability" evidence (Section 4.2, line 216–217) refers to *performance* scaling (comparable scores across parameter counts), not computational efficiency — the two are conflated. The claim should be either substantiated with runtime/complexity data or qualified.

- **The comparison with M-SMoE is in a regime it was not designed for.** The paper applies M-SMoE in a task-agnostic setting without retraining (Section 4.1), even though the paper correctly notes that M-SMoE was designed *with* retraining (Section 2, Table 1 marks it as requiring retraining). M-SMoE then unsurprisingly performs worst among baselines. This comparison is transparently reported, but it is not informative about M-SMoE's actual capabilities and therefore does not meaningfully strengthen the case for HC-SMoE. A comparison against M-SMoE *with* retraining (or at least a discussion of the trade-off) would have been more useful.

- **Calibration data sensitivity is not examined.** The method uses a fixed calibration set of 32×2048 tokens from C4. The paper does not investigate how sensitive clustering results (and downstream performance) are to different calibration datasets, different sample sizes, or different random draws from C4. For deployment where calibration data may mismatch the test distribution, this is a relevant concern.

### Trivial
None.

## Nice-to-Haves

- A brief analysis of *why* expert outputs provide better similarity than router-logits or weights — beyond the intuitive reasoning already given — would strengthen the paper. For instance, silhouette scores or dendrogram visualizations comparing clusters formed by different metrics.
- Wall-clock time for the clustering step would aid reproducibility and practical adoption.
- The paper could note that the number of clusters (merged experts) is currently determined by the experimental design (target reduction rate), and hierarchical clustering's dendrogram could also support automatic selection (e.g., by cutting at a similarity threshold).
- An experiment showing that when clustering is deliberately degraded (e.g., random grouping), different merging methods diverge dramatically — reinforcing the paper's own claim that clustering quality is the primary driver.

## Removed Points

These were raised by reviewers but are not included in the main weaknesses for the reasons stated:
- **"M-SMoE results primarily serve to inflate HC-SMoE's relative advantage"** — The paper is transparent about evaluating M-SMoE in a task-agnostic, retraining-free setting, and does not over-claim from this comparison. The transparency makes this an acknowledged limitation, not an unfair inflation.
- **"The 'first retraining-free, task-agnostic SMoE merging strategy' claim is plausible but narrow"** — This is a normative judgment, not a weakness. The paper correctly qualifies this as "to the best of our knowledge."
- **Strength Finder's claim that "HC-SMoE... outperforms the best baseline F-prune (0.4528) by 6.95% absolute" while also claiming "the competing merging method M-SMoE collapses to 0.3221"** — Both numbers are correct in the paper but the implied contrast is somewhat inflated since M-SMoE is used outside its intended regime, as noted above.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the method's behavior that the authors themselves have not already identified or claimed.

## Suggestions

1. **Specify the distance metric** used for expert output vectors (and justify the choice briefly). This is a one-line fix that closes the main reproducibility gap.
2. **Clarify the scalability claim**: either provide wall-clock measurements or O(·) analysis for the clustering step, or rephrase to distinguish performance scalability from computational scalability.
3. **Add a calibration-data sensitivity experiment** — even varying the sample size (e.g., 16 vs. 64 sequences) or drawing from a different corpus would help establish robustness.
4. **Acknowledge the M-SMoE comparison limitation** more directly: state that M-SMoE with retraining would be a different (and likely stronger) baseline, and that the reported results only show the inadequacy of router-logit-based grouping in a retraining-free setting.

## Score and Decision

This is a solid empirical paper with a clear contribution: a well-motivated, retraining-free expert merging method backed by thorough ablations that cleanly isolate clustering quality as the key design factor. The core findings are convincing and reproducible modulo one missing detail (the distance metric). The missed specification and the imprecise scalability claim are genuine but minor gaps that do not threaten the main conclusions. The paper represents a meaningful step forward for practical SMoE compression and merits acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>