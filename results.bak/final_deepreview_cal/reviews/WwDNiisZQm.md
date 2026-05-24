Now let me synthesize the final review.

## Summary

This paper introduces Content-Aware Mamba (CAM) for learned image compression. It addresses two fundamental limitations of standard Mamba applied to 2D images: (1) the content-agnostic raster scan that separates spatially distant but semantically similar tokens, and (2) strict causality that prevents tokens from accessing global context. The paper proposes Content-Adaptive Token Permutation (CTP), which uses a shared codebook with EMA-updated centroids to cluster tokens by feature similarity and reorder the scan sequence accordingly, and Global-Prior Prompting (GPP), which injects sample-specific global information into the SSM output matrix via a redundancy-aware prompt dictionary tied to the cluster centroids. The combined CMIC model achieves SOTA RD performance across Kodak, Tecnick, and CLIC, surpassing VTM-21.0 by 15.91%, 21.34%, and 17.58% BD-rate respectively, while maintaining moderate complexity.

---

## Strengths

- **Two novel, well-motivated mechanisms directly targeting known Mamba limitations.** CTP replaces the rigid content-agnostic scan with feature-space reordering (Table 2 shows 1.8–2.4% BD-rate improvement from CTP alone), and GPP relaxes strict causality without multi-directional scans (0.5–1.4% improvement from GPP alone). Both mechanisms are cleanly described (Algorithm 1, Section 3.4) and justified against alternatives (e.g., multi-directional scanning's 4× overhead).

- **SOTA RD performance with clear evidence.** CMIC achieves 15.91%/21.34%/17.58% BD-rate savings over VTM-21.0 on Kodak/Tecnick/CLIC (Table 1), surpassing prior Mamba-based LIC methods (MambaVC by 7–10%, MambaIC by 2–6%) as well as Transformer-based competitors (FTIC, TCM-L). The RD curves (Figures 4–6) show consistent gains across all bitrates. These results are supported by BD-PSNR and MS-SSIM metrics.

- **Comprehensive and informative evaluation.** The paper goes beyond standard RD tables with: thorough ablations isolating CTP and GPP (Table 2), architecture comparisons (Table 4), throughput/latency/memory analysis (Tables 1, 3), cluster-number sensitivity (Table 6), and cluster activation analysis (Table 5). The ablation on K values (Table 6) shows the model is robust to this hyperparameter.

- **Strong visual evidence for claimed mechanisms.** ERF visualizations (Figures 7–9) directly demonstrate that CTP reshapes the receptive field toward semantically relevant regions and that GPP extends influence beyond the causal scan boundary. Figure 9's single-layer ERF ablation showing strict raster-scan causality without GPP/CTP → global coverage with both is particularly convincing. Cluster visualizations (Figure 10) confirm that tokens with similar visual content are grouped together.

- **Efficiency advantage with principled design.** CMIC reduces parameters by 56%, FLOPs by 57%, latency by 39%, and peak memory by 78% compared to MambaIC, while achieving better RD performance. The prompt dictionary is tied to clustering centroids (via a learnable projection) rather than being a free learnable matrix, giving prompts explicit semantic meaning tied to redundancy distributions—a principled improvement over prior prompt-pool approaches.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The ablation does not include a control for "any reordering" vs. semantic grouping.** The baseline is raster-scan order; CTP groups similar tokens together. Without a control condition in which tokens are permuted randomly or by a simple non-semantic heuristic (e.g., sorting by L2 norm), the paper cannot fully exclude the possibility that breaking the raster-scan order alone—rather than the specific semantic grouping—contributes to the gain. This does not invalidate the core contribution (CTP clearly works and the cluster visualizations confirm semantic grouping), but adding such a control would strengthen the causal claim that "feature-space proximity" rather than "any reordering" drives the improvement.

- **The clustering mechanism uses non-gradient updates.** Centroids are updated via EMA of hard cosine-similarity K-means assignments rather than end-to-end gradient flow from the rate–distortion loss. The paper acknowledges this ("this non-gradient update process allows the codebook to encapsulate knowledge of the dataset-level feature distribution," Section 3.3), and the approach works well empirically (CTP yields 2% BD-rate gains). However, a fully differentiable alternative (e.g., Gumbel-Softmax assignments) could potentially yield larger gains, and the paper does not discuss whether this design choice is a deliberate trade-off for stability or a limitation.

- **No discussion of sensitivity to clustering initialization.** Centroids are initialized by segmenting the first batch. The paper does not study whether different initializations lead to similar final centroids (e.g., via centroid cosine similarity across seeds). Given that the clustering directly determines the token permutation, a brief initialization sensitivity study would increase confidence.

### Trivial

- Inconsistent capitalization of the model name: "CMiC" appears in figure captions and the abstract, while "CMIC" is used in the table and most of the main text. Should be unified.

---

## Nice-to-Haves

- A brief summary of the Appendix A.3 result (CAM blocks not beneficial in the entropy model) would be useful in the main text to preempt reader questions.
- A comparison with a learned, differentiable soft clustering variant (e.g., Gumbel-Softmax) would be informative, though not required.

---

## Removed Points

These points were flagged in the reviews but are removed per the filtering rules:

- *"The entropy model ablation is in the appendix and unavailable"* — The parser strips appendix content; the appendix exists in the original submission. Removed per the rule about missing appendix content.
- *"Criticism about model availability / reproducibility of cited entities"* — None present in the original inputs.
- *Strength Finder claims about "important problem" or generic strengths* — Removed as generic/superficial. The core strengths listed above are retained.
- *"The paper should compare with more models"* — The paper already compares with 13+ methods including both Mamba-based and Transformer-based SOTA. This is sufficient.

---

## Novel Insights

None beyond the paper's own contributions. The core insight—that content-adaptive token permutation via codebook-based clustering combined with global-prior prompting effectively addresses Mamba's limitations for compression—is clearly articulated by the authors themselves.

---

## Suggestions

1. Add a random-permutation baseline to the ablation (Table 2) to directly test whether the CTP gain comes from semantic grouping or from breaking the raster-scan order.
2. Add a brief initialization sensitivity study (e.g., cosine similarity of final centroids across seeds).
3. Unify model name capitalization as "CMIC" throughout.
4. Briefly mention the entropy-model finding (CAM not beneficial there) in the main text.

---

## Score and Decision

### Calibration

**Round 1 — Bracketing.** Three queries targeting different score bands on Mamba/LIC topics:

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| `cagNCwQEEN` — MLLM with SSM | 3.40 | R1 (low) | Much weaker; different domain, serious flaws |
| `RmmrHEH6Nx` — GroupMamba | 3.00 | R1 (low) | Much weaker; instability/inefficiency issues |
| `KgJwbsfN7G` — MambaVC | 4.80 | R1 (mid) | Direct competitor; simpler (just applied VSS blocks), weaker results, limited novelty. CMIC is clearly stronger. |
| `iDe1mtxqK5` — Spatial-Mamba | 7.00 | R1 (mid) | Similar-strength Mamba-for-vision paper; novel mechanism, accepted. CMIC comparable or slightly stronger in evaluation depth. |
| `Tv36j85SqR` — Lattice Transform Coding | 7.20 | R1 (mid) | Strong compression paper, accepted. Different contribution type (theoretical/quantization). |
| `CxXGvKRDnL` — Progressive Compression | 8.00 | R1 (high) | Very strong; diffusion-based compression, accepted. CMIC not at this level. |

**Round 1 bracket:** Between 5.5 and 7.5.

**Round 2 — Narrowing.** Queries inside the bracket:

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| `bsnRUkVn63` — Test-time Adaptation for IC | 6.00 | R2 | Solid but incremental; CMIC has stronger novelty. |
| `BGkqypmGvm` — 2D SSM Layer | 6.00 | R2 | Different domain; CMIC is stronger in compression-specific contributions. |
| `qtTIP5Gjc5` — Demystifying Token Dynamics | 7.50 | R2 | Strong theoretical paper; CMIC is more applied but comparably rigorous in empirical evaluation. |
| `MvEkN2ejZ1` — MamBEV | 6.60 | R2 | BEV perception; CMIC is at least as strong within its domain. |

**Final placement:** CMIC is clearly stronger than MambaVC (4.80) and the proxy-IC papers (~6.0). Compared to Spatial-Mamba (7.00, accepted) — the closest analog in terms of proposing a novel Mamba modification for vision — CMIC is at least comparable: both propose targeted architectural innovations, both provide thorough evaluation, and CMIC has more extensive visual evidence (ERF per-image, cluster activation). The weaknesses are minor (missing random-permutation control, non-gradient clustering) and do not threaten the core claims. The paper sits in the 7.0 band.

**MY FINAL SCORE: 7.0**
**MY FINAL DECISION: Accept**