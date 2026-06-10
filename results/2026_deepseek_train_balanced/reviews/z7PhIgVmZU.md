## Summary

This paper proposes BAT-CLIP, a test-time adaptation (TTA) method for CLIP that jointly updates the LayerNorm parameters of both the vision and text encoders. The method introduces two auxiliary losses beyond entropy minimization: a projection matching loss that aligns visual class prototypes (computed from pseudo-labels) with text features, and an inter-class separability loss that pushes prototypes apart in visual space. Experiments on CIFAR-10C, CIFAR-100C, and ImageNet-C show consistent accuracy improvements over existing CLIP-based TTA methods (TPT, VTE) and prior TTA methods adopted for CLIP (TENT, BN-1, RPL, SAR), while being substantially faster.

## Strengths

- **Major computational efficiency gain**: BAT-CLIP processes a full ImageNet-C task in ~45 seconds, compared to 40 minutes for TPT and 4 minutes for VTE (line 210). This ~53× speedup over VTE makes the approach practical for deployment.

- **Extreme parameter efficiency**: Only ~0.044% of CLIP's total parameters are updated (the LayerNorm affine parameters of both encoders), as stated in Section 4 (line 131). This is clearly quantified and far more efficient than full fine-tuning.

- **Consistent accuracy gains across benchmarks**: With ViT-B/16, the method achieves mean accuracy improvements of +9.7%, +5.94%, and +5.12% on CIFAR-10C, CIFAR-100C, and ImageNet-C over the next best method at severity level 5 (abstract, Table 2). These gains are reported across all 15 corruption types.

- **Thorough zero-shot analysis**: Section 3 systematically documents CLIP's degradation under corruptions across 4 visual backbones (RN101, ViT-B/16, ViT-B/32, ViT-L/14), 3 datasets, 15 corruption types, and 5 severity levels—with specific numbers (e.g., CIFAR-100 with Gaussian noise severity 5 drops to 10.79% from 49%). This provides a clear empirical motivation for the method.

- **Prompt-engineering-free design**: The method uses a single generic prompt template throughout (line 131), explicitly contrasting with VTE's prompt ensemble and TPT's reliance on hand-crafted initialization.

## Weaknesses

### Fatal
None.

### Major

1. **Missing key baseline: bimodal adaptation with entropy minimization alone.** The paper compares against TENT (Wang et al., 2021) applied only to the *vision* encoder (Table 3), but never evaluates simply applying entropy minimization to *both* encoders (vision + text) without the proposed `L_pm` and `L_sp` losses. This is the critical ablation needed to isolate the contribution of the proposed loss terms from the effect of simply adapting both modalities. Without it, the reader cannot determine whether the reported gains come from the proposed projection matching and separability losses, or just from the fact that both encoders are being updated—something any prior TTA method could have done. The paper's core claim is that `L_pm` and `L_sp` improve alignment and separability; this baseline is necessary to support that claim.

2. **Class separability loss (`L_sp`) formulation is incomplete for classes absent from a batch.** Equation 4 sums over all class pairs `(l, c)` in `C`, but the class prototype `\bar{v}_c` (Eq. 2) is undefined (division by zero) for any class with zero samples in the batch. With batch sizes of 200 on CIFAR-100 (100 classes) or 64 on ImageNet-C (1000 classes), many classes will have no samples. The paper does not specify whether such classes are excluded, and if so, how the loss behaves when only a sparse subset of class pairs is computed each batch. This is a methodological gap in the formulation as presented.

### Minor

1. **Pseudo-label quality is unexamined.** The paper acknowledges that "predicted labels could be wrong/noisy" (line 99), but never analyzes how pseudo-label accuracy evolves during adaptation or varies across corruption types/severities. At high corruption severity where zero-shot accuracy can be as low as ~10.79% (CIFAR-100, RN101, severity 5), class prototypes computed from predominantly wrong pseudo-labels (Eq. 2) would be corrupted. Under such conditions, maximizing the projection of these corrupted prototypes onto text features (Eq. 3) may not constitute meaningful alignment. The claimed mechanism is plausible but unsupported without this analysis. Adding a simple confidence filter (as SAR does for gradients) or tracking pseudo-label accuracy during adaptation would substantially strengthen the paper.

2. **No variance or statistical significance reporting.** All results are reported as single runs without error bars, standard deviations, or confidence intervals. While corruption benchmarks are deterministic in the data, TTA results can depend on random seeds, batch ordering, and optimizer stochasticity. Multiple trials would help establish whether the reported margins (e.g., ~5% on ImageNet-C) are reliable.

3. **Specific LayerNorm parameters not specified.** The paper states it updates "LayerNorm parameters" (line 131) of both encoders, citing ~0.044% of total parameters, but does not specify *which* LayerNorm layers are adapted (all transformer blocks? only certain stages? the final norm?). CLIP's ViT and text encoder have LayerNorm in multiple locations. This level of detail matters for exact reproducibility.

4. **Ablation study lacks textual discussion in extracted version.** Section 5.2 presents the ablation results as an embedded image with no accompanying prose analysis in the extracted text. While this may be a parser artifact, the absence of any written interpretation of which components contribute what is a deficiency in what can be evaluated from the submission.

### Trivial
None that survive filtering.

## Nice-to-Haves

- Extend evaluation to natural distribution shifts (ImageNet-R, ImageNet-Sketch, ImageNet-v2) to test whether the method generalizes beyond synthetic corruptions.
- Report per-corruption-type breakdown to identify which corruptions benefit most/least from bimodal adaptation (relevant because pseudo-label reliability varies by corruption type).
- Add explicit sign convention clarification for Eq. 5 (L_pm and L_sp are subtracted because they are maximized) — currently inferable but not stated.

## Removed Points

Points flagged for removal; treat with caution:

- **Harsh Critic: "Pseudo-label bootstrap problem is unacknowledged"** — Factually incorrect. The paper states at line 99: "However, within the batch, due to the image corruption, the predicted labels could be wrong/noisy." The substance of the concern (no analysis of pseudo-label accuracy) is retained as Minor weakness #1 above; the "unacknowledged" framing is removed.
- **Harsh Critic: "TPT/VTE comparison is staged rather than fair"** — Overstated. The paper compares against the only available CLIP-based TTA methods in the literature on standard benchmarks. The real gap (missing bimodal-entropy-only baseline) is retained as Major weakness #1 above. The claim that the comparison is intentionally misleading is removed.
- **Harsh Critic: "Table 1 presented only as an image"** — This is a parser artifact; images are standard in papers and the extracted text naturally cannot render them.
- **Harsh Critic: "Section 5.2 has no prose"** — Could be a parser artifact stripping the figure caption and surrounding text. Treated cautiously.
- **Harsh Critic: "Section 3.1 analysis is speculative"** — The analysis is grounded in empirical measurements (Fig. 2, Table 1). The interpretation may be informal but is not speculative beyond normal scientific discussion.
- **Strength Finder: "Inclusion of an ablation study"** — Partially retained, but the strength is qualified since the ablation content cannot be verified from the extracted text.

## Novel Insights

None beyond the paper's own contributions. The Harsh Critic and Strength Finder surface no observation about the paper that the paper does not already state itself.

## Suggestions

- **Run the critical missing baseline**: Compare (a) entropy minimization on both encoders alone vs. (b) entropy + L_pm vs. (c) entropy + L_sp vs. (d) all three combined. This single experiment would directly validate the paper's core claim.
- **Clarify L_sp formulation**: Explicitly state how classes absent from a batch are handled (e.g., sum only over classes present, or define a zero contribution for empty prototypes).
- **Add pseudo-label confidence filtering**: A simple entropy threshold (analogous to SAR's gradient filtering) would make prototype computation more robust at high corruption severity.
- **Report means and standard deviations over 3–5 random seeds** for the main results.
- **Specify exactly which LayerNorm parameters are updated** (which blocks, which layers) to enable exact reproduction.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>