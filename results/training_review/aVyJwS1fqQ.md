Now I have a thorough understanding of the paper and all claims. Let me synthesize the final review.

---

## Summary

The paper presents Mani-WM, a diffusion transformer-based world model that generates high-resolution, long-horizon videos of a robot arm executing a given action trajectory from an initial frame (trajectory-to-video task). The key technical innovations are a frame-level conditioning mechanism (Frame-Ada) that aligns each action in the trajectory with its corresponding generated frame, and a spatial-temporal attention design for computational efficiency. The method is evaluated on four real-robot datasets (RT-1, Bridge, Language-Table, RoboNet) and validated on a real robot for model-based planning across three manipulation tasks.

## Strengths

- **Frame-level conditioning is a well-motivated and effective design.** The paper identifies a genuine gap between text-to-video conditioning (one embedding for the whole video) and the trajectory-to-video task (each action must be precisely aligned to its frame). The proposed Frame-Ada encodes each action individually into per-frame scale/shift parameters in the spatial attention blocks. The ablation (Table 1) confirms that Frame-Ada consistently outperforms the video-level variant across all datasets, and human evaluation (Fig. 4) validates that these gains translate to human-preferred outputs.

- **Comprehensive empirical evaluation with consistent results.** Mani-WM is evaluated on four diverse real-robot datasets with different action spaces (2-DoF to 7-DoF), different resolutions, and different trajectory lengths. On short trajectories (Table 1), long trajectories (Table 2), and the RoboNet benchmark (Table 3), Mani-WM-Frame-Ada achieves the best or near-best scores on the primary metrics. The human preference study (Fig. 4) further confirms that Mani-WM-Frame-Ada is preferred over all baselines across all three datasets.

- **Demonstrated flexibility beyond training distributions.** The paper shows Mani-WM can generate realistic videos from trajectories produced by diverse out-of-distribution sources — keyboard arrows, VR controller inputs, and a learned policy (Fig. 6). The qualitative results are compelling and suggest robustness to distribution shift, which is important for practical interactive use.

- **Real-robot validation of model-based planning.** Mani-WM is deployed on a real robot to predict visual outcomes of candidate trajectories for goal-conditioned planning (Table 4, Fig. 7). This goes beyond pure video generation metrics and shows that the model's predictions are useful for downstream control, with both MSE and ResNet-based cost functions outperforming random trajectory selection.

## Weaknesses

### Fatal

None.

### Major

- **The claim of "superiority of transformer-based model" is not adequately isolated from the conditioning scheme.** The paper compares Mani-WM (Transformer + frame-level conditioning) against VDM and LVDM (U-Net + video-level conditioning). The ablation in Table 1 shows that within Mani-WM itself, frame-level conditioning outperforms video-level conditioning. Since both the backbone architecture (Transformer vs. U-Net) *and* the conditioning granularity (frame-level vs. video-level) differ between Mani-WM and the baselines, the observed advantage cannot be attributed to the Transformer backbone alone. The paper states "This demonstrates the superiority of transformer-based model" (Sec. 4.2), which overclaims. A proper isolation would require either: (a) a U-Net baseline with frame-level conditioning, or (b) comparing Mani-WM-Video-Ada (same DiT backbone, video-level conditioning) against VDM/LVDM to see if the Transformer alone provides gains. The paper does not report whether Mani-WM-Video-Ada outperforms VDM/LVDM, leaving the reader unable to disentangle the contributions. This does **not** invalidate the paper's core claim that *Mani-WM as a full system* outperforms baselines, but it does mean the architectural attribution is unsupported.

- **Missing ablation on the action injection method.** The paper only ablates video-level vs. frame-level conditioning. It does not compare against alternative ways to inject frame-level action information — e.g., cross-attending over action embeddings, concatenating action tokens to frame tokens, or adding action embeddings directly to patch tokens. Without these ablations, it is unclear whether the advantage of Frame-Ada comes from the per-frame conditioning concept or the specific adaptive normalization implementation.

### Minor

- **Model-based planning comparison uses an extremely weak baseline.** The real-robot planning experiment (Table 4) compares Mani-WM-based trajectory selection only against a random policy. While this demonstrates that Mani-WM's predictions carry useful information, it does not establish that Mani-WM is competitive with or better than alternative world models or simpler forward predictors for planning. The paper's claim that this shows Mani-WM "can be used for model-based planning" is fair, but the claim that it "significantly improves success rates" (contribution 3) is relative only to random, which sets a low bar.

- **Flexible controllability is only qualitatively demonstrated.** The keyboard/VR/policy experiments (Fig. 6) are visually compelling but lack any quantitative evaluation. There is no metric comparing the generated videos to real-robot rollouts under the same trajectories. Given that the paper's headline contribution is accurate trajectory-to-video generation, this omission weakens the claim of robustness to out-of-distribution inputs.

- **No analysis of error accumulation over autoregressive rollout length.** For long-trajectory generation (Table 2, Fig. 3b), the paper reports aggregate metrics but does not plot PSNR, FVD, or other metrics against the number of autoregressive steps. This would help readers understand how quickly quality degrades as rollouts extend and where the method's limitations lie.

- **The distinction from prior world models (DreamerV3, iVideoGPT, VLP) is discussed only at the level of resolution and frame count.** The related work section (Sec. 2) describes how Mani-WM differs from these methods ("high-resolution... long-horizon videos") but does not provide methodological comparisons or experiments against them on the main datasets (they are only compared on RoboNet). This limits the paper's positioning within the world model literature.

### Trivial

None.

## Nice-to-Haves

- A comparison of Mani-WM against a frame-level-conditioned U-Net baseline, to properly isolate the backbone's contribution.
- A quantitative evaluation of the flexible controllability experiments (e.g., FVD between generated and real rollouts for keyboard/VR trajectories).
- Ablation experiments comparing Frame-Ada against alternative frame-level conditioning methods (cross-attention, token concatenation, etc.).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Primary metrics (Latent L2, PSNR) are poorly justified"** — The paper explicitly justifies this choice (Sec. 4.1: "the variety is much smaller in the trajectory-to-video task... we prioritize the Latent L2 loss and PSNR") and validates it with human preference correlation (Fig. 4). The reviewer's assertion that "FVD should be the primary metric" is an opinion, not a factual error. The paper reports FVD as a secondary metric. This criticism is already addressed in the paper.

- **"The paper does not demonstrate that Mani-WM serves as a replacement for real-robot rollout (policy evaluation, data augmentation, RL)"** — This is explicitly scoped as future work in Sec. 5. Criticizing a paper for not doing things it explicitly leaves to future work is scope creep. The paper's contribution is the trajectory-to-video model itself, which is a prerequisite for those applications.

- **"SDXL VAE may introduce domain gap"** — This is speculative and not substantiated with any evidence of degradation. The empirical results (good PSNR, human preference) suggest the VAE is adequate.

- **"Scaling plot shows expected results, not a contribution"** — The scaling analysis (Fig. 5) is standard practice and valuable for demonstrating the approach's potential. Dismissing it as "expected" ignores that not all methods scale cleanly.

- **Missing related works / "not comparing against existing world models"** — The paper does compare against iVideoGPT and MaskViT on RoboNet (Table 3). The criticism ignores this comparison.

- **Formatting/style nitpicks and missing appendix details** — These are parser artifacts or outside-scope concerns.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the paper that the paper itself does not already articulate.

## Suggestions

1. **Add a baseline that isolates the backbone contribution.** The most impactful fix would be to implement frame-level conditioning in VDM or LVDM (or find an existing frame-conditioned video prediction baseline) and compare against it. If Mani-WM-Video-Ada already outperforms VDM/LVDM in the unreported portion of Table 1, that data should be explicitly stated and discussed. Either way, the "superiority of transformer-based model" claim should be calibrated to what the evidence supports.

2. **Add a non-random baseline to the planning experiment.** Even a simple forward predictor (e.g., next-frame prediction with a convolutional model) or an oracle baseline would substantially strengthen the claim that Mani-WM is useful for planning.

3. **Quantify the flexible controllability experiments.** Compute a metric (e.g., FVD or Latent L2) between generated videos and real-robot rollouts for the keyboard/VR/policy trajectories to substantiate the qualitative results.

4. **Add error accumulation plots** showing how PSNR/FVD evolve over autoregressive rollout steps.

5. **Ablate action injection methods** beyond the video-level vs. frame-level comparison to justify the specific Frame-Ada design.

## Score and Decision

**Originality:** 6/10 — Frame-level conditioning for trajectory-to-video is a sensible adaptation of existing adaptive normalization techniques; the combination is novel but not groundbreaking.

**Importance:** 8/10 — A scalable interactive world model for robot manipulation addresses a real bottleneck in robot learning. The trajectory-to-video formulation is practically motivated.

**Claims support:** 6/10 — The core claim that Mani-WM as a system outperforms baselines is supported. However, the claim of Transformer superiority is conflated with the conditioning scheme, and the planning experiment lacks a meaningful comparison point.

**Soundness:** 7/10 — Experimental design is generally solid with multiple datasets, human evaluation, and real-robot validation. The main weakness is the confounded baseline comparison and missing ablations.

**Clarity:** 7/10 — The method description is clear, but the paper would benefit from more precise claims about what the experiments actually demonstrate.

**Value:** 7/10 — The paper provides a useful system with strong empirical results that will likely be a useful reference for building robot world models.

The paper makes a solid contribution — an effective system for trajectory-to-video generation with good empirical results across multiple datasets and a real robot. The main weaknesses are (a) an overclaimed attribution of gains to the Transformer backbone without proper isolation, and (b) a weak planning baseline. Neither is fatal: the core contribution (Mani-WM as a full system with frame-level conditioning) is well-supported, and the weaknesses are addressable. The paper would benefit from revisions to calibrate claims and add ablations, but in its current form it represents a useful and well-executed contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>