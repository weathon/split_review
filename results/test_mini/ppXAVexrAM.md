Here is my consolidated final review:

---

## Summary

ARSS proposes the first decoder-only causal autoregressive transformer for novel view synthesis from a single image, conditioned on a pre-defined camera trajectory. The method combines three core components: (1) a video tokenizer (VidTok with FSQ) that produces temporally consistent discrete visual tokens, (2) a camera autoencoder that maps Plücker raymaps into camera tokens used as per-token 3D positional guidance, and (3) a hybrid token-order permutation strategy that shuffles spatial tokens within each frame while preserving temporal causality. Experiments on RealEstate10K, ACID, and zero-shot DL3DV show competitive results against diffusion-based and feed-forward baselines.

## Strengths

1. **First causal autoregressive model for NVS with camera control.** The paper genuinely demonstrates that decoder-only AR models (GPT-style next-token prediction) can be applied to novel view synthesis, which has so far been dominated by diffusion models. This opens a new paradigm for the task. (Lines 078-080, 112)

2. **Clean and principled system-level design.** The three-module decomposition — video tokenizer for temporal consistency, camera autoencoder for 3D positional instruction, hybrid permutation for bi-directional spatial context — is coherent and each component addresses a specific challenge of applying AR models to multi-view generation. The hybrid permutation strategy is convincingly ablated: it significantly outperforms both raster ordering (PSNR 16.29→19.22) and full spatiotemporal permutation (18.76→19.22) in Table 2.

3. **Competitive quantitative results with honest reporting of trade-offs.** On RealEstate10K, ARSS achieves the best PSNR (19.02), LPIPS (0.269), and FVD (50.51) among compared methods, and on ACID it obtains the best PSNR (21.93) and LPIPS (0.265). The paper transparently acknowledges that it underperforms SEVA on SSIM and FID (lines 419-420), which is commendable.

4. **Convincing qualitative results and zero-shot generalization.** The generated views (Figures 3-5) are visually sharp and geometrically consistent, especially compared to blurry LVSM outputs or distorted MotionCtrl/Genwarp results. The zero-shot evaluation on DL3DV (Table 1, Figure 4) and on AI-generated stylized images (Figure 5) demonstrates generalization beyond the training distribution.

## Weaknesses

### Fatal
None.

### Major

1. **Missing ablation of the camera autoencoder.** The camera autoencoder is one of the paper's three claimed contributions and a central novelty over prior AR image generation methods. It adds substantial complexity (dedicated pretraining, 3D convolutional encoder-decoder, geometric losses in Eq. 5). Yet the paper provides no controlled experiment comparing the full model against a simpler alternative — e.g., a global camera embedding (concatenated pose vector) + standard 2D positional encodings, without per-token camera tokens. The paper cites prior work (Pang et al., 2025; Yu et al., 2024a) for the claim that "positional instruction tokens are the key factor," but does not validate this for its own camera autoencoder design. Without this ablation, it is impossible to assess whether the camera token pipeline materially improves over simpler conditioning schemes, which is a significant methodological gap for a core module.

2. **Mixed quantitative results against SEVA undermine the headline claim.** The paper states it "outperforms current state-of-the-art methods" (line 114), but a closer look at Table 1 reveals a nuanced picture: on RealEstate10K, SEVA achieves higher SSIM (0.670 vs. 0.624) and lower FID (46.98 vs. 47.60); on ACID, SEVA has substantially better SSIM (0.664 vs. 0.623) and FID (33.16 vs. 47.76). The paper's lead on PSNR and LPIPS is genuine but modest. The claim of "outperforming" would be more accurate as "competitive with complementary strengths and weaknesses across metrics." While the paper does acknowledge these trade-offs in the text (lines 419-420), the abstract and conclusion use stronger language.

### Minor

3. **Inconsistent categorization of RayZer.** In the Related Work (line 118), RayZer (Ren et al., 2025b) is discussed in a paragraph about diffusion-based NVS methods, suggesting it is diffusion-based. But in the Experiments (line 265), it is categorized as a "non-diffusion NVS method." This inconsistency should be resolved.

4. **Error accumulation analysis is informative but not a fair comparison.** Figure 6 shows ARSS degrades more slowly per frame than baselines. As the critic notes, this is partly a structural property of the AR paradigm: ARSS generates each frame conditioned on previously generated frames (with ground-truth conditioning during evaluation), while the diffusion baselines generate all frames jointly. The comparison therefore conflates architectural advantage with task design. The analysis is still useful for showing ARSS does not collapse catastrophically, but the paper frames it too strongly as evidence of "superior long-horizon behavior" without acknowledging this confound.

5. **Camera token quantization is underspecified.** The paper specifies that visual tokens are discrete (FSQ quantization in VidTok), but it never states whether the camera tokens produced by the camera autoencoder are also quantized (discrete) or continuous. Since the camera tokens are inserted into an autoregressive sequence that predicts discrete visual tokens via cross-entropy over a codebook, the nature of the camera token representation matters for understanding the architecture. If continuous, the model must handle mixed discrete/continuous inputs, which is non-trivial.

6. **Tokenizer ablation compares image vs. video tokenizer, not two video tokenizers.** The ablation in Table 3 compares a VQ image tokenizer against the VidTok video tokenizer. The large improvement (FVD 137.68→52.56) is expected and shows that temporal encoding helps, but it does not isolate what matters: a comparison between two video tokenizers (e.g., FSQ-based vs. VQ-based video tokenizers) would be more informative about the specific design choice.

### Trivial
- The abstract states "achieves overall comparable to state-of-the-art" while the conclusion says "outperforms state-of-the-art methods" — these should be harmonized.
- Eq. 5 has a typo: "where $\mathbf{d}$ is the normalized camera ray direction, $\mathbf{d}$ is the momentum term" — the second $\mathbf{d}$ should be $\mathbf{m}$.

## Nice-to-Haves
- **Statistical significance / confidence intervals.** Many metrics in Table 1 are close (e.g., ARSS PSNR 19.02 vs. SEVA 18.73 on Re10K). Reporting variance across seeds or providing confidence intervals would strengthen reliability.
- **Camera autoencoder diagnostic analysis.** E.g., perturb camera tokens and measure the change in the generated view, to verify that the autoencoder is learning meaningful geometry.
- **Higher-resolution results.** The paper trains at 256×256 while many diffusion baselines operate at 512×512. A resolution scaling experiment would be a natural next step.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Criticism about baselines being unfair / out-of-setting (MotionCtrl, LVSM, Genwarp).** These are standard baselines in the NVS literature and are evaluated on the same task. The paper also transparently discusses each method's inductive biases. This criticism is overstated.
- **Criticism that RayZer should have been evaluated on DL3DV.** The paper's table caption clearly explains that SEVA, ViewCrafter, and RayZer trained on DL3DV, so zero-shot evaluation is not applicable. The critic misread the caption.
- **Criticism about Eq. 6 vs. Eq. 8 confusion.** The two equations describe different things (sequence structure vs. conditional factorization) and are internally consistent.
- **Request for "no permutation" baseline in ablation.** The "raster" condition is exactly the no-permutation baseline, as the critic later acknowledges.
- **Formatting/style nitpicks and missing appendix content** (parser artifacts).
- **Missing related works** (cannot verify without external sources).

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a novel observation about the method that the authors themselves did not identify.

## Suggestions
1. **Add an ablation of the camera autoencoder.** Compare the full ARSS against a variant that uses a global camera embedding (e.g., an MLP encoding of the full camera pose) + standard 2D RoPE or learned positional encodings, removing the per-token camera tokens. This is the single most important experiment missing from the paper; without it, the value of a core contribution is unverifiable.
2. **Harmonize the RayZer categorization** between the Related Work and Experiments sections.
3. **Clarify whether camera tokens are discrete or continuous**, and if discrete, how the quantization is performed.
4. **Tone down the "outperforms" claim** to reflect the mixed metric profile vs. SEVA, or frame it more precisely (e.g., "competitive with complementary strengths").

## Score and Decision

**Calibration anchors** (all retrieved in single batch):

| Path | Avg Score | Comparison to ARSS |
|------|-----------|-------------------|
| `/home/wg25r/review_agent/human_reviews_2026/PZQHihJlfm.md` (ArchonView, AR NVS) | 5.00 | Similar scope and novelty level — both first AR for NVS. ArchonView had clearer evaluation but was rejected. ARSS has comparable contribution level. |
| `/home/wg25r/review_agent/human_reviews_2026/pIyADlhQsp.md` (CausNVS, AR diffusion) | 3.50 | Also AR-style NVS but limited novelty (integration of known techniques). ARSS has stronger novelty (first causal AR for this task). ARSS scores higher. |
| `/home/wg25r/review_agent/human_reviews_2026/aJJppqAm6r.md` (XFactor, self-supervised NVS) | 6.00 | Stronger paper with clear problem framing, thorough evaluation, and elegant solution. ARSS is not at this level. |
| `/home/wg25r/review_agent/human_reviews_2026/O66RinTZTR.md` (Feature warping NVS) | 3.50 | Diffusion-based NVS with incremental contribution. ARSS has higher novelty. |
| `/home/wg25r/review_agent/human_reviews_2026/2wSORykWAc.md` (Zero-shot NVS) | 5.50 | Rejected despite strong faithfulness framing. ARSS is slightly weaker due to missing ablation. |
| `/home/wg25r/review_agent/human_reviews_2026/OH7joQ9jpl.md` (SPIDER, perception) | 2.50 | Unrelated paper, much lower quality. |
| `/home/wg25r/review_agent/human_reviews_2026/s8kdXG7Zu4.md` (ORT, visual AR) | 4.50 | Similar score — both have genuine contributions but significant gaps that prevent acceptance. |
| `/home/wg25r/review_agent/human_reviews_2026/tIVCfVnIHo.md` (Lyra, 3D recon) | 7.00 | Substantially stronger paper with thorough evaluation. ARSS well below this. |

**Final score: 4.5**

The paper tackles a genuinely novel and timely problem, and the system design is coherent with reasonable empirical support. However, the missing ablation of the camera autoencoder — a core claimed contribution — is a significant methodological gap that prevents full verification of the paper's claims. Combined with the mixed quantitative results vs. SEVA (which the paper honestly reports but then undercuts with overstated "outperforms" language in the conclusion), the paper falls short of the acceptance bar. A revised version adding the camera autoencoder ablation and refining the claims would be a stronger submission.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>