Now I have thoroughly verified the reviewer's claims against the paper. Let me produce the final consolidated review.

## Summary

This paper proposes CirT (Circular Transformer) for global subseasonal-to-seasonal (S2S) climate forecasting at 2-6 week lead times. The model has two main design elements: (1) **circular patching** — decomposing the spherical grid by latitude so each token represents one full parallel, avoiding the geometric distortion of rectangular patches; (2) **frequency-domain self-attention** — applying Discrete Fourier Transform (DFT) to patch embeddings before attention, then inverse-transforming back to the spatial domain. The model is trained end-to-end to directly predict bi-weekly averages (weeks 3-4 and 5-6) rather than rolling out autoregressively. Experiments on ERA5 show CirT outperforming both data-driven baselines (FourCastNetV2, PanguWeather, GraphCast, ClimaX) and numerical NWP systems (UKMO, NCEP, CMA, ECMWF).

## Strengths

- **Circular patching is a clean, geometrically motivated design.** Each latitude band becomes one token with physically meaningful circumference proportional to cos(latitude). This eliminates the unequal-area distortion of fixed-degree planar patches. The ablation (Table 2) confirms its value: replacing grid patching with circular patching (no FT) reduces z500 weeks 3-4 RMSE from 516 to 502.

- **Direct bi-weekly prediction is well-motivated for the S2S timescale.** By predicting weeks 3-4 and 5-6 averages directly from the initial state, CirT avoids the compounding errors that plague autoregressive rollouts over 42 days. The results support this design choice: CirT's relative improvement over baselines is consistently larger for weeks 5-6 than for weeks 3-4.

- **Strong empirical results, particularly in challenging high-latitude regions.** CirT achieves substantially lower RMSE in mid- and high-latitude areas (e.g., t500 weeks 3-4: 19.6%/16.2% improvement over best baseline in mid/high latitudes vs. 1.2% in low latitudes, Table 3). This is practically significant because many models struggle in polar regions.

- **Comprehensive evaluation scope.** The paper compares against 4 data-driven models (including ClimaX trained from scratch on the same S2S task) and 4 operational NWP systems, across multiple variables, pressure levels, and lead times, with spatial and temporal visualizations.

## Weaknesses

### Fatal
None. While the paper has significant issues, the empirical results are real and the circular patching contribution is valid.

### Major

- **The claimed "spatial periodicity modeling" via Fourier transform is not supported by the implementation.** The paper motivates DFT as capturing the $2\pi$ periodicity of the circular patch ($X_w = X_{w+W}$), stating: *"Considering the circular patch satisfies $X_w = X_{w+W}$. Therefore, instead of directly inputting $X$ into the transformer, we consider its Fourier transform"* (Section 3). However, the raw spatial signal $X^{(h)} \in \mathbb{R}^{W \times K}$ has already been flattened and projected to an embedding $E \in \mathbb{R}^{H \times D}$ before reaching the transformer. The DFT is then applied to **each row of the embedding matrix** — i.e., along the learned feature dimension $D = 256$ (Eq. 5), **not** along the longitudinal spatial dimension $W = 240$. There is no geometric relationship between the index $n$ in Eq. 5 (embedding coordinate) and the longitude index $w$ of the spherical grid. The paper never explains why decomposing learned embedding vectors into frequency components should encode spatial periodicity of the graticule. This is a genuine mismatch between the conceptual narrative and the actual mechanism. The method may still work well (spectral feature mixing can aid optimization, as the ablation suggests), but the paper's central claim about modeling spatial periodicity is misleading and unsubstantiated by the evidence presented. This is **not** a fatal flaw because (a) circular patching remains a valid contribution regardless, and (b) the empirical results are strong — but it is a significant weakness that undermines the paper's framing and would require major revision (either applying DFT along the spatial dimension, or re-explaining the actual role of the Fourier operation) to be acceptable.

- **The ablation does not test the claimed mechanism.** The ablation (Table 2) compares "Grid+FT" vs. "Grid" and "Cir+FT" vs. "Cir", showing that FT helps only with circular patches. But since FT is applied to the embedding (not the spatial signal) in all variants, the paper cannot distinguish whether FT helps because it "models spatial periodicity" or because it provides a useful spectral reparameterization of the feature space. To validate the specific claim of spatial periodicity modeling, the authors would need to test DFT applied directly along the longitudinal dimension $W$ (before or instead of projection to embeddings). Without this, the interpretation that FT captures *spatial* periodicity is speculative.

### Minor

- **Asymmetric comparison against pretrained short-term models.** FourCastNetV2, PanguWeather, and GraphCast were trained for 6-hourly/daily forecasting at 0.25° resolution, then run autoregressively for 42 days to produce bi-weekly averages, while CirT is trained end-to-end on the exact S2S objective. This asymmetry advantages CirT. However, this is **partially mitigated** by (a) the inclusion of ClimaX, which is trained from scratch on the same S2S task and which CirT still outperforms by significant margins (e.g., z500 weeks 3-4: 477 vs. 527), and (b) the fact that using pretrained SOTA models as baselines is standard practice in the field. The paper should more explicitly acknowledge this limitation and ideally include a direct-prediction ViT baseline trained from scratch.

- **Missing direct S2S baseline.** The paper acknowledges it cannot access Fuxi-S2S, which is a direct-prediction S2S model. This weakens the claim of S2S-specific superiority, though it is an understandable resource limitation.

- **No variance or confidence intervals reported.** The main results (Table 1) report single numbers without error bars or significance tests, making it difficult to assess the reliability of the reported improvements.

### Trivial

- Position embeddings are added to the projected embedding (Eq. 4) but their role is not discussed in the ablation — do they matter more/less with circular patching?
- The notation $N$ in the DFT equations (e.g., Eq. 5 uses $2\pi (k/N) n$) is ambiguous: in the Preliminaries $N$ is the sequence length, but in the architecture description it becomes the embedding dimension $D$.

## Nice-to-Haves

- Applying DFT along the longitudinal dimension $W$ (before projection or as a separate branch) and comparing against the current embedding-DFT approach would resolve the ambiguity about the mechanism.
- Training a ViT baseline (e.g., Pangu-style architecture) from scratch on the same direct S2S objective would tighten the fairness of comparisons.
- Reporting confidence intervals over multiple initialization seeds or temporal test samples would strengthen the statistical claims.
- Analysis of learned frequency components: which frequencies dominate in the embedding-DFT, and do they correlate with known spatial scales of atmospheric phenomena?

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Strength Finder's claim about "frequency-domain self-attention to model longitudinal periodicity"**: This strength conflicts with the verified weakness that DFT is applied to the embedding dimension, not the spatial dimension. Per the rule that when a strength and weakness disagree, the weakness wins, this strength is removed. The circular patching is valid, but the Fourier mechanism's claimed role is unsupported.

- **Criticism about unfair comparison (from harsh critic, treated as too severe)**: The harsh critic frames this as invalidating headline results. While the asymmetry is real, ClimaX (trained from scratch on S2S) provides a fair baseline that CirT convincingly outperforms. The critic's framing that "the comparison tests task specialization, not model quality" overstates the problem — comparing against SOTA pretrained models is standard, and the paper does include a fair baseline. This criticism is moved here as overstated in severity.

- **Strength Finder's point about "Comprehensive evaluation against both data-driven and numerical baselines"**: This is kept in strengths above — it is specific and backed by evidence. However, the Strength Finder's phrasing about CirT "consistently achieving the best RMSE and ACC" is kept but should be read alongside the baseline caveat.

## Novel Insights

The most interesting finding is that treating each latitude band as one token (circular patching) substantially improves S2S forecasts, especially in high latitudes where planar-patch models struggle most. This suggests that respecting spherical geometry through tokenization matters more than local spatial resolution within patches. The fact that adding Fourier processing further boosts performance — even though the DFT operates on learned embeddings rather than raw spatial signals — hints at a potentially general benefit of spectral reparameterization in transformer architectures for periodic or quasi-periodic data. However, the paper's failure to connect the DFT implementation to its spatial motivation means the mechanism behind this improvement remains unclear. A controlled experiment applying DFT along either the spatial or embedding dimension would be needed to resolve this.

## Suggestions

1. **Either align the implementation with the motivation by applying DFT along the longitudinal dimension $W$** (before projection or as a separate processing stream), **or rewrite the motivation to honestly describe what the DFT-on-embedding does** — e.g., as a form of spectral feature mixing that may help optimization without any specific geometric interpretation. The current framing is misleading and must be corrected.

2. **Add a direct-prediction ViT baseline trained from scratch** (e.g., a standard ViT with grid patching trained on the same S2S objective with the same budget) to provide a cleaner apples-to-apples comparison with CirT's circular patching + FT pipeline.

3. **Report error bars or confidence intervals** for the main results, at minimum across temporal test samples.

4. **Clarify the DFT notation**: explicitly state that the DFT is applied over the $D$ embedding dimensions, explain why this choice was made, and discuss whether the learned projection weights could encode spatial frequency information.

5. **Consider adding a local attention or cross-attention mechanism along the longitudinal direction** within each circular patch to capture intra-patch spatial correlations that the current single-token-per-band design discards.

## Score and Decision

The paper presents a genuine contribution in circular patching and demonstrates strong empirical results. However, the central conceptual claim about the Fourier transform modeling spatial periodicity is not supported by the implementation — DFT is applied to the embedding dimension, not the spatial dimension. This mismatch between narrative and mechanism is a significant flaw that would require substantial revision to correct. The baseline comparison issues, while partially mitigated by the ClimaX baseline, also weaken the strength of the claims. I cannot recommend acceptance in the current form.

**MY FINAL SCORE: <pineapple>4.5</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**