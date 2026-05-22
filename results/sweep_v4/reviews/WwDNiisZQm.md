Now I have all the information I need. Let me construct the final review.

## Summary

This paper introduces Content-Aware Mamba (CAM), a state-space model for learned image compression that replaces fixed raster scans with two novel mechanisms: (1) **Content-Adaptive Token Permutation (CTP)**, which clusters latent tokens by feature similarity and reorders the sequence so content-correlated tokens become contiguous regardless of spatial location; and (2) **Global-Prior Prompting (GPP)**, which injects sample-specific prompts derived from clustering centroids into the SSM's output projection to relax strict causality without multi-directional scanning. The resulting model, CMIC, is evaluated on Kodak, Tecnick, and CLIC, achieving BD-rate savings of 15.91%, 21.34%, and 17.58% over VTM-21.0 with moderate complexity (69M params, 2.39 TFLOPs).

## Strengths

- **Two clean, well-ablated architectural innovations.** CTP and GPP are both clearly motivated and individually validated. Table 2 shows that CTP alone yields 1.8%–2.4% BD-rate reduction and GPP alone yields 0.5%–1.4% across three datasets. The combined gain (2.7%–3.6%) is additive, demonstrating complementarity. Each component is also negatively ablated (removing it from the full model causes a clear drop), confirming necessity.

- **Strong rate-distortion performance with favorable efficiency.** CMIC outperforms prior Mamba-based LIC models (MambaVC, MambaIC) and leading transformer-based models (FTIC, TCM-L) in terms of BD-rate while maintaining substantially lower parameter count, FLOPs, and memory than MambaIC (e.g., 69M vs. 157M params, 4.44 GB vs. 20.32 GB peak memory). The efficiency claim is supported by concrete numbers in Table 1 and throughput ablations in Table 3.

- **Compelling ERF and clustering visualizations.** Figures 7–9 show that CMIC achieves substantially broader and more content-adaptive effective receptive fields than prior models. Figure 10 demonstrates that the learned codebook clusters semantically meaningful regions (e.g., red doors, sky, feathers). These visualizations provide interpretable evidence connecting the proposed mechanisms to their intended effects.

- **Thorough ablation and analysis.** The paper ablates cluster count K (Table 6), compares CAM against alternative blocks (Conv, 2D Mamba, Attention-only; Table 4), and analyzes dynamic activation patterns across datasets (Table 5), giving a clear picture of design decisions.

## Weaknesses

### Fatal
None.

### Major

None. The main concerns raised by reviewers do not rise to the level of major flaws under field standards.

### Minor

- **Cross-paper baseline comparison is the field standard but unacknowledged.** The headline SOTA claim relies on BD-rate numbers taken from original publications (MambaVC trained on CLIC/ImageNet splits, FTIC on different data, etc.) while CMIC is trained on Flickr2W. This practice is standard in learned image compression — virtually every ICLR/CVPR paper in this area does the same — but the paper does not acknowledge this limitation. The internal ablation (Table 2) convincingly validates CTP and GPP under controlled conditions, so the core contribution stands. However, the SOTA claim would be strengthened by noting the caveat or retraining the most direct competitors (MambaVC, MambaIC) on Flickr2W.

- **Gradient flow through hard clustering is not specified.** The paper forms a one-hot assignment matrix Γ via argmax (Algorithm 1, line 4), then writes P = ΓU (line 186). It states that the linear projection 𝒜 is "differentiable and trained end-to-end," but does not explain how gradients propagate through the non-differentiable Γ. A straight-through estimator is standard in VQ-VAE practice and likely what is used here, but the paper should state this explicitly for reproducibility.

- **Intra-cluster token ordering is unspecified.** The permutation π groups all tokens of cluster 1, then cluster 2, etc. (line 131), but the ordering of tokens *within* a cluster is not defined. Since the SSM processes tokens sequentially, this ordering could affect behavior, and the paper should clarify whether it is original raster order, random, or based on some criterion.

### Trivial

- No multiple-seed variance or confidence intervals are reported. This is standard practice in the LIC field (single runs are the norm), so it is not a weakness per se, but it is worth noting that the reported BD-PSNR differences against FTIC (e.g., 0.15 dB on Kodak) are small enough that readers cannot assess run-to-run variability.
- The Flickr2W dataset size is not stated in the main paper.

## Nice-to-Haves

- A controlled experiment perturbing future tokens in scan order to directly measure whether global information is actually used (beyond the ERF evidence) would strengthen the non-causality argument.
- Comparison against other content-adaptive methods for LIC (e.g., SegPIC, the CNN-clustering approach of Zhang et al. 2024b) could better contextualize the contribution within the content-adaptive sub-area.

## Removed Points

These points were flagged by reviewers but are removed after cross-checking against the paper:

1. **"Uncontrolled baseline comparison is a structural/fatal flaw"** — This overstates the issue. Cross-paper comparison with numbers taken from original publications is the standard practice in LIC research (as seen in every paper in Tables 1 of MambaVC, FTIC, MLIC++, ELIC, etc.). The paper's ablation studies (Table 2) are fully controlled and convincingly validate the contributions. The SOTA claim, while relying on the standard comparison, would benefit from a caveat but is not invalidated.

2. **"No empirical evidence to support diagnosis before proposing solution"** — The claim that "vanilla Mamba's content-agnostic, causal scan is suboptimal" is validated by the baseline model in Table 2 (the "no CTP, no GPP" row), which indeed performs worst. The paper presents the problem evidence as an integral part of the solution evaluation.

3. **"The expressiveness of the prompt is limited to what A can extract from fixed centroids"** — The mapping 𝒜 is differentiable and jointly optimized with the rate-distortion loss, so the network can learn to extract useful information from any centroid distribution. This is a standard feature learning setup, not a limitation.

4. **"Missing implementation details (inference engine, batch size for latency)"** — The paper states latency is measured on A100 GPUs for 2K-resolution images. Given that the appendix (A.14) is referenced for additional encoding latency details, this level of specification is adequate for the main paper.

5. **"Missing related works"** — Cannot be verified without external sources.

6. **All typographical/formatting nitpicks** — Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The two-reviewer synthesis confirms the paper's own framing: CTP and GPP are complementary strategies addressing two distinct weaknesses of Mamba (content-agnostic scanning and strict causality), and their individual efficacy is supported by clean ablations. The main insight from the reviews is that the paper would benefit from explicitly acknowledging the field-standard baseline comparison caveat, which would preempt a common criticism without weakening its contribution.

## Suggestions

1. **Explicitly acknowledge the baseline comparison limitation** in the paper (e.g., "BD-rate numbers for competing methods are from their original publications, which may use different training data; our internal ablation in Table 2 is fully controlled"). This adds 2–3 sentences and preempts the most common critique.

2. **Clarify gradient flow through hard clustering.** Add one sentence stating the approach (e.g., "the gradient of the loss w.r.t. the assignment matrix Γ is copied through the argmax operation via a straight-through estimator, following VQ-VAE [Oord et al., 2017]").

3. **Specify intra-cluster ordering.** State the ordering convention used when grouping tokens within each cluster (e.g., "tokens within a cluster retain their original raster-scan relative order").

4. **Report Flickr2W dataset size** (number of images) in the main paper for completeness.

## Score and Decision

**Calibration anchors (all retrieved in a single batch):**

| Path | Avg Score | Comparison to CMIC |
|------|-----------|-------------------|
| KgJwbsfN7G.md (MambaVC) | 4.80 | Weaker — applies VSS block without compression-specific design; considered low novelty |
| iDe1mtxqK5.md (Spatial-Mamba) | 7.00 | Stronger — evaluates on multiple vision tasks (cls/det/seg); CMIC has more novel compression-specific components but narrower scope |
| Cy5v64DqEF.md (Idempotence) | 7.50 | Stronger — theoretically grounded new paradigm; different contribution type |
| U67J0QNtzo.md (Disentangled Training) | 7.50 | Stronger — extensive cross-arch generalization, well-controlled experiments; CMIC has comparable innovation in its own domain |
| RmmrHEH6Nx.md (GroupMamba) | 3.00 | Weaker — limited novelty (SE-like module), unfair comparisons |
| gIrVoQEDQv.md (Unraveling NCA) | 3.40 | Much weaker — insufficient experiments, compares only against JPEG/WebP |
| 44cMlQSreK.md (NeuroQuant) | 7.20 | Different sub-area (video coding quantization); more thorough evaluation across architectures |
| PQpvhUrA1C.md (Autoregressive Mamba) | 5.75 | Comparable novelty level — explores Mamba pretraining; CMIC has stronger compression-specific design and ablation |
| GmE8ovvXaJ.md (MambaMatcher) | 5.50 | Different task (semantic correspondence); comparable technical depth |

**Positioning:** CMIC is significantly stronger than MambaVC (4.80) and GroupMamba (3.00) — it has genuine compression-specific innovations (CTP, GPP) that are well-ablated, not a straightforward architecture transplant. It is somewhat weaker than Spatial-Mamba (7.00) and the high-scoring LIC papers (7.20–7.50) in terms of evaluation breadth or theoretical depth, but its contributions are clearly original and well-supported by controlled experiments. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>