Now I have sufficient information to produce the final consolidated review. Let me compile everything.

## Summary

The paper proposes VQ-Transplant, a framework that enables plug-and-play replacement of VQ modules in frozen pretrained visual tokenizers (specifically VAR) without requiring costly end-to-end retraining. A lightweight decoder adaptation stage (5 epochs on ImageNet-1k) resolves the mismatch between the new quantized latent space and the frozen decoder. The paper also introduces MMD-VQ, a maximum-mean-discrepancy-based quantization method. Empirical results show 21.8× training speedup over vanilla VAR while achieving better reconstruction fidelity (0.81 vs. 0.92 r-FID on ImageNet-1k).

## Strengths

- **Practical framework with significant efficiency gains**: VQ-Transplant achieves a 21.8× speedup (44 vs. 960 GPU-hours) over fully training VAR (Table 1) while yielding competitive or better reconstruction. This is a concrete, verifiable efficiency improvement that directly supports the paper's core claim.

- **Plug-and-play compatibility demonstrated across 5 VQ methods**: The framework is validated with Vanilla VQ, EMA VQ, Online VQ, Wasserstein VQ, and MMD VQ, in both multi-scale (Table 3) and fixed-scale (Table 7) settings. This breadth of validation supports the generality of the framework.

- **Clear two-stage experimental decomposition**: The paper carefully separates "substitution stage" (VQ-only training) from "adaptation stage" (decoder fine-tuning), and the results in Tables 3 and 7 show that lower quantization error does not directly translate to better r-FID until the decoder is adapted. This cleanly confirms the distribution-mismatch diagnosis that motivates the framework.

- **Decoder adaptation shows consistent improvement across training length**: Table 5 and Figure 3 show monotonic r-FID improvement from 5 to 20 epochs (0.81→0.74 at K=8192), demonstrating that the lightweight adaptation can convert reduced quantization error into better reconstructions and that more epochs continue to help.

## Weaknesses

### Major

1. **Missing control experiment confounds the headline comparison**. The original VAR tokenizer was trained on OpenImages (~9M images) and evaluated on ImageNet-1k. VQ-Transplant replaces the VQ module *and* adapts the decoder on ImageNet-1k for 5 epochs. The paper never reports what happens when the *original* VQ module is kept and the decoder is fine-tuned on ImageNet-1k for the same 5 epochs. This is needed to separate the effect of the VQ replacement from the effect of dataset-specific decoder tuning. If this baseline also yields r-FID ~0.84, the marginal benefit of the transplanted VQ is small and the headline outperformance over VAR is partially an artifact of domain adaptation. This is not an ablation request—it is the control required to interpret the paper's central quantitative claim.

2. **Token-count mismatch in fixed-scale baseline comparisons undermines SOTA claims**. In Table 2, the proposed MMD VQ (fixed-scale) uses 512 tokens, while nearly all baselines (DQVAE, DiVAE, VQGAN, VQGAN-EMA, VQGAN-LC, Llama GEN) use 256 tokens. Token count directly affects reconstruction fidelity—more tokens almost always improve r-FID and PSNR. The paper does present RQVAE at 512 and 1024 tokens (r-FID 2.69 and 1.83), showing that token count matters, but does not provide matched-token baselines for the other methods. The only fair comparison is between MMD VAR (680 tokens) and VAR (680 tokens), which is valid. The fixed-scale SOTA claims in Table 2 against 256-token baselines are not supported.

3. **Cross-dataset "state-of-the-art" claims are based on uncontrolled comparisons**. Tables 8–10 compare Wasserstein/MMD VQ (512 tokens) against baselines from prior work that use different architectures, different token counts (256 vs. 512), and potentially different evaluation protocols. For example, on FFHQ (Table 8), the best prior result is VQGAN-LC (256 tokens, r-FID 3.81), compared to Wasserstein VQ (512 tokens, r-FID 1.21). The token-count difference alone could account for most of this gap. Without controlling for token count (e.g., by re-running baselines at 512 tokens or re-running the proposed method at 256 tokens), these SOTA claims are unsubstantiated. The paper should either add controlled comparisons or temper the language.

### Minor

4. **MMD-VQ advantage over Wasserstein VQ is marginal and not statistically substantiated**. The differences between MMD-VQ and Wasserstein VQ across all tables are typically 0.01–0.06 r-FID, and at some settings Wasserstein VQ slightly edges ahead (e.g., Table 7 adaptation, K=16384: Wasserstein 1.04 vs. MMD 1.05). No variance or statistical significance is reported. The theoretical motivation for MMD over Wasserstein (nonparametric, handles non-Gaussian features) is plausible, but the empirical evidence does not convincingly demonstrate a practical advantage. Since MMD-VQ is presented as a secondary contribution, this does not threaten the primary contribution but weakens the paper's overall impact.

5. **Training cost comparison conflates dataset differences**. Table 1 reports a 21.8× speedup (VAR: 16×A100×60h on OpenImages; VQ-Transplant: 2×A100×22h on ImageNet-1k). Since OpenImages (~9M images) is ~7.5× larger than ImageNet-1k (~1.2M), part of the speedup comes from training on a smaller dataset, not just from the decoupled framework. A fairer comparison would be against fine-tuning the full VAR model (including encoder) on ImageNet-1k for the same compute budget. The paper does compare against from-scratch training (Table 6), but that comparison (5-7 epochs of from-scratch training) is expected to be poor and is not the most informative baseline.

6. **The claim "state-of-the-art reconstruction fidelity" is overstated**. The paper achieves r-FID 0.81 (MMD VAR, K=8192) on ImageNet-1k reconstruction. While this beats VAR (0.92), more recent tokenizers exist (e.g., BSQ-ViT, SEED, ImageFolder) that operate at different settings/resolutions, and the paper does not engage with these. The qualifier "near state-of-the-art" in the abstract is more appropriate.

### Trivial

- The fixed-scale VQ uses sub-vector quantization (32-d → two 16-d sub-vectors), effectively doubling the quantizer capacity per spatial location. This should be stated upfront in the fixed-scale results rather than buried in the experiment setup paragraph.
- No error bars or variance reported for any metric. For claims of marginal improvements this is noticeable, though single-run evaluation is standard in this literature.

## Nice-to-Haves

- A synthetic experiment where features are non-Gaussian (mixture of Gaussians, heavy-tailed) to demonstrate when MMD-VQ's nonparametric advantage over Wasserstein VQ manifests empirically would strengthen the secondary contribution.
- The LDM-16 compatibility results (Table 16, appendix) are briefly mentioned as showing weaker performance; a short discussion in the main paper of when VQ-Transplant's generality is limited would improve credibility.

## Removed Points

These points were removed from the harsh critic's review for the following reasons:

- The criticism about whether the discriminator is frozen or re-initialized during adaptation (noted as adding computational cost): This is a detail the authors could clarify but is not a substantive weakness. The discriminator training cost is marginal relative to the total adaptation cost, and the paper's cost comparison (Table 1) is for the full pipeline.

- The claim that the "95% training cost reduction" is not a strict savings claim because datasets differ: This is reframed above as Weakness #5 (Minor). The claim is still meaningful—training on 44 GPU-hours is dramatically cheaper than 960 GPU-hours regardless of dataset.

- The criticism that "from-scratch training" comparison in Table 6 is "not particularly informative": This comparison is actually informative—it shows that VQ-Transplant dominates from-scratch training even when from-scratch training uses more GPU-hours, which is a useful data point.

- The critique about multi-Gaussian kernel bandwidth selection not being discussed: This is a reasonable implementation question but not a weakness of the paper's contributions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Run the missing control**: Keep the original VAR VQ module and fine-tune only the decoder on ImageNet-1k for 5 epochs. Report r-FID and compare to the VQ-Transplant results. This is the single most important experiment to validate the paper's central claim.

2. **Provide token-matched baselines**: For Table 2, either re-run the leading baselines at 512 tokens, or re-run MMD VQ at 256 tokens, to enable a fair comparison.

3. **Add controlled cross-dataset evaluation**: Either re-implement a leading baseline (e.g., VQGAN-LC) at 512 tokens for FFHQ/CelebA-HQ/LSUN-Churches, or present the results as "using the VQ-Transplant framework, our method achieves r-FID of X on dataset Y" without claiming SOTA over uncontrolled prior results.

4. **Calibrate the MMD-VQ claims**: Present it as an effective variant competitive with Wasserstein VQ rather than claiming "superior reconstruction fidelity," since the empirical differences are small and inconsistent.

5. **Break down training time**: In Table 1, report Stage I (VQ substitution) and Stage II (decoder adaptation) compute costs separately.

## Score and Decision

**Calibration Anchors** (all retrieved papers, path and comparison):

Round 1 — Bracketing:
- **IqGVIU4rvM** (2.50): VQ-VAE+Diffusion tokenizer combination paper. Much weaker; unclear method. VQ-Transplant is substantially stronger.
- **TDzAqTqDHV** (3.00): Quantized codebooks for retrieval. Different domain. VQ-Transplant is stronger.
- **5ncdKonxd4** (3.00): LVLM visual redundancy reduction. Different domain. VQ-Transplant is stronger.
- **bEvI30Hb2W** (3.00): Video reasoning. Different domain. VQ-Transplant is stronger.
- **yGnsH3gQ6U** (5.75, accept): BSQ-ViT — binary spherical quantization for tokenization. Similar evaluation fairness concerns, accepted. Comparable quality, VQ-Transplant slightly weaker due to missing control.
- **FlvtjAB0gl** (6.25, accept): Unified language-vision pretraining with visual tokenization. Stronger overall contribution. VQ-Transplant is weaker.
- **n64NYyc6rQ** (6.20, accept): Semantic-equivalent vision tokenizer. Stronger. VQ-Transplant is weaker.
- **YlWvQSBCgl** (4.00, reject): Channel-wise quantization for image generation. Had fundamental design concerns. VQ-Transplant is stronger.
- **GMwRl2e9Y1** (8.00, accept): VQ restructuring with rotation trick. Much stronger. VQ-Transplant is substantially weaker.
- **CxXGvKRDnL** (8.00, accept): Progressive compression with diffusion. Different domain, much stronger. VQ-Transplant is weaker.
- **wg1PCg3CUP** (8.00, accept): Scaling laws for precision. Different domain. VQ-Transplant not comparable.
- **eW4yh6HKz4** (7.60, accept): Cross-block quantization for LLMs. Different domain, much stronger. VQ-Transplant is weaker.

Round 2 — Narrowing:
- **sfTsvy05MX** (4.75, reject): LL-VQ-VAE — lattice VQ. Weaker evaluation. VQ-Transplant is clearly stronger.
- **CP6CAqxAGJ** (5.67, reject): UnifyVocab - vocabulary alignment in LLMs. Different domain but similar evaluation profile (missing control, SOTA claims overconfident). VQ-Transplant is comparable or slightly stronger.
- **mb2ryuZ3wz** (5.75, accept): Variable-length token representations (How many tokens). Thorough empirical analysis but some comparison issues. VQ-Transplant is comparable.

**Round 1 bracket**: Between scores 4.0 and 6.25.

**Round 2 narrowing**: The paper sits between LL-VQ-VAE (4.75) and BSQ/HowManyTokens (5.75). It has a practically useful contribution with real efficiency gains, but the evaluation issues (missing control, token-count mismatch, uncontrolled cross-dataset comparisons) prevent full confidence in the SOTA claims. The MMD-VQ secondary contribution is not convincingly differentiated from Wasserstein VQ. Comparable to BSQ (5.75) and HowManyTokens (5.75) in ambition and quality, but slightly weaker due to the more consequential evaluation gaps.

**Final score**: 5.0. The core framework idea is solid and the efficiency gains are real, but the evaluation has gaps that need to be addressed before the claims can be accepted at face value. The paper is between a clear reject and a clear accept.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>