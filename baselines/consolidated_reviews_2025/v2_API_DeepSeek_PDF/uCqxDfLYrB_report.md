## Summary
# Final Review Report

## Summary

This paper empirically investigates neural scaling laws for time series foundation models (TSFMs), extending prior work from in-distribution (ID) to out-of-distribution (OOD) settings and comparing encoder-only vs. decoder-only Transformer architectures. The authors train models spanning ~1K to ~100M parameters on a curated 16.8B time-point corpus across 7 domains, evaluating on ID validation data and two OOD benchmarks (LSF and Monash). 

**Key findings reported:** (1) NLL follows a power-law in both ID and OOD settings with similar exponents for parameter and compute scaling, but data scaling shows different behavior for NLL vs MAPE. (2) Encoder-only and decoder-only Transformers exhibit similar OOD scalability, with encoder-only having a slight ID advantage. (3) Architectural enhancements in Moirai and Chronos improve ID performance but reduce OOD scalability. (4) Design principles are provided for data, model, and compute scaling.

**Overall assessment:** The paper addresses a timely and important question — understanding how TSFMs scale across distributions and architectures. The experiments are extensive and the empirical methodology is largely sound. However, several issues reduce confidence in the quantitative claims: the parameter-count approximation may bias small-model exponents, key derivations (e.g., D ∝ N^0.8) lack traceable numerical values, the cross-distribution scaling summary contains an internal contradiction, and some claims (3M threshold, "larger model more important than more data") overstate the evidence. Novelty verification is deferred due to external literature search being unavailable in this run.

## Strengths
1. **Timely and well-motivated research question.** The paper asks three concrete, practically important questions about TSFM scaling — OOD behavior, architecture effects, and design principles — that are directly relevant to the growing TSFM community. The motivation is clearly articulated and the questions are non-trivial.

2. **Extensive experimental scope.** Training models across ~1K to ~100M parameters on a 16.8B time-point corpus is a substantial undertaking. The data curation pipeline (deduplication, SNR filtering, domain balancing) is methodologically sound and well-documented in the appendix. The inclusion of two independent OOD benchmarks (LSF and Monash) strengthens reliability.

3. **Novel cross-architecture comparison.** To our knowledge, this is the first systematic comparison of encoder-only vs. decoder-only Transformer scaling in the time series domain. The inclusion of Moirai and Chronos as case studies adds practical relevance. The finding that architectural enhancements can improve ID performance but reduce OOD scalability is actionable for TSFM design.

4. **Practical design principles.** Section 4 translates scaling exponents into actionable guidance (e.g., D ∝ N^0.8 relationship, compute allocation recommendations). These principles are directly useful for practitioners building larger TSFMs.

5. **Open reproducibility commitment.** The paper provides detailed training/evaluation configurations, hyperparameters, and a GitHub repository link. The appendix contains thorough dataset descriptions, evaluation metrics, and convergence analysis.

## Weaknesses
### W1. Parameter count approximation may distort small-model scaling (Major)
The parameter formula (Eq. 1) excludes embedding layers (32·dm), prediction head (512·dm), biases, and layer norm. For small models (~1K-10K parameters), these excluded terms can dominate (e.g., for dm=8, nlayer=2, approximate N≈1.5K but actual parameters ≈6K-8K). This systematically shifts small-model x-axis positions leftward in Figures 2-4, potentially biasing power-law exponent fitting, especially in the low-parameter regime that anchors the scaling curve.
*Verification check:* Parameter formula derivation was verified; embedding + head scaling confirmed to dominate for dm < 64.

### W2. Internal contradiction in cross-distribution scaling summary (Major)
The "Cross-distribution Scaling Effects" summary (Page 6) states that "For NLL, the model exhibits similar scaling patterns in both ID and OOD scenarios" for all three factors. However, the Data Scaling subsection on the same page explicitly states "ID and OOD performance do not exhibit the same scaling behavior when evaluated using NLL" and that "ID performance is more sensitive to the scaling of dataset size." This contradiction undermines the paper's core empirical claim (C1). The summary must be revised to precisely bound which factor × metric combinations show consistent vs. divergent scaling.

### W3. Design principle D ∝ N^0.8 lacks traceable exponent values (Major)
Section 4 derives D ∝ N^0.8 from the ratio α_N/α_D, but neither α_N nor α_D is reported numerically in the main text. Moreover, the 90%/97% reduction guidance (from data scaling) produces α_D ≈ 0.15 (OOD MAPE) and α_D ≈ 0.044 (ID MAPE). If parameter scaling α_N ≈ 0.3 (from visual inspection of Figure 2), the ratio α_N/α_D ≈ 2.0, not 0.8. This mathematical tension must be resolved by reporting actual fitted exponents and showing the calculation chain.

### W4. Qualitative architecture comparison without numeric exponent reporting (Major)
The encoder-only vs. decoder-only comparison (Section 3.2) relies on qualitative descriptions ("slight advantage," "marginally higher," "nearly identical scalability") without reporting actual power-law exponents, confidence intervals, or statistical tests. Given that C2 ("scaling laws across model architectures") is a core contribution, the absence of numerical exponent tables with uncertainty bounds significantly weakens the claim.

### W5. Conclusion overstates the "model-size vs data-size" claim (Major)
The Conclusion states "larger model may be more important than more data" without conducting joint scaling experiments (varying N and D simultaneously). The paper separately analyzes parameter, compute, and data scaling, which does not support a direct model-size vs. data-size comparison. This claim should be removed or replaced by a bounded statement.

### W6. OOD definition and evaluation protocol require stronger justification (Moderate)
The main text does not explicitly justify why LSF and Monash constitute out-of-distribution data relative to the pre-training corpus. The relevant analysis (Table 4 on SNR, shifting, stationarity, transition) is only in the appendix. Without this justification in the main text, the paper's primary contribution (C1 — OOD scaling laws) rests on an operationally unclear definition of OOD.

### W7. Chronos causal attribution is speculative (Moderate)
The paper attributes Chronos's limited NLL scalability to discrete probability prediction without conducting a controlled ablation. Other architectural differences (encoder-decoder vs. decoder-only, point-wise vs. patch-wise, different tokenization) could also contribute. The causal claim needs to be hedged or supported by experiment.

### W8. Missing variance and significance reporting (Moderate)
No confidence intervals, standard deviations, or significance tests are reported for any of the scaling exponents or performance metrics. Given that the paper reports "significant noise in NLL and MAPE during training" (Page 6), the absence of uncertainty quantification makes it difficult to assess whether observed differences between architectures or distributions are statistically reliable.

## Key Issues
### Ranked Error Board (High Risk First)

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence |
|------|-------|----------|--------------|------------|------------|
| 1 | W3: D ∝ N^0.8 lacks traceable exponents; potential mathematical inconsistency with 90%/97% data scaling numbers | Major | High: invalidates design principle | Fixable: report exponents and recalculate | High |
| 2 | W2: Cross-distribution scaling summary contradicts Data Scaling paragraph | Major | High: undermines C1 core claim | Fixable: revise summary to be factor×metric specific | High |
| 3 | W1: Parameter count approximation biases small-model exponents | Major | Medium-High: affects fitted α_N values | Fixable: add exact counts or sensitivity analysis | High |
| 4 | W4: Architecture comparison lacks numeric exponent values and CIs | Major | Medium: weakens C2 evidence | Fixable: add exponent table with intervals | High |
| 5 | W5: Conclusion overstates model-size vs data-size without joint experiment | Major | Medium: overclaim | Fixable: remove or bound the claim | High |

### Summary of Critical Issues Confirmed by Evidence Pack
- **None of the issues are fatal.** All major issues have concrete, feasible fix paths.
- **Highest priority:** Resolve W3 (D ∝ N^0.8 derivation) and W2 (internal contradiction) because they directly affect the reliability of the claimed contributions C1 and C3. Without these fixes, readers cannot trust the quantitative design principles.
- **Novelty risk:** External literature verification is deferred in this run (Retrieval-Disabled Mode), so novelty-related risk cannot be fully assessed. The paper's contributions (OOD scaling, architecture comparison) appear empirically sound, but comparison against related scaling-law papers (Edwards et al., Shi et al.) needs manual verification.

## Actionable Suggestions
### S1 (Must, W1): Report exact parameter counts and sensitivity analysis
Add a supplementary table showing both the approximate N (Eq. 1) and the exact total parameter count (including embedding, head, biases, layer norm) for each model size. Fit power-law exponents using both approximations and report the difference. If the exponents change by >10% for the small-model regime, refit all scaling curves using exact counts and update Figures 2-4.

**Location affected:** Page 4 - Eq. (1) and Figure 2.

### S2 (Must, W2): Revise cross-distribution scaling summary
Replace the current 3-point summary with a factor×metric table that precisely states which combinations show consistent vs. divergent OOD/ID scaling. Specifically:
- For (N, NLL): consistent OOD/ID (similar slopes, constant shift)
- For (C, NLL): consistent OOD/ID
- For (D, NLL): **inconsistent** — ID more sensitive than OOD
- For MAPE on all three factors: OOD exponents larger than ID

**Location affected:** Page 6 - Cross-distribution Scaling Effects.

### S3 (Must, W3): Report all fitted exponents with confidence intervals
Add a dedicated table (main text or appendix) reporting α_N, α_C, α_D for each (model architecture, metric, distribution) combination. Include 95% confidence intervals or standard errors. Show the calculation chain for D ∝ N^(α_N/α_D) explicitly, using the reported values. If the ratio is not 0.8, correct the claim.

**Location affected:** Page 9 - Model Parameters and Architecture design principle.

### S4 (Must, W4): Add exponent comparison table for encoder vs decoder
For the architecture comparison, add a table with fitted α values for encoder-only and decoder-only under each scaling factor and distribution, with confidence intervals. Use a simple statistical test (e.g., non-overlapping CI) to determine which differences are significant.

**Location affected:** Page 7 - Section 3.2.

### S5 (Must, W5): Remove or bound the model-size vs data-size claim
Replace the Conclusion sentence "larger model may be more important than more data" with: "Our separate analyses of parameter, compute, and data scaling suggest that within the tested range, parameter scaling yields the largest per-unit improvement in MAPE. Joint scaling experiments (varying N and D simultaneously) are needed to determine the optimal allocation between model size and data."

**Location affected:** Page 10 - Conclusion.

### S6 (Must, W6): Justify OOD designation in main text
Add a 2-3 sentence summary of Table 4 in the main text (Page 2, Dataset section) showing that LSF and Monash have lower SNR and different stationarity/transition characteristics compared to the pre-training corpus, justifying their OOD status.

### S7 (Nice-to-have, W7): Ablate discrete prediction head
Train the decoder-only Transformer baseline with a discrete-output prediction head (same quantization scheme as Chronos). Compare scaling exponents. If this is too expensive, add hedging language: "This pattern is consistent with the discrete prediction hypothesis, though encoder-decoder architecture differences may also contribute."

### S8 (Nice-to-have, W8): Add variance reporting
Report mean ± std over at least 3 random seeds for the key NLL/MAPE values in Figures 2-4, or provide bootstrap confidence intervals for the fitted power-law exponents.

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current narrative arc is: (P1) TS forecasting is important, TSFMs are emerging, scaling is trending → (P2) Scaling laws exist but only for ID, three open questions → (P3) Our experiments answer these questions → Contributions. This is functional but the stakes are not fully established until late in the introduction.

### Abstract Outline (Target: 5 sentences)
- **S1 (Problem+Domain):** "Neural scaling laws are essential for guiding the development of time series foundation models (TSFMs), but prior work has focused only on in-distribution (ID) settings."
- **S2 (Gap):** "It remains unknown whether scaling laws hold for out-of-distribution (OOD) forecasting — where TSFMs are most needed — and how model architecture affects scalability."
- **S3 (Method/Scope):** "We train encoder-only and decoder-only Transformers from 1K to 100M parameters on a 16.8B time-point corpus across 7 domains, evaluating on ID and two OOD benchmarks."
- **S4 (Key Quantified Finding):** "NLL follows a power law in both ID and OOD settings with comparable exponents (α_N ≈ 0.3), but data scaling shows divergent behavior: NLL improvements favor ID while MAPE improvements favor OOD."
- **S5 (Implication):** "We derive actionable design principles — including a D ∝ N^0.8 scaling relationship — and show that architectural modifications that improve ID performance can reduce OOD scalability."

### Introduction Outline (Paragraph-by-Paragraph)

**P1 (Big Picture + Stakes, ~8 sentences):**
Role: Establish why TSFM scaling laws matter practically.
Content: (1) Time series forecasting drives decisions in energy, climate, finance, and urban computing. (2) TSFMs promise universal forecasting across domains. (3) Scaling models and data has shown empirical gains. (4) However, the community lacks a predictive framework for expected returns on scaling investment.
*Transition to P2:* "Neural scaling laws (Kaplan et al., 2020) provide such a framework — but existing studies cover only a fraction of what TSFMs need."

**P2 (Scaling Laws + Prior Gap, ~7 sentences):**
Role: Introduce scaling laws and identify the precise gaps.
Content: (1) Standard scaling laws describe power-law improvement with N, C, D. (2) For TSFMs, only ID scaling has been studied. (3) OOD forecasting is where TSFMs are most impactful. (4) Architecture effects on scalability are unknown. (5) Three research questions emerge.
*Transition to P3:* "In this paper, we address these questions through systematic empirical study."

**P3 (Our Approach + Results, ~6 sentences):**
Role: Summarize experimental design and key findings.
Content: (1) We train encoder and decoder Transformers at multiple scales. (2) We evaluate on ID and OOD benchmarks. (3) Key result: NLL scaling is similar ID/OOD for N and C, but diverges for D. (4) Encoder and decoder scale similarly; advanced TSFMs gain ID but lose OOD scalability.
*Transition to P4 (Contributions):* "Our main contributions are threefold: ..."

**P4 (Contributions):**
Three explicit, bounded bullets as revised per Suggestion.

### Alternative Storyline Candidates

**Candidate A (Problem-First):** Start with a concrete failure case: a TSFM that works well on seen domains but fails on a closely related unseen domain. Then ask: could scaling laws predict this? This would immediately create reader engagement.

**Candidate B (Architecture-Centric):** Lead with the observation that TSFM architectures are diverging (encoder, decoder, encoder-decoder) and the community has no principled way to decide which scales better. This would position the paper as a practical guide.

**Recommended choice:** Keep the current structure but merge P2 (scaling laws) material into P1 for tighter pacing. Use Candidate A's hook as the opening of P1.

## Priority Revision Plan
### P0 — Critical (Must-fix before re-submission)

| Order | Task | Issue | Expected Impact | Effort |
|-------|------|-------|-----------------|--------|
| 1 | Report all fitted exponents (α_N, α_C, α_D) with CIs for each condition; recalculate D ∝ N^(α_N/α_D) | W3 | Resolves design principle validity; enables readers to verify quantitative claims | 2-3 days |
| 2 | Revise cross-distribution scaling summary to be factor×metric specific; resolve ID/OOD NLL contradiction | W2 | Core empirical claim becomes internally consistent | 1 day |
| 3 | Add exact parameter counts + sensitivity analysis for small models; refit exponents if needed | W1 | Ensures scaling curves are not biased in the low-parameter regime | 2-3 days |
| 4 | Add exponent comparison table for encoder vs decoder (with CIs) | W4 | Architecture comparison becomes quantitative instead of qualitative | 1-2 days |
| 5 | Replace overclaimed Conclusion sentence with bounded statement | W5 | Eliminates unsupported claim | 0.5 day |

### P1 — High Priority (Should-fix for best outcome)

| Order | Task | Issue | Expected Impact | Effort |
|-------|------|-------|-----------------|--------|
| 6 | Add OOD justification (Table 4 summary) to main text | W6 | Strengthens C1 foundation; OOD claim becomes verifiable | 0.5 day |
| 7 | Add confidence intervals / variance bars to scaling plots | W8 | Allows statistical assessment of exponent differences | 3-5 days |
| 8 | Soften Chronos causal attribution or add ablation | W7 | Improves scientific rigor of architecture case study | 2-5 days |

### P2 — Nice-to-Have

| Order | Task | Expected Impact | Effort |
|-------|------|-----------------|--------|
| 9 | Add quantitative analysis of emergent behavior prevalence across OOD datasets | Strengthens emergent phenomena section | 1-2 days |
| 10 | Restructure Related Work (TSFMs) into thematic instead of chronological listing | Improves readability and positioning | 0.5 day |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|--------------|-----------------|-------------------|
| E1 | Parameter scaling (encoder-only) | Train models 1K-100M on full corpus; evaluate ID and OOD | NLL, MAPE | Power-law scaling with N | C1 | Exponent values not reported; CI missing |
| E2 | Compute scaling (encoder-only) | Vary compute C = 6·N·B·S across 6 orders of magnitude | NLL, MAPE | Power-law scaling with C; optimal N varies | C1 | Compute formula notation ambiguous |
| E3 | Data scaling (encoder-only) | Train 1B models on 10M, 100M, 1B subsets | NLL, MAPE | Power-law scaling with D; different NLL behavior for ID vs OOD | C1 | Model size fixed at 1B; exponents may not generalize |
| E4 | Encoder vs decoder scaling | Compare encoder-only vs decoder-only on all three factors | NLL | Similar OOD scalability; encoder slight ID advantage | C2 | No numeric exponent comparison; no CIs |
| E5 | Encoder-only vs Moirai | Parameter scaling comparison | NLL | Moirai better ID but encoder-only catches up OOD | C2 | Causal attribution speculative |
| E6 | Decoder-only vs Chronos | Parameter scaling comparison | NLL, SMAPE | Chronos better ID but not OOD; discrete NLL issue | C2 | No discrete-prediction ablation |
| E7 | ETS comparison | Classical smoothing baseline | NLL, MAPE | Pre-trained models beat ETS at >3M parameters | C1 | Threshold not statistically validated |
| E8 | Emergent behavior analysis | Case study on 3 datasets | MAPE | Non-power-law improvement at ~10M threshold | — | Only 3 examples; no prevalence statistics |
| E9 | Ablation: Gaussian vs Student-t mixtures (Appendix B) | Compare mixture distributions | NLL | Student-t better convergence and performance | — | Only one comparison setting |

### Research-Theme Gap Diagnosis

**New Knowledge:** The paper's main new knowledge contribution is demonstrating that (a) OOD scaling laws exist and follow power-law patterns similar to ID for N and C but diverge for D, and (b) architecture choices affect scalability, with ID-optimized designs reducing OOD scalability. These findings are valuable to the TSFM community.

**Reproducibility:** The dataset curation, training protocol, and evaluation setup are well-documented. However, the missing exponent values and parameter approximation issues reduce the quantitative reproducibility of the scaling laws.

**Impact on Practice:** The design principles (Section 4) are the most practically impactful part of the paper. The D ∝ N^0.8 relationship and compute allocation guidance directly inform resource allocation decisions. However, the mathematical tension in the derivation (W3) currently undermines this impact.

### Proposed Research Experiments (P0/P1/P2)

**Exp-P0.1: Joint Parameter-Data Scaling (Target Claim C3)**
- *Hypothesis:* Optimal ratio of model size to data follows D ∝ N^(α_N/α_D) as derived, with the specific ratio confirmed by joint scaling experiments.
- *Minimal Design:* Train models at 3 parameter sizes (10M, 30M, 100M) × 3 data sizes (100M, 300M, 1B time points) = 9 runs.
- *Controls/Baselines:* Same training budget, same architecture (encoder-only).
- *Metrics:* NLL, MAPE on ID and OOD.
- *Success Criterion:* Joint surface confirms the exponent ratio within 20% of the independently derived value.
- *Estimated Cost:* ~3-5 GPU-days.
- *Expected Paper-Quality Gain:* Directly validates C3 design principle; resolves W3.

**Exp-P0.2: Small-Model Sensitivity Analysis (Target Claim C1)**
- *Hypothesis:* Power-law exponent values are stable when exact (not approximate) parameter counts are used.
- *Minimal Design:* Recompute Figure 2 x-axis using exact parameter counts (include embedding, head). Refit power law.
- *Controls/Baselines:* Same models, same metrics.
- *Metrics:* α_N (exact) vs α_N (approximate).
- *Success Criterion:* α_N changes by <10% for the range 1K-100M.
- *Estimated Cost:* 0.5-1 day of analysis.
- *Expected Paper-Quality Gain:* Resolves W1; strengthens confidence in all exponent-based claims.

**Exp-P1.1: Discrete Prediction Ablation (Target Claim C2 - Chronos analysis)**
- *Hypothesis:* The discrete output head (not the encoder-decoder architecture) is the primary cause of Chronos's reduced OOD scalability.
- *Minimal Design:* Modify decoder-only baseline to use discrete output head with same quantization as Chronos. Train at 3 sizes (1M, 10M, 100M).
- *Metrics:* NLL, SMAPE on ID and OOD.
- *Success Criterion:* Discrete-output decoder shows similar scaling pattern to Chronos.
- *Estimated Cost:* 2-3 GPU-days.
- *Expected Paper-Quality Gain:* Strengthens causal attribution in Section 3.2; resolves W7.

### ASCII Diagram — Experiment Upgrade Plan

```text
Exp-P0.1: Joint N×D Scaling
[3 Model Sizes] × [3 Data Sizes]
    10M    30M    100M     ← N
     │      │       │
100M ┼──────┼───────┼─── C1: verify D ∝ N^0.8
300M ┼──────┼───────┼───
  1B ┼──────┼───────┼───
     ↑       ↑       ↑
     Each: encoder-only, full training budget

Exp-P0.2: Exact Parameter Sensitivity
[Approx N] ──► [Exact N] ──► Compare α_N

Exp-P1.1: Discrete Ablation
[Decoder-only + continuous head] ──► Baseline
[Decoder-only + discrete head]   ──► Test (matches Chronos behavior?)
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

*Rationale:* The paper addresses a timely and important problem with extensive experiments. The core empirical findings (power-law scaling in OOD settings, architecture-dependent scalability) are valuable contributions. However, the score is constrained by:
- Several major weaknesses (W1-W5) that reduce confidence in the quantitative claims
- Internal contradiction in the core scaling summary (W2)
- Missing exponent values and CIs that prevent verification of design principles (W3, W4)
- Deferred novelty verification (external literature unavailable in this run)
- Overclaimed conclusion statement (W5)

The paper's research value is solid but the current presentation contains unresolved empirical tensions that must be addressed before the contributions can be fully trusted.

**Post-Revision Target: [7.5, 8.5] / 10**

This target assumes all P0 and most P1 items are addressed: exponent values with CIs are reported, the D ∝ N^0.8 derivation is corrected and traceable, the cross-distribution summary is made internally consistent, and overclaims are bounded. If authors also add joint scaling experiments (Exp-P0.1) and variance reporting, the upper bound (8.5) becomes realistic. Novelty verification via manual literature comparison would further strengthen the case.