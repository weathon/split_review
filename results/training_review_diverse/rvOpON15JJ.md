Now I have a thorough understanding of both the paper and the reviews. Let me write the final consolidated review.

## Summary

This paper proposes Diffusion Implicit Policy (DIP), a framework for scene-aware motion synthesis that disentangles human-scene interaction learning from motion synthesis during training. A motion diffusion model is trained on unpaired motion data only, and at inference time, interaction-based reward functions act as an implicit policy to guide the denoising process in a GAN-inversion manner. The method is evaluated on locomotion, object interaction, and long-term motion tasks across ShapeNet, PROX, and Replica scenes, with user study results showing competitive or superior performance to prior methods (DIMOS, SAMP, GAMMA) that require paired motion-scene data.

## Strengths

1. **Novel disentanglement of interaction from motion synthesis, removing the need for paired training data**: The core idea — train a motion diffusion model on unpaired motion data and enforce interaction plausibility only at inference via reward-guided diffusion — is a genuine departure from prior methods (DIMOS, SAMP, GAMMA) that all require paired motion-scene data for training. The paper states clearly: "paired motion-scene data are no longer necessary for training" (Sec. 1), and the results on real PROX/Replica scenes (Figs. 7-8) demonstrate generalization without scene-conditioned training.

2. **User study with strong perceptual evidence**: The user study (1,200 ratings from 15 participants, Table 3) is the most direct evidence for the method's effectiveness. DIP achieves the highest interaction plausibility (4.16/5 vs. 3.97 for DIMOS), diversity (3.91/5 vs. 3.64), and overall score (4.12/5 vs. 3.95), while matching DIMOS on motion naturalness — all without any paired motion-scene training data.

3. **Quantitative advantages on locomotion and interaction metrics**: On locomotion (Table 1), DIP achieves the shortest finish time (3.35s), smallest distance to goal (0.03m vs. 0.12m for DIMOS), and lowest scene penetration (0.95% vs. 4.64%). On interaction (Table 2), DIP reduces mean penetration and maximum penetration for both sitting and lying tasks while maintaining competitive contact and time scores.

4. **Technically sound GAN-inversion style optimization**: The optimization of the denoising distribution mean via `\hat{x}_0^\varphi(\mu_t, t-1, c)` rather than directly modifying `\mu_t` (Eq. 10) is well-motivated: it preserves motion continuity by operating through the full diffusion model prediction. The analogy to GAN inversion is clearly explained and distinguishes the approach from naive classifier guidance.

5. **Strong generalization across scene types without retraining**: The same trained motion diffusion model produces credible results on synthesized ShapeNet scenes, real scanned PROX scenes, and Replica scenes (Sec. 4), validating that disentangled training indeed enables generalization to unseen environments.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No variance or confidence intervals reported for main quantitative results (Tables 1, 2)**: The paper reports only mean values for locomotion and interaction metrics without standard deviations, confidence intervals, or number of trials. While this is common practice in parts of this community, it weakens the ability to assess whether reported improvements (e.g., 0.03m vs. 0.12m distance to goal) are statistically meaningful given the procedural generation of test scenes. An explicit statement of variance or number of test runs would strengthen the claims.

2. **Ablation studies not present in the main paper**: The paper defers all ablations to the supplementary material (line 272). At minimum, an ablation isolating the effect of the implicit policy (DIP vs. DIP without reward-based mean adjustment, using only the motion prior with ControlNet) should appear in the main text to directly demonstrate the benefit of the proposed optimization. The contribution depends on this comparison being transparent.

3. **COINS dependence qualifies the "unpaired" claim**: The paper frames itself as requiring "no paired motion-scene data," and the title uses "Unpaired Scene-aware Motion Synthesis." However, the pipeline uses COINS (line 99, line 248), a method trained on paired human-scene interaction data, to sample static interaction goals for long-term tasks. The core motion model training is indeed unpaired, and the paper acknowledges COINS usage, but the framing should be qualified — ideally clarifying that the motion synthesis component is unpaired while the full pipeline uses a pre-trained paired module for goal specification. This does not invalidate the contribution but would improve precision.

4. **Contact metric mismatch acknowledged but not fully resolved**: On locomotion (Table 1), DIP achieves worse contact scores than DIMOS. The paper attributes this to the metric using foot joints while the method focuses on foot vertex contact (line 232). This is a reasonable explanation, but the authors should verify or argue that the metric discrepancy does not affect the relative ranking — or adopt a metric that reflects what the method optimizes.

5. **Interaction evaluation shows an uncommented trade-off in max penetration**: For sitting (Table 2), DIP achieves lower mean penetration (0.10 vs. 0.24 for DIMOS) but higher maximum penetration (0.24 vs. 0.16). The paper does not comment on this trade-off. A brief explanation (e.g., whether this reflects a specific failure mode or is within tolerance) would improve transparency.

6. **Motion blending and inpainting components not individually evaluated**: The inpainting mechanism (Sec. 3.3) and the power-space motion blending (Sec. 3.5) are described but not ablated or compared against simpler alternatives (e.g., linear interpolation in axis-angle). While the overall results are positive, the individual contribution of these components is unclear.

### Trivial

- The paper reports "0.95" for penetration in locomotion without a percentage sign in the text, while the metric description says "percentage of body vertices" — consistent formatting would help readability.

## Nice-to-Haves

- A controlled comparison against a version of DIP using standard diffusion sampling (same ControlNet, same noise schedule) without the implicit policy optimization would directly demonstrate the value of the central proposed mechanism.
- Discussion of failure cases or limitations (e.g., when the reward optimization diverges, or scenes where the method struggles) would improve credibility.
- A brief note on sensitivity to the λ weight hyperparameters would help readers understand tuning requirements.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Over-reliance on supplementary material for critical details" (from Harsh Critic #3)**: The paper explicitly states where details are deferred ("Please kindly refer to the Supplementary Material," line 134). The reward function types (six terms) and the optimization approach (Eq. 10) are presented in the main paper. Exact formulations and λ weights are tuning details commonly placed in supplementary. This is not a structural weakness — the main paper provides sufficient information to understand the method's logic and evaluate its soundness.
- **"Ambiguous baseline configurations" (from Harsh Critic #2)**: The paper states that all methods use the same initial state and task goals (line 248) and uses scenes from DIMOS. The baselines are published, cited methods. Not re-stating their training details is standard practice. The reviewer's demand for per-baseline hyperparameter disclosure exceeds what is typical for this type of comparison.
- **"Justification for GAN Inversion analogy is weak" (from Harsh Critic Section-by-Section)**: The paper provides a clear analogy (line 169) with a concrete description of why optimizing through the diffusion prediction outperforms direct μ_t modification. This is adequately justified.
- **Strength Finder's claimed strengths that are generic**: Some strengths were phrased generically (e.g., "quantitative superiority") but these are backed by specific numbers in the paper, so they are kept. The "methodological gap" claims that inflate minor issues have been downgraded per instructions.

## Novel Insights

The reviews collectively surface a tension that the paper does not fully address: the "unpaired" framing is powerful and the core motion model genuinely requires no paired data, yet the full pipeline depends on COINS (a paired-data module) for goal specification. This does not invalidate the contribution, but future work should examine whether the goal-specification step can also be learned from unpaired data or heuristics, making the entire pipeline fully unpaired. Additionally, the contact metric mismatch (foot-vertex vs. foot-joint) highlights a broader evaluation challenge in the field: as methods optimize different aspects of contact, standardized evaluation protocols become increasingly important.

## Suggestions

1. Add variance measures (standard deviation or confidence intervals) to Tables 1 and 2.
2. Include one key ablation in the main paper — specifically, compare DIP with and without the implicit policy optimization (same ControlNet, same noise schedule) to directly demonstrate the benefit of the proposed mechanism.
3. Qualify the "unpaired" framing to clarify that the motion model training is unpaired while the full pipeline uses a pre-trained goal-specification module (COINS) that requires paired data.
4. Comment on the mean vs. max penetration trade-off for sitting in Table 2.
5. Either adopt a contact metric aligned with the method's optimization targets or provide analysis showing the metric mismatch does not affect relative rankings.

## Score and Decision

The paper presents a genuinely novel framework with a well-motivated technical approach. The core contribution — decoupling motion prior learning from scene interaction and combining them via guided diffusion at inference — is significant and addresses a real limitation in the field. The evaluation, while not exhaustive (no variance, ablations in supplementary), includes a substantial user study (1,200 ratings) and multiple quantitative metrics across diverse scenes that collectively support the main claims. The weaknesses are all minor (presentation, scope of what appears in the main text, precise framing) and addressable in a revision. No weakness threatens the core claim that unpaired training with inference-time reward optimization can produce competitive scene-aware motion synthesis.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>