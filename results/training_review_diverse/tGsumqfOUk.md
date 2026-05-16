Now I have verified all claims against the paper. Let me write the final consolidated review.

## Summary

The paper introduces FIPS, a parameter-sharing algorithm for transformer MLP layers that combines a shared low-rank basis (initialized via SVD) with sparse projection matrices, optimized by minimizing block-wise reconstruction error. Experiments on DeiT-B and Swin-L show FIPS achieves strong compression (25–40% parameter budgets) with minimal accuracy loss, outperforming AAFM and GFM baselines on ImageNet-1k.

## Strengths

1. **Sparsity is convincingly shown to be essential for effective parameter sharing.** The ablation in Table 3 (labeled "tab:sparsity_ablation") shows Dense decomposition achieves only 15.35% accuracy at 10% budget on DeiT-B vs. 70.04% with GMP-based FIPS, and this pattern holds across budgets. Figures 1a–b systematically investigate which factor should be sparsified and at what level, providing an evidence-driven justification for the algorithm's design.

2. **Strong empirical results on ImageNet-1k, outperforming strong baselines.** At 40% parameter budget, FIPS achieves 81.69% top-1 on DeiT-B, exceeding AAFM (80.33%) and distillation-assisted GFM (81.28%). For Swin-L, FIPS+FT reaches 82.13% at 10% budget. These results are the paper's primary empirical contribution and are clearly presented in Table 1.

3. **Principled, evidence-based recipe for designing parameter-sharing groups.** The paper systematically investigates concatenation strategies (Figure 1c), grouping of consecutive layers (Figures 2a–b), and optimal group size (Figures 2c–d), with the ablation confirming the importance of SVD initialization (1% drop with random init, Figure 3a) and global pruning (0.4% improvement over local pruning). This systematic approach provides reproducible design guidelines.

4. **Efficient optimization requiring minimal compute.** The local error minimization stage uses only 30 batches × 128 samples (3840 images) and 20 epochs, taking <1 hour on an A6000 GPU. Figure 3c shows increasing data or training length yields marginal gains (<0.1%), validating the efficiency of the proposed approach.

5. **Theoretical analysis of storage and computation trade-offs.** The paper derives a closed-form expression for storage savings (*F_sparse = 17F/(16D)*) and discusses two MAC implementation strategies (low-rank vs. full-rank materialization), connecting the algorithm to deployment considerations.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaimed novelty contradicted by the paper's own citations.** The conclusion states: "to the best of our knowledge for the first time, that inter-layer parameter sharing enables significant compression in Transformers." Yet the related work (line 329) cites MiniViT (2022), which introduces "Weight Multiplexing" — sharing parameters across ViT MLP modules with distillation. The paper also cites TBasis and Structured Multi-Hashing, both of which explore parameter sharing. While FIPS differs from MiniViT (sparse decomposition vs. full-weight multiplexing, no distillation required), the "first" claim is not supportable given the paper's own references. This is a framing error that overstates the contribution. The authors should remove or qualify the "first" claim and explicitly differentiate FIPS from MiniViT (e.g., no distillation, sparsity-enabled allocation of capacity).

### Minor

2. **Global finetuning (FT) shows inconsistent benefit without discussion.** At 40% and 50% parameter budgets on DeiT-B, FIPS+FT *underperforms* FIPS without FT (81.55 vs. 81.69 at 40%; 81.54 vs. 81.83 at 50%). The paper describes FT as "for best results, especially at lower compression levels" (line 115), which aligns with the data (FT helps at 10% and 25%), but it provides no explanation for why FT degrades performance at moderate budgets. The differences are small (<0.3%) and may be within noise, but the absence of discussion weakens the claim that FT is a reliable component. A brief explanation (e.g., overfitting to the local objective, interaction with the sparsity pattern learned during local optimization) would resolve this.

3. **No measured runtime, throughput, or actual memory numbers despite deployment framing.** The introduction motivates compression for "deployment on resource-constrained devices" (line 13), and the paper dedicates a subsection to memory/latency analysis. Yet no actual runtime measurements are reported — not on GPU, CPU, or edge hardware. The theoretical storage analysis is valuable, but the paper does not plug in its own experimental settings (e.g., 40% budget, 75% sparsity → 25% density) to compute whether actual storage is reduced. (Plugging F=0.4, D=0.25 into F_sparse = 17F/(16D) yields ~1.7× — storage *increases* with a bitmask.) The paper states the condition for savings (F/D < 0.94) but does not discuss that many of its own operating points violate this. Adding measured model sizes (in MB) and forward-pass latencies would directly support the deployment framing and clarify where the method offers practical benefits.

4. **Transfer learning evaluation lacks AAFM baselines and has inconsistent settings.** Table 2 compares FIPS+RigL FT against GFM (from prior work) but does not include AAFM. Since AAFM is the primary non-distillation baseline on ImageNet-1k, its omission from transfer tasks is a gap. Additionally, the GFM numbers are from a different paper; it is unclear whether the same training hyperparameters (epochs, learning rate schedule, augmentation) were used. The authors should confirm whether the comparison is like-for-like or note any differences.

5. **Missing τ hyperparameter value for neuron growth.** The hybrid initialization method (lines 313–315) uses a hyperparameter τ that was tuned via a sweep and found to outperform alternatives by 1–2%, but the optimal τ value (or range) is not reported. This is a small but unnecessary reproducibility gap.

### Trivial
- The paper has no limitations section discussing when FIPS might fail (e.g., models with few layers, attention module compression).
- The related work paragraph on parameter sharing describes MiniViT, TBasis, and Structured Multi-Hashing without positioning FIPS relative to them. A brief differentiating sentence would help.
- The "cache hits" claim (line 15) is hedged ("could, in theory") but a citation for the general principle would strengthen the motivation.

## Nice-to-Haves
- A forward-pass latency comparison on a representative device (GPU or CPU) would directly support the deployment motivation.
- Computing actual memory savings (in MB) for the paper's specific compression settings would clarify where FIPS offers storage benefits vs. where it trades storage for accuracy.
- A brief explanation of why global finetuning degrades at moderate budgets (even a hypothesis) would improve the paper's completeness.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Criticism that transfer learning table "does *not* include the baseline AAFM/GFM on those tasks"** (partially removed): GFM *is* included in the transfer learning table (Table 2). Only AAFM is missing. The corrected version appears in Minor weakness #4 above.
- **"Ablations section structure is misleading"**: This is a presentation/pedantic criticism about section naming. The section contains ablations, sensitivity sweeps, and alternative sparsity techniques — all relevant content. No substantive issue.
- **"Scaling vectors ablation could be streamlined"**: Minor presentation preference, not a weakness of the method or evidence.
- **"Claim about cache hits asserted without citation"**: The paper uses hedging language ("could, in theory"), and citing a survey on the general benefits of parameter sharing would be reasonable but the current language is not a factual error.

## Novel Insights
The reviews surface one genuinely novel observation beyond the paper's own contributions: the finding that global finetuning (FT) can *hurt* performance at moderate compression budgets (40–50% parameters) while helping at low budgets (10–25%) is unusual and deserves explicit investigation. Most compression papers assume FT either helps universally or is not applied; this non-monotonic behavior could point to an interesting interaction between the sparsity pattern learned during local optimization (via GMP) and the dynamic sparse training used during global FT (via RigL), where changing the sparsity pattern at moderate budgets disrupts an already-good local solution. The paper does not discuss this, but the data in Table 1 clearly shows it.

## Suggestions
1. **Correct the "first" claim.** Either remove it or replace with a precise statement such as: "to the best of our knowledge, the first demonstration that sparse tensor decomposition enables parameter sharing for significant compression in Transformers without requiring distillation."
2. **Add a brief discussion of global FT's inconsistent behavior** at moderate budgets — either explaining it or acknowledging it as a limitation.
3. **Report the optimal τ value** from the hyperparameter sweep.
4. **Add a limitations paragraph** discussing scope (MLP-only, ViT-specific group sizes) and failure modes.

## Score and Decision

This is a solid method paper with a sound core idea, thorough ablations, and compelling empirical results. The main weaknesses are a correctable novelty overclaim (major but not fatal to the contribution) and several gaps in evaluation scope (no latency numbers, missing AAFM on transfer, τ not reported). These do not undermine the paper's core empirical contribution — FIPS demonstrably works well. With revisions, the paper would be significantly strengthened.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>