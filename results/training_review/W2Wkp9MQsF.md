Now I have a thorough understanding of the paper and can verify the reviewers' claims. Let me produce the consolidated review.

## Summary

This paper introduces model folding, a data-free compression technique that merges structurally similar neurons within a single network using k-means clustering, without requiring fine-tuning or access to training data. The authors propose two data-free alternatives to the data-driven REPAIR method for correcting variance collapse after compression: Fold-AR (using an independence assumption to estimate cluster correlations) and Fold-DIR (using Deep Inversion synthesized images to update BatchNorm statistics). Experiments on ResNet18, VGG11, and LLaMA-7B show that model folding outperforms prior data-free methods (IFM) and approaches the performance of data-driven compression methods.

## Strengths

- **Principled data-free neuron merging via k-means clustering.** The paper provides a theoretical justification showing that k-means clustering minimizes the Frobenius norm approximation error for the weight matrix (Section 3.1, Equations 3–7), and extends this analysis to interdependent layers with concatenated weight matrices. This is a more principled foundation than the greedy iterative matching used in prior data-free methods like IFM.

- **Novel data-free statistics repair methods (Fold-AR and Fold-DIR).** The paper introduces two techniques to prevent variance collapse and overshooting after compression without data. Fold-AR estimates cluster correlations under an independence assumption, while Fold-DIR leverages a single batch of Deep Inversion–synthesized images. Figure 5 shows both methods closely approach the performance of data-driven REPAIR and significantly outperform IFM, especially at high sparsity levels. This is the paper's clearest contribution.

- **Identification and mitigation of both variance collapse and variance overshooting.** The paper observes that naive merging leads to variance collapse (Jordan et al., 2022) while IFM leads to variance overshooting. Maintaining a variance ratio close to 1 (Figure 4) is shown to be critical for accuracy. Fold-AR and Fold-DIR are explicitly designed to keep this ratio near 1, explaining their superior performance. The variance ratio diagnostic (Definition 1) is a useful contribution in itself.

- **Demonstration that model folding is viable on LLaMA-7B without data or fine-tuning.** Table 1 shows that model folding achieves perplexity and zero-shot accuracy comparable to data-driven structured pruning methods (LLM-Pruner, Wanda_sp, FLAP) while using no calibration data or gradients. Since LLaMA-like models have no BatchNorm, the method applies clustering alone — a useful practical data point.

- **Empirical evidence that wider networks benefit more from folding.** Figures 8 and 9 show that increasing model width improves compression quality, providing useful insight into the relationship between network redundancy and model folding effectiveness.

## Weaknesses

### Fatal

None.

### Major

1. **Ambiguity of which repair variant is used in the ImageNet experiments (Fig. 6).** The paper defines two data-free repair methods (Fold-AR and Fold-DIR), but Figure 6 — the main ImageNet comparison against IFM and structured magnitude pruning — only refers to "model folding" without specifying which variant is used. The preceding text discusses Fold-DIR, implying it may have been used, but this is not stated explicitly. This is a significant reproducibility and interpretability problem: Fold-AR is a purely analytic heuristic requiring no data at all, while Fold-DIR uses Deep Inversion to synthesize images. The reader cannot assess whether the claimed ImageNet results depend on the generative component or are achievable with the simpler analytic method. Both Fig. 1 and Fig. 5 explicitly name the variants; Fig. 6 should too.

2. **Uncontrolled sparsity allocation in the LLM comparison (Table 1) raises comparability concerns.** Model folding uses a hand-designed non-uniform sparsity allocation for LLaMA-7B (different rates per decoder block and per layer type, described as "following SOTA"). The baselines (LLM-Pruner, Wanda_sp, FLAP) determine sparsity allocation using their own importance scores. While it is standard in pruning to compare methods at the same *overall* sparsity with different allocations, the paper does not discuss whether the chosen allocation gives model folding an advantage. A controlled comparison — either using the same per-layer sparsity masks across methods, or showing model folding under a uniform allocation — would substantially strengthen the claim. As it stands, the LLM results are suggestive but not fully controlled.

### Minor

3. **Fold-AR's independence assumption is unvalidated.** Fold-AR estimates the mean cluster correlation \(E[c]\) by assuming the previous layer's outputs are uncorrelated (line 211). This is a strong assumption, and the paper provides no experiment comparing the estimated correlations to ground-truth correlations computed from held-out data. Since the scaling factor (Equation under line 202) depends directly on this estimate, the sensitivity of Fold-AR's performance to violations of the independence assumption is unknown. An ablation or diagnostic would help the reader understand when Fold-AR can be trusted.

4. **Novel data-free repair methods tested in detail on only one architecture/dataset.** Figures 4 and 5 show Fold-AR and Fold-DIR exclusively on ResNet18/CIFAR10. On ImageNet (Fig. 6), the repair variant is not specified and the comparison is with older structured pruning baselines (Cai et al., 2020; Yin et al., 2022). An ImageNet ablation comparing Fold-AR vs. Fold-DIR vs. Fold-R (data-based REPAIR) would significantly strengthen the paper and resolve the ambiguity in point 1.

5. **Theoretical optimality claim is limited to a specific objective.** The paper states that k-means is "theoretically optimal" for merging weights. This is correct for minimizing the Frobenius norm approximation of the concatenated weight matrix of successive layers, but the analysis treats the network as linear — it does not account for how approximation errors propagate through nonlinear activation functions (ReLU) or BatchNorm. The concatenation strategy (Eqs. 8–14) is a reasonable heuristic but falls short of an end-to-end theoretical guarantee. The claims should be scoped to the Frobenius norm objective and the heuristic nature of the multi-layer extension should be acknowledged more clearly.

### Trivial

- Table 1 caption references "Tab. Results of folding LLaMA2-7B" but this appears to be an unresolved placeholder/incomplete sentence (likely a parser artifact).

## Nice-to-Haves

- An ablation on LLaMA-7B showing the effect of uniform vs. non-uniform sparsity allocation for model folding itself would help disentangle the benefit of clustering from the benefit of smart sparsity allocation.
- A comparison on ImageNet between Fold-AR and Fold-DIR would clarify which method is preferable under different resource constraints.
- A simple validation experiment for Fold-AR's independence assumption (comparing estimated \(E[c]\) with data-computed \(E[c]\) for a few layers) would increase confidence in the method.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about missing related works (network slimming, filter grouping):** Removed per instructions — the reviewer cannot confirm whether these would be relevant or are already discussed elsewhere.
- **Criticism about the limitation "does not optimize sparsity per layer" contradicting the LLM experiment:** Removed — this is a misunderstanding. The limitation means the *method* does not automatically determine per-layer sparsity; the user can manually set different levels, which is exactly what was done. No contradiction.
- **Criticism that the LLM result is "meaningless" and "invalidates" the paper's main claim:** Downgraded from fatal to major. The sparsity allocation concern is legitimate but not fatal — comparing methods at the same overall sparsity is standard practice in pruning, and the paper's result is suggestive even if not perfectly controlled.
- **Criticism that Fig. 3 "does not involve any of the paper's claimed contributions":** Removed — Fig. 3 compares k-means to other clustering methods as a supporting ablation, which is standard practice and does not need to involve the repair methods.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the variance ratio diagnostic (Definition 1) combined with the discovery that IFM causes *overshooting* (not just collapse) is a genuinely useful analytical tool for the model merging/compression community. The paper shows that maintaining a variance ratio near 1 is both necessary and sufficient for good compression performance, and this insight is cleaner than any specific method. The contrast between Fold-AR (analytic, zero data cost) and Fold-DIR (requires synthetic data generation) also provides a clear design axis — data-freeness vs. approximation quality — that future work can build on.

## Suggestions

1. **Clarify which repair variant is used in every experiment.** Rename "model folding" in Fig. 6 to "Fold-AR" or "Fold-DIR" (whichever was actually used) and add an ImageNet ablation comparing both.
2. **Add a controlled LLM experiment.** Either (a) re-run the baselines under the same per-layer sparsity masks used for model folding, or (b) show model folding results under a uniform sparsity allocation, so the reader can assess whether the benefit comes from the clustering or the allocation.
3. **Validate Fold-AR's independence assumption** with a simple diagnostic comparing estimated vs. data-computed cluster correlations on CIFAR10.
4. **Scope the theoretical optimality claim** to the Frobenius norm objective and explicitly note that the multi-layer extension with nonlinearities is heuristic.

## Score and Decision

Originality (6/10) — k-means clustering for within-model merging and data-free REPAIR are novel, though the general idea of neuron merging is not new. Importance (7/10) — data-free compression is practically relevant. Claims supported (5/10) — the CIFAR10 results are solid, but ImageNet variant ambiguity and LLM comparison concerns weaken the support. Soundness (5/10) — core experiments are sound but reporting is incomplete. Clarity (4/10) — the ambiguity about which method is used where is a real problem. Value to community (6/10) — the variance ratio diagnostic and Fold-AR method are useful, but the paper needs polishing.

The paper has genuine contributions (the data-free repair methods and the variance ratio analysis), but the experimental reporting is too ambiguous about which variant is used in the most important experiments (ImageNet, Fig. 6). This is not a fatal flaw — it can be fixed with clarification in the text — but in its current form the paper does not allow the reader to fully assess the claims. The LLM comparison concern further weakens what would be the most impressive result. The paper is at the borderline and needs revisions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>