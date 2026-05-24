Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces WASI (Weight-Activation Subspace Iteration), a method that jointly compresses both weights and activations into low-rank subspaces during fine-tuning of transformer models, aimed at reducing memory and computation for on-device training. The approach combines activation subspace iteration (building on prior ASI work) with a novel Weight Subspace Iteration (WSI) that leverages the observation that weight subspaces remain stable across fine-tuning iterations. Experiments on ViT, SwinT, and TinyLlama demonstrate memory reductions up to 62× and FLOPs reductions up to 2× while maintaining accuracy, with a 1.4× speedup measured on a Raspberry Pi 5.

## Strengths

1. **Novel joint weight-activation compression framework**: WASI is the first method to simultaneously apply subspace iteration to both weight tensors and activation maps during transformer training. This unification of two previously separate lines of work (weight decomposition via SVD-based methods and activation compression via ASI) is a legitimate and well-motivated contribution.

2. **Real-world device latency improvement**: The paper reports a ~1.4× speedup for both training and inference on a Raspberry Pi 5 (Fig. 8), measured at ε=0.9 on ViT with CIFAR-10. This concrete on-device measurement directly supports the paper's core claim of enabling practical transformer fine-tuning on resource-constrained hardware — a type of evidence many comparable compression papers lack.

3. **Strong efficiency-accuracy trade-offs across multiple architectures**: WASI matches vanilla accuracy on SwinT while cutting memory by up to 62× and FLOPs by 1.5× (Section 4.3). The method is validated on three fundamentally different architectures (ViT, SwinT, TinyLlama) spanning vision and language tasks, demonstrating reasonable generality.

4. **Detailed complexity analysis**: Section 3.4 provides derivations of compression rates and speedup ratios for both training and inference, showing how WASI's gains scale with model size and rank. This analytical framing helps guide parameter selection and grounds the empirical results.

## Weaknesses

### Major

1. **Algorithm 1 (WSI) description contains an inconsistency that needs clarification**: At iteration 0, L is initialized as UΣ (non-orthonormal columns scaled by singular values) and R as V^T (orthonormal rows). In subsequent iterations, the algorithm computes R^T = W^T·L_{t-1} (so R = L_{t-1}^T W) and then updates L = Orthogonalize(W·R^T). After this update, L is orthonormal, but R was computed using the *previous* L_{t-1} and is never recomputed to be consistent with the new L. For the factorization W ≈ LR to be accurate, R should ideally satisfy R = L^T W given the new L. The paper does not analyze the approximation error introduced by this mismatch, nor does it explain under what conditions the stale R remains adequate. While the stability assumption (L_t ≈ L_{t-1}) may make the error small, the algorithm as presented deviates from standard subspace iteration practice and requires justification or correction for the method to be reproducibly trusted.

2. **Headline resource savings are reported for MLP linear layers only, without qualification in the abstract**: The paper states (Section 4.1) that measurements "focus on linear layers within multi-perceptron blocks" and promises extended results with attention layers in an appendix (stripped). However, the abstract and conclusion claim "up to 62× memory reduction" and "up to 2× FLOPs reduction" without this qualification. In ViT, attention projections (Q, K, V, output) account for a substantial fraction of parameters and FLOPs; excluding them inflates the headline savings. The main text should clearly state what portion of the model is covered and ideally report total model-level numbers.

### Minor

1. **Stability evidence for weight subspaces is thin**: The key hypothesis — that weight subspaces remain stable during fine-tuning — is supported by a single heatmap (Fig. 3a) showing singular values of one layer (W₆) at one ε value (0.8). No quantitative measure (e.g., subspace cosine similarity, normalized projection Frobenius norm) is provided, nor is the stability shown across multiple layers, datasets, or ε values. Given that this claim is central to WSI's efficiency advantage, stronger validation would significantly increase confidence.

2. **WSI vs. SVD comparison (Fig. 3b) lacks robustness**: The claim that WSI achieves "35% higher accuracy" at the same FLOPs budget is based on a single model (ViT) on a single dataset (Pets) with no error bars or multiple trials. While the qualitative direction (WSI is more FLOP-efficient than per-iteration SVD) is expected from subspace iteration theory, the specific 35% figure is presented without uncertainty quantification and would benefit from verification across more settings.

3. **TinyLlama experiment is limited**: Only the last 5 layers are fine-tuned, only one ε value (0.1) is tested, and the accuracy difference between WASI and vanilla (~0.6% on BoolQ) is within likely noise. The extreme compression ratios (953× activation memory, 30× weight memory) come from this aggressive single setting. A sweep over ε values and fine-tuning of more layers would strengthen the LLM generality claim.

4. **On-device evaluation covers only one model/dataset combination**: The Raspberry Pi 5 experiment tests only ViT on CIFAR-10. The paper does not verify that the same accuracy achieved in simulation is reproduced on the device, nor does it test other models (SwinT, TinyLlama) or hardware platforms.

5. **No dedicated limitations or failure-mode discussion**: The paper does not discuss when WASI might underperform — e.g., when the subspace stability assumption breaks (very different downstream tasks), when the subspace iteration overhead dominates for high ranks, or when activation compression causes significant gradient error propagation. A limitations section would improve completeness.

6. **SVD-LLM compression matching procedure is underspecified**: The paper states that "the same compression ratios are applied to SVD-LLM" but does not explain how this matching is performed (e.g., matched by rank, by parameter count, or by FLOPs). This makes the comparison harder to interpret.

### Trivial

- The claim of being "the first method for efficient model-activation-decomposition-aware training" is self-characterizing and could be toned down to "the first method to jointly..." since the novelty is in the combination rather than a wholly new category.
- The y-axis of Fig. 3b would benefit from explicit labels in the caption or figure itself.

## Nice-to-Haves

- A theoretical bound on the WSI approximation error or convergence of the subspace iteration would raise confidence in the method.
- A sensitivity study of the ε threshold across more values and its effect on convergence speed would help users configure the method.
- A direct comparison with LoRA (even if the paper explains why LoRA is not a primary competitor) on training memory alone would help readers situate WASI relative to the most widely used PEFT method.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"WSI vs SVD comparison based on a single layer"** — The reviewer claimed this comparison was for "a single layer," but the paper clearly states the experiment is fine-tuning the full ViT model on Pets (Fig 3b). The comparison is for the full model, not a single layer. Removed as factually incorrect.
- **Generic reproducibility concerns about appendix or missing artifacts** — Several points about missing appendix content (e.g., "the appendix may specify X but...") are removed per the instructions that the parser strips appendices from all papers.
- **"First method" claim as a weakness** — The reviewer's criticism that this is "overstated" is a minor phrasing preference; the paper's actual contribution (joint compression) is clear. Demoted to trivial note.
- **"Missing y-axis labels" on Fig. 3b caption** — The caption explicitly states "Top1 Validation Accuracy (%) vs FLOPs," so the labels are described. Likely a parser artifact from the figure rendering.
- **LoRA as a missing essential baseline** — The paper discusses LoRA in related work and explains why it is not directly comparable (does not reduce inference cost). SVD-LLM, which uses LoRA adapters, is included as a baseline. LoRA inclusion would be informative but not essential. Moved to Nice-to-Haves.
- **Request for theoretical guarantees as a weakness** — Demoted to Nice-to-Have, as the paper is primarily empirical and does not claim theoretical contributions.

## Novel Insights

The key insight that emerges from the reviews — beyond the paper's own contributions — is that the stability assumption for weight subspaces (claimed from prior work and verified in one narrow setting) is simultaneously the method's biggest enabler and its biggest vulnerability. If this stability holds broadly, the lightweight WSI update is well-justified; if it fails in some regimes (e.g., large distribution shifts, higher learning rates, or deeper layers), the approximation error could compound. A targeted stress test of the stability assumption across diverse fine-tuning scenarios would be the single most impactful addition. The reviews also surface a tension between the paper's practical motivation (on-device deployment) and the partial evaluation scope (MLP-only savings) — bridging this gap is important for the claimed real-world applicability.

## Suggestions

1. **Clarify Algorithm 1**: Either correct the WSI update to recompute R after L is updated, or provide an explicit error analysis showing why using the stale R is safe under the stability assumption. A one-line proof-of-concept on a single layer verifying that ∥W−LR∥ does not diverge across iterations would build trust.
2. **Report full-model resource numbers**: Recompute the memory/FLOPs curves with attention layers included (or at least state the breakdown clearly in the abstract and main text). If attention layers are included in the appendix, reference the all-inclusive numbers prominently.
3. **Strengthen the stability validation**: Add quantitative subspace similarity metrics (e.g., ∥L_t^T L_{t-1}∥_F^2 / K) across multiple layers, datasets, and ε values. Run the WSI vs. SVD comparison with error bars across 3+ seeds.
4. **Expand the TinyLlama experiment**: Vary ε, report vanilla accuracy in the same limited setting, and ideally compare with LoRA on the same layers.
5. **Add a limitations section**: Discuss regimes where WASI may underperform and how practitioners should choose ε.

## Score and Decision

I conducted calibration in three rounds:

**Round 1 (Bracketing)**:  
- Weak band (<3.5): Papers like "On-Device Transfer Learning based on Mixed Precision Partitioning" (2.50) and "HoLoRA" (3.00) — weaker papers on related topics. Our paper is clearly stronger than these.
- Middle band (3.5–7.5): Papers like "Differentiable Learning of Generalized Structured Matrices" (5.67, accept), "OATS" (6.25, accept), "RaNA Adapters" (6.00, accept), "ASVD" (6.25, reject), "Adapprox" (6.40, reject), "LQ-LoRA" (6.75, accept), "AdaRankGrad" (7.00, accept).
- Strong band (>7.5): Papers like "Cut Your Losses" (8.50), "Scaling Laws for Precision" (8.00) — clearly stronger, with more polished execution or broader impact.

**Round 1 bracket**: 4.5–7.0 (the paper is clearly above the weak band but below the strong band).

**Round 2 (Narrowing)**:  
- Inside (4.5, 6.5): "Compress then Serve" (5.25), "Differentiable Structured Matrices" (5.67), "Training with Low-Dim Error Feedback" (5.50), "OATS" (6.25).
- Inside (5.5, 7.5): "Adapprox" (6.40, reject), "AdaRankGrad" (7.00, accept), "ASVD" (6.25, reject), "LQ-LoRA" (6.75, accept), "Train Small, Infer Large" (6.20, accept).

**Comparison with anchors read in full**:

| Anchor | Score | Comparison |
|--------|-------|------------|
| Differentiable Structured Matrices (pAVJKp3Dvn) | 5.67 | WASI has real device results they lack, but less theoretical polish. **WASI is slightly stronger.** |
| ASVD (HyPofygOCT) | 6.25 | WASI has on-device latency they lack, but ASVD's methodology is cleaner. **Comparable.** |
| RaNA (uAtDga3q0r) | 6.00 | RaNA is cleaner methodologically but lacks wall-clock speed measurements. **Comparable, WASI slightly behind on clarity.** |
| Sine-Activated LR (cWGCkd7mCp) | 7.00 | Stronger theoretical foundation and broader evaluation. **WASI is weaker.** |
| LQ-LoRA (xw29VvOMmU) | 6.75 | Cleaner methodology, strong results. **WASI is weaker.** |

Based on these comparisons, the paper lands between the 5.67 and 6.25 anchors — closer to the lower end due to the algorithmic clarity issue and the MLP-only reporting concern. **Final score: 5.5.**

This paper presents a novel and well-motivated approach to enabling on-device transformer training through joint weight-activation subspace compression, backed by concrete device measurements and meaningful efficiency gains across multiple architectures. However, the algorithmic description of its core component (WSI) contains an unresolved inconsistency, and the headline efficiency numbers do not account for attention layers — two issues that undermine the reliability and transparency of the claims until clarified. The paper would benefit from revision and re-review.

**Decision**: Reject

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>