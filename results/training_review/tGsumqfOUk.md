Now I have all the evidence I need. Let me write the final consolidated review.

## Summary

This paper introduces FIPS (Factorized Inter-layer Parameter Sharing), a method that compresses the MLP modules of vision transformers (DeiT-B, Swin-L) by combining parameter sharing across layers with sparse tensor decompositions. The key idea is to share a dense low-rank basis **U** across a group of layers while each layer retains its own sparse projection matrix **V**ᵢ, initialized via SVD and optimized by minimizing block-wise reconstruction error. FIPS achieves 25–40% parameter budgets while maintaining top-1 accuracy within 1 percentage point of the uncompressed models, outperforming prior compression methods AAFM and GFM on ImageNet-1k.

## Strengths

- **Strong empirical results against established baselines:** FIPS at 40% parameter budget achieves 81.69% (DeiT-B) and 85.69% (Swin-L) top-1 accuracy on ImageNet-1k, surpassing AAFM (80.33%) and GFM (81.28%) for DeiT-B at the same budget while requiring substantially less compute for compression (Table 1). These are clean wins at identical budgets.

- **Systematic design-space exploration:** The paper performs extensive diagnostic experiments to justify each algorithmic choice — optimal sparsity placement (Fig. 1a–b), weight concatenation strategy (Fig. 1c), grouping of consecutive layers (Fig. 2a–d), and group size determination (Fig. 2c–d). The ablations (Section 5) isolate the contribution of SVD initialization (+1%), global pruning (+0.4%), and calibration data scaling, providing transparency.

- **Practical efficiency:** The local error minimization phase requires only ~1 hour on a single A6000 GPU using a small calibration set of 3840 images, making the method accessible without large-scale fine-tuning resources. The per-block gradient computation reduces memory requirements.

- **Transfer learning generalization:** FIPS-compressed models fine-tuned with RigL on downstream tasks (CIFAR-100, Flowers102, iNaturalist-2019) often match or exceed the uncompressed model's accuracy, sometimes at lower parameter budgets (Table 3), suggesting the shared bases learn reusable features.

## Weaknesses

### Fatal
None.

### Major

- **Missing baseline: independent per-layer low-rank decomposition without sharing.** The paper's central mechanism is parameter sharing (shared **U** across layers), but it never compares against the simplest alternative: decomposing each MLP independently with its own **U** and **V** at the same total parameter budget. This baseline would directly test whether sharing **U** provides any advantage over per-layer SVD compression. Without it, the reader cannot tell whether the benefit comes from sharing or from the low-rank+sparsity combination itself. The "Dense" row in Table 2 (no sparsity, with sharing) partially addresses sparsity's role but does not isolate the effect of sharing. Adding this baseline is the single most important experiment to support the paper's core claim.

### Minor

- **Global fine-tuning degrades accuracy at higher budgets without explanation.** For DeiT-B at 40% and 50% budgets, FIPS+FT (81.55, 81.54) *underperforms* FIPS without FT (81.69, 81.83). The paper notes that FT is "optional" and for "lower compression levels" but does not investigate or explain this degradation. While the main comparisons rely on FIPS (without FT) and still show strong results, this inconsistency raises questions about the stability of the two-stage pipeline and whether the local phase may be overfitting to the calibration set.

- **No variance or significance estimates.** All results are from single runs, and many claimed advantages are small (e.g., 0.41% over GFM at 40% for DeiT-B). Without multiple seeds or confidence intervals, the reliability of these differences is unclear, especially given the stochasticity of GMP/RigL and the small calibration set.

- **Baseline numbers taken from prior paper without controlled reproduction.** AAFM/GFM results are cited from CompressingTransformers (2023). It is not verified whether those baselines used the same calibration set size, optimizer hyperparameters, or tuning protocol. Protocol differences could inflate or deflate the reported advantage.

- **No ablation of the sharing constraint itself.** The ablation study (Fig. 5a) tests SVD initialization, global vs. local pruning, and scaling vectors, but never compares sharing **U** across layers against giving each layer its own **U** (at equal total parameters). This is directly connected to the major weakness above.

- **Incomplete transfer learning comparison.** GFM results at 25% budget are not available for transfer tasks, so the comparison is limited to 40% and 50% budgets where the numbers are sometimes close. The claim of "significantly better" transfer results is not fully supported across all budgets.

### Trivial
None.

## Nice-to-Haves

- Add multiple-seed runs with mean±std for key comparison points (especially Table 1 at 40% and 50%).
- Extend FIPS to attention projection matrices (Q, K, V, O) as mentioned in future work.
- Combine FIPS with quantization of the dense basis **U** for additional practical compression.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Circular" claim about group-size analysis (Section 2.3):** The critic argued that using FIPS to determine optimal group size is circular. This is standard hyperparameter tuning, not circular reasoning; almost all ML papers tune hyperparameters using the proposed method.

2. **"Overstated novelty of parameter sharing" / framing criticism:** The paper explicitly cites ALBERT and distinguishes its "fine-grained" approach from full-block reuse (lines 14–16). The claimed imprecision is not present in the paper.

3. **"Sparsity essential only supported by MSE experiments":** Table 2 (Sparsity Ablation) shows the "Dense" row (no sparsity, with sharing) achieving only 15.35% accuracy at 10% budget for DeiT-B, catastrophically worse than sparse variants. This strongly supports the claim that sparsity is essential.

4. **"FIPS at 25% outperforms GFM at 40% on Swin (85.16 vs 85.33 is lower)":** The critic's own arithmetic acknowledges this does not support the argument. The comparison is also between different budgets (25% vs 50%), not an apples-to-apples comparison.

5. **"Connection to sparsity is abrupt":** A presentation nitpick with no substantive basis.

## Novel Insights

The most interesting observation emerging from cross-referencing the reviews is that the paper's strongest evidence for its core contribution (parameter sharing) is actually indirect. The paper demonstrates that FIPS (sharing + sparsity + low-rank) outperforms AAFM and GFM, but AAFM is itself a per-layer compression method. This means the combined approach works better than per-layer alternatives, but which component — sharing or sparsity or both — drives this advantage remains unclear. The missing per-layer SVD baseline would resolve this. Additionally, the correlation between weight density and layer index (Fig. 8b, Pearson correlation of 0.922) is a genuinely useful diagnostic: it suggests that later layers are systematically harder to compress, and the global sparsity mechanism in FIPS correctly allocates more capacity to them. This finding has independent value for future compression work beyond the specific method.

## Suggestions

1. **Add the per-layer independent decomposition baseline.** Decompose each MLP module independently using SVD with matching total parameter budget (sum of ranks matches FIPS budget). Report results in Table 1. This directly tests whether the shared **U** contributes anything beyond per-layer compression. If the gap is small, the paper should reframe its contribution around the joint sharing+sparsity pipeline rather than sharing alone.

2. **Investigate and explain the FT degradation at 40%/50% budgets for DeiT-B.** Report validation curves during FT, or show that a hyperparameter search resolves the issue. If the degradation is systematic, discuss when FT is and is not recommended.

3. **Report at least 3 random seeds** for the key experimental conditions in Table 1 to establish statistical significance of the reported accuracy differences.

## Score and Decision

Based on the verified strengths and weaknesses, this paper presents a well-structured method with strong empirical results against existing baselines and thorough ablations. The most significant weakness — the missing per-layer independent decomposition baseline — is important but not fatal, as the method already outperforms prior published work. The FT degradation and single-run issues are notable but do not invalidate the core findings. With the suggested additions (particularly the per-layer baseline), the paper would make a solid contribution.

**Score: 6.5**

**Decision: Accept**

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>