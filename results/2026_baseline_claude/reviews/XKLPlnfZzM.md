## Summary

The paper introduces the Temporal Deaggregation Diffusion Model (TDDM), a hierarchical framework for large-scale mobility trajectory generation. The core idea is to factorize trajectory generation into two components: spatial priors (discretized marginal distributions over geographic occupancy, marginalized over time) and temporal dynamics conditioned on those priors. Canonicalization via similarity transforms maps each geographic region into a normalized coordinate frame, enabling parameter sharing and zero-shot cross-city transfer. The authors also construct a standardized three-city benchmark (Beijing/Porto/San Francisco) with a comprehensive suite of evaluation metrics, demonstrating consistent improvements over GAN-, VAE-, and diffusion-based baselines.

## Strengths

- **Principled spatial-temporal factorization with strong empirical gains.** The separation of *where* (spatial prior H) from *how* (temporal dynamics) is well-motivated and cleanly realized. Ablations confirm that removing spatial priors degrades KL-based distributional measures by ~5×, directly attributing the improvements to the proposed factorization rather than architectural novelties.

- **Consistent improvements across diverse datasets and metrics.** TDDM achieves symmetric KL divergence of 0.277 vs. 1.153/1.232 for the next-best diffusion baselines, JS of 0.059 vs. 0.198/0.209, and top or near-top scores on all ten reported metrics across three geographically and culturally distinct cities. The visual comparisons in Figure 2 corroborate the quantitative gains.

- **Convincing zero-shot generalization experiment.** The intra-city (25% map → full city) and cross-city (Porto/Geolife/Cabspotting ↔) transfer experiments are a principled test of the generalization claim. The result that Porto-trained models match or beat models trained on 25% of target-city data on most metrics is a genuinely interesting empirical finding.

- **Useful benchmark contribution.** Standardizing evaluation across three continents with a unified preprocessing pipeline and five conceptually distinct evaluation axes (fidelity, diversity, proportionality, usefulness, generalization) addresses a real reproducibility gap in the trajectory generation literature.

## Weaknesses

### Fatal
None.

### Major

- **Zero-shot transfer still requires target-city aggregate data.** Algorithm 2 (line 3) computes the spatial prior H from target-city trajectories (X_target). This means zero-shot cross-city transfer is not truly data-free for the target—it requires running target trajectories through the heatmap estimator. The paper does not quantify how many target observations are needed to estimate H reliably. If H requires a large number of target trajectories, the "zero-shot" claim is substantially weakened for genuinely data-scarce scenarios. The paper should clarify this dependency and ideally test sensitivity to target-data volume.

- **Comparison fairness against baselines.** The baselines (TimeGAN, DiffTraj, Diffusion-TS, etc.) are global models trained on all city trajectories jointly, while TDDM inherently trains and generates at the regional (3×3 km) scale. This regional decomposition acts as a form of data augmentation and implicit spatial regularization. The ablation "w/o spatial prior" retains the regional training structure and still substantially outperforms global baselines (KL_sym 1.334 vs. 1.153 for Diffusion-TS), suggesting that part of the gain comes from regional training rather than the spatial prior specifically. Adapting at least one baseline (e.g., Diffusion-TS) to the same regional training paradigm would isolate the contribution of the spatial prior conditioning.

### Minor

- **Missing ablation on canonicalization.** The paper claims canonicalization enables cross-city transfer, but the ablation study tests only the removal of spatial priors and region size variation. A version with spatial priors but without canonicalization (i.e., in raw geographic coordinates) would directly test whether coordinate normalization is necessary for generalization and how much it contributes.

- **KL divergence estimation details are absent.** For large-scale 2D data, KL divergence estimates from finite samples are sensitive to binning resolution and sample size. The paper reports KL values to three decimal places without describing the estimation procedure (grid resolution, smoothing, number of generated samples). This affects the reliability of the primary metric.

- **Trajectory stitching across region boundaries is unaddressed.** At inference time, a grid of overlapping 3×3 km regions tiles the city. The paper mentions "partial border overlap" but does not describe how trajectories straddling boundaries are handled or whether stitching introduces discontinuities.

- **"Universal source dataset" finding is unexplained.** The observation that Porto-trained models generalize better than partial local data is highlighted as significant but unsupported by any mechanistic analysis. A brief discussion of Porto's dataset properties (trajectory density, road network diversity, trip-length distribution) would strengthen the scientific value of this finding.

### Trivial

- The paper description writes "KL_apeed" and "KL_peeed" in tables—likely OCR artifacts from "KL_speed"—but given parser instructions, these are not counted against the paper.

## Nice-to-Haves

- Sensitivity analysis on the number of target-city trajectories needed to estimate H reliably would clarify the practical requirements for zero-shot transfer.
- A comparison or ablation including a regional Diffusion-TS baseline (same 3×3 km partition, no spatial prior) would make the ablation table more informative.
- Reporting variance for KL/JS metrics in Table 1 (not just TSTR) would improve confidence in the comparisons given single-run evaluation.

## Novel Insights

The paper's most genuinely novel insight is that *aggregate spatial distributions serve as transferable conditions precisely because they decouple location identity from motion dynamics*. Unlike sample-specific conditioning (which binds the model to individual trajectories and risks memorization), marginal occupancy distributions encode structural constraints—road networks, population density patterns—that are shared across cities at the appropriate scale. The canonicalization mechanism then makes these constraints location-agnostic, so the model can apply learned urban motion primitives anywhere. The incidental finding that Porto may represent a "universal" source dataset hints at a broader principle: some cities encode temporal dynamics that are broadly representative across urban mobility, which could guide principled dataset selection for cross-domain trajectory modeling.

## Suggestions

- Clarify and quantify the target-data requirement for spatial prior estimation in zero-shot settings (a sensitivity curve over number of target trajectories would be ideal).
- Add a regional Diffusion-TS ablation to isolate spatial-prior conditioning from regional training benefits.
- Add an ablation removing canonicalization to directly validate the cross-city transfer claim.
- Describe the KL divergence estimation procedure (grid resolution, sample count, smoothing) to ensure reproducibility.
- Discuss how boundary trajectories are handled during regional stitching.

## Score and Decision

TDDM presents a clean and principled idea—factorizing spatial occupancy priors from temporal dynamics—backed by large and consistent empirical gains across diverse datasets and a useful community benchmark. The zero-shot cross-city transfer experiments are genuinely novel for this problem class. The main unresolved concerns (target-data requirements for zero-shot transfer, comparison fairness against a regional baseline) are real but do not invalidate the core contribution. The method is clearly doing useful work as demonstrated by the ablations, and the benchmark is independently valuable. This sits solidly above the ICLR 2026 acceptance boundary.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>