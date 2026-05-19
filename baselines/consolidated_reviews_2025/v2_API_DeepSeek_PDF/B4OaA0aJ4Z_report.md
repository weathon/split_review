## Summary
# Final Review Report

## Summary

This paper presents FoundTS, a benchmarking framework for evaluating foundation models in time series forecasting (TSF). FoundTS covers 11 foundation models (both LLM-based and time-series pre-trained) and 7 specific models across 14 datasets spanning 10 domains. The benchmark supports three evaluation strategies—zero-shot, few-shot, and full-shot—with standardized settings for dataset splitting, sampling, and normalization. The authors conduct extensive experiments and produce several useful findings: (1) time-series pre-trained models generally outperform LLM-based models in few-shot settings; (2) no single model dominates across all datasets and characteristics; (3) the scaling law does not consistently hold across different model architectures; and (4) some lightweight specific models remain competitive with foundation models under data scarcity. The paper addresses a genuine need in the rapidly evolving TSF foundation model landscape. However, several methodological choices (best-per-lookback reporting, single-seed experiments, absence of statistical testing) and writing issues (unsubstantiated causal claims, vague contribution statements, missing limitations section) reduce the paper's rigor. With revisions addressing these issues, the benchmark could become a valuable community resource.

## Strengths
**S1. Timely and relevant benchmarking contribution.** The paper addresses a genuine gap in the TSF literature. As foundation models proliferate, the community urgently needs a standardized evaluation framework. FoundTS's coverage of 11 foundation models (both LLM-based and TS pre-trained) plus 7 specific models across 14 datasets is the most comprehensive among existing benchmarks.

**S2. Multi-strategy evaluation design.** The inclusion of zero-shot, few-shot, and full-shot evaluation strategies under a unified pipeline is the paper's strongest practical contribution. The standardization of dataset splitting, normalization, and sampling across all models directly addresses the fragmentation identified in Table 1, where prior work used inconsistent protocols.

**S3. Informative analysis of model characteristics.** Section 4.2 provides valuable insights, particularly the channel-dependence analysis (4.2.1), architecture comparison (4.2.2), pretrain vs. no-pretrain study (4.2.4), and efficiency analysis (4.2.5). These go beyond simple ranking and help explain *why* different models behave differently.

**S4. Useful taxonomy and categorization.** The classification of TS pre-trained models into reconstruction, autoregressive, direct prediction, and hybrid types (Section 3.2.1) provides a useful organizational framework for the community.

**S5. Reproducibility commitment.** The authors provide code and datasets, and define experimental settings (PyTorch, A800 GPU, L2 loss, Adam optimizer, early stopping) clearly in Appendix A.3.

## Weaknesses
**W1. "Best across lookback lengths" reporting undermines fairness.** (Page 6 - Evaluation Settings) The paper reports the best performance across tested lookback lengths for each model. This means different models are compared under different input conditions. A model that is sensitive to lookback length may appear better than a robust model simply because its optimal lookback is selected. This directly contradicts the paper's fairness objective (C2). The standard practice in time series benchmarking is to use a consistent lookback or report all lookback results separately.

**W2. No statistical significance or variance reporting.** All reported results are single-seed point estimates without confidence intervals, standard deviations, or significance tests. Given that performance differences between models are often small (e.g., 0.01-0.05 MSE), the rankings in Tables 4-6 may not be statistically reliable. This is a major gap for a benchmark that aims to provide "reliable insight."

**W3. Unsupported causal claims in analysis.** Several analytical conclusions use causal language without supporting evidence. Examples include: (Page 7) "smaller parameter sizes allow for faster fitting" — no control experiment isolates model size from architecture; (Page 3) "outstanding zero-shot capability" of LLM-based models — contradicted by the paper's own results showing LLM-based models often underperform; (Page 8) scaling law claims without controlled architecture experiments.

**W4. Missing Limitations section.** The Conclusion (Page 10) does not discuss any limitations of FoundTS itself (static benchmark, best-lookback reporting bias, training timeout constraints, dataset staleness). This omission reduces scientific credibility and completeness.

**W5. Abstract lacks quantitative anchoring.** The Abstract (Page 1) describes FoundTS's features but does not report any concrete results. For a benchmark paper, the Abstract should provide at least one quantitative finding that communicates the paper's empirical contribution.

**W6. Mixed evidence undermines strong pretrain conclusions.** (Page 9 - Section 4.2.4) Table 7 shows TimesFM performs worse WITH pretraining on Weather (MSE 0.436 vs 0.274), contradicting the general claim that pre-training helps. The text does not discuss this anomaly. Conclusions about LLM-based pre-training being harmful are also inconsistent across models in the same table.

**W7. Related work overstates LLM capabilities.** (Page 3) The claim that LLM-based models have "outstanding" zero-shot capabilities is at odds with the paper's empirical finding (Table 5) that LLM-based models generally underperform simple specific models in few-shot settings.

## Key Issues
**Issue 1 (Severity: Major) — Best-per-lookback evaluation confounds model comparison.** 
- **Evidence:** Page 6: "For each prediction length, we report the best performance across different lookback lengths."
- **Verification:** Cross-check with Appendix D shows each model's reported result may use a different lookback length (96, 336, or 512). The paper does not disclose which lookback each model used for each dataset.
- **Impact:** This design choice means the primary result tables (Tables 4-6) do not compare models under identical conditions. A model that works well at lookback=96 is compared with a model optimized for lookback=512, conflating model quality with lookback sensitivity. For a benchmark whose central claim is "fair comparison," this is a critical inconsistency.
- **Fix:** Report results per-lookback in main tables, or use average across lookbacks as the primary metric while keeping per-lookback results in appendix.

**Issue 2 (Severity: Major) — Missing variance and statistical testing.**
- **Evidence:** All reported results (Tables 4-6, 7, 11-16) are single runs. No standard deviations, confidence intervals, or significance tests are provided.
- **Verification:** In Table 5, performance differences between models on the same dataset are often <0.02 MSE (e.g., Timer 0.406 vs ROSE 0.399 on ETTh1). Without variance estimates, readers cannot assess whether these differences are meaningful.
- **Impact:** The paper's stated goal includes "reliable insight" and "informed decisions about model selection." Without statistical reliability indicators, these goals are not met. Rankings may flip with different random seeds.
- **Fix:** Run each experiment with at least 3 seeds; report mean+std; add pairwise significance tests (e.g., Diebold-Mariano) for key comparisons.

**Issue 3 (Severity: Major) — Unsupported causal claims weaken analytical credibility.**
- **Evidence:** Page 7 (few-shot analysis): "potentially because their smaller parameter sizes allow for faster fitting of simple time-series information"; Page 8 (architecture analysis): "current architectures do not fully reflect the 'scaling law'"; Page 9 (pretrain analysis): "LLM-based architecture may be well-suited for time series forecasting tasks."
- **Verification:** None of these claims are supported by controlled experiments. The "scaling law" claim is particularly problematic because a true scaling test requires varying parameters within a fixed architecture, which is not done.
- **Impact:** Causal overreach reduces the paper's scientific rigor and may mislead readers into treating correlational observations as established knowledge.
- **Fix:** Replace causal language with correlational observations; add controlled experiments where possible; explicitly call for further investigation where causality is uncertain.

**Issue 4 (Severity: Major) — No limitations section.**
- **Evidence:** The Conclusion (Page 10) omits any discussion of FoundTS's limitations.
- **Verification:** The paper has several inherent limitations: static dataset snapshot, best-lookback evaluation bias, single-seed runs, 5-hour timeout that penalizes some models, exclusion of certain important models (e.g., Lag-Llama).
- **Impact:** Omitting limitations gives an incomplete picture of the benchmark's reliability and scope. This may be viewed negatively by reviewers who expect transparent self-assessment.
- **Fix:** Add a dedicated Limitations paragraph acknowledging these constraints.

**Issue 5 (Severity: Minor) — Taxonomy inconsistency in model categorization.**
- **Evidence:** Page 5 (Section 3.2.1): TS pre-trained models are categorized as reconstruction, autoregressive, direct prediction, and hybrid.
- **Verification:** "Direct prediction" (TTM) and "Hybrid" (ROSE) categories overlap conceptually—TTM could also be considered a hybrid. The taxonomy mixes architectural (encoder/decoder) and objective (prediction/reconstruction) criteria inconsistently.
- **Impact:** Minor; does not affect results but reduces clarity and reusability of the classification.
- **Fix:** Use a two-axis taxonomy (architecture × training objective) for cleaner categorization.

## Actionable Suggestions
**Suggestion 1 (Must) — Change evaluation protocol from "best across lookbacks" to per-lookback or averaged reporting.**
- **What:** Modify the primary result tables (Tables 4-6) to report results for each lookback length separately, or use the mean across lookbacks as the ranking metric. Keep the "best" column as supplementary.
- **Why:** Ensures all models are compared under identical input conditions (fairness goal C2).
- **Where:** Page 6, Section 3.3.2, Tables 4-6, and Appendix D.

**Suggestion 2 (Must) — Add multi-seed experiments with variance reporting.**
- **What:** Rerun all experiments with at least 3 random seeds, report mean ± std, and add pairwise significance tests for key comparisons (e.g., best model vs runner-up per dataset).
- **Why:** Establishes statistical reliability for rankings and conclusions.
- **Where:** All result tables (4-6, 7, 11-16).

**Suggestion 3 (Must) — Add a Limitations section.**
- **What:** Insert a 3-5 sentence paragraph in the Conclusion acknowledging benchmark limitations.
- **Content:** Static dataset snapshot, best-lookback evaluation bias, single-seed design, 5-hour timeout constraints, and the need for community-maintained updates.
- **Where:** Page 10, Section 5 (Conclusion), before the final sentence.

**Suggestion 4 (Must) — Revise causal and unsupported analytical claims.**
- **What:** Rewrite the following:
  - Page 7 (few-shot, finding 4): Replace "smaller parameter sizes allow for faster fitting" with correlational language (e.g., "suggests a possible advantage, which warrants controlled investigation").
  - Page 8 (architecture, scaling law): Replace "do not fully reflect the 'scaling law'" with a more precise statement about architecture-dependence.
  - Page 9 (pretrain analysis): Acknowledge the TimesFM anomaly (pretraining hurts on Weather) and temper conclusions about LLM pre-training.
- **Why:** Maintains scientific rigor; avoids overclaiming.
- **Where:** Pages 7-9, Sections 4.1.2, 4.2.2, 4.2.4.

**Suggestion 5 (Must) — Add quantitative anchor to Abstract.**
- **What:** Insert one sentence summarizing the most important empirical finding, e.g., "Our evaluation reveals that TS pre-trained models outperform LLM-based models on 7/10 datasets in few-shot settings, while specific models retain advantages in full-shot settings on 4/7 datasets."
- **Why:** Makes the Abstract self-contained and informative, which is expected for an empirical benchmark paper.
- **Where:** Page 1, Abstract.

**Suggestion 6 (Nice-to-have) — Fix typos and informal language.**
- **What:** (a) Page 2 contribution list: "offer insights for us" → "offer insights for use" or "provide insights"; (b) Page 8: "not as smart as the specific models" → specific technical comparison of correlation handling mechanisms; (c) Page 3: "*thorugh*" → "*thorough*".
- **Where:** Pages 2, 3, 8.

**Suggestion 7 (Nice-to-have) — Sharpen the taxonomy of pre-trained models.**
- **What:** Use a two-axis classification (architecture type × pre-training objective) rather than the current four-category scheme, which has overlapping definitions.
- **Where:** Page 5, Section 3.2.1.

**Suggestion 8 (Nice-to-have) — Distinguish "Transition" and "Shifting" in data characteristics.**
- **What:** Rewrite the definitions to match their algorithmic computation (Appendix B), clarifying that Transition measures regularity of patterns while Shifting measures distributional change.
- **Where:** Page 4, Section 3.1(2), and Page 17-18, Appendix B.

## Storyline Options + Writing Outlines
The current storyline follows a standard "problem → gap → proposed solution → experiments → conclusions" structure, which is appropriate for a benchmark paper. However, the Abstract and Introduction can be tightened significantly.

### Abstract Outline (Complete)

**S1 (Problem/Domain):** "Time Series Forecasting (TSF) is critical in finance, weather, and energy, but foundation models for TSF lack standardized evaluation."

**S2 (Gap):** "Existing benchmarks either exclude LLM-based models, omit few-shot evaluation, or use inconsistent experimental setups that prevent fair comparison."

**S3 (Proposed Solution):** "We introduce FoundTS, a unified benchmark covering 11 foundation models (LLM-based and TS pre-trained) and 7 specific models across 14 datasets under standardized zero-shot, few-shot, and full-shot protocols."

**S4 (Key Result — NEW, currently missing):** "Our evaluation reveals that TS pre-trained models outperform LLM-based models on 7/10 datasets in few-shot settings, while specific models retain advantages in full-shot settings. No single model dominates across all data characteristics."

**S5 (Impact/Conclusion):** "FoundTS provides reproducible insights into foundation model strengths and limitations, guiding future TSF model design. Code and data are publicly available."

### Introduction Outline (Complete)

**P1 (Big Picture + Problem):** TSF importance → specific models dominate but generalize poorly → foundation models promise zero-shot generalization → BUT evaluation is fragmented.

**P2 (Prior Work Gap — revised):** Existing surveys [Liang, Jin] provide qualitative categorization but lack quantitative comparison. ProbTS covers only TS pre-trained models; TFB/BasicTS cover only specific models. No benchmark simultaneously evaluates LLM-based, TS pre-trained, AND specific models under unified protocols.

**P3 (Our Solution — FoundTS):** We propose FoundTS with three modules: (1) diverse datasets (10 domains, 7 statistical characteristics), (2) comprehensive model zoo (11 foundation + 7 specific models), (3) standardized evaluation pipeline (zero/few/full-shot, uniform settings).

**P4 (Contributions):** Explicitly list C1 (diversified models/datasets), C2 (fair evaluation pipeline), C3 (quantitative findings — with one specific result stated).

### Storyline Alternative

**Option A (Current — mostly effective):** Problem → Prior work gap → FoundTS architecture → Results → Analysis → Takeaways.
- *Strength:* Natural, easy to follow.
- *Weakness:* Abstract lacks results; Introduction gap statement too generic; contributions vague.

**Option B (Recommended — Results-first):** Start with a concrete finding (e.g., "No TSF foundation model consistently beats others—we need a standardized benchmark to find out why"), then introduce FoundTS as the tool, then present evidence.
- *Strength:* More engaging, immediately demonstrates value.
- *Weakness:* Requires restructuring the Abstract and first two Introduction paragraphs.

**Option C (Niche-focused):** Frame specifically around the finding that "scaling law does not hold," using FoundTS as the vehicle for this discovery.
- *Strength:* Novel angle.
- *Weakness:* The scaling law evidence is not strong enough to carry the paper's main narrative.

**Recommendation:** Keep the current structure (Option A) but strengthen the Abstract with a quantitative anchor, sharpen the Introduction gap statement with specific competitor limitations, and make the third contribution (C3) falsifiable by stating a concrete empirical finding.

## Priority Revision Plan
The following revision items are ordered by impact on paper quality, with P0 being publication-critical.

| Priority | Item | Issue Reference | Effort | Expected Impact |
|----------|------|----------------|--------|-----------------|
| **P0** | Change evaluation to per-lookback reporting (not best-only) | Issue 1, W1 | High | High — fixes fairness |
| **P0** | Add multi-seed variance and significance tests | Issue 2, W2 | High | High — enables reliable ranking |
| **P0** | Add Limitations section | Issue 4, W4 | Low | High — scientific completeness |
| **P0** | Revise causal claims (scaling law, small-model fitting) | Issue 3, W3 | Medium | High — rigor improvement |
| **P0** | Add quantitative result to Abstract | W5 | Low | Medium — self-contained abstract |
| **P1** | Discuss TimesFM anomaly in pretrain analysis (Table 7) | W6 | Low | Medium — fixes contradiction |
| **P1** | Fix typos and informal language ("smart", "for us") | W7, S6 | Low | Low — polish |
| **P2** | Sharpen model taxonomy to two-axis system | Issue 5 | Medium | Low — clarity improvement |
| **P2** | Distinguish Transition/Shifting definitions | Suggestion 8 | Low | Low — clarity improvement |

### Recommended Execution Order

```text
Phase 1 (Week 1): P0 items with low effort
  - Add Limitations section
  - Revise causal claims in analysis
  - Add quantitative anchor to Abstract
  - Fix typos and informal language

Phase 2 (Week 2-3): P0 items with medium-high effort
  - Rerun experiments with 3 seeds + variance reporting
  - Restructure evaluation protocol (per-lookback reporting)
  - Discuss TimesFM anomaly in pretrain analysis

Phase 3 (Week 4): P1-P2 items
  - Sharpen model taxonomy
  - Distinguish Transition/Shifting definitions
  - Final consistency check across all sections
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup (Data/Protocol/Baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Zero-shot evaluation of TS pre-trained models | 14 datasets, 6 TS pre-trained models, 4 prediction lengths | MSE, MAE (Tables 4, 11-12) | No single model dominates; TimesFM best overall | C3 | Only one seed; best-lookback reporting |
| E2 | Few-shot (5%) evaluation of all model types | 10 datasets, 7 TS pre-trained + 4 LLM-based + 7 specific models | MSE, MAE (Tables 5, 13-14) | TS pre-trained models lead on 7/10 datasets; Timer/ROSE excel | C3 | 5-hour timeout excludes some models; one seed |
| E3 | Full-shot evaluation | 6 datasets, 3 TS pre-trained + 2 LLM-based + 7 specific models | MSE, MAE (Tables 6, 15-16) | Specific models lead on 4/7 datasets; FM performance drops vs few-shot | C3 | Selection bias in FM subset |
| E4 | Channel independence vs dependence | 10 datasets, 2 foundation + 2 specific models | MSE (Figure 2) | Channel-dependent models better for high-correlation data | Analysis | Only 4 models compared |
| E5 | Architecture comparison | 7 TS pre-trained models, zero-shot | MSE vs params/data (Figure 3) | Scaling law does not hold across architectures | Analysis | Confounded by architecture differences |
| E6 | Performance across data characteristics | 7 characteristics, 7 models, 5% few-shot | MAE (Figure 4) | No single model excels across all characteristics | Analysis | One dataset per characteristic |
| E7 | Pretrain vs no pretrain | ETTh2, Weather; 10 models; 5% few-shot | MSE, MAE (Table 7) | TS pre-trained benefits from pretraining; LLM-based mixed | Analysis | Only 2 datasets; one seed |
| E8 | Model efficiency | ETTh2; all models; runtime + params + accuracy | Time, params, MSE (Figure 5) | ROSE/TTM best efficiency-accuracy tradeoff | Analysis | Few-shot FM vs full-shot specific (unfair) |

### Research-Theme Gap Diagnosis

- **New Knowledge (partial):** The paper generates several novel empirical findings (e.g., TS pre-trained > LLM-based in few-shot, scaling law does not hold across architectures). However, the lack of statistical testing means some findings may not be robust.
- **Reproducibility (partial):** Code and data are provided, but single-seed results mean exact reproduction may yield different rankings.
- **Impact on Practice/Understanding (good):** The finding that lightweight specific models (FITS, DLinear) compete with foundation models in few-shot settings has practical implications for practitioners. The channel-dependence analysis informs architectural design.

### Proposed Research Experiments (P0/P1/P2)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Quality Gain |
|--------|-------------|------------|----------------|---------------------|---------|-------------------|-----------|-------------|
| **P0-R1** | Ranking stability (W2) | Current rankings are stable across seeds | Rerun Tables 4-6 with 3 seeds | Same settings, different seeds | Mean±std MSE; rank consistency | Top-3 ranking stable across ≥2/3 seeds | 3× current compute | High — validates all conclusions |
| **P0-R2** | Lookback sensitivity (W1) | Best-lookback reporting inflates apparent performance | Report per-lookback results for all models on 3 diverse datasets | All models, all lookbacks | MSE per lookback; rank changes | ≥1 rank change when lookback is fixed | 1× current compute (already run) | High — fixes fairness |
| **P1-R3** | Causal test: small model advantage (W3) | Small model advantage is driven by architecture, not size | Compare FITS at 2×, 4× parameter sizes | Same architecture, varying width | Few-shot MSE vs params | Effect of size on performance quantified | Medium | Medium — resolves causal question |
| **P1-R4** | Pretrain anomaly (W6) | TimesFM pretraining hurts on Weather due to domain mismatch | Analyze pre-training data overlap with Weather domain | TimesFM, Timer, ROSE | MSE per domain; data overlap score | Identify specific domain conflict | Low | Medium — improves pretrain analysis |
| **P2-R5** | Scalability test | Controlled scaling within single architecture | Vary TimesFM/Timer sizes systematically (0.5×, 1×, 2× params) | Fixed architecture, varying width+ depth | MSE vs params (log-log) | Power-law trend observed | Medium-High | Medium — strengthens scaling law analysis |

### ASCII Diagram — Experiment Upgrade Plan

```text
[E1-E8 Current Experiments]
      │
      ├── P0-R1 (Multi-seed) ──────► Validates all rankings
      ├── P0-R2 (Per-lookback) ────► Fixes fairness design
      │
      ├── P1-R3 (Size control) ────► Resolves causal claim
      └── P1-R4 (Domain analysis) ──► Explains pretrain anomaly
      
      └── P2-R5 (Scaling study) ───► Strengthens architecture analysis
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

The paper addresses a timely and important problem—standardized benchmarking of foundation models for time series forecasting—and provides the most comprehensive model coverage among existing efforts. The multi-strategy evaluation design and the analysis of model characteristics are valuable contributions. However, the score is constrained by: (1) a methodological flaw in the evaluation protocol (best-per-lookback reporting) that undermines the paper's core fairness claim; (2) absence of statistical testing, which makes reported rankings potentially unreliable; (3) unsupported causal claims that reduce analytical rigor; and (4) missing limitations and vague contribution statements. These issues are fixable with moderate-to-high effort.

**Post-Revision Target: [7.5, 8.5]/10**

If the authors address the P0 items—particularly adopting a per-lookback or averaged evaluation protocol, adding multi-seed variance reporting, revising causal claims, adding a limitations section, and sharpening the Abstract—the paper could achieve a significantly higher score. The core benchmarking infrastructure is solid; the main gap is in experimental rigor and presentation discipline rather than in the underlying research contribution.