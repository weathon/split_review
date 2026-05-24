Now I have enough calibration data. Let me synthesize the final review.

## Round 1 Bracket
- **Weak anchors**: channel-wise quantization (4.00) — evaluation fairness concerns, fundamentally flawed motivation to some reviewers
- **Middle anchors**: BSQ-ViT (5.75) — new quantization method, missing some comparisons; ImageFolder (6.25) — novel tokenizer, some components from prior work
- **Strong anchors**: Rotation Trick (8.00) — elegant, well-motivated, extensive experiments

**Initial bracket: 5.0–7.0.**

## Round 2 Narrowing
Read anchors: variable-length tokens (5.75), SEED tokenizer (6.33), plus earlier BSQ-ViT (5.75) and ImageFolder (6.25).

VQ-Transplant has broader experiments than BSQ-ViT (5 VQ methods × 4 datasets), comparable novelty to ImageFolder, and stronger practical motivation than both. However, it has a significant missing baseline (decoder-only adaptation of original VAR) that BSQ-ViT and ImageFolder don't suffer from as acutely. SEED (6.33) is more ambitious but has more unclear design choices. VQ-Transplant sits between BSQ-ViT and ImageFolder: **final score 6.0**.

---

## Summary
This paper proposes VQ-Transplant, a framework that enables plug-and-play substitution of vector quantization (VQ) modules into frozen pre-trained visual tokenizers, followed by lightweight decoder adaptation (5 epochs on ImageNet-1k). The key insight is decoupling VQ exploration from costly end-to-end tokenizer retraining. The authors also introduce MMD-VQ, a VQ method using maximum mean discrepancy for distributional alignment. When transplanting MMD-VQ into a pre-trained VAR tokenizer, VQ-Transplant achieves 0.81 rFID on ImageNet-1k (vs. 0.92 for the original VAR) with 21.8× less training compute.

## Strengths
- **Resource-efficient VQ exploration**: The paper convincingly demonstrates that swapping VQ modules into a frozen pre-trained tokenizer with brief decoder adaptation yields reconstruction quality matching or exceeding the original, at a fraction of the cost. Table 1 quantifies this: 22 hours on 2 A100s vs. 60 hours on 16 A100s for the original VAR, a 21.8× speedup in GPU-hours. This directly addresses a real practical bottleneck in VQ research.

- **Thorough empirical validation of decoder adaptation's role**: Table 3 and Figure 2 clearly show that VQ substitution alone degrades reconstruction (e.g., MMD VAR K=8192 rFID drops to 1.49 after substitution) and that decoder adaptation restores and surpasses original quality (rFID 0.81). This two-stage dynamic is consistently demonstrated across all five VQ methods tested.

- **Broad compatibility across VQ methods and datasets**: The framework is validated with five distinct VQ algorithms (Vanilla, EMA, Online, Wasserstein, MMD) in both multi-scale (Table 3) and fixed-scale (Table 7) configurations. Cross-dataset generalization to FFHQ, CelebA-HQ, and LSUN-Churches (Tables 8–10) — datasets structurally distinct from the VAR tokenizer's original OpenImages training distribution — shows strong transfer, with Wasserstein VQ achieving rFID 1.21 on FFHQ, outperforming all listed baselines.

- **Well-executed ablation on adaptation duration**: Tables 4–5 and Figure 3 track rFID across 20 adaptation epochs, showing consistent improvement (MMD VAR K=8192: rFID 0.81 at epoch 5 → 0.74 at epoch 20), confirming that extended adaptation converts reduced quantization error into better reconstruction.

- **Honest comparison with from-scratch training**: Table 6 shows that from-scratch MMD VAR training for comparable or longer GPU-hours yields poor reconstruction (rFID 1.26–1.40), directly validating the necessity of decoupling VQ exploration from full retraining.

## Weaknesses

### Fatal
None.

### Major
- **Missing baseline: decoder-only adaptation of the original VAR tokenizer.** The paper claims VQ-Transplant achieves "superior reconstruction fidelity" over the original VAR tokenizer (0.81 vs. 0.92 rFID). However, the experiments do not include a control where the *original* VAR tokenizer's decoder is adversarially fine-tuned on ImageNet-1k for 5 epochs while keeping its native multi-scale VQ module frozen. Without this baseline, it is impossible to determine whether the rFID improvement from 0.92 to 0.81 comes from the transplanted MMD-VQ module or simply from the decoder adaptation protocol applied to any VQ module — including the original one. The same gap affects the cross-dataset experiments (Section 5.3): we cannot disentangle the effect of new VQ methods from the effect of decoder adaptation on out-of-domain data. This baseline is essential to substantiate the "superiority" claims; without it, the evidence only supports that VQ-Transplant *matches* original quality at lower cost — which is still valuable but requires recalibrated claims. The paper's primary contribution (the framework for cheap VQ exploration) is not invalidated by this omission, but the performance-superiority framing is not fully supported.

### Minor
- **MMD-VQ offers modest gains over Wasserstein VQ.** Across tables, MMD-VQ and Wasserstein VQ produce nearly indistinguishable results. For instance, in Table 3 (adaptation, K=8192): MMD VAR achieves rFID 0.81 vs. Wasserstein VAR's 0.83 — a difference of 0.02. The paper correctly notes MMD-VQ makes no parametric assumptions, but the practical benefit over Wasserstein VQ is small on these benchmarks. This is not a flaw in the method, but it means the secondary contribution carries limited weight.

- **No discussion of encoder freeze limitations.** The framework freezes the encoder, meaning the latent feature distribution cannot adapt to suit a new VQ method that might benefit from a different representation. This implicit limitation is not acknowledged or discussed anywhere in the paper.

### Trivial
- The code link in the abstract is a placeholder (not functional in the reviewed manuscript). Should be corrected for the camera-ready version.

## Nice-to-Haves
- Reporting standard deviations of rFID across multiple runs would clarify whether observed gaps (e.g., 0.81 vs. 0.83) are statistically meaningful.
- A deeper analysis of *why* MMD-VQ improves compatibility beyond raw metrics, e.g., visualization of learned codebook distributions or breakdown of loss components during adaptation.
- A more explicit discussion of the cost-performance trade-off as adaptation epochs increase (cost advantage narrows from 21.8× toward something smaller with 20 epochs).

## Removed Points
These points are flagged as having been removed. Treat them with caution.

- **"Missing ablation: decoder finetuning without VQ substitution" — partially retained as Major.** The core concern about attribution of performance gains is valid and retained above. However, the harsh critic's framing that this is "structural" and "fatal" was demoted to Major because the paper's primary contribution (the VQ-Transplant framework for cheap VQ exploration) does not depend on the superiority claim; the speedup and resource savings are independently demonstrated. The framework still enables rapid VQ iteration even if the original decoder could be fine-tuned to similar quality.

- **"Code link not functional" — removed as formatting artifact.** Per hard rules, availability concerns about cited materials are parser issues.

- **"The paper would benefit from deeper analysis of why MMD-VQ improves compatibility" — moved to Nice-to-Haves.** This is a suggestion for strengthening, not a weakness.

- **Strength Finder: "Decisive role of decoder adaptation" — kept but note that this interacts with the missing baseline concern.** The adaptation clearly improves metrics, but without the control, the improvement cannot be fully attributed to the VQ transplant specifically.

- **Strength Finder: "Strong cross-dataset generalization" — kept with caveat.** The results are impressive but attribution of gains to VQ transplant vs. decoder adaptation on new domains is confounded.

## Novel Insights
The paper's key insight — that VQ module development can be decoupled from expensive end-to-end tokenizer training through a simple transplant-and-adapt protocol — is practically valuable and not obvious from prior work. The empirical finding that decoder-quantizer mismatch is the primary bottleneck after VQ substitution, and that it can be resolved with surprisingly little decoder adaptation (5 epochs), is a concrete, actionable observation that could influence how the community approaches VQ research. The demonstration that distribution-alignment-based VQ methods (Wasserstein, MMD) are particularly compatible with this transplant paradigm also provides useful guidance.

## Suggestions
- Add the decoder-only fine-tuning baseline for the original VAR tokenizer on ImageNet-1k and cross-domain datasets. This is the single highest-impact addition: if the original decoder with native VQ also improves to ~0.81 rFID, reframe the contribution around cost-effective matching rather than superiority; if it does not improve significantly, the current superiority claims are validated.
- Discuss the implicit limitation of freezing the encoder (latent space cannot adapt to suit new VQ methods) and when this might matter.
- Consider reporting confidence intervals or standard deviations for key rFID comparisons.

## Score and Decision

### Anchor comparison summary
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| IqGVIU4rvM (VQ-VAE + diffusion) | 2.50 | 1 | Significantly weaker; narrower scope, less novel |
| YlWvQSBCgl (Channel-wise VQ) | 4.00 | 1 | Weaker; fundamental evaluation concerns, less practical |
| yGnsH3gQ6U (BSQ-ViT) | 5.75 | 1,2 | Comparable; novel quantizer but narrower experiments, missing comparisons |
| mb2ryuZ3wz (Variable-length tokens) | 5.75 | 1,2 | Comparable; novel idea but limited baselines, mixed results |
| QE1LFzXQPL (ImageFolder) | 6.25 | 1,2 | Slightly stronger; more novel core idea, but narrower experiments |
| 0Nui91LBQS (SEED tokenizer) | 6.33 | 2 | Slightly stronger; more ambitious scope but more design complexity |
| GMwRl2e9Y1 (Rotation Trick) | 8.00 | 1 | Clearly stronger; more elegant, better motivated, consistently high reviews |

VQ-Transplant sits between BSQ-ViT (5.75) and ImageFolder (6.25): broader experiments than BSQ-ViT, more practical framing, but held back by a significant missing baseline that weakens the superiority claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>