Now I have enough data to calibrate. Let me finalize the review.

**Calibration anchors retrieved:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| MambaVC | KgJwbsfN7G.md | 4.80 (Reject) | 1 | Direct competitor in same domain; CMiC is clearly stronger with compression-specific designs and better results |
| GroupMamba | RmmrHEH6Nx.md | 3.00 (Reject) | 1 | Mamba vision paper; CMiC is stronger in novelty and results |
| Window-Based LIC | 6j0GH40mFt.md | 3.40 (Reject) | 1 | LIC paper rejected for limited novelty; CMiC has significantly more novel contributions |
| NCA for Compression | gIrVoQEDQv.md | 3.40 (Reject) | 1 | Lightweight compression; CMiC is in a different league |
| Spatial-Mamba | iDe1mtxqK5.md | 7.00 (Accept) | 1 | Mamba architecture improvement for vision; comparable novelty level and quality to CMiC |
| Mamba (original) | AL1fq05o7H.md | 6.25 (Reject*) | 1 | Foundational Mamba paper; *rejected at ICLR but highly impactful |
| Progressive Compression UQDM | CxXGvKRDnL.md | 8.00 (Accept) | 1 | Novel diffusion-based compression; more theoretically novel than CMiC |
| Disentangled Training for LIC | U67J0QNtzo.md | 7.50 (Accept) | 2 | LIC paper; comparable domain and quality, slightly cleaner theoretical contribution |
| Lattice Transform Coding | Tv36j85SqR.md | 7.20 (Accept) | 2 | Approaching RD limits; more theoretical but similar tier |
| Idempotence & Perceptual IC | Cy5v64DqEF.md | 7.50 (Accept) | 2 | Novel perceptual compression paradigm |
| RECOMBINER | VkWbxFrCC8.md | 6.67 (Accept) | 2 | INR-based compression improvement; CMiC has stronger empirical results |
| MambaPEFT | UAKnJMIBwf.md | 6.00 (Accept) | 2 | Mamba PEFT; CMiC has more substantial novelty |
| Autoregressive Pretraining Mamba | PQpvhUrA1C.md | 5.75 (Accept) | 2 | Mamba vision pretraining; CMiC is clearly stronger |
| MambaQuant | KI45uDnmzv.md | 6.25 (Accept) | 2 | Mamba quantization; different focus, similar or lower novelty |

**Round 1 bracket:** 6.5–7.5
**Round 2 narrowing:** 6.5–7.5 confirmed. CMiC sits above MambaPEFT (6.0) and RECOMBINER (6.67) due to stronger empirical results and more comprehensive evaluation, and below Progressive Compression UQDM (8.0) and Disentangled Training for LIC (7.5) due to less theoretical depth. Spatial-Mamba (7.0) is the closest comparator — both are architecture-level improvements to Mamba with clean experiments and moderate novelty.

**Final score: 7.0**

---

## Summary
This paper introduces Content-Aware Mamba (CAM) for learned image compression with two mechanisms: (1) Content-Adaptive Token Permutation (CTP), which reorders scan sequences by clustering tokens into content-similar groups via a codebook-based cosine K-Means scheme, and (2) Global-Prior Prompting (GPP), which injects sample-specific prompts derived from clustering centroids into the SSM output projection to relax strict causality. The resulting model CMiC achieves state-of-the-art BD-rate on Kodak/Tecnick/CLIC while significantly reducing computational cost compared to prior Mamba-based LIC models.

## Strengths
- **SOTA RD performance with comprehensive comparisons**: Table 1 shows CMiC achieves BD-rate savings of −15.91%, −21.34%, −17.58% on Kodak, Tecnick, CLIC over VTM-21.0, consistently surpassing 14 competing methods including transformer-based (FTIC, TCM), CNN-based (ELIC), and both prior Mamba-based LIC models (MambaVC, MambaIC). The gap over the closest Mamba-based competitor MambaIC is 2.36%–6.48% BD-rate.
- **Highly favorable complexity-performance trade-off**: Table 1 shows CMiC achieves superior BD-rate with 69.11M params, 2.39 TFLOPs, 0.405s latency, and 4.44GB peak memory — compared to MambaIC's 157.09M params, 5.56 TFLOPs, 0.669s latency, and 20.32GB peak memory. The 78% reduction in GPU memory while achieving better RD performance is practically significant.
- **Well-designed ablation cleanly isolating each component's contribution**: Table 2 provides a systematic 2×2 ablation showing CTP and GPP are complementary (CTP alone: 2.0–2.4% BD-rate gain; GPP alone: 0.5–1.4%; combined: 2.7–3.6%), and Table 4 validates the hybrid CAM block design against alternatives.
- **Compelling ERF visualizations providing mechanistic evidence**: Figure 9 shows per-component ERF visualization of a single Mamba layer — column (b) shows strict raster-scan causality, column (c) shows GPP introduces non-zero activations beyond the causal boundary, and columns (d)-(e) show CTP reshapes ERF toward semantically correlated regions. This directly evidences both claimed contributions at the mechanistic level.
- **Practical and stable clustering mechanism**: The codebook-based clustering (Algorithm 1) with EMA-updated learnable centroids shows minimal overhead — throughput drops only from 23.19 to 22.05 samples/s (Table 3), and inference time increases by only 4%. Figure 10 validates clusters capture semantically meaningful regions (red doors, feathers, sky), and Table 5 shows only 16-32 of 64 centroids are active per image, confirming content-adaptive behavior.

## Weaknesses

### Fatal
None

### Major
- **Missing direct ablation against MambaIRv2-style standalone prompt pool**: The paper claims GPP's novelty lies in tying prompts to clustering centroids rather than using a standalone learnable prompt pool (as in MambaIRv2, acknowledged at line 177). However, Table 2 only ablates CTP/GPP presence/absence — it does not include a condition where GPP uses a MambaIRv2-style standalone prompt pool. This missing comparison would directly quantify whether the content-awareness of the prompt or simply the presence of a prompt drives GPP's contribution. The harsh critic correctly identifies this as the single highest-leverage addition. Without it, the novelty of the prompt generation mechanism remains partially unvalidated, though the overall contribution (CTP + GPP together achieving SOTA) is not in question.

### Minor
- **Non-differentiable clustering bottleneck lacks sensitivity analysis**: CTP assigns tokens via argmax over cosine similarity (non-differentiable), with centroids updated through non-gradient EMA of K-Means results, decoupled from the rate-distortion loss. The paper draws a valid analogy to VQ-VAE, and the prompt projection A(·) is end-to-end trainable. However, the EMA decay λ value is not stated in the main text (referenced in Algorithm 1 and Appendix A.8-A.10), and sensitivity to T=5 and λ is not analyzed. A brief sensitivity analysis would strengthen confidence in the mechanism's robustness. This is a standard design pattern, so the concern is bounded.

### Trivial
None

## Nice-to-Haves
- Analyzing what happens when clustering degrades (e.g., K too small like K=8, or codebook frozen after initialization) would clarify the contribution of the clustering mechanism itself vs. the downstream prompt mechanism.
- A brief main-text summary of the Appendix A.8-A.10 clustering stability findings would benefit readers who don't check appendices.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Code release URL appears incomplete"** — This is a PDF parsing artifact ("Code will be released at ."), not an actual issue in the paper.
- **MS-SSIM comparison gap as a weakness** — The paper explicitly addresses this at line 240 ("A direct MS-SSIM comparison is omitted because these two competing methods are only optimized for MSE"). This is a justified omission, not a gap.
- **Table 2 parsing artifact** — The harsh critic correctly identifies that the extracted text shows formatting issues, which is a PDF extraction problem, not a paper problem.
- **Harsh critic's general concern about d_s prompt dimension** — The paper doesn't discuss the choice of d_s, but this is a standard hyperparameter that doesn't affect the core contribution.

## Novel Insights
The paper provides genuinely compelling ERF visualizations (Figures 7-9) that go beyond typical ablation tables by offering mechanistic evidence for how CTP and GPP individually and jointly reshape the model's information processing. The observation that only 16-32 of 64 centroids are active per image (Table 5), with high variance (90.91 on Kodak), is an interesting finding supporting the adaptive upper-bound design of the codebook — K=64 acts as a capacity bound rather than a rigid hyperparameter, making the clustering inherently content-adaptive.

## Suggestions
- Add an ablation condition where GPP uses a standalone learnable prompt pool (MambaIRv2-style) instead of the redundancy-aware dictionary, to directly validate the novelty claim of tying prompts to clustering centroids.
- Report the EMA decay λ value in the main text and include a brief sensitivity table for λ and T.

## Calibration Reporting

**All anchors retrieved:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| MambaVC | KgJwbsfN7G.md | 4.80 | 1 | Direct Mamba-for-compression competitor, rejected for limited novelty; CMiC is clearly stronger |
| GroupMamba | RmmrHEH6Nx.md | 3.00 | 1 | Mamba vision paper, rejected; CMiC is stronger in novelty and results |
| Window-Based Dynamic Attention LIC | 6j0GH40mFt.md | 3.40 | 1 | LIC paper rejected for limited novelty; CMiC has significantly more novel contributions |
| NCA for Compression | gIrVoQEDQv.md | 3.40 | 1 | Lightweight compression, rejected; CMiC is in a different tier |
| Spatial-Mamba | iDe1mtxqK5.md | 7.00 | 1 | Mamba architecture improvement for vision; comparable novelty and quality to CMiC |
| Progressive Compression UQDM | CxXGvKRDnL.md | 8.00 | 1 | Novel diffusion-based compression; more theoretically novel than CMiC |
| Disentangled Training for LIC | U67J0QNtzo.md | 7.50 | 2 | LIC paper with cleaner theoretical contribution; comparable tier |
| Lattice Transform Coding | Tv36j85SqR.md | 7.20 | 2 | Approaching RD limits theoretically; similar tier |
| Idempotence & Perceptual IC | Cy5v64DqEF.md | 7.50 | 2 | Novel perceptual compression paradigm; more theoretically novel |
| RECOMBINER | VkWbxFrCC8.md | 6.67 | 2 | INR-based compression; CMiC has stronger empirical results |
| MambaPEFT | UAKnJMIBwf.md | 6.00 | 2 | Mamba PEFT; CMiC has more substantial novelty |
| Autoregressive Pretraining Mamba | PQpvhUrA1C.md | 5.75 | 2 | Mamba vision pretraining; CMiC is clearly stronger |
| MambaQuant | KI45uDnmzv.md | 6.25 | 2 | Mamba quantization; CMiC has comparable or higher novelty |
| Mamba (original) | AL1fq05o7H.md | 6.25 | 1 | Foundational Mamba; different context |

**Round 1 bracket:** 6.5–7.5. CMiC clearly sits above the rejected LIC/Mamba papers (3.0–4.8) and the weaker accepted Mamba papers (5.75–6.25), while below the most theoretically novel compression papers (7.5–8.0). Spatial-Mamba (7.0) is the closest comparator.

**Round 2 narrowing:** 6.5–7.5 confirmed. CMiC (strong SOTA results, clean ablations, compelling visualizations, one major weakness) aligns with Spatial-Mamba (7.0) in overall quality. It's slightly below Disentangled Training for LIC (7.5) due to the missing ablation against MambaIRv2-style prompts, which weakens the novelty claim for GPP.

**Final score: 7.0**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>