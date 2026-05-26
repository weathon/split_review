Now I have all the calibration data. Let me write the final consolidated review.

## Summary

This paper introduces Neon, a post-hoc method that improves generative image models by briefly fine-tuning them on their own synthetic samples (inducing predictable degradation), then reversing the resulting weight update via negative extrapolation θ_Neon = θ_r − w(θ_s − θ_r). The authors prove that mode-seeking inference samplers (low temperature, CFG, top-k/p) create anti-alignment between the synthetic-data gradient and the true-data gradient, so reversing the self-training direction corrects the model. Experiments span diffusion, flow matching, autoregressive (xAR, VAR), and few-step (IMM) models across CIFAR-10, FFHQ, and ImageNet, achieving an FID of 1.02 on ImageNet 256×256 with xAR-L — a new state-of-the-art — using only 0.36% additional training compute.

## Strengths

1. **State-of-the-art FID with minimal overhead**: On ImageNet-256, Neon improves xAR-L from FID 1.28 to 1.02 (surpassing UCGM's 1.06) using 0.36% additional training compute (Section 4.2, Figure 5). This is a strong, specific demonstration of the method's practical value.

2. **Universality across architectures**: Neon improves diffusion (EDM-VP), flow matching, autoregressive (xAR, VAR), and few-step (IMM) models — four fundamentally different families — with consistent FID reductions (Sections 4.1–4.3). This contrasts with prior methods (SIMS, DDO, Discriminator Guidance) that are architecture-specific.

3. **Rigorous theoretical justification**: Theorems 1 and 2 (Section 3.1) formally prove that mode-seeking samplers induce anti-alignment between synthetic and real-data gradients, guaranteeing that negative extrapolation reduces true-data risk under stated conditions. The honest discussion of the diversity-seeking sampler regime (where interpolation, not extrapolation, is optimal) adds credibility.

4. **Extreme data and compute efficiency**: Near-peak results are obtainable with as few as 1,000 synthetic samples (xAR-L FID 1.05 vs. 1.02), and the fine-tuning budget is consistently < 1% of original training (Figures 3, 5, 7). Cross-architecture transfer (Figure 8) further reduces the practical cost.

5. **No inference-time overhead**: Unlike Discriminator Guidance or SIMS, Neon is a one-time parameter merge that adds zero cost during sampling — a practically significant advantage.

6. **Mechanistic insight via precision-recall analysis**: Figure 4 explicitly confirms that Neon trades precision for recall, redistributing probability mass from over- to under-represented modes, directly verifying the theoretical mechanism. The joint optimization of w and CFG scale γ (Figure 6) is an important experimental contribution.

7. **Practical acceleration for few-step generators**: On IMM, Neon with 4-step inference nearly matches the 8-step base model quality (FID 1.69 vs. 1.98), effectively halving inference cost (Section 4.3, Figure 7).

8. **Robustness to synthetic data quality and base model quality**: Neon works across a wide range of CFG scales used for generating S (Figure 10) and across base models of varying quality (Figure 9), including a model trained on 40% less real data — confirming the theory's conditions are not fragile.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by evidence; the issues below are real but do not invalidate the central contribution.

### Minor

1. **Compute framing omits inference cost for synthetic dataset generation.** The paper repeatedly reports "0.36% additional training compute" (abstract, introduction, Figure 1) without including the cost of generating the synthetic dataset S. For xAR-L on ImageNet 256 with 750k samples, this generation is a non-trivial one-time cost. The paper partially mitigates this by noting that 1k samples achieve near-peak results (FID 1.05 vs. 1.02), but the abstract and introduction do not flag this caveat alongside the 0.36% figure. The framing is technically accurate (it is training compute), but the repeated emphasis on this percentage without disaggregating inference overhead creates a misleading impression of total resource burden. A more honest accounting would either include inference cost or add a sentence acknowledging it.

2. **Headline claims rest entirely on FID without human evaluation or complementary metrics.** The paper's SOTA claim (FID 1.02) and all quantitative results are FID-based. The precision-recall analysis (Figures 4, 6) is commendable and provides mechanistic insight, but it also reveals that Neon operates by trading precision for recall — raising the question of whether the FID improvement reflects genuine quality gains or a favorable shift along this trade-off that FID's particular functional form rewards. Without human preference judgments or alternative perceptual metrics (e.g., CLIP score, ImageReward, or a user study), the practical nature of the improvement is incompletely characterized. This is a standard concern in FID-only evaluations and does not undermine the paper's theoretical or empirical contributions, but it limits the strength of the headline quality claim.

3. **Anti-alignment (s = ⟨r_d, P r_s⟩) is never directly measured in a real model.** The core theoretical prediction is that s < 0 under mode-seeking samplers. This is validated in a 2D Gaussian toy example (Figure 2), but on real generative models the theory is only verified indirectly through downstream FID and precision-recall behavior. A direct measurement of the alignment angle between (θ_s − θ_r) and an oracle improvement direction (e.g., from a small held-out real sample) on a real model would transform the theory from a consistent story into a concretely verified mechanism. The absence of this experiment is the single most notable gap.

4. **Assumption A-MONO (curvature-density coupling) is not empirically checked.** Theorem 2's application to diffusion and flow models depends on this structural condition (Appendix B.7). While the downstream results confirm the method works, the paper would benefit from a brief discussion or small-scale verification of whether A-MONO actually holds for the tested models.

### Trivial
None.

## Nice-to-Haves
- **Direct comparison table with related methods on a common benchmark.** The paper defers SOTA comparisons to Appendix Table A.1. A main-text table comparing Neon with SIMS, DDO, and Discriminator Guidance on the same base model (e.g., EDM on CIFAR-10) with FID, computational overhead, and architectural constraints would immediately substantiate the paper's favorability claims.
- **Verification of A-MONO** on small-scale diffusion/flow models would strengthen Theorem 2's empirical grounding.

## Removed Points

These points were flagged in the reviewer inputs but are removed for the following reasons:

1. **"The statement 'the vector θ_s − θ_r corresponds to the synthetic gradient direction' is a minor imprecision"** — The paper's formal analysis in Section 3 correctly uses r_s for the gradient. The informal description in the introduction is accurate enough for a non-technical reader. This is a nitpick, not a substantive weakness.

2. **"A table comparing final FID, computational overhead, and architectural constraints for the same base model"** — The paper already provides this in Appendix Table A.1. The criticism ignores the appendix.

3. **"Missing related works"** — Per the review instructions, we do not flag missing references as we cannot independently verify their existence or relevance.

4. **Generic formatting/style nitpicks** — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface observations about the paper that the authors themselves do not already articulate. The insight that synthetic degradation is a structured signal rather than random noise, and that reversing it corrects sampler bias, is well-developed in the paper itself.

## Suggestions

1. **Add a direct measurement of anti-alignment.** Measure the cosine similarity between (θ_s − θ_r) and an oracle gradient estimated from a small held-out real dataset (or a real-data fine-tuned checkpoint) for at least one model (e.g., EDM-VP on CIFAR-10). Report the angle across different w values and verify that it is negative when the base model is good.

2. **Acknowledge inference cost explicitly in the main compute figure.** Either add a column in Figure 5's caption noting the cost of generating S (for the 750k case) and the far lower cost with 1k samples, or add a sentence in the abstract/introduction that "the total cost includes one-time inference to generate S; near-peak results require as few as 1k samples."

3. **Include at least one complementary perceptual metric or small human evaluation.** A CLIP-FID score, ImageReward evaluation, or 50-sample human preference comparison between base and Neon outputs on ImageNet would substantially de-risk the concern that the FID improvement is an artifact of the precision-recall trade-off.

4. **Briefly discuss A-MONO.** Add 2–3 sentences in Section 3.1 (or the appendix) discussing whether this curvature-density coupling condition is likely to hold for the specific model families tested, or cite empirical evidence.

## Score and Decision

**Calibration anchor comparison.** All anchors retrieved across rounds (not all read in full):

| Path | Avg Score | Source | Comparison to Neon |
|------|-----------|--------|-------------------|
| 8TbqoP3Rjg (Knowledge Distillation for Model Collapse) | 2.00 | r1-topic-low | Much weaker — no novelty, poor presentation, trivial experiments |
| QKqWnNkwPL (Self-distillation for diffusion) | 3.00 | r1-topic-low | Much weaker — narrow scope, limited contributions |
| 2LhCPowI6i (Self-Supervised Pseudodata Filtering) | 2.33 | r1-topic-low | Much weaker — different problem, limited results |
| 7DY2Nk9snh (SynthCLIP) | 4.75 | r1-topic-mid | Weaker — less novelty, weaker motivation, evaluation gaps |
| CjPt1AC6w0 (Synthetic Data Transfer Learning) | 6.25 | r1-topic-mid | Comparable breadth but weaker novelty and no theory |
| 9aIlDR7hjq (Augmented Conditioning) | 4.00 | r1-topic-mid | Weaker — narrower scope, less rigorous |
| et5l9qPUhm (Strong Model Collapse) | 8.00 | r1-topic-high; r1-weakness-6 | Stronger in theoretical depth, but rejected; different contribution type |
| 07yvxWDSla (Synthetic continued pretraining) | 8.00 | r1-topic-high | Stronger — highly polished, accepted; different domain (NLP) |
| 3b9SKkRAKw (LeFusion) | 8.00 | r1-topic-high | Stronger — medical domain, accepted; not comparable topic |
| 6p74UyAdLa (Dynamic Negative Guidance) | 6.25 | r2-narrow | Weaker — limited evaluation (MNIST/CIFAR-10 only), no theory |
| ShjMHfmPs0 (Self-Consuming Models Go MAD) | 6.67 | r2-narrow | Weaker — analysis paper without a method, simpler theory, limited datasets |
| KZgo2YQbhc (PaRa) | 7.50 | r2-narrow | Comparable — similar novelty and thoroughness; PaRa focused on personalization, Neon on broader improvement |
| HMVDiaWMwM (Guided Score Identity Distillation) | 6.50 | r2-narrow | Weaker — narrower contribution |
| 1Z6PSw7OL8 (BiGR) | 6.50 | r2-narrow | Different contribution type |
| P5UETqZXqT (Chain of Diffusion) | 5.75 | r1-weakness-model-collapse | Weaker — less novel, narrower experiments, methodological concerns |
| Xr5iINA3zU (Collapse or Thrive?) | 5.75 | r1-weakness-model-collapse | Weaker — analysis paper, no method |
| Im2neAMlre (One slice is not enough) | 7.33 | r3-optional | Evaluation-focused paper; not comparable |

**Round-1 bracket**: I initially placed this paper between 6.0 and 8.0 based on its novelty, theoretical depth, and experimental breadth relative to the weak/mid bands. The low-band topic anchors (2.00–3.00) failed in novelty, experimental rigor, and clarity — none of which are shared by the Neon paper. The weakness-anchored model-collapse papers (5.75) had issues with insufficient causal analysis and limited experimental scope — Neon is stronger on both.

**Round-2 narrowing**: Within the 6.0–8.0 bracket, Neon sits above Dynamic Negative Guidance (6.25) and Self-Consuming Models (6.67) due to its stronger theory, broader experiments, and practical SOTA result. It is roughly comparable to PaRa (7.50): both have novel ideas and thorough evaluations, though Neon's weaknesses (compute framing, FID-only, anti-alignment measurement gap) are slightly more substantive than PaRa's (missing SOTA comparisons). The paper does not reach the 8.0 level of Strong Model Collapse, which had deeper theoretical results.

**Final score**: **7.0** — a strong paper with clear novelty, solid theory, and extensive experiments across multiple architectures. The weaknesses are real but not fatal.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>