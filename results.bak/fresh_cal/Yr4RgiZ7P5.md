Now I have a complete picture. Let me produce the final consolidated review.

## Summary

This paper introduces the Distorted Shape Testbench (DiST), a benchmark that measures global shape sensitivity through an oddity detection task: given two texture-synthesized images with preserved local features but distorted global structure, plus one original image, a model must identify which image is most different. The paper makes three main contributions: (1) showing that models scoring high on the standard cue-conflict shape bias benchmark (e.g., ResNet50-SIN) do not outperform standard baselines on DiST, challenging the equivalence between style-transfer resistance and global shape sensitivity; (2) providing human psychophysical data (16,800 trials, 32 subjects, 85.5% accuracy) establishing a human baseline; and (3) proposing DiSTinguish, a training method that augments classification with shape-distorted data, improving DiST performance while maintaining accuracy on standard tasks.

## Strengths

- **Key empirical finding that style-transfer resistance ≠ global shape sensitivity** (Section 4.1, Figure 5): The paper demonstrates that ResNet50-SIN (highest cue-conflict shape score) performs no better than a standard ResNet50 on DiST (~60%). This is a concrete, specific result that directly supports the paper's central thesis — that prior shape-bias evaluations may primarily measure local rather than global shape sensitivity. The finding is well-supported by the data shown in Figure 5 across many model architectures.

- **Novel benchmark (DiST) with clean task design and human psychophysical validation** (Section 3.1–3.2): DiST uses Gram-matrix texture synthesis (Gatys et al., 2015) to distort global shape while preserving local features, then formulates evaluation as an oddity-detection task (N=2 distorted + 1 original). The paper includes a rigorous human experiment with 32 subjects, 16,800 trials, 800 ms stimulus presentation, and no feedback, establishing a human baseline of 85.5%. This provides both a well-motivated alternative to cue-conflict benchmarks and a meaningful performance target.

- **DiSTinguish training improves global shape sensitivity and is complementary to style augmentation** (Section 4.2, Tables 2–3): On ImageNet10 (all trained from scratch with identical configurations), DiSTinguish improves DiST from 50.4% to 57.0% (DiSTinguish-C) and 55.5% (DiSTinguish-A). On ImageNet1K, DiSTinguish raises DiST to 67.6% and combining with stylized augmentation reaches 69.7%, while maintaining competitive original accuracy. The ImageNet10 experiment is cleanly controlled and supports the method's efficacy.

- **Qualitative sensitivity-map analysis provides mechanistic insight** (Section 4.2.3, Figure 7): SmoothGrad visualizations show that stylized-augmented models focus on single local features (e.g., an eye) while DiSTinguish-trained models attend to broader object regions. This mechanistic evidence supports the claim that the two training methods target different levels of shape information.

## Weaknesses

### Fatal
None.

### Major

- **Unfair comparison in ImageNet1K training experiment (Table 3)**: The paper states: "Except for the pretrained Baseline model, where we directly use the IMAGENET1K V1 weights, all other models are trained under identical configurations." This means the baseline uses pretrained ImageNet weights (trained for many epochs) while DiSTinguish, Stylized Augmentation, and their combination are trained from scratch. The claim that DiSTinguish "maintains comparable results on the original dataset" (74.5% vs. baseline 76.1%) is not interpretable given this confound — the performance gap could be due to insufficient training of the from-scratch models rather than a property of DiSTinguish. A fair comparison requires either training all models from scratch under identical conditions (as was done correctly in the ImageNet10 experiments) or fine-tuning all from the same pretrained checkpoint. This weakness directly affects the paper's third core claim about "preserving accuracy."

### Minor

- **DiST benchmark validation is implicit rather than demonstrated**: The paper relies on the well-established property of Gram-matrix texture synthesis (Gatys et al., 2015) that local texture statistics are preserved while global spatial structure is randomized. However, the paper does not include a control experiment demonstrating that a model with no access to global shape (e.g., a BagNet or patch-based classifier) performs near chance on DiST, or that humans fail the task when local cues alone are available. While the benchmark's construct validity is reasonable given the established literature, explicit validation would strengthen the claim that DiST measures *global* shape sensitivity rather than some other property of the distorted images. This is a matter of evidence depth, not a fatal flaw.

- **Reliance on a single distortion method for both evaluation and training**: Both DiST evaluation and DiSTinguish training use the same texture-synthesis pipeline (Gatys et al., 2015). This raises the concern that DiSTinguish-trained models may learn to detect artifacts specific to this pipeline rather than acquiring a general notion of global shape. The paper does not test generalization to other forms of global shape distortion (e.g., jigsaw permutations, elastic warping, random patch reorderings). The claim that DiSTinguish improves "global shape sensitivity" would be significantly strengthened by validation on at least one alternative distortion type. The sensitivity map analysis partially mitigates this concern but does not resolve it.

- **ViT conclusion is overclaimed relative to the evidence**: The paper concludes "ViT models do not show significant advantages over CNNs on DiST." Table 1 shows only three ViT variants (S/16, B/16, L/16). No confidence intervals or statistical tests are reported. While the claim is modest (absence of advantage rather than inferiority), the current evidence is anecdotal — limited to a few variants without sampling error quantification. The broader model survey (Figure 5) does include additional architectures (BEiT, DeiT, ConvNeXt), strengthening the conclusion somewhat, but the specific ViT-centric claim would benefit from more variants and proper intervals.

### Trivial

- The paper uses final-layer features for the DiST metric without discussion or ablation of why this layer was chosen over intermediate layers, which are known to encode more local information. A brief justification or ablation would improve confidence in the metric design.
- The number of optimization steps for DiST image generation and specific VGG layers used for Gram-matrix matching are not fully specified, slightly reducing reproducibility.
- Human performance is reported as a single mean (85.5%) without inter-subject variability (standard deviation or confidence intervals).

## Nice-to-Haves
- Report rank correlations (Spearman's ρ or Kendall's τ) between cue-conflict and DiST scores across all tested models to quantify the divergence shown qualitatively in Figure 5.
- Compare DiSTinguish-A performance on the *validation* DiST across different approximation steps (5, 10, 20, 50) on ImageNet10 to show stability of the approximation.
- Quantify the sensitivity map analysis (e.g., percentage of sensitivity mass inside/outside object bounding box) rather than relying solely on qualitative comparisons.

## Removed Points
These points are flagged to be removed — treat them with caution:

- **"The texture synthesis does not guarantee local features are preserved / optimization could introduce artifacts"**: Demoted from Fatal to removed. This is speculative. The paper uses a well-established method (Gatys et al., 2015) with extensive literature validating its property of preserving texture statistics while randomizing global structure. The reviewer offers no evidence of systematic artifacts. A control experiment would be nice but the construct is standard.
- **"Missing Swin/DeiT/ConvNeXt from comparison"**: Removed. The paper's model survey (Section 4.1) explicitly includes BEiT, DeiT, and ConvNeXt as tested models. The ViT-specific comparison in Table 1 is focused on the ViT family; the broader comparison appears in Figure 5.
- **"Missing rank correlations"**: Removed — this is a nice-to-have, not a weakness.
- **"The paper does not discuss limitations"**: Removed — this is a presentation suggestion, not a substantive weakness.
- **"Stylized augmentation's original accuracy (77.8) is higher than baseline (76.1) — unexpected, likely artifact"**: Removed — this actually suggests the from-scratch training is competitive, which weakens the reviewer's own argument about the unfair comparison. Not a weakness.
- **"Missing related works"**: Removed per instructions (no external sources to confirm).
- **"Typos / formatting / grammar"**: Removed per instructions (parser artifacts, not author errors).

## Novel Insights

The harsh critic correctly identifies the two most significant tensions in the paper — the unfair ImageNet1K baseline comparison and the reliance on a single distortion method — but also generated several speculative or overstated critiques (particularly around DiST construct validity) that do not hold up against the paper's content. The strength finder accurately identifies the paper's genuine contributions but overweights the ViT finding relative to its evidentiary basis. A genuinely novel observation that emerges from synthesizing both reviews is that the paper's strongest evidence actually resides in two places the reviews underappreciate: (1) the ImageNet10 experiments (Table 2), which are cleanly controlled (all from scratch, same configuration) and show DiSTinguish-C achieving 57.0% vs. baseline 50.4% on DiST, and (2) the orthogonal-efficiency finding in Table 3 showing DiSTinguish + Stylized Augmentation (69.7%) outperforming either alone on DiST while maintaining competitive accuracy — this suggests the two methods genuinely target different levels of shape information, consistent with the sensitivity map analysis. The paper's core contribution — challenging the equation of style-transfer resistance with global shape bias — is well-supported by the DiST model comparisons (finding 1) and does not depend on the training experiments.

## Suggestions

1. **Fix the ImageNet1K comparison**: Retrain all models from scratch (including the baseline) with identical random seeds and training schedule, or fine-tune all from the same pretrained checkpoint. This is the single most impactful fix.
2. **Add at least one alternative distortion type** (e.g., jigsaw shuffling or elastic warping) to validate that DiSTinguish-trained models generalize beyond the specific texture-synthesis pipeline. Even a small-scale experiment on ImageNet10 would substantially strengthen the paper.
3. **Include a control experiment** showing that a local-features-only model (e.g., BagNet) performs near chance on DiST, as explicit construct validation for the benchmark.
4. **Report confidence intervals** for key metrics (DiST scores, human performance, training results) and statistical tests where appropriate.

## Score and Decision

**Originality**: High — the paper identifies a meaningful gap in how shape bias is measured and proposes a genuinely different approach.  
**Importance of research question**: High — understanding what "shape bias" benchmarks actually measure matters for the community's research direction.  
**Claims support**: Moderate — the core observation (style-transfer ≠ global shape) is well-supported; the training method claims are partially compromised by the unfair baseline comparison.  
**Soundness of experiments**: Moderate — the human psychophysics and ImageNet10 experiments are sound; the ImageNet1K comparison has a significant confound.  
**Clarity of writing**: Adequate — the core ideas are communicated clearly, though some implementation details are sparse.  
**Value to community**: High — the benchmark, human data, and empirical findings are likely to influence future work on shape bias.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>