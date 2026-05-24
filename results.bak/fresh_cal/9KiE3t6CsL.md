Now I have a solid understanding of the paper. Let me write the consolidated review.

---

## Summary

ALBAR proposes an adversarial training framework for debiasing action recognition models against both background and foreground static biases. The key idea is to sample a static clip (a single frame repeated) from the video, apply an adversarial cross-entropy loss that penalizes correct predictions from static cues, combine it with entropy maximization to prevent trivial "label-flipping" solutions, and add a gradient penalty to stabilize training. The method requires no attribute annotations or separate critic models. The paper achieves state-of-the-art contrasted accuracy on the HMDB51 bias protocol (+12% over prior methods), identifies and fixes a background-leakage flaw in the existing UCF101 bias evaluation protocol using segmentation masks, and demonstrates downstream benefits on anomaly detection and temporal action localization.

## Strengths

- **Adversarial debiasing without attribute labels or separate critic models.** The method uses only a static clip sampled from the video itself, applying losses through the same 3D encoder. This is a meaningful methodological simplification over prior work that requires scene/object classifiers or separate 2D critics. Evidence: Sections 3.3–3.4 and the Introduction ("we break away from this formulation and design an adversarial framework based on a single 3D encoder model").

- **Large and well-documented improvements on debiasing benchmarks.** ALBAR achieves **53.02% contrasted accuracy** on the HMDB51 SCUBA/SCUFO protocol, improving over the previous best (StillMix, 40.91%) by over 12% absolute. The combination with StillMix pushes this further to 53.68%. These gains are large enough that tuning artifacts cannot explain them. Evidence: Table 1 and Section 4.4.

- **Identification and mitigation of a benchmark flaw.** The paper demonstrates that the existing UCF101 bias protocol uses bounding boxes that leak background information around the subject, and proposes a corrected protocol using SAMTrack segmentation masks with manual verification. This is a meaningful secondary contribution that improves evaluation rigor. Evidence: Section 4.2, Figure 2.

- **Ablation study validates each loss component.** Table 3 shows that (a) the adversarial loss alone causes a label-flipping degenerate solution, (b) entropy maximization prevents this by forcing uniform predictions on static clips, and (c) the gradient penalty stabilizes training. All three components are necessary for the best result. This is clear and well-motivated.

- **Compatibility with augmentation-based methods.** ALBAR can be combined with StillMix augmentations to further improve performance (53.02% → 53.68%), showing it captures different debiasing signals than augmentation-based approaches. Evidence: Section 4.4.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Unclear whether baselines on the improved UCF101 protocol were reproduced under the same setup.** The paper introduces a new evaluation protocol (segmentation-based masks for UCF101), reports results for multiple baselines on this protocol in Table 2, but does not explicitly state whether these baselines were re-trained or re-evaluated using the new masks, or whether numbers are taken from prior papers that used the old (leaky) protocol. If the latter, the comparison would be unreliable since the test conditions differ. Given that the masks change the test data, this needs clarification. However, the main HMDB51 results (Table 1) do not suffer from this concern.

- **No variance reported despite averaging over 3 runs.** The paper states it reports "average Top-1 accuracy across 3 runs" but does not provide standard deviations or confidence intervals for any table. While the large margins on HMDB51 make this unlikely to change conclusions, this limits the reader's ability to assess result stability, particularly for smaller margins (e.g., UCF101 in Table 2, downstream tasks in Table 5).

- **Loss weights and hyperparameter tuning are not discussed.** The combined loss uses three weights (ω_adv, ω_ent, ω_gp), but the paper does not state how these were chosen, whether a validation search was performed, or how sensitive the method is to their values. This matters for reproducibility and for understanding the method's robustness.

- **Kinetics400 SCUBA/SCUFO results are deferred to the appendix.** The abstract and introduction claim evaluation on Kinetics400, but the main paper does not include these results. Given that Kinetics400 is the pretraining dataset and the largest benchmark, showing whether debiasing transfers to Kinetics-scale evaluation would strengthen the paper's generality claims.

### Trivial

None. (Formatting issues in the parsed text are PDF extraction artifacts, not author errors.)

## Nice-to-Haves

- A side-by-side comparison on the original (leaky) UCF101 protocol alongside the improved protocol would help readers directly see the effect of the leakage.
- A brief discussion of computational overhead (training speed, memory) from the additional adversarial losses would help practitioners assess practical cost.
- Training the debiased model directly on the target datasets (UCF_Crime, THUMOS14) rather than using a frozen HMDB51-trained encoder would be a stronger downstream evaluation, though the zero-shot transfer result is already evidence of better feature quality.

## Removed Points

- **Criticism about "whether baseline hyperparameters were tuned per method" (Harsh Critic).** The harsh critic himself notes the margin is large enough that tuning artifacts are unlikely to explain the improvement, making this a speculation rather than a concrete identified problem. Removed as a non-substantive concern.
- **Criticism about "qualitative results not rigorous" (Harsh Critic).** The paper presents the integrated gradients as "corroborative evidence, not primary," which is a reasonable framing. The critic's own assessment agrees. Removed because it is not presented as a weakness by the critic.
- **"The paper could include a comparison on the original UCF101 protocol side by side in the main paper" (Harsh Critic).** This is a presentation suggestion, not a weakness. Moved to Nice-to-Haves.
- **Strengths from Strength Finder about "addressing important problem" and similar generic framings.** The retained strengths are all specific and grounded. No additional generic strengths were present.

## Novel Insights

The reviews converge on the observation that the paper's main innovation is not architectural but *loss-functional*: it repurposes the same 3D encoder as both the primary classifier and the adversarial component by feeding it a static version of the same input, then applying a three-term loss (adversarial CE + entropy maximization + gradient penalty) that prevents the degenerate "label flipping" solution that plagues naive adversarial debiasing. This design choice — using the video's own content as the adversarial signal rather than a separate model or external attribute labels — is both practically convenient and conceptually clean. The reviews also highlight that the corrected UCF101 protocol using segmentation masks is a non-trivial contribution: the existing bounding-box protocol leaks enough background to provide a shortcut, and fixing it changes the ranking of methods (the margin shrinks for ALBAR on the corrected protocol).

## Suggestions

- Clarify in the experimental section whether all baselines in Table 2 were re-evaluated on the improved UCF101 protocol under the same training setup, or if numbers were obtained differently.
- Report variance (standard deviation) for the 3-run averaged results, at least for the main contrasted accuracy figures.
- Add a brief discussion of loss weight selection (tuning procedure, validation set, sensitivity analysis) and consider including ω values in the main paper.
- Move the Kinetics400 SCUBA/SCUFO results from the appendix into the main paper (at least a summary table), since the abstract references them.

## Score and Decision

This is a strong paper with a clean, practical method, substantial empirical improvements, a useful secondary contribution (protocol fix), and thorough ablations. All identified weaknesses are minor presentation/detail issues that do not threaten the core claims. The contribution — a practical, effective adversarial debiasing framework for action recognition that requires no attribute labels — is well-supported and significant.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>