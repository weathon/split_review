Now I have a clear picture. Let me synthesize my analysis and write the final review.

---

## Summary

ARSS presents the first framework to cast single-image novel view synthesis as a next-token prediction task using a GPT-style decoder-only autoregressive transformer, conditioned on a camera trajectory. It combines three components: a causal video tokenizer for temporal consistency, a camera autoencoder that compresses Plücker raymaps into 3D positional guidance tokens, and a hybrid token ordering that permutes spatial tokens while preserving temporal order. The method achieves competitive results with state-of-the-art diffusion-based approaches on RealEstate10K and ACID, and generalizes zero-shot to DL3DV.

## Strengths

- **Genuine architectural novelty.** ARSS is the first framework to apply decoder-only causal autoregressive transformers to novel view synthesis with camera control. This is a non-trivial integration requiring solutions to three distinct problems (temporal tokenization, camera encoding, and spatial permutation), each of which is validated through ablation. The paper opens a new direction for NVS that is distinct from the dominant diffusion paradigm.

- **Competitive quantitative results.** Table 1 shows ARSS achieves the best PSNR (19.02 on RealEstate10K, 21.93 on ACID) and lowest LPIPS (0.269, 0.265) among compared methods. On zero-shot DL3DV it leads in LPIPS (0.347) while remaining competitive in other metrics. These are solid results for a model trained from scratch without pretrained diffusion weights.

- **Strong ablations support key design choices.** The token permutation ablation (Table 2, Figure 7) convincingly shows that preserving temporal order while shuffling spatial tokens is critical — "full perm." and "raster" both degrade significantly. The tokenization ablation (Table 3) demonstrates a 62% FVD reduction (137.68 → 52.56) from using a video tokenizer over per-frame VQ, confirming the need for temporal coherence in the latent space.

- **Meaningful error accumulation analysis.** Figure 6 shows that ARSS maintains higher per-frame PSNR/SSIM and lower LPIPS across the trajectory, with visibly flatter degradation slopes than all baselines. This is a substantive finding that distinguishes the method beyond aggregate metrics.

- **Zero-shot generalization.** The method, trained only on RealEstate10K and ACID, produces sharp, geometrically consistent views on DL3DV (Table 1, Figure 4) and on AI-generated stylized images (Figure 5), indicating meaningful generalization beyond training distributions.

## Weaknesses

### Major

- **The central motivation for the AR design is not experimentally validated.** The introduction motivates the autoregressive approach by arguing it is "desirable to process observations in a sequential and causal manner" for "scaling to large environments and long trajectories" with "incremental reuse of previously generated views." Yet all experiments use fixed 17-frame sequences matching the training horizon. There is no demonstration of: (a) generating beyond the training length, (b) conditioning on the model's own prior outputs for further generation, or (c) incremental view synthesis where new frames are added to an existing sequence. The error accumulation analysis (Figure 6) shows slower per-frame degradation, but this is on the same fixed-length sequences — it does not isolate the benefit of the causal structure versus a joint model's overall fidelity. This gap between motivation and evidence weakens the paper's core thesis.

- **Baseline fairness is inadequately addressed.** RayZer (PSNR 12.97) and ViewCrafter (PSNR 12.67) produce implausibly poor results on RealEstate10K — far worse than would be expected from methods designed for related tasks. The paper provides no details on how these models were adapted to single-image NVS, whether they were fine-tuned on the same data, or whether off-the-shelf checkpoints were used. Without this information, the reported gaps may overstate ARSS's advantage. Even against the better-performing SEVA, the picture is mixed: SEVA achieves higher SSIM (0.670 vs. 0.624) and substantially better FID (46.98 vs. 47.60) on RealEstate10K, with similar pattern on ACID. The introduction's claim of "out-performs current state-of-the-art methods" is not fully supported by the evidence (the abstract's "comparable" is more accurate).

### Minor

- **No ablation on the camera autoencoder against simpler alternatives.** The camera autoencoder is a non-trivial component (3D convolutions, geometry-aware loss), but the paper does not compare it against simpler encoding strategies such as directly embedding Plücker coordinates with an MLP or concatenating them as extra channels. The contribution of this module relative to its complexity is unclear.

- **Inference cost and speed are not discussed.** AR next-token prediction can be slow for long sequences, and while the paper mentions parallel decoding is possible (Section 3.2.3), no quantitative speed or memory comparison against diffusion baselines is provided. This matters for the practical utility of the method.

- **The overclaim in the introduction** ("out-performs current state-of-the-art methods") contradicts the more measured abstract ("comparable") and the actual results, where SEVA wins on SSIM and FID. This should be corrected.

### Trivial

- The camera autoencoder architecture is described only as "stacked 3D convolutional and downsampling blocks" without precise specification of layer counts or dimensions.
- The description of how camera latent tokens are integrated into the transformer could be more precise (are they used as additional regular tokens, or as position embeddings?).

## Nice-to-Haves

- **Length-extrapolation experiments.** Testing the model on trajectories longer than 17 frames, or feeding its own generation back as conditioning for further synthesis, would directly test the claimed AR advantage.
- **Causal vs. non-causal ablation.** A bidirectional transformer baseline using the same tokenizer and camera embeddings but attending non-causally would isolate the effect of the causal mask.
- **Multi-view consistency metrics** beyond per-frame scores (e.g., reprojection error, depth consistency) would strengthen claims of geometric consistency.
- **Statistical significance measures** or confidence intervals for the main quantitative results.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh critic: "a diffusion model or a feed-forward transformer could also exhibit a relatively flat degradation curve on a fixed-length output"** — This is speculation. The paper empirically shows ARSS has flatter degradation; the critic's counterfactual is not demonstrated by any baseline in the paper. Demoted.

- **Harsh critic: "missing appendix" or "proofs in appendix"** — The parser strips appendices; the original submission includes them. Removed per hard rules.

- **Harsh critic: "no discussion of diversity or sampling strategies"** — NVS is typically evaluated deterministically; this is not standard to demand. Removed as scope creep.

- **Harsh critic: "the parallel decoding claim is stated but never quantified"** — Parallel decoding is mentioned as a capability but is not presented as a core claim; demanding quantification is excessive for a first demonstration paper. Moved to nice-to-have via inference cost discussion.

- **Strength Finder: "The camera autoencoder provides a principled 3D positional signal"** — This is a design description, not an empirically validated strength. The geometry-aware loss is well-motivated, but without an ablation there is no evidence it is better than alternatives. Kept only as design rationale, not as a standalone strength.

## Novel Insights

The synthesis of the reviews reveals a structural tension in this paper that is not obvious from a surface reading: the AR framework is motivated by properties (causal scaling, incremental reuse, trajectory extension) that the diffusion baselines are also not evaluated on — meaning the claimed advantage of AR over diffusion for world modeling is asserted rather than demonstrated. At the same time, the paper does convincingly show that an AR model *can work* for NVS at all, which is a genuinely non-obvious result given the challenges of adapting next-token prediction to multi-view 3D-consistent generation. The real contribution is establishing feasibility, not demonstrating superiority of the AR paradigm for the motivating use case. Reframing the paper around feasibility rather than motivation-driven advantage would align the claims with the evidence.

## Suggestions

- Reframe the introduction to emphasize that ARSS demonstrates *feasibility* of autoregressive view synthesis with competitive quality, rather than claiming AR's superiority for long trajectories. Save the scaling claims for when they are tested.
- Add a brief description of how RayZer, ViewCrafter, and MotionCtrl were adapted (or acknowledge their limitations as baselines not designed for this task).
- Add an ablation replacing the camera autoencoder with a simple MLP embedding of Plücker rays to clarify whether the autoencoder complexity is warranted.
- Correct the intro's "out-performs" to "is competitive with" or "achieves comparable results to" to match the abstract and the data.

## Score and Decision

### Anchor comparison:

| Anchor | Avg Score | Round | Comparison to ARSS |
|--------|-----------|-------|-------------------|
| LVSM (QQBPWtvtcn) | 7.67 | R1 | Clearly stronger: more thorough experiments, two architectures, fair baselines, stronger results. ARSS is weaker on evaluation rigor. |
| GST (NuHYh4YKNe) | 6.25 | R1+R2 | Similar novelty level (AR for spatial tasks). GST has its own evaluation/motivation gaps but demonstrates joint-task benefits. ARSS is comparable in contribution scale but has the motivation-experiment gap. |
| VD3D (0n4bS0R5MM) | 6.20 | R2 | Similar contribution type (first to apply technique X to architecture Y). VD3D has more thorough ablation. ARSS has stronger novelty but weaker alignment of motivation and evidence. |
| 4DiM (d2UrCGtntF) | 6.50 | R1 | Stronger paper: more comprehensive evaluation, novel calibration pipeline. ARSS is below this level. |
| Zero-shot NVS via Video Diffusion (zDJf7fvdid) | 6.00 | R1 | Similar evaluation scope. ARSS has comparable contribution level with different strengths/weaknesses. |
| "3D-free meets 3D priors" (VLuJL8cnGk) | 5.00 | R1+R2 | ARSS is clearly stronger: genuine architectural novelty, end-to-end training, competitive results vs. test-time optimization with limited novelty. |

**Bracket from Round 1:** 5.0–7.5.  
**Narrowed by Round 2:** The paper sits between the 5.0 and 6.5 anchors. It is clearly stronger than the 5.0 anchor and comparable to but slightly weaker than the 6.0–6.25 anchors due to the motivation-experiment gap and baseline fairness concerns.

**Final score: 6.0.** The paper makes a genuine contribution as the first AR framework for NVS with competitive results and solid ablations. The motivation-experiment gap is a real weakness but does not invalidate the contribution of demonstrating that AR models can work for this task. The baseline fairness issues and overclaim are addressable presentation problems. The paper would benefit from revision but makes a sufficient contribution to warrant acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>