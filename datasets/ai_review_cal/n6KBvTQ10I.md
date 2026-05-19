- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3
Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes UNIC, a method that unifies deep image clustering and Generalized Category Discovery (GCD) by mining positive and negative neighbors in a DINO ViT embedding space. The key innovations are: (1) a second-order neighborhood cleaning strategy that discards noisy positive neighbors based on the union size of their neighbors' neighborhoods; (2) mining far-away samples as negative neighbors with a binary cross-entropy loss; and (3) a unified end-to-end finetuning pipeline that adapts naturally to GCD by using labeled data as ground-truth neighbors. The method achieves SOTA results on several clustering and GCD benchmarks.

## Strengths

1. **Second-order neighborhood cleaning is a novel and well-validated contribution.** The paper introduces a principled heuristic — discarding positive neighbors whose second-order neighborhood union exceeds a threshold η — and empirically validates in Figure 4 that second-order neighborhood size correlates with true-positive rate. This is a genuine improvement over prior clustering methods (SCAN, NNM) that use raw nearest neighbors without such cleaning.

2. **Negative neighbor mining provides a strong supervisory signal, as validated by controlled ablations.** Ablations in Table 3 and Figure 5 systematically isolate the contribution of each loss component. The L_neg term alone achieves competitive accuracy (~73% on ImageNet-50) and, importantly, prevents the trivial collapsed solution without requiring the entropy maximization term that prior methods rely on. This is a meaningful empirical finding.

3. **The GCD ablations (Table 4) directly demonstrate the benefit of mined over random neighbors.** Replacing random negatives with mined negatives improves all-class accuracy from ~70% to 73.7% on ImageNet-100 GCD, providing concrete evidence that the neighbor mining strategy benefits the semi-supervised setting beyond simply using labeled data.

4. **The unified pipeline is a clean conceptual contribution.** Treating GCD as a partially supervised version of the same neighbor-mining framework (using labels as perfect neighbors) is elegant and eliminates the need for separate clustering-based initialization that prior GCD methods require. The approach demonstrably works for both tasks with minimal adaptation.

## Weaknesses

### Fatal
None.

### Major

1. **Backbone-controlled comparison is insufficient to fully support the SOTA claim.** UNIC uses DINO ViT-B/16, while several baselines in the clustering table (SCAN, NNM, SPICE) use ResNet backbones. The paper does compare against k-means on the same DINO backbone (k-means DINO in Table 1), showing that UNIC improves over this controlled baseline. However, the SOTA claim relative to prior methods would be stronger if additional backbone-controlled experiments were run — e.g., running SCAN/NNM on DINO ViT-B/16 embeddings, or comparing UNIC against TEMI under identical backbone conditions (TEMI also uses ViT, but the paper's reimplementation of TEMI may differ from the original). The large gains over ResNet-based methods could reflect backbone quality differences as much as the proposed methodological innovations. Given that the paper's own text notes (line 35) that TSP/TEMI "leverage ViTs to outperform the earlier methods (which mainly use ResNets)," this concern should have been addressed explicitly.

2. **Hyperparameter sensitivity is insufficiently analyzed.** The neighbor cleaning threshold η and negative neighbor cutoff τ₂ vary dramatically across datasets without a systematic sensitivity analysis or a principled selection procedure. Specifically: τ₂ = 6300 for ImageNet splits, 1000 for STL/CUB, 10,000 for CIFAR-10; η = 1500 for ImageNet splits (clustering), 70 for ImageNet-100 (GCD), CIFAR-10, and STL-10 (lines 103, 130). The paper describes these as "based on heuristics" (line 103) without specifying the heuristic or showing how performance varies with η/τ₂. This makes it unclear whether the method requires expensive per-dataset tuning to achieve SOTA, which limits its claims of generality.

3. **Negative neighbor mining strategy is not compared against plausible alternatives.** The paper uses all images beyond distance rank τ₂ as negatives. For ImageNet splits with τ₂=6300 and ~1.3M images, this means ~1.29M negatives per anchor, most of which are trivially easy (images from completely different visual domains). The ablation in Table 4 shows "mined negatives" beat "random negatives" (which suffer from false negatives), but the paper never compares against *hard* negatives (e.g., nearest neighbors of a different predicted class, or samples near the decision boundary). Without this comparison, it is unclear whether the proposed strategy is actually an effective choice or merely adequate.

### Minor

1. **No error bars or multiple-run statistics are reported.** Given the sensitivity to hyperparameters (η, τ₂) and random initialization, single-run results make it difficult to assess whether small-margin improvements (e.g., +0.8% on ImageNet-100 GCD) are statistically meaningful. This is standard practice to include for the paper's level of empirical rigor.

2. **The computational cost of using all negatives (potentially millions per anchor) is not discussed.** The paper does not specify whether negatives are subsampled per batch, how memory is managed, or the training time. This information is important for reproducibility and practical adoption.

3. **Backbone specification for GCD baselines in Table 2 is unclear.** The paper states it uses DINO ViT-B/16, but does not clearly list which backbone each baseline method in Table 2 uses (ResNet-50 vs. ViT-B/16 vs. DINO ViT-B/16). Since backbone choice strongly affects GCD performance, this omission makes the comparison harder to interpret.

### Trivial

1. **Notation inconsistency:** The outer loss weights in Equation 9 are denoted α_{sim} and α_{ent}, while the ablation weights in Table 3 and Figure 5 are denoted λ_{POS}, λ_{NEG}, λ_{ENT}, λ_{CON} — although they serve similar purposes. The figure axis and caption also use "λ" while the equation uses "α." This is confusing and should be harmonized.

## Nice-to-Haves

- A sensitivity analysis sweeping η and τ₂ across a range of values for at least one dataset, to demonstrate the method's robustness to these hyperparameters.
- A comparison against hard negative mining strategies (e.g., mining the closest images predicted to belong to different classes) to better justify the "far negative" choice.
- Reporting results with standard deviations over 3-5 random seeds, especially for datasets where improvements are marginal.

## Removed Points

The following criticisms raised in the input reviews were evaluated against the paper and found to be unsupported or misinformed, and are removed from the main review:

- **"The claim that L_neg alone converges to a stable solution is misleading"** — The harsh critic misinterprets "stable" as "high-performing." In the clustering literature, "stable" means the model does not collapse to a trivial solution (all images in one cluster). The paper's claim that L_neg alone prevents collapse (line 148) is factually accurate; the fact that full method achieves 82% vs. 73% with L_neg alone does not contradict this claim.
- **"TEMI reimplementation may be suboptimal" as a standalone fatal concern** — The paper transparently marks baselines with † for "our implementations." While reimplementation quality is a valid general concern, the reviewer provides no specific evidence of a bug or poor tuning, and the paper does compare against the original TEMI paper's published numbers (acknowledged in the table). This is noted but does not rise to a substantiated weakness.
- **"The negative mining is unlikely to provide a strong learning signal"** — This is a speculative claim contradicted by the paper's empirical evidence (ablation results in Table 3 and Figure 5 show L_neg substantially improves performance). The concern about hard negatives not being compared is kept (Major 3), but the assertion that the strategy is "likely ineffective" without evidence is removed.
- **"Missing related works"** — Removed per instructions (no external sources to verify).
- **Various formatting/typo criticisms** — Removed as parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation about the paper not already stated by the authors.

## Suggestions

1. **Add backbone-controlled experiments** for the clustering baseline comparisons. Running k-means on the same DINO ViT-B/16 features for all baseline methods (even approximately) would isolate the gain from the proposed neighbor mining and cleaning pipeline from the gain of using a stronger backbone.
2. **Include a hyperparameter sensitivity study** (e.g., sweep η across {50, 200, 500, 1000, 2000} on one or two datasets and report how accuracy varies). This is the single most impactful addition the authors could make.
3. **Add a hard negative mining comparison** to justify the "far negative" design choice. Without this, one of the paper's two main technical components (negative mining) is weakly motivated relative to alternatives.
4. **Harmonize notation** for loss weights (use either α or λ consistently between equations, tables, and figures).
5. **Report results with error bars** across multiple runs for small-margin improvements.
