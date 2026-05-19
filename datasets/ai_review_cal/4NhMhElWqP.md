- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8
Now I have a thorough understanding of the paper and all reviewer inputs. Let me construct the final consolidated review.

## Summary
The paper proposes DAM (Deep data-dependant approximate analytical model), a transformer-based model for universal time series forecasting. Its key innovations are: (1) a long-tail History Sampling Regime (HSR) that irregularly samples context points to efficiently capture both recent and distant temporal structure, and (2) forecasting via explicit continuous basis functions (sine/cosine compositions) whose coefficients are the model output, enabling arbitrary-horizon prediction without retraining. A single univariate DAM trained on 25 datasets is evaluated across long-term forecasting, zero-shot held-out transfer, very-long-term forecasting, and imputation, achieving competitive or state-of-the-art results against specialized per-dataset baselines.

## Strengths

- **Continuous-time basis function output genuinely removes the fixed-horizon barrier (Section 3.3, Equation 2).** The forecasting mechanism is a continuous function of time parameterized by learned basis coefficients. Section 4.3 concretely demonstrates this advantage: the same trained DAM produces meaningful 5000-step forecasts on the Weather dataset, while PatchTST and DLinear trained specifically for those horizons fail to produce useful outputs. This is a fundamentally different capability from existing vector-output models.

- **HSR enables a global temporal perspective at the same sample cost (Section 3.2, Figure 2).** The Cauchy-like long-tail distribution (Equation 1) allows the model to sample distant history points with higher probability than uniform sampling while retaining focus on the recent past. Figure 2 provides a direct visual comparison showing that HSR-based context covers much more of the signal history than regular sampling with the same number of points.

- **A single model achieves the most top metrics across 18 long-term forecasting datasets (Table 1).** The DAM (trained once) achieves 39 of 80 top metrics across 18 datasets and 4 horizons, while the closest competitor (PatchTST) requires separate training for each of the 40 dataset-horizon combinations and achieves 28. The held-out experiments (Table 2) provide even cleaner evidence: the DAM achieves state-of-the-art on 14 of 16 metrics across 8 held-out datasets in zero-shot mode, and in several cases outperforms baselines trained from scratch on the target data.

- **Interpretability via explicit frequency decomposition and attention (Section 5.1, Figures 5–6).** The basis function composition allows the forecast to be decomposed into low-to-high frequency components (Figure 6), and attention weights can be visualized per token (Figure 5). The model learns interpretable patterns—high basis coefficients at daily and weekly frequencies for the ETT datasets, for example. This is a level of transparency not typical for forecasting models.

- **Flexible inference cost without retraining (Section 5.3, Figure 7).** The same trained DAM can trade off inference time for accuracy by adjusting the HSR context size at test time, with MSE decreasing approximately exponentially while cost increases linearly. This is a practical advantage for deployment across environments with different compute budgets.

## Weaknesses

### Fatal
None.

### Major

- **The imputation evaluation (Table 3, Section 4.4) lacks sufficient detail on baseline protocol and framing clarity.** The paper presents DAM imputation using only basis function initialization (θ₀) with no backbone training, reporting lower MSE than TimesNet (which the paper notes "evidenced SoTA performance on the imputation task"). However, the paper does not describe how the comparison baselines were applied—whether they were re-trained for imputation, used out-of-the-box forecasting models for gap-filling, or followed their original papers' protocols. Without this detail, it is unclear whether the comparison is a valid benchmark or a demonstration of a fundamentally different (and not directly comparable) approach to filling missing values. The section should either provide full baseline imputation methodology or be reframed as a demonstration of the DAM's reconstruction capability rather than a competitive claim.

### Minor

- **The in-distribution comparison (Table 1) has an acknowledged but under-discussed asymmetry.** The DAM was trained on 25 datasets that *include* the 10 evaluation datasets, while baselines were trained per dataset-horizon. The paper argues (reasonably) that generalizing across many datasets is harder than specializing, but this is a different comparison than "model A beats model B at the same task." Additionally, the headline tally of "39 of 80" conflates the standard DAM (no per-dataset tuning) with DAM_HSR-tuned (context size and σ selected per dataset on validation). The paper states this transparently, but reporting separate tallies would allow readers to distinguish inherent generalization from per-dataset tuning.

- **No ablation or sensitivity analysis on the basis frequency set (Section 3.3).** The 437 frequencies are selected by concatenating even samples across minute-to-year ranges. Since the basis function composition is central to the forecasting mechanism, the paper should show sensitivity to this choice (e.g., reduced set, coarser resolution). Without such analysis, it is unclear whether performance depends on careful frequency engineering or is robust to the choice.

- **The architecture ablation (Table 4) is limited to ETT datasets only.** While the results clearly show the cross-basis feed-forward block (FF_B_cross) is critical, confirming these findings on a more diverse subset of datasets (e.g., Weather, ECL, Traffic) would strengthen the claim that the findings generalize.

- **Statistical significance is not reported.** Results are averaged over only 3 seeds without confidence intervals or standard deviations. For close comparisons in Table 1, it is unclear whether differences are meaningful or within noise.

- **Very-long-term forecasting (Section 4.3) does not fully describe the baseline training protocol.** The paper states PatchTST and DLinear were "trained on this horizon" but does not specify their context length, training configuration, or whether they were optimized specifically for very-long horizons. Since these methods were designed for horizons up to 720 steps, training them for 5000-step outputs may place them at a disadvantage that is not solely about model capability.

### Trivial

- The "39 of 80" tally would be more informative if reported separately for standard DAM and DAM_HSR-tuned.
- Baseline implementation sources and hyperparameter settings are not specified beyond "trained to specialise."

## Nice-to-Haves

- A controlled ablation isolating the effect of the HSR (comparing DAM with uniform sampling vs. HSR sampling) would directly test whether the long-tail distribution is the source of the model's generalization advantage.
- Reporting the optimal HSR context size and σ values selected per dataset for the HSR-tuned variant would aid reproducibility and give insight into how much tuning is needed per dataset.
- A discussion of training time and memory usage relative to baselines would be useful context for the "foundation model" framing.

## Removed Points

*These points were flagged for removal; treat with caution.*

- **Criticism about missing related works (Lag-Llama, TimesFM, MOMENT).** Removed per rule: the reviewer cannot confirm the existence or timeline of these references relative to the paper's submission.
- **Criticism about potential data leakage between train/test splits.** The paper includes evaluation datasets in the training set (which it acknowledges) but this is about *which datasets* are used, not about temporal split overlap within datasets. The concern is speculative without further evidence.
- **"The first model" claim being too strong.** This is the authors' characterization of their contribution; it is defensible given the HSR + continuous basis function combination. The paper qualifies it ("to the best of our knowledge").
- **Several generic "Strengthening the Paper on Its Own Terms" suggestions** (e.g., discuss limitations more concretely, show where DAM fails). These are reasonable suggestions but are framed as weaknesses-of-omission rather than identified flaws in the presented work. Moved here to avoid inflating the weakness count.
- **Runtime/memory criticism.** Noted in the nice-to-haves; it is not a weakness of the presented results.

## Novel Insights

The synthesis of the two reviews reveals a subtle point that neither reviewer fully articulated: the DAM's strongest experimental evidence (held-out zero-shot transfer in Table 2) and its most novel methodological component (the HSR + continuous basis function output) are tightly coupled but not directly causally linked by any experiment in the paper. The held-out results convincingly demonstrate generalization across domains, but the mechanism driving that generalization could be any combination of: (a) the HSR's access to global temporal structure, (b) the inductive bias of the sinusoidal basis functions, (c) training on diverse multi-domain data, or (d) the continuous-output formulation. Isolating these factors through targeted ablations (uniform sampling baseline, neural output head instead of basis functions) would substantially strengthen the paper's scientific contribution beyond what either reviewer explicitly called for.

## Suggestions

1. **Clarify the imputation evaluation.** State explicitly how each baseline (TimesNet, PatchTST, etc.) was applied to the imputation task—cite exact protocols, whether models were re-trained, and whether the comparison is apples-to-apples. If the baselines were not originally designed for imputation, either train them properly for masked reconstruction or reframe the section as a demonstration of reconstruction capability rather than a competitive benchmark.

2. **Report separate tallies for standard and HSR-tuned DAM in Table 1.** This lets readers see how often the zero-tuning variant (fixed context 720, σ=720) beats or ties baselines, separate from the per-dataset tuned variant.

3. **Add a frequency-set ablation.** Show results with, e.g., 100 frequencies, only frequencies within the training datasets' periodicities, or a coarser frequency grid. This would address concerns about whether performance relies on careful frequency engineering.

4. **Add an HSR ablation.** Compare the DAM with a uniform-sampling baseline (same number of context points, uniformly sampled over history) to isolate the effect of the long-tail distribution. This directly tests a core claimed contribution.

5. **Report confidence intervals or standard deviations** across seeds for the key comparison tables.
