Now I have all the information needed. Let me compile the final review.

## Summary

This paper proposes AdcVSR, a compressed one-step diffusion model for real-world video super-resolution (Real-VSR). The method builds on the AdcSR image-domain compression framework by: (1) augmenting a pruned 2D SD2.1 backbone with lightweight 1D temporal convolutions to add temporal modeling, and (2) introducing a dual-head, dual-domain adversarial distillation scheme that disentangles detail richness and temporal consistency objectives. Distilling from the large 3D DiT teacher DOVE, AdcVSR achieves a 95% parameter reduction and 8× inference speedup while maintaining competitive video quality, and attains the best temporal consistency (warping error) among 11 compared methods.

## Strengths

**1. Novel dual-head, dual-domain discriminator design with clear causal evidence.** Table 3 directly isolates the effect of the proposed discriminator scheme: replacing either the dual-head aspect or the dual-domain aspect causes one of the two key metrics (CLIPIQA or E_warp*) to degrade substantially, while only the full design achieves strong results on both simultaneously (CLIPIQA 0.6861, E_warp\* 2.22 on YouHQ40). This is strong, clean evidence that the disentanglement works as intended.

**2. Best temporal consistency among all 11 compared methods on both synthetic and real-world benchmarks.** Table 1 shows AdcVSR achieves the lowest warping error on UDM10 (1.67 vs. teacher DOVE's 2.22) and VideoLQ (6.74 vs. DOVE's 8.41), outperforming even multi-step diffusion models and its own teacher. This is a measurable head-to-head advantage.

**3. 95% parameter reduction and 8× speedup over teacher DOVE with competitive quality.** These core efficiency claims are well-supported by Table 1: DOVE (10.55B params, 4.42s) → AdcVSR (0.57B, 0.55s), while AdcVSR ranks top-3 on most quality metrics across multiple datasets.

**4. Well-motivated architectural hypothesis validated by controlled comparison.** Table 2 shows that the 2D backbone alone (AdcSR) collapses (DISTS 0.2418, E_warp\* 4.43), while adding 1D temporal convolutions restores performance close to a pruned 3D DiT (DISTS 0.2112 vs. 0.2098) at 7% of its parameters.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

**1. Factual ranking error in Figure 4 caption.** The caption states AdcVSR achieves "the second-lowest parameter number, and the second-highest inference speed." Table 1 shows AdcVSR (0.57B params, 0.55s) is *third* in both rankings, behind RealBasicVSR (0.04B, 0.35s) and AdcSR (0.46B, 0.52s). While the core efficiency claims (95% reduction, 8× speedup vs. DOVE) are correct and well-supported, this localized factual error in a figure caption weakens the paper's credibility and should be corrected.

**2. Temporal modeling capacity with kernel-3 1D convolutions is not analyzed.** The paper relies on 1D temporal convolutions with kernel size 3 to enforce temporal consistency, but provides no analysis of the effective temporal receptive field, no ablation varying the kernel size, and no discussion of whether the receptive field is sufficient for the evaluated videos. The claim that "1D temporal convolutions are sufficient" rests primarily on the comparison to a 2D-only baseline (Table 2) rather than on direct characterization of temporal modeling capacity. This is a gap the authors could address with targeted analysis.

**3. Warping error improvement over the teacher is unexplained and potentially confounded.** AdcVSR achieves lower warping error than its teacher DOVE (1.67 vs. 2.22 on UDM10), which is unusual for a compressed student. Lower warping error can result from genuinely better temporal coherence or from reduced high-frequency detail (blurrier frames produce smaller optical flow errors). Table 1 shows LPIPS degrades substantially (0.2648 → 0.3065, +15.7%), which is consistent with some detail loss. While the ablation in Table 3 shows the dual-head design maintains CLIPIQA, the mechanism by which the student surpasses the teacher in consistency is never explained. An analysis on detail-preservation metrics in temporally stable vs. high-motion regions would clarify this.

**4. The comparison to the original ADC pipeline is partially incomplete.** Although Table 2 compares against a pruned 3D DiT (the original ADC approach applied to DOVE) and a 2D-only AdcSR, neither row represents exactly "original ADC pipeline (2D student + single-head discriminator) trained with DOVE as teacher." The 2D row (AdcSR) was trained with a different teacher (PiSA-SR), not DOVE. A direct ablation controlling for the teacher while isolating the effect of the architecture and dual-head scheme would strengthen the "Improved ADC" framing.

### Trivial
None.

## Nice-to-Haves

- **Code/model release** would significantly increase the practical value given this is a compression method.
- **A dedicated limitations section** discussing the limited temporal receptive field, dependence on AdcSR's pruning, and the detail-head labeling choice (no positive supervision from real videos for the detail head).
- **Statistical significance** (confidence intervals / variance) for key metrics, given the stochastic nature of adversarial training.
- **An analysis of the detail-head labeling choice:** real video details are labeled "unlabeled" (y_d=0), meaning the detail head only receives positive supervision from static images. This design choice is explained but not ablated.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"Efficiency claims are overstated"** (harsh critic's broader framing): The paper's core efficiency claims (95% parameter reduction, 8× speedup vs. DOVE) are factually correct and properly attributed. The paper explicitly states it adopts AdcSR's pruned backbone. The critic's argument that these gains are "inherited" conflates the compression technique (from AdcSR) with the compression measurement (against the teacher DOVE). The paper correctly measures compression against its own teacher; AdcSR was not trained from DOVE. **REMOVED** — the criticism misattributes the claim.

- **"Missing baseline: original ADC applied to Real-VSR"** (harsh critic's #2): The paper includes this baseline in Table 2 ("3D (A Pruned DOVE)") which is explicitly described as "obtained by the original ADC approach." The critic's claim that this comparison is absent is factually incorrect. The subtler missing ablation (2D student + original ADC pipeline + DOVE teacher) is preserved as Minor weakness #4 above. **REMOVED** the stronger framing.

- **"Dual-head discriminator labeling concern"** (harsh critic's Section 3.3 note): The paper clearly explains the motivation for labeling real video details as "unlabeled" — to prevent the detail head from penalizing real-world temporal variation. This is an explicitly reasoned design choice, not an oversight. **REMOVED**.

- **"Feature-domain discriminator uses same architecture as generator"** (harsh critic's Section 4.1 note): The discriminator backbone is *frozen* (pretrained), and only the added convolution layers and heads are trainable. This is standard practice in adversarial training and not a concern. **REMOVED**.

- **"Comparison fairness"** and **"No Teacher HR GT Only"** criticisms: These are standard experimental practices properly executed. **REMOVED**.

- **"Missing related works," formatting, and reproducibility nitpicks**: Removed per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the Figure 4 caption** to accurately reflect the ranking shown in Table 1 (third-lowest parameters, third-fastest inference).
2. **Add an analysis of temporal receptive field** — compute the effective receptive field of the stacked 1D convolutions and ablate kernel size (e.g., compare kernel sizes 1, 3, 5) to support the claim that kernel-3 convolutions are sufficient.
3. **Analyze the warping error improvement over DOVE** — compare warping error on temporally stable regions vs. high-motion regions, or add a controlled experiment that correlates warping error with a detail-preservation metric to disentangle the confound.
4. **Add a direct ablation**: train a 2D-only student (no temporal convs) with DOVE as teacher using the original single-head discriminator, to isolate the contribution of the 2D+1D architecture from the switch of teacher.
5. **Add error bars or confidence intervals** for the key metrics (especially E_warp\* and CLIPIQA) to assess whether differences between methods are statistically significant.

## Score and Decision

### Calibration Report

**Retrieved Anchors (all rounds):**

| Anchor | Score | Round & Source | Comparison to this paper |
|--------|-------|----------------|-------------------------|
| Distillation-Free One-Step Diffusion (DFOSD) | 4.75 | R1-topic-mid | Weaker: criticized for marginal optimization and lack of novelty; this paper has clearer contributions and better ablations |
| AddSR | 5.00 | R1-topic-mid / R2 | Similar quality: AddSR had perception-distortion issues and missing baselines; this paper has slightly better ablation design |
| DiffIR2VR-Zero | 5.25 | R1-weakness-Q4 | Similar quality: training-free method with limited novelty; this paper has a stronger method contribution |
| Does Diffusion Beat GAN | 5.75 | R2 | Stronger in rigorousness but weaker in novel contribution; this paper proposes a new method with good validation |
| Multi-Student Diffusion Distillation | 4.25 | R2 | Weaker: contested contribution with mixed reviews (3,8,3,3) |
| Dissecting Arbitrary-scale SR Capability | 5.25 | R2 | Similar quality: analysis paper without new method |
| VideoDiT | 2.50 | R1-topic-low | Much weaker: unclear methodology and evaluation issues — this paper shares none of those failures |

**Round-1 bracket:** 4.5–6.0.

**Narrowing:** Round 2 anchored the paper against AddSR (5.00), DFOSD (4.75), DiffIR2VR-Zero (5.25), and Does Diffusion Beat GAN (5.75). The paper under review is stronger than DFOSD and AddSR (cleaner ablations, better contribution isolation), comparable to DiffIR2VR-Zero (but with a stronger method), and weaker than the analysis-paper Does Diffusion Beat GAN in rigorousness.

**What the low-band anchors (2.5–3.2) failed at:** unclear methodology, unsound evaluation, insufficient support for claims. This paper does NOT share those failures — its methodology is sound, evaluation is standard, and core claims are well-supported.

**Final position:** 5.5. The paper has genuine contributions (dual-head discriminator with clean ablation, best temporal consistency, substantial compression), supported by thorough experiments. The issues are minor (a localized caption error, some analytical gaps) and do not undermine the core claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>