I have read and verified the paper thoroughly. Let me now produce the final consolidated review.

---

## Summary

The paper addresses the Lookback Window Limitation (LWL) in long-term time series forecasting, where Transformer-based models fail to benefit from longer input windows beyond a certain point. It proposes two model-agnostic modules: the Information Bottleneck Filter (IBF), which uses noise-injection variational IB to select informative subsequences and filter redundancy, and the Hybrid-Transformer-Mamba (HTM), which splits input sequences into shorter blocks processed by a Transformer while Mamba captures global dependencies — reducing complexity from quadratic to approximately linear. Combined with patching, the resulting PIH model extends the lookback window to 1024 (longer than typical prior work) and achieves state-of-the-art results across seven benchmark datasets.

## Strengths

1. **Convincing demonstration of overcoming LWL for the core model.** Figure 3(a) shows the average MSE of PatchTST improves from L=96 to L=512 but declines at L=1024, while PIH improves monotonically from L=96 to L=1024. This directly validates the central claim that the proposed modules enable productive use of longer windows, and the figure averages over all 7 datasets and all 4 prediction horizons, providing robust evidence.

2. **Model-agnostic modules generalize across architectures.** Section 4.2 integrates IBF and HTM into Transformer, Informer, and Autoformer. Figure 5 shows performance-vs-window curves for three datasets (ETTm1, Electricity, Traffic), with triangular markers indicating that the window limitations are raised (e.g., on ETTm1 from 48 to 192, on Traffic from 120 to 228). This demonstrates generality beyond PatchTST.

3. **Substantial computational efficiency gain.** Figure 3(b) reports that HTM (without IBF) reduces runtime and memory by 2–3× relative to pure Transformer (PatchTST) and also outperforms pure Mamba (PatchTSM). IBF adds negligible overhead since it consists of only an MLP. This makes very long windows practical.

4. **Component ablation confirms individual contributions.** Figure 6 (left) shows that adding either IBF or HTM individually to PatchTST improves average MSE, and combining both yields the best result. This validates the design rationale for both modules.

5. **Principled optimization of information bottleneck for patch sequences.** The paper derives a tractable variational upper bound via noise injection (Eqs. 8–10), relaxing the combinatorial discrete selection problem into a differentiable objective with a Gumbel-sigmoid reparameterization. This is a technically sound adaptation of VIB to the time series patch setting.

## Weaknesses

### Fatal
None.

### Major

1. **IBF's specific selection mechanism is not causally validated.** The paper claims IBF filters redundant information and identifies important subsequences, but no experiment compares IBF-selected patches against (a) randomly selected patches (same number), (b) uniform downsampling, or (c) no selection (full sequence). The ablation study (Fig. 6) shows that adding IBF improves over PatchTST, but this could be due to any of: the noise injection regularization, the added Mamba layer before IBF, the extra parameters, or the selection mechanism specifically. Without controlling for these confounds, the paper's attribution of improvement to information bottleneck-guided selection specifically is unsupported. The interpretability claim (Fig. 3c, one sample from Electricity) is purely anecdotal — no analysis confirms the selected patches correspond to meaningful temporal patterns.

2. **No statistical significance or variance reporting.** All results are single MSE/MAE point estimates without error bars, confidence intervals, or multiple runs. Time series forecasting can be sensitive to random seeds, data splits, and optimization stochasticity. Without variance information, the reader cannot assess whether reported improvements are robust or within noise. While single-run reporting is common in LTSF literature, it is still a limitation that weakens the strength of comparative claims.

### Minor

1. **LWL evidence for model-agnostic integrations is narrower than for the core model.** Figure 3(a) for PatchTST vs. PIH averages over all 7 datasets and all 4 prediction horizons. The model-agnostic experiments (Fig. 5) only show performance-vs-window curves for 3 datasets and a single prediction horizon (T=720), while the bar charts in Fig. 4 show only the best result per model across windows. The claim that the modules "enable models to overcome LWL" is thus more thoroughly validated for PatchTST than for the other architectures.

2. **Key hyperparameters not reported.** The paper defines patch length P, stride S, number of blocks K, and IB coefficient β but does not state their values, whether they are tuned, or whether they vary per dataset. Additionally, temperature τ for the Gumbel-sigmoid is not specified. This reduces reproducibility.

3. **Selective reporting of prediction horizons in model-agnostic experiments.** The integration into Transformer, Informer, and Autoformer (Sec. 4.2) only reports results for T=720. Results for T ∈ {96, 192, 336} are not shown, making it unclear whether the benefit holds across all forecast lengths.

### Trivial

1. **The naming "HMM" in the ablation (Mamba-handled hybrid variant) vs. "PatchTSM" in the computation comparison could be confusing.** The paper uses HMM to denote a variant where Mamba handles both long and short sequences, and PatchTSM for a separate pure-Mamba baseline. These are not clearly distinguished.

2. **Section 4.1 contains a dangling fragment "5." at the end of the first paragraph** (line 143: "significantly longer than in previous studies.5.") — likely a leftover reference marker from appendix stripping.

## Nice-to-Haves

- A sensitivity analysis of K (number of blocks) would be informative, as K directly controls the Transformer's effective sequence length and the trade-off between computation and sequence modeling capacity.
- The paper could clarify how the prior work on IB-based feature selection for sequences (e.g., Yu et al. 2021a/b) differs from the proposed time-series-patch application, beyond the domain difference.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Critical Issue #1 from Harsh Critic ("baseline comparison is systematically biased"):** The paper reruns baselines across 7 windows and selects the *best* result, which favors baselines (they pick their optimal setting), not the proposed method. For the main competitors (PatchTST, DLinear, NLinear), L=1024 is used for all, and the paper references Appendix A.3 showing PIH also outperforms at shorter windows (336, 512). The asymmetry, if any, favors baselines — this does not inflate the proposed method's apparent advantage.
- **Critical Issue #5 (partially) — "model-agnostic experiments do not report MSE-vs-window curves":** Factually incorrect. The paper explicitly states Fig. 5 shows "performance changes across the Traffic, Electricity, and ETTm1 datasets" with "triangular markers indicat[ing] the window limitations" — these are MSE-vs-window curves showing where the original models hit LWL and where the modified models push past it.
- **"HMM naming" as a major issue:** PatchTSM (pure-Mamba baseline) and HMM (ablation variant of HTM using Mamba for both branches) are different models in different experimental contexts. The naming is clear enough given context.
- **"Missing random split or no-split baseline for HTM" (Critical Issue #4):** The ablation already validates HTM's overall contribution (+HTM improves over PatchTST in Fig. 6). The specific comparison between interval vs. block split is a secondary design choice, and the paper openly acknowledges this as an open question.
- **"Missing related works" (TimesNet, DLinear variants, Bi-Mamba+):** Cannot be verified without external sources; the paper's SOTA claim is relative to its baseline set.
- **Pure formatting/style nitpicks** and **typos** that are parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The key insight — that LWL can be addressed through a combination of information bottleneck-based redundancy filtering and a hybrid Mamba-Transformer architecture with block splitting — is the paper's own contribution. The reviewers did not surface a novel observation about the work that the authors themselves did not articulate.

## Suggestions

1. **Add a causal validation of IBF:** Compare IBF-selected patches against (a) random selection of the same number of patches, (b) uniform downsampling, and (c) no selection (full set of patches), controlling for all other architectural components. This would isolate whether the IB-guided selection specifically drives the improvement.

2. **Report variance:** Provide standard deviations or confidence intervals over at least 3–5 runs with different random seeds for the main results.

3. **Report key hyperparameter values** (P, S, K, β, τ) in the main text or appendix, preferably per dataset.

4. **Extend model-agnostic curves** to more datasets and prediction horizons to match the evidentiary standard of Fig. 3(a), or explicitly acknowledge the narrower scope.

## Score and Decision

The paper tackles a well-motivated problem, proposes two principled and architecturally clean modules, and provides compelling evidence that its core model (PIH) overcomes the lookback window limitation and achieves strong results at L=1024. The computational benefits are substantial and well-documented. The main weaknesses — lack of causal validation for the IBF selection mechanism specifically, absence of variance estimates, and uneven evidentiary depth across the model-agnostic experiments — are real but non-fatal. The paper makes a genuine contribution to the LTSF literature and opens a promising direction toward exploring even longer windows.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Accept</decision>