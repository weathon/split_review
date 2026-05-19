## Summary
# Final Review Report

## Summary

This paper introduces **Model Manager**, a framework that uses Large Language Models (LLMs) to generate natural-language "verbalizations" describing the differences between pairs of machine learning models trained on the same dataset. The approach works by serializing input features and model predictions into JSON, passing them to an LLM via a zero-shot prompt, and asking the LLM to describe where and how the two models' decision boundaries diverge. The authors propose a quantitative evaluation protocol where a second LLM uses the verbalization to reconstruct model-2 outputs from model-1 outputs, measuring accuracy via three metrics: mismatch accuracy (Acc_mismatch), match accuracy (Acc_match), and overall accuracy (Acc_overall). Experiments test three LLMs (Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro) across three model types (Logistic Regression, Decision Trees, KNN) on three small tabular datasets (Blood, Diabetes, Car), with ablation studies on including model internals and omitting model-type information.

**Core contributions claimed by the authors:**
- **C1**: A framework using LLMs to verbalize differences between ML models via input-output sample comparison (zero-shot prompting).
- **C2**: A novel evaluation protocol quantifying verbalization informativeness through LLM-based output reconstruction (Acc_mismatch/Acc_match/Acc_overall).
- **C3**: Empirical findings showing that (a) the framework works well for parametric models (LR, DT) but struggles with instance-based models (KNN), (b) providing model internals helps for DTs but not KNNs, and (c) removing model-type information has negligible effect.

**Overall assessment:** The paper tackles an interesting and timely problem—automated model comparison for transparency. The evaluation protocol is a creative methodological contribution. However, the work has significant limitations in external validity (small datasets, simple models, artificial model-pair generation), methodological rigor (LLM-as-verbalizer-and-evaluator confound, missing sampling details), and evidence quality (selective reporting, overclaiming). The strongest result (LR on Blood: ~80% accuracy) is narrow; broader claims are not supported. With major revisions to scope claims, add controls, and improve experimental rigor, this could become a useful contribution to XAI/model management.

## Strengths
1. **Timely and relevant problem framing.** The "model lake" problem—proliferation of poorly documented models—is a real challenge in practical ML deployment. Automated tools for model comparison could have significant impact on model selection, auditing, and transparency. The authors correctly identify a gap between tools that document individual models and tools that systematically compare them.

2. **Creative evaluation protocol.** Using LLM-based output reconstruction (predicting model-2 outputs from model-1 outputs + verbalization) as a proxy for verbalization quality is a clever idea that provides an automatic, quantitative metric. The decomposition into Acc_mismatch and Acc_match separately captures detection of real differences vs. avoidance of false differences, which is more informative than a single accuracy number.

3. **Systematic ablation studies.** The paper studies two important design decisions—providing model internals and including/excluding model-type information—across multiple model types and datasets. The finding that providing decision tree structures vastly improves performance (e.g., GPT-4o Acc_overall jumps to 0.966) while providing KNN parameters slightly hurts is a non-obvious result that reveals meaningful differences in how LLMs process model information.

4. **Multi-LLM comparison.** Testing three state-of-the-art LLMs (Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro) reveals substantial performance variation, with Claude generally outperforming the others. This provides useful guidance for practitioners considering LLM-based XAI approaches.

5. **Reproducibility effort.** The paper provides detailed prompt templates (Box 1, Appendix B) and full result tables (Tables 4-6), which are valuable for replication and extension by other researchers.

## Weaknesses
1. **Limited external validity (MAJOR).** Experiments are restricted to three small tabular datasets (Blood: 784 rows, Diabetes: 768 rows, Car: 1,728 rows) and three simple model types (LR, DT, KNN). The framework's applicability to larger datasets, higher-dimensional feature spaces, or modern models (neural networks, gradient boosting, ensembles) is untested. Claims of "flexibility" and "extensibility" are not supported by the evidence.

2. **Artificial model-pair generation (MAJOR).** Model pairs are created by injecting Gaussian noise into coefficients/hyperparameters rather than by training independent models. This produces potentially unrealistic patterns that LLMs may exploit. The paper does not compare against naturally varying model pairs, making it unclear whether reported accuracies reflect genuine verbalization ability or detection of injected noise patterns.

3. **LLM-as-verbalizer-and-evaluator confound (MAJOR).** Using the same LLM family for both LLMverb and LLMeval creates a circularity risk: the evaluator may benefit from familiarity with the verbalizer's phrasing style rather than purely from verbalization informativeness. No cross-model evaluation is conducted to bound this effect.

4. **Selective reporting and overclaiming (MAJOR).** The main results (Figure 2) selectively show Blood and Car datasets while omitting Diabetes, where performance is substantially lower. For example, DT Acc_mismatch on Diabetes is only 0.551 for Claude, yet the narrative claims "strong performance" and "LLMs are generally able to verbalize the difference between DTs effectively." The abstract's "up to 80% accuracy" cherry-picks the best single condition.

5. **Missing sampling and split details (MAJOR).** The representative sample (verb split) selection method is not described: is it random, stratified, or deterministic? How many samples exactly? What random seed? Without this information, the experimental setup cannot be precisely reproduced.

6. **No statistical significance testing.** Error bars (±values) are reported but never defined (standard deviation? standard error? confidence intervals?). Differences between LLMs are described qualitatively ("competitive," "lags behind") without significance tests. Given that many reported differences are within overlapping error margins, the conclusions about LLM ranking may not be statistically robust.

7. **Weak related-work positioning.** The related work section is organized as isolated mini-surveys per topic rather than as a comparative analysis. The closest prior work (Kroeger et al., 2023 on LLM-based model explanation; Singh et al., 2023 on text module explanations) is discussed but not systematically compared on dimensions like task scope, required model access, or evaluation approach.

8. **Overly optimistic discussion and conclusion.** The Discussion speculates about extending to DNNs without any supporting evidence. The Conclusion uses hyperbolic language ("foundational step," "excels," "more transparent, accountable, and effective AI systems") that is disproportionate to the demonstrated scope.

## Key Issues
### Issue 1: Artificial noise injection undermines external validity of all experimental results
**Severity: Critical | Page 6 - Model generation paragraph**

The core experimental methodology creates model pairs by injecting Gaussian noise into model parameters (coefficients for LR, split thresholds for DT). This produces differences that may be more structured and detectable than naturally occurring model variations. The paper treats this as if it merely generates "diverse" model pairs, but the noise injection fundamentally changes what the LLM is being asked to detect: it may be identifying a specific noise signature rather than genuine model-behavior differences. Without a control experiment using independently trained model pairs, the entire accuracy evaluation is at risk of being an artifact of the generation procedure.

**Required action:** Add a supplementary experiment with naturally varying model pairs (different seeds, hyperparameters, training subsets) and compare performance.

---

### Issue 2: LLM self-evaluation confound threatens metric validity
**Severity: Critical | Page 5 - Evaluation section, Page 6 - Evaluator paragraph**

Using the same LLM family as both verbalizer and evaluator creates a confound where the evaluator may be familiar with the verbalizer's phrasing patterns, allowing it to predict model-2 outputs from style cues rather than verbalization content. The paper's justification ("to avoid bias introduced when LLMs process outputs of other language models") addresses a different concern (cross-model processing bias) but does not address the self-consistency confound. Without at least a cross-model evaluation experiment, the Acc_mismatch and Acc_match numbers cannot be interpreted as pure measures of verbalization informativeness.

**Required action:** (1) Add a cross-model evaluation condition (e.g., GPT-4o verbalizer with Claude evaluator). (2) Add a no-verbalization baseline where the evaluator predicts model-2 outputs from the sample alone. (3) Discuss the confound explicitly.

---

### Issue 3: Selective reporting inflates perceived performance
**Severity: Major | Pages 7-8 - Results sections**

The main results narrative emphasizes Blood and Car datasets while omitting Diabetes from the primary discussion and figures. When Diabetes is examined (Table 4-6), performance drops substantially: e.g., LR Acc_mismatch on Diabetes for Claude is 0.522 at Level 1 and 0.610 at Level 2—much lower than the Blood dataset numbers that dominate the narrative. The abstract's "up to 80% accuracy" is the single best-case condition (LR on Blood, Level 2-3). This selective presentation makes the framework appear more capable than the full evidence supports.

**Required action:** Include all datasets in main figures. Report average performance across all settings alongside best-case numbers. Bound abstract claims to the conditions tested.

---

### Issue 4: Missing experimental design details hinder reproducibility
**Severity: Major | Page 3 - Representative Sample, Page 5 - Datasets**

Critical experimental details are absent: (a) How the verb/eval split is sampled (random? stratified? seed?), (b) exact n_verb size per dataset, (c) definition of error bars (±values), (d) number of model pairs per condition, (e) whether multiple random splits were used. Without these, the experiments cannot be independently reproduced or verified.

**Required action:** Add a detailed experimental design subsection specifying all sampling procedures, error bar definitions, and replication counts.

---

### Issue 5: Overclaiming in abstract, discussion, and conclusion
**Severity: Major | Pages 1, 10 - Abstract, Discussion, Conclusion**

The paper uses language that systematically exceeds the evidence: "pronounced results," "effectively verbalizes," "foundational step," "excels in identifying differences." Given the limited scope (three small tabular datasets, three simple model types, artificial model pairs), these claims are disproportionate. For instance, the conclusion claims "excels in identifying differences between parametric models," but the average Acc_mismatch across all LR conditions is approximately 0.65-0.75, leaving substantial room for improvement.

**Required action:** Replace hyperbolic language with evidence-bounded wording. Scope all claims to the actual experimental conditions.

## Actionable Suggestions
### S1: Revise abstract to be evidence-bounded (Must)
Replace the current abstract with a compact 4-5 sentence version that clearly bounds claims:
- State the problem (model lake, difficult model comparison).
- State the gap (existing tools document individual models but do not compare them).
- State the proposed method (LLM-based verbalization of model differences via input-output sampling).
- State the key result with scope: e.g., "On pairs of logistic regression models with 20-25% output divergence, the best-performing LLM (Claude 3.5 Sonnet) achieves up to 83% mismatch accuracy on a simple binary classification dataset; performance decreases for non-linear models and multi-class settings."
- State significance with measured caution: "These results suggest LLM-based model comparison is a promising direction, though broader validation is needed."

### S2: Add control experiments for evaluation protocol (Must)
- **S2a: Cross-model evaluation.** Add an experiment where LLMverb = GPT-4o and LLMeval = Claude (and vice versa). Report Acc_mismatch and Acc_match. If results are similar, the confound concern is alleviated. If results drop, this indicates a genuine confound that must be discussed.
- **S2b: No-verbalization baseline.** Add a baseline where LLMeval receives only the evaluation sample (X_eval, y_1) without any verbalization, and must predict y_2 from the sample alone. This measures how much of the accuracy comes from the verbalization versus from other information in the sample.

### S3: Add naturally varying model pairs (Must)
Create a supplementary experiment with 30-50 model pairs trained independently (different random seeds, hyperparameter configurations) rather than by noise injection. Compare LLM performance on these natural pairs vs. noise-injected pairs. If performance is significantly lower on natural pairs, this indicates that the main results are inflated by the noise-injection procedure.

### S4: Disclose all experimental design details (Must)
Add a reproducibility subsection specifying:
- Sampling method for verb/eval split (e.g., stratified random sampling with seed=42).
- Exact sample sizes per dataset.
- Error bar definition (e.g., ±1 standard error across N model pairs).
- Number of model pairs generated per condition.
- Multiple split replication (if not done, add a note stating the limitation).

### S5: Include all datasets in main results (Must)
Add Diabetes results to Figure 2 or create a comprehensive table in the main text. The current practice of showing only Blood and Car in the figure and mentioning Diabetes only in text creates an incomplete picture.

### S6: Restructure Related Work as comparative analysis (Nice-to-have)
Reorganize into 3-4 categories with explicit comparison axes: (a) scope: single-model vs. cross-model, (b) required model access: black-box vs. internal, (c) output type: explanation vs. documentation vs. comparison. End with a synthesis paragraph stating how Model Manager differs from the closest approaches.

### S7: Tone down Discussion and Conclusion (Must)
Replace speculation about DNNs with concrete next steps based on current results. Remove hyperbolic phrasing ("foundational step," "excels"). The conclusion should be a concise summary of validated findings, bounded limitations, and specific future work items.

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current storyline follows this sequence: (1) Model lake problem + prior documentation tools → (2) LLMs as explainers → (3) Model Manager design → (4) Evaluation protocol → (5) Experiments → (6) Ablations → (7) Discussion → (8) Conclusion.

**Problems with current storyline:**
- The introduction does not establish a clear, specific research question until the end.
- The gap ("existing tools don't verbalize differences") is asserted but not demonstrated with a concrete failing example.
- The contribution statements (bullet points) are listed too late and read as findings rather than claims.
- There is tension between framing as a "model management" paper and an "XAI/explainability" paper.

### Proposed Revised Storyline: "LLM-as-Comparator"

**Abstract Outline (4-5 sentences):**
- S1 (Problem): "The proliferation of machine learning models has created a 'model lake' where selecting between similar models is difficult due to lack of systematic comparison tools."
- S2 (Prior gap): "Existing tools document individual models but do not verbalize how or where their predictions differ."
- S3 (Method): "We introduce Model Manager, which uses a large language model to analyze input-output samples from two models and produce natural-language descriptions of their decision-boundary differences."
- S4 (Key result, bounded): "On pairs of logistic regression models with controlled output divergence, the best LLM achieves 83% mismatch accuracy on simple binary data, though performance degrades for non-linear models and complex datasets."
- S5 (Significance): "These results establish a proof-of-concept for LLM-based model comparison and identify clear directions for improvement."

**Introduction Outline (5 paragraphs):**

- **P1 (Stakes and problem):** Open with a concrete scenario: a practitioner choosing between two models for a medical diagnosis task. Despite similar accuracy, the models may have different failure modes. Current tools (Model Cards, ModelDB) provide individual documentation but no comparative analysis. The gap: systematic model comparison is missing. *Transition: "We address this gap by proposing an LLM-based framework that compares models through their input-output behavior."*

- **P2 (LLM opportunity):** LLMs have shown ability to analyze structured data and explain model behavior. Recent work [Kroeger et al., 2023; Singh et al., 2023] demonstrates LLMs can produce post-hoc explanations. This suggests an untapped capability: comparative reasoning across models. *Transition: "We test this hypothesis with the Model Manager framework."*

- **P3 (Our approach, high-level):** Model Manager takes input-output samples from two models, serializes them, and prompts an LLM to verbalize where and how the decision boundaries diverge. Key design choices: zero-shot prompting (no in-context examples needed), JSON serialization (structured format), optional model-internals inclusion. *Transition: "Evaluating such verbalizations requires a quantitative metric."*

- **P4 (Evaluation protocol):** We propose a reconstruction-based metric: an LLM evaluator uses the verbalization to predict one model's outputs from the other's. Three sub-metrics (Acc_mismatch, Acc_match, Acc_overall) separate detection of real differences from introduction of false ones. *Transition: "We test this framework across models, datasets, and LLMs."*

- **P5 (Contributions, scoped):** (1) A zero-shot framework using LLMs for cross-model verbalization. (2) A quantitative evaluation protocol for verbalization quality. (3) Empirical results showing the approach works for parametric models under limited conditions, with clear failure modes for instance-based learning. We discuss limitations and necessary extensions.

### Alternative Storyline Candidate: "Protocol-First"
Lead with the evaluation protocol as the primary contribution and the Model Manager as a case study. Structure: Evaluation problem → Proposed reconstruction metric → Theoretical properties → Model Manager as one implementation → Experiments validating the metric → Findings about model types. This would position the paper as a measurement contribution rather than a model-management one, which may be more defensible.

### Recommended Storyline
The **"LLM-as-Comparator"** storyline is recommended because it aligns with the paper's actual evidence and positions the contribution more precisely. The current "Model Manager" framing implies a more comprehensive tool than what is demonstrated.

## Priority Revision Plan
### P0 (Critical — must address for publication)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P0.1 | Artificial model-pair generation threatens validity | Add naturally varying model pairs (30-50 pairs) as control experiment | Medium (1-2 weeks) | High — determines whether core results are valid |
| P0.2 | LLM self-evaluation confound | Add cross-model evaluation (GPT-4o↔Claude) and no-verbalization baseline | Low (few API calls) | High — affects interpretation of all accuracy metrics |
| P0.3 | Selective reporting | Include Diabetes in all main figures; report average performance across all settings | Low (re-plotting) | High — affects perceived framework capability |
| P0.4 | Missing experimental details | Add reproducibility subsection with sampling, seeds, error-bar definitions, exact sizes | Low (write-up) | High — necessary for scientific validity |

### P1 (Major — strongly recommended)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P1.1 | Overclaiming in abstract/conclusion | Rewrite to bound claims to tested conditions | Low | Medium — improves objectivity |
| P1.2 | Statistical significance | Add significance tests (e.g., paired bootstrap) for LLM comparisons | Medium | Medium — strengthens comparisons |
| P1.3 | Related work positioning | Restructure as comparative analysis with synthesis paragraph | Medium | Medium — clarifies novelty |
| P1.4 | Discussion speculation | Replace DNN speculation with concrete next steps based on current results | Low | Medium — avoids overreach |

### P2 (Nice-to-have — quality improvement)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P2.1 | Storyline clarity | Restructure introduction per recommended outline | Medium | Medium — improves readability |
| P2.2 | Further model types | Add one more model type (e.g., Random Forest, linear SVM) | Medium | Medium — broadens scope |
| P2.3 | Larger datasets | Add one larger dataset (e.g., 10K+ rows) to test scalability | High | Medium — tests practical utility |
| P2.4 | Human evaluation | Add small-scale human evaluation of verbalization quality | High | High — strengthens qualitative claims |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup (Data/Models) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|--------------------|---------|--------------|-----------------|-------------------|
| E1 | LR verbalization performance (Blood/Car) | LR models, Blood/Car datasets, Level 1-3 | Acc_mismatch, Acc_match, Acc_overall | Claude best: Acc_mismatch 0.831 (Blood), 0.605 (Car) | C1, C3 | Only 2 of 3 datasets shown in main figure; Diabetes omitted |
| E2 | DT verbalization performance | DT models, all datasets, Level 1-3 | Same as E1 | Claude best: 0.700 (Blood), 0.700 (Car); lower on Diabetes (0.551) | C1, C3 | Diabetes under-reported in narrative |
| E3 | KNN verbalization performance | KNN models, all datasets, Level 1-3 | Same as E1 | Poor: Claude Acc_mismatch 0.686 (Blood), 0.490 (Car), 0.603 (Diabetes) | C3 (limitation) | Confirms expected weakness |
| E4 | Ablation: model internals (LR) | LR, Level 2, all datasets, all LLMs | Same | Marginal 3-5% improvement | C3 | Gains minimal; not statistically tested |
| E5 | Ablation: model internals (DT) | DT, Level 2, all datasets, all LLMs | Same | Major improvement: GPT-4o 23.8% relative gain (Blood) | C3 | Percentage increase format ambiguous |
| E6 | Ablation: model internals (KNN) | KNN, Level 2, all datasets, all LLMs | Same | Minimal/negative effect | C3 | Consistent with hypothesis |
| E7 | Ablation: exclude model-type | All models, Level 2, all datasets, all LLMs | Same | No significant effect (within error margin) | C3 | Only tested at Level 2 |

### Research-Theme Gap Diagnosis

1. **New knowledge gap:** The paper's primary knowledge contribution is establishing that LLMs can perform cross-model verbalization on simple tabular models. However, this finding is undermined by the artificial model-pair generation method—if the LLM is simply detecting a noise signature, then the "knowledge" is about LLMs' noise-detection ability rather than model-comparison ability.

2. **Reproducibility gap:** Missing experimental details (sampling procedure, error-bar definition, exact sample sizes, replication counts) prevent independent reproduction.

3. **Impact-on-practice gap:** The paper claims practical value for model selection and transparency, but the tested conditions (3 small datasets, simple models, artificial pairs) are far from real deployment scenarios. No demonstration of how the verbalizations would help a practitioner make a real decision.

### Proposed Research Experiments

**E8 (P0) — Natural model-pair control**
- Target Claim: C1 (framework works for LR/DT pairs)
- Hypothesis: Performance on naturally varying model pairs is lower than on noise-injected pairs
- Minimal Design: Train 50 LR pairs independently (different seeds + hyperparameters), 50 DT pairs similarly
- Controls/Baselines: Compare against matched noise-injected pairs (same disagreement levels)
- Metrics: Acc_mismatch, Acc_match, Acc_overall; paired difference test between noise and natural conditions
- Success Criterion: If gap ≤ 5% (absolute), noise injection is a valid proxy; if >10%, main results are compromised
- Cost: Low (training simple models + API calls)
- Expected Gain: Determines whether core experimental methodology is valid

**E9 (P0) — Cross-model evaluation**
- Target Claim: C2 (evaluation protocol validity)
- Hypothesis: Accuracies are similar when verbalizer and evaluator are different model families
- Minimal Design: 4 conditions: GPT-4o→Claude, Claude→GPT-4o, GPT-4o→Gemini, Claude→Gemini
- Controls/Baselines: Same-model condition as current (reference)
- Metrics: Acc_mismatch, Acc_match per condition
- Success Criterion: If cross-model accuracy > 90% of same-model accuracy, confound is limited
- Cost: Low (limited API calls)
- Expected Gain: Validates or invalidates the evaluation metric

**E10 (P1) — Dataset scalability check**
- Target Claim: C1 (framework can be used with various datasets)
- Hypothesis: Performance degrades with larger feature spaces and more rows
- Minimal Design: Add one dataset with 10+ features and 5K+ rows (e.g., Adult Income)
- Controls/Baselines: Compare per-dimension and per-class-size against current datasets
- Metrics: Same as E1; also measure verbalization length and prompt token count
- Success Criterion: Acc_mismatch > 0.5 for LR on new dataset
- Cost: Medium (data prep + model training + API calls)
- Expected Gain: Tests practical scalability claim

**E11 (P1) — Statistical significance analysis**
- Target Claim: C3 (LLM ranking differences)
- Hypothesis: Some inter-LLM differences are not statistically significant
- Minimal Design: Bootstrap resampling of model pairs within each condition, compute 95% CI for pairwise differences
- Controls/Baselines: N/A
- Metrics: p-values for Claude vs. GPT-4o, Claude vs. Gemini, GPT-4o vs. Gemini
- Success Criterion: Report which comparisons are significant at α=0.05
- Cost: Low (computational only)
- Expected Gain: Strengthens or qualifies cross-LLM comparisons

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 5.0 / 10

**Rationale:** The paper addresses a relevant problem and introduces a creative evaluation protocol. However, the experimental methodology has critical validity concerns (artificial model-pair generation, LLM self-evaluation confound), the evidence is selectively reported, and the claims systematically exceed the demonstrated scope. The research value is limited by the narrow experimental conditions (small tabular datasets, simple models) and the absence of key controls. Novelty is moderate—the combination of LLM-based cross-model verbalization and reconstruction-based evaluation is new, but the individual components (LLM for explanation, zero-shot prompting, behavioral comparison) are established techniques.

### Post-Revision Target: [6.0, 7.0] / 10

**Rationale:** If the authors address the P0 issues (natural model-pair control, cross-model evaluation, complete reporting, reproducibility details) and substantially tone down claims, the paper could reach 6.0-7.0. The upper bound reflects that even with perfect execution, the scope (simple models, tabular data) is inherently limited. The evaluation protocol remains the strongest contribution; repositioning the paper around this measurement contribution rather than a comprehensive "model management" framework would produce a more defensible submission.