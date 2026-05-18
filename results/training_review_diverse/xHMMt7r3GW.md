Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper introduces Lie group Relative position Encodings (LieRE), which generalize Rotary Position Embeddings (RoPE) to higher-dimensional inputs by learning dense rotation matrices parameterized via a skew-symmetric basis and the matrix exponential. The key idea is to replace the block-diagonal 2D rotations used in RoPE/RoPE-Mixed with full rotation matrices, allowing the model to learn richer positional representations for multi-dimensional data (2D images, 3D videos). Empirically, LieRE shows consistent accuracy improvements over absolute position embeddings and existing relative encoding methods (RoPE-Mixed, VisionLlama), along with data and compute efficiency gains on CIFAR-100 and UCF101 classification tasks.

## Strengths

1. **Principled generalization of RoPE via differentiable Lie-group parameterization.** The paper provides a clean mathematical framework: learning a skew-symmetric matrix basis and mapping it to rotations via matrix exponential. The connection to RoPE is explicit (block size 2 recovers RoPE-Mixed), and the block-size knob allows controlled capacity scaling from exact commutativity (small blocks) to richer but approximate relative encoding (large blocks). This is technically sound and novel.

2. **Consistent empirical improvements over multiple baselines in a controlled setting.** When all methods share the same backbone, augmentation, and training regimen, LieRE outperforms absolute PE, VisionLlama, and RoPE-Mixed across CIFAR-100, ImageNet, and UCF101 (Table 1). The 2.2% relative improvement over RoPE-Mixed on CIFAR-100 and 1.5% on UCF101 are modest but consistent, and the gains over absolute PE are substantial (10.0% on CIFAR-100, 15.1% on UCF101). The improvement holds across ViT-Tiny, ViT-B, and ViT-L scales (Table 4).

3. **Demonstrated data and compute efficiency.** On CIFAR-100, LieRE requires ~3.9× fewer training steps to match the absolute-PE baseline accuracy (Figure 4b) and achieves the full-data baseline accuracy with only 70% of the training data (Figure 3b). These are practically meaningful efficiency improvements, evaluated in a controlled setting where only the position encoding changes.

4. **Patch-shuffling experiment provides direct evidence of positional encoding usage.** Under patch shuffling, LieRE shows the largest accuracy drop among all methods (Table 3), convincingly demonstrating that the model actually leverages the learned positional representations rather than ignoring them.

5. **Robustness across parameter-sharing regimes and resolutions.** LieRE benefits from per-head/per-layer learned bases (Table 2) and maintains its advantage across varying inference resolutions (Figure 2), indicating that the encoding generalizes well.

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguity about the "DeiT III" baseline and what it actually contains.** The abstract and introduction claim comparison against "DeiT III," but Section 4 describes the setup as using "the standard backbone sizes of ViT-Tiny, ViT-B and ViT-L" with "All experiments use RandAugment." The full DeiT III recipe (Touvron et al., 2022) includes LayerScale, stochastic depth, repeated augmentation, 3-Augment, mixup/cutmix, and color jitter — none of which are mentioned. Table 1 labels the baseline "∗equivalent to DeiT," not "DeiT III." If the baseline is a simplified ViT+absolutePE+RandAugment rather than the actual DeiT III recipe, the headline claim of "10.0% relative improvement over DeiT III" is misleading. **This does not affect the comparison against RoPE-Mixed and VisionLlama** (which are implemented in the same shared framework), but it undermines the paper's most prominently advertised accuracy numbers and requires clarification. The authors need to either (a) document that they fully implemented the DeiT III recipe, or (b) rebrand the baseline as "ViT with absolute PE" and adjust the claims accordingly.

2. **No reported error bars or number of random seeds.** The Table 1 caption mentions "95% confidence intervals," but no intervals, standard deviations, or seed counts appear anywhere in the extracted text. The margins over the closest relative competitor (RoPE-Mixed) are small (2.2% relative on CIFAR-100, 1.5% on UCF101). Without multiple random seeds and error bars, it is impossible to assess whether these differences are statistically meaningful or within run-to-run noise. This is the single most important empirical gap to address.

### Minor

3. **No ablation controlling for added capacity in a non-rotation form.** LieRE adds ~580k parameters (ViT-B). The paper's block-size ablation (Section 5.3.2) shows that larger block sizes improve performance, which demonstrates that the *rotation structure* benefits from more capacity, but it does not control for simply adding the same parameter budget to the baseline via a non-rotation mechanism (e.g., a small MLP or learned additive bias). Without this control, one cannot fully rule out the possibility that some of the gain comes from "more learned parameters" rather than "better structural inductive bias."

4. **Approximation error of the relative-position interpretation is not analyzed.** The paper correctly notes that for block sizes >2, the rotation matrices do not commute, so the score R(p_i)^T R(p_j) only approximately encodes relative positions p_j − p_i (Equation 1). The paper frames this as a tradeoff (line 52) but provides no empirical analysis of how the approximation degrades with distance or block size, nor any theoretical bound. For long sequences where p_i and p_j can be far apart, the approximation could in principle degrade. An empirical sanity check (e.g., measuring ∥R(p_i)^T R(p_j) − R(p_j − p_i)∥ for various position differences) would strengthen the paper's theoretical grounding.

5. **Missing implementation details essential for reproducibility.** The paper does not specify:
   - How the skew-symmetric basis matrices {A_i} are initialized.
   - The learning rate and optimizer settings for the basis matrices (distinct from the backbone?).
   - The computational overhead of the matrix exponential vs. precomputed RoPE rotations (is it negligible, or does it add non-trivial latency?).
   - The number of random seeds used for any experiment.

6. **Numerical inconsistency between abstract and conclusion.** The abstract reports "3.9-fold reduction in training time" while the conclusion (line 220) says "3.5 times less training compute[d]." These should be reconciled.

### Trivial

7. The paper refers to "standard1 transformer backbone" (line 82) with a superscript "1" but no corresponding footnote is visible in the extracted text — likely a formatting artifact.
8. Minor wording: "DEIT III basline" in abstract is a typo (though likely a parser artifact).

## Nice-to-Haves

- **Approximation analysis** as described in Weakness 4 above — not required for acceptance but would strengthen the theoretical story.
- **Failure case discussion**: are there settings (very small models, very long sequences) where LieRE underperforms RoPE-Mixed?
- **Computational cost benchmark**: wall-clock time comparison of LieRE vs. RoPE per forward pass, to quantify the matrix exponential overhead.

## Removed Points

These points from the reviewers are flagged to be removed; treat them with caution:

- **Data efficiency attribution (Harsh Critic, Other Observations #1):** The critic claimed the paper falsely attributes data/compute efficiency exclusively to LieRE. However, the paper explicitly states (line 145) "learnable relative position encodings, such as LieRE and RoPE-Mixed, exhibit substantially greater data efficiency" and notes (line 183) that LieRE shows "the largest reduction" — correctly distinguishing the general property from the best-in-class result. The criticism misreads the paper.

- **Patch shuffling comparison with RoPE-Mixed (Harsh Critic, Other Observations):** The critic speculates that "if LieRE and RoPE-Mixed drop by similar amounts, the experiment adds little" without verifying. Table 3 is an image in the original submission; the critic has no basis to assert this and did not provide evidence.

- **Block-size >2 outperformance claim (Harsh Critic, Other Observations):** The critic states the paper "never shows that block sizes >2 consistently outperform block size 2." The paper explicitly states (line 159) that "LieRE8 consistently outperforms alternatives across all evaluated model sizes" and refers to Figure 4a which plots accuracy vs. block dimension. The results are in the figure (unreadable only due to parser limitations on the image).

- **Generic strengths from Strength Finder:** The claim that LieRE shows "dramatic compute and data efficiency" (Strength #2) is retained in the main review but the phrasing is toned down to match the weaker evidence (only tested on CIFAR-100). The point about "stronger use of positional information than prior relative encodings" (Strength #3) is retained but only the patch-shuffling evidence supports it, and the magnitude vs. RoPE-Mixed is unclear from the extracted text. These are kept in the Strengths section with appropriate caveats.

## Novel Insights

The reviews collectively highlight an interesting tension: the paper makes a theoretically principled contribution (generalizing RoPE via Lie groups) but its empirical evaluation creates an asymmetry where the strongest headline numbers (10.0% over "DeiT") rest on the shakiest ground (unclear baseline reproduction), while the more modest but better-controlled comparisons (2.2% over RoPE-Mixed) lack error bars. This pattern suggests the paper's genuine contribution — dense learned rotations for multi-dimensional positional encoding — is real, but the presentation inflates it by juxtaposing it against a potentially weak absolute-PE baseline labeled as "DeiT III." The actual value of the work is better captured by the controlled comparison against RoPE-Mixed (implemented in the same framework), where the gains are modest but consistent across tasks and model sizes.

## Suggestions

1. **Clarify the baseline.** Either document that the full DeiT III recipe (LayerScale, stochastic depth, repeated augmentation, mixup/cutmix, etc.) was used, or rename the baseline to "ViT with absolute PE" and adjust all claims accordingly. The 10.0% figure is only defensible if the baseline is genuinely DeiT III.

2. **Report error bars.** Run all key experiments (Table 1, compute efficiency, data efficiency) with at least 3 random seeds and report mean ± std or confidence intervals. This is essential given the small margins over RoPE-Mixed.

3. **Add a capacity-control ablation.** Add the same ~580k parameters to the absolute-PE baseline via an extra linear layer or learned additive bias and verify that LieRE's improvement exceeds what extra capacity alone provides.

4. **Reconcile 3.9× vs. 3.5×** discrepancy between abstract and conclusion.

5. **Disclose initialization, hyperparameters, and seed counts** for full reproducibility.

## Score and Decision

The paper introduces a novel and principled generalization of RoPE with consistent empirical evidence across multiple tasks, scales, and ablations. The core idea is solid and the controlled comparisons against RoPE-Mixed and VisionLlama are fair. However, the ambiguity surrounding the "DeiT III" baseline and the complete absence of error bars are significant gaps that prevent full confidence in the headline claims. The paper is publishable after moderate revisions.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>