## Summary

OF-Diff proposes a layout-to-image (L2I) diffusion framework for remote sensing that combines (1) an Enhanced Shape Generation Module (ESGM) to extract shape priors from category labels, (2) an online-distillation strategy with dual decoders (shape-feature and mix-feature) to learn image features without requiring real-image patches at inference, and (3) DDPO fine-tuning for diversity. Experiments on DIOR, DOTA, and HRSC2016 across 13 metrics show consistent improvements over AeroGen, CC-Diff, LayoutDiffusion, and GLIGEN, with notable per-class detection gains for difficult categories (e.g., airplane +8.3% mAP₅₀).

## Strengths

- **Online-distillation architecture cleanly removes the need for real-image patches at inference.** The dual-decoder design (Eq. 4-6) trains the shape-feature SD decoder to match the mix-feature SD decoder's output via a consistency loss \( \mathcal{L}_c \), so that at sampling time only the shape decoder and frozen ControlNet are used (Figure 3(b), Section 3.2). This is a concrete architectural improvement over CC-Diff, which requires full image patches at inference.

- **Large per-class detection gains on the hardest categories.** On DIOR, mAP₅₀ improves by 8.3% for airplane, 7.7% for ship, and 4.0% for vehicle — among the most morphologically complex remote sensing classes — after augmenting training with OF-Diff images (Figure 5(a), Section 4.3). These are the largest per-class improvements across all compared methods.

- **Best shape-fidelity across all five metrics on both datasets.** OF-Diff achieves the best IoU, Dice, Chamfer Distance, Hausdorff Distance, and SSIM on DIOR and DOTA (Table 2), with clear margins (e.g., IoU 0.1009 vs. 0.0891 for next-best CC-Diff on DIOR).

- **ESGM's contribution is cleanly isolated by ablation.** Adding ESGM alone boosts YOLOScore from 41.20 to 55.08 — a >10-point gain (Table 4, rows 1→2). This demonstrates that the shape-prior extraction mechanism is the primary driver of layout consistency.

- **Strong generalization to unseen layouts.** On the DIOR validation set (layouts not seen during training), OF-Diff obtains the best FID (24.18 vs. 28.62 for second-best AeroGen) and mAP₅₀ (56.65 vs. 55.11), despite a known edge case where CC-Diff scores higher on YOLOScore (Table 3).

## Weaknesses

### Fatal

None. No verified issue invalidates the paper's core claims.

### Major

- **Table 4 has an unexplained duplicate row.** Two rows carry ESGM✓, Lc✓, DDPO✓ but report drastically different FID values (37.98 vs. 24.92) and other metrics. The text states that ablation experiments "were conducted based on the absence of caption input," which suggests the duplicate may correspond to a with/without caption variable, but this is never stated in the table or caption. As presented, the table is not interpretable — a reader cannot determine what each row corresponds to, which undermines confidence in the reported contributions of individual modules.

- **DDPO reward function is underspecified in the main text.** Equation (9) defines \( r(\mathbf{x}_0, c) = (KNN(\mathbf{x}_0, \mathbf{x}_0) - \omega KL(\mathbf{x}_0, \mathbf{x}_0')) \). The notation \( KNN(\mathbf{x}_0, \mathbf{x}_0) \) would conventionally be a distance from a point to itself (trivially zero or one), and the KL divergence between two individual images is not defined without specifying the distributions used. The paper says "implementation details are in Appendix A.2," which is stripped, but the main paper should provide a self-contained, reproducible definition. Since DDPO fine-tuning is presented as a contribution, this is a meaningful gap.

### Minor

- **The "without real-image references" framing is imprecise.** The ESGM constructs a mask pool from training-set images, and during sampling it selects shapes from this pool (Section 3.3: "it selects enhanced shapes from a lightweight mask pool collected during or after training"). These shapes are derived from real image data via RemoteCLIP+RemoteSAM. The genuine advance over CC-Diff is not "zero real-data reference" but **"patch-free inference"** — the model uses shape priors rather than full image crops. This distinction should be clarified.

- **Unknown-layout results: CC-Diff outperforms OF-Diff on YOLOScore.** In Table 3, CC-Diff achieves YOLOScore 51.74 vs. OF-Diff's 49.59. While OF-Diff leads decisively on FID (24.18 vs. 49.92), mAP (33.02 vs. 32.49), and most other metrics, this reversal is not discussed. The paper should acknowledge and explain when and why the competing method achieves better layout consistency on unseen layouts.

- **Stop-gradient design on \( c_s \) in Eq. (3) is not ablated.** The paper states it is "to serve as a stable anchor point" (citing Chen & He 2021) but does not show what happens without it. Since this is a nontrivial design choice (stopping gradients on one branch while mixing with another), an ablation would strengthen confidence.

- **DDPO's marginal additive benefit.** The full pipeline (row 8 in Table 4) yields YOLOScore 58.99 vs. row 5 (ESGM+Lc, no DDPO) at 57.83, and mAP₅₀ 54.44 vs. 54.31. The individual DDPO gain is small, and the interaction where DDPO without ESGM (row 4) gives mAP₅₀ 53.41 (better than baseline but worse than ESGM alone) is not discussed. The paper should address why DDPO helps less when ESGM is already present.

### Trivial

- Equation (9) notation \( KNN(\mathbf{x}_0, \mathbf{x}_0) \) is almost certainly a notational error (likely intended to be a distance to the real-data manifold, e.g., \( \sum_{\mathbf{x}' \in \text{NB}(\mathbf{x}_0)} \|f(\mathbf{x}_0) - f(\mathbf{x}')\| \)).

## Nice-to-Haves

- Ablate the stop-gradient on \( c_s \) in Eq. (3) to demonstrate its necessity.
- Report mask pool size and discuss behavior when encountering truly novel shape categories.
- Provide the number of DDPO fine-tuning steps, reward normalization, and baseline value details.
- Include cropped instance visualizations with edge maps in the main paper (currently relegated to Appendix A.8).
- Analyze why DDPO helps less when ESGM is already present (non-additive interaction).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"ESGM uses RemoteCLIP to generate a textual description from a cropped region, which is non-trivial, and no examples provided"** — The paper does not claim this as a core contribution; it is a standard application of RemoteCLIP for mask generation. The presence/absence of caption examples is a minor presentation point and the reviewer is overstating its importance.
- **"Circular evaluation risk from metrics using models trained on the same distribution"** — The paper partially counters this with downstream detection on held-out test sets, which is standard practice. This is a generic concern that applies to nearly all generative evaluation; not specific enough to retain.
- **"Shape augmentation could produce unrealistic masks"** — Pure speculation without evidence. The quantitative results (Table 2) show strong shape fidelity, which undercuts this concern.
- **"Comparison with AeroGen on unknown layouts is modest (33.02 vs 32.98 mAP)"** — This conflates one metric; OF-Diff leads on FID (24.18 vs 28.62) and mAP₅₀ (56.65 vs 55.11) which are more meaningful differences. Cherry-picking the smallest gap.
- **Strength about "addressing an important problem"** — Generic; removed per filtering rules.
- **Strength about "the method outperforms all baselines"** — Vague and already covered by specific strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation that the paper itself does not already articulate or imply.

## Suggestions

1. **Fix the duplicate row in Table 4** by adding an explicit column or footnote indicating whether captions are used. This single fix would resolve the most damaging ambiguity.
2. **Rewrite Eq. (9)** to clearly define \( \text{KNN}(\mathbf{x}_0) \) as the average distance to the \( k \)-nearest neighbors of \( \mathbf{x}_0 \) in the CLIP embedding space of real images, and replace the KL term with a well-specified distributional divergence (e.g., feature covariance matching or a distance to the mean feature vector). Or simplify the reward to rely only on the KNN term.
3. **Rephrase the "without real-image references" claim** throughout the paper to "without full real-image patches at inference" or "with shape-only priors at inference" to accurately reflect what the ESGM mask pool contains.
4. **Add a brief discussion** of the YOLOScore reversal on unknown layouts (Table 3), explaining why CC-Diff achieves better layout consistency there despite worse fidelity.
5. **Ablate the stop-gradient** on \( c_s \) in Eq. (3) as a straightforward experiment to validate the claimed stabilization.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| DiffusionSat (`I5webNFDgQ.md`) | 6.25 | R1 | Broader scope remote sensing diffusion foundation model; OF-Diff is more specialized |
| Adversarial Supervision L2I (`EJPIzl7mgc.md`) | 6.00 | R1 | Cleaner L2I method with stronger experimental design; OF-Diff is comparable in evaluation thoroughness but weaker in presentation |
| SatDiffMoE (`BDf1IBIuFx.md`) | 4.50 | R1 | Remote sensing diffusion with underspecified methodology; OF-Diff is stronger |
| Lay-Your-Scene (`u6y9uIzqAB.md`) | 4.00 | R2 | Layout generation paper with clarity issues; OF-Diff is stronger |
| GDCC L2I (`cHKuyeHmS9.md`) | 5.33 | R2 | Similar L2I+detection augmentation paper with comparable contribution level; OF-Diff is slightly weaker on methodological clarity |
| GeoDiffusion (`xBfQZWeDRH.md`) | 6.50 | R2 | Cleaner L2I+detection pipeline for autonomous driving; OF-Diff has more complex architecture with less cleanly demonstrated marginal gains |
| Diffusion for Visual Perception (`rMOhA1JNPo.md`) | 6.50 | R2 | Different task, but demonstrates the caliber of accepted diffusion papers |

**Round 1 bracket:** 3.5–6.5. OF-Diff is clearly above the weak anchors (1.5–3.2) but not at the 8.0 level.

**Round 2 narrowing:** Within the bracket, OF-Diff sits below GeoDiffusion (6.5) and DiffusionSat (6.25) due to the Table 4 ambiguity and underspecified DDPO reward. It is roughly comparable to GDCC (5.33) but with more evaluation breadth. The most significant unresolved issue (Table 4 duplicate row) is a presentation gap that prevents full confidence.

**Final score:** The paper has a legitimate core contribution (ESGM + online-distillation), thorough evaluation (13 metrics, 3 datasets, downstream detection), and clear evidence of practical utility. However, two issues — the uninterpretable Table 4 row and the underspecified DDPO reward — prevent the paper from meeting the ICLR bar for methodological rigor and clarity. The plausible gain from DDPO is marginal, and the core insight (shape priors + distillation) is well-supported but incrementally grounded on prior work.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>