## Summary
# Final Review Report

## Summary

This paper presents ChEF (Comprehensive Evaluation Framework), a modular framework for standardized and holistic evaluation of Multimodal Large Language Models (MLLMs). ChEF decomposes evaluation into four components — Scenario (datasets), Instruction (queries and in-context examples), Inferencer (PPL, CoT, Multi-Turn strategies), and Metric (task-specific scores) — that can be composed into Recipes. The authors further define six "desiderata" recipes (calibration, in-context learning, instruction following, language performance, hallucination, robustness) to profile MLLM capabilities beyond visual perception. Nine MLLMs are evaluated across nine scenarios.

**Core Strengths:** The modular design is well-motivated and addresses a genuine community need for standardized, extensible MLLM evaluation. The stability analysis (Section 3.4) convincingly shows that PPL-based Inferencers reduce query-induced variance compared to free-form direct output. The desiderata dimensions cover important capabilities often ignored in perception-only benchmarks.

**Major Weaknesses:** (1) The RIAM and RRM metrics (Eq. 1, Eq. 2) have mathematical validity issues when model accuracy equals or falls below random guessing (which occurs for several models in Table 1). (2) The detection evaluation protocol converts open-vocabulary detection into a narrow multi-choice task using ground-truth-derived answer pools, limiting its validity for measuring detection capability. (3) The Pearson correlation analysis (Section 3.5) is performed on only N=9 models, making statistical conclusions unreliable without p-values or confidence intervals. (4) The calibration finding (Section 3.3) risks trivial interpretation — low ECE with low accuracy may reflect uniform underconfidence rather than meaningful uncertainty. (5) Reproducibility is undermined by missing model version specifications, inference hyperparameters, and corruption severity levels.

**Retrieval Status:** External literature verification was unavailable in this run (Retrieval-Disabled Mode). Novelty and comparison claims (e.g., "first to incorporate ICL into evaluation framework") are deferred for manual verification.

## Strengths
**S1. Modular and extensible design.** ChEF's four-component decomposition (Scenario, Instruction, Inferencer, Metric) is well-conceived and addresses the real problem of fragmented MLLM evaluation. The Recipe abstraction allows any existing benchmark to be expressed within ChEF, making the framework both backward-compatible and future-extensible. This is a genuine contribution to evaluation methodology.

**S2. Stability analysis of evaluation protocols.** Section 3.4 provides strong empirical evidence that PPL-based Inferencers reduce query-induced variance compared to direct free-form output. This finding is practically important — it shows that much of the reported variance across MLLM benchmarks may come from evaluation protocol choices rather than model capability differences. The boxplot comparison across Inferencer types (Direct vs PPL vs CoT vs Multi-Turn) is convincing and actionable for the community.

**S3. Broad coverage of models and tasks.** Evaluating 9 MLLMs across 9 scenarios and 6 desiderata is a substantial empirical effort. The inclusion of both generative and discriminative task types, single-task and multi-task benchmarks, and six capability dimensions beyond perception makes this one of the more comprehensive MLLM evaluations in the literature.

**S4. Valuable cross-dimensional insights.** The correlation analysis between desiderata and visual performance (Section 3.5), despite its sample size limitation, generates interesting and plausible hypotheses — particularly the finding that hallucination correlates strongly with MMBench performance and that choice distribution biases affect discriminative evaluation. These insights can guide future benchmark design.

**S5. Transparency about limitations.** The Conclusion admits several honest limitations: limited scenario coverage (safety, bias not included), residual query variance, and undetermined GPT evaluation effectiveness. This candor is commendable and helps readers calibrate their confidence in the findings.

## Weaknesses
**W1. Mathematical validity of RIAM and RRM metrics.** (Page 5-6, Desiderata section) Both the Relative ICL Accuracy for Multi-Choice (RIAM, Eq. 1) and Relative Robustness for Multi-Choice (RRM, Eq. 2) use denominators (acc0-shot − accrand) and (acc − accrand) that can be zero or negative. For Kosmos-2 on MMBench, acc=25.60 vs accrand=27.57 — the denominator is negative, inverting the metric's interpretation. This is not an edge case: several models in Table 1 perform near or below random on multiple scenarios. The metrics require a bounded formulation or explicit handling of the degenerate case.

**W2. Detection evaluation validity.** (Page 4, Section 2.2) The VOC2012 detection protocol converts object detection into multi-choice QA using answer pools generated by "random scaling and translating the ground-truth bounding boxes." This means: (a) the model only chooses among near-GT candidates, not open-vocabulary proposals; (b) false positives (detecting non-existent objects) are not penalized; (c) the task reduces to fine-grained localization discrimination, not detection. The reported "detection performance" numbers should be interpreted with this strong caveat.

**W3. Statistical reliability of correlation analysis.** (Page 8-9, Section 3.5) Pearson correlations are computed on N=9 data points (one per MLLM). With N=9, the 95% confidence interval for r=0.7 spans approximately [0.1, 0.93], meaning most reported correlations are not statistically distinguishable from weak or moderate associations. No p-values, confidence intervals, or effect-size measures are reported. The claim that "hallucination is strongly correlated with MMBench performance" is plausible but not statistically established.

**W4. Calibration interpretation confound.** (Page 7, Section 3.3) The paper states "Most MLLMs exhibit good calibration" and attributes this to "relatively low accuracy...and lack of confidence." This describes a trivial calibration scenario: a model that is always underconfident will achieve low ECE but provides no useful per-instance uncertainty. The paper should distinguish between calibration (aggregate confidence-accuracy alignment) and sharpness/discrimination (confidence varies with task difficulty). Without this distinction, readers may overinterpret "good calibration" as meaningful uncertainty quantification.

**W5. Missing reproducibility specifications.** (Page 6, Section 3.1) Several critical experimental details are absent: exact model versions/checkpoints used (e.g., LLaVA-7B vs 13B), inference temperature/top-p/max-tokens, number of PPL candidate answers per task, ICE retrieval randomness handling (was it averaged over multiple seeds?), and corruption severity levels for robustness evaluation. These omissions prevent independent reproduction.

**W6. Unsupported novelty claims.** (Page 2, Introduction) The claim "we are the first to incorporate ICL into the evaluation framework" lacks the scoping needed for verifiability. ICL evaluation exists in LLM frameworks like HELM, and few-shot evaluation is common in VLM literature. Without explicit boundary conditions (e.g., multimodal ICE with image retrieval across diverse visual tasks), this claim is vulnerable to challenge. External verification is deferred (Retrieval-Disabled Mode).

**W7. GPT-based evaluation reliability.** (Page 6, Section 2.3/Desiderata) Language performance evaluation uses GPT-4 to score CoT outputs. While the paper acknowledges "flickering" and averages multiple rounds, GPT-based evaluation has known position bias, verbosity bias, and sensitivity to prompt wording. No human correlation study or calibration check specific to this task is reported. The claim that "GPT-based metrics have shown to be well correlated with human evaluation" cites prior work but does not establish that the correlation holds for this specific use case (evaluating CoT reasoning quality for MLLMs on science questions).

**W8. Missing statistical significance in main results.** (Page 7, Table 1) All results in Table 1 are reported as point estimates without variance (no standard deviation, no confidence intervals, no multi-seed runs). Given the known high variance of LLM outputs across decoding configurations, single-run evaluation makes it impossible to assess whether observed differences between models are meaningful or due to random variation. This is especially critical when differences are small (e.g., InstructBLIP 84.27 vs LLaVA 89.40 on CIFAR — a 5-point gap where the weaker model reportedly outperforms the stronger).

## Key Issues
**Issue 1 (Critical): RIAM/RRM denominator can produce undefined or inverted values.** Equations (1) and (2) use denominators (acc0-shot − accrand) and (acc − accrand) that are zero or negative when model accuracy ≤ random baseline. This occurs for Kosmos-2 on MMBench (25.60 vs 27.57 random) and other near-random entries in Table 1. This invalidates the metric values for those model-scenario pairs and distorts any aggregate ICL or robustness ranking that uses them. *Fix:* Replace with a bounded formulation: RIAM' = (accICL − acc0-shot) / (max(acc0-shot, 1−1/n) − acc0-shot), with a floor to avoid division by zero.

**Issue 2 (Major): Detection evaluation does not measure open-vocabulary detection.** The VOC2012 Recipe transforms detection into multi-choice QA with answer pools derived from ground-truth boxes. This design: (a) only tests the model's ability to discriminate among near-GT proposals, (b) does not penalize false positive detections, and (c) cannot measure recall. Consequently, the high VOC scores from Shikra (55.23) and Kosmos-2 (54.55) may reflect learned localization priors rather than genuine detection competence. *Fix:* Add distractor boxes from other objects in the same image, and report precision/recall in addition to multi-choice accuracy.

**Issue 3 (Major): Correlation analysis lacks statistical grounding.** Figure 7(a) reports Pearson correlations on only N=9 data points. No p-values, confidence intervals, or bootstrap estimates are provided. The claim of "strong correlation" between hallucination and visual performance cannot be reliably distinguished from noise with this sample size. *Fix:* Report p-values, add 95% CIs via Fisher z-transform or bootstrapping, and discuss the small-N limitation explicitly.

**Issue 4 (Major): Reproducibility-critical details missing.** The paper does not specify model checkpoint versions, inference hyperparameters (temperature, top-p, max tokens), PPL answer pool sizes, ICE random seed handling, or corruption severity levels. Without these, independent reproduction is not possible. *Fix:* Add an appendix table with all experimental configurations.

**Issue 5 (Major): Calibration finding conflates "low ECE" with "good uncertainty."** Low ECE can arise from trivial uniform underconfidence when accuracy is low, which provides no meaningful per-instance uncertainty signal. The paper's interpretation ("most MLLMs exhibit good calibration") may mislead readers. *Fix:* Add sharpness metrics (e.g., Brier score decomposition, average confidence) and discuss the calibration-sharpness tradeoff.

**Issue 6 (Major): Three key findings in Introduction lack evidence anchors.** Page 3 lists three findings abstractly ("significant tug-of-war," "struggling with ICL," "strong correlation") without a single supporting number. This undermines reader trust. *Fix:* Add one concrete data point per finding (e.g., "average RIAM < 0.2 across models").

**Issue 7 (Major): "First to incorporate ICL" claim is underspecified.** The novelty claim about ICL integration (Page 2) needs explicit scoping to be verifiable. ICL/few-shot evaluation exists in prior LLM frameworks and VLM benchmarks. *Fix:* Scope to "first to systematically incorporate multimodal ICE with image retrieval across diverse visual tasks within a unified evaluation framework."

## Actionable Suggestions
**Suggestion 1 [Must — Mathematical robustness].** Revise RIAM (Eq. 1) and RRM (Eq. 2) to handle the degenerate case where model accuracy ≤ random baseline. Proposed replacement for RIAM:
$$ \text{RIAM}^* = \frac{\text{acc}_{\text{ICL}} - \text{acc}_{\text{0-shot}}}{\max(\text{acc}_{\text{0-shot}},\;1 - 1/n) - \text{acc}_{\text{0-shot}}} $$
where $n$ is the number of answer choices, ensuring a positive denominator. Apply the same fix to RRM using $\max(\text{acc},\;1 - 1/n)$ as the upper bound. Add an explicit flag for cases where the numerator is also near-zero (define RIAM = 0 if both numerator and denominator are below a threshold ε).

**Suggestion 2 [Must — Evaluation validity].** Revise the VOC2012 detection Recipe to include distractor boxes from other objects in the same image (not just perturbed GT boxes). Report both multi-choice accuracy and a detection-specific metric (e.g., mean precision@k or recall@k) to provide a more complete picture of detection behavior. Explicitly discuss in the paper that the current protocol tests localization discrimination rather than open-vocabulary detection.

**Suggestion 3 [Must — Statistical rigor].** For the correlation analysis (Section 3.5): (a) report Pearson r with 95% confidence intervals using Fisher z-transformation, (b) add p-values and flag non-significant correlations (p > 0.05), (c) include scatter plots with per-model labels so readers can visually assess outlier influence, and (d) add a caveat paragraph acknowledging the small sample size (N=9) and recommending cautious interpretation.

**Suggestion 4 [Must — Reproducibility].** Create an appendix table with the following for each model: checkpoint URL or exact version identifier, inference temperature, top-p, max-tokens, PPL answer pool construction method and size, ICE number of shots and random seed(s), and corruption severity levels (specify which ImageNet-C or similar severity was used). Also report whether multiple random seeds were used for ICE retrieval and how results were aggregated.

**Suggestion 5 [Must — Calibration interpretation].** Add a paragraph in Section 3.3 distinguishing calibration (ECE) from sharpness/discrimination. Report the average confidence alongside accuracy so readers can assess whether low ECE reflects meaningful uncertainty or uniform underconfidence. Consider reporting the Brier score decomposition (uncertainty, resolution, reliability) for deeper insight.

**Suggestion 6 [Must — Key findings anchoring].** In the Introduction (Page 3, bullet list), replace the abstract three findings with evidence-anchored versions. For example: "(1) No model ranks in the top-3 across more than 5 of 9 scenarios; e.g., InstructBLIP excels on MMBench (65.73) but trails on VOC (27.65) compared to Shikra (55.23). (2) Average ICL accuracy improvement over zero-shot is less than 3 points for 7/9 models. (3) Hallucination accuracy and MMBench accuracy show Pearson r > 0.8 (N=9), though this requires larger-sample validation."

**Suggestion 7 [Must — Novelty claim scoping].** Replace "we are the first to incorporate ICL into the evaluation framework" with: "To our knowledge, ChEF is the first evaluation framework to systematically incorporate multimodal in-context examples with image-level retrieval across diverse visual tasks within a unified modular interface."

**Suggestion 8 [Nice-to-have — GPT evaluation validation].** Report human correlation results specific to your GPT-4 evaluation setup. If a full human study is infeasible, provide: (a) example CoT outputs with their GPT-4 scores to allow qualitative calibration, (b) agreement rates across GPT-4 evaluation rounds (not just averaging), and (c) sensitivity analysis showing whether conclusions change under different GPT prompts/temperature settings.

**Suggestion 9 [Nice-to-have — Variance reporting in main table].** Add standard deviations or confidence intervals to Table 1, ideally from multiple decoding runs or temperature sampling. At minimum, add a footnote explaining which results are single-run and would need multi-seed confirmation, especially for small-margin comparisons.

**Suggestion 10 [Nice-to-have — Language performance scope].** Clarify whether GPT-4 evaluates only grammatical correctness, factual consistency, reasoning coherence, or a composite score. The current description ("language performance") is ambiguous between fluency and reasoning quality.

## Storyline Options + Writing Outlines
### Abstract Outline (Compact 5-Sentence Structure)

| Sentence | Role | Content | Evidence Anchor |
|----------|------|---------|-----------------|
| S1 | Problem & domain | MLLMs show remarkable multimodal abilities, but their evaluation lacks a standardized framework. | Page 1 - Abstract |
| S2 | Challenge/gap | Existing benchmarks are fragmented — they focus on individual datasets or narrow capability dimensions. | Page 1 - Abstract, Page 1-2 - Introduction |
| S3 | Proposed method | We introduce ChEF, a modular framework decomposing evaluation into Scenario, Instruction, Inferencer, and Metric, composable as Recipes. | Page 1 - Abstract, Page 2 - Method |
| S4 | Key results | Evaluating 9 MLLMs across 9 scenarios and 6 desiderata reveals: no model excels universally; ICL and robustness remain weak; hallucination correlates with visual performance. | Page 7 - Table 1, Page 8-9 - Sections 3.4-3.5 |
| S5 | Impact & release | ChEF is released as an open-source toolkit for community-wide standardized MLLM evaluation. | Page 1 - Abstract |

### Introduction Outline (Paragraph-by-Paragraph Plan)

**P1 — The MLLM evaluation gap [Current: Page 1, lines 32-45]**
Role: Establish territory and identify gap. Start by stating the practical importance of evaluating MLLMs, then immediately identify the concrete problem: the lack of a standardized, extensible framework. Avoid opening with general LLM praise.
*Transition:* "This fragmented evaluation landscape has two concrete costs..."
*Evidence anchor:* Existing benchmarks are dataset-specific or dimension-limited.
*Mentor Revised Opening:* "Evaluating Multimodal Large Language Models is essential for understanding their capabilities and guiding progress, yet the community lacks a standardized framework that can holistically profile different models. Existing benchmarks tend to focus on isolated datasets or target only one or two capability dimensions. Frameworks that attempt broader coverage often lack scalability to new datasets or evaluation dimensions. As a result, cross-model comparisons conflate task performance, evaluation protocol choices, and model intrinsic properties."

**P2 — Proposed framework ChEF [Current: Page 1-2]**
Role: Occupy the niche. Present ChEF's four components and explain how each addresses a specific gap from P1. Introduce the Recipe abstraction.
*Transition:* "To address these issues, we propose ChEF..."
*Evidence anchor:* Figure 1 conceptual diagram, Section 2 design principles.

**P3 — Desiderata and six new recipes [Current: Page 3]**
Role: Introduce the six evaluation dimensions beyond perception. Explain why these are essential for real-world deployment.
*Transition:* "Beyond standard visual task evaluation, a competent MLLM agent must exhibit..."
*Evidence anchor:* Six desiderata list, Figure 3-4.

**P4 — Key findings preview [Current: Page 3]**
Role: Preview the three most important empirical takeaways with concrete numbers, not abstract statements. This builds credibility.
*Transition:* "Our large-scale evaluation yields three principal findings..."
*Evidence anchor:* Each finding should cite one specific result from Table 1 or Figure 5.

**P5 — Contributions (can merge with P4)**
Role: Explicit numbered contribution summary. Currently implicit in the text.
*Mentor Revised Version:* "Our contributions are: (1) ChEF, the first modular evaluation framework for MLLMs with four composable components; (2) six new desiderata recipes covering calibration, ICL, instruction following, language performance, hallucination, and robustness; (3) the finding that PPL-based Multi-Turn Inferencers reduce query-induced variance by X% compared to direct output; (4) an open-source toolkit enabling community-driven extension."

### Alternative Storyline Candidates

**Candidate A (Current):** Evaluation gap → ChEF framework → Desiderata → Experiments → Correlation analysis → Conclusion
*Strength:* Covers all content. *Weakness:* Framework description is interleaved with motivation, and key results are deferred too late.

**Candidate B (Recommended):** Evaluation gap + concrete costs → ChEF components as targeted solutions → Stability advantage of PPL Inferencer (most novel technical insight) → Desiderata as real-world readiness test → Findings with evidence anchoring → Limitations and release
*Strength:* Leads with the paper's most original technical contribution (stability measurement). Better for engaging methodology-oriented readers.

**Candidate C:** Motivating application (real-world deployment failures) → What capabilities are needed → How to measure them → ChEF framework → Validation of ChEF's reliability → Findings per capability → Implications for future model design
*Strength:* Strong application-driven narrative. Better for demonstrating practical impact.

**Recommendation:** Candidate B is the strongest because the stability analysis (Section 3.4) is the paper's most unique empirical contribution — showing that evaluation protocol choices introduce substantial variance that confounds model comparisons. Leading with this insight would better differentiate ChEF from prior work and engage readers earlier.

## Priority Revision Plan
| Priority | Issue | Action | Effort | Impact | Requirement |
|----------|-------|--------|--------|--------|-------------|
| P0 | RIAM/RRM mathematical invalidity | Bound denominator, add degenerate-case handling | Low (formula change + re-run metrics) | High — core metric validity | Must |
| P0 | Detection evaluation validity | Add distractor boxes, precision/recall metrics | Medium (code change + re-run) | High — evaluation claims | Must |
| P0 | Reproducibility specs | Add appendix table with model versions, hyperparameters, seeds, corruption levels | Low (documentation only) | High — reproducibility | Must |
| P1 | Correlation statistical rigor | Report p-values, CIs, scatter plots, caveats | Low (compute stats) | High — conclusion reliability | Must |
| P1 | Calibration interpretation | Add sharpness metrics, Brier decomposition | Medium (additional analysis) | Medium — avoids misinterpretation | Must |
| P1 | Key findings evidence anchoring | Add one concrete number per finding in Introduction | Low (text revision) | High — reader trust | Must |
| P1 | Novelty claim scoping | Tighten "first to incorporate ICL" wording | Low (text revision) | Medium — defensibility | Must |
| P2 | GPT evaluation validation | Report human correlation or sensitivity analysis | High (human study or re-analysis) | Medium — evaluation confidence | Nice-to-have |
| P2 | Variance reporting in Table 1 | Add multi-seed or multi-run std dev | Medium (re-run) | Medium — statistical reliability | Nice-to-have |
| P2 | Language performance scope | Clarify what GPT-4 evaluates (fluency vs reasoning vs factuality) | Low (text revision) | Low — clarity | Nice-to-have |

**Revision Stage 1 (P0, before next submission):** Fix RIAM/RRM formulas, revise detection evaluation protocol, add reproducibility appendix. These are required for metric validity and reproducibility.

**Revision Stage 2 (P1, before next submission):** Add statistical rigor to correlation analysis, revise calibration interpretation, anchor key findings with numbers, scope novelty claims. These strengthen the paper's defensibility.

**Revision Stage 3 (P2, for camera-ready):** Validate GPT evaluation, add variance reporting, clarify language performance scope. These improve quality but are not blockers.

```text
ASCII Diagram — Revision Strategy Roadmap
[P0: RIAM/RRM fix] 
    -> [Expected: Valid metrics across all model-scenario pairs]
    -> [Gate: No undefined or inverted values in reported tables]
[P0: Detection protocol revision]
    -> [Expected: Open-vocabulary detection measured, not just localization]
    -> [Gate: Precision/recall reported alongside accuracy]
[P0: Reproducibility appendix]
    -> [Expected: All configs fully specified]
    -> [Gate: Independent reproduction possible]
[P1: Statistical + calibration + evidence fixes]
    -> [Expected: Claims match evidence strength]
    -> [Gate: No unsupported interpretative leaps]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Visual performance across scenarios | 9 MLLMs, 9 scenarios, default Recipe with PPL | Accuracy (per task) | InstructBLIP leads on most; no model dominates all (Table 1) | C1 (framework enables fair comparison) | No variance/CI; detection protocol validity concern |
| E2 | Calibration assessment | MMBench + SQA, standard query, Multi-Turn ECE | ECE (1-ECE → score) | Most models show low ECE | C2 (desiderata quantification) | Low ECE may reflect trivial underconfidence |
| E3 | ICL evaluation | MMBench + SQA, random ICE, Multi-Turn | RIAM | Most models show poor ICL; Otter best but still weak | C2 (ICL measurement) | RIAM formula can be undefined when acc0-shot ≤ accrand |
| E4 | Instruction following | MMBench + SQA, verbalizer-manipulated queries | Match Ratio (MR) | Low MR for unnatural instructions | C2 (instruction following) | Limited to 3 verbalizer categories |
| E5 | Language performance | MMBench + SQA, CoT outputs, GPT-4 evaluation | GPT-4 score (normalized) | Mostly satisfactory except Kosmos-2 | C2 (language quality) | GPT-4 reliability for this task unverified |
| E6 | Robustness | MMBench + SQA, image + text corruptions | RRM | Most models struggle under corruption | C2 (robustness measurement) | RRM denominator zero risk; severity unspecified |
| E7 | Hallucination | MSCOCO, POPE protocol, PPL Inferencer | Accuracy | InstructBLIP and Shikra lead; correlates with MMBench | C2 (hallucination); C3 (correlation insight) | Single dataset (MSCOCO) |
| E8 | Stability of Inferencer types | CIFAR10 + SQA, multiple queries, 3 MLLMs | Accuracy distribution (boxplot) | PPL reduces variance vs Direct; Multi-Turn (CoT+PPL) best | C1 (framework reliability) | Only 2 scenarios, 3 models tested |
| E9 | Correlation analysis | 9 MLLMs, MMBench accuracy vs 6 desiderata | Pearson r | Hallucination ↔ MMBench strong; calibration independent | C3 (desiderata reveal composite performance) | N=9, no p-values/CIs |

### Research-Theme Gap Diagnosis

1. **New Knowledge Contribution:** The paper's primary knowledge contribution is methodological — showing that evaluation protocol choices (Inferencer type, query wording) introduce substantial variance that confounds MLLM comparison. This is a valid and useful finding. However, the *substantive* MLLM capability insights (e.g., "models struggle with ICL") are limited by metric validity issues (RIAM/RRM) and statistical weaknesses (N=9 correlations), reducing their knowledge value until these are addressed.

2. **Reproducibility/Reusability:** The framework reusability is the strongest aspect, but the missing experimental specifications (model versions, hyperparameters) directly undermine reproducibility of the empirical findings.

3. **Impact on Practice/Understanding:** The finding that hallucination correlates with discriminative task performance has practical implications for benchmark design. However, this finding needs stronger statistical support before it can change practice.

### Proposed Research Experiments

**P0 Experiment 1 — RIAM/RRM robustness to degenerate cases**
- Target Claim: "RIAM and RRM reliably measure ICL and robustness improvement"
- Hypothesis: Reformulated metrics will produce consistent rankings without undefined/inverted values
- Minimal Design: Re-compute all RIAM and RRM values with bounded denominator; compare ranking correlation (Spearman) between original and revised metrics
- Controls/Baselines: Also report raw accuracy deltas (accICL − acc0-shot) as reference
- Metrics: Rank correlation, fraction of undefined values eliminated
- Success Criterion: Zero undefined/inverted values; rank correlation > 0.8 with original where original is defined
- Estimated Cost/Time: Low (re-computation from existing raw accuracies in Table 1 and Figure 5)
- Expected Quality Gain: Core metric validity restored

**P0 Experiment 2 — Detection protocol with open-vocabulary test**
- Target Claim: "ChEF evaluates object detection capability in MLLMs"
- Hypothesis: Current protocol overestimates detection performance by using GT-derived answer pools
- Minimal Design: Add distractor boxes from: (a) other objects in same image, (b) random objects from other images. Compare accuracy and precision/recall
- Controls/Baselines: Current GT-only protocol as baseline
- Metrics: Multi-choice accuracy, precision@k, recall@k
- Success Criterion: Detection ranking changes between old and new protocol for at least 2 models
- Estimated Cost/Time: Medium (code modification to answer pool generation, re-run all 9 models)
- Expected Quality Gain: Valid detection evaluation, more credible comparison of Shikra/Kosmos-2 vs others

**P0 Experiment 3 — Reproducibility documentation**
- Target Claim: (supporting all claims)
- Minimal Design: Create one appendix table with all hyperparameters, model versions, and random seeds used
- Estimated Cost/Time: Low (documentation only)
- Expected Quality Gain: Enables independent reproduction; addresses a critical current gap

**P1 Experiment 4 — Calibration sharpness analysis**
- Target Claim: "MLLMs exhibit good calibration"
- Hypothesis: Low ECE is driven by uniform underconfidence, not meaningful per-instance uncertainty
- Minimal Design: Compute Brier score decomposition (uncertainty, resolution, reliability) and average confidence per model
- Controls/Baselines: Compare against a uniform-predictor baseline
- Metrics: Brier score components, average confidence, ECE
- Success Criterion: Resolution component is low (indicating poor per-instance discrimination) if trivial calibration confound exists
- Estimated Cost/Time: Low (re-use existing PPL probabilities)
- Expected Quality Gain: Honest calibration interpretation; avoids misleading readers

**P1 Experiment 5 — Correlation robustness with bootstrapping**
- Target Claim: "Hallucination strongly correlates with visual performance"
- Hypothesis: Observed correlations are robust under resampling
- Minimal Design: Bootstrap the Pearson correlation (10,000 resamples with replacement from N=9 models); report 95% CI
- Metrics: Bootstrap CI width, p-value
- Success Criterion: 95% CI excludes zero for the hallucination-MMBench correlation
- Estimated Cost/Time: Low (computational, from existing data)
- Expected Quality Gain: Statistical credibility for a key finding

### ASCII Diagram — Experiment Upgrade Plan
```text
P0 (Before Resubmission)
├── Exp 1: Fix RIAM/RRM denominators
│   └── Re-run metrics → Valid rankings
├── Exp 2: Fix detection protocol
│   └── Add distractor boxes → Honest detection scores
└── Exp 3: Reproducibility table
    └── Document all configs → Independent reproduction

P1 (Before Resubmission)
├── Exp 4: Calibration sharpness analysis
│   └── Brier decomposition → Honest uncertainty assessment
└── Exp 5: Bootstrap correlation analysis
    └── 95% CI from resampling → Statistical rigor

P2 (Camera-ready)
├── GPT evaluation validation
├── Multi-seed variance reporting
└── Language performance scope clarification
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

The paper addresses an important need (standardized MLLM evaluation) and has several genuine strengths: the modular framework design, the stability analysis showing PPL reduces evaluation variance, and the broad model coverage. However, the score is limited by:

- **Research value (moderate):** The framework contribution is useful but largely organizational — combining existing benchmarks and metrics under one interface, with the main novel technical insight being the stability analysis of Inferencer types. The six desiderata individually follow established methods (POPE for hallucination, ECE for calibration, HELM-inspired methodology).
- **Validity risks (high):** Two core metrics (RIAM, RRM) have mathematical defects that can produce undefined or inverted values. The correlation analysis (N=9) lacks statistical grounding. The detection evaluation does not measure what it claims to measure. These issues directly affect the credibility of reported conclusions.
- **Novelty (uncertain, deferred):** The "first to incorporate ICL" claim and the overall framework novelty require external literature verification that was unavailable in this run. Marked as deferred.
- **Reproducibility (low):** Critical experimental specifications are missing.
- **Writing quality (adequate):** Generally clear but the Introduction would benefit from more evidence-anchored findings and tighter narrative structure.

**Post-Revision Target: [6.5, 7.0] / 10**

If the authors address the P0 and P1 items (fix RIAM/RRM, revise detection protocol, add reproducibility appendix, strengthen correlation statistics, revise calibration interpretation, anchor findings with numbers, scope novelty claims), the score is estimated to reach 6.5-7.0. This range assumes the framework's research value is validated and its methodological rigor is brought to an acceptable standard. Further improvement beyond 7.0 would require stronger novelty differentiation from prior evaluation frameworks, which cannot be assessed without external literature review.

### Score Breakdown

| Dimension | Score (1-10) | Rationale |
|-----------|-------------|-----------|
| Problem Significance | 8 | Standardized MLLM evaluation is a timely and important problem |
| Novelty | 5* | Framework design is useful but incremental; stability analysis is novel; *deferred for external verification |
| Methodological Soundness | 4 | Core metrics have mathematical defects; detection protocol has validity concerns |
| Experimental Rigor | 4 | Missing variance/CIs; N=9 correlation; missing reproducibility specs |
| Writing & Presentation | 6 | Clear structure but abstract findings lack evidence anchoring |
| Reproducibility | 3 | Critical configuration details absent |
| Overall | 5.5 | Important problem, useful framework, but validity and reproducibility gaps require substantial fixes |