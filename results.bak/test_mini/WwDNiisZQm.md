Now I have sufficient calibration data. Let me write the final consolidated review.

Here's my bracket analysis:
- Round 1 bracketing: The paper is clearly stronger than MambaSIC (4.0) and SF-Mamba (4.5), and slightly stronger than SSM Neural Rep (5.0). It's somewhat weaker than the compression papers scoring 6.0. Narrow bracket: **5.0–6.0**.
- Round 2 narrowing: Fore-Mamba3D (5.5, accepted poster) offers a fair comparison—similar mix of genuine contribution with some claims that exceed what's fully demonstrated. CMIC has stronger empirical validation but a moderately overstated claim. Score: **5.5**.

---

## Summary

This paper proposes Content-Aware Mamba (CAM) for learned image compression, addressing two limitations of standard Mamba for this task: its rigid content-agnostic raster scan order and its strict causal processing. The authors introduce (1) **Content-Adaptive Token Permutation (CTP)** — a codebook-based clustering strategy that reorders tokens so that semantically similar ones become contiguous in the scan sequence, and (2) **Global-Prior Prompting (GPP)** — a mechanism that injects cluster-conditioned prompts into the SSM output projection. Their CMiC model achieves strong rate-distortion performance across Kodak, Tecnick, and CLIC datasets, surpassing prior Mamba-based LIC models by substantial margins while using fewer parameters and FLOPs.

## Strengths

1. **Content-Adaptive Token Permutation is a well-motivated and clearly effective contribution.** The clustering-based reordering is rigorously described (Section 3.3, Algorithm 1), with EMA-stabilized training and efficient inference. Ablations (Table 2) show CTP alone yields 1.8–2.4% BD-rate improvement, and Figure 10 convincingly demonstrates that tokens sharing visual semantics (red doors, sky, feathers) are grouped together. This directly addresses the genuine limitation of Mamba's fixed raster scan for image compression.

2. **State-of-the-art rate-distortion performance with favorable efficiency.** On Kodak, Tecnick, and CLIC, CMiC achieves BD-rate savings of -15.91%, -21.34%, and -17.58% vs. VTM-21.0 (Table 1). It surpasses the best prior Mamba-based model (MambaIC) by 2.36–6.48% while reducing parameters by 56% (157M → 69M), FLOPs by 57%, and memory by 78%. The throughput of 22.05 samples/s (Table 3) ≈2–3× faster than prior Mamba-based LIC models.

3. **Clean ablations isolate the contributions of each component.** Table 2 systematically shows CTP (+1.8–2.4%), GPP (+0.5–1.4%), and their combined effect (+2.7–3.6%). Table 4 compares CAM blocks against Conv, 2D Mamba, attention-only, and CAM-only variants — all fair comparisons that support the design choices.

4. **Effective receptive field analysis is thorough and informative.** Figures 7–9 compare ERFs across nine LIC models, demonstrating that CMiC achieves broader, more content-adaptive receptive fields than CNN-, Transformer-, and Mamba-based competitors. The per-image ERF visualizations (Figure 8) showing semantic alignment (hair in Kodim17, shoreline in Kodim16) are compelling evidence of content awareness.

## Weaknesses

### Fatal
None.

### Major

1. **The claim that Global-Prior Prompting "relaxes strict causality" is not supported by the described mechanism.** The paper states GPP allows the SSM to "see beyond" the strictly causal scan. However, in the equation `O_i = (C + P)h_i + Dx_i`, the hidden state `h_i` depends only on tokens up to position `i`, and the prompt `P_i` depends only on token `x_i` (via cluster assignment against fixed centroids) and the learned dictionary. There is no computational path from future tokens to `O_i`. The system remains strictly causal. The ERF evidence in Figure 9(c) — non-zero activations beyond the causal boundary — is inconsistent with causal SSM dynamics and requires explanation. If the ERF is computed through the entire network (not a single layer), or if soft clustering creates a gradient path through centroids, this should be explicitly stated. As written, the paper claims a property that doesn't follow from the mathematics. **This is a central claim (contribution item 2).**

   *However, this does not invalidate the paper.* GPP still provides real and measured gains (0.5–1.4% BD-rate, Table 2) and is a sensible design — it functions as cluster-conditioned semantic modulation of the SSM output, even if it is not non-causal. The authors should reframe this contribution accordingly.

### Minor

1. **The "state-of-the-art" claim is slightly imprecise on Kodak.** Table 1 shows MLICv2 achieves -16.16% vs. CMiC's -15.91% on Kodak. While CMiC wins on the other two datasets and has better overall efficiency, the paper's framing ("state-of-the-art") would benefit from acknowledging this nuance rather than stating uniform superiority.

2. **Gradient flow through hard clustering assignments is not discussed.** The paper uses argmax-based hard assignment (non-differentiable) but does not explain how gradients are propagated back to the encoder features that determine cluster assignments. The standard straight-through estimator or gradient-through-indexing approach should be acknowledged. This is a standard concern and addressing it briefly would improve clarity.

3. **The entropy model contribution is not independently ablated.** The paper mentions adding CAM to the entropy model gave negligible gains (Section 4.5), but the entropy model itself is modified from SCTX with depthwise conv + gated MLP. An ablation separating entropy model improvements from transform improvements would help isolate the source of gains.

### Trivial
None.

## Nice-to-Haves
- Reporting BD-rate variance or confidence intervals across multiple training seeds, especially for the small Kodak dataset (24 images).
- Quantitative comparison with Zhang et al. (2024b), which also uses clustering to rearrange features for compression, beyond the brief discussion in Section 2.3.
- Ablation on the cluster number K with a finer grid (values between 32, 64, 128).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The comparison with SOTA is unfair"** (not from reviewers — not present). No issue here.
- **Harsh critic: "Statistical significance: BD-rate without variance."** While technically true, single-run evaluation is the norm for large-scale LIC benchmarks. Demoting to nice-to-have.
- **Harsh critic: "The paper should discuss why the ERF in Figure 9(c) shows non-zero values."** This is already encompassed in the Major weakness above.
- **Strength Finder strength #3: "Global-prior prompting relaxes strict causality. Figure 9..."** This conflicts with the verified weakness and is removed — GPP does not demonstrably relax causality.
- **Strength Finder strengths about the problem being important.** These are generic and removed. Concrete strengths (RD performance, ablations, ERF analysis) are retained.
- **Harsh critic: "Missing related works / more comparison with Zhang et al."** I cannot evaluate missing references; this is removed per instructions.
- **Harsh critic formatting nitpicks, grammar/style concerns** — removed per instructions.

## Novel Insights

The most insightful observation is the asymmetry between the two reviewers: the harsh critic correctly identifies that the GPP non-causality claim is unsupported by the mathematics, while also acknowledging the empirical benefits. This reveals an interesting pattern where a method can provide real, measurable improvements (0.5–1.4% BD-rate) via a mechanism that is less exotic than claimed (cluster-conditioned modulation rather than non-causal processing). The ERF visualization showing non-causal patterns despite the causal mechanism merits further investigation — it may be an artifact of soft clustering during visualization, multi-layer gradient flow, or a genuine implementation detail not captured by the paper's equations. Resolving this discrepancy would strengthen both the paper and the community's understanding of how prompting interacts with SSM causality.

## Suggestions

1. **Reframe the GPP contribution.** Drop or substantially revise the "relaxes strict causality" language. Describe GPP as cluster-conditioned semantic modulation that injects dataset-level prior knowledge into the SSM output, enhancing global awareness through the learned prompt dictionary. The empirical gains remain valuable without this framing.
2. **Clarify the ERF computation in Figure 9.** Explain whether the ERF is computed on a single layer or the whole network, and whether soft clustering creates gradient paths that could produce the observed non-causal patterns. If the scan order in (c) is not the standard raster (e.g., content-adapted via some mechanism), state this explicitly.
3. **Acknowledge the gradient handling for hard clustering.** Briefly explain how gradients flow through the argmax assignment in CTP (e.g., straight-through estimation, or treating the permutation as a deterministic, differentiable indexing operation).

## Score and Decision

**Calibration Anchors Used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| MambaSIC (0dHrYUd17W.md) | 4.00 | R1 | Weaker method novelty and empirical results; CMIC has stronger architectural contributions |
| SSM Neural Rep (R5xBLfD9Dv.md) | 5.00 | R1 | Similar ballpark; CMIC has stronger empirical validation but more questionable central claim |
| MemMamba (jPYJuvzof2.md) | 4.00 | R1 | Weaker; limited novelty relative to CMIC's concrete application |
| SF-Mamba (X4KsowemNB.md) | 4.50 | R2 | Similar topic (Mamba causality); SF-Mamba was rejected, CMIC has stronger empirical case |
| S3Mamba (42gPoLZLQB.md) | 4.50 | R2 | Weaker empirical validation |
| Fore-Mamba3D (e4t1775UJ1.md) | 5.50 | R2 | Best comparison anchor; both have incremental components + strong results, accepted poster |
| CoTAM (YDRoTtmXu1.md) | 6.00 | R2 | Stronger novelty/different sub-area; CMIC doesn't quite reach this level |

**Round 1 bracket:** 5.0–6.0  
**Round 2 narrowing:** Fore-Mamba3D (5.5, accepted poster) provides the closest analog — a paper with genuine contributions and strong empirical validation, but with some claims that modestly exceed what is fully demonstrated. CMIC sits at a similar level: real contributions in CTP and overall architecture, thorough experiments, but the unsupported non-causality claim for GPP is a tangible weakness that prevents it from reaching the 6.0 tier.

**Final Score: 5.5**  
**Decision: Accept (Poster)**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>