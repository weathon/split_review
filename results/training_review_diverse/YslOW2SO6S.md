## Summary

This paper introduces CirT (Circular Transformer), a geometry-inspired model for global subseasonal-to-seasonal (S2S) climate forecasting. It proposes two key designs: (1) **circular patching** that partitions the graticule by latitude into uniform circular patches, addressing geometric distortion from planar projection, and (2) **frequency-domain self-attention** using Discrete Fourier Transform on patch embeddings followed by multi-head attention in the frequency domain. The model is trained to directly predict biweekly averages (Weeks 3–4 and 5–6) from an initial state, avoiding error accumulation from iterative rollouts. Experiments on ERA5 show consistent improvements over data-driven baselines (FourCastNetV2, PanguWeather, GraphCast, ClimaX) and competitive physics-based models.

## Strengths

- **Circular patching provides a clean, well-motivated geometric fix that works.** The paper correctly identifies that planar decomposition of spherical data creates patches of unequal area and shape, and proposes decomposing by latitude into equidistant circular patches. Ablation results (Table 2) confirm this alone reduces z500 Weeks 3–4/5–6 RMSE from 516/501 to 502/498 (without FT), establishing this as an independent, effective design choice.

- **Direct prediction for S2S yields large practical gains over iterative models.** CirT directly predicts Weeks 3–4 and 5–6 averages rather than unrolling an autoregressive model. Table 1 validates this: CirT's z500 RMSE stays nearly flat from Weeks 3–4 to 5–6 (477→471), while iterative models degrade sharply (e.g., FourCastNetV2: 646→757, PanguWeather: 690→800). This is a meaningful engineering contribution for the S2S setting.

- **Empirical results are strong and consistent across variables, lead times, and geography.** Table 1 shows CirT outperforms all baselines on every reported variable. The ablation (Table 2) confirms both design choices contribute. Table 3 and Figures 4–5 show the gains hold across latitude bands and months, with particularly large relative improvements in mid- and high-latitude regions where geometric distortion is most severe (e.g., t500 Weeks 3–4: 1.2% improvement in low-latitudes vs. 19.6%/16.2% in mid-/high-latitudes).

## Weaknesses

### Major

- **The claim that the Fourier transform captures "spatial periodicity along longitude" is not supported by the implementation.** The paper repeatedly states that the DFT extracts periodic spatial features from the circular patch (e.g., Section 1: *"leverage the Fourier transform to extract the global features and model the spatial periodicity"*; Section 3: *"Considering the circular patch satisfies X_w = X_{w+W}. Therefore, instead of directly inputting X into the transformer, we consider its Fourier transform"*). However, the actual implementation applies the DFT to the **learned embedding dimension (D)** of each patch after flattening and linear projection (Eq. 6: S_{h,k} = Σ_{n=1}^{D} E_{h,n} cos(...)). The embedding dimension is a learned latent space with no guaranteed spatial ordering along longitude — the projection matrix W_p ∈ ℝ^{(W·K)×D} mixes all spatial positions and channels. Applying a 1D DFT to this arbitrary feature dimension does not, in any principled way, analyze spatial frequencies along the longitude axis. This is a significant overclaim: the Fourier step may help for unrelated reasons (e.g., frequency-domain regularization, better-conditioned attention), but the paper provides no analysis — not even a comparison with a version applying DFT along the spatial W axis — to support the periodicity claim. The contribution would need to be either reframed as a general spectral mixing mechanism (with appropriate comparisons to other spectral methods) or re-engineered to genuinely operate on spatial dimensions.

- **The comparison with physics-based numerical models (NWP) is insufficiently documented.** The paper claims CirT *"remarkably outperforms numerical models in almost all cases"* (line 170), listing ECMWF, UKMO, NCEP, and CMA. However, no quantitative results (exact RMSE/ACC values) are provided for these baselines — only a heatmap (Figure 3) where individual values are not readable. The paper does not specify which model version was used, the source of the forecasts (operational hindcasts? reforecasts? which database?), the lead times and initial conditions, or how the evaluation period aligns temporally with the CirT test set (2018). For a claim of this magnitude — beating the world's most skillful operational S2S system (ECMWF) — the evidence must be transparent and quantitative. A table with exact RMSE/ACC values and a clear description of the forecast data source is essential and currently absent.

### Minor

- **The data-driven baselines comparison is asymmetric, though partially mitigated.** FourCastNetV2, PanguWeather, and GraphCast are used as **pretrained** medium-range models via iterative rollout + averaging, not trained or fine-tuned for the specific S2S biweekly prediction task. ClimaX is retrained for the same task (which partly addresses this), and the ablation's grid-patch baseline (Table 2, z500 RMSE 516/501) approximates a direct-prediction ViT that CirT outperforms. Nevertheless, the comparisons against the other three baselines conflate architectural superiority with the advantage of direct over iterative prediction. Training a standard direct-prediction ViT or fine-tuning one of these baselines for S2S would strengthen the claim.

- **The ablation does not directly test whether DFT on the spatial axis is what matters.** The current ablation (Table 2) tests grid vs. circular patching with and without FT on the embedding. To validate the **spatial periodicity** claim, an experiment applying 1D DFT along the longitude dimension (W, before projection) would be the most direct test. Without it, the improvement from the Fourier step could stem from general frequency-domain feature processing rather than specifically from exploiting latitudinal periodicity. (This is partly a consequence of the first major weakness.)

- **The optimizer is not specified.** The implementation details list learning rate (0.01), batch size (16), hidden dim (256), layers (8), heads (16), and epochs (20), but do not state the optimizer (e.g., AdamW, SGD, Adam with specific betas). This is a minor reproducibility gap.

### Trivial

- **DFT notation inconsistency.** The forward DFT (Eq. 6) sums from n=1 to D but writes "N" in the cosine argument denominator (2π(k/N)n). The inverse (Eq. 10) similarly uses "N" in the argument while normalizing by 1/D. The variable N should be D throughout. This does not affect the model's correctness but signals carelessness.

## Nice-to-Haves

- Provide a table with exact RMSE/ACC values for ECMWF, UKMO, NCEP, and CMA along with the forecast data source and evaluation period.
- Include a direct-prediction version of at least one medium-range baseline (e.g., train a ViT from scratch for the S2S task beyond the ablation's grid-patch variant).
- Test DFT applied along the spatial longitude axis (before projection) as an additional ablation to validate the spatial periodicity hypothesis.
- If the Fuxi-S2S resource becomes available, include it as a direct-prediction S2S baseline.
- Report per-variable results for all 63 variables rather than the 7 selected, or provide the full table in supplementary material.

## Removed Points

- *"Coarse 1.5° resolution"* — This is a deliberate design choice appropriate for S2S computation, acknowledged as future work for higher resolution. Not a weakness of the presented study.
- *"Fuxi-S2S exclusion"* — The paper transparently states the resource is unavailable. This is not the authors' fault.
- *"Potentially unfair comparison" framed as a structural flaw* — The paper retrains ClimaX for the same task and the ablation provides a direct-prediction baseline (grid + no FT). The asymmetric comparison is a real concern but is partially addressed and belongs in Minor rather than the strong language used by the critic.
- *Strength Finder's claim about "principled way to inject spatial periodicity"* — This endorses the paper's unsupported mechanism claim. Rephrased to focus on the empirical finding rather than the unverified mechanism.

## Novel Insights

The most interesting tension exposed across the reviews is that the paper's **empirical success** (consistent outperformance across all metrics and ablations) is stronger than its **mechanistic justification** (the DFT-on-embedding approach does not do what the paper claims it does, spatially speaking). This suggests the model may work well for reasons other than those advertised — possibly because the DFT acts as a learnable-frequency regularization or a spectral bottleneck that improves generalization on periodic climate data in the latent space, or because the attention in the frequency domain better captures cross-latitude interactions. Distinguishing these alternatives would strengthen the paper considerably and could lead to a cleaner design in follow-up work.

## Suggestions

1. **Reframe the Fourier transform contribution.** Either (a) show that applying DFT along the spatial longitude axis (before projection) yields equivalent or better performance, thus validating the spatial periodicity claim, or (b) reposition the DFT-on-embedding as a general spectral mixing mechanism, drop the spatial periodicity language, and compare against alternative spectral mixers (e.g., FNO-style mixing on patches) to isolate why this particular design helps.

2. **Add a table with exact RMSE/ACC for NWP models.** Include the forecast source (e.g., S2S database hindcasts), model versions, lead times, and ensure the evaluation period matches the CirT test set. Without this, the headline claim of beating operational systems is unverifiable.

3. **Train a direct-prediction ViT or fine-tune PanguWeather/GraphCast for S2S** to disentangle the benefit of direct prediction from architectural superiority. The ablation's grid-patch + no FT baseline partially serves this, but making it explicit would strengthen the paper.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>