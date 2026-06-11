Now I have a thorough understanding of the calibration landscape. Let me synthesize my final review.

**Calibration Summary:**

**Round 1 bracket:** Between MambaVC (4.80) and Spatial-Mamba (7.00).

CMIC is clearly above MambaVC (4.80) — MambaVC was a straightforward application of VSS blocks with weak baselines, while CMIC has genuinely novel mechanisms and comprehensive SOTA comparisons. CMIC is clearly above MamBEV (6.60) and RECOMBINER (6.67) — those papers have more significant weaknesses (limited novelty, weaker comparisons, don't beat SOTA). CMIC is comparable to Spatial-Mamba (7.00) in overall quality — Spatial-Mamba has a slight edge from its theoretical analysis, but CMIC has stronger empirical depth (ERF analysis, clustering visualizations, complexity analysis). The one major weakness (entropy model confound in cross-method comparisons) and two minor issues (causality language precision, Kodak SOTA qualification) pull CMIC slightly below Spatial-Mamba. 

**Final score: 6.5** — borderline accept, a well-executed paper with novel mechanisms, strong results, and thorough analysis, held back by one significant but addressable evidential gap.

---

## Summary

This paper proposes Content-Aware Mamba (CAM), an adaptation of Mamba-style state-space models for learned image compression. CAM introduces two mechanisms: Content-Adaptive Token Permutation (CTP), which uses a codebook-based clustering to reorder tokens by feature similarity before the SSM scan, and Global-Prior Prompting (GPP), which injects sample-specific global priors derived from cluster centroids into the SSM output projection. The full model, CMIC, achieves BD-rate improvements over VTM-21.0 of 15.91%, 21.34%, and 17.58% on Kodak, Tecnick, and CLIC respectively, with favorable complexity trade-offs (69.11M parameters, 2.39 TFLOPs).

## Strengths

- **CTP demonstrably improves SSM-based compression.** Table 2 shows that adding CTP to a vanilla Mamba baseline yields BD-rate reductions of 2.0% (Kodak), 2.4% (Tecnick), and 1.8% (CLIC). The clustering visualizations in Fig. 10 confirm that tokens corresponding to semantically coherent regions (red doors/windows in Kodim01, clouds/sky in Kodim21, feathers in Kodim23) are correctly grouped, validating that the codebook-based clustering captures meaningful content structure.

- **GPP effectively mitigates Mamba's causality at low cost.** The ERF visualizations in Fig. 9 provide direct mechanistic evidence: with GPP enabled (column c), non-zero activations appear beyond the scan position, and the model can incorporate global context without multi-directional scans. Performance gains are independently validated in Table 2 (0.5%–1.4% BD-rate improvement from GPP alone).

- **Strong complexity-performance trade-off.** CMIC achieves the best BD-rate among Mamba-based methods while using substantially fewer resources than MambaIC (69.11M vs 157.09M parameters, 2.39 vs 5.56 TFLOPs, 0.405s vs 0.669s latency, 4.44GB vs 20.32GB peak memory). The single-scan design avoiding multi-directional scans drives these savings.

- **Thorough and well-structured ablation design.** The paper systematically isolates CTP and GPP (Table 2), compares CAM blocks against Conv and 2D Mamba alternatives (Table 4), ablates cluster count K (Table 6), and reports training throughput impact (Table 3). Each ablation answers a distinct design question.

- **ERF analysis across competing architectures is informative.** Figure 7 compares ERFs of 10 LIC models, showing CMIC's analysis transform has a broader global spatial context than CNN-, Transformer-, and Mamba-based competitors. Figure 8 shows CMIC's high-influence regions align with semantic structures while competitors show compact, content-agnostic isotropic patterns.

- **Honest reporting of limitations.** The paper notes that adding CAM to the entropy model yields negligible gains while increasing latency (Sec 4.5), and that K=128 provides diminishing returns over K=64 (Table 6). The cluster activation analysis (Table 5) showing only ~36% of centroids are active per image with high variance (90.91) provides credible evidence of content-adaptivity rather than degenerate clustering.

## Weaknesses

### Fatal
None.

### Major
- **Entropy model contribution is not disentangled from CAM in cross-method comparisons.** CMIC uses an enhanced SCTX entropy model with depthwise convolutions and gated MLPs (Fig. 3, Sec 3.2), while baselines like MambaIC and MambaVC use their own different entropy models. When CMIC is compared against these baselines in Table 1, a reader cannot tell how much of the gain (e.g., the 2.36% BD-rate advantage over MambaIC on Kodak) comes from CAM transform blocks versus the enhanced entropy model. The paper isolates CAM's contribution within its own architecture (Tables 2 and 4), but does not report a "CMIC with vanilla SCTX entropy model" data point to cleanly separate the two contributions for cross-method comparisons. Table 4 partially addresses this by showing CAM blocks outperform alternatives within the same entropy model framework, but the headline result in Table 1 conflates multiple architectural changes. This matters for the paper's claim that CAM specifically drives the SOTA results against prior methods.

### Minor
- **Causality language is imprecise in places.** The paper describes GPP as enabling "non-causal" processing (abstract, Fig. 9 caption: "introduces non-causality beyond raster scan") and "overcoming the sequential dependency." However, GPP modifies the output projection matrix **C** (Eq: **O**_i = (**C** + **P**)**h**_i + **D****x**_i), while the hidden state recurrence **h**_i = **Ā****h**_{i-1} + **B̄****x**_i remains causal. What GPP actually provides is globally-conditioned readout from a causal state. The ERF visualizations in Fig. 9 are consistent with this — the prompt broadens the receptive field — but they demonstrate globally-conditioned sequence modeling, not non-causal modeling per se. The paper should describe GPP as injecting global conditioning into an otherwise causal scan. This is a precision issue, not a methodological flaw; the mechanism is correctly described in Section 3.4.

- **SOTA claim is slightly overbroad on Kodak.** The paper states it "achieves state-of-the-art (SOTA) RD performance" without qualification. Table 1 shows MLICv2 achieves −16.16% BD-rate on Kodak, while CMIC achieves −15.91% — a 0.25% gap. CMIC does lead on Tecnick and CLIC by clear margins, and is more parameter-efficient than MLICv2 (69.11M vs 84.30M), so a qualified claim (e.g., "SOTA or competitive on all datasets, with clear wins on high-resolution images") would be both accurate and more precise.

### Trivial
- **MS-SSIM BD-rate values could be more clearly labeled.** In Section 4.3, the paper states "It outperforms TCM-L and FTIC by -7.34% and -3.87% respectively." While the preceding sentence mentions MS-SSIM, explicitly labeling these as "MS-SSIM BD-rate" values would prevent momentary confusion.

## Nice-to-Haves
- Disentangling the entropy model contribution from CAM with a "CMIC + vanilla SCTX entropy model" data point would substantially strengthen the evidence that CAM, specifically, drives cross-method gains.
- Tightening the causality language throughout to consistently describe GPP as "globally-conditioned sequence modeling" rather than "non-causal modeling" would improve precision without weakening the contribution.
- Reporting total training epochs/steps in Section 4.1 would improve standalone reproducibility (the paper reports learning rate, optimizer, λ values, architecture dimensions, and K-Means iteration count, but omits training duration).
- Ablating the window size or discussing how local (window attention) and global (CAM) modeling complement each other could strengthen the architectural analysis.
- Including encoding latency in the main text rather than deferring entirely to Appendix A.14 would be helpful given its practical importance.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "Causality claims are overstated and imprecise (Structural)."** → DEMOTED to Minor. The paper explicitly describes the mechanism correctly (modifying C, not the recurrence) in Section 3.4, and the ERF evidence supports the practical effect. The language imprecision does not invalidate the contribution or mislead about the mechanism. The paper says "relaxing the strict causal constraint" and "mitigates the strict causality," not "eliminates causality entirely."

- **Harsh Critic: "Table 2 has a parser-induced formatting error."** → REMOVED per formatting nitpick rule. The table structure is a parser artifact; the original submission does not have this issue.

- **Harsh Critic: "The baseline value (-13.26% on Kodak) is not shown explicitly as a separate row."** → REMOVED. This is a consequence of the same parser formatting issue in Table 2. The intended table structure (both-disabled baseline, CTP-only, GPP-only, both-enabled) is reconstructible from the text discussion.

- **Harsh Critic: "The interaction between window attention and CAM blocks is underexplored."** → MOVED to Nice-to-Haves. This is a reasonable suggestion for strengthening the paper but is not a weakness — the paper already demonstrates CAM's contribution through Table 4.

- **Harsh Critic: "Encoding latency is deferred to Appendix A.14."** → MOVED to Nice-to-Haves. For a compression method, encoding time is practically relevant, but the paper already provides decoding latency and FLOPs, and the appendix reference is appropriate.

- **Harsh Critic: "Training duration and batch size feel important enough for the main paper."** → MOVED to Nice-to-Haves. Batch size is mentioned for throughput (line 281: "batch size 8"), and training epochs are standard appendix material. Not a substantive weakness.

## Novel Insights
The paper's clustering mechanism demonstrates an interesting architectural pattern: EMA-updated codebook centroids updated via non-gradient K-Means, combined with a differentiable prompt projection trained end-to-end. This cleanly separates distributional clustering (which benefits from dataset-level statistics) from gradient-based optimization (which drives the compression objective). The ERF analysis in Fig. 9 also provides a useful methodological template for analyzing SSM receptive fields in vision — the column-wise ablation shows exactly how each component (CTP, GPP) reshapes the ERF from a strict raster-scan pattern to a globally-aware one.

## Suggestions
- Add a "CMIC with vanilla SCTX entropy model" data point to Table 1 or a supplementary table to cleanly separate the transform and entropy model contributions in cross-method comparisons.
- Replace "non-causal" language with "globally-conditioned" throughout, and update the Fig. 9 caption accordingly.
- Qualify the SOTA claim on Kodak by noting the 0.25% gap to MLICv2 while highlighting the wins on Tecnick/CLIC and the parameter efficiency advantage.

## Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| MambaVC | KgJwbsfN7G.md | 4.80 | R1 | CMIC is substantially stronger — novel mechanisms vs. straightforward VSS application, comprehensive SOTA comparisons vs. weak baselines. |
| Spatial-Mamba | iDe1mtxqK5.md | 7.00 | R1 | Comparable quality. Spatial-Mamba has theoretical analysis edge; CMIC has stronger empirical depth. CMIC slightly below due to entropy model confound. |
| Autoregressive Pretraining w/ Mamba | PQpvhUrA1C.md | 5.75 | R1 | CMIC is stronger — more novel mechanisms and task-specific depth. |
| MamBEV | MvEkN2ejZ1.md | 6.60 | R2 | CMIC is stronger — more thorough ablations, clear efficiency data, better SOTA positioning. |
| RECOMBINER | VkWbxFrCC8.md | 6.67 | R2 | CMIC is stronger — achieves SOTA in its domain vs. lagging VAE methods, more comprehensive comparisons. |
| Idempotence & Perceptual Compression | Cy5v64DqEF.md | 7.50 | R2 | CMIC is weaker — lacks the theoretical depth of this anchor. |

**Round 1 bracket:** 4.80–7.00 → narrowed to 6.50–7.00 in Round 2. CMIC sits above MamBEV (6.60) and RECOMBINER (6.67) due to stronger SOTA results and more thorough experiments, but slightly below Spatial-Mamba (7.00) due to the entropy model confound and less theoretical depth. Final score reflects borderline accept level.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>