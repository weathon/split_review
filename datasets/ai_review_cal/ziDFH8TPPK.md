- Decision: Accept
- Avg Score: 6.25
- Scores: 3, 6, 8, 8
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

The paper proposes LT3P, a framework for typhoon trajectory prediction that uses real-time Unified Model (UM) NWP data instead of ERA5 reanalysis data (which has a 3-5 day latency). The approach has two phases: (1) pre-train a physics-conditioned encoder on ERA5 to learn atmospheric representations, and (2) train a bias corrector that maps UM data to the ERA5 distribution, then use the corrected representations (via cross-attention) for trajectory prediction up to 72 hours ahead. The paper also releases the PHYSICS TRACK dataset and shows strong results against data-driven baselines.

## Strengths

- **Real-time +72h prediction without reanalysis data at inference:** The paper's core contribution — replacing ERA5 (3-5 day latency) with real-time UM data (≈3-hour delay) via learned bias correction — is practically significant and well-motivated. The framework design is novel and sensible: pre-train on high-quality but delayed data, then adapt to real-time data. Evidence: The full pipeline achieves 143.03 km FDE at 72h (Table 1, bias-corrected UM ensemble), outperforming all data-driven baselines that also use only real-time inputs.

- **Bias-correction framework is validated as critical:** The ablation study (Table 5) shows clear evidence that the bias corrector is essential — adding it to the pipeline drops FDE from 198.11 km → 143.03 km (a ~28% improvement). The qualitative visualization (Figure 5) further confirms the bias corrector reduces the UM-to-ERA5 discrepancy in zonal wind fields.

- **Systematic ablation and backbone generality:** The paper ablates each component (UM-only, joint training, pre-training, bias correction) and also shows the LT3P framework improves three different backbone trajectory predictors (GAN, CVAE, diffusion). This demonstrates the contribution is in the framework, not a specific architecture choice. Evidence: Tables 5 and 6.

- **Dataset and code release:** The paper commits to releasing the PHYSICS TRACK dataset (ERA5, UM, best-track aligned) along with code and pretrained weights, enabling reproducibility and downstream use (stated in abstract and conclusion).

## Weaknesses

### Fatal

None.

### Major

- **Comparison with operational NWP models is not properly controlled for identical test conditions.** The paper claims to "outperform NWP-based typhoon trajectory forecasting models by significant margins" (line 63), but the NWP numbers (JTWC, JMA-GEPS, ECMWF-EPS, NCEP-GEFS, UKMO-EPS) are cited from Chen et al. (2023) without stating whether those evaluations used the same 90 test typhoons (2019–2021) or the same filtering criteria. The paper does note that MMSTN and MGTCF results (from prior work) "were evaluated only in 2019" (Table 1 note), but no equivalent note exists for the NWP values. Without establishing test set overlap, the headline claim of surpassing operational forecast centers by "significant margins" is not rigorously supported. The technical contribution (using bias-corrected UM instead of ERA5) is valuable regardless — this weakness is about the evaluation claim outrunning the evidence, not about the method itself.

### Minor

- **Remarkably low short-lead errors lack analysis or a persistence baseline.** The ensemble FDE at 6 hours is 6.30 km (bias-corrected UM) and the stochastic FDE is 1.97 km. No persistence baseline ("typhoon stays where it is") is reported to contextualize these numbers. Given that the UM input has a 3-hour data acquisition delay, the model may be learning a near-identity mapping at very short leads. The paper should report (a) a persistence baseline on the same test set and (b) the distribution of raw UM errors vs. ERA5 by lead time to show how much improvement actually comes from the bias corrector vs. the inherent accuracy of short-range UM forecasts.

- **Ablation reveals pre-training hurts without bias correction, but this is not discussed.** In Table 5, "Joint Training" alone (80.39/190.75) outperforms "Joint+Pre-Training" without bias correction (85.62/198.11). The paper states "all components, barring the UM Only training, yield good results" — this glosses over the fact that pre-training degrades performance by ≈4% relative to joint training alone. The role of pre-training should be clarified: is it essential, or would end-to-end training (jointly learning the encoder and bias corrector) work as well? This omission weakens the claimed design rationale.

- **Stochastic evaluation uses best-of-20 (oracle) metric, which differs from the NWP ensemble-mean evaluation.** The paper reports "the results have the lowest error among 20 generated trajectories" (line 340). This is standard in trajectory prediction literature and is transparently stated, but it means the stochastic numbers in Table 2 represent an upper bound that no real system could achieve. The comparison to NWP models is in Table 1 (ensemble mean), so this does not affect the main NWP claim — but the paper should also report the ensemble mean of the 20 stochastic samples for completeness, so readers can compare like-with-like.

### Trivial

None.

## Nice-to-Haves

- **Report the persistence baseline** on the test set to contextualize the very low 6-hour errors.
- **Show standard deviation or error bars** for the main results (90 test typhoons is sufficient for meaningful variance estimates).
- **Provide a quantitative breakdown of UM bias vs. ERA5 by forecast lead time** to support the claim that bias correction is meaningfully improving over raw UM at each lead time.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"Related work discussion of human trajectory prediction is padding"** — This is a subjective style opinion, not a substantive weakness. The paper connects both fields and notes their differences.

2. **"Pre-training task lead time not specified"** — The paper does specify the temporal setup. Input dimension is B×12×9×240×320 (12 timesteps at 6-hour intervals = 72 hours), and Eq. (4) states the model predicts from time t to t+t_f given input from t-t_f to t.

3. **"Table 1 Dataset column is confusing"** — The table clearly marks BST/ERA5/UM columns for each method, and the paper explains the different input modalities (line 326). The comparison acknowledges MGTCF uses ERA5 at inference.

4. **"Only a few qualitative examples shown"** — This is typical for papers and not a substantive weakness; the examples shown are representative.

5. **"Missing UM forecast lead time details"** — The paper states UM has a "3-hour data acquisition delay" and that the UM forecast at +72 hours differs from ERA5 (Figure 1 caption). The temporal setup is adequately described for the paper's scope.

6. **"Missing statistical significance/variance"** — Single-run evaluation on fixed benchmarks is standard practice in this area. Not a weakness specific to this paper.

7. **"Reproducibility / missing appendix details"** — The parser strips appendix content; these exist in the original submission. The paper promises dataset and code release.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a pattern or implication that the authors themselves had missed.

## Suggestions

1. **Clarify the NWP comparison.** Either (a) obtain and report the NWP forecast errors on exactly the same 90 test typhoons (2019–2021), or (b) explicitly caveat that the NWP numbers are from a prior evaluation (Chen et al., 2023) and may not use the identical test set, and temper the "outperforming NWP" claim accordingly.

2. **Add a persistence baseline** to the main table. This is trivial to compute and would anchor the very low short-lead errors in a meaningful way.

3. **Acknowledge the pre-training degradation** in the ablation discussion. Explain whether pre-training is still necessary (e.g., for convergence speed or data efficiency) or whether an end-to-end training approach could replace the two-stage design.

4. **Report ensemble-mean results for stochastic predictions** alongside the best-of-20 numbers, so readers can see both the upper bound and the average-case performance.

5. **Show UM error distribution by lead time** (e.g., raw UM FDE vs. ERA5 before correction) to quantify what the bias corrector contributes at each horizon.
