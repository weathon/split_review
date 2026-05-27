Initial bracket: The paper improves on ElasticTok (avg 6.00) in theoretical grounding, empirical performance, and inference efficiency. It's likely in the 6-8 range. Let me narrow.Now I have enough calibration. Let me finalize the review.

**Calibration summary:**
- Round 1 bracket: Comparable to ElasticTok (6.00) which it directly improves upon, with better theory and empirics; below LARP (7.50) which has strong generation results. Bracket: 6.0–7.5.
- Round 2: InfoTok is clearly stronger than ElasticTok (improves both theory + empirics, 11× fewer NFEs, optimal-search ablation showing near-optimality, ablations across architectures). It is below LARP because LARP demonstrates strong downstream generation while InfoTok is reconstruction-only. It is stronger than BSQ-ViT (5.75) and ALIT (5.75). Lands around 7.0.

## Summary
InfoTok proposes an adaptive discrete video tokenizer that allocates per-video token budget using an ELBO-based router (a surrogate for negative log-likelihood) on top of a fixed-length backbone (Cosmos-DV), paired with a transformer-based adaptive compressor that retains tokens with the highest per-position ELBO. The paper provides an information-theoretic motivation drawn from Shannon's source-coding theorem, proves uniform-router adaptive tokenizers can be arbitrarily suboptimal, and demonstrates consistent reconstruction-quality and inference-efficiency wins over ElasticTok across TokenBench and DAVIS at matched compression rates.

## Strengths
- **Direct empirical win at matched compression vs. ElasticTok (Table 1, Figure 4).** At BPP₁₆=0.81 on TokenBench, InfoTok achieves PSNR 30.08 / LPIPS 0.145 / FVD 49 vs. ElasticTok's 28.26 / 0.244 / 141, with similar margins at BPP₁₆=0.56 and on DAVIS. This is a substantive, not marginal, gain over the principal adaptive baseline.
- **Inference efficiency (Figure 4g).** InfoTok requires 1 additional NFE (one decoder pass to compute the ELBO) versus ElasticTok's 11 NFEs for binary-search-over-threshold; this 11× improvement is a real practical advantage for long videos.
- **Optimal-search ablation (Table 2).** Across three compression rates and two datasets, the ELBO router matches a brute-force per-video search to within ~0.1 PSNR and a few FVD points (e.g., 29.86 vs. 29.92 PSNR at BPP₁₆=0.81). This is the strongest piece of evidence in the paper — much more persuasive than the theorems — that the routing signal is near-optimal.
- **Cross-architecture ablation (Table 3 Right).** Applying the ELBO routing mechanism to an ElasticTok-style ViT backbone still gives PSNR 27.21 → 28.64 and FVD 198 → 114, suggesting the gain comes from the adaptive mechanism, not solely the Cosmos backbone.
- **Compressor design is non-trivial (Table 3 Left).** ELBO-based masking beats R2L (27.43 → 29.30 PSNR) and Jump masking (28.07 → 29.30), confirming the likelihood-based selection rule contributes meaningfully beyond random/structured masking.

## Weaknesses

### Fatal
None.

### Major
- **Theoretical framing oversells what is proven for the lossy/continuous regime.** Theorem 2.1 is Shannon source-coding restated under the idealized assumption that "the tokenizer can perfectly reconstruct any input video x with p(x)>0" (Section 2.2), and reasons over |𝔻| as if it were a finite alphabet — the regime the method actually operates in is lossy on a continuous distribution, so this is intuition, not a guarantee for the operating regime. Theorem 2.2 is an existence claim ("for any κ>1, there exists 𝔻 and large N…"), not a quantitative characterization of how suboptimal uniform routing is on real video distributions. Theorem 3.1's bound also has a unit inconsistency: H_C(𝔻) is defined with log_C while E[-log p(x)] and ELBO are in natural log, so as written the bound is not unit-coherent. The abstract and Section 1 ("rigorously prove…approaches theoretical optimality", "guarantee a near-optimal compression rate in theory") promise more than the statements deliver. The algorithm still works, but the rhetorical scaffolding should be recalibrated.
- **ELBO → router justification is partially abandoned in practice.** Section 3.1's final paragraph admits "using the reconstruction error itself (without the KL term) to derive r_β is sufficient, as the KL term is approximately proportional to the reconstruction error". So the deployed router is effectively "allocate tokens proportional to per-video reconstruction error" — a sensible heuristic, but the chain Shannon → ELBO → algorithm is more rhetorical than load-bearing. The paper should either justify this approximation empirically (e.g., the proportionality claim) or scope back the theoretical claim.
- **Evaluation is reconstruction-only while motivation is downstream usage.** The introduction repeatedly motivates the work by "long video sequences processing", "downstream video-understanding or generation", and "unified multi-modal models", but the evaluation is exclusively PSNR/SSIM/LPIPS/FVD on reconstruction. Section 6 acknowledges this, but the gap is central: variable-length token sequences are harder to consume by downstream autoregressive models than fixed-length grids, so a 20% token saving at fixed reconstruction quality does not automatically translate into matching downstream gains. The contribution would be substantially more decisive with even a small downstream generation or understanding experiment.

### Minor
- **Per-token ELBO decomposition for the compressor is under-specified.** Section 3.2 says the compressor "preserves the top N_x tokens according to their corresponding per-token log-likelihood, which is also approximated via the ELBO values." But ELBO is a video-level quantity, and the paper does not describe how it is decomposed onto individual spatio-temporal positions. Given Table 3 (Left) shows this design is one of the more impactful choices (R2L 27.43 → 29.30 PSNR), the procedure deserves an explicit definition.
- **"Without influence on performance" is slightly aggressive for DAVIS.** The abstract's "saving 20% tokens without influence on performance" holds on TokenBench (PSNR 30.01 vs 30.08, FVD 49 vs 49) but on DAVIS at BPP₁₆=0.81 InfoTok is mildly behind Cosmos-DV (PSNR 25.92 → 25.79, LPIPS 0.208 → 0.223). Acknowledging this regression in-text would be more honest.
- **Section 2.3's simplification of ElasticTok's inference to an "oracle returning the minimal length conditioned on loss being minimized" is a strawman of the actual binary-search procedure.** The theoretical critique therefore lands on a simplified version of the baseline. The empirical comparison in Section 4 is what actually establishes the baseline is worse, and that result is genuine — but the theoretical critique of the baseline should be framed accordingly.
- **All baselines evaluated at 256×256 to accommodate ElasticTok.** The paper discloses this, but Table 1's relative ordering of fixed-length baselines (Cosmos-DV, Open-MAGVIT2, OmniTokenizer) should not be over-interpreted as a fair head-to-head, since these tokenizers are evaluated outside their typical setup. The disclaimer is the right move; just don't over-claim from it.

### Trivial
None worth listing.

## Nice-to-Haves
- Add a small downstream experiment (e.g., AR generation on short clips, or a frozen-features probing task) to test whether adaptive token sequences translate to downstream gains.
- A random-masking baseline in Table 3 (Left), in addition to R2L and Jump, would more directly isolate the value of the likelihood-based selection.
- Characterize what kinds of videos receive more vs. fewer tokens (e.g., breakdown by motion magnitude, scene complexity), going beyond the dog vs. cat-fighting illustration.
- A scatter plot of per-video allocation (ELBO router vs. brute-force optimal) would visually replace the theoretical guarantee with direct evidence.
- Briefly discuss whether the ELBO router transfers to continuous-token adaptive tokenizers (CAT, FlexTok), since the framework is general.
- Tighten the abstract to acknowledge the DAVIS regression.

## Removed Points
These points are flagged to be removed, treat them with caution:

- *"ELBO assumes a learned variational posterior trained against a learned prior, but VQ-style tokenizers use deterministic encoder + quantization."* — The paper addresses this directly in Section 3.1's final paragraph by switching to reconstruction error in practice, and uses the standard VAE-style reading of the reconstruction loss. The harsh critique reduces to a presentation concern about the principled-ness framing, which is already captured in the "theoretical framing oversells" Major weakness; including this separately would double-count.
- *"Reproducibility: implementation details for per-token ELBO."* — Already kept as a Minor, not a reproducibility nitpick.
- *Strength: "addresses an important problem"-style framing* — generic, removed per instructions.

## Novel Insights
None beyond the paper's own contributions. The core observation — that information-theoretically motivated token allocation matches a brute-force per-video optimal search to within 0.1 PSNR on multiple rates and datasets — is itself a useful empirical insight, but it belongs to the paper.

## Suggestions
- Recalibrate the abstract, Section 1, and Section 3.1 so the theorems are framed as informal motivation for content-dependent token allocation rather than as guarantees on near-optimal compression in the deployed regime. Fix the unit inconsistency in Theorem 3.1.
- Promote Table 2 (optimal-search ablation) to a primary result rather than an ablation — it is more persuasive than the theorems.
- Specify the per-token ELBO decomposition used by the compressor (e.g., per-position MSE, per-receptive-field reconstruction loss).
- Add at least one small downstream experiment (autoregressive generation on short clips) or explicitly re-scope the contribution to reconstruction in the abstract and introduction.
- Acknowledge the small DAVIS regression at BPP₁₆=0.81 in the abstract.

## Axis Evaluation
- **Originality:** Moderate-to-high. The specific recipe — ELBO-driven router on top of a strong fixed tokenizer plus a likelihood-thresholded compressor with mask side-information — is a fresh and well-motivated combination, even if individual pieces (ELBO, adaptive tokenization, masking-based compressors) are not new.
- **Importance:** High. Adaptive video tokenization is a real bottleneck for long-video and multi-modal modeling, and the principal prior method (ElasticTok) has known inefficiencies the paper directly addresses.
- **Claim support:** Mixed. Empirical claims are well-supported; theoretical claims are partially supported and overstated relative to what the theorems prove for the lossy regime.
- **Soundness of experiments:** Solid. Ablations isolate the router, the compressor design, and the architecture; the optimal-search comparison is particularly strong.
- **Clarity:** Mostly good; per-token ELBO and the precise router computation are under-specified.
- **Value to the community:** Substantial. The optimal-search alignment result and the 11× NFE improvement are genuinely useful empirical findings, and the framework is general enough to inspire follow-ups in other modalities.

## Score and Decision

**Anchor papers retrieved:**

Round 1:
- `IqGVIU4rvM.md` (avg 2.50, R1) — VQ-VAE + diffusion image tokenizer, rejected; clearly weaker than this paper.
- `DsMxVELk3K.md` (avg 3.00, R1) — text compression, off-topic and weaker.
- `lvgsPjRtLM.md` (avg 2.50, R1) — VideoDiT, rejected; off-topic.
- `6j0GH40mFt.md` (avg 3.40, R1) — image compression with dynamic attention; weaker.
- `tFV5GrWOGm.md` (avg 6.00, R1) — **ElasticTok**, the direct baseline this paper improves upon in theory, empirics, and inference cost.
- `yGnsH3gQ6U.md` (avg 5.75, R1) — BSQ-ViT, similar reconstruction-quality framing but non-adaptive; this paper sits above it because it adds principled adaptivity and shows clear wins over its adaptive predecessor.
- `mb2ryuZ3wz.md` (avg 5.75, R1) — ALIT, adaptive image tokenizer; weaker empirical setup (ImageNet-100, mixed results), this paper is clearly stronger.
- `CxXGvKRDnL.md` (avg 8.00, R1) — Progressive compression with diffusion + ELBO; stronger theoretical novelty, this paper is below.
- `9Cu8MRmhq2.md` (avg 8.00, R1) — Long-term noisy video correspondence; off-topic, above.
- `j7b4mm7Ec9.md` (avg 7.60, R1) — Watermarking; off-topic.
- `tyEyYT267x.md` (avg 8.00, R1) — Diffusion language models; off-topic, above.

Round 2:
- `8ROIRnKloJ.md` (avg 5.67, R2) — ε-VAE, denoising as decoding; rejected with mixed scores; this paper is stronger.
- `Wr3UuEx72f.md` (avg 7.50, R2) — **LARP**, video tokenizer with strong AR-generation results; this paper is below because LARP demonstrates downstream wins while InfoTok is reconstruction-only.
- `bW9fGYo44s.md` (avg 7.33, R2) — MotionAura with 3D-MBQ-VAE; comparable level, similar scope but with downstream generation.
- `44cMlQSreK.md` (avg 7.20, R2) — NeuroQuant for variable-rate video coding; comparable theoretical-framing-plus-empirics paper.
- `lKK50q2MtV.md` (avg 7.00, R2) — TokenFlow video editing; off-topic, comparable score.
- `NGB6YNnO5o.md` (avg 6.25, R2) — Info-theoretic VAE/diffusion generalization analysis; this paper has stronger empirics, comparable theoretical clarity.
- `Cy5v64DqEF.md` (avg 7.50, R2) — Idempotence in perceptual compression; stronger theoretical contribution.
- `aXwukBD6M6.md` (avg 6.50, R2) — Information-theoretic compressed descriptions for image generation; similar tier.

**Positioning:** Clearly above ElasticTok (6.00) because it improves the same problem on theory, on empirical reconstruction quality at matched rates, and on inference efficiency. Clearly above BSQ-ViT/ALIT (5.75). Comparable to NeuroQuant (7.20) and somewhat below LARP (7.50) and MotionAura (7.33), which also demonstrate downstream wins. The reconstruction-only scope and the overstated theory keep it from matching LARP, while the strong empirical package and the near-optimal-router ablation push it well above the 6.0–6.25 cluster.

Final position: 7.0.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>