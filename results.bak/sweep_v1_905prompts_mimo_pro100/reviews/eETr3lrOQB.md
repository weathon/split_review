Now I have enough information to write the final review. Let me synthesize everything.

## Summary

This paper proposes VQ-Transplant, a two-stage framework (VQ module substitution + lightweight decoder adaptation) for replacing VQ modules in frozen pre-trained visual tokenizers without end-to-end retraining, and MMD-VQ, a nonparametric distribution-alignment VQ method designed for compatibility with that framework. The primary contribution is the framework itself, which enables cheap exploration of novel VQ methods; the secondary contribution is MMD-VQ, which uses maximum mean discrepancy to align feature and codebook distributions.

## Strengths

- **Impressive efficiency gains with strong reconstruction quality**: Table 6 directly compares VQ-Transplant against from-scratch MMD VAR training at comparable compute budgets: VQ-Transplant achieves 0.81 r-FID in 22 hours on 2×A100, while from-scratch training achieves only 1.26 r-FID in 35 hours. This is a compelling head-to-head comparison that validates the core thesis.

- **Clean, well-motivated two-stage framework**: The insight that a frozen decoder expects features from a particular quantization space and needs lightweight adaptation is intuitive and well-supported. Table 3 (Substitution vs. Adaptation phases) clearly demonstrates that decoder-quantization mismatch is real and that decoder adaptation resolves it — e.g., MMD VAR at K=4096 goes from 1.52 r-FID after substitution to 0.91 after just 5 epochs of adaptation.

- **Cross-dataset generalization beyond the tokenizer's training domain**: Tables 8–10 show strong results on FFHQ (1.21 r-FID), CelebA-HQ (2.60 r-FID), and LSUN-Churches (1.79 r-FID), despite the original VAR tokenizer being trained on OpenImages. The FFHQ result notably outperforms all baselines including VQGAN-LC.

- **Fair, controlled evaluation across multiple VQ methods**: Five VQ algorithms (Vanilla, EMA, Online, Wasserstein, MMD) are evaluated under identical conditions with the same host tokenizer, in both multi-scale and fixed-scale configurations, with consistent patterns across settings. This design credibly demonstrates that the framework generalizes across VQ algorithms.

## Weaknesses

### Fatal

None.

### Major

- **Generality claim outpaces the evidence**: The paper claims to enable "plug-and-play replacement of arbitrary VQ modules within pre-trained visual tokenizers," but all main-text experiments use only the VAR tokenizer. The one attempt on a different tokenizer (LDM-16, Section 5.1) yields worse performance, with the authors acknowledging "its adaptability is lower compared to VAR-based models" (line 274). This is a meaningful gap between the framing and the demonstrated capability. The paper would be more accurate as "efficient VQ integration for VAR-like multi-scale tokenizers," and the LDM-16 results deserve honest discussion in the main text rather than an appendix mention.

- **No downstream generation evaluation**: Visual tokenizers exist to serve generative models, but the paper evaluates only reconstruction quality. Distributional shifts in the quantization space could degrade autoregressive generation even if reconstruction improves — this is an empirical question, not a given. The paper's claim that VQ-Transplant "democratizes quantization research" presupposes that improved r-FID translates to improved generation. A single generation experiment (e.g., autoregressive sampling using an adapted tokenizer) would close this loop.

### Minor

- **MMD-VQ's empirical advantage over Wasserstein VQ is marginal**: In Table 7 (fixed-scale), after decoder adaptation the differences are small — e.g., r-FID of 0.86 vs. 0.92 at K=65536, 0.97 vs. 0.98 at K=32768, 1.05 vs. 1.04 at K=16384. The paper claims MMD-VQ has advantages because it "makes no parametric assumptions," but the multi-Gaussian kernel still introduces bandwidth hyperparameters (σ_i), and the empirical gains are inconsistent (Wasserstein VQ actually edges out MMD-VQ at K=16384). The contribution does not sink the paper but does not meaningfully strengthen it either.

- **Table 1 speedup comparison uses different datasets and hardware**: The 21.8× speedup compares VQ-Transplant on ImageNet-1k (2×A100, 22 hours) against VAR trained on OpenImages (16×A100, 60 hours). The paper does acknowledge this indirectly by providing Table 6 as the fairer comparison, but the abstract still leads with the 21.8× claim without the caveats.

- **No error bars or variance estimates**: VQ training can be sensitive to initialization, and no results include variance over multiple seeds. Even 2–3 runs for key results (e.g., Table 3) would strengthen confidence in the reported improvements.

- **Parallel quantization for fixed-scale methods receives minimal explanation**: The choice to partition 32-dimensional feature vectors into two 16-dimensional sub-vectors for independent quantization is a nontrivial engineering decision that could affect results, but it receives only a single sentence (line 215).

### Trivial

None.

## Nice-to-Haves

- Report total computation in GPU-hours (including frozen encoder forward passes in Stage I and discriminator training in Stage II) for a more complete efficiency picture.
- Discuss failure cases: under what conditions does VQ-Transplant break down? What if the new VQ space is radically different from the original?
- Discuss the relationship between the pre-training domain (OpenImages) and the adaptation domain (ImageNet-1k is a subset of OpenImages) — does this limit applicability when the target domain differs substantially?

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Typos/formatting issues"** — These are parser artifacts, not author errors.
- **"MMD-VQ's 'no parametric assumptions' claim is overstated due to bandwidth hyperparameters"** — While technically valid, this is a minor nitpick; the paper does use a multi-Gaussian kernel, but the claim of nonparametric distribution matching via characteristic kernels is standard and correct in the MMD literature.
- **"Missing appendix discussions"** — The appendix is stripped by the parser; content exists in the original submission.

## Novel Insights

The paper's most valuable observation is the demonstration (via Table 3 and Table 6) that decoder-quantization mismatch is a first-class problem — simply substituting a better VQ module can worsen reconstruction despite lowering quantization error — and that this mismatch is efficiently resolved by lightweight decoder adaptation. This insight has practical implications beyond the specific framework: it suggests that the decoder in modern tokenizers is tightly coupled to the quantization space in ways that are not fully appreciated, and that this coupling can be cheaply addressed. The Table 6 comparison — showing transplant beats from-scratch training at equal compute — is a strong empirical contribution that validates the broader premise of modular tokenizer design.

## Suggestions

1. Bring the LDM-16 results (currently in Appendix D) into the main text with honest discussion of limitations. This would significantly strengthen the generality claim.
2. Add a single downstream generation experiment using an adapted VQ module to validate that reconstruction improvements propagate to generation quality.
3. Scope the claims more carefully: the abstract's "reducing the training cost by 95%" and "21.8× faster" claims should reference Table 6 (fair comparison) rather than Table 1 (cross-dataset comparison).

## Score and Decision

**Calibration anchors retrieved across all rounds:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Dual-token LLM VQ-VAE paper (IqGVIU4rvM) | 2.50 | 1 | Clearly below our paper — weaker method, weaker evaluation |
| QCR: Quantised Codebooks for Retrieval (TDzAqTqDHV) | 3.00 | 1 | Clearly below — different domain, weaker contribution |
| DM-Codec (UFwefiypla) | 3.00 | 1 | Clearly below — less impactful contribution |
| Efficient Vision-Language Models Victor (tNxr38vfYR) | 5.00 | 1 | Below our paper — more incremental, weaker evaluation |
| RAQ-VAE (iqqpx8hgSQ) | 5.50 | 2 | Below our paper — weaker experiments, less clear novelty |
| BSQ-ViT: Binary Spherical Quantization (yGnsH3gQ6U) | 5.75 | 1 | Comparable — good method paper with evaluation gaps |
| Progressive Parameter Efficient Transfer Learning (YNbLUGDAX5) | 6.00 | 2 | Similar level — solid contribution with clear strengths and evaluation limitations |
| From Pixels to Tokens BPE (3TnLGGHhNx) | 6.00 | 1 | Comparable — novel method with good experiments |
| Qinco2 (2zMHHZ569S) | 6.40 | 2 | Slightly above — broader applicability, cleaner novelty |
| Unified Language-Vision Pretraining (FlvtjAB0gl) | 6.25 | 1 | Slightly above our paper |
| Project and Probe (f6CBQYxXvr) | 7.00 | 2 | Above our paper — cleaner novelty, broader scope |
| Towards Seamless Adaptation for VPR (TVg6hlfsKa) | 7.25 | 2 | Above our paper |
| Restructuring VQ with Rotation Trick (GMwRl2e9Y1) | 8.00 | 1 | Clearly above — more fundamental contribution with 11 training paradigms |
| Vision Transformers Need Registers (2dnO3LLiJ1) | 8.00 | 1 | Clearly above — broader impact |

**Round-1 bracket**: Between 5.0 and 7.0. The paper is clearly above the rejected/weak papers (2.5–5.0) and clearly below the strong accepts (8.0+). The core framework is well-executed and the Table 6 comparison is genuinely impressive.

**Round-2 narrowing**: The paper sits around 6.0, comparable to ProPETL (6.0) which has a similarly clean contribution with evaluation limitations, and slightly below Qinco2 (6.4) which has broader applicability. The paper's strengths (Table 6 comparison, cross-dataset generalization, clean framework) are real and concrete, but the overclaimed generality (only VAR tested in main text) and missing generation evaluation are meaningful limitations that keep it from the 6.5–7.0 range. The MMD-VQ secondary contribution being marginal further prevents a higher score.

**Final score: 6.0**. A solid, practical contribution with genuinely impressive efficiency gains, but scoped somewhat narrower than its claims suggest.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>