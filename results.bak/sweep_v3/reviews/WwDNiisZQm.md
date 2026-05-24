Now I have all the evidence needed. Here is the final consolidated review:

---

## Summary

This paper introduces Content-Aware Mamba (CAM) for learned image compression (LIC), addressing two fundamental limitations of standard Mamba-style SSMs for image tasks: (1) content-agnostic raster scans that ignore feature-space similarity between spatially distant tokens, and (2) strict causality that prevents each token from accessing global context. The authors propose Content-Adaptive Token Permutation (CTP), which uses codebook-based clustering to group semantically similar tokens into contiguous sequences before scanning, and Global-Prior Prompting (GPP), which injects sample-specific global priors into the SSM's output projection to relax causality without multi-directional scans. The resulting model (CMIC) achieves SOTA rate-distortion performance across Kodak, Tecnick, and CLIC datasets (BD-rate savings of 15.91%, 21.34%, and 17.58% vs. VTM-21.0) while requiring substantially lower computation than prior Mamba-based LIC models.

## Strengths

1. **Well-motivated and non-trivial technical novelty.** CTP and GPP are genuine, domain-specific innovations for Mamba-based compression, not a straightforward application of an existing backbone. CTP replaces the rigid raster scan with a content-adaptive ordering driven by feature-space clustering (Fig. 10, Table 5), and GPP anchors the prompt dictionary on the same clustering centroids (Eq. 2, line 184) rather than using a standalone learnable pool as in MambaIRv2. This explicit semantic grounding is the key distinction from prior work.

2. **SOTA RD performance with significantly lower complexity.** CMIC outperforms all prior learned methods on all three benchmarks (Table 1) while using 56% fewer parameters, 57% fewer FLOPs, 39% lower latency, and 78% less peak memory than the leading Mamba-based competitor MambaIC (Zeng et al., 2025). This efficiency-performance balance is the paper's strongest practical result.

3. **Thorough ablation and analysis.** Component ablations (Table 2) quantify the independent contributions of CTP (1.8–2.4% BD-rate improvement) and GPP (0.5–1.4%). Structure ablations (Table 4) compare against Conv, 2D Mamba, attention-only, and CAM-only alternatives, confirming that the hybrid design is optimal. Throughput analysis (Table 3) shows only ~5% training overhead from the proposed modules.

4. **Compelling qualitative evidence.** ERF visualizations (Figs. 7–9) provide direct visual proof that CMIC achieves substantially larger and more content-adaptive receptive fields than CNN, Transformer, and prior Mamba LIC models. The per-layer ERF analysis in Fig. 9 cleanly isolates the independent effects of CTP (breaking the raster-scan spatial pattern) and GPP (extending activations beyond the causal boundary). Cluster visualizations (Fig. 10) confirm that centroids capture semantically meaningful patterns (edges, textures, smooth regions) shared across images.

## Weaknesses

### Fatal
None.

### Major

1. **Unexplained gradient flow through discrete clustering operations.** The permutation π is built from argmax cluster assignments (Algorithm 1, line 4), which are non-differentiable. The centroids are updated via EMA (non-gradient). The paper states that "the mapping 𝒜(·) is differentiable" (line 186) but this only covers the centroid-to-prompt projection, not the assignment or permutation steps. The paper says it "draw[s] inspiration from VQ-VAE" (line 119), which uses straight-through estimation, but never explicitly states whether straight-through, stop-gradient, or another technique is used. Given that the model trains successfully to SOTA, some mechanism must be in place, and the features likely receive gradients through the SSM's processing of their reordered content (since PyTorch's gather/scatter indexing is differentiable for the gathered values). However, this is never clarified, which is a meaningful reproducibility gap. The authors should explicitly describe how gradients flow (or do not flow) through the discrete assignment and permutation, and whether any form of gradient approximation is used. (Note: this is not fatal — training clearly works — but the omission is substantial enough that a reader cannot fully reconstruct the training procedure from the paper alone.)

### Minor

2. **EMA decay λ is not specified.** Algorithm 1 includes λ as a hyperparameter, and the text states the centroids are updated via EMA, but the actual value of λ is never reported. This is a small but concrete omission that harms reproducibility.

3. **ERF analysis is qualitative only.** The paper claims a "significantly larger" receptive field (Figs. 7–8, line 304), and the visual evidence is compelling, but no quantitative metric (e.g., the radius capturing 95% of gradient magnitude, or relative coverage ratio) is provided to support this claim numerically.

4. **No limitations discussion.** The paper does not discuss any limitations. For example, the fixed codebook size (64 centroids) is an upper bound that might not generalize well to highly out-of-distribution images; the clustering itself depends on pretrained feature representations; and each CAM block stores its own codebook, which adds memory. A brief limitations paragraph would strengthen the paper.

5. **No clustering quality metric.** The visual cluster assignments in Fig. 10 are informative, but a quantitative measure (e.g., average intra-cluster cosine similarity or silhouette score) would substantiate the claim that the codebook learns "semantically meaningful visual features" (line 123).

### Trivial

6. **Inconsistent naming in Table 1.** The paper uses "MambaC" in Table 1 (line 218) and the accompanying text (line 231), while using "MambaIC" consistently in figure captions, the related work, and the reference to Zeng et al. (2025). This should be harmonized.

## Nice-to-Haves

- A comparison against a variant that replaces hard clustering with a soft (Gumbel-Softmax) relaxation would strengthen the methodological justification.
- Reporting confidence intervals or variance across multiple training seeds for BD-rate numbers, while not standard practice in this field, would improve statistical rigor.
- A breakdown of FLOPs/latency attributable specifically to the clustering step at inference time (separate from the SSM) would help practitioners assess deployment cost.

## Removed Points

These points were flagged in the input reviews but are removed with justifications:

1. **"Missing multi-directional Mamba comparison"** (Harsh Critic) — REMOVED. Table 4 already compares CAM against "2D Mamba" (−14.13% BD-rate vs. CAM's −15.91%). This directly addresses the concern about whether CTP+GPP match multi-directional scanning. The harsh critic missed this existing comparison.

2. **"Model would fail to learn without gradient approximation"** (Harsh Critic) — DEMOTED from fatal/critical to Major (above). The claim that training "cannot reach the feature representations" is incorrect: the features ARE the content that flows through the SSM and the permutation is a reindexing operation, so gradients backpropagate through the token content. The assignment decisions don't receive gradient, but this is analogous to VQ-VAE's straight-through setup. The omission of explicit description remains a real issue, but not a fatal one.

3. **"Reproducibility concern about citing other papers' models"** — REMOVED (hard rule: all cited entities are assumed to exist).

4. **"Missing related work comparisons"** — REMOVED (hard rule).

5. **"Formatting/presentation nitpicks about figures"** — REMOVED (hard rule).

6. **Strength Finder claims that are generic** — REMOVED. Strengths like "the paper is well-motivated" or "addressed an important problem" are generic and not tied to specific evidence in the paper.

7. **"Reproducibility concern about hyperparameters and appendix"** — REMOVED. The parser strips appendices; they exist in the original submission. References to Appendix A.8-A.10 (line 129) confirm content exists in the full version.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation about the method, results, or implications that the paper itself does not already provide. The gradient-flow question is a methodological clarification, not a conceptual insight.

## Suggestions

1. Explicitly state whether straight-through estimation is used for gradient propagation through the discrete clustering, or describe the actual gradient path (e.g., the permutation is a differentiable indexing operation on token content, while centroids are updated via EMA without gradient).
2. Report the EMA decay λ value used in Algorithm 1.
3. Add a quantitative ERF metric (e.g., the spatial radius capturing 95% of the gradient magnitude) to support the "significantly larger" claim numerically.
4. Add a brief limitations paragraph discussing the fixed codebook size, potential failure cases for OOD images, and the memory cost of per-block codebooks.
5. Harmonize "MambaC" vs. "MambaIC" naming throughout the paper and tables.

## Score and Decision

**Calibration anchors** (from the deepreview_13k dataset, all retrieved via the single batch call):

| Paper (Path) | Avg Score | Comparison to CMIC |
|---|---|---|
| MambaVC (`KgJwbsfN7G.md`) | 4.80 | Simpler application of Mamba to LIC without content-adaptive innovations; CMIC is significantly stronger in novelty, results, and thoroughness. |
| Spatial-Mamba (`iDe1mtxqK5.md`) | 7.00 | Comparable novelty level for SSM-based vision modeling; CMIC has more thorough compression-specific evaluation but is narrower in task scope. |
| GroupMamba (`RmmrHEH6Nx.md`) | 3.00 | Limited novelty (channel grouping + SE-like modulation); CMIC has substantially more technical contribution and better empirical support. |
| FATransformer (`HKGQDDTuvZ.md`) | 6.00 | Similar tier of LIC paper with SOTA results; CMIC has stronger novelty (CTP/GPP are more creative than frequency decomposition) and comparable experimental rigor. |
| Frequency-Aware LIC (`HKGQDDTuvZ.md`) | 6.00 | Mid-range LIC paper with thorough evaluation but limited novelty discussion; CMIC's innovations are more specific and better motivated. |

Positioned relative to these anchors, the paper under review is stronger than the 4.8 and 3.0 anchors, comparable to or slightly stronger than the 6.0 anchors, but below the 7.0 anchor in breadth of impact (Spatial-Mamba targets general vision tasks, CMIC is specific to compression). The paper's main gap (gradient flow clarification) is meaningful but fixable and does not undermine the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>