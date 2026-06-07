## Summary

This paper proposes a cross-attention autoencoder architecture to embed arbitrarily shaped (variable-length, ungridded, permutation-variant) Total Electron Content (TEC) observations into fixed-size vectors, then uses these embeddings as features for downstream electron density prediction. The encoder uses learnable query tokens that cross-attend to the raw TEC point cloud; the decoder reconstructs TEC at arbitrary query locations from the embedding. Experiments show that the embedding captures information beyond what can be predicted from standard space-weather indices alone, and that concatenating a 16-dimensional TEC embedding into a feed-forward electron density model (DINN) modestly improves nmf2 (peak density) prediction on independent ionosonde data during storm conditions.

## Strengths

- **Well-designed NoEmbedCompare baseline demonstrates the embedding captures real TEC state, not just climatology.** The paper trains a decoder-only model that predicts TEC from time + driving indices (Kp, ap, Dst, f10.7), using the same reconstructor architecture. All three embedding variants (sizes 16, 128, 512) outperform this baseline substantially (Figure 4, line 135), proving the autoencoder is doing more than memorizing cyclical patterns. This is the strongest piece of evidence in the paper.

- **Validation on independent GIRO ionosonde data during storm conditions.** The electron density predictions are tested against ground-truth ionosonde measurements (Figures 7-8, lines 156-166), not just the GPSRO training data. The DINN eTEC model shows consistent improvement in nmf2 correlation and MAE across all Kp ranges, including storm-time (Kp×10 ≥ 50). This provides real-world validation beyond in-distribution test sets.

- **Transparent and physically grounded discussion of limitations.** The paper openly reports that hmf2 (peak height) predictions worsen with TEC embeddings, and offers a clear physical explanation: TEC is an integral quantity correlated with peak density but not profile shape, and the model may overfit to GPSRO biases (line 161). This candor is rare and strengthens credibility.

- **Systematic scaling study over embedding dimension.** Three embedding sizes (16, 128, 512) are trained and compared, showing monotonic improvement in reconstruction quality with larger capacity (Table 1, Figure 4). This confirms the method's behavior is predictable and well-behaved.

## Weaknesses

### Major

- **Failure to cite extensive prior work on the same core mechanism, and framing the technique as a novel proposal.** The paper states: "We propose a method of using cross attention to do this [embed oddly shaped data into a fixed size and shape]" (abstract, line 4). However, using learnable query tokens that cross-attend to a variable-length input to produce a fixed-size latent representation is the central mechanism of **Set Transformer** (Lee et al., ICML 2019 — Induced Set Attention Block), **Perceiver** (Jaegle et al., ICML 2021), and **Perceiver IO** (Jaegle et al., ICML 2022). The encoder-decoder structure (compress via cross-attention with learnable queries, reconstruct via cross-attention from latent to output) is directly analogous. None of these works are cited. For a submission to ICLR, where this is well-known architecture, this omission is serious — it misrepresents the contribution as a new method when it is a direct application of established architectures to a new domain. The paper must be repositioned as an application paper demonstrating the effectiveness of known set-encoding architectures on TEC data, with clear discussion of any domain-specific adaptations.

- **No ablation comparing the cross-attention encoder to simpler compression baselines.** The paper's central claim is that the specific cross-attention mechanism with learnable queries is the right way to embed oddly shaped data. Yet there is no comparison to obvious simpler alternatives: mean-pooling per-point features, max-pooling, a learned attention-weighted average (standard attention pooling), or a small MLP per point followed by pooling. The only baseline (NoEmbedCompare) skips compression entirely and predicts TEC from indices. Without these ablations, the paper cannot justify that the cross-attention machinery itself provides value beyond what any reasonable compression scheme would achieve. This is a critical gap for a paper whose primary contribution is claimed to be architectural.

### Minor

- **Missing architectural details needed for full understanding.** The paper does not specify the number of attention heads, the length of the learnable query sequence (is it 1 token of dimension D, or N tokens that are pooled?), or which standard transformer components (layer normalization, residual connections, feed-forward sublayers) are retained/modified. The "internal attention size of 32" (line 81) is mentioned but it is unclear how this interacts with the embedding dimension and the multi-head mechanism. These details matter because the paper claims to "follow the structure for a transformer outlined by Vaswani et al. (2017)" but it is unclear which components are carried over.

- **The improvement in electron density prediction is modest and the practical significance is unclear.** The gain is ~0.80→0.82 Pearson r for GPSRO data (Figure 6) and visible but modest nmf2 improvements on ionosonde data (Figures 7-8). The paper's own honest discussion notes that hmf2 actually worsens (line 161). While the improvement is consistent, the paper should more carefully calibrate the practical significance of these gains.

- **Permutation invariance is noted but not explicitly addressed.** The paper states TEC data "is not ordered (i.e., to not introduce bias, the order data is processed should not affect the output)" (line 17), but never clarifies whether positional encodings or other ordering-sensitive components are used, and whether permutation invariance is guaranteed by the architecture. (Cross-attention without positional encodings on the input sequence would be permutation-invariant, but this should be stated explicitly.)

### Trivial

- Table 1 is an embedded image and many model parameters are not readable from the text. The internal attention size of 32 is stated, but the number of parameters per model should be explicitly listed in the text or in a properly formatted table.

## Nice-to-Haves

- Confidence intervals or bootstrap estimates on the correlation coefficients would further strengthen the evidence, though at the sample sizes used (2B and 185M points) the estimates are already extremely precise.
- A quantitative comparison of TEC completion to existing methods (Pan et al., 2021; Sun et al., 2023) would substantiate the capability mentioned at line 137, though the paper correctly scopes this as future work.
- A dedicated table reporting correlation, MAE, and RMSE for all models (DINN, DINN eTEC, RDINN, RDINN XRS) on both nmf2 and hmf2 would allow direct comparison without relying on figures alone.

## Removed Points

These points were raised by reviewers but are removed from the main review for the following reasons:

1. **"Differences might be within noise of a single run"** — Removed as factually incorrect. With N=2 billion (TEC) and N=185 million (electron density), the standard error of Pearson r is on the order of 10⁻⁵, making the observed differences (0.02) overwhelmingly statistically significant. The concern about *practical* significance is retained as a Minor weakness.

2. **"TEC completion claimed but not validated"** — Removed because the paper explicitly states "the accuracy of this completion is out of the scope of this paper" (line 137) and presents it as future work. The paper does not claim validated TEC completion.

3. **"Omission of time features creates asymmetry against NoEmbedCompare"** — Removed because omitting time features makes the embedding task *harder*, not easier. The comparison demonstrates the embedding captures more than what can be predicted from time + indices, which is a stronger test.

4. **"No open-source code or model weights are mentioned"** — Removed per the rule that questioning availability of artifacts not cited in the paper is outside scope.

5. **"Missing training hyperparameters (learning rate, optimizer, weight decay, scheduling)"** — Removed per the rule against nitpicks about undisclosed hyperparameters, as these are standard implementation details.

6. **"RDINN/RDINN XRS results not quantitatively shown"** — Removed because Figures 7 and 8 do include these models; the captions are sparse but the data is present. This is a presentation issue at most.

## Novel Insights

Both reviews correctly identify the central tension: the paper applies a well-established ML architecture (learnable-query cross-attention for set encoding) to a genuinely difficult and underexplored domain problem (TEC embedding for ionospheric modeling). The reviews converge on the assessment that the contribution is primarily in the application domain, not in the architectural innovation. A productive path forward would be to use this as an opportunity: reframe the paper as a rigorous case study of how set-encoding transformers can be adapted to operational space-weather data, emphasizing the domain-specific challenges (temporal alignment of TEC snapshots with GPSRO profiles, the asymmetry between integral TEC and profile shape) that do not arise in standard benchmark settings and that provide new constraints on how these architectures behave in practice.

## Suggestions

1. **Reframe the paper's contribution.** Reposition it as an application of set-encoding transformer architectures (Set Transformer, Perceiver) to TEC data for ionospheric modeling, with clear citations to prior work and explicit discussion of any domain-specific adaptations. The current framing as proposing a new method is inaccurate and will be immediately flagged by reviewers familiar with the literature.

2. **Add ablation studies comparing the cross-attention encoder to at least two simpler baselines:** (a) mean-pooling per-point features, and (b) a learned attention-weighted average (standard attention pooling) without learnable inducing points. This will demonstrate whether the learnable-query cross-attention mechanism specifically provides value beyond straightforward compression.

3. **Specify the full architecture:** number of attention heads, query sequence length, which transformer components (layer norm, residual connections, FF layers) are retained, and initialization scheme for the learnable queries. For an architecture-centric paper, these details are essential.

4. **Provide a dedicated results table** with correlation, MAE, and RMSE for all four models (DINN, DINN eTEC, RDINN, RDINN XRS) on both nmf2 and hmf2, so readers can directly compare numerical values without reading figures.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>