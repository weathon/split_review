- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5
Now I have verified the claims against the paper. Let me write the final consolidated review.

---

## Summary

This paper introduces Sinkhorn Output Perturbations (SOP), a method that adds structured pseudo-label noise to semi-supervised segmentation by formulating output perturbation as an optimal transport problem. The approach computes a perturbed target distribution via softmax-mining (accumulating sub-maximal evidence) and beta-interpolation, then reallocates pseudo-labels to match this target using the batched Sinkhorn-Knopp algorithm. SOP imposes no architectural requirements and can be layered on top of existing strong-weak augmentation pipelines. The method achieves state-of-the-art results on Cityscapes (especially in the low-data regime of 6.25% and 12.5% labeled partitions) and competitive results on Pascal VOC 2012.

## Strengths

- **State-of-the-art results on Cityscapes low-data regimes**: On the 6.25% labeled partition with ResNet50, SOP achieves 77.1 mIoU, outperforming the previous best UniMatch (76.1) by a full point (Table 1). On 12.5%, SOP improves by 0.7 points with ResNet50 and 0.8 with ResNet101. These gains are the paper's strongest empirical contribution and directly support the core claim.

- **Principled formulation as optimal transport**: The paper casts pseudo-label perturbation as a linear program with entropy regularization, solved via batched Sinkhorn-Knopp (Equations 9–12). This provides a theoretically grounded and GPU-parallelizable alternative to ad-hoc noise injection, and cleanly separates SOP from prior work that only perturbs input or feature spaces.

- **Comprehensive ablation study**: The paper systematically investigates patch size (Table 4), beta distribution shape (Tables 5, 6), scaling parameter φ, and loss weighting λ/τ (Figure 6), providing clear evidence of how each hyperparameter controls the local–global tradeoff, perturbation diversity, and training influence. The analysis of why uniform allocation (reduced diversity) and very sharp allocation (also reduced diversity) both underperform the intermediate setting is thoughtful.

- **Controlled random noise baseline shows SOP's structure matters**: The paper demonstrates that adding 2.5% random label noise to the same baseline improves mIoU only marginally (74.8 → 75.1 on Cityscapes 12.5%), while SOP on the same baseline achieves 78.2. This controlled comparison (same baseline, same partition, similar change rates per Figure 5) directly isolates the benefit of structured over unstructured noise.

## Weaknesses

### Fatal

None.

### Major

- **UniMatch combination experiment is compromised on the 92-label partition**: The paper reports a reproduction of UniMatch on Pascal 92 labels at 71.6 mIoU versus the published 75.2 — a gap of 3.6 points. When SOP is added to this flawed reproduction, the result is 75.8. This does **not** demonstrate that SOP improves upon the true UniMatch; it shows that SOP partially compensates for a reproduction that substantially underperforms the published method. The paper acknowledges the shortfall but provides no investigation or explanation. The claim that "UniMatch can further benefit from added output perturbation" is unsupported on this partition. (The 183-label case is clean — reproduction matched, and SOP improves 78.3 → 79.0 — but the 92-label result needs resolution.)

### Minor

- **No variance or replication for any result**: All main results (Tables 1, 2, 3) and all ablations (Tables 4, 5, 6) are reported as single numbers without error bars, confidence intervals, or replication counts. Semi-supervised training is known to be sensitive to initialization and data splits. While single-run reporting is common practice in this specific sub-area, the absence is notable given that ablation hyperparameter choices produce swings of 0.5–1.0 mIoU — the same magnitude as claimed improvements. Adding ≥3 seeds for the main comparisons (at least on Cityscapes 12.5%) would substantially strengthen reliability.

- **"State-of-the-art" claim is imprecise**: The abstract and conclusion claim "state-of-the-art results on Cityscapes." On the 25% partition with ResNet50, SOP (78.4) does **not** beat AugSeg (78.8), and on 25% with ResNet101 it ties several methods. The paper's own text (Section 4.2.1) acknowledges this. The SOTA claim is accurate for the low-data partitions (6.25%, 12.5%) but should be qualified accordingly in the abstract.

- **Random noise baseline is underspecified**: The paper states random labels are injected after downsampling by 0.25× but does not specify whether the random label is drawn from a uniform distribution or the class prior (Section 4.1, Figure 4). The downsampling factor also creates a specific block-level spatial structure (4×4 pixel blocks before upsampling to ~16×16), which is itself a form of structure. Clarifying these details and reporting per-pixel random noise (different spatial structure) would help separate the effect of noise type from spatial granularity.

- **Hyperparameter search budget unstated**: The ablation shows sensitivity to φ, α/β, patch size, λ, and τ. The paper does not state how the values used in the main results were selected (h/4×w/4, φ=0.4, α=β=0.5, λ=6 for Cityscapes, λ=1.5 for Pascal, τ=0.3). If these were tuned on the same splits reported in the main results, there is a subtle overfitting concern. The paper should clarify the selection protocol.

- **Computational cost not discussed**: The batched Sinkhorn-Knopp algorithm runs per patch per iteration with multiple inner iterations. The paper should report training time overhead relative to a baseline like CPS or to the base mean-teacher without SOP, so readers can assess the practical tradeoff.

### Trivial

- The softmax-mining filter (Equation 4 uses A_{p_oh(y)}) excludes classes that never appear as the top-1 prediction in any pixel of a patch, even if they have high softmax probabilities as second choices. This design choice is mentioned but not justified. A brief rationale would help.

## Nice-to-Haves

- **Class-level mIoU analysis**: The paper hypothesizes that SOP helps rare or poorly-predicted classes by mining evidence from sub-maximal probabilities. A per-class breakdown (e.g., which classes improve on Cityscapes) would directly validate this hypothesized mechanism and substantially strengthen the narrative.
- **Ablation with multiple seeds for best/worst configurations**: Given that many ablation configurations differ by ≤0.3 mIoU, even a 3-seed replication for the best and worst settings would clarify whether differences are meaningful.
- **Negative interpolation motivation earlier**: The Discussion (Section 5) explains that positive-only interpolation causes contour-growing on low-frequency objects. Moving this motivation into the method section (3.2.3) would make the design rationale clearer upfront.

## Removed Points

These points were raised by reviewers but removed after cross-checking against the paper:

- **"No direct comparison between SOP and random pseudo-label noise"** (removed): The paper **does** provide this comparison. Section 4.1 reports the baseline at 74.8 mIoU on Cityscapes 12.5%, random noise at 75.1, and Table 1 shows SOP at 78.2 on the same partition and backbone. The control exists and shows SOP substantially outperforms unstructured noise. The critic's claim that this comparison is missing is factually incorrect.
- **"Reproducibility concerns about code/model availability"** (removed per hard rule): The abstract states code is available. Criticisms about omitted links or "not yet released" are not permitted.
- **UniMatch as a fatal flaw** (demoted from Fatal to Major): The UniMatch issue affects only the 92-label partition. On the 183-label partition, the reproduction matches published results and SOP shows a clean 0.7 mIoU improvement. The core standalone results (Table 1) are unaffected. This is a significant but confined weakness, not a structural flaw.
- **Reviewer speculation about appendix contents, missing proofs, and missing related work references**: Removed per hard rules (parser strips appendices; no external sources to verify missing references).
- **Formatting and typographical nitpicks**: Removed per hard rules (parser artifacts, not author errors).

## Novel Insights

The harsh critic's observation that the paper's framing argues output perturbations can overcome limitations of input/feature perturbations, yet the mechanism is never explicitly argued at a mechanistic level, is worth noting. The paper asserts that SOP escapes the model's current state because it "extracts evidence from sub-maximal probabilities" and can "move away from the model's current confident classifications," but it does not formalize why output perturbations should be less constrained than input or feature perturbations. A reader might ask: if both the teacher's pseudo-label and the perturbation are derived from the same model parameters, what guarantees that the perturbation represents genuinely new signal rather than a different projection of the same learned features? The paper's empirical results suggest the structure matters, but the theoretical argument could be sharper. Separately, the observation that the random noise baseline at 2.5% change rate improves performance (74.8 → 75.1) while SOP at a similar change rate achieves 78.2 provides strong evidence for the value of structure — this comparison deserves more emphasis in the paper than it currently receives.

## Suggestions

1. **Fix the UniMatch reproduction on the 92-label partition or remove the claim.** Run the published UniMatch code with the same seeds as the original paper to identify the source of the 3.6 mIoU gap. If impossible, explicitly qualify that the improvement is shown on the 183-label partition only.
2. **Add at least 3 random seeds for the main Cityscapes comparisons** (especially 12.5% with ResNet50) and report mean ± std. This is the single highest-impact addition for credibility.
3. **Qualify the "state-of-the-art" claim** in the abstract to reflect that SOP achieves SOTA on the 6.25% and 12.5% partitions and is competitive on 25%.
4. **Include a per-class mIoU table** for SOP vs. the baseline on Cityscapes to validate the hypothesized mechanism (softmax-mining helps rare classes).
5. **Report training-time overhead** of SOP relative to the base semi-supervised method.
