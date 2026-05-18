## Summary

This paper identifies that sliding-window-based forecasting models fail to capture long-term variations extending beyond the window length, and proposes AutoCon — a self-supervised contrastive loss that uses global autocorrelation (computed from the entire series) to define positive/negative pairs between windows arbitrarily far apart in time. This loss is combined with a redesigned decomposition architecture that separates short-term (linear) and long-term (TCN encoder + multi-scale moving average decoder) branches. On nine datasets with prediction lengths extended up to 2160 steps, the model achieves 42 first-place finishes and average error reductions of 12% at the longest horizons compared to the second-best method.

## Strengths

1. **Empirically demonstrates a genuine, overlooked problem**: The paper provides concrete evidence (Figure 1) that time series contain non-zero autocorrelations and Fourier components well beyond conventional window sizes, and shows (Figure 2) that existing models (PatchTST, TimesNet) produce near-constant representation similarities across distant windows, confirming they fail to capture long-range dependencies. This diagnosis directly motivates the solution.

2. **Novel contrastive loss (AutoCon) that learns cross-window dependencies without augmentation**: The loss (Equation 4) uses the global autocorrelation to define relative positive/negative pairs across arbitrarily distant windows in a batch, avoiding the common limitation of contrastive methods that only consider temporally close samples. The ablation study (Table 3, Figure 5b) confirms that removing AutoCon degrades long-term performance substantially (e.g., ETTh2 at O=2160: MSE rises from 0.198 to 0.236).

3. **Strong empirical results on extended long-term forecasting**: Across nine diverse benchmarks, the model achieves 42 first-place results with prediction horizons extended to 2160 steps (Table 1). The improvements are most pronounced at the longest horizons (12% average error reduction at 1440/2160), directly validating the core claim. Results are consistent across multiple data domains (electricity, traffic, weather, economics, disease).

4. **Principled analysis linking method effectiveness to data properties**: Figure 4 shows that datasets with stronger outer-window autocorrelation (ETTh2, Electricity) yield larger improvements (34%, 11%), while Weather with weaker correlation shows only 3% improvement. This evidence supports the mechanism and honestly bounds what the method can achieve.

5. **Well-controlled ablation and computational efficiency**: The ablation study (Table 3, Figure 5b) isolates each architectural component — removing the short-term branch hurts short horizons, removing the long-term branch hurts long horizons, and removing AutoCon degrades both. The method is also computationally efficient (33.2 ms/iter) compared to Transformer-based models (365.7+ ms/iter).

## Weaknesses

### Fatal

None.

### Major

1. **Multivariate evaluation is too limited to support claims of generality.** The paper shows multivariate results (Table 5) only on the four ETT variants, with modest improvements (e.g., ETTh2: 0.372 vs 0.414; ETTm2: 0.281 vs 0.291). No multivariate results are reported on Electricity, Traffic, Weather, Exchange, or ILI — datasets that feature prominently in the univariate main results. The paper's claim of outperforming 14 models across nine benchmarks is based on univariate experiments; the multivariate evaluation covers only one data source (ETT) and does not establish that the method generalizes beyond this setting. Given that multivariate forecasting is critical for practical deployment, this omission significantly weakens the generality claim. **Why it matters:** The contribution would be substantially less impactful if the method only works well in univariate mode or on ETT-family data.

### Minor

2. **Batch composition sensitivity is not analyzed.** AutoCon's relative selection strategy defines positive/negative pairs based on ordering within a batch. If a batch happens to contain windows that are mostly temporally close (with similar autocorrelations), the ordering may collapse and the gradient signal could weaken. The paper asserts that "a mini-batch can consist of windows that are temporally far apart" (lines 114-115) but provides no empirical diagnostic — such as a histogram of pairwise lags in training batches, or loss stability across different batch sizes — to verify that informative negatives are reliably available. The concern is theoretical rather than demonstrated to cause failure, but the core mechanism depends on this assumption. **Why it matters:** Without analysis, it is unclear whether the method's performance is robust to dataset length, batch size, and sampling strategy.

3. **Autocorrelation as the sole relationship measure is a strong assumption with no alternatives tested.** The paper defines window relationships as r(T₁, T₂) = |R_SS(|t₁-t₂|)|, which assumes (a) the series is sufficiently stationary for autocorrelation to be meaningful at large lags, and (b) linear correlation adequately captures similarity between distant windows. The paper acknowledges the linearity limitation in the Discussion (lines 472-474) but does not test alternative measures (e.g., mutual information, time-warped correlation) or verify that autocorrelation ordering correlates with actual forecasting-relevant similarity. The analysis in Figure 4 partially addresses this by showing the method works better when autocorrelation is stronger, which is consistent with the mechanism but also circular — improvement is predictably marginal when the loss signal is weak. **Why it matters:** A controlled comparison against an alternative similarity measure would strengthen confidence in the design choice.

4. **No statistical significance or multi-seed variance reported.** Given that many comparisons show small margins, reporting results from a single run makes it impossible to assess whether improvements are statistically reliable. Standard deviations across 3–5 seeds are a standard expectation. **Why it matters:** Without this, some of the claimed improvements (especially the smaller ones) may not be replicable.

5. **Encoder timestamp integration is underspecified.** The paper states the encoder "leverages both sequential information and global information (i.e., timestamp-based features derived from 𝒯)" (line 181) but does not describe how timestamps are incorporated — whether as additional channels, positional embeddings, conditioning inputs, or otherwise. This makes the architecture harder to reproduce. **Why it matters:** Reproducibility requires this detail.

### Trivial

6. **Minor inconsistency between text and equation for the negative pair condition.** The text (line 137) describes negative pairs as having "global autocorrelation *lower than* that of the anchor pair" (strict inequality), but Equation 4 uses ≤ in the indicator function. This means pairs with equal autocorrelation are treated as negative, which the text does not clarify. The formulation itself is not broken (including the positive in the denominator is standard practice in contrastive learning), but the text-equation mismatch should be resolved.

7. **Autocorrelation estimation procedure is unspecified.** The paper computes the global autocorrelation once from the training set without describing the estimator (biased vs. unbiased, whether truncation is applied, how boundary effects at large lags — where few point pairs contribute — are handled). Large-lag estimates may have high variance, particularly for moderate-length datasets. A brief description and/or sensitivity analysis would strengthen the paper.

## Nice-to-Haves

- **Validate representation ordering.** For a held-out set of windows, plotting true pairwise autocorrelation vs. learned representation cosine similarity would directly test whether AutoCon's optimization is achieving the intended monotonic relationship. The paper already presents a qualitative version in Figure 2 (representation similarities for one anchor), but a systematic plot across all pairs would be more informative.
- **Synthetic data experiment.** A controlled experiment with synthetic data of known periodicities would isolate AutoCon's contribution from architectural choices and directly test whether the loss recovers the correct representation structure.
- **Multivariate results on at least 2–3 additional datasets** (e.g., Electricity, Traffic) would substantially strengthen the generality claim.

## Removed Points

These points were flagged by reviewers but are removed or downgraded per the review guidelines; treat them with caution:

1. **"Denominator includes the positive, breaking the contrastive formulation"** — Removed as factually incorrect. Standard contrastive formulations (InfoNCE, NT-Xent) routinely include the positive sample in the denominator. The only real issue is the ≤ vs. strict inequality text-equation inconsistency, which is kept as Trivial (#6 above).
2. **Generic praise from Strength Finder** — Some claimed strengths were redundant (e.g., "this paper addressed an important problem") and dropped. The retained strengths are specific and evidence-backed.
3. **"Missing related works"** — Not mentioned by any reviewer; no action needed.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses converge on the same picture: the method is well-motivated and empirically strong in its primary (univariate, long-horizon) setting, but the multivariate evaluation is too narrow to support broad claims of generality, and several auxiliary analyses (batch diagnostics, autocorrelation alternatives, multi-seed variance) are missing. These gaps reduce confidence in the method's robustness but do not undermine its core empirical achievements.

## Suggestions

1. **Expand multivariate experiments** to at least 2–3 non-ETT datasets (Electricity and Traffic are natural candidates) to demonstrate generality beyond the ETT family.
2. **Add multi-seed results** (3–5 seeds with mean ± std) for at least the main results table to establish statistical reliability.
3. **Provide a batch diagnostic** (e.g., distribution of pairwise lags in training batches, or loss curves across batch sizes) to address the batch composition concern.
4. **Specify the encoder's timestamp integration mechanism** (e.g., "timestamps are embedded via learned positional encodings concatenated with the input channels").
5. **Resolve the ≤ vs. strict inequality inconsistency** in Equation 4's text description.
6. **Describe the autocorrelation estimator** (biased or unbiased, any truncation), and optionally include a sensitivity analysis for large-lag estimates.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>