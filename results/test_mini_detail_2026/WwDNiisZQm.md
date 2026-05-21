Now I have all the information I need. Let me construct the final consolidated review.

**Round 1 Bracket**: The paper sits between the weak band (2.5–3.0 — MambaMatch, TVMamba, all withdrawn/rejected) and the strong band (8.0 — unrelated topics). It clearly belongs in the middle band (4.0–5.0+).

**Round 2 Anchors**: 
- MambaSIC (avg 4.0, withdrawn): weaker novelty, engineering-oriented 
- SF-Mamba (avg 4.5, reject): weaker empirical results, novelty concerns
- S3K neural representations (avg 5.0, accept poster): comparable to slightly stronger
- Hierarchical coding (avg 5.5, accept poster): similar tier, CMIC has more architectural novelty
- SP-MoMamba (avg 6.0, reject) and CoTAM (avg 6.0, accept poster): different subfields

**Final position**: CMIC is clearly above the 4.0–4.5 Mamba papers (stronger novelty, better evaluation) and comparable to or slightly above the 5.5 accepted-poster LIC paper. The weaknesses are real but minor. Score is well-calibrated at **6.0**.

---

## Summary

This paper introduces Content-Aware Mamba (CAM) for learned image compression (LIC). It identifies two key limitations of Mamba-style SSMs for image compression — content-agnostic raster scanning and strict causality — and proposes two mechanisms to address them: (1) Content-Adaptive Token Permutation (CTP), which clusters tokens by feature similarity and reorders the scan sequence accordingly, and (2) Global-Prior Prompting (GPP), which injects sample-specific global priors into the SSM's output projection to relax strict causality without multi-directional scans. The resulting model (CMIC) achieves competitive RD performance on Kodak, Tecnick, and CLIC while reducing parameters by 56%, FLOPs by 57%, and peak memory by 78% compared to the prior best Mamba-based model (MambaIC).

## Strengths

1. **Clear, well-motivated architectural innovation.** The paper identifies two genuine limitations of Mamba for image compression — content-agnostic scanning and strict causality — and proposes CTP and GPP as targeted remedies. The codebook-based clustering (Sec. 3.3) is a practical alternative to per-sample online K-Means, and the prompt dictionary tied to centroids (Sec. 3.4) is a principled way to inject global information. The connection between mechanism and limitation is explicit throughout.

2. **Strong empirical evidence for the two core mechanisms.** Table 2 shows that CTP alone improves BD-rate by 2.0%/2.4%/1.8% on the three datasets, GPP alone by 0.5%/1.4%/0.5%, and the combination yields super-additive gains (2.7%/3.6%/2.7%). The ERF visualizations in Fig. 9 directly confirm that GPP expands the receptive field beyond the causal cutoff and that CTP reshapes it toward semantically correlated regions — mechanistic evidence that goes beyond simple metric reporting.

3. **Favorable complexity-performance trade-off.** CMIC achieves competitive RD performance while being significantly more efficient than prior Mamba-based models: 56% fewer parameters, 57% fewer FLOPs, 39% lower latency, and 78% lower peak memory than MambaIC (Table 1). The throughput ablation (Table 3) confirms that CTP and GPP add only ~5% overhead. This makes the contribution practically relevant, not just an accuracy improvement.

4. **Thorough ablation study and interpretability analysis.** The paper ablates component contributions (Table 2), alternative block structures (Table 4), cluster counts (Table 6), and provides ERF visualizations (Figs. 7–9) that concretely demonstrate content-adaptivity. The per-image ERF analysis (Fig. 8) showing content-correlated activation patterns — versus the isotropic fields of competing methods — is particularly compelling.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical significance or variance reporting.** All BD-rate results are point estimates with no confidence intervals, error bars, or multi-seed training. Given that the best competing method (MLICv2, 84.3M params) beats CMIC on Kodak by 0.25% BD-rate (-16.16% vs -15.91%, Table 1), it is unclear whether this difference (or other head-to-head gaps of similar magnitude) is meaningful or within training noise. For an archival evaluation, at minimum the main result should include mean ± std over multiple seeds.

2. **Overclaiming "state-of-the-art" without qualification.** The abstract and Section 4.3 state that CMIC achieves "state-of-the-art" performance and "consistently outperforms leading methods across all evaluated datasets." However, on Kodak, MLICv2 achieves -16.16% BD-rate versus CMIC's -15.91% — CMIC actually loses on that dataset. While CMIC wins convincingly on Tecnick (-21.34% vs -20.13%) and CLIC (-17.58% vs -15.79%), the unqualified phrasing overstates the result. The paper should acknowledge this gap and offer a reasoned explanation (e.g., Kodak's lower resolution may reduce the global modeling advantage).

### Minor

3. **Missing content-adaptive baseline (SegPIC).** SegPIC (Liu et al., 2024b), which also uses content-adaptivity (semantic masks + dynamic CNNs) for compression, is mentioned in Related Work (Sec. 2.1) but is not included in any experimental comparison. Since the paper's central claim is that content-adaptivity improves compression, comparing against the most directly related prior work would strengthen the evaluation.

4. **Non-differentiability of the clustering assignment not discussed.** The token permutation is based on hard argmax assignments (Sec. 3.3, Algorithm 1), but the paper does not explain how gradients flow through this operation during training. The centroid codebook is updated via EMA (non-gradient), and the prompt mapping A(·) is differentiable, but the hard assignment for the permutation itself is not addressed. While a straight-through estimator or detached assignment is standard practice, it should be stated explicitly.

### Trivial
None.

## Nice-to-Haves

- Reporting encoding latency separately from decoding latency would be useful for deployment characterization (the paper notes these are provided in Appendix A.14, which is stripped).
- Ablating the cluster count K on a higher-resolution dataset (CLIC or Tecnick) in addition to Kodak would increase generality.
- The entropy model ablation showing that CAM provides negligible benefit there (noted as in the appendix) is a useful negative result that could be mentioned in the main text.

## Removed Points

- **"Encoding latency not reported"** — The paper states "We also provide detailed encoding latency on A100 and RTX3090 GPUs in Appendix A.14" (Sec. 4.2, line 227). The critic missed this. REMOVED.
- **"Entropy model described only briefly"** — Figure 3 and Sec. 3.2 describe the entropy model architecture (SCTX-based with depthwise convolution and gated MLPs). The description is proportionate for a methods paper where the entropy model is not the main contribution. REMOVED as a weakness.
- **"No comparison with other Mamba variants"** — The paper already compares with MambaVC and MambaIC, and the "2D Mamba" variant is ablated in Table 4. This covers the relevant comparisons. REMOVED.
- **Strength Finder's generic claims about "importance of the problem"** — Dropped per filtering rules (generic, not specific to this paper's evidence).
- **Missing related works** — Per filtering rules, I cannot mention these.
- **Formatting nitpicks about figures** — Parser artifacts, not author errors.

## Novel Insights

The harsh critic's analysis surfaced a nuanced observation about the relationship between the two proposed mechanisms: CTP and GPP are not simply additive but exhibit super-additive interaction (the combined gain exceeds the sum of individual gains on all three datasets). This suggests that content-adaptive scanning and global prompting work synergistically — the prompt provides non-causal information that is especially useful once tokens are grouped by content similarity (because the prompt encodes global cluster-level statistics), and the permutation ensures that the scanning path aligns with the prompt's semantic grouping. This interaction insight is not explicitly discussed in the paper and could usefully inform future content-adaptive SSM designs.

## Suggestions

- Add multi-seed training (at minimum 3 seeds) for the main results and report mean ± std for BD-rate, or at minimum acknowledge the lack of variance as a limitation.
- Acknowledge the Kodak deficit against MLICv2 explicitly, with a reasoned explanation (e.g., image resolution, model capacity differences).
- Consider including SegPIC or another content-adaptive LIC method as a baseline. If the code is not publicly available, acknowledge the omission.
- State explicitly how the hard clustering assignments handle gradient backpropagation (straight-through estimator, detached assignment, or soft relaxation).

## Score and Decision

**Calibration Anchors (all rounds):**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| MambaMatch | 2.50 | R1 weak | SLAM feature matching; withdrawn/reject; much weaker contribution. CMIC is far stronger. |
| TVMamba | 3.00 | R1 weak | Mamba quantization; withdrawn/reject. CMIC is clearly stronger. |
| HG-Mamba | 3.00 | R1 weak | Laparoscopic desmoking; withdrawn/reject. Not comparable; CMIC has better evaluation. |
| MambaSIC | 4.00 | R1 mid | Stereo image compression; withdrawn/reject. Criticized as "engineering-oriented" with limited novelty. CMIC has stronger architectural contributions and evaluation. |
| S3Mamba | 4.50 | R1 mid | Super-resolution; withdrawn/reject. Criticized as "module replacement" with limited insight. CMIC has more novelty and stronger results. |
| SF-Mamba | 4.50 | R1 mid | Vision Mamba; reject. Criticized for limited novelty and marginal downstream gains. CMIC has clearer contributions. |
| S3K/SSM neural repr. | 5.00 | R1 mid | SSM for neural representations; accept poster. Comparable novelty but CMIC has more direct practical impact and stronger evaluations. |
| Hierarchical coding | 5.50 | R2 narrow | LIC with spectral regularization; accept poster. Similar venue tier; CMIC has more architectural novelty vs training-only contributions. |
| CoTAM (MLLM compression) | 6.00 | R2 narrow | Compression for MLLMs; accept poster. Different subfield but similar venue tier. |
| SP-MoMamba | 6.00 | R2 narrow | SSM for super-resolution; reject. Different task. |
| Mamba-3 | 7.00 | R2 narrow | SSM for language; accept oral. Foundational work; CMIC is not at this level. |

The paper makes a genuinely novel architectural contribution (not just module replacement or training tricks), is well-motivated, has strong empirical support including mechanistic evidence, and achieves competitive results with clear efficiency advantages. The identified weaknesses (lack of variance reporting and overclaiming relative to MLICv2) are real but manageable. The paper is strongest in the middle of the acceptance tier — not a top-oral, but a solid poster-level contribution that advances the state of the art in applying Mamba to learned image compression.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>