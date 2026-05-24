Now let me write the consolidated review.

## Summary

This paper argues that time series forecasting's performance plateau stems from the "self-stimulation" assumption (using only historical data, ignoring external influences). It formalizes this through a control-theoretic analysis proving an irreducible error bound when influences are unobserved (Proposition 2.1), and shows that incorporating influence information reduces this bound (Proposition 3.1). To operationalize the proposed Influence-Aware Time Series Forecasting (IATSF) paradigm, the paper introduces a leak-free multi-domain benchmark with temporally-synced textual influences, and FIATS, a lightweight LLM-free model whose Channel-Aware Adaptive Sensitivity Modeling (CASM) and Channel-Aware Parameter Sharing (CAPS) mechanisms explicitly model how each channel responds to textual influence signals. Experiments on synthetic, physics-based, and human-driven systems show FIATS consistently outperforms strong self-stimulated baselines (including billion-parameter foundation models), with ablations confirming the gains come from influence modeling rather than model capacity.

## Strengths

1. **Rigorous theoretical framing of an underappreciated limitation.** Proposition 2.1 formally proves that models restricted to historical data converge to the conditional expectation over influences, producing an irreducible error covariance bounded by the influence sensitivity and variance. Proposition 3.1 then shows that any measurable influence information (including textual) reduces this bound. While the core mathematics is elementary (law of total variance), applying it to diagnose the self-stimulation bottleneck in forecasting practice is a genuinely useful conceptual contribution that the paper then tests empirically.

2. **Leak-free benchmark design that addresses a real confound in prior multimodal datasets.** Section 4.1 explicitly enforces that only *independently evolving* influences are included and that future system states are never encoded into the influence text. This is a principled response to information-leakage problems that have plagued earlier multimodal time-series datasets (e.g., Time-MMND, GPT4MTS), where influence descriptions could inadvertently summarize the future trajectory. The benchmark covers three distinct categories (toy, complex real-world, human-driven) with extended horizons.

3. **Ablation studies that causally attribute gains to influence modeling, not capacity.** Table 3 shows that (i) removing all influence inputs ("Zero News") drops FIATS's performance to the level of self-stimulated baselines and (ii) removing channel descriptions ("Zero Desc.") degrades performance significantly, confirming that the CASM mechanism for channel-specific sensitivity is responsible for the gains. Robustness across three different text embedding backends (OpenAI, MiniLLM, mpnet) rules out dependence on a specific encoder.

4. **Consistent and large improvements across diverse systems.** Table 1 shows FIATS achieves average MSE reductions of 36.0% on Atmospheric Physics and 44.3% on NYC Traffic Speed over the strongest self-stimulated baseline (PatchTST), with gains holding across all prediction horizons. On GAUD (Figure 4), FIATS outperforms PatchTST by 12.6% on average and ranks first on 59.6% of games, including cold-start scenarios. These results are numerically impressive.

5. **Interpretable architectural design with clear visualization.** The CASM attention maps (Figure 5) reveal which textual sentences influence which channels, and the CAPS decoder attention patterns (Figure 3) show distinct behaviors for periodic vs. event-driven channels. The controllability demonstration (orange line in Figure 3, with swapped influences) provides a concrete sanity check that the model actually conditions its predictions on the influence text.

## Weaknesses

### Major

- **Missing critical baseline: same external information in numerical form.** The paper's headline experiments compare FIATS (which receives external textual influence) against self-stimulated baselines (which receive zero external information). This design cannot distinguish between "influence-aware modeling is the right paradigm" (the paper's central claim) and "having additional predictive features helps" (a trivial statement). On the Atmospheric Physics dataset, the influences are weather forecasts — naturally numerical quantities (temperature, wind speed, humidity, pressure). A standard time series model (e.g., DLinear, PatchTST, or a simple ARIMAX) that concatenates these weather variables as numerical exogenous features is the obvious control experiment. Without it, the reader cannot tell whether the gains come from the textual modality, the CASM/CAPS architecture, or simply from having access to weather variables that baselines lack. This gap is consequential because the paper also claims textual modality is *necessary* to capture "non-quantifiable" influences — but every dataset in the benchmark uses influences that could be expressed numerically (weather forecasts, holidays, developer logs). The paper does not provide a single example where textual information is genuinely uniquely valuable (e.g., a "port strike" event that has no numerical expression).

- **FIITS is undefined.** The baseline "FIITS" appears in Table 1 with results across all datasets but is never defined in Section 6's baseline list or anywhere else in the paper. The reader cannot determine whether FIITS is a variant of FIATS (e.g., without CASM, without CAPS, or with a different decoder), a different model, or a typo. This is a basic reproducibility concern.

- **The core theoretical results, while correctly stated, are elementary and their framing is overstated.** Proposition 2.1 is essentially the law of total variance applied to a linear dynamical system. The "hard mathematical barrier" language implies a deeper result than what is on the page. The nonlinear case is stated but not developed (the bound involves the Jacobian ∇_U F, which has no closed form for arbitrary nonlinear systems). Proposition 3.1 follows directly from Proposition 2.1 by partitioning the influence set. The paper would benefit from a more precise statement of what new theoretical insight is being claimed beyond applying well-known statistical identities to the forecasting setting.

### Minor

- **The claim that self-stimulated models "fail spectacularly" on the FM Toy is exaggerated for shorter horizons.** Table 1 shows PatchTST achieves MSE 0.006 at horizon 14 (vs. FIATS's 0.003) — this is near-perfect performance by any reasonable standard, not a failure. The statement becomes more justified at longer horizons (e.g., horizon 120: 0.168 for PatchTST vs. 0.027 for FIATS), but the blanket characterization in the text is imprecise.

- **No statistical significance or variability reporting.** All results in Table 1 are reported as single MSE values with no standard deviations, confidence intervals, or multi-seed runs. While this is common practice in large-scale forecasting benchmarks, the paper's claims of "consistent" and "significant" improvements would be stronger with error bars — especially for cases where the margins between FIATS and the second-best are narrower (e.g., Electricity Utility at pred. len. 96: 0.124 vs. 0.130).

- **The evaluation assumes perfect future influence information.** The benchmark provides ground-truth future influences at test time, but in deployment these must be predicted (e.g., weather forecasts have errors). Figure 6 tests noise added to embeddings, which is a partial proxy but not the same as using real forecast data from archives. The paper acknowledges this in Appendix B.3 but does not provide any results under realistic imperfect-influence conditions.

- **No ablation isolating CASM from CAPS.** Table 3 shows that removing channel descriptions ("Zero Desc.") degrades performance, which the paper attributes to CASM. But this ablation removes the channel description input, not the CASM mechanism itself. An ablation that keeps influence text and channel descriptions but replaces CASM with a simpler fusion (e.g., concatenation) would more cleanly isolate the contribution of the CASM design.

### Trivial

- Line 148 contains garbled notation: `Argmax_i(kW_K)_i` and an undefined `b_{ij}` in the CASM equation description. This is likely a formatting artifact.
- The abbreviation "IATSF" is used throughout but never spelled out on first use — it appears first in the abstract.
- Table 1 shows "Pred. Len." as column header but there are no units or explanation of the prediction lengths in the table caption.

## Nice-to-Haves

- A real-world case study where a non-numerical influence (e.g., a policy announcement described only in text) demonstrably improves forecasts over the best numerical-exogenous model.
- Evaluation on the ETT dataset with corresponding external influences would connect this work to one of the most widely-used benchmarks in the field and demonstrate the paradigm's generality.
- Multi-seed results with standard deviations for the main table.

## Removed Points

These points were flagged but are removed from the main review with brief justification:

- **Harsh Critic: "The paper's own Table 1 shows PatchTST outperforming DLinear on some datasets" as a critique of the claim about foundation models vs. linear baselines.** The paper's claim is about the general phenomenon of performance plateaus, which is a recognized observation in the field. Pointing out that PatchTST outperforms DLinear on some datasets does not undermine the broader claim, which is about marginal gains from increasingly complex architectures relative to simpler approaches. Furthermore, this claim is contextual (motivating the work), not a core experimental finding. REMOVED (strawman: the paper's motivation claim is nuanced and the counterexample is not dispositive).

- **Harsh Critic: "Proposition 2.1 is essentially the law of total variance" presented as a weakness.** The paper acknowledges the linear case explicitly and the bound for the nonlinear case is a correct application of the law of total variance to this setting. Framing a known statistical result in a new application context is a legitimate theoretical contribution, even if the underlying math is elementary. The reviewer's factually correct observation is more of a characterization than a weakness. DEMOTED to the framing observation already included in weakness 3 above (Major) — it's about overstatement, not invalidity.

- **Harsh Critic: "The exposition relies on a linear system for the closed-form bound. The nonlinear case is stated but not developed."** This is acknowledged as a limitation by the paper's own assumption of "analytical clarity" (line 47: "For analytical clarity, we assume full observability, i.e. X = Z. We also discuss a simple linear system case"). The paper states the nonlinear bound in Proposition 2.1 using the Jacobian. This is standard practice. Already captured under the minor point about overstatement of theoretical depth.

- **Harsh Critic: "The GAUD dataset uses developer logs as influences. Are these logs truly independent of the system's past states?"** This is a speculative concern. The paper explicitly defines the leak-free principle in Section 4.1 as requiring independently evolving influences. Without evidence that the logs actually violate this, the criticism is unfounded. REMOVED (speculative).

- **Harsh Critic: "Code link is provided, but the paper should be self-contained enough for a reader to understand the design."** The paper provides a thorough architectural description in Section 5 with all three inputs (time series, news embeddings, channel descriptions), the CASM block design with query/key/value mappings, and the CAPS decoder. The claim that the architecture description is "incomplete" is unsupported given what is presented. The garbled equation is acknowledged as a trivial artifact below.

- **Harsh Critic: "The benchmark provides future influences at test time. The paper acknowledges this requires prediction of influences in deployment (Appendix B.3), but no results are shown with imperfect influence predictions."** This is a valid point but partially addressed by Figure 6 (noise added to embeddings), and the paper explicitly acknowledges this as a limitation in its conclusion section. I've included a toned-down version as a Minor weakness above.

- **Several formatting/style nitpicks** about the paper's presentation are removed per the hard rules about parser artifacts.

- **Strength Finder strengths about the problem being "important" or the benchmark being "useful"** — generic strengths removed. Kept only those grounded in specific evidence.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that the authors themselves do not already articulate.

## Suggestions

1. **Add the critical control experiment:** Feed the same external information (weather forecasts, holiday flags, developer logs) as numerical exogenous features into DLinear, PatchTST, or ARIMAX. If FIATS still wins, the case for textual influence modeling is strong. If the numerical baseline matches FIATS, the contribution reduces to "adding features helps," and the paper should reframe accordingly and emphasize cases where textual information provides unique value.

2. **Define FIITS clearly** — either rename it to something informative (e.g., "FIATS-Ablation" or "FIATS-noCASM") or remove it from the table if it is not a meaningful baseline.

3. **Tone down the rhetorical claims** about "spectacular failure" of self-stimulated models (Table 1 shows PatchTST is competitive at short horizons) and "hard mathematical barrier" (the theory is well-understood conditional expectation / law of total variance). The paper's empirical contributions are strong enough to stand on their own without embellishment.

4. **Report standard deviations** across multiple seeds for the main results, even if only for a subset of datasets, to establish statistical significance.

5. **Provide at least one experimental result** using real (imperfect) influence predictions (e.g., archived weather forecasts) rather than synthetic noise, to demonstrate practical viability under realistic deployment conditions.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Human Score | Comparison to Paper Under Review |
|--------|--------|-----------------------------------|
| Beyond Trend and Periodicity: Guide TSF with Textual Cues (mfc6FKgtQA.md) | 5.00 | Very similar paper (text-guided TSF, benchmarks, cross-attention). IATSF has stronger theoretical framing and ablation design but shares the same critical gap (no numerical-exogenous control). IATSF is slightly stronger overall. |
| Dual-Forecaster: Multimodal Time Series (QE1ClsZjOQ.md) | 4.50 | Similar multimodal TSF paper. IATSF has deeper theory, better leakage control, and more thorough ablations. Clearly stronger. |
| Time-MoE: Billion-Scale Time Series Foundation Models (e1wDDFmlVu.md) | 7.33 | Large-scale foundation model with MoE. Different contribution type; stronger experimental scale and rigor. IATSF has a different, more conceptual contribution (diagnosing the self-stimulation problem) but with weaker empirical validation against obvious baselines. |
| LST-Bench (2wwPG1wpsu.md) | 2.50 | Simple benchmark paper with low novelty. IATSF is substantially stronger in every dimension. |
| Forecasting Needles in a Time Series Haystack (PTjKXwrVCT.md) | 3.75 | Benchmark-centric paper with some novelty in spike modeling. IATSF has a broader contribution (paradigm + theory + model + benchmark) and is clearly stronger. |
| Context Matters: Leveraging Contextual Features (xW4J2QlqRx.md) | 5.00 | Similar idea (using external context for TSF). Comparable quality. |

The paper has real contributions: a well-motivated critique of the self-stimulation paradigm, a leak-free benchmark, a principled lightweight model with interpretable attention mechanisms, and strong numerical results. However, a critical experimental gap (no baseline using the same external information in numerical form) prevents the paper from fully supporting its strongest claims. This is the same weakness that brought down closely related papers in this area (e.g., the TGForecaster paper scored 5.00 and was rejected). The paper is clearly stronger than low-scoring anchors (2.50–3.75) but has a gap that places it below high-scoring ones (7.33). Relative to the medium-scoring anchors (4.50–5.75), it is competitive but not clearly above, due to the missing control experiment.

MY FINAL SCORE: 5.0

MY FINAL DECISION: Reject