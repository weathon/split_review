Now I have a comprehensive view of the paper, the reviews, and the calibration anchors. Let me synthesize the final review.

## Summary of Calibration

**Round 1 bracket**: The paper falls between the weak band (scores ~2.6–3.4, weakly related) and the strong band (7.67+, top papers like LVSM). The middle band contains papers scoring 5.00–6.50.

**Round 2 narrowing**: I read full reviews of AR-1-to-3 (5.00, Reject), GST (6.25, Accept), Zero-shot NVS (6.00, Accept), 4DiM (6.50, Accept), CamTrol (5.80, Accept), and Training-free Camera Control (5.80, Accept).

**Positioning**: ARSS is clearly stronger than AR-1-to-3 (5.00) — more datasets, stronger ablations, more novel architecture. It is comparable to Training-free Camera Control (5.80) and Zero-shot NVS (6.00) but has methodological gaps (camera autoencoder not validated) that keep it from reaching the level of GST (6.25) or 4DiM (6.50). **Final score: 5.5** — borderline, needs substantial revision.

Now let me write the review.

---

# Final Consolidated Review

## Summary
ARSS proposes the first decoder-only autoregressive transformer (GPT-style) for novel view synthesis from a single image, conditioned on a camera trajectory. The method uses a video tokenizer for temporally consistent discrete tokens, a camera autoencoder that converts Plücker raymaps into 3D positional guidance tokens, and a hybrid token permutation strategy (spatial-only shuffle preserving temporal order). Experiments on RealEstate10K, ACID, and zero-shot DL3DV show competitive results against diffusion-based NVS methods.

## Strengths

- **Novel architecture for causal NVS.** ARSS is the first to apply a decoder-only causal autoregressive model to novel view synthesis with explicit camera control (lines 111–113). This is a genuine architectural contribution that opens a new direction in NVS beyond the dominant diffusion paradigm. The results in Table 1 confirm that this approach can compete with established diffusion-based methods.

- **Hybrid token permutation strategy is well-motivated and validated.** The spatial-only shuffle (preserving temporal order) is cleanly motivated and ablated in Table 2 and Figure 7. It significantly outperforms both raster-order (PSNR 19.22 vs 16.29) and full-permutation (19.22 vs 18.76). The visual evidence in Figure 7 confirms the geometric distortions that the other strategies introduce.

- **Error-accumulation analysis demonstrates a genuine advantage of the causal AR structure.** Figure 6 shows that ARSS maintains consistently higher PSNR/SSIM and lower LPIPS across 16-frame trajectories, with flatter degradation slopes than all baselines. This directly supports the paper's motivation that causal generation is beneficial for long-horizon view synthesis.

- **Clean ablations.** The paper provides thorough ablations on both the token permutation strategy (Table 2) and the tokenizer choice (Table 3), clearly isolating the contribution of each design decision.

## Weaknesses

### Major

1. **Camera autoencoder is central to the contribution but its reconstruction quality is never validated.** The camera tokens are a core claimed contribution — they provide "3D positional guidance" that enables spatial permutation and camera control. However, the paper reports no metrics on the camera autoencoder's reconstruction accuracy (e.g., mean angular error of ray directions, depth error, whether the unit-norm and orthogonality constraints are satisfied after reconstruction). Without this validation, it is unclear whether the camera tokens actually encode useful 3D geometry, or whether the model relies primarily on temporal ordering and visual context. An ablation that **replaces camera tokens with learnable positional embeddings** (indexed by frame number and spatial position) would directly test this, and its absence is a significant methodological gap.

2. **Baseline comparisons have fairness concerns that are not fully addressed.** LVSM (designed for 2–3 input views), RayZer (designed for multiple posed images), and ViewCrafter (typically uses multiple conditioning frames) are tested with a single input view, which is a setting their architectures were not designed for. The paper does not describe how these baselines were adapted. While SEVA and Genwarp are directly comparable (same task), the inclusion of methods tested out-of-regime inflates the appearance of superiority. The paper's main claim — "consistently outperforms most of the baselines" — would be more reliably supported if the comparison focused on methods designed for the same single-view setting or described the adaptation procedure in detail.

3. **Unexplained discrepancy between Table 1 and Table 2.** The "Ours" row in Table 1 reports PSNR 19.02, SSIM 0.624 on RealEstate10K, while the "ours" row in Table 2 reports PSNR 19.22, SSIM 0.565 (the same dataset, same method). The SSIM gap (0.624 vs 0.565) is substantial. The paper does not explain whether these come from different evaluation splits, different random seeds, or different settings. This needs clarification because it affects the reliability of the reported numbers.

### Minor

1. **Sampling / decoding strategy not specified.** The paper mentions "iteratively sample the target tokens using a next-token prediction manner" (line 375) and "parallel decoding" (line 262), but does not specify the sampling strategy: temperature, top-k, top-p, or greedy decoding. This affects both reproducibility and quality. Autoregressive model behavior is highly sensitive to sampling parameters.

2. **Camera autoencoder loss notation is sloppy.** In Eq. 5, the paper writes "$\mathbf{d}$ is the momentum term formulated as $\mathbf{m} = \mathbf{o} \times \mathbf{d}$" — the same symbol $\mathbf{d}$ is used for both the direction and, incorrectly, the momentum. It should read "$\mathbf{m}$ is the momentum term." This is a minor but distracting error in a key equation.

### Trivial

- "purpose" should be "propose" (lines 126, 127).
- Extra period in "steps. . We apply" (line 348).

## Nice-to-Haves
- A direct demonstration of the claimed advantage of causal generation over joint generation: an experiment where a user adds an extra view to a trajectory and ARSS generates only the new view (without regenerating the full sequence), while a diffusion method must regenerate everything.
- A diversity/stochasticity analysis: NVS should ideally be deterministic given the input and camera trajectory, but the paper does not discuss whether multiple runs produce consistent results or vary stochastically.
- Explicit discussion of AR video generation methods (e.g., Phenaki, VideoPoet) in related work to clarify how ARSS differs from / improves upon these (the key difference being explicit camera control for NVS, which these methods lack).

## Removed Points

These points were raised in the inputs but are removed for the following reasons:

- **"Methods like MotionCtrl and Genwarp are video-diffusion methods not specifically tuned for NVS from a single input view"** — Partially retained above (item 2 in Major). The critic's framing that this "invalidates the claimed superiority" is too strong; SEVA and Genwarp are directly designed for single-view NVS, and the paper acknowledges mixed results with SEVA. The concern is real but not fatal. Retained in weakened form.

- **"The paper does not adequately situate itself relative to prior AR-based video/multi-view generation methods (Phenaki, VideoPoet, TATS)"** — Removed. These are text-to-video AR generation methods, not NVS methods with camera control. The paper's novelty claim is about NVS with explicit camera control, not AR video generation generally. However, a brief discussion would strengthen the paper; moved to Nice-to-Haves.

- **"Data leakage issue regarding the first frame"** — Removed. The paper's description of the training/inference setup (lines 344–375) is sufficiently clear: the input view's tokens are always visible, camera tokens for target views are provided as condition. This is a standard conditional generation setup, not a data leakage issue.

- **"The paper does not report inference cost"** — Removed. This is a nice-to-have but not a core weakness. Many NVS papers do not report detailed inference costs.

- **"The claim of being the first AR NVS method is weakened by not comparing against any AR video baseline"** — Removed. There are no existing AR video baselines designed for single-view NVS with camera control. The claim is appropriately scoped to the specific setting.

- **"Missing comparison with Cat3D or other 3D reconstruction-based methods"** — Removed. These address a different problem setup (multi-view to 3D vs single-view to multi-view). The paper scopes its task appropriately.

- **"Inference details missing: The sampling strategy (temperature, top-k, top-p) is not specified"** — Moved to Minor (item 1 above). This is a valid point but minor relative to the core contributions.

- **"No human evaluation"** — Removed. Human evaluation is valuable but not standard for benchmarking NVS on established datasets with ground-truth views. Pixel-aligned and perceptual metrics are the norm.

- **"No diversity evaluation"** — Moved to Nice-to-Haves. Relevant but not a core flaw.

## Novel Insights
None beyond the paper's own contributions. The reviews primarily surface concerns about validation of the camera autoencoder and baseline fairness rather than synthesizing novel observations about the method itself.

## Suggestions

1. **Validate the camera autoencoder.** Report reconstruction accuracy (mean angular error, unit-norm violation, orthogonality error) on held-out camera trajectories. Show that perturbing camera tokens leads to expected view changes, or that nearest-neighbor camera tokens in latent space correspond to geometrically similar poses.

2. **Ablate camera tokens.** Replace camera tokens with learnable positional embeddings indexed by (frame, spatial position). If performance drops significantly, the 3D information is crucial. This would be the cleanest validation of a core contribution.

3. **Explain the Table 1 vs Table 2 discrepancy.** State whether these come from different evaluation splits, different random seeds, or other factors. If the ablation uses a subset, say so explicitly.

4. **Clarify baseline adaptation.** Describe how LVSM, RayZer, and ViewCrafter were adapted to the single-view setting. If they were given only one input view, state this explicitly. If the results in Table 1 for these methods are from their original papers or from re-implementation, clarify the source.

5. **Specify sampling parameters.** Report temperature, top-k, top-p, or note that greedy decoding was used.

## Score and Decision

All anchors retrieved:

| Anchor ID | Avg Score | Round | Comparison to ARSS |
|-----------|-----------|-------|-------------------|
| I86z54CL2y (GeoGS3D) | 3.40 | R1 | Weaker — different task, lower quality |
| hWlCc7Iksi (ARVideo) | 3.40 | R1 | Weaker — video representation learning, not NVS |
| hrXt6Fdl2P (FV-NeRV) | 2.60 | R1 | Much weaker — compression task |
| mHkbi3XM58 (Cond. density) | 3.25 | R1 | Weaker — different formulation |
| pOcGFvfgjS (AR-1-to-3) | 5.00 | R1/R2 | Weaker — similar task but less evaluation, weaker ablations, diffusion+AR not pure AR |
| NuHYh4YKNe (GST) | 6.25 | R1/R2 | Stronger — joint pose+NVS, accepted, more comprehensive |
| QQBPWtvtcn (LVSM) | 7.67 | R1 | Much stronger — accepted with high scores |
| zDJf7fvdid (Zero-shot NVS) | 6.00 | R2 | Slightly stronger — training-free, accepted |
| KUz8QXAgFV (Bridging AR) | 5.50 | R2 | Similar — different task, both have methodological gaps |
| KI1zldOFz9 (CamTrol) | 5.80 | R2 | Slightly stronger — accepted, training-free camera control |
| d2UrCGtntF (4DiM) | 6.50 | R2 | Stronger — more comprehensive, higher resolution, accepted |
| VLuJL8cnGk (3D-free meets 3D) | 5.00 | R2 | Weaker — rejected |
| tJoS2d0Onf (SV4D) | 6.25 | R2 | Stronger — accepted |
| fectsEG2GU (Diffusion²) | 6.25 | R2 | Stronger — accepted |

**Round 1 bracket**: Between 3.5 and 7.5. **Round 2 narrowing**: The paper is weaker than GST (6.25) and 4DiM (6.50), comparable to training-free methods like CamTrol (5.80), and stronger than AR-1-to-3 (5.00).

The paper has a genuine contribution (first decoder-only AR for NVS with camera control) and strong ablations, but the camera autoencoder validation gap and baseline fairness concerns are significant weaknesses. The paper is borderline — it would need substantial revision (particularly validating the camera autoencoder and addressing baseline concerns) to be a clear accept.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>