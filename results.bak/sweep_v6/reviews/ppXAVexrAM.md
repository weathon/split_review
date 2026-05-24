Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper introduces ARSS, the first decoder-only autoregressive transformer for novel view synthesis (NVS) from a single image with camera trajectory conditioning. It employs a video tokenizer (VidTok) for temporally-consistent discrete tokens, a camera autoencoder that compresses Plücker raymaps into 3D positional guidance tokens, and a hybrid token permutation strategy (spatial shuffle, temporal fixed) to adapt the uni-directional causal transformer to bi-directional visual data. Experiments on RealEstate10K, ACID, and zero-shot on DL3DV show competitive results.

## Strengths

- **First application of decoder-only AR to NVS with camera control.** While previous AR visual generation works (LlamaGen, VAR, etc.) target single-image or text-to-image generation and diffusion-based NVS methods dominate, ARSS is the first to formulate multi-view synthesis as next-token prediction in a GPT-style causal transformer with explicit camera conditioning. This is a genuine and well-motivated novel application.

- **Hybrid token permutation ablation cleanly validates the design choice.** Table 2 and Figure 7 compare raster order, full (spatial+temporal) permutation, and the proposed spatial-only permutation. The proposed strategy outperforms both alternatives substantially (PSNR 19.22 vs. 16.29 raster / 18.76 full perm.), directly supporting the claim that maintaining temporal causality while permitting spatial bidirectionality is effective.

- **Error accumulation analysis demonstrates robustness over long trajectories.** Figure 6 tracks per-frame metrics across 17 frames. ARSS maintains consistently higher or near-highest PSNR/SSIM and lowest LPIPS at every timestep, with notably flatter degradation slopes than all baselines. This is a non-trivial result for an autoregressive model and provides the clearest evidence of the method's practical advantage.

- **Video tokenizer ablation shows large gains in temporal consistency.** Table 3 shows that replacing the video tokenizer with a VQ image tokenizer drops FVD from 52.56 to 137.68 (62% worse), confirming that the temporal encoding in the tokenizer is critical — a clean ablation that strengthens the paper.

## Weaknesses

### Major

- **Missing ablation of the camera autoencoder.** The paper advertises three main modules: video tokenizer, camera autoencoder, and autoregressive transformer with hybrid permutation. Only the tokenizer and permutation are ablated. The camera autoencoder is never compared against (a) raw Plücker coordinates fed as features, (b) a simple learned per-frame embedding, or (c) no camera conditioning at all. Without this, it is impossible to assess whether the camera autoencoder design contributes meaningfully, or whether the gains attributed to "3D positional guidance" could be achieved by much simpler alternatives. This is the single most consequential experimental gap.

- **Overclaiming relative to mixed quantitative results.** The introduction states the method "out-performs current state-of-the-art methods" (line 114), but the actual numbers tell a mixed story. On RealEstate10K, ARSS leads on PSNR (19.02 vs. SEVA 18.73, +1.5%) and LPIPS (0.269 vs. 0.349, −22.9%), but trails SEVA on SSIM (0.624 vs. 0.670, −6.9%) and FID (47.60 vs. 46.98, +1.3%). On ACID, the FID gap is large (47.76 vs. SEVA 33.16, −44%). The paper notes that SEVA uses larger-scale training data and higher resolution, but nonetheless, the headline claim of outperforming SOTA is unsupported — "competitive" or "comparable" (as the abstract more carefully states) would be accurate. A controlled comparison matching training conditions is needed to substantiate superiority.

- **Central motivation for AR over diffusion is unvalidated.** The paper argues that AR's "strictly causal structure" enables incremental generation and adaptation to trajectory changes, and that this is less straightforward with diffusion. Yet no experiment demonstrates either advantage: no comparison against an autoregressive video diffusion baseline (e.g., frame-by-frame generation), no test of incrementally extending a trajectory, and no ablation isolating whether the causal structure (as opposed to tokenizer or other design choices) drives the error accumulation benefits in Figure 6. The claimed advantage remains a rationale, not a validated property.

### Minor

- **Camera autoencoder loss contains redundant constraints.** Equation 5 includes terms λ₃(‖d̂‖ − 1)² and λ₄(d̂ · m̂)² to enforce unit direction and orthogonality. However, the input Plücker coordinates already satisfy these properties by construction. A well-trained autoencoder should preserve them without explicit regularization. While not a fatal flaw, this suggests the loss design is not carefully justified and may explain why the camera autoencoder ablation was omitted (the constraints may not matter much).

- **Parallel decoding claim is unquantified.** Section 3.2.3 states that random spatial permutation "allows parallel decoding" and "the system has the capacity to predict multiple tokens at one time," but no wall-clock times, throughput comparisons, or speedups are reported. This is a concrete potential advantage of the AR approach over diffusion methods and should be measured.

- **No failure cases or limitation analysis in qualitative results.** The qualitative figures (3, 4, 5, 7) show only successful outputs. For an autoregressive model that can accumulate errors, showing failure modes (geometric inconsistencies, temporal artifacts) is important for assessing practical utility. The discussion section does mention tokenizer limitations, but no visual evidence is provided.

### Trivial

- Equation 7 is notational unclear — the cross-entropy appears to be missing its second argument (the target sequence), making the training objective ambiguous as written. (If this is a parser artifact from PDF extraction, it should be corrected in the final version.)

## Nice-to-Haves

- A controlled comparison with SEVA under matched training data and resolution would clarify whether ARSS's competitive PSNR/LPIPS reflect architectural merit or just data asymmetry.
- Visualization of what the camera autoencoder's latent tokens encode (e.g., reconstructing Plücker maps from latents) would build confidence in the 3D positional guidance claim.
- Standard deviations or confidence intervals on Table 1 would help assess whether the observed differences are significant given the mixed patterns.

## Removed Points

The following points from the input reviews were removed or demoted per instructions:

- **Criticism about SEVA on DL3DV being "unexplained":** The paper explicitly states "DL3DV was part of its training data" and why it's excluded from zero-shot comparison. This is a reasonable justification, not an omission. *Removed.*
- **Criticism about "Figure 1 caption states 'photorealistic and 3D consistent' as fact":** This is a standard qualitative caption in NVS papers and not a methodological weakness. *Removed.*
- **Complaint about missing related works:** Per hard rules, I cannot confirm or deny missing related works. *Removed.*
- **Request for standard deviations/confidence intervals:** While noted in nice-to-haves, treating this as a core weakness would impose an evaluation standard uncommon for this type of benchmarking. *Demoted to nice-to-have.*
- **Exposure bias analysis request:** A reasonable suggestion but not standardly expected for first applications of AR to NVS. *Demoted to nice-to-have.*
- **Strength Finder's "camera autoencoder for 3D positional guidance" as a strength:** This point is kept as a strength because the design is genuinely novel, even though the missing ablation tempers its impact.

## Novel Insights

The most interesting finding from the reviews is that the error accumulation analysis (Figure 6) — a routine diagnostic for autoregressive models — turns out to be the strongest empirical evidence in the paper. The hybrid permutation strategy's ablation shows clean gains, but without the camera autoencoder ablation, it is unclear whether the camera tokens or the permutation itself drives the quality improvement. This reveals a broader pattern: the paper's contributions are best demonstrated by what they *are* (a novel first application) rather than by the headline quantitative comparisons, which are mixed and uncontrolled.

## Suggestions

- Add an ablation of the camera autoencoder comparing against (a) raw Plücker concatenation, (b) learned per-frame embedding, and (c) no camera conditioning. This is the minimum requirement to validate the claimed 3D positional guidance contribution.
- Tone down claims in the introduction and discussion to match the evidence: "competitive with" or "comparable to" SOTA rather than "outperforms."
- Provide wall-clock timing or throughput numbers for the parallel decoding claim.
- Include failure case visualizations to give a balanced picture of the method's limitations.
- Fix the notation in Equation 7.

## Score and Decision

**Calibration anchors (all from DeepReview corpus):**

| Anchor | Avg Score | Comparison to ARSS |
|---|---|---|
| LVSM (QQBPWtvtcn) | 7.67 | Much stronger: cleaner results, controlled comparisons, thorough evaluation. ARSS is less mature. |
| GST (NuHYh4YKNe) | 6.25 | Similar AR-for-spatial-reasoning approach; mixed reviewer opinions (3,8,6,8). ARSS has weaker ablation coverage. |
| FreeVS (dTGH9vUVdf) | 5.80 | Accepted despite gaps (single dataset, missing ablation). ARSS has broader evaluation but similar ablation issues. |
| AR-1-to-3 (pOcGFvfgjS) | 5.00 | Closest match: both apply AR to NVS with similar types of weaknesses (uncontrolled comparisons, missing ablations). ARSS is slightly more novel (decoder-only + real scenes vs. AR-diffusion + synthetic objects). |
| Zero-shot NVS (zDJf7fvdid) | 6.00 | Cleaner paper with training-free approach and solid evaluation. |
| InjectAR (K5wFwpaUvK) | 3.50 | Much weaker: poor results, thin experiments. |
| Balancing Token Eff. (IqGVIU4rvM) | 2.50 | Very weak: fundamental misunderstandings, poor results. |

ARSS introduces a genuine novel application (first decoder-only AR for NVS with camera control) and has some clean ablations (token permutation, video tokenizer). However, the experimental support for its core claims is incomplete: the camera autoencoder — one of three main contributions — is not ablated, the claimed superiority over SOTA is unsupported by the mixed quantitative results, and the central motivation for AR over diffusion (causal structure, incremental generation) is not experimentally validated. The paper is competitive with the AR-1-to-3 anchor (5.00) in overall quality and slightly weaker than the GST anchor (6.25). 

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>