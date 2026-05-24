Now I have sufficient calibration material. Let me write the final consolidated review.

## Summary

This paper proposes LDP, a lightweight (642K-parameter) denoising autoencoder plug-in that improves the generalization of existing super-resolution models to unseen degradations. LDP works as a conditional degradation model: it takes an SR output, adds patch-dependent noise, denoises it conditioned on LR high-frequency features, and downsamples to produce a predicted LR image. Cycle-consistency between this predicted LR and the original LR input serves as a training-time regularization loss; LDP can also guide inference-time posterior sampling in diffusion models. Experiments on four SR architectures (FeMaSR, StableSR, SwinIR, MambaIR) across five synthetic degradation types and three real-world datasets show consistent improvements in PSNR, SSIM, and LPIPS when LDP is used as a fine-tuning auxiliary loss.

## Strengths

- **Consistent improvements across diverse SR architectures and degradation types (Table 3).** LDP improves PSNR, SSIM, and LPIPS for every baseline model (GAN-, diffusion-, Transformer-, and Mamba-based) on all five synthetic degradation types. The gains are substantial for some cases (e.g., StableSR +2.16 PSNR on Hybrid). This demonstrates that LDP generalizes beyond a single architecture family.

- **LDP learns meaningful degradation patterns rather than collapsing to trivial downsampling (Table 2).** The predicted LR images from LDP have substantially lower similarity to bicubic-downsampled SR than DRN's predictions do (e.g., SSIM 0.8895 vs. 0.9638 on Down). This confirms that LDP's cyclic regularization is non-trivial, unlike prior degradation models that merely approximate downsampling.

- **Lightweight and practical design.** LDP has only 642K parameters and trains in ~16 hours on a single GPU, making it feasible to attach to existing SR models without prohibitive overhead.

- **Loss component ablation (Table 6) shows complementary benefits.** The ablation systematically varies the L1, LPIPS, frequency, and symmetric loss terms, finding that the full configuration (LDPV7) achieves the best PSNR and LPIPS, confirming that the design choices are complementary.

## Weaknesses

### Fatal

None.

### Major

- **Missing control: fine-tuning without LDP.** The paper's main claim is that LDP's cycle-consistency mechanism improves generalization. Yet the experimental setup (Table 3 and Section 4.3) fine-tunes models *with LDP as an auxiliary loss* and compares only against the original pretrained checkpoint — not against a model fine-tuned on the same data for the same number of steps *without* LDP. The ablation in Table 6 compares only within the LDP loss framework (baseline = no fine-tuning at all). While LDPV1 (frequency loss only, no LDP cycle loss) provides a partial control — it improves PSNR from 23.52→23.99 vs. LDPV7's 23.52→24.35 — this experiment is limited to a single model (SwinIR) on a single dataset (Hybrid). The main multi-model, multi-degradation results in Table 3 lack this control entirely. Without isolating LDP's contribution from the effect of additional fine-tuning, the magnitude of LDP's specific benefit is unclear.

### Minor

- **Inference-time posterior sampling results are overstated.** The paper claims "improvements across nearly all metrics on most datasets" for diffusion posterior sampling (Table 5). However, results are mixed: LDM+LDP on RealSR worsens on NIQE, CLIPIQA, and QAlign; UPSR+LDP on RealSRSet degrades QAlign; many ResShift+LDP changes are negligible (<0.001). While StableSR benefits consistently, the overall support for the inference-time claim is weaker than the paper's language suggests.

- **No comparison against a fixed, non-learned degradation model for cycle consistency.** The ablation studies always use the full LDP architecture. The paper never compares against a simpler alternative: e.g., bicubic downsampling of the SR output (optionally with a fixed Gaussian blur) with an L1 cycle-consistency loss. Without this control, it is unclear whether LDP's learned degradation modeling provides meaningful advantage over a fixed downsampler, or whether most of the benefit comes from any cycle-consistency constraint regardless of the degradation model complexity.

- **Several real-world results contradict the "consistent improvement" narrative.** In Table 4, FeMaSR+LDP on DPED hurts MANIQA, CLIPIQA, MUSIQ, and QAlign; StableSR+LDP on DPED hurts NIQE and CLIPIQA on RealSRSet; SwinIR+LDP on RealSRSet hurts NIQE. While the paper acknowledges some of these cases by suggesting artifact suppression penalized by certain metrics, the pattern weakens the claim of universal improvement.

### Trivial

- No FLOPs or memory usage reported for LDP during training (only parameter count and training time), which would be helpful for practitioners evaluating it as a "plug-in."

## Nice-to-Haves

- A direct experiment comparing fine-tuning with LDP vs. fine-tuning without LDP (same data, same iterations, same base optimizer) for all four architectures.
- Comparison against a fixed-downsampler cycle loss (e.g., bicubic + Gaussian blur) to isolate the value of learned degradation.
- Analysis of cases where inference-time LDP guidance harms results (e.g., LDM on RealSR) — why does the gradient introduce artifacts in some settings?

## Removed Points

- "The connection between the diffusion model property and LDP's design is never explained." — **Removed.** The paper explicitly states in Section 3.1: "after noise is added, HR features and LR features become aligned... making denoising noisy HR features equivalent to denoising noisy LR features. This allows us to perform degradation modeling on HR images using a denoising autoencoder." The connection is clearly described.
- "Why patch-dependent noise? What does the DPM learn that a simple regression would not?" — **Removed.** The paper justifies patch-dependent noise: "this patch-wise formulation enables each image region to undergo a different level of degradation, allowing the model to better capture spatially varying corruption" (Section 3.2). This is a clear rationale.
- "Baselines DRN (2020) and DualSR (2021) are outdated" — **Removed.** These are degradation-modeling baselines (the only relevant prior methods for Tables 1-2). The main SR comparisons in Table 3 use recent architectures (StableSR 2024, MambaIR 2024). The reviewer conflates two different sets of comparisons.
- "Table 2 interpretation is inconsistent (DRN outperforms LDP in Table 1 yet collapses to downsampling)" — **Removed.** The two tables measure different things: Table 1 measures LR prediction accuracy, Table 2 measures similarity to bicubic downsampling. A model can predict accurate LR images while collapsing to downsampling (high similarity in Table 2 is a *flaw*, not a competing evaluation). The paper's interpretation is coherent.
- "The motivation invokes a property from diffusion models... The cited property is about the distributions... not about the architecture" — **Removed.** The paper uses this property as motivation for *why a denoising autoencoder can model degradation*, not as a specific architectural prescription. The reviewer misinterprets the role of this citation.
- Missing related works — **Removed** per policy (I cannot independently verify existence of missing citations).
- Formatting/style nitpicks — **Removed** per policy.
- Reproducibility concerns about undisclosed hyperparameters — **Removed** per policy. The paper provides adequate implementation details for LDP (Section 4.1) and defers SR model fine-tuning details to the appendix (which is stripped by the parser).

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same issues that the paper itself partially acknowledges (mixed real-world results, inference-mode limitations) and one important missing control that the authors did not address (no fine-tuning-without-LDP baseline). No reviewer identifies a fundamentally different interpretation of the results or an unexpected connection to other lines of work.

## Suggestions

1. **Add the missing control experiment.** Fine-tune all four baseline models on the same DF2K+BSRGAN data for the same number of steps *without LDP* (or with only the base SR loss functions). Report these results alongside the +LDP results in Table 3. This is the single most impactful addition for establishing LDP's causal contribution.

2. **Tone down the inference-time claims** or add a more nuanced discussion of when LDP helps vs. hurts diffusion posterior sampling. A failure analysis of LDM on RealSR would be informative.

3. **Add a simple baseline**: compare LDP's cycle-consistency loss against a variant that uses bicubic downsampling (+ fixed Gaussian blur) of the SR output with an L1 loss against the input LR. This would isolate whether LDP's learned degradation modeling is the source of improvement or merely any cycle constraint.

## Score and Decision

**Calibration anchors (all from the human-review corpus):**

| Path | Avg Score | Comparison to this paper |
|------|-----------|--------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/owziuM1nsR.md` (RGT Transformer) | 7.50 | Stronger — full architectural contribution with comprehensive ablation; this paper is less ambitious in scope and has a missing control experiment. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/my0RqY48xz.md` (Cooperative Game Theory for SR) | 6.50 | Comparable ambition but this paper tests on more diverse modern architectures; that paper has theoretical grounding this one lacks. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JkCJBoNUcU.md` (RealDGen data generation) | 6.00 | Comparable — both address SR generalization with a plug-in approach; this paper has broader architecture coverage but that paper has cleaner experimental controls. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/46mbA3vu25.md` (Diffusion vs GAN comparison) | 5.75 | Comparable — both have clear contributions but notable limitations; this paper's plug-in is a tangible artifact, that paper's insights are comparative/qualitative. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/QO3yH7X8JJ.md` (Arbitrary-scale SR from diffusion) | 5.25 | Comparable — both have interesting ideas but incomplete evidence; this paper has stronger empirical breadth. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MdBt0ttZrZ.md` (Laplacian SR loss) | 3.50 | Weaker — limited scope and unclear novelty; this paper's architecture coverage and two-mode operation are clearly more substantial. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OKOjkFrhSs.md` (Prompt-guided dynamic network) | 3.00 | Weaker — limited novelty relative to prior work; this paper's degradation modeling approach is more clearly original. |

The paper makes a real contribution: LDP is a lightweight, practical plug-in that consistently improves SR model generalization across diverse architectures. Table 3 provides strong evidence for this. However, the missing fine-tuning-without-LDP control tempers confidence in attributing the gains specifically to LDP's cycle-consistency mechanism, and the inference-time results are weaker than claimed. On balance, the paper sits between a mid-range and strong submission — it has clear value but requires a key control experiment for full validation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>