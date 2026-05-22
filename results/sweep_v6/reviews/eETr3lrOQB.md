Now I have a solid set of calibration anchors. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

---

**Anchor list (all returned from calibration batch):**  
1. **GMwRl2e9Y1** — "Restructuring VQ with Rotation Trick", avg 8.00. Clean mathematical contribution, extensive experiments across 11 VQ paradigms. Stronger than this paper in theoretical rigor and experimental control.
2. **yGnsH3gQ6U** — "BSQ-ViT", avg 5.75. Strong SOTA tokenizer with thorough benchmarks. Better controlled comparisons. Somewhat stronger.
3. **mb2ryuZ3wz** — "How many tokens is an image worth?", avg 5.75. Variable-length tokenizer with solid analysis but limited baselines. Comparable quality.
4. **nS2DBNydCC** — "VQ by Distribution Matching" (Wasserstein VQ), avg 4.75. Similar topic; criticized for Gaussian assumption and marginal improvements. Comparable or slightly weaker.
5. **ZVe2k7mNAP** — "MQ-VAE", avg 4.50. Meta-learning for VQ; limited to small datasets. Weaker.
6. **BmYzoPppij** — "LLMCO2", avg 3.33. Not topically similar; serves as low anchor.
7. **IqGVIU4rvM** — "Balancing Token Efficiency", avg 2.50. Fundamentally flawed with poor results. Much weaker.

---

## Summary

This paper proposes VQ-Transplant, a two-stage framework that replaces the VQ module in a pre-trained visual tokenizer (specifically VAR) while keeping the encoder-decoder frozen, then performs lightweight decoder adaptation (5 epochs). A secondary contribution is MMD-VQ, which uses Maximum Mean Discrepancy for distributional alignment between features and codebook. The framework is demonstrated across five VQ algorithms and achieves competitive reconstruction fidelity at a fraction of the training cost of full end-to-end training.

## Strengths

- **21.8× training speedup with competitive reconstruction fidelity.** Table 1 shows VQ-Transplant requires 44 GPU-hours (2×A100×22h) versus VAR's 960 GPU-hours (16×A100×60h), while MMD VAR (K=8192) achieves r-FID 0.81 versus VAR's 0.92 (Table 2). The speedup figure is clearly documented with specific hardware/configurations.

- **Plug-and-play integration of five distinct VQ methods.** Tables 3 and 7 demonstrate that VQ-Transplant successfully integrates Vanilla VQ, EMA VQ, Online VQ, Wasserstein VQ, and MMD VQ in both multi-scale and fixed-scale configurations into a single pre-trained VAR tokenizer. This shows generality beyond a single algorithm.

- **Lightweight decoder adaptation resolves quantization–decoder mismatch.** Table 3 shows that after VQ substitution, MMD VAR (K=8192) has r-FID 1.49, which improves to 0.81 after only 5 epochs of decoder adaptation — surpassing the original VAR tokenizer (0.92). Figure 2 provides visual corroboration.

- **Cross-dataset generalization.** Tables 8–10 show Wasserstein/MMD VQ via VQ-Transplant achieves strong reconstruction on FFHQ (r-FID 1.21), CelebA-HQ, and LSUN-Churches, demonstrating that the framework generalizes to datasets structurally different from ImageNet-1k/OpenImages.

- **VQ-Transplant outperforms from-scratch training under comparable compute.** Table 6 shows MMD VAR trained from scratch for 35 hours achieves r-FID 1.34 (K=4096) and 1.26 (K=8192), while VQ-Transplant at 22 hours achieves 0.91 and 0.81 respectively. This provides direct evidence of the efficiency benefit.

## Weaknesses

### Fatal

None.

### Major

- **Uncontrolled comparisons weaken the "state-of-the-art" claim.** In Table 2, baselines differ substantially in token count (256 vs 512 vs 680), codebook size, and architecture. MMD VAR with K=8192 achieves 0.81 r-FID versus VAR baseline with K=4096 at 0.92 — but the paper never runs VAR with K=8192 as a control. The improvement could partly reflect the larger codebook rather than the transplantation or MMD-VQ method. MMD VAR with K=4096 achieves 0.91 (essentially tied with VAR's 0.92), which suggests the K=8192 gain is due in part to the codebook scaling. Without proper controls, the headline "state-of-the-art" and "outperform" claims are overclaimed.

### Minor

- **MMD-VQ is not empirically distinguished from Wasserstein VQ.** The paper motivates MMD-VQ by arguing it handles non-Gaussian feature distributions without parametric assumptions (Section 4.2), but never demonstrates that (a) feature distributions are actually non-Gaussian, or (b) MMD-VQ outperforms Wasserstein VQ in any scenario where this matters. Across all tables (Table 3, 7, 8–10), Wasserstein VQ and MMD VQ produce nearly identical results (e.g., Table 3: both achieve quantization error 0.255/0.234). The claimed advantage is purely hypothetical. This weakens the secondary contribution significantly.

- **Only one base architecture (VAR) is tested.** The paper repeatedly calls VQ-Transplant a "plug-and-play" framework, but all experiments use a single pre-trained tokenizer (VAR). The LDM-16 experiment (Table 16 in appendix) shows lower compatibility. Without testing on VQGAN, ViT-VQGAN, or other architectures, the generality claim remains unsubstantiated.

- **5-epoch decoder adaptation length is somewhat arbitrary.** Table 5 shows that extending adaptation to 20 epochs yields further improvements (r-FID 0.74 vs 0.81 at K=8192). The paper acknowledges this but doesn't justify why 5 epochs is the "right" number for the headline results. This doesn't invalidate the core claim but is worth clarifying.

### Trivial

None.

## Nice-to-Haves
- A controlled experiment running the original VAR tokenizer with K=8192 (matching MMD VAR's codebook size) would cleanly separate the effect of VQ-Transplant from the effect of larger codebooks.
- A brief analysis of feature distribution Gaussianity (e.g., visualizing feature PCA or computing normality tests) would substantiate MMD-VQ's motivation.
- Testing on one additional base architecture (e.g., VQGAN) would significantly strengthen the generality claim.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

1. **"Deceptive efficiency claim"** — The harsh critic argues the 95% reduction excludes the cost of the pre-trained VAR tokenizer. However, the paper's *entire premise* is about plugging into a pre-trained tokenizer that is assumed to exist (e.g., released by others). The comparison is VQ-Transplant (for getting a *new VQ module*) vs. training VAR from scratch — a fair comparison for the stated use case. The paper is transparent about the hardware and time used. The 95% figure is an unconditional claim about the incremental cost of obtaining a tokenizer with a different VQ method, not about building one from scratch.

2. **"No downstream generation evaluation"** — The harsh critic demands generation experiments, but this is scope creep. Tokenizer papers (VQGAN, VAR, VQVAE, BSQ-ViT) standardly evaluate reconstruction fidelity. Generation is downstream and not required to validate the core contribution.

3. **"From-scratch training uses too few epochs"** — The paper explicitly acknowledges that "discrete tokenizers typically require hundreds of epochs to achieve high-quality visual reconstruction when trained from scratch." The comparison is about efficiency: VQ-Transplant achieves good results in 22h while from-scratch achieves poor results even with 35h. This is valid evidence for the efficiency claim.

4. **"VAR Tokenizer w/o VQ is unclear"** — This baseline is the encoder-decoder output without quantization. It is a meaningful reference point to show quantization's effect on reconstruction.

5. **Strength: "MMD-VQ achieves 100% codebook utilization with lower quantization error"** — Wasserstein VQ achieves the identical numbers (0.255/0.234 quantization error, 100% utilization). This strength conflicts with the verified weakness that MMD-VQ is not differentiated from Wasserstein VQ. The weakness wins.

## Novel Insights

The reviews surface an interesting tension: the paper's primary contribution (VQ-Transplant as a modular framework) is practically useful and well-demonstrated, but it is paired with a secondary contribution (MMD-VQ) that is empirically indistinguishable from the prior Wasserstein VQ. This creates a mismatch between the narrative (which sells MMD-VQ as a novel method) and the evidence (which shows it performs equivalently). A cleaner paper might have focused solely on the VQ-Transplant framework and treated MMD as an incremental variant of Wasserstein VQ rather than a standalone contribution. Additionally, the uncontrolled comparisons highlight a recurring issue in tokenizer papers: comparing methods that differ in token count, codebook size, and architecture simultaneously makes it impossible to attribute improvements to any single factor.

## Suggestions

1. **Control for codebook size when comparing to VAR.** Add a row to Table 2 with VAR using K=8192. This would cleanly separate the effect of larger codebooks from the effect of MMD-VQ/VQ-Transplant.
2. **Tone down or qualify the "state-of-the-art" claim.** Explicitly note that cross-method comparisons involve different token counts and codebook sizes, and that a controlled comparison shows MMD VAR at K=4096 matches VAR (0.91 vs 0.92).
3. **Either demonstrate MMD-VQ's advantage empirically or de-emphasize it.** Run a synthetic experiment where features are deliberately non-Gaussian (e.g., mixture of Gaussians, heavy-tailed) and show MMD-VQ outperforms Wasserstein VQ. If no advantage can be shown, present MMD-VQ as an alternative rather than an improvement.
4. **Test on at least one additional base architecture** to substantiate the "plug-and-play" claim. VQGAN would be the natural choice given its widespread use.

## Score and Decision

Compared to the calibration anchors:
- **Rotation Trick (8.00)**: Much cleaner theoretical contribution and more rigorous experimental control. Current paper is significantly weaker.
- **BSQ-ViT (5.75)**: Better controlled comparisons, SOTA on benchmarks. Current paper is slightly weaker.
- **How Many Tokens (5.75)**: Similar level of experimental rigor. Comparable.
- **Wasserstein VQ (4.75)**: Similar themes but current paper has a stronger primary contribution (practical framework vs. marginal improvement over vanilla VQ). Current paper is slightly stronger.
- **MQ-VAE (4.50)**: Limited to small datasets. Current paper is stronger.
- **LLMCO2 (3.33)** and **Balancing Token Efficiency (2.50)**: Much weaker papers.

The paper has a practical, sensible core contribution. The weaknesses are real but not fatal: the uncontrolled comparisons and undemonstrated MMD-VQ advantage weaken the claims without invalidating the framework's utility. With better controls and qualified claims, the paper would be stronger. In its current form it is borderline but leans toward rejectable at ICLR rigor levels — however the core idea is publishable with revisions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>