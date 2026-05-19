## Summary
This paper proposes xLSTM-Mixer, a recurrent architecture for multivariate long-term time series forecasting that combines a channel-independent linear forecast (NLinear) with sLSTM blocks and multi-view reconciliation. The model processes variates as sequential tokens through sLSTM stacks, enabling cross-variate interaction via the recurrent hidden state rather than quadratic-complexity self-attention. Additional components include learned initial embedding tokens (soft prompts), weight-shared up-projection, and a multi-view mechanism that reconciles forward and reversed latent representations.

**Strengths**: Competitive empirical results across 8 benchmarks (best or second-best average MAE on 7/8 datasets); well-designed ablation study covering 12 configurations; favorable scaling with lookback length; Shapley-based attribution analysis provides interpretability insight.

**Key weaknesses**: Overclaimed contributions (redundant SOTA claims, 'superior' and 'extraordinary' language); main text contradicts Appendix A.5 regarding variate ordering sensitivity; ablation reporting is selective; missing statistical significance discussion; formula-level implementation ambiguity.

**Novelty verdict**: Deferred — external literature verification unavailable in this run. The core architectural novelty lies in combining sLSTM recurrence over variates with linear time mixing and multi-view reconciliation. The degree of overlap with concurrent xLSTM-based time series work (xLSTMTime, Kong et al. 2024) and mixer-based methods (TSMixer, TimeMixer) requires manual literature comparison.

## Strengths
1. **Competitive empirical results**: xLSTM-Mixer achieves best or second-best average MAE on 7 out of 8 long-term forecasting benchmarks. The performance is particularly strong on Weather (MSE 0.219, MAE 0.250), ETTm1 (MSE 0.339, MAE 0.366), and Electricity (MSE 0.153, MAE 0.245). This demonstrates that well-designed recurrent architectures remain highly competitive for multivariate forecasting.

2. **Thorough ablation study**: Table 3 covers 12 architectural variants, systematically testing the contribution of time mixing (NLinear/DLinear), sLSTM type, recurrence order (variates/time/none), initial embedding tokens, and multi-view mixing. The ablation confirms that sLSTM blocks are the primary accuracy driver, with additive gains from the other components.

3. **Favorable computational scaling**: Figure 7 and the associated analysis show that xLSTM-Mixer's memory and time requirements scale sub-linearly with lookback length T (doubling from ~0.01s to ~0.02s as T goes from 96 to 1024, with memory remaining at ~1,000 MB). This contrasts favorably with Transformer-based models whose attention cost grows with sequence length.

4. **Interpretability analysis**: The Shapley-based feature attribution (Figure 5) provides useful insight into cross-variate dependency learning, showing that the variate-marching design creates a structured pattern of influence where each variate is affected primarily by preceding variates. This helps validate the intended behavior of the architecture.

5. **Reproducibility effort**: The authors provide source code, detailed hyperparameter choices (Table 4), and standard deviation estimates (Table 8). The use of established benchmark procedures (Wu et al. 2021, Zhou et al. 2021) supports backward comparability.

6. **Robustness analysis**: Figure 6 demonstrates stable performance across varying lookback lengths (96 to 2048) and prediction horizons, suggesting that the model does not overfit to a specific input window size.

## Weaknesses
Listed from most to least impactful:

1. **Main text contradicts appendix evidence on variate ordering sensitivity**. Section 3.2 states variate ordering is "empirically not a significant limitation," but Appendix A.5 (Table 7) shows up to 26% relative MSE degradation on Electricity at horizon 720 under permutation. This contradiction undermines the paper's self-assessment and suggests the limitation is more significant than stated. [Major]

2. **Overclaimed contribution statements**. The contribution list (Page 2) redundantly separates (i) the mixing approach and (ii) the method proposal, and uses unsupported "state-of-the-art" labeling. The conclusion uses "45 out of 64 cases" (summing MSE and MAE wins, which are correlated metrics) to inflate the apparent win count. "Extraordinary performance" is promotional language not supported by the evidence. [Major]

3. **Missing statistical significance analysis**. Although standard deviations are reported in Appendix A.6 (Table 8), the main results (Section 4.1, Table 2) do not reference them, and no significance tests are performed. Given that improvements over baselines are modest (2-5% relative MAE gains), the reader cannot assess whether differences are statistically reliable. [Major]

4. **Incomplete ablation analysis**. Of 12 ablation configurations in Table 3, only 4 are discussed in the main text (#1, #4, #5, #9). Configuration #8 (remove sLSTM entirely) is mentioned only indirectly in a parenthetical phrase despite showing the largest degradation. Interaction effects between components (e.g., init. token vs. view mixing in configurations #10-#12) are not analyzed. [Minor]

5. **Implementation ambiguity in key formulas**. The sLSTM equations (1)-(8) lack explicit tensor shape annotations. The multi-view mixing description (Section 3.3) does not precisely define what "reversed embedding" means. The NLinear dimension semantics could be clarified. These ambiguities reduce reproducibility. [Minor]

6. **Efficiency analysis overstates and underspecifies**. The claim of "one or two orders of magnitude less memory" (Page 9) does not specify which baseline model at which setting. Time increase from ~0.01s to ~0.02s as T grows from 96 to 1024 is described as "negligible" but represents a doubling. No variate-count scaling analysis is provided, which would be most informative given the variate-marching design. [Minor]

7. **Related work is a chronological list rather than a structured comparison**. Section 5.1 enumerates model families without comparison axes or explicit differentiation of xLSTM-Mixer's design space position. The connection to MLP-Mixer (interleaved mixing) is mentioned but the key architectural difference (sLSTM instead of MLPs) is not discussed. [Minor]

## Key Issues
### Issue 1: Main-text claim vs. appendix evidence on variate ordering (Severity: Major)
**Evidence**: Page 4 - Section 3.2 states variate ordering is "empirically not a significant limitation." Appendix A.5, Table 7 shows on Electricity at H=720, MSE is 0.183 (default) vs. 0.230 (Permutation #1), a 26% relative degradation. On ETTm1 at H=720, MSE is 0.409 vs. 0.413 across permutations (1% variation). On Weather, variation is negligible.
**Root cause**: The claim overgeneralizes from Weather-like datasets where ordering matters little, to Electricity-like datasets where it matters substantially.
**Impact**: Misleading self-assessment that could lead practitioners to underestimate the importance of variate ordering.
**Fix**: Revise Section 3.2 to qualify the claim with dataset-dependent evidence and reference Appendix A.5 explicitly.

### Issue 2: Inflated "45 out of 64 cases" metric (Severity: Major)
**Evidence**: Page 10 - Conclusion states "outperforming previous methods in 45 out of 64 cases." This sums 20 MSE wins + 25 MAE wins out of 32 settings each. Since MSE and MAE are correlated metrics on the same predictions, summing them double-counts.
**Root cause**: The authors treat MSE and MAE as independent evaluation dimensions, which is not statistically valid.
**Impact**: Inflates the apparent win rate. A reader comparing models would observe best MAE on 6/8 datasets (not 25/32).
**Fix**: Report "best or second-best average MAE on 7/8 datasets" instead.

### Issue 3: Missing statistical significance (Severity: Major)
**Evidence**: Table 2 reports averaged results without variance. Table 8 (Appendix) reports std but is never referenced in the main results narrative. Gains over baselines are 2-5% relative.
**Root cause**: Standard practice in time series benchmarking has often omitted significance testing; the authors follow this convention.
**Impact**: Readers cannot determine if reported improvements are statistically reliable, especially for small-margin cases.
**Fix**: Add a note in Section 4.1 referencing Table 8, e.g., "the MAE improvements exceed one standard deviation of the baseline on 5 of 8 datasets."

### Issue 4: Contribution list redundancy and hype (Severity: Major)
**Evidence**: Page 2 - Contribution (i) describes the architecture, (ii) claims SOTA for the same method. Both (ii) and (iii) use "state-of-the-art" before evidence is presented.
**Root cause**: The authors conflate methodological contributions with performance outcomes.
**Impact**: Reduces credibility with reviewers who expect distinct, falsifiable contribution claims.
**Fix**: Merge (i) and (ii) into one architectural contribution; rephrase (iii) to describe empirical findings rather than claiming SOTA.

### Issue 5: Selective ablation reporting (Severity: Minor)
**Evidence**: Table 3 contains 12 configurations. Only #1, #4, #5, #9 are discussed. Configuration #8 (remove sLSTM entirely, leaving only time mixing) shows the largest degradation (13.7% on Weather-192) but is mentioned only indirectly.
**Root cause**: The authors focus on components they consider important, overlooking the most informative baseline (the simplest non-recurrent variant).
**Impact**: The ablation narrative understates the importance of the sLSTM component relative to time mixing.
**Fix**: Discuss #8 explicitly as the minimal non-recurrent baseline and use it to quantify the marginal benefit of sLSTM refinement.

## Actionable Suggestions
### S1 (Must) — Revise contribution claims and tone
**Target**: Page 2 - Contribution list; Page 10 - Conclusion
**Action**: Replace the three overlapping contributions with two distinct claims:
- "(i) Architecture: We propose xLSTM-Mixer, which integrates time-mixing (NLinear), variate-marching sLSTM blocks with learned initial tokens, and multi-view reconciliation. (ii) Empirical findings: On 8 long-term benchmarks, xLSTM-Mixer achieves best or second-best average MAE on 7/8 datasets. Ablation, sensitivity, and interpretability analyses provide insight into each component's contribution."
**Rationale**: Separates architectural novelty from empirical findings; removes unsupported SOTA language.

### S2 (Must) — Reconcile main text and appendix on variate ordering
**Target**: Page 4 - Section 3.2
**Action**: Replace "While this is empirically not a significant limitation" with: "The sensitivity to variate ordering varies across datasets. Appendix A.5 shows that random permutations cause up to 26% relative MSE degradation on Electricity at long horizons, while effects on Weather and ETTm1 are smaller (<2%). Investigating optimal ordering strategies is left to future work."
**Rationale**: Aligns main text with empirical evidence; provides dataset-specific context.

### S3 (Must) — Fix inflated "45/64" metric in Conclusion
**Target**: Page 10 - Conclusion
**Action**: Replace "outperforming previous methods in 45 out of 64 cases" with "achieving the best or second-best average MAE on 7 out of 8 datasets."
**Rationale**: MSE and MAE are correlated; summing them double-counts same predictions.

### S4 (Must) — Add statistical significance context to main results
**Target**: Page 6 - Section 4.1
**Action**: Add one sentence after the numeric results: "As shown in Appendix Table 8, the MAE improvements over the second-best method exceed one standard deviation on 5 of 8 datasets, supporting the reliability of the reported gains."
**Rationale**: Connects main text to variance estimates; helps readers assess reliability.

### S5 (Nice-to-have) — Improve ablation narrative
**Target**: Page 7 - Ablation Study paragraph
**Action**: Add explicit discussion of configuration #8 (no sLSTM, only time mixing): "The largest degradation occurs when the sLSTM blocks are removed entirely (#8), indicating that the recurrent refinement is the primary accuracy driver. The remaining components (init. token, view mixing, NLinear vs. DLinear) provide additive but smaller gains."
**Rationale**: Provides a more complete and accurate picture of component importance.

### S6 (Nice-to-have) — Clarify implementation ambiguities
**Target**: Page 3 - sLSTM equations; Page 5 - Multi-View Mixing
**Actions**:
- After Eq. (8), add: "All states $c_t, n_t, h_t \in \mathbb{R}^d$ share the same dimensionality. The stabilizer $m_t \in \mathbb{R}$ is a scalar. Recurrent matrices $R$ are block-diagonal with $H$ heads."
- In Section 3.3, specify: "The reversed embedding $\hat{x}_{up}$ is obtained by reversing the $D$ latent dimensions: $\hat{x}_{up}[v, :] = \text{reverse}(x_{up}[v, :])$. The initial token $\eta$ is also reversed."

### S7 (Nice-to-have) — Strengthen efficiency analysis
**Target**: Page 9 - Model Efficiency paragraph
**Actions**:
- Replace "one or two orders of magnitude less memory" with specific numbers: "xLSTM-Mixer requires ~1,000 MB vs. PatchTST's ~10,000 MB at T=96 on Weather."
- Add a sentence on variate-count scaling: "When varying the number of variates rather than lookback length, xLSTM-Mixer's complexity grows linearly with V."
- Replace "negligible" with "sub-linear: time per iteration doubles from ~0.01s to ~0.02s as T increases from 96 to 1024."

## Storyline Options + Writing Outlines
### Abstract Outline (Complete revision)
Current abstract uses ~170 words but does not compactly convey the core idea. Target 4-5 sentences:

**S1 (Problem + Domain)**: "Multivariate time series forecasting requires models that capture both temporal dynamics and cross-variate dependencies, but existing approaches either assume channel independence (losing inter-variate information) or use quadratic-complexity attention (limiting scalability)."

**S2 (Gap)**: "Recurrent architectures offer a natural alternative due to their sequential processing of tokens, but have been under-explored for multivariate mixing."

**S3 (Method)**: "We propose xLSTM-Mixer, which combines a linear forecast (shared across variates) with sLSTM blocks that process variates sequentially, enabling cross-variate dependency learning at linear complexity. A multi-view mechanism reconciles forward and reversed latent representations under shared weights."

**S4 (Key Results — bounded)**: "On 8 long-term forecasting benchmarks, xLSTM-Mixer achieves the best or second-best average MAE on 7 of 8 datasets, with strongest gains on Weather, ETT, and Electricity."

**S5 (Implication)**: "Ablation and attribution analyses confirm that the sLSTM refinement is the primary accuracy driver and that the model learns interpretable cross-variate patterns."

### Introduction Outline (Complete paragraph-by-paragraph plan)

**P1 — Motivation and gap** (replace current P1):
"Role: Establish concrete stakes and specific unsolved challenge."
"Time series forecasting is critical in domains from energy management to healthcare (citing 2-3 key refs). A core challenge in multivariate settings is jointly modeling temporal evolution and cross-variate dependencies. Many approaches handle one aspect well but not both: channel-independent methods (PatchTST, DLinear) scale well but ignore inter-variate correlations; joint-mixing methods (Transformers, TCN) capture correlations but at higher computational cost."
→ Transition: "This gap motivates our design of a recurrent architecture that achieves both."

**P2 — Method positioning** (replace current P2):
"Role: Position xLSTM relative to prior art; state why recurrence for variates."
"Recurrent models were historically used for time series but limited by vanishing gradients. Recent advances in LSTM architectures — specifically the xLSTM family with exponential gating and memory mixing — offer improved expressivity. We argue that the natural sequential nature of recurrence is better suited for processing variates (as tokens) than for processing time steps, because variate count is typically smaller and more structured than time length."
→ Transition: "This insight drives our architecture design."

**P3 — Architecture preview** (revise current P3):
"Role: Give a 2-3 sentence high-level walkthrough before Section 3."
"xLSTM-Mixer has three stages: (1) a per-variate linear forecast (NLinear) that captures basic temporal patterns, (2) sLSTM blocks that refine these forecasts by processing variates sequentially with learned initial memory states, and (3) a multi-view reconciliation stage that combines forward and reversed representations."
→ Transition: "Contributions below."

**P4 — Contributions** (rewrite current contribution list):
"Role: State exactly 2 distinct contributions, no hype."
"(i) We propose xLSTM-Mixer, which integrates time mixing (linear forecast), variate-marching sLSTM recurrence, and multi-view reconciliation for multivariate forecasting. (ii) We provide extensive empirical evidence across 8 benchmarks, including ablation (12 variants), sensitivity, robustness, and Shapley-based interpretability analyses."

### Revised Title (optional)
Current: "xLSTM-Mixer: Multivariate Time Series Forecasting by Mixing via Scalar Memories"
Suggested: "xLSTM-Mixer: Multivariate Time Series Forecasting via Variate-Marching sLSTM with Multi-View Reconciliation"
Rationale: More precise about what is novel (variate-marching recurrence for mixing) and removes the underinformative "Scalar Memories."

## Priority Revision Plan
### P0 (Must — before resubmission)

| Order | Task | Target Section | Expected Impact | Effort |
|-------|------|----------------|-----------------|--------|
| 1 | Revise contribution list: merge (i)+(ii); remove unsupported SOTA language | Page 2 | Corrects overclaim; improves credibility | Low (text edit) |
| 2 | Reconcile variate-ordering claim with Appendix A.5 evidence | Page 4 - Section 3.2 | Fixes factual inconsistency | Low (text edit) |
| 3 | Replace "45/64" metric with per-dataset average MAE ranking | Page 10 - Conclusion | Eliminates misleading double-count | Low (text edit) |
| 4 | Add sentence referencing standard deviations (Table 8) to main results | Page 6 - Section 4.1 | Adds significance context | Low (1 sentence) |
| 5 | Soften "exceptional" and "extraordinary" to evidence-consistent language | Pages 1, 6, 10 | Removes hype | Low (text edit) |

### P1 (High priority — strengthen validity)

| Order | Task | Target Section | Expected Impact | Effort |
|-------|------|----------------|-----------------|--------|
| 6 | Discuss ablation config #8 explicitly as minimal baseline | Page 7 | Completes ablation narrative | Low (2-3 sentences) |
| 7 | Add tensor shape annotations to sLSTM equations | Page 3 - Eq. (1)-(8) | Improves reproducibility | Low (1 sentence) |
| 8 | Clarify "reversed embedding" definition in Section 3.3 | Page 5 - Section 3.3 | Resolves implementation ambiguity | Low (1 sentence) |

### P2 (Nice-to-have — quality improvement)

| Order | Task | Target Section | Expected Impact | Effort |
|-------|------|----------------|-----------------|--------|
| 9 | Quantify "1-2 orders of magnitude" efficiency claim with specific baseline numbers | Page 9 | Improves precision | Low |
| 10 | Restructure Related Work Section 5.1 with comparison axes | Page 10 | Improves reader understanding | Medium |
| 11 | Add variate-count efficiency scaling experiment | Page 8-9 / Appendix | Fills gap in efficiency analysis | Medium |
| 12 | Conduct paired significance tests for key comparisons | Appendix | Strengthens statistical rigor | Medium |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|--------------|-----------------|-------------------|
| E1 | Long-term forecasting (Table 2) | 8 datasets, 4 horizons, 12 baselines | MSE, MAE (3 seeds averaged) | Best/2nd-best MAE on 7/8 datasets | C2 (performance) | No significance tests; variance in appendix only |
| E2 | Ablation study (Table 3) | Weather & ETTm1, 12 configs, 4 horizons | MSE, MAE | Full model (#1) best overall; sLSTM critical | C1 (architecture) | Selective reporting; interaction effects not analyzed |
| E3 | Hidden dimension sensitivity (Fig. 4) | Electricity, varying up-proj. dim D | MSE | Larger D improves longer horizons | Robustness | Single dataset; no computational cost tradeoff |
| E4 | Initial token visualization (Fig. 3) | Weather, ETTm1, ETTh2, 4 horizons | Decoded forecast | Tokens capture dataset-specific patterns | Interpretability | Single seed for noisy datasets |
| E5 | Shapley attribution (Fig. 5, Fig. 8) | Weather, ETTh2, ETTm1 | Attribution scores | Lower-triangular cross-variate pattern | Interpretability (cross-variate) | No quantitative summary metric; causal direction confound |
| E6 | Model efficiency (Fig. 7) | Weather & Electricity, varying T, H=336 | Time/iter, GPU memory | Sub-linear scaling with T | Efficiency | No variate-count scaling; ambiguous baseline comparison |
| E7 | Lookback robustness (Fig. 6) | ETTm1, T=96 to 2048, 4 horizons | MSE | Stable performance across T | Robustness | Single dataset |
| E8 | Variate permutation (Table 7, Appendix) | Weather, ETTm1, Electricity, 4 permutations | MSE, MAE | Performance varies (up to 26% degradation) | Sensitivity | Only 4 permutations; Electricity worst-case |
| E9 | Short-term forecasting (Table 5, Appendix) | PEMS03, PEMS08, H=12 | MAE, MAPE, RMSE | Competitive but not best | Coverage | Only 2 datasets; no comparison to short-term specialists |
| E10 | Standard deviation (Table 8, Appendix) | All 8 datasets | MSE, MAE ± std | Low variance (0.000–0.046) | Reproducibility | Not integrated into main results |

### Research-Theme Gap Diagnosis

1. **Causal attribution gap**: The paper attributes gains to specific components (sLSTM, time mixing, view mixing) but does not establish causal separation. The ablation study shows correlation between component presence and performance, but confounders (parameter count, training dynamics) are not controlled.

2. **Generalization gap**: All experiments are in-distribution long-term forecasting. The paper claims robustness (varying lookback, hyperparameters) but does not test distribution shift, noise, or missing data scenarios.

3. **Practical value gap**: The efficiency analysis (Fig. 7) varies lookback length but not variate count. Since the main complexity advantage is linearity in variates, this experiment would be most informative for practitioners choosing the model for high-dimensional settings.

4. **Batch effect gap**: All experiments use standardized preprocessing and fixed train/val/test splits. There is no cross-validation or assessment of sensitivity to data partitioning.

### Proposed Research Experiments

**P0 (Minimum for publication readiness)**

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|--------|-------------|------------|---------------|-------------------|---------|------------------|-----------|---------------|
| PE1 | C2 (Performance) | Gains exceed baseline variance | Add paired significance test against best baseline per dataset | Same data splits, 5 runs | p-value, effect size | p<0.05 on ≥5/8 datasets | 1 GPU-day | Validity |
| PE2 | C1 (Ordering sensitivity) | Different orderings materially affect performance | Re-run top-5 models under 5 random variate permutations | xLSTM-Mixer, TimeMixer, PatchTST | MSE, MAE variance across permutations | Report mean±std across permutations | 2 GPU-days | Honest limitation |

**P1 (High priority for robustness)**

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|--------|-------------|------------|---------------|-------------------|---------|------------------|-----------|---------------|
| PE3 | Robustness | Model remains stable under input noise | Add Gaussian noise (σ=0.01, 0.05, 0.1) to test inputs | Same model, no noise baseline | MSE relative increase | <10% at σ=0.05 | 1 GPU-day | Robustness evidence |
| PE4 | Efficiency (variate scaling) | xLSTM-Mixer scales linearly with V | Run on synthetic data with V=10, 50, 100, 500, 1000 | NLinear, PatchTST, TimeMixer | Time/iter, GPU memory | Sub-linear in V relative to Transformers | 1 GPU-day | Practical guidance |
| PE5 | Cross-variate learning | Shapley scores correlate with known dependency strength | Use synthetic data with controlled dependency matrix | Random baseline | Correlation between known and learned dependencies | Spearman ρ>0.5 | 1 GPU-day | Mechanism validation |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score**: 6/10

Rationale: The paper presents a well-engineered architecture with competitive empirical results across 8 benchmarks. However, the score is reduced by (1) overclaimed contribution statements (redundant claims, unsupported SOTA language, inflated "45/64" metric), (2) a factual inconsistency between the main text and appendix regarding variate ordering sensitivity, (3) missing statistical significance analysis for small-margin improvements, and (4) novelty uncertainty due to concurrent related work (xLSTMTime, Kong et al. 2024). The architectural design (variate-marching sLSTM + multi-view mixing) has merit and is supported by thorough ablation, but the paper's presentation weakens its impact.

**Post-Revision Target**: [7, 8]/10

If the authors address the P0 items (revise contribution claims, reconcile main text/appendix, add significance context, soften hype language) and P1 items (complete ablation narrative, clarify implementation ambiguities), the paper could reach a score of 7-8. The empirical foundation is solid; the main barriers are presentation rigor and evidence consistency. With the proposed robustness experiments (noise sensitivity, variate-count scaling), the score could reach 8.