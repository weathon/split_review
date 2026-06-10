## Summary

Loopy proposes an end-to-end, audio-conditioned portrait video diffusion model that removes the need for manually specified spatial motion templates (face locators, speed layers) at inference time. Its two key technical contributions are: (i) **inter- and intra-clip temporal layers** with a temporal segment module (TSM) that extends the motion-frame receptive field from ~0.2 seconds to ~5 seconds — a roughly 25–30× increase — enabling the model to capture motion style (e.g., blink timing, head movement patterns) from long context; and (ii) an **audio-to-latents (A2L) module** trained with mixed audio and spatial-motion signals (landmarks, head/expression variance) that maps both to a shared set of learnable motion latents, so that at inference only audio is needed. Experiments on CelebV-HQ, RAVDESS, and an open-set test show consistent improvements over SadTalker, Hallo, VExpress, and EchoMimic on IQA, FVD, FID, and motion-dynamics metrics, with particularly strong gains on RAVDESS where motion dynamics (Glo, Exp) closely approach ground-truth values.

## Strengths

- **Inference-time template freedom is convincingly demonstrated.** The paper shows that removing face locators and speed layers (used by all prior end-to-end diffusion methods) while maintaining — and even improving — stability is possible via long-term temporal modeling. Table 1 shows Loopy achieving the best IQA (3.780 vs. Hallo's 3.505), Sync-C (4.849), FVD-Res (49.153), and FID (33.204) on CelebV-HQ without any auxiliary spatial conditions during inference. Table 2 further strengthens this: Loopy's Glo (2.962) and Exp (0.343) on RAVDESS are dramatically closer to ground truth (3.335, 0.317) than any competitor (the closest, EchoMimic, achieves Glo=0.641, Exp=0.184), directly proving the approach produces *more* natural motion, not less.

- **Temporal segment module extends motion-frame coverage by ~25–30× with a principled design.** The TSM compresses ~124 preceding frames (≈5 seconds at 25 fps) into 20 motion-frame latents using geometrically expanding segments (stride *s*, expand ratio *r*). This is validated by the ablation in Table 3: the full model (s=4, r=2) outperforms the narrower s=4, r=1 variant on IQA (4.507 vs. 4.424) and Sync-D (7.749 vs. 8.004), and removing TSM entirely degrades IQA from 4.507 to 4.386. The ablation explores 6 different s/r configurations and 3 sampling strategies, providing a thorough empirical characterization.

- **Systematic 12-variant ablation isolates each design choice.** Table 3 goes beyond simple component removal: it compares the full model against variants removing the inter-clip temporal layer, the TSM, the A2L module, using a single temporal layer with 20 motion frames, and exploring different TSM parameters (s=1–4, r=1–2, mean/random/uniform sampling). This allows readers to attribute gains to specific architectural decisions rather than global capacity effects.

- **Motion-dynamics metrics on RAVDESS provide uniquely strong evidence.** The near-ground-truth Glo and Exp scores (2.962 vs. 3.335, 0.343 vs. 0.317) demonstrate that the long temporal context genuinely captures motion style, not just appearance. Competing methods produce nearly static results (VExpress Glo=0.007, Hallo Glo=0.194), confirming that spatial templates suppress dynamics while Loopy's template-free approach preserves them.

## Weaknesses

### Major

- **Missing comparison with EMO, the closest methodological sibling.** The paper cites EMO (Tian et al., 2024) extensively — as the basis for the multi-layer wav2vec audio feature extraction (Section 3.3), the end-to-end single-diffusion paradigm (Section 2), the two-stage training strategy (Section 3.4), and the source of the E-FID metric. EMO uses the same dual-U-Net architecture with AnimateAnyone-style reference net and is the closest existing method to Loopy. Yet EMO is completely absent from all quantitative comparisons (Tables 1, 2, and the open-set user study) and from the ablation baselines. This omission makes it impossible to assess whether Loopy's specific innovations (separate inter-/intra-clip temporal layers, A2L module) improve over the strongest comparable framework rather than just over weaker or older baselines.

- **The training-data confound is not acknowledged.** Loopy is trained on 160 hours of proprietary web video plus HDTF. The compared methods (SadTalker, Hallo, VExpress, EchoMimic) are evaluated using their publicly released pretrained models, each trained on different (and likely smaller) datasets. The large FVD gap on RAVDESS (Loopy: 16.134 vs. Hallo: 38.471) and the Sync-C gap on CelebV-HQ (Loopy: 4.849 vs. Hallo: 4.130) could be partially driven by training data quality and quantity rather than architectural superiority. The paper should at minimum state this confound explicitly and ideally retrain one baseline (e.g., Hallo or the closest available method) on a matched data subset. Without this, the reader cannot cleanly attribute the reported gains to the method.

### Minor

- **The A2L module's claimed shared-representation mechanism is not directly verified.** The paper's central story is that the A2L module maps audio and spatial motion signals to a shared motion-latent space, allowing weakly correlated audio to benefit from strongly correlated spatial signals during training. However, the only evidence is the "w/o A2L" ablation (Table 3), which removes the entire module and conflates mixed training, learnable embeddings, and extra capacity. There is no direct analysis — no latent-space visualization (t-SNE, cosine similarity), no comparison of audio-derived vs. landmark-derived motion latents on the same samples, and no ablation isolating *why* the module helps (mixed training vs. learnable embeddings vs. extra capacity). The mechanism is a plausible story but lacks supporting evidence.

- **Several reproducibility details are missing.** (a) The Stable Diffusion version (SD 1.5, SD 2.1, or SDXL) is never specified — the paper says only "built upon Stable Diffusion (SD)" (Section 3.1). (b) It is unclear whether the reference network weights are frozen or trainable during the two-stage training process. (c) The "temporal squeezing" operation (Section 4.1, "After temporal squeezing, this was compressed to 20 motion frame latents") is described only by name; while the TSM mechanism is explained in Section 3.2, the connection is never explicitly made. (d) The paper does not discuss how 12-frame clips are stitched into long videos — the autoregressive generation strategy and mechanisms for temporal coherence across clip boundaries are absent.

- **Sync-C metric reliability is not contextualized.** On RAVDESS (Table 2), VExpress achieves the best Sync-C (5.001) despite producing nearly static outputs (Glo=0.007). The paper correctly notes that static videos inflate Sync-C scores. However, the same issue applies to Loopy's own Sync-C leadership on CelebV-HQ (Table 1), where Loopy's Glo (2.233) is still substantially below GT (3.249), meaning the generated videos are also less dynamic than real video. The paper should discuss whether Sync-C is a valid standalone ranking metric and whether the CelebV-HQ Sync-C advantage might partially reflect reduced motion rather than better synchronization.

- **The open-set user study is underspecified.** It uses only 10 users in a forced-choice per-dimension design. The paper does not report inter-annotator agreement, statistical significance, or confidence intervals. Given the small sample, the voting results (Figure 3) may not be reliable.

### Trivial

- Equation (1) labels the TSM output as a "mean value" but actually computes the midpoint frame index, not an average of frames within a segment. The formalism for start_index/end_index using \( k = \lfloor i/s \rfloor \) is also needlessly complex; a concise pseudocode description would be clearer.

- The term "temporal squeezing" is used exactly once (Section 4.1) without definition, though the TSM is the intended mechanism.

## Nice-to-Haves

- A direct comparison of motion statistics (blink frequency, head-movement autocorrelation, etc.) between Loopy and ground truth would sharpen the central claim that 5-second context produces more natural motion cycles.
- A runtime/FLOPs comparison between Loopy's 3-pass CFG inference and the overhead of the spatial condition modules it replaces (face locator MLP, speed layers) would help practitioners assess the computational trade-off.

## Removed Points

These points were considered but removed with justification:

- **"Template-free framing is overstated"** — The paper explicitly states that spatial signals (landmarks, head/expression variance) are used *during training* and only audio is used *during inference* (Section 3.3, "During testing, we only input audio to generate motion latents"; abstract, "during inference"). The claim is properly scoped; no overstatement.
- **"CFG cost not discussed"** — Valid as a practical consideration but not a weakness of the method's correctness or evidence. Moved to Nice-to-Haves.
- **Training data confound as a fatal flaw** — While valid as a concern, it does not invalidate the results; moved to Major rather than treated as fatal.
- Generic section-by-section nitpicks about presentation that do not affect the paper's core claims.

## Novel Insights

The reviews surface one insight that goes beyond the paper's own framing: the dramatic quality collapse in the "single temporal layer + 20 motion frames" ablation (IQA drops from 4.507 to 4.072, smoothness from 0.9932 to 0.9752) suggests that simply feeding more motion frames to a standard temporal layer is not just suboptimal but actively destabilizing. This implies the inter-/intra-clip separation is not merely a performance improvement but a *necessary* architectural condition for leveraging long temporal context — the standard single-temporal-layer design appears to conflate cross-clip motion patterns with intra-clip noise in a way that degrades both identity preservation and temporal stability. The paper does not discuss this collapse mechanism, but understanding why it happens (training instability? attention dilution? conflicting gradient signals?) could inform future architectural design for long-context video diffusion.

## Suggestions

1. **Add EMO to quantitative comparisons.** If weights were available, include EMO in Tables 1 and 2. If not, state this explicitly and explain why it could not be compared — the paper currently leaves the omission unaddressed.
2. **Acknowledge the training-data confound directly** in the experimental section, and if feasible, retrain one baseline (Hallo or EMO) on a matched data subset.
3. **Add a diagnostic analysis of the A2L latent space** — e.g., t-SNE visualization of motion latents from audio vs. spatial inputs, or cosine-similarity distributions — to verify the shared-representation claim.
4. **Specify the SD version** and clarify whether the reference network is frozen or trainable in stage 2.
5. **Explain the autoregressive inference pipeline:** how 12-frame clips are stitched, whether there is overlap, and how temporal coherence is maintained across clip boundaries.
6. **Report inter-annotator agreement or significance tests** for the open-set user study, or increase the number of participants.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Weak Accept</decision>