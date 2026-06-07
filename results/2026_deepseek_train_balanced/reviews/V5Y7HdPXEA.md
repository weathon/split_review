## Summary

This paper proposes UUDS, a CLIP-based framework for unsupervised cross-domain medical image segmentation. The method integrates domain adaptation and segmentation into a single end-to-end pipeline using two types of prompts (a hard domain prompt for global style features and a learnable soft segmentation prompt for region-level content), combined with uncertainty-guided pseudo-labeling on target data. Experiments on BraTS (T2↔FLAIR) and VS (ceT1↔hrT2) benchmarks report improvements over several traditional UDA baselines, and an ablation study confirms the individual contribution of each proposed component.

## Strengths

- **Dual-prompt design is well-motivated and empirically validated.** The paper identifies a genuine limitation of CLIP for medical segmentation — CLIP captures global image-level features but struggles with fine-grained anatomical detail — and addresses it by splitting the prompt into a hard domain prompt (for global style) and a learnable soft prompt (for region-level content). The ablation in Table 3 (Sec. 4.3) shows that removing the segmentation prompt drops Dice from 75.22% to 64.03% (>10 percentage points), providing clear quantitative evidence that both prompt types contribute independently.

- **Ablation study cleanly isolates each component's contribution.** Unlike papers that report only a single "w/o all" degradation, Table 3 separately ablates the domain prompt, segmentation prompt, and uncertainty estimation, with the text reporting each numerical drop (Sec. 4.3, lines 236–241). This gives the reader a concrete picture of which design choices drive performance.

- **Non-adversarial domain adaptation framework.** The method avoids GAN-based adversarial training (whose instability is well-documented, Sec. 1, line 12) and instead uses CLIP-based prompt-driven alignment. The VS results (Table 2) show that adversarial baselines like CDAC performed poorly, while UUDS achieved 68.87% Dice, demonstrating that the non-adversarial approach is a viable alternative.

## Weaknesses

### Major

1. **Internal contradiction: ViT layer vs. ResNet backbone.** Line 84 states "the domain feature representation X_d^i is learned from *ViT layer* of CLIP image encoder," but line 185 states "The *ResNet version* of CLIP is chosen as the backbone." A ResNet-based CLIP does not have ViT layers. This is a concrete contradiction in the method description — one of these statements is wrong — and it undermines confidence in the architectural details. Until this discrepancy is resolved, the reader cannot determine what features are actually being extracted and from where.

2. **Unconventional contrastive loss formulation with unclear optimization behavior.** The domain distillation loss L_DD (Eq. 1, line 89) uses `(1−sim)` where standard InfoNCE uses `sim` directly, and the overall structure lacks a clear negative sign that would align it with standard contrastive objectives. The text says the loss maximizes source similarity and minimizes target similarity (line 86), but the equation's behavior under optimization is non-obvious — it is unclear whether minimizing or maximizing this loss produces the claimed effect. The second L_DD term for synthetic images (Eq. 2, line 95) replicates the same structure without explanation of why it is needed or how it differs. This formulation needs to be re-derived and justified; as written, it undermines confidence in the method's correctness.

3. **No variance or statistical significance on any result.** All Dice and ASSD scores (Tables 1–3) are reported as single point estimates with no standard deviations, confidence intervals, or indication of multiple runs. Given the stochastic nature of CLIP fine-tuning and the modest test set sizes (BraTS: 41 images; VS: 28 patients), the reported improvements could fall within run-to-run noise. Basic experimental hygiene — 3–5 seeds with variance — is needed to establish that differences are meaningful.

4. **No CLIP-based or VLM-based baselines in the comparison.** All seven baselines (ADVENT, SIFA, CUT, AccSeg, HRDA, CDAC, MIC) are traditional adversarial or feature-alignment methods; none use a vision-language model. Since UUDS's backbone is CLIP, it is unclear whether the reported gains come from CLIP's strong pretrained representations or from the specific architectural innovations (dual-prompts, uncertainty estimation). At minimum, a CLIP-feature extractor with a standard UDA head, or a single-prompt variant of UUDS itself, should be compared to disentangle these effects.

### Minor

1. **Several implementation details critical for reproducibility are omitted.** The number `M` of learnable context vectors for the segmentation prompt (line 111) is not given; the uncertainty threshold `χ` (line 142) is named but its value is unspecified; the CLIP variant is only described as "ResNet version" without specifying RN50, RN101, or another variant; and the definition of "containing the segmentation object" for the in-batch contrastive loss (line 115–116) is not explained — for whole-slice medical images, most patches contain a mix of foreground and background, making it unclear how binary categorization is performed.

2. **Novelty claims are stronger than the paper's evidence supports.** The paper states it is "the first" to unify domain adaptation and segmentation (lines 17, 247) and "the first" to extend CLIP to unsupervised cross-domain medical segmentation (line 19). The former claim is inadequately justified: the paper does not articulate precisely why prior methods that also use segmentation losses on translated images (e.g., SIFA, CycADA, DAR-Net — all cited in the paper) are considered "two separate steps" while UUDS is not. The latter claim is difficult to assess without any VLM-based baseline comparisons. The paper's contributions are real but would be better framed precisely rather than with sweeping priority assertions.

3. **No failure analysis or limitation discussion.** The paper does not discuss when UUDS might struggle, how the uncertainty threshold affects results, what types of domain shift it handles poorly, or whether it overfits given that all CLIP parameters are fine-tuned on relatively small datasets (~200 patients). These are standard considerations for a UDA paper.

### Trivial

- Line 84: "the domain feature representation X_d^i is learned from ViT layer" — even ignoring the ResNet contradiction, the superscript notation switches inconsistently between `X_d^i`, `X_d^s`, and `X_d^t` within a few lines, making the method harder to follow.

## Nice-to-Haves

- Reporting per-region metrics (enhancing tumor, tumor core) on BraTS and Hausdorff distance would improve comparability with the broader literature.
- An estimate of inference-time cost would help readers assess practical applicability, since fine-tuning all CLIP parameters on 4× L40s GPUs is computationally heavy.
- A discussion of how the uncertainty threshold χ was selected (tuned per dataset or fixed) would strengthen the uncertainty estimation component.

## Removed Points

These points were identified by the reviewers but removed during consolidation with justification:

- *Missing related works (CLIP-based UDA methods from MICCAI 2023–2024)* — Removed per policy: the reviewer does not have external sources to verify the existence of such methods.
- *Speculation that "the paper dates to mid-2025 but cites only through early 2024"* — Removed per policy: the reviewer cannot independently verify the timeline or the existence of specific missing works.
- *Criticism about 0.00% Dice on VS being "unusually catastrophic"* — Removed: the paper is reporting this as a lower-bound baseline result to illustrate domain shift severity, not as a claimed result.
- *Code release expectations* — Removed per policy: reproducibility nitpicks about unreleased code.
- *Missing appendix content / proofs* — Removed per policy: the parser strips these; they exist in the original submission.
- *Formatting/style nitpicks* — Removed per policy.
- *Generic strengths from Strength Finder about "addressing an important problem" or "interesting question"* — Removed as generic/superficial.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a recurring tension: the ablation study (Table 3) is unusually thorough in isolating each component, but this rigor contrasts sharply with the lack of statistical reporting (variance, multiple seeds) and the incomplete baseline set. The paper would benefit from applying the same rigor it shows in component analysis to its overall evaluation strategy — running multiple seeds and including variant-based baselines (e.g., UUDS minus its CLIP text encoder). A second observation is that the ViT/ResNet contradiction and the unconventional loss formulation both suggest insufficient proofreading of the method section, which is particularly damaging for a paper whose main novelty is architectural.

## Suggestions

1. **Resolve the ViT/ResNet contradiction** — clarify which CLIP variant is used and from which layers domain vs. content features are extracted.
2. **Re-derive and clearly explain the L_DD formulation** — verify that the optimization direction is correct and provide intuition for why (1−sim) is used instead of sim.
3. **Add variance across multiple seeds (3–5) to all quantitative results.**
4. **Include at least one CLIP-based or prompt-based baseline** — e.g., a variant that uses only the domain prompt with a standard segmentation head, or a CLIP-feature-extractor + UDA head combination.
5. **Specify all missing parameters** — M, χ, exact CLIP variant, and the definition of "containing the segmentation object" for the in-batch contrastive loss.
6. **Tone down novelty claims** — replace "for the first time" assertions with a precise articulation of what distinguishes UUDS from prior coupled approaches (e.g., SIFA, CycADA).
7. **Add a limitations section** discussing failure modes, sensitivity to χ, and overfitting concerns.

## Score and Decision

The paper proposes a sensible combination of CLIP-based dual prompts and uncertainty-guided pseudo-labeling for medical UDA, and the ablation study provides meaningful evidence that each component matters. However, the paper in its current form has several issues that prevent it from meeting the ICLR bar: (a) an internal contradiction in the architecture description (ViT vs. ResNet) that must be resolved before the method is reproducible; (b) a contrastive loss formulation with unclear optimization behavior; (c) no variance or statistical rigor on any result; (d) a baseline set that cannot distinguish whether improvements come from CLIP's backbone or the paper's specific design; and (e) underspecified implementation details for several critical parameters. These are fixable but collectively substantial enough that the paper as submitted does not convincingly demonstrate its claimed contributions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>