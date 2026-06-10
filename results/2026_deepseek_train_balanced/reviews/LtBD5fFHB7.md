## Summary

This paper proposes Motion Inversion, a method for motion customization in video generation that learns explicit "Motion Embeddings" from a reference video and injects them into the temporal transformer modules of a T2V diffusion model. The method introduces two complementary embeddings: a 1D Motion Query-Key Embedding (spatially invariant, targeting attention maps for global motion) and a 2D Motion Value Embedding (spatially detailed, with an inference-time frame-differencing operation to remove static appearance). Experiments on 66 video-text pairs with three baselines (DMT, VMC, Motion Director) show the method achieving best scores on 4/5 metrics, with the strongest evidence from a 121-participant user study (39.35% vs. 27.27% preference).

## Strengths

1. **Principled two-part motion embedding design** — The paper explicitly separates motion representation into complementary QK (1D, attention-map-oriented) and V (2D, value-oriented) embeddings with a clear rationale: the temporal attention map already carries spatial appearance information, so adding spatial dimensions to the QK embedding would entangle appearance (§3.3). This is a more structured and interpretable approach than LoRA-based methods like Motion Director.

2. **Differencing operation for appearance debiasing** — The frame-differencing operation on the Value Embedding at inference time (Eq. 133) is a clean, interpretable mechanism for removing static appearance components, conceptually linked to optical flow (§3.3). The ablation study confirms this design choice is beneficial.

3. **Strong user study results** — With 121 participants across 10 scenarios, the method achieves a 39.35% preference rate versus 27.27% for the next-best method (Motion Director). This 12-percentage-point gap is the most compelling evidence of practical advantage.

4. **Compatibility with multiple T2V backbones** — Results are demonstrated with both ZeroScope and AnimateDiff (§4, Figure 1), indicating the motion embeddings are not architecture-specific.

## Weaknesses

### Fatal
None.

### Major

1. **Ablation study is entirely qualitative** — The paper makes specific, separable design claims (1D vs 2D QK embeddings, differencing vs normalize vs vanilla) but validates them only through visual results (Figure 6 caption: "Visual Result of the Ablation Study"). No quantitative metrics (Text Similarity, Motion Fidelity, Temporal Consistency) are reported for configurations (a)–(f). Given that the main quantitative margins over baselines are modest, the absence of quantitative ablation is a significant evidentiary gap — the reader cannot assess whether the claimed design choices are responsible for the observed performance or whether alternative configurations would be competitive.

2. **No measures of variability for main quantitative results** — Table 1 reports point estimates without standard deviations, confidence intervals, or number of seeds. The margins over Motion Director are small (Text Similarity: 0.3113 vs 0.3042, ~2.3%; Motion Fidelity: 0.9552 vs 0.9391, ~1.7%), and without variance estimates it is unclear whether these differences are statistically meaningful or within the noise inherent to diffusion model inference.

3. **FID scores are likely uninformative due to content mismatch** — The reported FID values (550–696) are extremely high. The reference set consists of frames from 89 DAVIS videos (depicting one set of objects/scenes), while the generated frames depict different objects/scenes per text prompt. FID is sensitive to distributional differences in content, not just quality. Values above 500 suggest the metric is primarily measuring content mismatch rather than generation quality, making the FID column in Table 1 of unclear interpretability.

### Minor

1. **The "debiasing" claim for the 1D QK embedding is overstated** — The paper argues that excluding spatial dimensions from M^QK "debias[es] appearance" because the attention map "inherently carries spatial details of objects" (lines 34, 155–158). However, the feature tensor F already encodes all appearance information before any embedding is added. The 1D design primarily limits the embedding's capacity to learn spatially structured patterns rather than genuinely removing appearance from the attention computation. The attention map still reflects object shape because F encodes it.

2. **Training-inference discrepancy for the differencing operation is not experimentally validated** — The Value Embedding is optimized during training without differencing (Eq. 114: m_i^V added directly to F before V projection) but applied with differencing at inference (Eq. 133). The rationale (debiasing static appearance, analogous to optical flow) is stated, but the paper provides no analysis — no reconstruction experiment, no noise prediction error comparison — to verify that the learned denoising trajectories transfer to the differenced embedding. While the qualitative ablation suggests the operation works, the mechanism is unexamined.

3. **Thin margins on automated metrics** — Beyond the lack of variance, the absolute improvements over Motion Director are small (0.007 on Text Similarity, 0.016 on Motion Fidelity), and the method trails VMC on Temporal Consistency (0.9354 vs 0.9448). The user study is the strongest evidence, but the automated metrics tell a less clear story.

## Nice-to-Haves
- A reconstruction experiment (source video → source video with original prompt) to establish an upper bound on motion fidelity.
- Ablation with differencing incorporated during training (vs. inference-only) to directly test the mismatch concern.
- Reporting of computational cost (training time, inference overhead, parameter count) given that the paper criticizes DMT for "additional computation costs."
- Quantitative ablation results in a table.

## Removed Points
- "Discussion with video editing method deferred to supplementary" — Removed per instruction: appendix/supplementary content stripped by parser artifact; not a genuine weakness.
- "The paper never explains why the differencing substitution is valid" — The paper does explain the rationale (lines 130–131, 165). The valid residual concern (lack of experimental validation) is retained in Minor #2.
- "No reconstruction experiment" / "No analysis of embedding interpretability" / "Computational cost not reported" — These are nice-to-haves rather than core weaknesses; moved to Nice-to-Haves.
- Strength Finder: "Systematic ablation covering both embedding design and inference strategy, providing direct ablation evidence" — Overstated; the ablation is qualitative only. Removed from Strengths.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add a quantitative ablation table (Text Similarity, Motion Fidelity, Temporal Consistency) for each embedding configuration (a–d) and inference strategy (e–f). Without this, the paper's central design claims are unsupported by quantitative evidence.
2. Report mean and standard deviation across multiple seeds for all metrics in Table 1.
3. Either justify the FID evaluation (e.g., by using a content-matched reference set, or by measuring FID between generated outputs and source video reconstructions) or replace it with a more appropriate quality metric.
4. Add a reconstruction experiment to verify that the learned embeddings faithfully capture the intended motion.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>