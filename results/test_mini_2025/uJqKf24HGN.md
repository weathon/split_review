Now let me construct the final consolidated review.

## Summary

This paper proposes UniCon, an adapter architecture for controllable diffusion models that replaces the standard bidirectional feature-modification paradigm (as in ControlNet) with unidirectional information flow: the frozen diffusion model only performs forward passes, and a trainable full-size adapter directly produces the denoised output. This eliminates the need to compute and store gradients through the diffusion model during adapter training, substantially reducing memory and speeding up training. The method is validated on both U-Net (SD) and Transformer (DiT) backbones across multiple conditional generation tasks.

## Strengths

1. **Well-motivated architectural contribution with clean ablation evidence.** The core idea — unidirectional flow from frozen diffusion model to adapter — is clearly motivated by the growing cost of backpropagating through ever-larger diffusion models. The key ablation (Table 1c) directly compares the same adapter architecture with and without the unidirectional design, and the "Full" variant shows a clear improvement: PSNR 36.53→37.34 and FID 23.04→20.34 on SR. This cleanly isolates the design's benefit from parameter-count effects.

2. **Consistent superiority across both DiT and SD U-Net backbones.** Table 2 shows UniCon outperforming ControlNet and T2I-Adapter on Canny, Depth, Pose, SR, and deblur tasks for both DiT and SD U-Net. The breadth of validation (two fundamentally different diffusion architectures, five diverse tasks) convincingly demonstrates that the unidirectional design is backbone-agnostic — a claim explicitly made in Section 3.

3. **Quantified training-efficiency gains.** The breakdown in Figure 6 into Weight/Activation/Gradient/Optimizer costs clearly shows where the savings come from. For DiT, UniCon-Full reduces gradient memory by roughly half (from ~13GB to ~1GB) and overall VRAM from ~33GB to ~20GB, with corresponding training-time savings. The VRAM breakdown is more informative than a single aggregate number.

4. **ZeroFT connector improvement.** Table 1b shows the proposed ZeroFT connector consistently outperforms ZeroMLP and ShareAttn across both Canny (SSIM 0.5426 vs. 0.5343/0.5236) and SR (FID 22.07 vs. 22.99/23.03). This provides a concrete, reusable architectural improvement beyond the main design principle.

## Weaknesses

### Major

1. **Inconsistency in reported efficiency numbers.** The abstract claims a "one-third" GPU memory reduction, the introduction claims "saves half" the VRAM, and Figure 1(c) states "2X vs 1X" (50%). These are three different numbers for the same claim. Separately, the 2.3× training speedup claimed in the abstract and introduction does not clearly match Figure 6, where UniCon-Full shows roughly 1.5× speedup over ControlNet-Full on DiT (~8s/iter vs ~12s/iter). The paper never explains which specific comparison yields 2.3×, nor reconciles it with the figure. Inconsistent headline numbers undermine trust even if the underlying trend (UniCon is faster and lighter) is genuine.

2. **Inference cost is not discussed.** UniCon requires both the frozen diffusion model and the full-size adapter copy at *inference* time, roughly doubling the inference computation and memory relative to standard diffusion inference, and roughly doubling it relative to ControlNet (whose adapter is typically encoder-only). The paper frames its efficiency contributions entirely around training and never acknowledges this trade-off. While the paper's scope is training efficiency, a practitioner evaluating deployment viability would be misled without this information.

3. **Parameter-count asymmetry in main comparison (Table 2) is insufficiently controlled.** For the DiT results on Canny, Depth, and Pose, the ControlNet baseline uses the "Encoder" variant (~half the full-network parameters), while UniCon uses the full model copy (~2× the parameters). Without UniCon-half results for these tasks, the reader cannot distinguish whether the large gains (e.g., Canny SSIM 0.4748→0.5458) come from the unidirectional design or simply from having 2× the adapter capacity. The paper does provide the controlled comparison in Table 1c for the "Full" variant, which supports the design claim — this is the strongest evidence and should be elevated. But the main comparison table should either include UniCon-half for all tasks or explicitly state the parameter disparity.

### Minor

1. **No statistical significance or variance reporting.** The paper reports single-run metric values with no confidence intervals or multiple-seed experiments. For comparisons where differences are small (e.g., SD Canny Clip-IQA: ControlNet 0.6683 vs. UniCon 0.6704), the reader cannot assess whether the improvement is meaningful.

### Trivial

- Figure 6 has cluttered layout making exact value reading difficult.
- Footnote about "UniCon-Encoder design is ineffective" is valuable information that should be in the main method section, not a footnote.

## Nice-to-Haves

- Add UniCon-half rows for Canny, Depth, and Pose in Table 2 (or explain why not applicable). This would cleanly resolve the parameter-count asymmetry concern.
- Provide intuitive explanation for *why* unidirectional flow improves over bidirectional. The paper currently shows *that* it works but offers no analysis of the mechanism.
- Include inference-time latency and memory measurements to give a complete picture.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The claim 'reduces GPU memory usage by one-third and increases training speed by 2.3 times' is not well-anchored to a specific, reproducible comparison."* → The inconsistency among abstract/intro/Figure 1(c)/Figure 6 is kept as Weakness #1 above. The specific complaint about lacking "precise experimental context" for the 2.3× number is merged into that weakness.
- *"Statistical significance concerns"* → Moved to Minor weakness above.
- *"Missing related works"* → Removed per instructions (cannot verify).
- *"Formatting issues"* → Removed per instructions (parser artifacts).
- *"Missing appendix/proofs"* → Removed per instructions (parser strips appendix).
- Generic complaints about "overclaimed scope" and "evaluation lacking rigor" not anchored to specific paper content → Removed.
- Strength Finder's generic strengths ("important problem", "interesting question") → Removed.
- Strength Finder's strength about "ability to scale adapter parameters without extra compute" → Merged into the retained strengths.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's insight that the unidirectional-vs-bidirectional comparison (Table 1c) should be the headline result rather than the resource-efficiency comparison is a valid presentational observation but not a novel finding about the paper itself. The strength finder's observations are well-aligned with the paper's own claims.

## Suggestions

1. **Reconcile the efficiency numbers.** Pick one consistent framing for VRAM savings (Figure 6 data supports ~40%, close to "over one-third" from the abstract) and clearly specify which configuration yields the 2.3× speedup, connecting it visually to Figure 6.
2. **Add an inference-cost paragraph.** Even one sentence acknowledging that inference requires both models and reporting the combined parameter count and approximate FLOPs would address a major practical concern.
3. **Elevate Table 1c to a primary result.** The controlled unidirectional-vs-bidirectional comparison is the cleanest evidence for the design principle. Consider moving it — or at least its key row — into the main contribution summary.
4. **Add UniCon-half to all rows in Table 2** or add a clarifying note explaining the parameter counts for each method.
5. **Add multiple-seed standard deviations** for at least the core comparison (Table 2's main rows).

## Score and Decision

**Round 1 bracketing:** I queried calibration papers on "diffusion model controlled generation adapter architecture" in bands [(-∞, 3.5)], [3.5, 7.5], and [7.5, ∞]. The weak band returned papers scoring 1.5–3.4 (rejected/withdrawn); the middle band returned 3.67–6.5 (mix of withdrawn and accepted poster); the strong band returned 8.0 (spotlights/orals). UniCon clearly sits above the weak band and well below the top band, giving an initial bracket of [4.5, 7.0].

**Round 2 narrowing:** I queried for more targeted anchors in [4.5, 6.5] and [5.0, 7.5]. Key anchors:
- **SaRA** (6.20, accepted poster) — efficient diffusion fine-tuning with sparse low-rank adaptation. Similar efficiency-focused contribution. SaRA's core assumption was questioned by reviewers but it still received 6.2. UniCon has cleaner ablation and more consistent gains, placing it comparably or slightly below.
- **CTRL** (6.50, accepted poster) — RL-based conditional control. Novel formulation but limited experiments/missing baselines. UniCon has more thorough experiments and cleaner evidence.
- **Diffusion Few-shot** (5.20 overall, but high variance 3-8-3-6, rejected) — few-shot dense prediction. Had serious presentation and plagiarism concerns. Not a good comparison.
- **3D-Adapter** (5.60, rejected) — plug-in module for 3D generation. Had mixed reviews.
- **APCtrl** (3.67, withdrawn) — alternative projection control. Limited novelty relative to prior work.
- **C-CoDe** (4.60, withdrawn) — inference-time guidance. Had significant weaknesses about triviality.

Comparing UniCon against SaRA (6.2, accepted) — the closest topical neighbor — UniCon has a stronger core insight and more convincing ablation, but suffers from the undiscussed inference cost and inconsistent efficiency numbers that SaRA does not. Placing UniCon slightly below SaRA accounts for these issues.

**Final calibration anchors:**

| Anchor | Path | Round | Avg Score | Comparison |
|--------|------|-------|-----------|------------|
| TCIG | RFJGFrMvYj.md | 1 | 1.50 | Much weaker — rejected, poor quality |
| ELR-Diffusion | edx7LTufJF.md | 1 | 2.50 | Much weaker — withdrawn, limited contribution |
| APCtrl | yPxhj1FKhG.md | 1 | 3.67 | Weaker — novelty questioned, withdrawn |
| C-CoDe | MBDH5zyxHM.md | 1 | 4.60 | Weaker — method concerns, withdrawn |
| Few-shot Dense | az5WtGe48n.md | 2 | 5.20 | Weaker — mixed reviews, rejected |
| 3D-Adapter | C0HDYvGwol.md | 2 | 5.60 | Similar score but rejected; UniCon is stronger |
| DiffusionNAG | dyG2oLJYyX.md | 2 | 5.75 | Different topic (NAS), accepted poster |
| Denoising as Adaptation | jsBhmOCKYs.md | 2 | 5.80 | Different topic (domain adaptation), accepted poster |
| **SaRA** | wGVOxplEbf.md | 2 | **6.20** | **Most similar — efficient diffusion adaptation, accepted poster. UniCon has stronger core insight but undiscussed inference cost** |
| Adversarial SiD | lS2SGfWizd.md | 2 | 6.25 | Different topic (distillation), accepted poster |
| Probabilistic Adaptation | pjtIEgscE3.md | 2 | 6.25 | Different topic (black-box adaptation), accepted poster |
| Prompt Pruning | 3BhZCfJ73Y.md | 2 | 6.25 | Different topic (pruning), accepted poster |
| CTRL | svp1EBA6hA.md | 1 | 6.50 | Stronger paper overall — novel RL formulation, accepted poster |
| CADS | zMoNrajk2X.md | 1 | 8.00 | Much stronger — spotlight |
| RB-Modulation | bnINPG5A32.md | 1 | 8.00 | Much stronger — oral |
| Shortcut Models | OlzB6LnXcS.md | 1 | 8.00 | Much stronger — oral |

The paper's core idea is sound and well-motivated, and the ablation evidence for the unidirectional design (Table 1c) is strong. The experiments are comprehensive across two backbones and multiple tasks. However, the undiscussed inference cost is a practical concern, and the inconsistencies in the headline efficiency numbers (one-third vs half vs 2X VRAM; 2.3× speedup not matching Figure 6) are real presentation flaws that weaken the otherwise compelling story. Relative to SaRA (6.20) — the closest topical anchor accepted as a poster — UniCon has a stronger core contribution but material completeness issues that SaRA did not face. I therefore assign a score of **6.0**, placing it slightly below SaRA but clearly above the withdrawn papers (APCtrl at 3.67, C-CoDe at 4.60).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>