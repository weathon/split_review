Now I have a thorough understanding of the paper and the calibration anchors. Let me write the consolidated review.

**Round-1 bracket**: After comparing with MambaVC (4.80) and Spatial-Mamba (7.00), the initial bracket is [6.5, 7.5]. The paper is clearly far stronger than MambaVC (which was a straightforward application of existing VSS blocks to LIC), and its novelty and thoroughness are comparable to Spatial-Mamba which received 7.00.

**Round-2 narrowing**: Within the [6.5, 7.5] bracket, the paper compares favorably to Spatial-Mamba (7.00) — both propose novel mechanisms addressing Mamba's vision limitations, but CMIC has a more extensive evaluation and ERF analysis for its target task. It's not at the level of the 8+ generative/compression theory papers. Final anchoring: ~7.0.

---

## Summary

This paper proposes Content-Aware Mamba (CAM) for learned image compression, addressing two inherent limitations of Mamba-style SSMs: (1) the content-agnostic raster scan order, which fails to group semantically related tokens, and (2) the strict causality that prevents tokens from accessing future context without expensive multi-directional scans. CAM introduces Content-Adaptive Token Permutation (CTP) — codebook-based clustering that reorders tokens by feature similarity — and Global-Prior Prompting (GPP) — a prompt dictionary that modulates the SSM output with sample-specific global statistics. Built into the CMIC model, these mechanisms achieve SOTA rate-distortion performance (15.91%, 21.34%, 17.58% BD-rate savings over VTM-21.0 on Kodak, Tecnick, CLIC) while maintaining favorable complexity (56% fewer parameters, 57% fewer FLOPs than MambaIC).

## Strengths

1. **Well-motivated and concretely grounded innovation.** The paper identifies two specific, verifiable limitations of Mamba for image compression (rigid scan order in §3.3, strict causality in §3.4) and proposes mechanisms that directly target each one. The ERF visualization in Figure 9 convincingly shows that CTP breaks the raster-scan pattern and GPP introduces non-causal activations — the mechanisms work as claimed.

2. **Strong empirical evidence across multiple dimensions.** The RD comparisons (Table 1, Figures 4-6) show CMIC outperforming a large set of strong baselines including prior Mamba-based methods by wide margins (7.5-10% BD-rate reduction over MambaVC). The ablation study (Table 2) cleanly isolates CTP (2.0-2.4% BD-rate gain) and GPP (0.5-1.4% gain), and the architecture ablations (Table 4) show CAM blocks outperform Conv, 2D Mamba, and pure-attention alternatives.

3. **Compelling and informative ERF analysis.** Figures 7-9 provide unusually strong evidence for the claimed mechanisms. The per-image ERFs in Figure 8 show CMIC adapting its receptive field to semantic structures (hair, feathers, shorelines) while transformer baselines yield isotropic, content-agnostic ERFs. Figure 9 directly demonstrates the individual effects of CTP and GPP on a single layer — this is the kind of diagnostic that makes the paper's claims credible.

4. **Favorable efficiency-performance trade-off.** CMIC achieves the best RD performance among all compared methods while using substantially fewer parameters (69.11M) and lower peak memory (4.44GB) than MambaIC (157.09M, 20.32GB), and decoding latency of 0.405s is competitive with efficient methods.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported by the evidence.

### Minor

1. **Training data mismatch for baseline comparisons.** The paper trains CMIC on Flickr2W, but reports BD-rate numbers for baselines (MLIC++, FTIC, MambaVC, MambaIC, etc.) presumably taken from their original papers where different training datasets were used (ImageNet, CLIC, etc.). This is a well-known limitation in the LIC literature, but it does mean the reported margins may partially reflect training data differences rather than architectural superiority. The most relevant comparison (vs. MambaVC and MambaIC) shows very large gaps (7.5-10%) that are unlikely to be fully explained by this confound, but acknowledging this limitation explicitly would strengthen the paper. Retraining at least the Mamba baselines under the same pipeline would make the SOTA claim unassailable.

2. **Entropy model confound in the ablation design.** The baseline in Table 2 (no CTP, no GPP) already uses the enhanced entropy model (built upon SCTX with depthwise conv and gated MLPs), so the relative gains of CTP and GPP are correctly isolated from that baseline. However, the total improvement of the full model over a standard SCTX-based baseline is not reported. The paper's own statement (§4.5) that "adding CAM yields negligible performance gains [in the entropy model]" addresses a different question. A simple ablation — replacing the enhanced entropy model with the standard SCTX in the baseline — would clarify how much of the overall gain comes from the entropy model improvements vs. the CAM mechanisms.

3. **VTM configuration not specified.** The BD-rate anchor is VTM-21.0, but the encoding mode, QP range, and rate control settings are not reported. This is a minor documentation gap that makes exact reproduction harder.

4. **Origin of baseline complexity numbers is ambiguous.** The Table 1 caption states "FLOPs, peak memory and decoding latency are measured on 2K-resolution images" but does not clarify whether these are re-measured on the authors' hardware or taken from original papers (the >10s latency for FTIC suggests the latter). A simple footnote would resolve this.

### Trivial

- Encoding latency is reported only in the appendix (§A.14). A brief mention in the main paper would be useful since encoding time is often the practical bottleneck.
- The paper does not discuss the choice of VTM encoding parameters (QP range, intra-mode settings), which can shift BD-rate anchor points.

## Nice-to-Haves

- Confidence intervals or multiple-run statistics for the BD-rate numbers in ablation studies would strengthen the conclusions, though this is not standard practice in the field.
- An experiment retraining MambaVC or MambaIC on Flickr2W under the same pipeline would definitively address the training data confound.

## Removed Points

- **Stability concerns about EMA centroid updates during training** — this is speculation; the paper already describes the EMA mechanism and notes it ensures stability. No evidence of actual instability is presented.
- **"Statistical significance not reported" as a major weakness** — confidence intervals for BD-rate on standard test sets are not standard practice in LIC; this is a minor point at best.
- **Criticism that CTP/GPP gains might be from entropy model** — the paper's ablation is correctly designed to isolate CTP and GPP contributions (entropy model is fixed across all configurations). The concern is valid about a *different* question (total gain over SCTX baseline), which I've reflected in the Minor section above.
- **Suggestion to address problems outside stated scope** — various requests for additional architectural explorations that go beyond what the paper claims to contribute.

## Novel Insights

None beyond the paper's own contributions. The ERF diagnostic methodology (Figure 9) showing how each component individually transforms the receptive field is particularly insightful and well-executed.

## Suggestions

1. In the rebuttal or revision, clarify the source of all baseline numbers (BD-rate and complexity) in Table 1. If possible, retrain MambaVC on Flickr2W and report those numbers alongside the originals.
2. Add a small ablation comparing the enhanced entropy model against the standard SCTX entropy model with everything else held fixed, to separate entropy model gains from transform network gains.
3. Specify the VTM encoding parameters used for BD-rate computation in the experimental setup.

## Score and Decision

**Calibration anchors used across all rounds:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|-------------------------|
| MambaVC (KgJwbsfN7G) | 4.80 | R1 | Much weaker — straightforward application of existing VSS blocks, limited novelty, fewer baseline comparisons |
| Spatial-Mamba (iDe1mtxqK5) | 7.00 | R1 | Comparable — both propose novel mechanisms for Mamba's vision limitations. CMIC has more thorough evaluation for its target task |
| Mamba (AL1fq05o7H) | 6.25 | R1 | Not directly comparable (foundational SSM paper, not LIC) |
| Idempotence (Cy5v64DqEF) | 7.50 | R2 | Different contribution type (theoretical). CMIC's empirical thoroughness is higher |
| Approaching RD Limits (Tv36j85SqR) | 7.20 | R2 | Different contribution (theoretical lattice quantization). CMIC is stronger in empirical validation |

**Round-1 bracket:** [6.5, 7.5]  
**Round-2 narrowing:** The paper is clearly above MambaVC (4.80) by a large margin. It is comparable to Spatial-Mamba (7.00) with slightly more thorough evaluation on its target task. It does not reach the level of the 8+ papers which make more fundamental theoretical contributions.  
**Final score:** 7.0

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>