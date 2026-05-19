- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have all the verification I need. Let me synthesize the final review.

## Summary

OCEBO proposes a self-distillation framework for pretraining object-centric models (slot attention) from scratch on real-world data, removing the reliance on frozen non-object-centric foundation models (DINO/DINOv2) that impose an upper bound on performance and cause poor data scalability. The method uses an EMA-updated target encoder to inject object-centric inductive biases, combined with a cross-view patch filtering mechanism to prevent slot collapse from random initialization. When pretrained on 241k COCO images, OCEBO achieves unsupervised object discovery performance comparable to prior methods that use frozen encoders pretrained on 142M images, and demonstrates scaling beyond ~16k images where prior approaches saturate.

## Strengths

- **First pretraining of object-centric models from scratch on real-world data without slot collapse.** Table 2 shows OCEBO (trained on 241k COCO images) achieves FG-ARI and mBO comparable to DINOSAUR, FT-DINOSAUR, and SPOT — all of which rely on frozen encoders pretrained on 1.3M–142M images. This directly validates that the object-centric inductive biases injected via EMA bootstrapping can make up for orders-of-magnitude less data.

- **Cross-view patch filtering prevents collapse from random target encoder initialization.** Table 1(a) shows that omitting patch filtering causes immediate collapse (d = −0.37), while the full OCEBO avoids collapse (d = 0.18). Figure 2 provides insight into the dynamics: only ~10% of patches pass the filter in early epochs, growing to ~70% by epoch 200, enabling stable bootstrapping from scratch.

- **Scalability beyond prior object-centric models.** Table 1(d) shows that scaling from COCO (118k) to COCO+ (241k) consistently improves FG-ARI on MOVi‑E (52.2 → 64.5) and EntitySeg (42.9 → 45.2), directly contrasting with the saturation at ~16k images reported by Didolkar et al. (2024) for frozen-target methods.

- **Systematic ablation isolating each component.** Table 1 separately ablates patch filtering, the object-centric loss, and mask sharpening, providing clear causal evidence that each component is necessary. The introduction of a quantitative slot-collapse measure *d* (cross-view patch similarity advantage) gives a reproducible, non-qualitative diagnostic that prior work typically assessed only with visual inspection of masks.

- **PCA visualizations (Figure 3) provide qualitative support for learned instance-level separation.** The first three principal components from OCEBO's target encoder separate a bear from a human (same semantic category), while DINOv2 groups them together — directly illustrating that EMA updates inject object-centric inductive biases into the target encoder.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Missing critical hyperparameter: k in cross-view patch filtering (Eq. 7) is never stated.** The paper defines the binary mask using *k* nearest neighbors (mutual condition) but never specifies the value of *k*. Since this mechanism is the primary collapse-prevention component and the method's sensitivity to *k* is not explored, this is a genuine reproducibility gap. The paper should report the value used and ideally include a sensitivity analysis to establish robustness.

- **The central claim about object-centric inductive biases in the target encoder lacks a fully controlled ablation.** The paper argues that EMA-updating the target encoder with object-centric inductive biases is the key advantage over frozen non-object-centric encoders. However, the main comparison (Table 2) conflates multiple differences: backbone size (ViT‑S vs. ViT‑B for FT‑DINOSAUR), decoding strategy (MLP vs. autoregressive for SPOT), and post-processing (high-resolution training). The paper honestly acknowledges these confounds, but the core hypothesis would be more directly tested by a controlled ablation: keep the same ViT‑S backbone and MLP decoder, and compare a frozen DINOv2 target encoder vs. OCEBO's EMA-updated target encoder (both trained on COCO, no mask sharpening). The existing evidence (Table 1b — removal of object-centric loss causes collapse; Figure 3 — PCA visualizations) is supportive but indirect.

- **No variance or statistical significance reported.** The main results (Tables 1 and 2) are presented as single numbers. Given stochasticity from random augmentations, random initialization, and slot attention, reporting means and standard deviations over multiple seeds (e.g., 3 runs) would help assess the method's stability, especially for the ablation experiments.

### Trivial
None.

## Nice-to-Haves

- **Ablation on the sensitivity of *k* in patch filtering.** If the method is robust to a range of *k* values, reporting this would strengthen the paper. If not, discussing the heuristic or validation used to select *k* would be helpful.
- **Larger-scale pretraining experiments.** The paper already acknowledges dataset limitations (COCO+ at 241k is modest; ImageNet is unsuitable for object-centric learning). Demonstrating the scalability trend continues with ~500k–1M curated multi-object images would further validate the approach, but this is outside the paper's stated scope.

## Removed Points

- *"Scalability evidence is positive but limited"* (Harsh Critic, Critical Issue 3). The paper's claim is specifically about scaling "well beyond a few thousand training images" compared to prior saturation at ~16k. Going from 118k→241k with consistent improvement supports this claim. The paper explicitly acknowledges dataset limitations in the conclusion. This is a scope-expansion request, not a genuine weakness.
- *"Centering and sharpening parameter tuning"* (Harsh Critic, Missing Parts). The paper states "If not mentioned, a hyperparameter has the same value as in DINO." This is standard practice; requesting documentation of tuning for default-inherited parameters adds no substantive value.
- *"Statistical significance" as Major vs. Minor.* Calibrated down from the critic's implied severity. Single-run evaluation on large-scale benchmarks is common practice in this subfield; the lack of variance reporting is a minor documentation gap, not a structural flaw.
- *Strengths from Strength Finder that are generic or about problem importance.* Removed (e.g., "this paper addressed an important problem") as they are not concrete, paper-specific evidence.

## Novel Insights

None beyond the paper's own contributions. The synthesis of reviews does not surface any observation about OCEBO that is not already articulated in the paper.

## Suggestions

1. **Specify *k* in Eq. 7** and add a brief sensitivity analysis (or rationale for the chosen value) — this is the single most actionable fix for reproducibility.
2. **Run a controlled ablation** comparing OCEBO's EMA-updated target against a frozen DINOv2 target with identical ViT‑S backbone and MLP decoder to directly isolate the effect of object-centric inductive biases.
3. **Report results over multiple seeds** (mean ± std) for the main experiments and critical ablations to quantify variability.
