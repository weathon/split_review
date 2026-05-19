Now I have all the information needed to write the final consolidated review.

## Summary

STORM presents a feed-forward Transformer architecture for reconstructing dynamic outdoor scenes from sparse multi-view, multi-timestep posed images. It predicts per-frame 3D Gaussians with associated velocities, aggregates them into an amodal representation via velocity-based transformation, and is trained with only reconstruction losses. Motion tokens enable emergent motion grouping and unsupervised segmentation. Experiments on Waymo, NuScenes, and Argoverse2 show STORM outperforms both per-scene optimization methods and existing feed-forward models in rendering quality while being roughly 1000× faster than per-scene approaches.

---

## Strengths

1. **Novel architecture for feed-forward dynamic scene reconstruction.** STORM is the first method to use a pure Transformer to jointly predict 3D Gaussians and their scene flows from sparse temporal views in a single forward pass. The motion-token design (Section 3.1, Eq. 3–5) is a clean mechanism for capturing low-dimensional motion structure while enabling emergent grouping.

2. **1000× speedup over per-scene optimization.** Per-scene methods (EmerNeRF, PVG, DeformableGS) take 1,000–1,500 s to optimize a 2-second clip; STORM reconstructs it in 0.18 s (Table 1). This is a qualitative difference in capability, validated by explicit timing on a single A100 GPU.

3. **Strong quantitative results across multiple outdoor datasets.** On Waymo (Table 1), STORM achieves 26.78 full-image PSNR, surpassing the best feed-forward baseline by +1.5 dB and the best per-scene method by ~0.5 dB. On NuScenes and Argoverse2 (Table 2.1), it also achieves best full-image PSNR and Depth RMSE among generalizable methods, demonstrating cross-dataset generalization.

4. **Self-supervised scene flow estimation competitive with LiDAR-based methods.** In Table 3, STORM achieves EPE3D of 0.11 vs. 0.23 (NSFP) and 0.18 (NSFP++) while using only camera images at test time, whereas the baselines require LiDAR input. This is a genuine advance for practical deployment.

5. **Practical design for in-the-wild scenes.** The sky token and affine token (Section 3.2) address real artifacts in driving data — sky regions with undefined depth and camera exposure mismatch — with clear visual evidence in Figure 2. The Latent-STORM variant further improves fine-grained human motion reconstruction (Figure 3) and large-view extrapolation.

---

## Weaknesses

### Fatal
None.

### Major

- **Dynamic-region evaluation metric is undefined, undermining the headline quantitative claim.** The paper reports PSNR gains of +5 dB on "dynamic regions" (Table 1) and prominently features this in the abstract and results section, but never specifies how these regions are defined. Is the mask computed from ground-truth 3D bounding boxes (available in Waymo), from a pretrained segmentation model, or from the model's own motion token assignments? If the latter, the metric is circular — it measures fit on the same regions the model is biased to allocate Gaussians to, while per-scene baselines that optimize a single global representation may be unfairly penalized. Without a documented, independent protocol, the main quantitative claim (+5 dB, +0.346 SSIM over PVG) cannot be verified or compared against by future work. This is the single most important issue to resolve.

### Minor

- **Depth supervision source is not disclosed, making the "self-supervised" framing imprecise.** The reconstruction loss includes a depth term (Section 3.3). The paper never states where the depth ground truth comes from. The baseline sentence "Since LiDAR data is not provided at test time in our setup, we train these baselines without LiDAR supervision to ensure a fair comparison" (Section 4.1) strongly implies that STORM *does* use LiDAR depth during training. If so, the method is not purely self-supervised — it uses a LiDAR-derived geometric signal. The abstract and introduction should be clarified to avoid claiming "solely a self-supervised reconstruction loss." This is a disclosure issue, not a methodological flaw, but it matters for honest positioning.

- **Motion segmentation is claimed but only evaluated qualitatively.** The paper states that motion tokens yield "high-quality masks" and demonstrate "instance-level or motion-level segmentations" as an emergent property (Figures 1, 6), but reports no segmentation metric (mIoU, F1, etc.) against any ground truth. Waymo provides 3D bounding boxes that can be projected to pixel masks. Without quantitative evaluation, the segmentation claim remains anecdotal, and applications like scene editing (Figure 7) rely on segmentation quality that is unverified.

- **Ablation study is extremely brief and lacks numerical support.** The entire ablation section (Section 4.3) is three sentences with no tables or figures. The paper states that without velocity regularization "training collapses" and that STORM is "robust to the choice of M" and shows "zero-shot generalization to varying input timesteps," but provides no learning curves or ablation tables to back these claims. For a paper with novel design components (motion tokens, velocity regularization), this is inadequate evidence.

- **Sky region identification mechanism is unexplained.** The sky loss "encourages zero opacity for Gaussians on the sky-region" (Section 3.3), but the paper does not specify how sky regions are identified during training. If this relies on a pretrained segmentation model or heuristic, that is additional supervision worth disclosing.

- **Training details missing.** Total training time, number of GPUs, optimizer hyperparameters, and dataset preprocessing steps are not reported, limiting reproducibility.

### Trivial
None.

---

## Nice-to-Haves

- Quantitative point-tracking evaluation (e.g., against ground-truth trajectories or OmniMotion) would strengthen the motion estimation claims beyond qualitative demos (Figure 5).
- A failure analysis discussing cases where the constant-velocity assumption breaks (accelerating/braking objects) would improve credibility.
- Reporting inference time for Latent-STORM separately from STORM would clarify the speed-quality trade-off.
- A discussion of the reasoning behind forward/backward velocity vectors vs. a single velocity would help readers understand the design choice.

---

## Removed Points

These points were flagged by reviewers but are removed or demoted after cross-checking against the paper:

- **Inference speed claim criticized as implausible.** The harsh critic's FLOPs computation (~3×10¹⁵ FLOPs → 10 s on A100) is inconsistent and inaccurate. A ViT-B processing ~7,200 tokens involves roughly 1–2 TFLOPs in the Transformer. At 312 TFLOPS peak on an A100 (and using flash-attention-optimized kernels), 0.18 s for the full pipeline (encoding, Transformer, mask decoder, Gaussian prediction, rasterization) is plausible and consistent with published benchmarks for similar architectures. This criticism is removed as it is based on erroneous arithmetic.

- **Missing related works.** Per instructions, I cannot confirm omitted citations without external sources.

- **Formatting and presentation nitpicks.** Parser artifacts are not author errors.

- **Generic scope-creep criticisms** (e.g., "should also do Y" for problems the paper explicitly scopes out).

---

## Novel Insights

The harsh critic's FLOPs-based attack on the speed claim and the strength finder's correct identification of the 1000× speedup as a core contribution together highlight something interesting: **the paper is straddling two very different evaluation regimes.** The speed claim belongs to systems-level reasoning (optimized kernels, memory bandwidth, practical pipeline profiling) while the rendering-quality claims belong to traditional computer-vision benchmarking. The paper would be stronger if it acknowledged this duality explicitly — providing standard FLOPs/parameter counts alongside wall-clock time — because the two regimes produce very different expectations in different readers. The critic's bad-FLOPs arithmetic and the strength-finder's pitch-perfect identification of the speed as a "qualitative difference" show that readers need both kinds of evidence.

---

## Suggestions

1. **Define the dynamic-region evaluation protocol clearly.** Report the source of dynamic masks (e.g., Waymo 3D bounding boxes projected to pixels), or use a precomputed, fixed segmentation from a third-party model applied to both STORM and all baselines. Publish this protocol so it is reproducible.

2. **Disclose the depth supervision source explicitly.** If LiDAR depth is used during training, state this clearly in Section 3.3 and qualify "self-supervised" in the abstract to avoid misleading readers. If depth comes from a monocular estimator, name the estimator.

3. **Expand the ablation study.** Add at least one table showing the effect of: (a) varying M (number of motion tokens), (b) removing velocity regularization (show gradient explosion), (c) varying λ_reg, and (d) number of input timesteps.

4. **Add quantitative segmentation evaluation.** Report mIoU or F1 against projected Waymo bounding boxes for the motion-grouping masks (Figure 6). Even a modest score would substantially strengthen the claim.

5. **Report training details** (GPU count, total training hours, optimizer, learning rate schedule, batch size) in the main paper or appendix.

---

## Score and Decision

**Originality:** High — first feed-forward Transformer for outdoor dynamic scene reconstruction with a novel motion-token mechanism.  
**Importance of research question:** High — enabling fast, scalable dynamic scene reconstruction from sparse inputs has clear applications in autonomous driving and robotics.  
**Claims supported:** Moderate — the strongest claim (+5 dB on dynamic regions) is not verifiable due to an undefined metric; other claims are well-supported.  
**Soundness of experiments:** Moderate — extensive evaluation across three datasets is commendable, but the missing dynamic-region definition and absent ablation tables weaken the evidence.  
**Clarity of writing:** Good — architecture and method are clearly described; missing evaluation details (dynamic region definition, depth source) are notable gaps.  
**Value to the research community:** High — code/model release promised, practical speed makes the approach reusable.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>