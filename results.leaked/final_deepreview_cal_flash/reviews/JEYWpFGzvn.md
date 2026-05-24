Now I have a clear picture from the calibration. Let me synthesize everything and write the final review.

Here's my reasoning for the score:
- **ElasticTok** (avg 6.00): Direct predecessor. InfoTok has stronger theory, better results, 11× better efficiency. Clearly better.
- **BSQ-ViT** (avg 5.75): Quantization method, not directly comparable, but InfoTok has better theoretical grounding.
- **"How many tokens" / ALIT** (avg 5.75): Image-only adaptive tokenization, less theory. InfoTok is stronger.
- **"Role of Discrete Tokenization"** (avg 7.00): Pure theory paper. InfoTok has a mix of theory + systems with some clarity issues.

InfoTok's main weaknesses (underspecified per-token importance, slightly overstated claims) are real but fixable. The core contribution is solid. I place it between ElasticTok (6.00) and the polished theoretical paper (7.00) — at **6.5**.

Let me note: the paper info says it's accepted as an ICLR 2026 Oral. This doesn't affect my calibration, which is based on human-reviewed anchors.

Now let me write the review.

## Summary

The paper introduces InfoTok, a principled adaptive video tokenization framework grounded in information theory. It uses an ELBO-based router to dynamically determine token length per video and a transformer-based adaptive compressor to produce variable-length discrete tokens. The authors prove that existing data-agnostic training methods are suboptimal and that their method achieves near-optimal compression rates.

## Strengths
1. Rigorous information-theoretic proofs (Theorem 2.2 and 3.1) establishing suboptimality of prior methods and near-optimality of the proposed approach.
2. Strong empirical results: InfoTok matches/exceeds Cosmos-DV with 20% fewer tokens and outperforms ElasticTok by a large margin (1-2 dB PSNR, 40-60% FVD reduction).
3. 11× inference efficiency gain over ElasticTok (1 NFE vs 11 NFEs).
4. Comprehensive ablation study (Table 2: oracle comparison, Table 3: component ablations across architectures).

## Weaknesses

### Fatal
None.

### Major
- **Per-token importance estimation is underspecified.** The adaptive compressor preserves the top N_x tokens "according to their corresponding per-token log-likelihood, which is also approximated via the ELBO values" (lines 173-174). However, the ELBO as defined in Eq. (3) is a video-level scalar. The paper never explains how per-token ELBO values are derived from the video-level reconstruction error or whether a different decomposition is used. This is the core mechanism of the compressor; without specifying it, the method is not reproducible from the main text. While the appendix (removed in parsing) may contain these details, a reader should be able to understand the core design from the main body.

### Minor
- **Inconsistency in compression claims.** The abstract claims "saving 20% tokens without influence on performance" (line 19), which is supported (InfoTok at 0.81 BPP: 30.08 PSNR vs Cosmos-DV at 1.00 BPP: 30.01). However, the introduction claims "save approximately 50% tokens without loss of reconstruction quality" (line 49), which corresponds to InfoTok at 0.56 BPP (29.30 PSNR) vs Cosmos-DV (30.01) — a 0.71 dB drop that contradicts "without loss." The 20% claim is accurate; the 50% claim overstates the quality preservation.

- **ElasticTok baseline specification.** The main comparison (Table 1) does not state whether ElasticTok uses the same Cosmos backbone or its original architecture, leaving open the possibility that part of the advantage comes from the base tokenizer. The ablation in Table 3 (Right) partially mitigates this by comparing mechanisms on the same Cosmos backbone, but a clear statement in the main results section is needed.

- **No uncertainty quantification.** Reconstruction metrics are reported as single points without variance or confidence intervals. Several key comparisons (e.g., 30.08 vs 30.01 at 0.81 BPP) involve small differences that could fall within run-to-run variation.

- **Binary mask description is self-contradictory.** The text says "N_x tokens with the lowest ELBO values are 1 and the remaining are 0" (line 174), which conflicts with the stated goal of preserving the "top N_x tokens" by information content. The encoding of the mask (which value means "keep") needs clarification.

### Trivial
- Equation (4) maps a continuous ELBO ratio to integer N_x without specifying the rounding/clipping operation.
- The paper does not explicitly state whether the base encoder/decoder from Cosmos is frozen or fine-tuned during InfoTok training. Algorithm 1 optimizes both φ and θ, implying fine-tuning, but the text says InfoTok is "on top of existing fixed-length tokenizers" (line 115), which could be read as frozen.

## Nice-to-Haves
- Provide empirical evidence for the claim that the KL term in the ELBO is approximately proportional to the reconstruction error and can be omitted without affecting token ordering.
- Report wall-clock inference latency (beyond NFE counts) to fully characterize the practical speedup.
- State whether a fixed crop was used for evaluation to ensure deterministic results.

## Removed Points
- Criticisms about the ElasticTok baseline not being reimplemented on the same backbone (Issue 2 in the harsh critic): The controlled ablation in Table 3 (Right) directly addresses this. The critic's concern is partially valid but significantly mitigated by the paper's own evidence. Retained in weakened form.
- Criticisms about missing training details (optimizer, learning rate, batch size) are standard reproducibility concerns that belong in the appendix (which was stripped by the parser).
- Criticisms about Theorem 2.2 not applying to real video distributions: The theorem is an existential result providing motivation, standard practice in theoretical CS — not a weakness.
- Criticisms demanding downstream task evaluation (video generation): Explicitly scoped out by the paper (line 228). This is not a weakness of the paper as written.
- Generic "could add more datasets/models" type suggestions.

## Novel Insights
The central insight — that token length should be proportional to per-video ELBO as a surrogate for negative log-likelihood, with a theoretical near-optimality guarantee — is genuinely novel and represents a meaningful advance over the heuristic masking strategies used by ElasticTok and related works. The practical observation that this ELBO-based allocation can be computed with a single additional decoder pass (vs. 11 NFEs for ElasticTok's binary search) makes the theoretical contribution directly actionable. The oracle comparison in Table 2, showing the ELBO router performs within 0.1 dB of an exhaustive search, is particularly convincing evidence that the proxy is well-calibrated.

## Suggestions
- Add a clear, step-by-step explanation of how per-token importance scores are extracted. If this involves decomposing the pixel-wise reconstruction error and mapping it back to latent positions, write it explicitly. This is the single most important reproducibility detail.
- Reconcile the 20% and 50% claims: either remove the 50% "without loss" claim or qualify it precisely (e.g., "50% token reduction with minimal quality degradation").
- State the ElasticTok backbone configuration explicitly in the main text.
- Consider adding a brief uncertainty estimate (e.g., standard deviation over 3 seeds or a bootstrap over the test set) for the key comparison points.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>