## Summary
The paper proposes EDPA (Embedding Disruption Patch Attack), an adversarial patch attack targeting Vision-Language-Action (VLA) models that requires access only to the visual encoder—not the full model, action space, or robot-platform knowledge. EDPA uses two complementary loss functions: a contrastive loss maximizing embedding discrepancy between clean and adversarial inputs, and an alignment loss disrupting visual-linguistic correspondence. The paper also proposes an adversarial fine-tuning scheme for the visual encoder as a defense. Experiments on the LIBERO benchmark across three state-of-the-art VLA models (OpenVLA, OpenVLA-OFT, π₀) support the effectiveness of both attack and defense.

---

## Strengths

- **Relaxed threat model with clear motivation.** EDPA's primary contribution—reducing attack prerequisites from full-model access + action-space knowledge to encoder-only access—is well-motivated and clearly evidenced by Table 1 and Figure 1. This makes the attack applicable to a wider range of VLA architectures and robotic platforms.

- **Broad multi-model evaluation.** Evaluating across three distinct VLA models (OpenVLA, OpenVLA-OFT, and π₀) with different architectures and camera configurations, on all four LIBERO task suites, provides substantial empirical coverage and reveals meaningful differences in robustness across models.

- **Attack + defense completeness.** Providing both the attack and a principled defense (adversarial fine-tuning of the visual encoder) within a single framework makes the work self-contained and immediately actionable for the community.

- **Interesting overfitting hypothesis.** The observation that adversarial patches consistently exhibit robotic-arm-like patterns, and the corresponding hypothesis that VLA visual encoders overfit to robotic arm appearance due to data scale/viewpoint limitations, is a genuinely interesting insight that could inform future VLA design.

---

## Weaknesses

### Fatal
None.

### Major

1. **"Model-agnostic" terminology is misleading.** The paper titles the attack as "model-agnostic," but the experiments generate a separate patch for each target model's own encoder. True model-agnosticism—one patch transferring across architectures without access to the target's encoder—is never demonstrated. What EDPA actually achieves is *encoder-sufficient* attacking (no need for the LVLM backbone, action space, or robot type), which is still a valuable contribution, but calling it "model-agnostic" overstates the result. The paper should clarify this distinction explicitly, e.g., by testing whether a patch optimized on one VLA's encoder degrades a different VLA's performance.

2. **Defense effectiveness is overstated.** The abstract and Section 4.2 claim the defense "effectively mitigates this degradation," but the post-defense failure rates remain very high in several settings: 73.9% (Libero-Goal with EDPA), 91.2% (Libero-Long with EDPA), and 97.4% (Libero-Long with UADA) compared to clean baselines of 26.9%, 48.1%, and 48.1% respectively. The defense is never close to recovering clean performance in the harder task suites. The framing should be recalibrated to reflect that the defense *partially reduces* the attack impact rather than "effectively mitigates" it.

3. **No encoder-free white-box ablation.** There is no comparison to a version of EDPA with the backbone included in the loss (i.e., a stronger oracle attack). Without this, it is impossible to quantify the cost of the encoder-only constraint in terms of attack strength, which is central to the paper's motivation.

### Minor

1. **Defense evaluated on one model only.** Adversarial fine-tuning is tested exclusively on OpenVLA. Whether this defense transfers to OpenVLA-OFT and π₀ is left unexplored, limiting generalizability claims.

2. **Image-instruction alignment loss ambiguity.** Equation (3) uses an absolute value of cosine-similarity change, which neither explicitly maximizes nor minimizes alignment—it just measures deviation from the original alignment. A more principled formulation would explicitly minimize alignment between adversarial image embeddings and the correct instruction's language embeddings. No analysis is provided showing whether the adversarial patch's alignment with the instruction increases or decreases.

3. **Patch size not ablated in main text.** A 50×50 patch on a 224×224 image is substantial (~22% linear coverage). The sensitivity appendix is mentioned but not accessible; an ablation in the main paper on patch size would strengthen the contribution.

### Trivial

- Minor phrasing inconsistencies (e.g., "In comparison to prior methods" vs. "Compared to").

---

## Nice-to-Haves

- A cross-model transferability experiment (patch trained on OpenVLA's encoder applied to π₀) would directly validate or refine the "model-agnostic" claim.
- Reporting success rates (not just failure rates) in the defense tables would make the residual vulnerability more transparent.
- An analysis of how attack effectiveness varies with patch location and size would be informative for understanding physical-world threat realism.

---

## Novel Insights

The observation that adversarial patches optimized on VLA encoders consistently develop structural patterns reminiscent of robotic arms—and the hypothesis that this arises from overfitting of the visual encoder to limited-viewpoint robotic datasets—goes beyond the paper's stated contributions. If this hypothesis holds, it suggests that visual encoder diversity (e.g., multi-viewpoint pretraining, as in π₀) is a passive defense against representation-level attacks, and that the robustness gap between single-camera and multi-camera VLAs is not merely architectural but deeply tied to pretraining data diversity. This could motivate a new line of work on data-driven robustness for embodied vision systems.

---

## Suggestions

- Rename "model-agnostic" to "encoder-sufficient" or "encoder-access-only" throughout, and add a cross-model patch transfer experiment to test true transferability.
- Add a white-box EDPA variant (backbone gradients included) as an oracle to quantify the encoder-only relaxation's cost in attack strength.
- Extend defense evaluation to OpenVLA-OFT and π₀ to validate generalizability of the fine-tuning approach.
- Explicitly state the direction (increase or decrease) of vision-language alignment induced by the adversarial patch and report this as a diagnostic metric.

---

## Score and Decision

The paper addresses a timely and important problem (adversarial security for deployed embodied AI), provides a technically sound attack formulation, and evaluates it across multiple SOTA VLA models and task suites. The core relaxation of attack requirements over prior work is meaningful and well-motivated. The main drawbacks are: the "model-agnostic" claim is not fully substantiated without cross-model transfer experiments; the defense partially—not fully—mitigates attacks in harder settings and is only evaluated on one model; and the image-instruction alignment loss lacks a principled direction. These are correctable gaps rather than fatal flaws, and the contribution stands as a useful step for the community.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>