## Summary

This paper proposes VQ-Transplant, a framework that enables plug-and-play replacement of the VQ module in pre-trained visual tokenizers without costly end-to-end retraining, by (1) substituting the VQ module with a frozen encoder-decoder, and (2) performing lightweight decoder adaptation (5 epochs on ImageNet-1k) to resolve the quantization-decoder mismatch. The paper also introduces MMD-VQ, a quantization method leveraging Maximum Mean Discrepancy for distribution alignment between features and codebook. Experiments across multi-scale and fixed-scale VQ configurations, as well as cross-dataset settings, show that VQ-Transplant achieves strong reconstruction fidelity (e.g., 0.81 rFID with MMD VAR) while reducing training cost by ~95% compared to training VAR from scratch.

---

## Strengths

- **Demonstrated ~95% training cost reduction with competitive reconstruction fidelity**: Table 1 shows VQ-Transplant uses 44 GPU-hours (2×A100, 22 h) versus 960 GPU-hours (16×A100, 60 h) for vanilla VAR. Table 2 reports that the full pipeline with MMD VAR (K=8192) achieves 0.81 rFID at this dramatically reduced cost, directly supporting the paper's core claim of enabling near-state-of-the-art performance with far less compute.

- **Decoder adaptation empirically resolves the quantization-decoder mismatch**: Table 3 cleanly demonstrates the two-stage benefit: Stage I (VQ substitution only) yields poor rFID (1.49–1.52), and Stage II (5 epochs of decoder adaptation) improves to 0.81–0.91 rFID, surpassing the original VAR's 0.92. This controlled within-method comparison isolates the decoder adaptation effect and convincingly validates the framework design.

- **MMD-VQ achieves near-100% codebook utilization with low quantization error**: Across all tested codebook sizes and VQ configurations (Tables 3, 5, 7), MMD-VQ attains ≥99.8% utilization and the lowest quantization error among competing methods, providing concrete evidence that the non-parametric distribution alignment (Eq. 5) works as intended.

- **Systematic experimental scope across multiple dimensions**: The evaluation covers five VQ algorithms (Vanilla, EMA, Online, Wasserstein, MMD), two VQ paradigms (multi-scale and fixed-scale), three codebook sizes (4096/8192, 16384/32768/65536), an ablation over 20 adaptation epochs, and held-out datasets (FFHQ, CelebA-HQ, LSUN-Churches). This breadth substantiates the framework's generality.

- **Clear documentation of the multi-scale to fixed-scale VQ transfer pattern**: Tables 3 and 7 show nearly identical performance patterns across both VQ paradigms, confirming that conclusions about distribution-alignment VQ methods and decoder adaptation transfer robustly across VQ architectures.

---

## Weaknesses

### Major

- **Confounded comparison between original VAR and VQ-Transplant**: The original VAR tokenizer (Tian et al., 2024) was trained on **OpenImages** and evaluated zero-shot on ImageNet-1k (0.92 rFID). VQ-Transplant fine-tunes the decoder on **ImageNet-1k** for 5+ epochs as part of Stage II. The reported improvement to 0.81 rFID could therefore be partly or entirely due to domain adaptation (learning ImageNet-1k-specific statistics during decoder fine-tuning) rather than the superiority of the transplanted VQ module. The paper lacks the necessary control experiment: fine-tune the original VAR's native VQ module + decoder on ImageNet-1k for the same compute budget, and compare rFID. Without this, the headline claim "superior reconstruction fidelity" (0.81 vs 0.92) is not properly attributed. The paper's own Figure 3 shows that extending adaptation from 5 to 20 epochs steadily improves rFID from 0.81→0.74, a pattern consistent with domain adaptation being a significant factor. While the framework's practical value (cheap VQ exploration) is not invalidated, the comparative fidelity claim is unsupported as presented. **This is the single most important issue to address.**

- **Token count confound in cross-dataset comparisons (Tables 8–10)**: VQ-Transplant methods use **512 tokens**, while every baseline cited in these tables (RQVAE, VQGAN, VQGAN-FC, VQGAN-EMA, VQGAN-LC, etc.) uses **256 tokens**. Since more tokens naturally improve reconstruction fidelity (as Table 2 itself shows: RQVAE improves from 3.20 to 1.83 rFID when going from 256 to 1024 tokens), this confound means the cross-dataset comparisons do not show a fair architecture-level advantage. The paper does not acknowledge or control for this. Authors should either provide 256-token VQ-Transplant results or explicitly discuss the token count asymmetry's likely impact on the reported rFID gaps (e.g., FFHQ 1.21 vs VQGAN-LC 3.81).

### Minor

- **From-scratch comparison (Table 6) is incomplete**: Table 6 shows VQ-Transplant (22h, 0.81 rFID) vs from-scratch training for 5–7 epochs (25–35h, 1.26–1.40 rFID). The paper acknowledges that discrete tokenizers "typically require hundreds of epochs" to converge from scratch. Running from-scratch training to convergence (not just 7 epochs) and comparing total compute cost would be far more informative. As presented, the comparison only confirms the expected fact that 5–7 epochs of from-scratch training is insufficient.

- **Cross-dataset baselines are dated**: The baselines in Tables 8–10 (VQGAN, RQVAE, VQGAN-EMA, VQGAN-LC, etc.) represent an older generation of tokenizers. More recent work (e.g., TiTok, DiIT, FlexTok, Infinity Tokenizer) is not included, weakening claims of state-of-the-art status on these datasets.

- **No variance or confidence intervals**: All reported metrics (rFID, PSNR, SSIM) are point estimates with no indication of variance across runs or seeds. This is common in large-scale benchmark reporting, but at least a single-sentence note on whether results come from a single run or multiple seeds would improve reliability assessment.

### Trivial

- No explicit limitations section discussing failure modes (e.g., when the pre-trained encoder produces features too specialized to the original VQ space, or when the decoder is shallow).
- Hyperparameter γ (Eq. 3) and multi-Gaussian kernel bandwidths for MMD not specified in the main text (presumably deferred to the appendix).

---

## Nice-to-Haves

- A brief discussion of when VQ-Transplant might fail (e.g., with shallow decoders or highly specialized encoder features). The lower adaptability on LDM-16 (mentioned as deferred to Appendix D) hints at this sensitivity; including a systematic statement in the main text would sharpen the contribution.
- A small analysis of codebook collapse behavior under VQ-Transplant — the paper reports utilization but could further investigate whether different VQ methods exhibit different collapse patterns during the substitution stage.

---

## Removed Points

These points were raised by reviewers but removed after verification or filtering:
- *"From-scratch comparison is a straw man"* (Harsh Critic) — Overstated. The table is not a straw man; it simply shows expected behavior. However, it is incomplete (Minor) as noted above.
- *"MMD gradient flow should be clarified"* — The paper is sufficiently clear: Eq. 3 defines L_VQ with commitment loss + MMD uniqueness loss; the encoder is frozen, so gradients flow to codebook vectors through the MMD term. The formulation is standard.
- *"The 95% cost reduction claim conflates dataset differences"* — Table 1 is clearly marked with dataset names for each method. The speedup factor is computed from GPU-hours, which is a valid comparison even with different datasets. The claim is not misrepresented.
- *"Missing related work"* — Removed per protocol (I cannot verify external completeness of related work).
- Various formatting/style nitpicks, missing appendix references, and speculative concerns about code release — all removed per protocol.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Add the missing control experiment**: Fine-tune the original VAR tokenizer (native VQ + decoder) on ImageNet-1k for the same compute budget (5 epochs, 2×A100). Report rFID. If VQ-Transplant + MMD VAR still outperforms this baseline, the comparative claim is supported. If not, reframe the contribution appropriately (e.g., "VQ-Transplant combined with domain adaptation achieves…").

2. **Acknowledge or control for the token count confound** in Tables 8–10. Either run VQ-Transplant at 256 tokens to provide a direct comparison, or add a paragraph discussing the expected impact of 512 vs 256 tokens on the metric gaps.

3. **For Table 6**: either run from-scratch training to convergence (~100+ epochs) and report total cost, or reposition the table as a within-budget comparison rather than an efficiency comparison, to avoid inviting the natural "of course 7 epochs isn't enough" objection.

4. **Add a limitations section** to the main paper discussing when VQ-Transplant may not work well (e.g., shallow decoders, highly specialized encoder features, LDM-style continuous tokenizers).

---

## Score and Decision

**Calibration summary:**

| Anchor ID | Avg Score | Round | Comparison to This Paper |
|-----------|-----------|-------|--------------------------|
| RYHzkIqHI4 | 4.00 (Reject) | R1 | "Image Tokenizer Needs Post-Training" — weaker evaluation; this paper is stronger |
| QteJJF57yG | 5.00 (Accept Poster) | R1 | "WeTok" — similar contribution level; comparable quality |
| pBz9imKi56 | 4.67 (Reject) | R2 | "A Gain for Reconstruction..." — weaker empirical support than this paper |
| juM14y0caI | 6.00 (Accept Poster) | R1/R2 | "FVQ/VQBridge" — stronger evaluation, cleaner comparisons; this paper is slightly weaker |
| 1jBsi98fVe | 6.50 (Accept Poster) | R2 | "DeTok" — stronger evaluation and broader impact demonstration; this paper is weaker |
| xF0Dcmvsl0 | 5.33 (Accept Poster) | R2 | "PaDT" — different domain but comparable rigor |
| a4fSF5pGJq | 6.50 (Withdrawn/Reject) | R2 | "AToken" — stronger technically but withdrawn |

**Round-1 bracket:** 4.5–6.5
**Round-2 narrowing:** The paper sits between WeTok (5.0) and FVQ (6.0) — stronger than the 4.0–5.0 Reject anchors but weaker than the 6.0+ Accept anchors due to the confounded comparison. The evaluation design issue prevents it from reaching the 6.0 tier of VQBridge/FVQ, but the core framework contribution is genuine and the experimental breadth is solid.

**Final score: 5.0** — The paper presents a well-motivated framework with a practical contribution and extensive experiments, but the central comparative claim is undermined by a domain-adaptation confound that requires a control experiment to resolve. The cross-dataset evaluation has a token-count confound that should also be addressed.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>