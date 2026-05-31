## Summary

This paper develops a learnable three-channel neural codec inspired by the Gray-Wyner Network (GWN), targeting efficient joint coding of two machine vision tasks by separating shared ("common") information from task-specific ("private") information. The paper extends classical Gray-Wyner theory to the lossy setting, proving bounds relating Gács-Körner and Wyner's lossy common information via interaction information (Theorem 1), and derives a tractable Lagrangian training objective with a tunable transmit-receive rate tradeoff parameter β (Theorem 2). Experiments on synthetic data, colorized MNIST edge cases, and two pairs of real vision tasks (segmentation + depth estimation; object + keypoint detection) show the proposed "Shared" architecture outperforms independent coding by an average of −81.58% BD-rate on transmit rate.

---

## Strengths

- **Genuine theoretical extension.** Theorem 1 extends Wyner's lossless result to the lossy setting, bounding both forms of lossy common information via interaction information. Theorem 2 reformulates the GWN Lagrangian in terms of entropy functions for deterministic encoders, enabling direct gradient-based optimization—an important bridge from theory to practice.

- **Well-designed ablation with ground truth.** The synthetic dataset provides analytically computable mutual information, joint entropy, and rate-distortion bounds, enabling direct comparison of empirical estimates with theory. This rigorously validates that the common channel captures the right amount of information under different β settings (Figure 3).

- **Edge-case coverage.** The colorized MNIST experiments with Dependent, Independent, and Mixture PMFs test the method at theoretically meaningful extremes—full dependence (MI = log₂10), zero dependence (MI = 0), and partial dependence (MI = 1.4 bits)—and the method behaves correctly in all three cases.

- **Significant empirical gains.** On COCO and Cityscapes, the proposed transmit-rate-optimized codec achieves +13.16% and +23.32% BD-rate relative to the Joint codec, while substantially outperforming Independent coding (+77.36% and +143.69%), confirming the practical utility of the common channel.

- **Clear motivation and structure.** The transmit-receive tradeoff is concisely formalized (Section 2.1), and the corresponding architectural and loss design choices flow naturally from the theory.

---

## Weaknesses

### Fatal
None.

### Major

1. **No comparison with existing multi-task learnable codecs.** The paper explicitly cites Chamain et al. (2021), Feng et al. (2022), and Guo et al. (2024) as related multitask codecs, noting their key distinction (no private channels). However, none of these are included as baselines. Even acknowledging the architectural difference (no private channels), comparing against them would situate the paper's contributions within the actual state of the art and clarify whether the three-channel design offers measurable gains over simpler shared-channel approaches beyond what the Joint baseline captures.

2. **Ad hoc masking mechanism (Eq. 14) lacks detailed justification in the main text.** The core operation—zeroing out entries where the two task-specific encodings of Y₀ disagree—is a discrete coincidence test on quantized integer tensors. The paper defers theoretical justification to Appendix C (not readable here) and relies on an auxiliary loss (Eq. 15) to make it work. In the main text, it is not shown how often elements agree in practice, whether the mechanism degenerates at low or high rates, or how sensitive results are to quantization resolution. Without this, the central architectural contribution appears heuristic.

3. **β ablation is incomplete for vision tasks.** The synthetic study clearly shows β = 3/2 is reasonable (Figures 3c-d), but the paper does not report results for multiple β values on the real-world vision benchmarks (Cityscapes, COCO). It is unclear whether the choice of β matters in practice for vision tasks or whether the gap to Joint depends on β.

### Minor

1. **The auxiliary loss weight γ = 1 is asserted without ablation.** The paper states that small and large γ both hurt performance but fixes γ = 1 without validating this choice empirically, even on the synthetic dataset.

2. **Both real-world task pairs involve closely related perceptual tasks.** Segmentation + depth and detection + keypoints are all scene-understanding tasks on similar image types. Testing a more divergent pair (e.g., classification + segmentation) would better stress-test the common information extraction.

3. **Cityscapes curves exhibit anomalous behavior.** The paper notes "some curves in the Cityscapes experiments have an increase in distortion with the lowest compression," attributed informally to lack of regularization. This artifact is not analyzed further, and it potentially undermines BD-rate estimates in that regime.

### Trivial
None.

---

## Nice-to-Haves

- Empirical measurement of how frequently Y₀^(1) and Y₀^(2) elements match across training, and how this varies with β and task pair, would directly validate the masking mechanism.
- A three-task extension experiment or at least a discussion of architectural complexity beyond the exponential channel-count scaling concern would help assess future scalability.
- Reporting actual encoding/decoding latency would clarify whether the three-encoder architecture introduces prohibitive overhead relative to single-task codecs.

---

## Novel Insights

The paper's most genuinely novel insight is that the interaction information I(X₁, X₂; Ẑ₁; Ẑ₂) serves as a tractable surrogate that bounds both lossy common information measures from above (Wyner's) and below (Gács-Körner), and that the gap between these measures is typically non-zero in practice (e.g., zero Gács-Körner CI for Gaussian sources). This motivates the transmit-receive tradeoff as a continuous design axis for practical codecs—not merely two extreme operating points—and Theorem 2 makes this axis directly optimizable via a single scalar β. This framing could be reused in other settings where partial information sharing is desirable without full joint coding.

---

## Suggestions

- Add at least one existing multi-task codec (e.g., Chamain et al. or Guo et al.) as a baseline, even if the comparison is labeled as approximate due to architectural differences.
- Report, for the masking mechanism, the average fraction of elements in Y₀ that are active (i.e., match) across different rates and tasks; this would empirically verify that the common channel is non-degenerate.
- Include a β sweep on at least one real-world task pair (e.g., COCO) to confirm that β = 3/2 is a robust choice outside the synthetic setting.
- Provide a brief ablation on γ ∈ {0.1, 1, 10} on the synthetic dataset to validate the fixed γ = 1 choice.

---

## Score and Decision

The paper makes a principled and original contribution: it extends classical Gray-Wyner theory to the lossy setting, derives a practical training objective, and demonstrates a learnable architecture that captures common information between vision tasks. The theoretical results are sound and the empirical validation is well-structured. The main gap—absence of existing multi-task codec baselines and incomplete justification of the masking mechanism in the main text—weighs against acceptance but does not invalidate the core claims. This is a borderline-accept paper that would benefit from modest revisions to close these gaps.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>