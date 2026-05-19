- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes Relay Diffusion Model (RDM), a cascaded diffusion framework that "continues" the diffusion process across resolutions instead of restarting from pure noise at each stage. The key ideas are: (1) a frequency-domain analysis showing that the same noise level yields higher SNR at higher resolutions, (2) "block noise" — correlated noise that approximates the spectral properties of upsampled low-resolution noise, and (3) patch-wise blurring diffusion to smoothly transition between stages. RDM achieves state-of-the-art sFID on ImageNet 256×256 (3.97 with guidance) and FID 3.15 on CelebA-HQ 256×256, and maintains strong sample quality at low sampling budgets.

## Strengths

- **Principled frequency-domain motivation for resolution-aware noise.** Section 3.1 and Figure 3 use DCT analysis to show that the same noise level produces higher SNR at higher resolutions, and that block noise (kernel size 4) on 256×256 nearly matches the frequency spectrum of independent Gaussian noise on 64×64. This provides a principled foundation for the relay mechanism — a contribution that is well-grounded and clearly illustrated.

- **State-of-the-art sFID on ImageNet 256×256.** Table 2 reports RDM achieves sFID 4.39 (no guidance) and 3.97 (with guidance + class balance), surpassing all prior diffusion models (ADM: 6.02, DiT-XL/2: 6.85, MDT-XL/2: 5.23) and even the GAN-based StyleGAN-XL (4.02). This result directly supports the paper's main performance claim.

- **Robust sample quality at low sampling budgets.** Figure 7 (Figure 6 in the paper) shows that at <200 NFE, RDM maintains near-peak FID while DiT-XL/2 and MDT-XL/2 degrade sharply. This is a practical advantage that follows from the relay design (skipping regeneration of low-frequency information).

- **Ablation evidence for core design choices.** The paper provides controlled comparisons validating: (a) block noise improves FID over isotropic-only noise (Figure 5), and (b) moderate stochasticity (η=0.2) significantly outperforms ODE sampling (Table 3, Table 4 in the paper). These go beyond typical system-level comparisons and help isolate the contribution of each component.

- **Training efficiency is clearly demonstrated.** RDM achieves competitive FID using ~1.2B training images versus MDT-XL/2's 1.7B, and the 64×64 stage uses 1/10 the FLOPs of the 256×256 stage, giving quantitative backing to the efficiency claims.

## Weaknesses

### Fatal
None.

### Major

- **Incomplete comparison with Cascaded Diffusion Models (CDM) and a partially inaccurate FID claim.** The paper states that RDM "outperforms all the other methods by FID except MDT-XL/2" (Section 4.2). However, Table 2 shows CDM (FID 4.88, no guidance) surpasses RDM without guidance (FID 5.27). CDM is the most directly related cascade baseline, yet the paper neither reports CDM's guided FID nor discusses this comparison. The core claim ("superiority over prior cascaded models") is partially supported — RDM wins on sFID and on FID *with* guidance — but the evidence is incomplete. This does not invalidate the paper's contributions (the sFID advantage is genuine and guidance closes the gap), but the authors should either report CDM's guided result, acknowledge the discrepancy, or clarify that the advantage is specific to sFID / guided settings.

### Minor

- **Hyperparameter α (block noise weight) lacks sensitivity analysis.** The block noise mixture weight α is set to 0.15 with no ablation across different values (e.g., 0.0, 0.05, 0.1, 0.2, 0.3). The ablation in Figure 5 only compares α>0 vs α=0. While this establishes that block noise helps, it does not characterize the method's robustness to the choice of α. A sensitivity sweep would strengthen the claim that block noise — rather than a specifically tuned weighting — is responsible for the gains.

- **Inconsistency between text and Algorithm 1 regarding block noise at sampling.** The text (end of Section 3.3, line 189) states that isotropic noise ε in the sampler "should be replaced" with Tilde{ε} — a weighted sum of block noise and isotropic noise. However, Algorithm 1 uses plain ε in all stochastic update steps (lines 206, 218) and initializes from isotropic Gaussian noise (line 196). If block noise is intended during sampling, the algorithm is missing this detail; if not, the text is misleading. This needs clarification.

- **Confusing NFE allocation notation in Figure 7 caption.** The caption states: "For allocation of NFE $=N$ in RDM, $10n+(\frac{N}{2}-n)$ means $10n$ for the first stage and $\frac{N}{2}-n$ for the second." The expression does not sum consistently: total FLOPs-adjusted NFE evaluates to N/2, not N. The notation appears to be in error or insufficiently explained, making the figure harder to interpret precisely.

### Trivial

- Minor typo: "stochaticity" in Section 4.3 (line 351).

## Nice-to-Haves

- An ablation of the blurring diffusion component (vs. using only block noise + isotropic noise without blurring) would more fully characterize the contribution of each design element.
- Reporting the total compute cost including the pretrained first stage (even though the checkpoint is reused) would aid practitioners in estimating resource requirements.
- A brief spectral visualization of how the block-noise / isotropic-noise mixture ratio changes as a function of the diffusion timestep (to illustrate why the simple weighted average works) would strengthen the intuitive explanation in Section 3.2.

## Removed Points

These points from the input reviews are removed or excluded from the main assessment:

- **"CelebA-HQ table lacks baselines from other diffusion cascades"** — The comparison set (LSGM, WaveDiff, LDM-4, StyleSwin) is adequate; the paper demonstrates improvement over StyleSwin (prior SOTA) with far fewer training iterations. ADM on CelebA-HQ is not a standard benchmark.
- **"Frequency analysis does not lead to a practical noise schedule"** — The paper openly acknowledges this in the conclusion. This is honest reporting, not a weakness. The paper's contribution is the relay mechanism, not an optimal schedule.
- **"Explanation of the weighted average is hand-wavy"** — The spectral intuition ("low-frequency component of block noise is much larger... vice versa") is reasonable and standard for a conference paper.
- **"No discussion of total compute cost"** — Moved to Nice-to-Haves; the paper does report training iterations and FLOPs comparisons, which is sufficient.
- **"Missing ablation of blurring diffusion vs. isotropic diffusion"** — Moved to Nice-to-Haves; the paper's contribution is the full relay mechanism, not isolating blurring diffusion specifically.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the CDM comparison.** Add a sentence discussing CDM's FID result (4.88) relative to RDM without guidance (5.27), and report CDM's guided FID if available. Qualify the claim "outperforms all other methods by FID" to exclude CDM or explain why the comparison is not directly applicable.
2. **Add an α ablation sweep** (e.g., 0.0, 0.05, 0.1, 0.15, 0.2, 0.3) to demonstrate robustness of the block-noise weighting.
3. **Fix the inconsistency between text and Algorithm 1.** Either update the algorithm to use Tilde{ε} (weighted block + isotropic noise) in the stochastic updates, or explain in the text why isotropic noise suffices during sampling despite the motivation for block noise.
4. **Correct or clarify the NFE allocation notation** in the Figure 7 caption.
