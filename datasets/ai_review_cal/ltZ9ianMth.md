- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 5, 5, 6
Now I have thoroughly verified all claims. Let me produce the final consolidated review.

## Summary

This paper addresses robust time series forecasting under anomalies (TSFA). It defines three anomaly types (Constant, Missing, Gaussian), analyzes loss robustness (anomalies in Y) and sample robustness (anomalies in X), and proposes RobustTSF — an algorithm combining L1 trend filtering with position-weighted anomaly scoring and MAE-based sample selection. Experiments on Electricity and Traffic datasets show consistent improvements over baselines.

## Strengths

- **Empirical demonstration that anomaly position matters (Section 4, Table 1):** Controlled experiments clearly show that anomalies near the label degrade performance far more than those at the front or middle of the input window, even at the same anomaly rate. This insight directly motivates the position-dependent weighting in the algorithm. The finding is intuitive but well-demonstrated.

- **Consistent empirical superiority across diverse settings (Section 6, Tables 2-4):** RobustTSF achieves the best MAE/MSE on essentially all anomaly types (Constant, Missing, Gaussian), rates (0.1, 0.3), datasets (Electricity, Traffic), and forecasting horizons (single-step, multi-step with O=4,8). Improvements over vanilla MAE are substantial (e.g., Electricity, Constant η=0.3: RobustTSF 0.183/0.070 vs. Vanilla MAE 0.206/0.086). The low Δ values (0.003–0.004) also demonstrate superior training stability.

- **Generalization to subsequence anomalies and heavy-tailed distributions (Section 6.3, Table 4):** RobustTSF outperforms all baselines on subsequence anomalies modeled by a Markov process with ϕ from 0.1 to 0.9, showing robustness beyond point-level anomalies. This broadens practical applicability.

- **Ablation study validating design choices (Section 6.4, Table 5):** Comparing MAE vs. MSE, Dirac vs. exponential weighting, and trend filter vs. prediction-based detection confirms that the full RobustTSF (MAE + Dirac + trend filter) yields the best performance across all anomaly types. This provides evidence that each component contributes.

## Weaknesses

### Major

- **Proposition 1 (MAE robustness to Constant/Missing anomalies) is not justified by the stated theory (Section 3, Proposition 1).** Theorem 1 provides a *sufficient* condition for robustness: ℓ(f(x), y) + ℓ(f(x), y^A) = C_x (constant w.r.t. f). The paper asserts "From Theorem 1, MAE is robust to Constant and Missing type anomalies" without verifying that MAE satisfies this condition. Checking directly: for Constant anomaly (y^A = y + ε), MAE gives |f−y| + |f−y−ε|, which is *not* globally constant w.r.t. f (it equals ε only when f ∈ [y, y+ε], and grows unboundedly outside this interval). The same issue holds for Missing anomalies (y^A = ε). Therefore Proposition 1 does not follow from the presented reasoning. This undermines the paper's claim of providing a "theoretically grounded" bridge between LNL and TSFA. The algorithm's empirical success is independent of this theory, but the theoretical framing of the paper is overclaimed and the central justification for labeling MAE as the "robust loss" is unsupported as presented. **This does not invalidate the empirical contributions**, but the paper should either (a) correct the theoretical analysis or (b) honestly recharacterize Section 3 as empirical motivation rather than rigorous proof.

### Minor

- **Fixed threshold τ = 0.3 without ablation study (Section 6.4).** The hyperparameter tuning section compares loss type, weighting, and detection method, but does not ablate τ, λ, or K'. The paper maintains τ=0.3 uniformly across all datasets, anomaly types, and rates without studying sensitivity. While the consistent good results suggest some robustness to this choice, the paper's claim that τ "yields favorable results across diverse datasets and settings" would be stronger with a systematic ablation.

- **Limited experimental scope: two datasets, one architecture.** All main experiments use only Electricity and Traffic datasets with LSTM models. Multi-step forecasting is only on Electricity, not Traffic. While LSTM is standard in prior TSFA work, evaluating on at least one additional dataset (e.g., from the benchmarks cited in the introduction) and one additional architecture (e.g., Transformer) would significantly strengthen the generality claims.

- **Baseline tuning not fully documented.** The Offline/Online imputation baselines require anomaly detection thresholds, but the paper does not report how these were chosen. Some settings show baselines performing close to or slightly worse than vanilla MAE, making it unclear whether they are well-tuned. The consistent RobustTSF advantage across all settings mitigates this concern, but full documentation would remove doubt.

- **No variance or confidence intervals reported.** Results are reported as point estimates without standard deviations or error bars. Given that differences in some settings are modest (e.g., Clean setting), the reader cannot assess statistical significance.

### Trivial

- The Dirac weighting with K'=K-1 effectively checks only the last time step, but the paper could more clearly justify this design choice and discuss when it might be insufficient (e.g., longer horizons).

## Nice-to-Haves

- Adding runtime comparisons to substantiate the claim of efficiency over detection-imputation pipelines.
- A sensitivity study on the trend filtering parameter λ.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim that Theorem 2 (Gaussian robustness) is "trivially true"**: While the result follows from zero-mean noise, formalizing this connection for the TSFA regression setting is a legitimate contribution. The critic correctly notes the population-level vs. finite-sample distinction, which the paper itself acknowledges (line 118). Not a real weakness.

- **Harsh critic's claim that baselines underperform vanilla MAE "suspiciously"**: The critic speculates about poor baseline tuning. The paper does not report thresholds, but a method that consistently underperforms a simpler baseline is not suspicious — it is evidence that the detection-imputation pipeline is noisy. This is precisely the paper's critique of those methods. The concern is valid only as a documentation gap (moved to Minor above).

- **Strength Finder's claim about "formal proof that MAE is robust to Constant/Missing anomalies"**: This strength is removed because, as noted in Major weakness #1, the proof is not correctly justified. The strength conflicts with a verified weakness.

- **Harsh critic's claim about "trend filtering optimization not described"**: The paper references Kim et al. 2009 for the original algorithm and describes the L1 modification. Citing the original work for solver details is standard. Not a weakness.

- **Strength Finder's claim about "first formal connection between LNL and TSFA (Equation 15)"**: This claim is weakened by the theoretical flaw in Proposition 1. While the paper does present Equation (15), the foundation for why MAE works for Constant/Missing anomalies is unsupported.

- **Harsh critic's speculation about "boundary effects in Table 1 due to padding"**: This is a speculative concern without evidence in the paper. The experiments are cleanly set up.

## Novel Insights

None beyond the paper's own contributions. The key insight — that anomaly position near the label matters more for forecasting performance — is empirically demonstrated and well-motivated. The position-weighted scoring scheme is a practical takeaway. However, the reviews do not surface any fundamentally new interpretation or connection that the paper itself does not already articulate.

## Suggestions

1. **Fix the theoretical justification.** The simplest path is to drop the claim that Proposition 1 follows from Theorem 1 and instead present it as empirical motivation (note that MAE empirically works better, and the LNL literature provides independent reason to expect robustness). Alternatively, provide a correct proof — for example, by noting that while the condition in Theorem 1 is not satisfied globally, the sum ℓ(f,y) + ℓ(f,y^A) for MAE under Constant anomalies has a unique minimum on [y, y+ε], which may provide a different form of robustness. Either way, the paper should be honest about what is and is not proven.

2. **Add an ablation study for τ** (and optionally λ and K'). Show performance across at least 3-5 values of τ on one dataset/anomaly setting to demonstrate robustness or provide guidance for setting it.

3. **Expand the experimental evaluation** to include at least one more dataset and one more architecture (e.g., a simple Transformer or MLP). Report results with at least 3 random seeds and include standard deviations.

4. **Document baseline configuration** — state explicitly how thresholds were set for Offline/Online imputation baselines.
