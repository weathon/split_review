## Summary

This paper introduces HG-DCM, a framework that uses a CNN to predict compartmental model (DELPHI) parameters by leveraging historical data from multiple past pandemics (Ebola, SARS, Dengue, Influenza) to improve early-stage forecasting of a novel outbreak. The core idea — cross-disease temporal transfer, where the neural network learns universal epidemiological dynamics from historical pandemics and applies them to a new outbreak — is well-motivated and addresses a genuine problem in pandemic modeling. Experiments on early COVID-19 forecasting across 258 global locations show median MAE improvements over the standard DELPHI model (38.2% reduction at 2 weeks) and reduced overshooting behavior.

## Strengths

- **Novel cross-disease temporal transfer paradigm for cold-start forecasting.** The paper proposes a framework that systematically transfers knowledge from multiple historically distinct pandemics to a novel outbreak, a direction explicitly identified as not addressed by prior work. This is a genuine conceptual contribution — prior transfer learning in epidemiology focused on spatial transfer (location to location) or same-disease transfer, not cross-disease transfer across biologically distinct pathogens.

- **Construction and release of a multi-pandemic dataset.** The authors compiled a new dataset containing daily/weekly case data, epidemiological metadata, and country-level indicators for major outbreaks since 1990 (COVID-19, Ebola, SARS, Dengue, seasonal influenza). The paper notes that no public database existed for this purpose, making this a tangible resource that directly enables the proposed approach.

- **Empirical evidence of median MAE improvement and overshooting reduction.** The ablation study (Table 2, 258 locations) shows HG-DCM reduces median MAE by 38.2% over DELPHI with 2 weeks of training data. Figure 4 demonstrates substantially fewer overshooting events (predicted >5× true cumulative cases) across all training window lengths. These results directly support the claim that historical guidance stabilizes predictions when current data is sparse.

- **Principled architectural modifications for cross-pandemic generalization.** The paper identifies that Batch Normalization layers cause instability due to differing batch statistics across historically distinct pandemics and removes them (Section 2.1). This is a targeted design choice supported by a clear rationale. The data augmentation strategies (window-shift for historical data, block-masking for current pandemic data) are thoughtful and tailored to the problem structure.

- **Interpretable parameter inference with statistical validation.** The paper extracts DELPHI parameters from HG-DCM and compares them to standard DELPHI fits (Section 3.2.3, Figure 5). Wilcoxon signed-rank tests confirm significant differences (p<0.05) in key parameters, with HG-DCM producing more conservative estimates that are less prone to overfitting initial noise. This provides evidence that the model's improvements are grounded in more stable epidemiological parameter estimation.

## Weaknesses

### Fatal
None.

### Major

1. **Limited SOTA comparison with mixed results.** The benchmarking against GradABM and EiNNs (Table 1) is conducted on only two geographic units (United States and Massachusetts), selected "because these locations were the only locations in which there was available data and code for the comparison methods." The results are mixed: EiNNs beats HG-DCM on 4-week US MAE (729 k vs. 2,548 k) and 6-week Massachusetts MAE (25 k vs. 39 k). The paper's claim that HG-DCM "consistently achieves lower MAE in most tasks" is technically true but the mixed results on just 2 locations provide a weak foundation for the strong comparative claims in the abstract ("significantly outperforms state-of-the-art methods").

2. **Unaddressed catastrophic failure mode in mean MAE at 4 weeks.** In Table 2, HG-DCM's **mean** MAE at the 4-week training window is 110,452, while the CNN baseline achieves 11,238 and T-DCM achieves 17,691. This means HG-DCM produces some predictions with errors roughly **10× worse** than a simple CNN, severely inflating the mean above the median. The paper discusses only median improvements and overshoot reduction, completely ignoring this degradation. For a method whose core claim is improving *stability* and *reliability* of early-stage forecasts, a failure mode where predictions can be an order of magnitude worse than a simple baseline in a non-trivial fraction of locations is a critical omission. The paper should characterize which locations produce these failures and whether they are predictable.

3. **Evaluation on a single target pandemic limits the generality claims.** The paper is titled and framed around a "new paradigm" for general pandemic forecasting, yet only COVID-19 is used as the target. A proper test of cross-disease transfer would hold out one historical pandemic (e.g., SARS or Ebola), train on all others including COVID-19, and forecast the held-out pandemic in its early stage. Without this, it is unclear whether HG-DCM would generalize to a truly novel pathogen with different dynamics, or whether its success on COVID-19 benefits from similarity to seasonal influenza (which dominates the historical data). The "new paradigm" language in the abstract and introduction is not supported by a single case study.

### Minor

4. **CNN baseline training setup is ambiguous.** The paper does not specify whether the CNN baseline is trained on historical pandemics + current data, or only on current data. The main text calls it a "purely end-to-end CNN model" that "bypasses mechanistic structure" but never clarifies its training data. Since T-DCM (which excludes historical data) is a separate ablation, this suggests CNN may use historical data, but the paper should state this explicitly. The interpretation of the CNN comparison (whether the gap is due to "epidemiological inductive bias" or simply access to historical data) depends on this detail.

5. **No statistical significance reported for main forecasting results.** The Wilcoxon signed-rank test is used only for parameter inference (Section 3.2.3). The headline forecasting comparisons (Table 1, Table 2) are reported without any significance testing across the 258 locations. A paired test on MAE differences would directly strengthen the evidence that improvements are systematic rather than driven by a subset of locations.

6. **Missing simple baselines.** The paper does not include basic forecasting baselines (e.g., flat extrapolation, exponential growth fit, ARIMA). Without these, the reader has no sense of absolute performance — whether MAEs in the thousands are good or bad relative to trivial alternatives. This is important for calibrating the difficulty of the early-stage forecasting task.

7. **Hyperparameter β (history weight) receives no sensitivity analysis.** The paper introduces β as the weight balancing past and current pandemic loss (Eqn. 5) and notes it "determines the amount of information inherited from past pandemics," but never discusses how it was chosen, whether it was tuned on a validation set, or how sensitive results are to its value. A sensitivity analysis would increase trust in the method's robustness.

### Trivial

None.

## Nice-to-Haves

- The MAPE term in the loss function (Eqns. 3–4) involves division by \(C_{ij}\). When \(C_{ij}=0\) (possible early in a pandemic), this is undefined. A small clarification on handling (e.g., a smoothing constant or masking) would be helpful.
- The LDoA detection threshold (25% of global maximum) is acknowledged but its sensitivity is not discussed. A brief comment on robustness to this choice would strengthen the augmentation description.
- The paper could quantify the fraction of locations where HG-DCM *worsens* predictions relative to DELPHI, providing a more complete picture of the trade-off.

## Removed Points

- **"The sigmoid ranging function description is vague."** — The paper states the purpose (enforcing physical bounds) and the technique (sigmoid normalization). This is sufficient at the level of detail typical in method descriptions; the specific ranges are defined by the DELPHI parameter semantics. Removed as a minor presentation nitpick that does not affect the paper's substance.
- **"No ablation showing that removing BatchNorm helps."** — While a cleaner experiment would confirm the choice, the paper provides a clear rationale (differing batch statistics across pandemics). This is a reasonable design decision rooted in a specific identified problem; requesting an ablation is a nice-to-have, not a weakness.
- **"The paper never directly validates the assumption that human behavioral responses create universal dynamics."** — This is stated as a motivating hypothesis (Section 1), not as an empirical claim that the paper must prove. The paper's contribution is to demonstrate empirically that cross-disease transfer works; the behavioral universality is the plausible justification, not the claim being tested.
- **Claims about missing code/data release as "reproducibility" weaknesses.** — The paper is under double-blind review and does not include a code/data availability statement, which is standard for the submission format. This is not a weakness of the scientific content.
- **"Training hyperparameters not given in the main text"** — A systems/empirical paper at ICLR commonly defers training details to the appendix (which was stripped by the parser). This is not a valid weakness given the known parsing issue.
- **"Statistical significance is reported only for parameter inference"** — Actually kept as a Minor weakness above (point 5), since it directly supports the main forecasting claims.

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments surface the gap between the paper's ambitious framing ("new paradigm") and its narrow empirical support (single target, limited SOTA comparison, unexplained mean MAE failures), but this tension is already implicit in the paper's structure.

## Suggestions

1. **Add a held-out pandemic evaluation.** Train on all pandemics except one (e.g., exclude SARS or Ebola, train on COVID-19 + remaining historical data) and forecast the held-out pandemic. This directly validates the cross-disease transfer claim.
2. **Characterize and explain the high-error locations at 4 weeks.** Report the fraction of locations where HG-DCM is worse than DELPHI or CNN, and analyze what features (case count magnitude, demographic profiles) predict failure. This is necessary for any practical deployment claim.
3. **Report statistical significance for main forecasting results.** A paired Wilcoxon test across 258 locations comparing HG-DCM vs. each baseline's MAE would directly strengthen the evidence.
4. **Add simple baselines** (exponential growth model, ARIMA) to Table 2 to calibrate the absolute difficulty of the early-stage forecasting task.
5. **Add a sensitivity analysis for β** (history weight) over a range of values (e.g., 0.1, 0.5, 1.0, 2.0) to demonstrate robustness.
6. **Tone down the "new paradigm" language** in the abstract and conclusion unless a held-out pandemic evaluation is added.

## Score and Decision

**Calibration Anchors:**

| Anchor Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/qckiBWmodZ.md` | 3.00 | R1 | Weak. Pandemic intervention policy paper with narrower scope and weaker evaluation. Current paper is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/hgj1LQmD09.md` | 2.00 | R1 | Weak. Avian influenza forecasting with GNNs; significantly less mature. |
| `/home/wg25r/review_agent/human_reviews_2026/oPDPnzNHQC.md` | 3.00 | R1 | Weak. Flood forecasting benchmark; different domain, comparable thoroughness. |
| `/home/wg25r/review_agent/human_reviews_2026/ECc2td0LCZ.md` | 3.00 | R1 | Weak. ODE learning from single trajectory; different domain. |
| `/home/wg25r/review_agent/human_reviews_2026/5veGth37O2.md` | 4.00 | R1/R2 | **Key anchor.** CAPE: cross-disease pre-trained epidemic forecaster, tested on 17 diseases across 50+ regions. Broader evaluation than HG-DCM but similar novelty level. CAPE was rejected (avg 4.0) with concerns about missing baselines and limited novelty. HG-DCM has a cleaner, more explicit mechanism (CNN → DELPHI params) but significantly narrower evaluation (1 target disease, 2 SOTA comparison locations). **Comparable or slightly weaker.** |
| `/home/wg25r/review_agent/human_reviews_2026/JZp0GcNjH8.md` | 4.40 | R1/R2 | EpiDiff: hybrid diffusion + mechanistic model for epidemic forecasting. Tests on multiple datasets (COVID-19, influenza). HG-DCM is similar in quality but with narrower evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/DgnsohAUMn.md` | 6.50 | R1 | Panda: pretrained model for chaotic dynamics. Much more comprehensive evaluation (zero-shot, scaling laws, emergent PDE forecasting). Clearly stronger than HG-DCM. |
| `/home/wg25r/review_agent/human_reviews_2026/okus8iObwH.md` | 4.50 | R1 | Cross-city traffic flow transfer learning. Different domain but similar methodology. |
| `/home/wg25r/review_agent/human_reviews_2026/KiOqKKXomL.md` | 4.50 | R2 | Intervention dynamics; different domain. |
| `/home/wg25r/review_agent/human_reviews_2026/gbQ3VykJbJ.md` | 5.50 | R2 | Transfer learning in Cox survival models. Stronger theoretical grounding but different domain. |
| `/home/wg25r/review_agent/human_reviews_2026/QBzFrjEF59.md` | 5.50 | R2 | Hybrid neural ODE sparsification. More thorough evaluation (synthetic + real, multiple baselines). |
| `/home/wg25r/review_agent/human_reviews_2026/Y0zPlHDO5p.md` | 4.50 | R2 | AntigenLM: DNA language model for influenza. Different domain. |
| `/home/wg25r/review_agent/human_reviews_2026/oy4fc9h9oT.md` | 4.00 | R2 | DORIC: universal time-series forecasting. Different domain. |

**Round 1 Bracket:** Between 3.5 and 6.0. The paper is clearly stronger than the 2–3 range pandemic papers but has significant gaps compared to the 5.5–6.5 range papers which have more thorough evaluations.

**Round 2 Narrowing:** The closest topical anchor is CAPE (4.00), which has a similar cross-disease transfer goal but a substantially broader evaluation (17 diseases vs. 1). HG-DCM has a cleaner mechanism but narrower evaluation. The unaddressed mean MAE failure at 4 weeks is a significant concern that CAPE did not have in its evaluation. The mixed results on the limited (2-location) SOTA comparison further weaken the evidence. **I place HG-DCM slightly below CAPE**, near 4.0.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>