- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 6, 6, 5, 5
Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces QB-Net and QSB-Net, two families of binarized convolutional neural networks whose core innovation is a structural strategy: starting with few channels in shallow blocks and quadrupling channels during downsampling, combined with a novel smooth downsampling that applies two sequential 1-D downsampling steps (heightwise then widthwise). The models replace binarized 3×3 convolutions (used in ReActNetA) with FP32 depthwise separable convolutions plus binarized pointwise convolutions, reducing computational cost. On ImageNet-1K, QSB-Net-Large with SE attention achieves 71.2% Top-1 accuracy at 0.63×10⁸ OPs, with real-hardware latency measurements on Raspberry Pi 4B and Exynos processors confirming practical speedups.

## Strengths

1. **Channel quadrupling with shallow-thin/deep-wide design is well-motivated and effective**: The paper demonstrates that starting with few channels in shallow blocks and quadrupling during downsampling (Table 1, Figure 1(b)) produces strong accuracy at low OPs. QB-Net-Large achieves 69.8% Top-1 with 0.53×10⁸ OPs vs. ReActNetA's 69.4% with 1.34×10⁸ OPs — roughly 2.5× fewer OPs for slightly higher accuracy. The ×8 channel expansion ablation (Section 5.3) confirms that increasing deep-block complexity provides a 2.6% gain, directly supporting the design principle.

2. **Real-hardware latency measurements on multiple platforms**: Table 3 reports latency on Raspberry Pi 4B and Samsung Exynos-9820 using Larq Compute Engine, measuring 300-run averages. QB-Net-Large runs at 65.5 ms on RPi 4B vs. ReActNetA's 89.3 ms while achieving higher accuracy. This is rare and valuable in the BCNN literature, where OPs are often the only cost metric.

3. **Thorough ablation studies that validate individual design choices**: Section 5.3 isolates the impact of removing learnable bias before DS convolutions (−2.1%), using 1×1 BCONV instead of 3×3 in shallow channels (−1.8%), and applies 8-bit quantization to DS conv + FC layers (70.8% vs. 70.6%, minimal drop). These controlled experiments establish that the reported gains come from specific architectural decisions rather than training recipe engineering.

4. **Generalization to semantic segmentation**: Table 4 shows QSB-Net-Large(SE2) achieves 69.2 mIoU on PASCAL VOC, outperforming FP32 ResNet18 (68.2) and the binarized CBNN (68.5), demonstrating the architecture transfers beyond image classification.

5. **Training-from-scratch results confirm structural contribution**: Section 5.3 reports QSB-Net-Large(SE1) trained from scratch (no teacher-student) achieves 67.5% Top-1 — outperforming QuickNet's 63.3% (which also uses teacher-student). This rules out the possibility that all gains come from the training recipe.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison with AdaBin and ReBNN in the main evaluation table**: The paper cites AdaBin (Tu et al., 2022, ~71.0% Top-1) and ReBNN (Xu et al., 2023, ~70.7% Top-1) in Related Work (Section 2) but omits their results from Table 2. QSB-Net-Large(SE2) achieves 71.2% — the margin over AdaBin's reported 71.0% is 0.2%, well within training variance. Without knowing AdaBin's OPs and without including these methods in the comparison, the paper's central claim of "outperforming other counterparts" and "overcoming the limitations of existing BCNNs" is not adequately supported. The reader cannot tell whether the architectural innovations (channel quadrupling, smooth downsampling) are responsible for the accuracy or whether a simpler architecture with a stronger training recipe would match it. This is the single most important gap in the evaluation.

### Minor

2. **Frequency-domain analysis is qualitative and based on a single sample**: Section 4.4 and Figure 5 use output features from a single goose image to claim that channel quadrupling provides a wider dynamic range. No statistics (e.g., average over the validation set, correlation with accuracy, control experiment with artificially narrowed range) are provided. The claimed theoretical insight is plausible but unsubstantiated; the observed accuracy gains could simply come from increased parameter count in deep blocks rather than any frequency-domain property.

3. **Smooth downsampling accuracy-latency tradeoff is acknowledged but not analyzed in depth**: QSB-Net-Large improves Top-1 by 0.8% over QB-Net-Large (69.8% → 70.6%) at a cost of 20.7 ms additional latency on RPi 4B (a 32% increase from 65.5 ms to 86.2 ms). The paper mentions this (line 194) but does not provide a pareto-style accuracy vs. latency comparison, discuss under what deployment scenarios this tradeoff is acceptable, or compare the efficiency ratio (accuracy per ms) against alternatives.

4. **No variance or confidence intervals reported**: No standard deviations, multiple seeds, or confidence intervals are reported for either accuracy or latency measurements. Given that the margins over some baselines are small (e.g., 0.2% vs. AdaBin's reported number), the absence of any variance estimation makes it impossible to assess whether performance differences are statistically significant.

5. **Large model architectures are not fully specified**: The Large variants (QB-Net-Large, QSB-Net-Large) are described only in footnotes to Table 1 ("adopt TypeQ and TypeQS in the 9-th block and set the number of channels as 2048 from the 10-th block"). The exact channel progression per block, number of blocks per stage, and stride details are not given with the same level of detail as the Small variants, which hurts reproducibility.

### Trivial
None.

## Nice-to-Haves

- **Include AdaBin and ReBNN results in Table 2**, even if only as reported numbers from their papers (with OPs if available). This would directly address the major evaluation gap.
- **Quantify the frequency-domain analysis**: Compute average frequency-domain dynamic range over the validation set and show a scatter plot against accuracy.
- **Provide an accuracy-vs-latency pareto plot** for QB-Net, QSB-Net, and QSB-Net+SE variants to clarify deployment tradeoffs.
- **Ablate channel quadrupling vs. doubling** at the same downsampling points to directly test whether the ×4 factor is optimal, or whether simpler ×2 expansion would suffice.

## Removed Points

These points were raised but are removed or demoted for the following reasons:

- **"Smooth downsampling tradeoff not discussed"** (Harsh Critic, Critical Issue 3): The paper *does* discuss this tradeoff (line 194: "Although QSB-Net-Large can enhance Top-1 accuracy by 0.8%, its latency increased by 20.7 ms"). The critic's numerical claim of 0.6% is also inconsistent with the paper's stated 0.8%. The underlying concern about insufficient depth of analysis is kept as a Minor weakness.
- **"Large FC layer unresolved"** (Harsh Critic, Missing Parts): The paper explicitly identifies the FC layer storage as a weakness (line 196: "the main weakness of the proposed models is the increasing storage costs for the final FC layer") and provides solutions (8-bit quantization, binarized convolutions) with experimental validation. This is not an omission.
- **"Frequency-domain analysis is a strength showing wider dynamic range"** (Strength Finder): Moved here because, as verified, the analysis is based on a single image and lacks statistics — the weakness (Minor #2) overrides the claimed strength per the disagreement rule.
- **"Section 3 is vague"** (Harsh Critic, Section-by-Section): This is a subjective style critique without a concrete, specific problem identified in the paper's content.
- **"Design choice in Section 4.2 presented as post-hoc fix"** (Harsh Critic, Section-by-Section): The paper presents this transparently as an empirical finding from ablations, which is standard practice.
- **"Missing appendix, proofs"**: Parser-stripped content; assumed present in the original submission.

## Novel Insights

The harsh critic and strength finder together surface a tension that the paper does not fully resolve: the channel-quadrupling strategy is clearly effective (ablations show large gains), and the smooth-downsampling trick provides a real but modest accuracy improvement at a notable latency cost. However, neither reviewer identified a deeper insight beyond what the paper already articulates — the basic idea of concentrating model capacity in deep blocks while keeping shallow blocks thin for BCNNs is well within the scope of what the paper itself explains. The one genuinely novel observation from cross-referencing the reviews is that the training-from-scratch experiment (Section 5.3) is underappreciated by the harsh critic but actually serves as strong evidence that the architecture itself — not just the teacher-student training recipe — drives the gains.

## Suggestions

1. **Restore AdaBin and ReBNN to the comparison table.** This is the single change that would most strengthen the paper. Even if their OPs are unknown, include their reported Top-1 accuracy alongside a note about architectural differences. If the gap is indeed marginal, discuss it explicitly rather than leaving it implicit.

2. **Add statistical rigour to the frequency analysis.** Either compute average frequency range over a representative subset of ImageNet-1K or replace the qualitative claim with a more rigorous justification (e.g., effective rank of feature representations).

3. **Add a pareto-style accuracy vs. latency plot** for all QB-Net and QSB-Net variants, including the SE variants, so readers can assess deployment tradeoffs at a glance.

4. **Provide full architectural specifications for Large variants** in the main paper or appendix, matching the detail of Table 1 for Small variants.

5. **Tone down the "outperforming" language** or explicitly qualify it (e.g., "outperforms prior BCNNs with comparable or lower OPs among methods using teacher-student training on MobileNet-based architectures").
