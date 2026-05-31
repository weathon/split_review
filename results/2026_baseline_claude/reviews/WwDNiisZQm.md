Now let me write the full review.

---

## Summary

The paper introduces Content-Aware Mamba (CAM), a novel adaptation of Mamba-style State-Space Models (SSMs) for learned image compression. Two limitations of vanilla Mamba in this setting are identified and addressed: (1) fixed raster-scan order that ignores feature-space proximity, handled by Content-Adaptive Token Permutation (CTP) via codebook-based cosine K-Means with EMA updates; and (2) strict causality that prevents tokens from accessing non-preceding global context, mitigated by Global-Prior Prompting (GPP) that injects cluster-derived sample-specific prompts into the SSM output matrix. The resulting CMIC model achieves state-of-the-art BD-rate performance, outperforming VTM-21.0 by 15.91%, 21.34%, and 17.58% on Kodak, Tecnick, and CLIC, respectively, while remaining computationally competitive with prior work.

---

## Strengths

- **Substantial and consistent SOTA performance**: CMIC outperforms all prior LIC methods on all three evaluated benchmarks under both MSE and MS-SSIM metrics (Tab. 1, Figs. 4–6). Gains over the strongest prior Transformer-based method (FTIC) reach up to 0.36 dB BD-PSNR, and gains over the best Mamba-based method (MambaIC) reach up to 6.48% BD-rate on Tecnick — neither trivial differences.

- **Clean ablation with complementary gains**: Tab. 2 cleanly isolates CTP (+1.8–2.4% BD-rate alone) and GPP (+0.5–1.4% alone), together reaching 2.7–3.6% over the baseline. The two components are shown to be complementary, which validates the design rationale for both independently.

- **Compelling ERF visualizations**: Figures 7–9 offer unusually strong qualitative evidence. The single-layer ERF visualization in Fig. 9 directly demonstrates that (i) vanilla raster-scan Mamba produces ERFs that stop exactly at the current scan position, (ii) GPP enables activation beyond the causal horizon, and (iii) CTP breaks the Euclidean-neighbor constraint and reshapes ERF to content-correlated regions. Fig. 10 shows that cluster centroids learn semantically coherent visual concepts shared across images (edge patterns, colored textured regions, smooth backgrounds).

- **Excellent efficiency**: CMIC reduces FLOPs by 57%, latency by 39%, and peak GPU memory by 78% versus MambaIC, while simultaneously improving BD-rate by ~2–6% — making it Pareto-dominant on the complexity–performance frontier. CTP and GPP together add only a 4% latency overhead (Tab. 3).

- **Thorough baseline coverage**: Thirteen prior LIC methods are included, spanning CNN, Transformer, hybrid, and SSM architectures. Complexity dimensions (FLOPs, latency, peak memory, parameter count) are all reported, not just performance.

---

## Weaknesses

### Fatal
None.

### Major

- **The non-causality claim is partially overstated.** GPP injects cluster-level global statistics into the output matrix **C**, which is a soft modulation derived from per-image centroid activations. This is meaningfully different from full bidirectional attention or a true non-causal mechanism: the SSM still processes tokens sequentially, and the "global" signal is only a coarse, K-dimensional cluster membership vector. The ERF evidence in Fig. 9 (column c) confirms that GPP broadens the receptive field beyond the raster-scan horizon, but the activated regions are limited and qualitatively less global than the full CTP+GPP case. The paper should more precisely characterize GPP as *soft global conditioning* rather than a strict relaxation of causality.

- **The non-differentiable permutation is underexplored.** CTP reorders tokens via a non-gradient K-Means assignment. As a result, the permutation π itself carries no gradient signal back to the feature extractor that generates the tokens being clustered. The clustering objective (cosine distance to EMA centroids) is decoupled from the rate-distortion loss. The paper briefly notes that the mapping A(·) for prompt generation is differentiable, but does not discuss whether the lack of end-to-end gradient through the permutation operation limits performance, or whether an alternative (e.g., soft/differentiable assignment) might be beneficial. This is a non-trivial design choice that deserves more justification.

### Minor

- **Table 2 contains a parser-damaged row.** The first two rows both show CTP=✓, GPP=✗, which is clearly an OCR/table-parsing artifact; the text refers to a "baseline block with both components disabled" whose numbers are consistent with the first row (−13.26/−17.74/−14.87 ≈ CTP-only minus ~2%). This is a parser issue and not a paper flaw per the hard rules, but the table's logical structure would benefit from an explicit "baseline" row label.

- **Entropy model contribution is undercharacterized.** The paper introduces a modified entropy model (depthwise conv + gated MLP in SCTX; Fig. 3) but its isolated contribution is not ablated. Since the entropy model is a known performance lever in LIC, it is unclear how much of the gain over MambaIC comes from CAM vs. the improved entropy model.

- **The ablation on K (Tab. 6) shows K=128 gives −15.96% vs K=64 giving −15.91%**, essentially equivalent. This is fine, but the paper would benefit from reporting the computational cost of K=128 vs K=64 to confirm the diminishing returns story is also computationally justified.

### Trivial

- The CTP and GPP conceptual inspirations (VQ-VAE codebook, MambaIRv2 prompting) are acknowledged but their differences from the proposed mechanisms could be stated more sharply in the main text rather than just the related work.

---

## Nice-to-Haves

- An analysis of failure cases — images where the content-adaptive clustering assigns tokens poorly (e.g., highly textured noise-like images) — would strengthen the paper's practical characterization.
- A soft/differentiable variant of the token assignment (e.g., Gumbel-softmax or sinkhorn-based) could be briefly explored as a comparison point to validate the EMA K-Means design choice.
- Extending CMIC to video compression (given Mamba's sequential nature) would be a natural future direction worth mentioning.

---

## Novel Insights

The most genuinely novel insight in this work is that the scanning order of an SSM is itself a form of inductive bias that can be learned from data rather than fixed by spatial geometry, and that VQ-VAE-style codebook clustering provides a stable, efficient, and deterministic mechanism to achieve this at inference time without iterative per-sample optimization. The per-image ERF ablation in Fig. 9 provides unusually clear empirical support for this idea: raster-scan Mamba has a hard causal boundary at the scan midpoint; codebook-permuted Mamba redistributes receptive field mass to semantically relevant locations regardless of spatial position. The additional finding that only 16–32 of 64 codebook centroids are active per image — with the activated subset varying by content — suggests the model discovers a sparse, content-specific vocabulary of visual patterns, which is interesting beyond image compression.

---

## Suggestions

- **Clarify the gradient flow through permutation**: Add a short discussion on why the non-differentiable CTP step does not harm end-to-end training, citing relevant prior work on gradient-free operations in deep networks (e.g., VQ-VAE's straight-through estimator) or an experiment comparing EMA-K-Means vs. a soft variant.
- **Separate the entropy model contribution**: A single-row ablation replacing the proposed entropy model with the standard SCTX baseline (keeping all else equal) would disambiguate the gains from CAM vs. the entropy model.
- **Refine causality language**: Replace "overcomes strict causality" / "mitigates strict causal constraint" with more precise phrasing such as "injects global distributional context that softens the dependence on scan order" or similar, to avoid overclaiming.

---

## Score and Decision

The paper makes a meaningful and well-executed technical contribution to learned image compression: two principled modifications to Mamba scanning that achieve substantial and consistent SOTA gains across three benchmarks with strong efficiency. The ablations, visualizations, and complexity comparisons are thorough and compelling. The main limitations — an overstated causality claim and underexplored gradient-flow implications of the non-differentiable permutation — are significant but do not invalidate the core results. This is a clear accept.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>