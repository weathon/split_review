- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6
Now I have all the evidence I need. Let me compose the final consolidated review.

## Summary

This paper proposes BaFTA, a backpropagation-free test-time adaptation method for vision-language models (e.g., CLIP). Instead of fine-tuning text prompts via gradient descent (as TPT does), BaFTA performs online clustering in a projected embedding space to estimate class centroids, then aggregates predictions from both text embeddings and clustering centroids using Rényi entropy weighting. Experiments across 15 datasets with ViT-B/16 and RN50 backbones show consistent and often substantial gains over TPT, CoOp, PromptAlign, and CALIP, while achieving ~5× speedup.

## Strengths

1. **Backpropagation-free design delivers ~5× speedup while improving accuracy over TPT.** Section 4.2 reports BaFTA at 158.7 ms vs. TPT at 873 ms per image (ViT-B/16), while Tables 1–2 show BaFTA outperforms TPT on ImageNet (+3.17%), OOD average (+4.65%), and fine-grained average (+3.67%). This directly validates the core claim of stable and efficient adaptation.

2. **Rényi entropy aggregation systematically outperforms prior confidence-weighting schemes.** Table 5 shows Rényi entropy (α=0.5) yields 71.00% accuracy vs. 70.34% for TPT's entropy-threshold averaging and 69.43% for simple averaging on ImageNet (ViT-B/16). Table 4 further confirms BaFTA (Rényi) beats BaFTA-Avg (simple average) by 1.87% averaged over 15 datasets.

3. **Combining text-embedding and online-clustering predictions via Rényi aggregation yields additive gains over either alone.** Table 4 shows BaFTA-TE (text embeddings only, 66.70%) and BaFTA-OC (clustering only, 64.29%) individually underperform their combination in full BaFTA (68.11%) across 15 datasets. This demonstrates the claimed synergy between the two prediction streams.

4. **Multi-template prompts are leveraged without extra test-time cost.** Prompt-tuning methods (TPT) are constrained to single-template prompts; BaFTA uses CLIP's multi-template prompts at no additional inference cost. Table 1 shows the multi-template baseline (68.34% on ImageNet) exceeds single-template (66.73%), and BaFTA builds on this advantage.

5. **Consistent gains across 15 diverse benchmarks with two backbones.** BaFTA outperforms all zero-shot baselines on average across ImageNet, four OOD variants, and ten fine-grained datasets with ViT-B/16, and also with RN50. This breadth demonstrates robustness beyond a single setting.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Online clustering assignment step is not explicitly defined.** Section 3.1 (Eq. 112–114, line 116) updates centroid $w_{y_i}$ "based on its prediction $y_i$" but never states how $y_i$ is computed for the assignment. The natural interpretation (nearest-centroid: $y_i = \arg\max_j \cos(P^*(v_i), w_j)$) can be inferred from context and from Eq. (144) in Section 3.3, but the method description in Section 3.1 should state this explicitly. This is a reproducibility concern, not a methodological flaw — the algorithm is unambiguous to a reader familiar with online clustering, but an explicit equation or pseudocode would strengthen the paper.

2. **Rényi entropy formulation is ambiguously described.** Line 147 calls it "the negative Rényi Entropy" and then gives the standard Rényi entropy formula $Re(p) = \frac{1}{\alpha-1} \log \sum (p[j])^\alpha$ (Eq. 148). For $\alpha<1$, this formula already yields negative values, so calling it "negative" could be read as $-\!H_\alpha(p)$ (which would be positive) vs. $H_\alpha(p)$ (which is negative for $\alpha<1$). The math is self-consistent — the normalization in Eq. (153)–(156) handles sign correctly — but the naming should be clarified to avoid confusion. Recommend rewording to "the (negative-valued) Rényi entropy" or explicitly writing $-\!H_\alpha(p)$.

3. **The $\beta$ hyperparameter is introduced without specification.** Eq. (153)–(156) introduces $\beta$ to balance text-embedding and clustering prediction weights, but its value is never reported, nor is there any discussion of how it was set (dataset-specific default? tuned? fixed?). The ablation study (Table 6) varies $\alpha$ but not $\beta$, leaving the reader unable to assess sensitivity to this parameter.

### Trivial
None.

## Nice-to-Haves

- A brief limitations paragraph discussing scenarios where online clustering might struggle (e.g., severe class imbalance, non-i.i.d. test streams) would improve completeness but is not required for acceptance.
- Reporting variance or confidence intervals for main results (Tables 2–3) would strengthen the paper, though the large and consistent margins make this non-critical.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Fairness of comparison – cross-sample accumulation confounds the TPT comparison."** The critic argued that because TPT resets per sample while BaFTA accumulates across samples, the comparison is unfair. However, Table 4 already provides the relevant controlled ablation: BaFTA-TE (text embeddings + Rényi aggregation, no clustering, no cross-sample accumulation) achieves 66.70%, outperforming TPT (64.21%) by 2.49%. This shows that the gains do not depend on cross-sample accumulation. The critic's suggested "BaFTA-reset" experiment is effectively already present. Removed as a strawman — the concern is addressed by existing data.

- **"No statistical significance reported."** Standard practice in this benchmark line of work; not a weakness specific to this paper.

- **"Inference time analysis could be more detailed."** The paper already provides a clear breakdown: (1) fewer forward/backward passes, (2) offline text encoding. The 5× figure is credible and sufficiently documented.

- **"CALIP results missing for ViT-B/16."** The paper reports official scores from cited works; not a missing baseline.

- **"No discussion of limitations."** Nice-to-have, not a weakness.

## Novel Insights

The reviews did not surface any insight about the paper that goes beyond the paper's own claims. The key observations (online clustering as a backprop-free alternative to prompt tuning, Rényi entropy's empirical advantage, additive gains from dual prediction streams) are all present and well-supported in the paper itself.

## Suggestions

1. **Explicitly define the cluster assignment step.** In Section 3.1, add a line such as: "The prediction $y_i = \arg\max_j \cos(P^*(v_i), w_j)$ determines which centroid to update." Consider adding a brief pseudocode block for the full algorithm.
2. **Clarify the Rényi entropy naming.** Change "negative Rényi Entropy" to either "Rényi entropy (which is negative for $\alpha<1$)" or restructure to define $Re(p) = -H_\alpha(p)$ with the appropriate formula.
3. **Report the value of $\beta$ and any sensitivity analysis.** State the default value used across all experiments and, ideally, add a brief ablation of $\beta$ on one or two datasets.
