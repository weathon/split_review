Now I have all the information I need. Let me compose the final review.

---

## Summary

This paper introduces ARSS, the first decoder-only autoregressive (GPT-style) framework for camera-controlled novel view synthesis from a single image. The approach tokenizes multi-view sequences via a video tokenizer, encodes camera trajectories into latent tokens via a dedicated camera autoencoder with geometric losses, and uses a hybrid token permutation strategy (random spatial order within each frame, fixed temporal order across frames) to enable causal next-token prediction while respecting the bi-directional nature of visual data. Experiments on RealEstate10K, ACID, and zero-shot on DL3DV show competitive results against diffusion-based and feed-forward baselines, with Table 1 reporting best PSNR (19.02) and LPIPS (0.269) on RealEstate10K and best zero-shot PSNR (16.70) on DL3DV.

## Strengths

- **First decoder-only AR model for camera-controlled NVS.** The paper genuinely delivers the first application of a causal decoder-only transformer to novel view synthesis with explicit camera trajectory conditioning (stated in Abstract and Section 5). This is a clear conceptual contribution that opens a new direction in NVS separate from the diffusion-dominated landscape.

- **Camera autoencoder with geometric loss for 3D positional guidance.** The design of a dedicated camera autoencoder that compresses Plücker raymaps into latent tokens with geometrically-motivated losses (Eq. 5: ray direction, momentum, unit-norm, orthogonality) provides per-token 3D conditioning. Combining this with the hybrid permutation strategy creates a mechanism where camera tokens serve as positional instruction tokens analogous to those used in prior AR image generation work, but now extended to the 3D multi-view setting.

- **Hybrid token permutation is well-validated by ablation.** The ablation in Table 2 and Figure 7 convincingly demonstrates the value of the proposed permutation strategy: it substantially outperforms both raster-order (PSNR 16.29→19.22) and full spatiotemporal permutation (PSNR 18.76→19.22), with clear qualitative improvements. This directly validates a core design choice.

- **Competitive quantitative results with controlled ablations.** Table 1 shows ARSS achieving the best PSNR (19.02) and LPIPS (0.269) on RealEstate10K and best zero-shot PSNR (16.70) on DL3DV among all compared methods. The video-tokenizer ablation (Table 3), showing FVD improvement from 137.68 (VQ) to 52.56 (video tokenizer), confirms the importance of temporal encoding for this task.

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation of the camera autoencoder design.** The camera autoencoder with geometric losses is a central contribution—it provides the 3D positional guidance that enables spatial permutation with correct localization. Yet the paper provides no experiment that isolates its contribution. The paper should compare against simpler alternatives: directly feeding Plücker coordinates as per-token conditioning without a learned encoder, using only a global camera embedding per frame, or removing camera tokens entirely and relying solely on spatial permutation (which would test whether the permutation strategy alone carries 3D information). Without this, it is unclear whether the complexity of training a separate autoencoder is justified or whether the reported gains come from the camera tokens at all. This is a structural gap in the evidence for the method's design.

- **SEVA omitted from the error accumulation analysis (Figure 6).** The per-frame quality comparison in Figure 6 plots PSNR/SSIM/LPIPS over 16 frames for LVSM (mislabeled "L2SM"), MotionCtrl, RayZer, and ViewCrafter—but excludes SEVA, which is ARSS's strongest diffusion-based competitor (Table 1 shows SEVA achieves competitive SSIM 0.670 vs. ARSS 0.624 on RealEstate10K). The paper states that ARSS "accumulates significantly less error over time," but this claim is only supported against weaker baselines. SEVA uses a two-stage generation (anchor + interpolation) that may have different error accumulation characteristics, and its inclusion is necessary to substantiate the claim that causal generation offers a concrete advantage over diffusion for long trajectories.

- **Baseline evaluation protocol is uncontrolled.** Table 1 reports numbers for SEVA, Genwarp, MotionCtrl, LVSM, etc., but the paper never states whether these baselines were re-evaluated under the same conditions (same frame selection, trajectory length, resolution). ARSS uses 256×256 resolution while SEVA is known to use 512×512; resolution differences directly affect PSNR, SSIM, LPIPS, and FID. If the numbers are cited from original papers with different protocols, the "outperforms most baselines" claim is not reliable. The paper should either re-evaluate baselines under matched conditions or explicitly flag which numbers are from original publications and discuss potential confounds.

### Minor

- **"Trained from scratch" claim is ambiguous and potentially misleading.** The Discussion (Section 5) states that "our method is trained from scratch using limited public datasets" and contrasts this with diffusion methods that "mostly finetuned from pre-trained models." However, the Implementation Details reveal that ARSS adopts LlamaGen as its backbone model and VidTok as the video tokenizer—both pretrained models. If the transformer backbone is initialized from LlamaGen weights, this is fine-tuning, not training from scratch. If only the architecture is borrowed with random initialization, this should be stated clearly. As written, the claim undermines the narrative of lightweight, accessible training.

- **Missing inference speed and parallel decoding details.** The paper mentions that random shuffling "allows parallel decoding (Pang et al., 2025)" and that "the system has the capacity to predict multiple tokens at one time," but does not report whether parallel decoding is actually used, what speedup is achieved, or any inference-time cost. For an autoregressive method being positioned as an alternative to diffusion, practical inference throughput is an important point of comparison.

- **Equation 7 is incompletely specified.** As written, `L = CE(f_θ([S, [x_{21}^{P2(1)}, ..., x_{ln}^{Pl(n)}]]))` appears to pass only one argument to the cross-entropy function, whereas Eq. 3 shows the expected two-argument form `CE(predicted, target)`. This is likely a formatting artifact from PDF extraction, but the authors should clarify the correct formulation showing the shift between input and target sequences.

- **Camera autoencoder architecture is underspecified.** The architecture is described only as "stacked 3D convolutional and downsampling blocks" (encoder) with symmetric upsampling (decoder). The number of layers, channels, downsample factors, latent dimension, and training details (dataset, iterations, learning rate) are not provided. This is insufficient for reproduction.

- **Quantitative comparison with SEVA is discussed but not contextualized by controlled experiments.** The paper notes that ARSS has lower SSIM and higher FID than SEVA on RealEstate10K and ACID, attributing this to SEVA's "large-scale, high-resolution training data and heavy computational resources." This may be accurate, but without a controlled experiment (e.g., training ARSS at higher resolution or with more data), this explanation remains speculative.

### Trivial

- **"L2SM" typo in Figure 6 caption.** The figure labels one method as "L2SM" which appears to be a typo for LVSM.
- **Duplicate period in implementation details:** "The learning rate is set to $5e-4$ with 5K steps warm up and a cosine schedule to decrease to 0 after the warm up steps. ." (extra period before the space).

## Nice-to-Haves
- The VQ vs. video tokenizer ablation (Table 3) is useful but unsurprising—a more informative comparison would be against a video tokenizer without causal structure, or against an image tokenizer with explicit inter-frame post-processing.
- Temporal consistency evaluation beyond FVD (e.g., temporal warping error, human evaluation of flicker) would strengthen the video-quality claims.
- Zero-shot evaluation on DL3DV would be stronger if it included a diffusion method also not trained on DL3DV (the current comparison only includes MotionCtrl and LVSM).
- Provide a forward-looking discussion of how the causal structure enables dynamic trajectory extension (e.g., incrementally adding new views), which is claimed as a conceptual advantage but never demonstrated.

## Removed Points
- **Criticism that "paper never demonstrates a concrete advantage of causal structure in practice"** (e.g., incremental generation). While fair as a limitation, this is a nice-to-have beyond the paper's stated scope of demonstrating competitive performance on fixed-length trajectories. The error accumulation analysis partially addresses this advantage.
- **Criticism that VQ tokenizer ablation is "unsurprising"** — this is a matter of opinion; the ablation is valid and informative. Retained only as a note in Nice-to-Haves.
- **Criticism about missing related works** — removed per instructions (cannot verify existence of external works).
- **Request for diversity/confidence intervals** — not standard practice in this evaluation setting; removed as scope creep.
- **Strength about "slower error accumulation"** — partially retained but weakened by the SEVA omission weakness, which is noted.
- **Strength Finder's generic strengths** (e.g., "addressed an important problem") — removed per instructions as generic/superficial.

## Novel Insights

The most notable observation from cross-referencing the reviews with the paper is that the hybrid token permutation strategy (random spatial order, fixed temporal order) appears to be doing most of the heavy lifting. Table 2 shows it accounts for a ~3 PSNR gain over raster order and ~0.5 PSNR gain over full spatiotemporal permutation. However, the camera autoencoder's contribution to these gains is not isolated from the permutation strategy—it could be that the permutation itself, combined with any form of position token (not necessarily the learned camera autoencoder), would yield similar gains. This is a missed diagnostic opportunity. The paper's second important (implicit) finding is that a decoder-only AR pipeline can match diffusion-based NVS on standard benchmarks using only 256×256 resolution and modest compute (8×H100, 100K iterations), which is a genuine data point for the field about the viability of alternative generative paradigms.

## Suggestions
1. **Add a camera autoencoder ablation.** Compare against: (a) directly feeding Plücker coordinates as per-token embeddings without a learned encoder; (b) a single global camera embedding per frame; (c) removing camera tokens entirely. This is the single most important addition to validate the method's design.
2. **Include SEVA in the error accumulation analysis** (Figure 6). Report per-frame metrics for SEVA or, if its two-stage generation prevents this, explain why and provide alternative evidence.
3. **Clarify the evaluation protocol for Table 1.** State explicitly whether baselines were re-evaluated under matched conditions or whether numbers are cited from original papers. If cited, add a caveat in the table caption.
4. **Clarify the "trained from scratch" claim.** Specify whether LlamaGen weights were used for initialization or whether the transformer was randomly initialized. Revise the Discussion to accurately reflect the training setup.
5. **Report inference speed.** Provide tokens per second and total time for generating a 16-frame trajectory. Clarify whether parallel decoding is used.
6. **Fix the "L2SM" typo** in Figure 6 to "LVSM" and provide more architectural details for the camera autoencoder.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Searched for similar papers in three bands:
- Low band (score < 3.5): mostly unrelated papers (dynamic view synthesis, visual odometry). 
- Middle band (3.5–7.5): Four anchors including ArchonView (avg 5.00, Reject) — an autoregressive model for zero-shot single-image NVS — and Kaleido (avg 4.50, Accept Poster) — a sequence-to-sequence NVS model. These are the most topically relevant.
- High band (> 7.5): papers at score 8.00 that are largely unrelated (text-to-3D, navigation, visual geometry learning).

**Initial bracket:** 4.0 – 6.0.

**Round 2 (Narrowing):** Searched within (4.0, 6.0) and (4.0, 6.5) with topic-specific queries. Retrieved:
- ArchonView (avg 5.00, Reject, scores 2/8/4/6) — most similar: also autoregressive single-image NVS with "trained from scratch" claim while using pretrained components. ArchonView had stronger evaluation (more benchmarks, better ablations, inference speed reported) but easier task (object-centric, no camera control).
- Kaleido (avg 4.50, Accept Poster, scores 2/6/6/4) — sequence-to-sequence NVS, accepted despite missing comparisons, but with more thorough ablation and scaling analysis.
- SHARP (avg 5.00, Accept Poster, scores 6/4/4/6) — feed-forward 3DGS regression, clean evaluation but engineering-focused contribution.
- "Faithfulness" NVS (avg 5.50, Reject, scores 4/8/6/4) — training-free diffusion-based NVS, rejected despite high scores due to evaluation concerns.
- XFactor (avg 6.00, Accept Oral, scores 4/6/8/6) — strong self-supervised NVS with clear theoretical framing, much stronger overall.
- AR4D (avg 4.50, Withdrawn/Reject, scores 6/4/4/4) — autoregressive but for 4D generation, similar issue with "SDS-free" claim contradicted by use of MVDream.

**Final calibrated score:** The paper sits between ArchonView (5.00, Reject) and AR4D/Kaleido (4.50, Reject/Accept). ARSS has a stronger novelty claim than Kaleido (which was accepted) but weaker evaluation (missing camera AE ablation, uncontrolled comparisons, selective omission from error analysis). Compared to ArchonView (which was rejected despite cleaner evaluation), ARSS's evaluation gaps are more significant while tackling a harder problem. On balance, the paper is at the borderline: genuine contribution, but the evaluation gaps prevent the claims from being fully established.

**Final score: 4.5.** This reflects a paper with a clear conceptual contribution whose evidential support is incomplete in several structurally important ways.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>