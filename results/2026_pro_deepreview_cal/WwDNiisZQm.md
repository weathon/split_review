Now I have a clear calibration picture. Let me compile my findings.

**Bracketing Round 1:**
- MambaVC (4.80): First Mamba-for-LIC paper, limited novelty, weak baselines
- MambaIC (not retrieved but in the paper's Table 1): Similar domain
- Spatial-Mamba (7.00): Novel SSM with state fusion, good theory, strong vision results
- FTIC (6.00): Strong LIC paper, frequency-aware transformer, SOTA results

**Round 2 narrowing:**
- FTIC (6.00): Most directly comparable — SOTA LIC paper with novel transformer blocks, comprehensive evaluation, minor missing ablations

CMIC is clearly stronger than FTIC: more novel mechanisms, more comprehensive ablations, stronger SOTA results, better efficiency analysis. Slightly below Spatial-Mamba (7.00) in theoretical depth but deeper in domain-specific innovation. **Bracket: 6.0–7.0, final score: 6.5.**

Now let me write the final review.

Let me verify my key assessments against the paper one more time:

1. Gradient flow: The paper uses EMA-updated centroids and the permutation is a gather/scatter of token values. The token features themselves are trained end-to-end through the SSM. This is standard practice (VQ-VAE style). The harsh critic's claim that this is a "structural concern" is overstated. I'll note it as a minor clarity issue.

2. Missing simpler baselines: The paper ablates CTP on/off and GPP on/off, showing each contributes. But comparing against random permutation or global average pooling would strengthen the evidence. This is a moderate weakness.

3. Efficiency comparison: The paper reports CMIC is more efficient than MambaIC, which is true regardless of whether it's from single-scan or parameter count. The paper doesn't falsely attribute all savings to single-scan. Minor weakness.

4. Statistical variability: Standard practice in LIC. Nice-to-have.

Let me write the review now.Now I have all the information I need. Let me compile the final review.

---

## Summary

This paper introduces Content-Aware Mamba (CAM), which augments Mamba-style state-space models for learned image compression with two novel mechanisms: (1) Content-Adaptive Token Permutation (CTP) that uses codebook-based cosine clustering to reorder the SSM scan sequence by feature-space similarity rather than spatial proximity, and (2) Global-Prior Prompting (GPP) that injects cluster-derived, sample-specific prompts into the SSM output projection to relax strict causality without multi-directional scanning. The resulting CMIC model achieves state-of-the-art rate-distortion performance (15.91%, 21.34%, 17.58% BD-rate savings over VTM-21.0 on Kodak, Tecnick, CLIC) while maintaining practical efficiency.

## Strengths

- **Genuinely novel mechanisms tailored for the problem.** CTP addresses a real and well-motivated limitation of Mamba for images — the rigid raster scan poorly matches feature-space redundancy structure. GPP provides a lightweight alternative to multi-directional scanning for relaxing causality. Both are designed specifically for compression, not borrowed wholesale from prior work. The codebook-based clustering with EMA updates is a pragmatic design that avoids per-sample online K-means instability.

- **Comprehensive and well-structured ablation studies.** Table 2 cleanly isolates the contributions of CTP (2.0–2.4% BD-rate reduction alone) and GPP (0.5–1.4% alone), showing they are complementary (2.7–3.6% combined). Table 4 validates the CAM block against Conv, 2D Mamba, attention-only, and CAM-only alternatives. Table 6 explores cluster count sensitivity. The ERF visualizations (Figures 7–9) are particularly effective — Figure 9 convincingly demonstrates how GPP introduces non-causality (ERF extends beyond the scan midpoint) and how CTP reshapes the receptive field toward semantically correlated regions.

- **Strong state-of-the-art results with clear margins.** Table 1 shows CMIC outperforms all compared methods across three datasets, including recent strong baselines (MLICv2, DCAE, FTIC, MambaIC). The gains over Mamba-based competitors are substantial: 7.51%–10.09% over MambaVC and 2.17%–6.48% over MambaIC in BD-rate. The RD curves (Figures 4–6) show consistent advantages across the entire bitrate range.

- **Practical efficiency preserved.** Despite the added adaptivity, training throughput drops only marginally (23.19→22.05 samples/s, Table 3) and decoding latency increases by only 4% on 2K images. The single-scan design yields substantial memory savings (78% less GPU memory than MambaIC).

- **Qualitative evidence supports the content-adaptive claim.** Figure 10 shows clusters capture semantically meaningful patterns (red doors/windows, clouds, feathers) across images, and Table 5 confirms the number of active centroids adapts dynamically per image (mean 23–26 out of 64, high variance).

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported by the evidence presented.

### Minor

- **Missing simpler reordering and prompting baselines.** The ablation studies compare CTP on/off and GPP on/off, which establishes that each component helps. However, the paper does not compare CTP against simpler content-adaptive orderings — such as sorting tokens by a learned scalar projection or even a random permutation — that would test whether the full codebook-based clustering adds value beyond merely breaking the spatial raster order. Similarly, GPP is not compared against a lightweight alternative like global average pooling of tokens as a prompt. These comparisons would substantially strengthen the evidence that the specific designs (cosine clustering with EMA codebook, cluster-tied prompt dictionary) are necessary rather than just beneficial. The current results leave open the possibility that simpler mechanisms could achieve comparable gains, though the strong absolute performance makes this unlikely to change the overall conclusion.

- **Gradient flow through the permutation is not explicitly discussed.** The CTP mechanism uses hard cluster assignments from a non-gradient K-means procedure (Algorithm 1), with centroids updated via EMA. While this is a standard and sound approach (analogous to VQ-VAE), the paper does not specify whether token features are detached before clustering or clarify that gradients flow through the permutation indices back to the token values (the SSM processes the permuted tokens, so gradients do reach the original features through the gather/scatter). A brief clarification would prevent reader confusion about training soundness and improve reproducibility.

- **Efficiency comparison with MambaIC is partially confounded by model scale.** CMIC (69M params, 2.39 TFLOPs) is substantially smaller than MambaIC (157M params, 5.56 TFLOPs). While it is fair to report that CMIC is both better and more efficient, the paper's attribution of efficiency gains to the single-scan design is not fully isolated — some fraction of the FLOPs and parameter reduction stems from architectural differences beyond the scan strategy. The paper does not overclaim this point, but the comparison would be stronger with a MambaIC variant matched for parameter count.

### Trivial

- The abstract states GPP "overcomes the sequential dependency," which slightly overstates the mechanism — the hidden state remains causal; only the readout is conditioned on global priors. The main text uses more measured language ("mitigates," "relaxes"), so this is a minor phrasing inconsistency.

## Nice-to-Haves

- Reporting per-image BD-rate standard deviation on Kodak (24 images) would give a better sense of result reliability, though omitting this is standard practice in the LIC literature.
- A quantitative clustering quality metric (e.g., intra-cluster vs. inter-cluster variance) alongside the qualitative Figure 10 visualizations would further support the clustering claims.
- The paper notes that CAM in the entropy model yields negligible gains — a brief discussion of why (e.g., entropy modeling may not benefit from content-adaptive scanning in the same way the transform does) would add insight.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Harsh critic: "Non-differentiable token permutation is a fundamental technical gap — the training procedure is underspecified and its soundness is not established."** REMOVED as fatal/major. The EMA codebook update is a well-established technique (VQ-VAE, VQ-GAN, and many successors). Token features are not detached — they flow through the SSM and receive gradients from the loss, so the features that determine cluster quality ARE trained end-to-end. The centroids track the evolving feature distribution via EMA. This is a clarity issue (the paper should state that tokens are not detached), not a soundness flaw. Downgraded to Minor.

2. **Harsh critic: "No statistical variability reported — makes it difficult to judge reliability on Kodak."** MOVED to Nice-to-Haves. Reporting BD-rates without confidence intervals is universal practice in the LIC literature; virtually every paper in Table 1 follows this convention. Applying a different field's standards here is scope creep.

3. **Harsh critic: "Training details missing — crop size, epochs, LR schedule, batch size."** REMOVED. The parser strips appendices; these details are explicitly deferred to the appendix (Section 4.1 references Appendix for additional details). The paper does state key hyperparameters: Adam optimizer, initial LR of 10⁻⁴, λ values, channel dimensions, block counts, cluster count K=64, window size=8, and K-means iterations T=5.

4. **Harsh critic: "Interaction between EMA codebook update and batch size deserves comment."** REMOVED. This is an implementation detail that does not affect the paper's contributions or claims.

5. **Harsh critic: "Whether centroids are shared across CAM blocks not discussed."** REMOVED — factually incorrect. The paper explicitly states: "Each CAM block holds its own cluster centroids" (Section 3.3, paragraph on codebook initialization) and "Each CAM block maintains and updates its own codebook of cluster centroids" (same section).

6. **Strength Finder: "This paper addressed an important problem" type strengths.** REMOVED as generic/superficial. Only concrete, evidence-backed strengths retained.

## Novel Insights

The ERF-based analysis of non-causality (Figure 9) is a genuinely insightful contribution beyond the method itself. By visualizing the effective receptive field of a single Mamba layer with and without CTP/GPP, the paper provides a clear, intuitive diagnostic for understanding how these mechanisms alter the SSM's information flow. The observation that a vanilla Mamba layer's ERF stops exactly at the scan midpoint (column b), that GPP enables ERF beyond the causal boundary (column c), and that CTP reshapes the ERF away from raster patterns toward semantic structures (columns d–e) is a compelling visual argument that could inform future SSM designs beyond compression.

## Suggestions

- Add a random-permutation baseline in the CTP ablation to isolate the benefit of content-adaptive ordering from merely breaking the raster scan.
- Compare GPP against a simple global-average-pooling prompt to demonstrate the value of the cluster-tied dictionary.
- Add one sentence clarifying that token features are not detached before the permutation step, so gradients flow through the SSM back to the analysis transform.
- Tone down "overcomes the sequential dependency" in the abstract to "mitigates" or "relaxes" to match the main text.

## Score and Decision

**Calibration anchors:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| MambaVC (KgJwbsfN7G) | 4.80 | R1 | CMIC has substantially more novelty (CTP+GPP vs. applying VSS blocks), stronger SOTA results, and far better ablations. CMIC is clearly superior. |
| FTIC (HKGQDDTuvZ) | 6.00 | R2 | Both are strong LIC papers with novel mechanisms and SOTA results. CMIC has more comprehensive ablations (structure comparisons, ERF diagnostics, cluster visualizations), better BD-rate margins, and addresses a more fundamental architectural limitation. CMIC is clearly stronger. |
| Spatial-Mamba (iDe1mtxqK5) | 7.00 | R1 | Spatial-Mamba has broader task coverage and theoretical analysis unifying Mamba with linear attention. CMIC has deeper domain-specific innovation with two complementary mechanisms. CMIC's missing simpler-baseline ablations put it slightly below Spatial-Mamba's thoroughness. |
| Autoregressive Mamba Pretraining (PQpvhUrA1C) | 5.75 | R2 | Different task (classification pretraining vs. compression). CMIC has stronger domain results. |
| ElasticTok (tFV5GrWOGm) | 6.00 | R2 | Different task. Both have adaptive token mechanisms. Comparable quality level. |

**Round 1 bracket:** 4.80–7.00, narrowed to 6.0–7.0 based on comparison with FTIC and Spatial-Mamba.

**Round 2 narrowing:** CMIC is clearly above FTIC (6.00) — more novelty, better ablations, stronger results. It is slightly below Spatial-Mamba (7.00) — Spatial-Mamba has theoretical depth and broader task validation, while CMIC has a moderate gap (missing simpler baselines). **Final score: 6.5.**

The paper makes a genuine contribution with two well-motivated novel mechanisms, achieves clear SOTA results, and provides thorough empirical validation. The weaknesses are real but addressable — none threaten the core claims.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>