Now I have all the evidence needed. Let me synthesize the review.

---

## Summary

INFO<sub>TOK</sub> proposes an adaptive video tokenizer that dynamically allocates tokens based on a video's information complexity. It adds two components on top of a fixed-length tokenizer (Cosmos-DV): (1) an ELBO-based router that selects the token budget per video proportionally to reconstruction difficulty, and (2) a transformer-based adaptive compressor that masks out low-information tokens and redistributes their content into the surviving positions. Experiments on TokenBench and DAVIS show it saves ~20% tokens compared to Cosmos-DV at matched quality, outperforms the prior adaptive method ElasticTok by 2.3× compression at better reconstruction metrics, and requires only 1 extra decoder pass vs ElasticTok's 11 binary-search passes. Controlled ablations on a shared Cosmos backbone confirm the gains come from the ELBO router and likelihood-based compressor.

## Strengths
- **Clear practical gains over the prior adaptive method**: On a controlled Cosmos backbone (Table 3, right), INFO<sub>TOK</sub>'s ELBO router + likelihood compressor achieves PSNR 29.30 / FVD 71 vs ElasticTok's uniform router + right-to-left masking at PSNR 27.35 / FVD 152 at the same average BPP<sub>16</sub> of 0.56 — a substantial and well-controlled improvement that isolates the contribution of the proposed adaptive mechanism.
- **Efficient inference**: The ELBO router needs one additional decoder forward pass to determine token length, vs 11× additional NFEs for ElasticTok's binary search (Figure 4g). This is a genuine practical advantage for deployment.
- **Router validated against oracle search**: Table 2 shows the ELBO router achieves reconstruction quality nearly identical to an exhaustive optimal-search baseline (e.g., PSNR 29.86 vs 29.92 at BPP<sub>16</sub> 0.81 on TokenBench), confirming that the router's length selection is near-optimal without brute-force overhead.
- **Compressor design validated by ablation**: Likelihood-based masking outperforms right-to-left masking (PSNR 29.30 vs 27.43) and jump masking (28.07) at matched compression (Table 3, left), showing per-token information selection matters.
- **Framework generalizes across architectures**: The INFO<sub>TOK</sub> adaptive mechanism applied to both Cosmos (CNN-based) and a ViT backbone consistently beats the ElasticTok mechanism (Table 3, right), demonstrating the approach is not tied to one tokenizer design.
- **Well-motivated problem**: Variable information density across videos is a real bottleneck for long-video processing, and adaptive tokenization is a natural solution that the paper frames clearly.

## Weaknesses

### Fatal
None.

### Major
- **Overclaimed theoretical optimality**: The paper repeatedly frames its method as achieving "near-optimal compression rate in theory" (Introduction, line 43), "approaches theoretical optimality" (Abstract, line 19), and "near-optimal token allocation" (Section 3.1, line 151). The theoretical foundation is Shannon's source coding theorem (Theorem 2.1), which explicitly assumes *lossless* reconstruction ("can fully reconstruct video data," line 71). The actual tokenizer is lossy — it operates at a chosen average compression rate β trading length against reconstruction quality, not at perfect reconstruction. Theorem 3.1 bounds *expected token length* but does not characterize reconstruction quality, so it is not a rate-distortion result. The paper acknowledges the gap implicitly ("ELBO values are believed to be close enough to the log-likelihoods," line 165) but provides no empirical or theoretical justification. This misalignment between the theoretical framing and the actual problem weakens the paper's theoretical contribution claims. The empirical results stand on their own, but the "near-optimal" language should be downgraded to "well-motivated heuristic."

- **Undocumented per-token ELBO computation**: The adaptive compressor selects tokens to mask by "their corresponding per-token log-likelihood, which is also approximated via the ELBO values" (line 173). However, the router computes an *aggregate* ELBO for the entire video (Section 3.1). The method for decomposing this aggregate value into per-token contributions is never specified. Since the ELBO-based masking is the core mechanism of the compressor — and Table 3 (left) shows it substantially outperforms alternative masking strategies — this is a significant reproducibility gap. The paper must specify how per-token ELBO is computed (e.g., whether it attributes reconstruction error to each token's receptive field, or uses some other decomposition) and ideally validate the decomposition's quality.

### Minor
- **Uncontrolled comparison in the main results table**: Table 1 compares INFO<sub>TOK</sub> (built on Cosmos-DV) against the original ElasticTok (built on a different, likely weaker backbone). The controlled comparison on a shared Cosmos backbone exists in Table 3 (right) and still shows clear wins, but it is buried in the ablation section. The headline Table 1 overstates the gain attributable to the adaptive mechanism alone. The paper would be stronger if the controlled comparison were promoted to the main results and the cross-backbone comparison clearly labeled as such.

- **Limited evaluation scope**: The paper evaluates only video reconstruction quality (PSNR, SSIM, LPIPS, FVD) and does not test downstream tasks such as video generation or action recognition. The authors acknowledge this limitation (Section 6) and note the computational cost, but it means the practical value of the adaptive tokens for their stated motivation (enabling long-video processing in multi-modal models) remains unvalidated.

### Trivial
- The paper states "storing the mask adds about 5% token overhead" but does not describe the encoding scheme for the binary mask. Clarifying whether this is losslessly compressed or padded to a fixed bitrate would strengthen the compression-rate calculations.

## Nice-to-Haves
- The motivation in Section 2.2 could be strengthened by directly noting that different videos demand different amounts of information, without invoking the lossless entropy baseline H_C(D) which the method does not actually meet.
- The claim in Section 3.1 that "ELBO values are believed to be close enough to the log-likelihoods" would benefit from a brief empirical verification (e.g., a scatter plot of ELBO vs. some proxy for video complexity).
- Adding error bars or discussing cross-video variance in reconstruction metrics, especially for the adaptive algorithms where per-video token length varies, would help assess reliability at low compression rates.

## Removed Points
*These points are flagged to be removed — treat them with caution.*

- **Harsh Critic Point about missing training details**: The paper states "please refer to Appendix C" for training details. The parser stripped the appendix. The main paper does mention the key architecture (8-layer transformer, block-causal attention, Cosmos-DV backbone, FSQ quantization, β ranges). Removed as the appendix likely contains the full details and the main text has sufficient architectural description.
- **Harsh Critic Point about variance/confidence intervals**: This is a generic request not standard in video tokenization benchmarking. Removed (moved to Nice-to-Haves).
- **Strength Finder "Rigorous theoretical justification"**: The theory is not rigorous for the lossy setting. Kept the empirical strengths but dropped the theoretical strength claim as stated.
- **Strength Finder "proves that existing...methods are suboptimal"**: The proof is specific to uniform routers under a loss-minimization condition. This is a valid but narrow result. The strength is retained in modified form above.

## Novel Insights
The paper's most interesting finding is that a simple ELBO-based router — requiring just one extra decoder pass — can match the performance of an exhaustive optimal search over token lengths (Table 2). This suggests that reconstruction error (ELBO) is a surprisingly effective proxy for per-video complexity in the video tokenization setting, and that the information-theoretic intuition of allocating more tokens to higher-entropy content translates cleanly to practice. The result that the adaptive mechanism generalizes across CNN (Cosmos) and ViT backbones (Table 3, right) further suggests the principle is architecture-agnostic, which could inform future tokenizer design beyond video.

## Suggestions
- Reframe the theory as motivation rather than a guarantee. Either develop a proper rate-distortion analysis or explicitly state that the ELBO-based router is a well-motivated heuristic inspired by source coding, with the empirical results standing as the primary evidence.
- Fully document the per-token ELBO decomposition with a precise description and ideally a validation (e.g., correlation with oracle per-token importance).
- Promote the controlled Cosmos-backbone comparison (Table 3, right) to the main results table or at minimum add a clear note in Table 1 about the backbone difference with ElasticTok.

---

**Calibration report:**

*Round 1 (bracketing):* Retrieved anchors across three bands. Weak band (<3.5): IqGVIU4rvM (2.50, combining VQ-VAE + diffusion tokenizers, rejected), lvgsPjRtLM (2.50, VideoDiT, rejected), UFwefiypla (3.00, DM-Codec speech, rejected), vlOfFI9vWO (3.00, MARL for ViT, rejected) — all clearly weaker than INFOTOK. Middle band (3.5–7.5): tFV5GrWOGm (6.00, ElasticTok — the direct prior work), mb2ryuZ3wz (5.75, "How many tokens is an image worth?"), yGnsH3gQ6U (5.75, BSQ-ViT), FlvtjAB0gl (6.25, dynamic discrete visual tokenization). Strong band (>7.5): CxXGvKRDnL (8.00, progressive compression diffusion), 9Cu8MRmhq2 (8.00, multi-granularity correspondence), 2dnO3LLiJ1 (8.00, ViT registers), tyEyYT267x (8.00, interpolating AR/diffusion LMs). **Round-1 bracket: [6.0, 7.5]** — INFOTOK clearly exceeds ElasticTok (6.00) but the strong-band papers at 8.00 are in a different tier.

*Round 2 (narrowing):* Retrieved within (5.5, 7.0) and (6.5, 8.0). Key anchors: tFV5GrWOGm (6.00, ElasticTok, confirmed as direct prior), yGnsH3gQ6U (5.75, BSQ-ViT), mb2ryuZ3wz (5.75, variable-length image tokens), VkWbxFrCC8 (6.67, RECOMBINER), Wr3UuEx72f (7.50, LARP — holistic video tokenization + AR prior, SOTA FVD), WNLAkjUm19 (7.00, theory of discrete tokenization in MIM), lKK50q2MtV (7.00, TokenFlow), bW9fGYo44s (7.33, MotionAura).

INFOTOK is clearly stronger than ElasticTok (6.00): it improves on every dimension (router design, compressor, inference efficiency, reconstruction quality) and provides controlled ablations. It is weaker than LARP (7.50): LARP includes video generation experiments, has a more novel architecture (holistic queries + AR prior), and its theoretical claims are more grounded. INFOTOK is slightly below WNLAkjUm19 (7.00): that paper provides more rigorous theory for its setting. This places INFOTOK at **6.5**, a clear step above the prior adaptive method but not reaching the 7.0+ tier of papers with stronger theory or downstream validation.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>