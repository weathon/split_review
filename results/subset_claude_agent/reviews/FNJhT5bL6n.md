Let me read more to understand the conclusion more clearly.Now I have enough information to write a thorough draft review. Let me draft it before calibration.Round 1 bracket: The paper sits between **3 and 5** based on the anchors. The idea is interesting but the evaluation has fundamental issues. Let me narrow down.Based on my reading of the paper and comparison with calibration anchors:

- **PTN (5.25)** - A data-centric plugin for TSF with proper baselines, SOTA results across 7 datasets. The paper under review is clearly weaker: no raw-exogenous baseline, admitted median effect ≈ 0%.
- **PErM (4.33)** - A frequency-domain preprocessing plugin with theoretical analysis and proper comparisons, but flawed presentation. The paper under review has a comparable idea but worse evaluation.
- **TSAA (4.50)** - Data augmentation for TSF with a real comparison framework.

The paper under review is worse than all round-2 anchors in evaluation quality: it lacks the central comparison (morphed vs. raw exogenous), uses post-hoc selection from 25 configurations, and the authors themselves admit median effect ≈ 0%. I place it below PErM (4.33) → **score: 3.0**.

---

## Summary
The paper proposes "shape morphing," a preprocessing framework for exogenous variables in transformer-based time series forecasting. For each exogenous channel, a sliding-window statistical function (rolling correlation, covariance, mutual information, FARM, or entropy) computes a morph ratio that scales exogenous amplitudes based on local similarity to the target series. The framework is evaluated across 7 datasets, 5 transformer architectures, 5 saliency methods, and 5 window sizes. The central premise — that statistical preprocessing can decouple saliency detection from transformer learning — is motivated by an observed alignment between TFT attention weights and FARM saliency scores.

---

## Strengths

- **Concrete motivating evidence (Figure 1)**: A direct empirical comparison of TFT attention weights and FARM saliency weights on a pedestrian-count dataset shows remarkably similar temporal patterns, providing tangible support for the hypothesis that statistical proxies can substitute for learned attention in saliency detection.

- **Controlled synthetic validation (Figure 2)**: A toy example with known relevance regimes cleanly demonstrates the morphing mechanism — the morph ratio rises during predictive intervals and falls during irrelevant ones, producing a 6% MSE reduction over a Ridge forecaster. This is a focused, interpretable illustration of the mechanism independent of model-specific effects.

- **Broad design space coverage**: The ablation spans 7 diverse datasets, 5 transformer architectures, 5 saliency functions, and 5 window sizes. The scale of experimentation is a genuine asset regardless of the evaluation protocol issues.

---

## Weaknesses

### Fatal
None verifiable from the paper as written.

### Major

- **No raw-exogenous baseline — the central claim is untestable as evaluated.** Table 1 compares morphed exogenous against *no exogenous data*, not against *raw (unmorphed) exogenous data*. Section 4.1 explicitly states: "the relative number indicating the gain compared to a forecast without exogenous information." This collapses the distinction between (a) the value of including any exogenous data and (b) the value of morphing specifically. The paper's thesis is that morphing improves how transformers utilize exogenous data, but this is never directly tested. Every reported improvement could be entirely attributable to simply adding exogenous channels at all, which is a well-known result requiring no method contribution.

- **Post-hoc hyperparameter selection inflates all reported results, and the authors admit it.** The 73% improvement rate is derived from "the best result of the performed ablation test obtained with the optimal configuration" (Section 4.1) — the optimum over 5 saliency × 5 window = 25 configurations per dataset-model-horizon cell, with no validation-set selection protocol. Most critically, Section 5 directly states: *"Morphing is not universally better when used blindly (typical median effect ≈ 0%)."* This self-contradiction between the abstract's headline and the conclusion's admission is severe: the untuned median effect is the realistic picture of what a practitioner would observe, and it equals zero.

- **The headline +31.9% improvement reflects correcting a near-degenerate Crossformer baseline, not a general result.** From Table 1, even after morphing, Crossformer's MSEs remain 3–10× higher than other models on the same tasks: ETTh2/336=0.710 (vs. PatchTST 0.228), ETTm2/192=0.133 (vs. PatchTST 0.101), ETTm1/720=0.831 (vs. iTransformer 0.080). These figures indicate the Crossformer baseline was severely misconfigured or non-functional on these benchmarks. Averaging its large recovery gains with well-behaved models to produce the headline figure misrepresents morphing's general utility. For the non-pathological models (PatchTST, iTransformer, TimeXer), most individual improvements in Table 1 fall in the 0–5% range — consistent with the admitted median ≈ 0%.

### Minor

- **Inference-time morphing for the forecast horizon is ambiguous.** The morph ratio requires both $x_t$ and $y_t$ in the same sliding window (Eq. 1). During iterative forecasting, $y_t$ is unknown for steps within the forecast horizon. Section 4 states "the point of interest is set on the last data point of the sliding window" and "exogenous data always comprise the original information," but does not specify how morph ratios are handled for the exogenous data beyond the lookback window. Whether the final ratio is held constant, extrapolated, or computed from forecasted $y$ values is unstated, which is material for horizons of 336–720 steps.

- **Iterative single-step forecasting diverges from the direct multi-step protocol used by all five reference models**, introducing a systematic confound between morphing effects and forecasting-protocol effects. The cited comparison (Wang et al. 2024b) is not independently verifiable, and most LTSF benchmarks including the hyperparameter sources use direct multi-step forecasting.

- **Table 2 presents a circular conclusion.** Section 4.2 states "no modelling approach without morphed input data was able to compete among the top five models." But Table 2 only reports morphed configurations by construction — non-morphed baselines are never included in this ranking. The conclusion is guaranteed to hold regardless of morphing's actual utility.

### Trivial
None.

---

## Nice-to-Haves
- A paired morphed vs. raw-exogenous comparison on each dataset, with configuration selected on a held-out validation split, would be the single most valuable addition and would either confirm or decisively challenge the central claim.
- Reporting the untuned median improvement prominently (alongside the best-case figures) would more honestly characterize the method's practical utility.
- Sensitivity analysis of morphing range and smoothing choices (mentioned in the toy example but absent from real-dataset descriptions) would clarify how sensitive the results are to these implicit design parameters.
- Investigating whether Crossformer instability is a configuration artifact; reporting it separately from well-calibrated models would clarify the headline figure.

---

## Removed Points
*These points were flagged for removal — treat with caution:*

- **FARM self-citation / conflict-of-interest concern**: "Auth1 et al. (2023)" is a blinded double-blind citation. This is standard review procedure, not an author error.
- **Method specification deferred to Appendix D**: Parser strips appendix sections; the specification exists in the original submission.
- **Strength "73% of experiments improved is strong evidence"**: This is not a genuine strength. The 73% is from post-hoc best-case selection; the authors admit untuned median ≈ 0%.
- **Strength "Table 2 all top-5 are morphed"**: Circular construction — Table 2 only includes morphed entries by design.

---

## Novel Insights
The paper's most informative admission appears in Section 5: "typical median effect ≈ 0%." This is actually a useful finding for the community — simple amplitude scaling of exogenous variables does not systematically help transformer forecasters when applied without tuning, but can benefit specific model-dataset pairs under optimal configuration. Separately, the alignment between TFT attention weights and FARM rolling correlations (Figure 1), though anecdotal, suggests that low-complexity statistical proxies could replace learned attention for saliency detection in certain settings, which is a hypothesis worth rigorously testing in future work.

---

## Suggestions
1. Add a raw-exogenous condition to Table 1 (same models, same data, unmodified exogenous channels) — this is the missing baseline that would actually test the paper's claim.
2. Establish a validation-split protocol for selecting morphing hyperparameters before reporting test-set performance.
3. Report Crossformer results separately with a note on its baseline instability; exclude it from aggregate improvement statistics until the instability is understood.
4. State explicitly in the main text how morph ratios are assigned to the exogenous data points in the forecast horizon during inference.
5. Move the "typical median effect ≈ 0%" finding to the abstract and main results, not just the conclusion — it is the most honest characterization of the method's reliability.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| qU1GtrDDst.md (financial TS repr.) | 1.80 | R1 weak | Much weaker — incomplete, poorly grounded; paper under review is better |
| 0Q1mBvUgmt.md (VIPER) | 3.00 | R1 weak | Roughly comparable — both have methodological issues, VIPER is rejected; paper under review is similar tier |
| xJ5CF1aOOX.md (self-supervised TS) | 2.50 | R1 weak | Slightly weaker overall |
| WFlLqUmb9v.md (FIA-Net hyper-complex) | 2.50 | R1 weak | Weaker |
| xW4J2QlqRx.md (ContextFormer) | 5.00 | R1 mid | Clearly stronger — proper comparisons, multimodal exogenous, valid evaluation |
| 6hJ3khuJY4.md (PTN) | 5.25 | R1 mid / R2 | Stronger — proper learned transformation with valid baseline comparisons, actual SOTA claims. Paper under review lacks the central comparison. |
| SwIkknEqmt.md (PErM) | 4.33 | R1 mid / R2 | Comparable or slightly better — PErM has proper comparisons but weaker theoretical grounding. Paper under review has worse evaluation design. |
| TYXtXLYHpR.md (Transparent TSF) | 5.75 | R1 mid | Stronger |
| KXOB15k1br.md (TSAA) | 4.50 | R2 | Comparable — also a preprocessing/augmentation plugin for TSF, similar scope and reject decision |
| DNjHslZrqu.md (Tabular transformer) | 3.67 | R2 | Paper under review is slightly below this, given the evaluation design is more fundamentally flawed |
| ZkEsEFFUyo.md (CloudOps pre-training) | 4.33 | R2 | Paper under review is below this — CloudOps has proper evaluations |
| X8aFMdXk3N.md (TSF benchmark) | 4.25 | R2 | Paper under review is below this |

**Round 1 bracket**: 3.0–4.5

**Round 2 narrowing**: The paper under review compares unfavorably to all round-2 anchors (PErM 4.33, TSAA 4.50, PTN 5.25, CloudOps 4.33, Benchmark 4.25). Its central experimental flaw (missing the fundamental raw-exogenous baseline), combined with the admitted median-effect-zero finding, places it below PErM (4.33). It sits closer to VIPER (3.00) and the tabular baseline paper (3.67) than to PErM, though its idea has more specificity than VIPER. Final calibrated score: **3.0**.

**Evaluation on axes:**
- *Originality*: Moderate — the morphing concept is novel for exogenous preprocessing, but the idea is a natural extension of existing statistical preprocessing.
- *Importance of research question*: Good — exogenous variable utilization in transformers is a genuine and underexplored problem.
- *Claims well-supported*: Weak — the central claim (morphing improves exogenous utilization) is not empirically testable with the current evaluation.
- *Soundness of experiments*: Poor — no raw-exogenous baseline, post-hoc hyperparameter selection, degenerate Crossformer driving headline, and iterative vs. direct forecasting divergence.
- *Clarity of writing*: Acceptable — the motivation and method are presented coherently, though formal definitions are deferred to the appendix.
- *Value to the research community*: Limited in current form — the key admission (median effect ≈ 0%) and missing baseline mean the paper cannot support actionable conclusions.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>