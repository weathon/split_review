Now I have sufficient calibration data. Let me construct the final review.

## Summary

The paper proposes ARSS, a decoder-only autoregressive transformer framework for novel view synthesis from a single image with camera trajectory control. It uses a video tokenizer for temporally consistent discretization, a camera autoencoder that encodes Plücker raymaps into 3D positional tokens, and a spatial-only permutation strategy that preserves temporal causality while enabling bi-directional spatial context. Evaluations on RealEstate10K, ACID, and DL3DV show competitive results against diffusion-based and feed-forward baselines.

## Strengths

- **First decoder-only AR model for NVS with explicit camera control.** The paper establishes a new paradigm distinct from joint-denoising diffusion methods. The claim is clearly stated and well-supported by the architecture description (Section 1, Section 3). This is a genuine methodological contribution that opens a new direction for causal view generation.

- **Hybrid token permutation strategy is well-motivated and validated.** The spatial-only permutation (maintaining temporal order) is a sensible adaptation of prior AR image-generation work to multi-view sequences. Table 2 quantitatively confirms it outperforms both raster ordering (19.22 vs. 16.29 PSNR) and full spatiotemporal permutation (19.22 vs. 18.76), and Figure 7 visually demonstrates the qualitative benefits.

- **Camera autoencoder with geometry-aware losses is thoughtfully designed.** The loss function (Eq. 5) includes ray-direction reconstruction, momentum reconstruction, unit-norm regularization, and orthogonality constraints — explicit geometric inductive biases that tie camera tokens to accurate 3D positional information. This design is critical for incorporating camera control into an AR sequence.

- **Error accumulation analysis, while imperfect, addresses a key failure mode.** Figure 6 tracks per-frame metrics over 17 frames and shows that ARSS maintains higher quality with slower degradation than all baselines. This is a direct benefit of the causal AR structure that joint-denoising methods cannot offer, and few NVS papers analyze this at all.

- **Zero-shot generalization is demonstrated.** Competitive results on DL3DV (16.70 PSNR, +0.84 over LVSM) and qualitative generalization to AI-generated images (Figure 5) show the method does not overfit to the training distribution.

## Weaknesses

### Major

- **Inconsistent quantitative reporting between Table 1 and ablation tables.** The main results (Table 1) report "Ours" at PSNR 19.02 on RealEstate10K, while the ablation studies (Tables 2 and 3) report 19.22 for the identical "ours" condition with very different FID values (47.60 vs. 60.11 vs. 52.56). The paper never specifies which dataset or split the ablations are evaluated on. This discrepancy undermines trust in the reported numbers. The ablations should clearly state the evaluation protocol used or reconcile the values.

- **Key baseline (Genwarp) is absent from the quantitative comparison.** Genwarp (Seo et al., 2024) is listed as a baseline in Section 4.1 and appears prominently in qualitative comparisons (Figures 3, 4), but is completely absent from Table 1 with no explanation. For DL3DV, only three methods are reported and the exclusion criteria applied to SEVA/ViewCrafter/RayZer (training data overlap) are not applied consistently. Without quantitative comparisons, the visual superiority claims against Genwarp remain unsubstantiated.

- **Claims of "outperforming" SOTA are inconsistent with the evidence.** The Introduction states the method "out-performs current state-of-the-art methods," and the Discussion repeats "outperforms state-of-the-art methods." However, on ACID, ARSS is substantially worse than SEVA in SSIM (0.623 vs. 0.664, −6.2%) and FID (47.76 vs. 33.16, +44%). On RealEstate10K, ARSS trails SEVA in SSIM (0.624 vs. 0.670) and FID (47.60 vs. 46.98). The quantitative results section itself notes these trade-offs, but the overarching claims in the Introduction and Discussion do not reflect this nuance. A method with mixed metric performance — winning on PSNR/LPIPS but losing on SSIM/FID — should be described as "competitive" or "comparable," not "outperforming."

### Minor

- **Error accumulation analysis lacks formal comparison.** Figure 6 plots per-frame metrics and visually compares slopes, but no confidence intervals, standard deviations, or formal tests of degradation-rate differences are provided. The baselines also start at different initial quality levels, so the visual "slower degradation" claim partly conflates starting quality with accumulation rate. This weakens but does not invalidate the analysis — the per-frame gap is visually clear even at frame 0.

- **256×256 resolution is low relative to current NVS standards.** Many diffusion-based methods operate at 512×512 or higher. The paper acknowledges this limitation in the Discussion but does not discuss whether the approach scales. This restricts the practical relevance of the results.

- **The parallel decoding claim is mentioned but unsupported.** Section 3.2.3 states that random token shuffling "allows parallel decoding" and provides "capacity to predict multiple tokens at one time," but no speed benchmarks or parallelism analysis are provided to substantiate this.

- **Inconsistency between abstract and introduction claims.** The abstract describes results as "overall comparable to state-of-the-art," while the Introduction claims the method "out-performs current state-of-the-art methods." These should be harmonized.

### Trivial

- Eq. (7) notation for the cross-entropy loss appears to pass only one argument (`CE(f_theta([...]))`) while Eq. (3) correctly uses two arguments. This is likely a formatting/parsing artifact but should be corrected.

## Nice-to-Haves

- Include Genwarp in Table 1 if quantitative evaluation is feasible; if not, state the reason explicitly.
- Report confidence intervals or per-run variance for key metrics in Tables 1–3.
- Benchmark inference speed (frames per second) against diffusion-based baselines, especially given the sequential nature of AR decoding.
- Provide formal slope analysis for error accumulation (metric vs. frame index with confidence intervals across multiple sequences).
- Show failure cases to provide a balanced qualitative assessment.

## Removed Points

- **Criticism about notation (P_i(j) not defined):** The paper explicitly defines this notation in Section 3.2.3: "x_{ij}^{P_i(j)} represents the j-th randomly shuffled token under i-th frame... This means any given token x_{ij} can only be swapped with x_{ik}, where 1 ≤ j ≠ k ≤ n." The definition is present and sufficient. *Removed as factually wrong.*

- **Criticism that Eq. (7) is "malformed":** The PDF parser may have dropped the second CE argument; this is a formatting artifact, not a paper error. *Removed per hard rules on parser artifacts.*

- **Computational resources contradiction:** The paper's claim about "without such requirements" refers to not needing the large-scale pre-training and high-resolution data that SEVA requires, not that 8 H100s are negligible. *Removed per rule against misreading.*
- **Missing appendix/proofs:** Parser strips these from all papers. *Removed per hard rules.*
- **Missing related work references:** Cannot verify without external sources. *Removed per hard rules.*
- **Generic "gap between motivation and evaluation" about world models:** The paper's experiments evaluate NVS on standard benchmarks; this is a reasonable evaluation of the core technical contribution. *Removed as scope creep.*
- **Strength Finder's generic strengths about "important problem":** Generic and not specific to this paper. *Removed.*
- **Strength Finder's strengths conflating with weaknesses:** Retained only concrete, evidence-backed strengths.

## Novel Insights

None beyond the paper's own contributions. The key insight — that spatial-only token permutation within a causal AR framework enables decoder-only view synthesis — is clearly stated and well-demonstrated.

## Suggestions

1. Reconcile the "ours" numbers between Table 1 and the ablation tables. Specify which dataset/split the ablations use and present the results under a consistent evaluation protocol.
2. Either add Genwarp's quantitative results to Table 1, or explicitly state why it cannot be included. Consider reporting results on a subset where quantitative comparison is feasible.
3. Calibrate the claims in the Introduction and Discussion to match the evidence — e.g., "achieves competitive results" or "outperforms on perceptual metrics while trading off on pixel-aligned ones" rather than a blanket "outperforms."
4. Add confidence intervals or error bars to Figure 6, or at minimum report the slope of each metric vs. frame index for each method.
5. Provide at least one speed benchmark (inference time per frame) to substantiate the parallel decoding claim or remove the claim.

## Score and Decision

**Calibration anchors** (from batch retrieval):

| Anchor | Avg Score | Comparison to ARSS |
|--------|-----------|-------------------|
| **LVSM** (QQBPWtvtcn) | 7.67 | Significantly stronger in experimental rigor, evaluation breadth, and result quality. LVSM achieves clean SOTA gains; ARSS has mixed metric performance and evaluation issues. |
| **Where Am I / GST** (NuHYh4YKNe) | 6.25 | Mixed reviews; stronger novelty claims but controversy over prior art. ARSS has clearer novelty but weaker evaluation. |
| **Zero-shot NVS via Video Diffusion** (zDJf7fvdid) | 6.00 | Clean training-free method with clear advantages. ARSS is comparable in presentation quality but has evidential inconsistencies. |
| **DnD-Transformer** (wryFCrWB0A) | 6.20 | Well-received AR image generation paper with thorough evaluation. ARSS is weaker in evaluation rigor. |
| **AR-1-to-3** (pOcGFvfgjS) | 5.00 | Closest anchor: same topic (AR for multi-view generation), similar quality level, similar issues with rigor and evaluation scope. ARSS is slightly stronger in breadth (multiple datasets, zero-shot) but both have real evidential weaknesses. |
| **CCM-DiT** (15lk4nBXYb) | 3.00 | Clearly weaker: poor presentation, minimal evaluation, unclear math. ARSS is substantially stronger. |
| **GeoGS3D** (I86z54CL2y) | 3.40 | Weak reconstruction paper. ARSS is much stronger in technical contribution and experimental scope. |

Relative to these anchors, ARSS is most comparable to AR-1-to-3 (5.0). It has a genuine methodological contribution and reasonable experiments, but the inconsistent numbers, missing baseline, and overclaimed results prevent acceptance without substantial revision. It is clearly stronger than the sub-4.0 papers but notably weaker than the 6+ papers.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>