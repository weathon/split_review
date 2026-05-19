## Summary
This paper introduces TRAM (Temporal Reasoning for Large Language Models Benchmark), a multi-task benchmark comprising 10 temporal reasoning tasks (38 subtasks, ~526.7k questions) in multiple-choice format. The tasks are organized into three groups: foundational understanding (ordering, frequency, duration, typical time), temporal interpretation/computation (ambiguity resolution, arithmetic), and advanced understanding (temporal relations, temporal NLI, temporal causality, storytelling). The authors evaluate GPT-4, GPT-3.5, PaLM2, Llama2-13B, and BERT/RoBERTa models across zero-shot and few-shot settings with standard and chain-of-thought prompting. GPT-4 achieves the highest average accuracy (87.4% with 5-shot CoT), but still trails human expert performance by ~10 percentage points. Manual error analysis identifies assumption bias, calculation slips, and implicit oversights as dominant error types. The benchmark aims to provide a unified evaluation framework for temporal reasoning in LLMs.

## Strengths
1. **Comprehensive task coverage**: TRAM spans 10 diverse temporal reasoning tasks (38 subtasks, 526.7k questions), covering temporal aspects from foundational concepts (duration, frequency, ordering) to complex narrative and causal reasoning. This is the most comprehensive temporal reasoning benchmark assembled to date, addressing the fragmentation of prior datasets.

2. **Structured taxonomy**: The three-group organization (Foundational, Interpretation/Computation, Advanced) provides a clear diagnostic hierarchy, enabling researchers to pinpoint which temporal abilities a model lacks.

3. **Rigorous human baseline**: Expert annotators with a stringent 92% screening threshold provide a credible human upper bound (~95.2% average accuracy), and the comparison with non-specialists (63.5%) offers a useful reference for task difficulty.

4. **Broad model evaluation**: The paper evaluates 8 distinct model families (BERT-base/large, RoBERTa-base/large, Llama2-13B, PaLM2, GPT-3.5, GPT-4) under multiple prompting conditions (zero/few-shot, SP/CoT), providing a comprehensive reference benchmark.

5. **Error analysis**: The manual error categorization (assumption bias, calculation slips, implicit oversights) across three task groups provides actionable insights for future research on temporal reasoning improvements.

6. **Publicly sourced construction**: The benchmark combines existing datasets, human-crafted templates, programmatic generation, and web sources, demonstrating a reproducible methodology for multi-task benchmark construction.

## Weaknesses
1. **Subset evaluation limits statistical reliability** (Severity: Major). The paper evaluates only 200 examples per category (or all available if fewer). For benchmarks with >100k examples (Relation, Temporal NLI), this is <0.2% coverage. With 200 examples per category, the 95% confidence interval for accuracy is ~±7 percentage points for 2-way MCQs and larger for 3/4-way formats, meaning many cross-model comparisons may fall within the margin of error. Variance and confidence intervals are not reported.

2. **Unfair comparison between fine-tuned BERT and zero-shot LLMs** (Severity: Major). The paper compares fine-tuned BERT/RoBERTa (using 1-50% of training data) against zero/few-shot LLMs without fine-tuning. The finding that RoBERTa-large outperforms Llama2-13B is confounded by training paradigm, not model capacity. No controlled experiment disentangles these factors.

3. **Incomplete novelty/comparison analysis** (Severity: Major). External literature verification was unavailable in this run. The paper's claim of being the "first comprehensive temporal reasoning benchmark" cannot be fully validated without systematic comparison to prior benchmarks like TimeDial, TempQuestions, and recent temporal QA datasets. This is flagged as deferred manual verification.

4. **Task validity concerns for Temporal NLI and Typical Time** (Severity: Medium). The Temporal NLI task uses keyword filtering from SNLI/MNLI, but many keyword-matched examples may be solvable without temporal reasoning (e.g., general NLI ability suffices). The Typical Time task is dominated (69.84%) by Reading Comprehension subtasks that primarily test time-entity extraction rather than temporal reasoning about typicality.

5. **Human baseline limited coverage** (Severity: Medium). The human performance estimate (95.2%) is based on ~1,900 questions (<0.4% of the benchmark) with each expert answering 50 questions per category. No per-annotator or per-category variance is reported, limiting reliability of the human upper bound.

6. **Missing discussion of data contamination risk** (Severity: Medium). Several TRAM tasks draw from public sources (Wikipedia, SNLI, SQuAD, MCTACO) that may appear in LLM pre-training corpora, potentially inflating reported performance. This is only briefly acknowledged and not quantitatively assessed.

7. **"Best results after multiple runs" reporting practice** (Severity: Minor). Reporting best-of-multiple-runs without mean/variance is known to inflate performance estimates, especially for the small 200-example subsets used here.

## Key Issues
### Key Issue 1: Statistical reliability of evaluation results
**Severity**: Major | **Validity Risk**: High | **Fixability**: Easy

The evaluation uses only 200 examples per category, but no confidence intervals or significance tests are reported. With 200 examples, a 3-way MCQ has a 95% CI of roughly ±6-7 percentage points. Many reported differences between models (e.g., Llama2 vs GPT-3.5 on frequency: 73.7% vs 78.5%) fall within or near this range. The paper states "we report the best results after multiple runs for each experimental setting" without reporting variance.

**Fix**: Report mean±std across ≥3 independent runs (or bootstrap confidence intervals) for each model/setting. Provide a significance test (e.g., McNemar's test) for the comparison between GPT-4 and the next-best model per task. Increase evaluation subsets to at least 500 per category for the main comparison table.

### Key Issue 2: Confounded comparison between BERT-style models and LLMs
**Severity**: Major | **Validity Risk**: High | **Fixability**: Medium

The paper compares fine-tuned BERT/RoBERTa (trained on 1-50% of task data) with zero/few-shot LLMs. The conclusion that "RoBERTa-large surpasses Llama2 in average performance" is confounded by training regime. BERT models receive task-specific parameter updates while LLMs do not.

**Fix**: (a) Add zero-shot evaluation for BERT/RoBERTa classification heads to enable direct comparison; (b) fine-tune Llama2 on the same minimal supervision subsets and then compare; (c) explicitly acknowledge the confound and qualify the conclusion.

### Key Issue 3: Validity of Temporal NLI and Typical Time tasks
**Severity**: Medium | **Validity Risk**: Medium | **Fixability**: Medium

Temporal NLI uses keyword filtering from SNLI/MNLI, but the paper does not verify whether selected examples genuinely require temporal reasoning. The Typical Time task is 69.84% Reading Comprehension (time-entity extraction), not temporal reasoning about typicality.

**Fix**: For Temporal NLI, conduct an additional validation: create a control set by masking temporal keywords and measuring accuracy drop. Report the fraction of questions where temporal information is necessary for the correct answer. For Typical Time, either rebalance subtask weights or filter Reading Comprehension questions to require multi-sentence temporal inference.

### Key Issue 4: Missing data contamination analysis
**Severity**: Medium | **Validity Risk**: Medium | **Fixability**: Medium

Many TRAM sources (Wikipedia, SNLI, SQuAD, MCTACO) are likely present in LLM pre-training data. The paper acknowledges this only generically in Limitations.

**Fix**: Perform a contamination analysis: (a) measure exact/near-exact n-gram overlap between TRAM questions and common pre-training corpora (e.g., C4, Pile); (b) report per-task contamination ratios; (c) discuss how contamination may affect GPT-4's strong performance.

### Key Issue 5: Introduction storyline needs sharper gap articulation
**Severity**: Medium | **Validity Risk**: Low | **Fixability**: Easy

The introduction motivates temporal reasoning broadly but does not clearly articulate the specific gap that TRAM fills relative to each prior benchmark. The claim "none of these works have tackled broad aspects of TeR within a unified framework" is asserted without a structured comparison showing exactly what each prior benchmark covers and misses.

**Fix**: Add a comparison table or structured paragraph mapping prior datasets to the 10 TRAM task dimensions, showing coverage gaps explicitly.

## Actionable Suggestions
### S1 (Must) — Add confidence intervals and significance tests to all experimental results
Replace the current "best results after multiple runs" reporting with mean±std over ≥3 runs. Add McNemar's test or bootstrap confidence intervals for the primary model comparisons (GPT-4 vs second-best per task). Increase evaluation to at least 500 examples per category for the main comparison table. This is the single most impactful revision for improving the paper's scientific rigor.

### S2 (Must) — Add zero-shot BERT/RoBERTa evaluation or fine-tuned Llama2 baseline
To make the BERT-vs-LLM comparison fair, either: (a) evaluate BERT/RoBERTa in a zero-shot classification setting (using [CLS] + linear probe without fine-tuning), or (b) fine-tune Llama2 on the same minimal supervision subsets used for BERT. Report both comparisons separately in Table 2 or a supplementary table. Qualify the RoBERTa > Llama2 finding to acknowledge the training regime confound.

### S3 (Must) — Add data contamination analysis
For each TRAM task sourced from public datasets (Wikipedia, SNLI, SQuAD, MCTACO, ROCStories), compute n-gram overlap with common LLM pre-training corpora (C4, The Pile). Report per-task contamination rates in a supplementary table. For the highest-contamination tasks, provide a "contamination-controlled" subset of new, non-public questions and re-evaluate GPT-4 on it.

### S4 (Should) — Validate temporal necessity for Temporal NLI and Typical Time tasks
For Temporal NLI: create a control set by removing/masking temporal keywords and measure the accuracy drop of a strong NLI model. Report the fraction of questions where temporal information changes the correct answer. For Typical Time: rebalance subtask weights or explicitly filter Reading Comprehension questions to require multi-sentence temporal inference rather than span extraction.

### S5 (Should) — Expand human baseline with per-category breakdown and variance
Report human expert performance with per-category breakdown (not just aggregate) and per-annotator variance. Increase the human evaluation sample to at least 100 questions per category to improve statistical reliability. Add 95% confidence intervals to the human row in Table 2.

### S6 (Nice-to-have) — Restructure Related Work around comparison axes
Replace the chronological survey of temporal reasoning datasets with a structured comparison table mapping each prior benchmark to TRAM's 10 task dimensions. This will make the comprehensive coverage claim immediately visible and defensible.

### S7 (Nice-to-have) — Add benchmark release commitment and leaderboard plan
Add a statement committing to public release of TRAM, standardized evaluation scripts, and a public leaderboard. Include a plan for a held-out, non-public test set for contamination-controlled evaluation.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)

**S1 (Problem & Domain)**: "Reasoning about time is essential for understanding events described in natural language, but existing benchmarks evaluate only isolated temporal phenomena such as event ordering or time-sensitive QA, preventing systematic diagnosis of LLMs' temporal reasoning capabilities."

**S2 (Gap)**: "No existing benchmark jointly covers foundational temporal understanding (duration, frequency, typical time), temporal computation (arithmetic, ambiguity resolution), and advanced temporal reasoning (relations, causality, narrative inference) within a unified evaluation framework."

**S3 (Proposed solution)**: "We introduce TRAM, a benchmark of 10 tasks (38 subtasks, 526.7k questions) spanning these three dimensions in a multiple-choice format designed for reproducible LLM evaluation."

**S4 (Key results)**: "Evaluating GPT-4, GPT-3.5, PaLM2, Llama2-13B, and BERT/RoBERTa, we find that GPT-4 achieves the highest average accuracy (87.4% with 5-shot chain-of-thought), yet trails human expert performance by approximately 10 percentage points."

**S5 (Implication)**: "Manual error analysis reveals that models consistently struggle with implicit temporal cues and assumption biases across all task categories, providing a roadmap for targeted improvements in LLM temporal reasoning."

### Introduction Outline (Complete)

**P1 — Motivation and general challenge** (Page 1, paragraph 1 revised):
Role: Establish why temporal reasoning matters and that LLMs still struggle.
Target claim: Temporal reasoning is fundamental and remains unsolved.
Transition: End with a concrete statement of what is missing in prior work.

Mentor Revised Version:
"Temporal reasoning is fundamental to human understanding of events, narratives, and causality. While large language models have made significant progress on many NLP benchmarks, mastering temporal reasoning — with its inherent variability in expressions, need for contextual grounding, and multi-step computation — remains an open challenge. Crucially, existing temporal reasoning benchmarks evaluate only isolated facets such as event ordering or duration, leaving a unified assessment of core temporal abilities unaddressed."

**P2 — Prior work and gap** (Page 1, paragraph 2 revised):
Role: Review prior temporal reasoning datasets and identify the fragmentation gap.
Target claim: Prior benchmarks cover narrow subsets, no unified framework exists.
Transition: Lead into the need for a comprehensive benchmark.

Mentor Revised Version:
"Recent work in temporal reasoning has produced valuable datasets targeting specific subtasks: MCTACO focuses on commonsense duration and ordering, TEMPREASON evaluates event-time relations, and TEMPLAMA probes temporal knowledge via cloze tasks. While these studies confirm that current models fall short of human-level performance, each addresses only one or two dimensions. None jointly spans foundational temporal concepts, temporal interpretation and computation, and advanced narrative or causal understanding. This fragmentation prevents researchers from systematically diagnosing which temporal abilities LLMs lack and under what conditions."

**P3 — TRAM benchmark description** (Page 1, paragraph 3 revised):
Role: Introduce TRAM as the solution covering the identified gap.
Target claim: TRAM provides a comprehensive, unified evaluation framework.
Transition: Bridge from benchmark design to key results.

Mentor Revised Version:
"To address this gap, we introduce TRAM (Temporal Reasoning for Large Language Models Benchmark), a collection of 10 tasks and 38 subtasks with 526.7k multiple-choice questions. TRAM is organized into three groups: foundational understanding (ordering, frequency, duration, typical time), temporal interpretation and computation (ambiguity resolution, arithmetic), and advanced understanding (temporal relations, temporal NLI, temporal causality, storytelling). Each question has exactly one correct answer, verified through expert annotation and programmatic consistency checks, enabling scalable and reproducible evaluation."

**P4 — Results preview** (Page 2, paragraph 1 revised):
Role: Summarize main experimental findings and the human gap.
Target claim: Even the best LLM (GPT-4) trails human performance, especially on implicit temporal cues.
Transition: Conclude with the paper's three contributions.

Mentor Revised Version:
"We evaluate eight model families (BERT, RoBERTa, Llama2-13B, PaLM2, GPT-3.5, GPT-4) under zero-shot and few-shot settings with standard and chain-of-thought prompting. GPT-4 achieves the strongest results (87.4% average accuracy), yet expert human performance reaches 95.2% — a gap of roughly 10 percentage points. Manual error analysis reveals that models consistently fail on nuanced understanding and implicit temporal cues across all task groups, suggesting that improved temporal reasoning requires advances beyond scaling alone."

**P5 — Contributions** (Page 2, bullet list):
Keep current three-point list but rephrase for clarity:
(1) "TRAM: a unified benchmark of 10 temporal reasoning tasks in MCQ format."
(2) "Extensive evaluation across 8 model families and multiple prompting strategies, establishing reference results."
(3) "Error analysis identifying consistent failure modes (assumption bias, calculation slips, implicit oversights) across temporal task categories."

### Current Storyline Evaluation

The current introduction follows a reasonable arc (motivation -> prior work gap -> benchmark description -> results preview -> contributions), but P1 and P2 lack specificity. P1 ends with a generic challenge statement, and P2 lists prior datasets without structured comparison. The proposed revision above adds concrete gap articulation in P1-P2 and quantitative results in P4, improving Problem Alignment, Variable Alignment, and Contribution-Evidence Alignment.

### Alternative Storyline Candidate

**Candidate B — Problem-first, then backward compatibility:**
P1: Same motivation.
P2: Show a unified coverage matrix (tabular form) comparing TRAM's 10 tasks against MCTACO, TEMPREASON, TimeDial, TempQuestions, and others. This immediately visualizes the gap.
P3: Describe TRAM benchmark.
P4: Results and error analysis.
P5: Contributions.

**Selected storyline**: The primary proposed outline above (P1-P5) is recommended because it is accessible, vertically coherent, and easy for readers to follow.

## Priority Revision Plan
### P0 — Critical (must fix before acceptance)

| Priority | Task | Action | Expected Impact | Effort |
|----------|------|--------|----------------|--------|
| P0.1 | Add confidence intervals & significance tests | Replace "best results after multiple runs" with mean±std over ≥3 runs; add bootstrap CIs to Table 2 | High: establishes statistical reliability of all reported comparisons | Medium (computational cost of 2 extra runs) |
| P0.2 | Add zero-shot BERT baseline or fine-tuned Llama2 | Run BERT/RoBERTa in zero-shot classification OR fine-tune Llama2 on minimal supervision | High: resolves confounded model comparison | Medium |
| P0.3 | Add data contamination analysis | Compute n-gram overlap with C4/Pile; report per-task contamination ratios | High: quantifies performance inflation risk | Low (computational analysis) |

### P1 — Major (should fix before acceptance)

| Priority | Task | Action | Expected Impact | Effort |
|----------|------|--------|----------------|--------|
| P1.1 | Validate temporal necessity of NLI and Typical Time tasks | Create masked-keyword control sets; report accuracy drop | Medium: validates task construct validity | Medium |
| P1.2 | Expand human baseline | Per-category human breakdown; per-annotator variance; increase sample to 100 questions/category | Medium: improves human upper-bound reliability | Medium |
| P1.3 | Restructure Related Work | Add comparison table mapping prior datasets to TRAM's 10 task dimensions | Medium: makes coverage gap immediately visible | Low |

### P2 — Nice-to-have (improves quality)

| Priority | Task | Action | Expected Impact | Effort |
|----------|------|--------|----------------|--------|
| P2.1 | Revise abstract | Add key numbers (GPT-4: 87.4%, Human: 95.2%) and specific gap articulation | Low: improves first impression | Low |
| P2.2 | Add benchmark release commitment | Statement on public release, evaluation scripts, leaderboard, held-out test set | Medium: enables community adoption | Low |
| P2.3 | Introduction rewrite | Sharper gap articulation in P1-P2; add structured prior work comparison | Medium: improves narrative clarity | Low |
| P2.4 | Temporal NLI rebalancing or filtering | Filter out questions solvable without temporal cues | Medium: improves task validity | Medium |

### Revision Roadmap Diagram

```text
ASCII Diagram — Revision Strategy Roadmap

[P0.1: Add CIs & significance tests]
    -> [Validity: every comparison becomes statistically grounded]
    -> [Expected: eliminates ranking uncertainty concern]

[P0.2: Zero-shot BERT / fine-tuned Llama2]
    -> [Validity: RoBERTa>Llama2 claim properly bounded]
    -> [Expected: fair model comparison established]

[P0.3: Data contamination analysis]
    -> [Validity: performance inflation risk quantified]
    -> [Expected: GPT-4 results interpreted with appropriate caution]

[P1.1: Temporal NLI/Typical Time validation]
    -> [Construct validity: tasks genuinely measure temporal reasoning]
    -> [Expected: benchmark credibility strengthened]

[P1.2: Expanded human baseline]
    -> [Reliability: human upper bound with per-category CIs]
    -> [Expected: more precise gap estimation]

[P2.1-P2.4: Writing & release improvements]
    -> [Adoption: easier for community to use and cite TRAM]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Compare LLMs on TRAM tasks | 8 models (BERT-base/large, RoBERTa-base/large, Llama2-13B, PaLM2, GPT-3.5, GPT-4); 10 tasks; zero/few-shot SP/CoT | Accuracy (Acc./F1 for Relation, NLI) | GPT-4 (5S, CoT): 87.4% average; trails humans by ~10% | C1 (benchmark utility), C2 (model comparison) | No confidence intervals; subset evaluation (200/category) |
| E2 | Minimal supervision fine-tuning of BERT-style models | 4 models fine-tuned on 1-50% of training data (size-dependent sampling); same test set as LLMs | Accuracy/F1 | RoBERTa-large: 65.9% average; outperforms Llama2-13B | C2 (BERT baseline) | Confounded comparison: fine-tuned BERT vs zero/few-shot LLMs |
| E3 | Human expert baseline | Expert annotators (screened at 92% threshold); 50 questions/category; ~1,900 total | Accuracy | Human: 95.2% average | C2 (human upper bound) | Small sample (<0.4% of benchmark); no per-category variance |
| E4 | Human non-specialist baseline | Amazon Mechanical Turk workers; same 1,900 questions as experts | Accuracy | Non-specialists: 63.5% average | C2 (difficulty reference) | No demographic/background controls reported |
| E5 | Error analysis | Manual review of LLM mistakes across all task groups; prompted model explanations | Error type proportions (Figure 4) | Assumption bias (32% foundational), Calculation slips (42% computation), Implicit oversights (34% advanced) | C3 (error taxonomy) | Based on model self-explanations, which may not reflect true reasoning process |
| E6 | SP vs CoT prompting comparison | Within Table 2: comparison across all models × tasks × shot settings | Accuracy delta between SP and CoT | CoT improves performance on most tasks | C2 (prompting effect) | No statistical test of CoT vs SP significance |
| E7 | Storytelling augmentation quality check | GPT-2 generated incorrect endings filtered for temporal themes | Qualitative filtering | Augmented data used for storytelling task | C1 (dataset construction) | No quantitative measure of augmentation quality (e.g., human eval of generated endings) |

### Research-Theme Gap Diagnosis

Three core research-value claims are weakly supported by current evidence:

1. **"Comprehensive unified benchmark"** (C1): While TRAM covers more temporal dimensions than any single prior dataset, the paper does not quantitatively demonstrate that TRAM's multi-task evaluation provides different insights than running individual existing benchmarks separately. A correlation analysis between task performances and comparison with individual benchmark scores would strengthen this claim.

2. **"LLMs still trail human performance"** (C2): The reported 10% gap is based on a small human sample (~1,900 questions) with no per-category breakdown. Without knowing which tasks contribute most to the gap, researchers cannot prioritize specific temporal abilities for improvement.

3. **"Error analysis reveals consistent challenges"** (C3): The error categorization relies on model self-explanations, which may not reflect the model's actual reasoning process. The analysis does not link specific architectural properties or prompting strategies to error types.

### Proposed Research Experiments

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Paper-Quality Gain |
|--------|-------------|-----------|---------------|-------------------|---------|------------------|----------------|---------------------------|
| RP0.1 | C2: Reliable model ranking | Current ranking may change with larger evaluation subsets | Re-evaluate GPT-4, GPT-3.5, PaLM2 on 1,000 examples/category (vs current 200) for 3 runs each | Same models, same prompts, larger sample | Mean accuracy, 95% CI, Cohen's kappa between rankings | CI width ≤ 2 percentage points for top-2 models | 2-3 GPU-days API cost | High: establishes statistical reliability of all comparisons |
| RP0.2 | C2: Fair model comparison | Fine-tuned Llama2 may match or exceed RoBERTa-large | Fine-tune Llama2-13B on same minimal supervision subsets used for BERT (1-50% of training data); evaluate on same test set | RoBERTa-large results from Table 2 | Accuracy per task | Llama2 fine-tuned achieves ≥ RoBERTa-large average | 5-10 GPU-days | High: resolves confounded model comparison |
| RP0.3 | C1: Contamination-controlled evaluation | GPT-4 performance may be inflated on public-source tasks | Create a held-out set of 50 new, non-public temporal reasoning questions per task | Compare GPT-4 performance on public vs held-out questions | Accuracy drop (public - held-out) | Drop ≤ 5 percentage points on average | 1-2 weeks for question creation + API eval | High: quantifies contamination risk |
| RP1.1 | C3: Causal error analysis | Error types correlate with model architecture (e.g., bidirectional vs causal attention) | For each error category (Figure 4), compute error rate per model architecture; control for accuracy | Stratify by model family and prompting strategy | Error-type × model interaction effect size | Significant interaction (p<0.05) for at least 2 error types | Analysis only | Medium: links architecture to failure modes |
| RP1.2 | C1: Temporal NLI validity | Some NLI questions are solvable without temporal cues | Create control set by masking temporal keywords (Table 7) in Temporal NLI questions; evaluate GPT-4 and RoBERTa-large on control vs original | Same models on original Temporal NLI test set | Accuracy difference (original - control) | Average drop > 10 percentage points, indicating temporal information is necessary | 1 day analysis + API calls | Medium: validates task construct |
| RP2.1 | C2: Human baseline reliability | Per-category human performance varies substantially | Sample 100 additional questions per category (total 150/category) for expert evaluation; report per-category accuracy and CI | Current human results (50/category) | Per-category accuracy, 95% CI, agreement between annotators | CI width ≤ 5 percentage points per category | 2-3 weeks annotation effort | Medium: improves human baseline reliability |

### Experiment Upgrade Plan Diagram

```text
ASCII Diagram — Experiment Upgrade Plan

P0 Experiments (Before Resubmission)
├── RP0.1: Larger evaluation subsets (1,000/category)
│   └── Enables: statistically reliable model ranking
├── RP0.2: Fine-tune Llama2 on minimal supervision
│   └── Enables: fair comparison with BERT-style models
└── RP0.3: Contamination-controlled held-out set
    └── Enables: quantify performance inflation risk

P1 Experiments (Before Acceptance Decision)
├── RP1.1: Error-type × architecture interaction
│   └── Enables: linking architectural properties to failure modes
└── RP1.2: Temporal NLI keyword masking control
    └── Enables: validating temporal necessity of NLI questions

P2 Experiments (For Camera-Ready)
└── RP2.1: Expanded human baseline (150 questions/category)
    └── Enables: per-category reliable human upper bound
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score**: 6.5 / 10

**Rationale**: TRAM is a large-scale, multi-task temporal reasoning benchmark with comprehensive coverage and a thorough evaluation. Its strengths include the structured taxonomy across 10 tasks, the broad model evaluation (8 model families), and the inclusion of human expert baselines. However, the score is constrained by three major validity concerns: (1) the lack of confidence intervals and statistical significance testing for all experimental results, given the small evaluation subsets (200 examples/category); (2) the confounded comparison between fine-tuned BERT models and zero/few-shot LLMs; and (3) the absence of data contamination analysis, which could materially affect GPT-4's reported performance. The benchmark's ultimate impact depends on resolving these methodological concerns. The novelty dimension cannot be fully assessed in this run due to retrieval limitations; the paper's claim of being the first comprehensive temporal reasoning benchmark requires external verification.

**Post-Revision Target**: [7.5, 8.0] / 10

**Rationale**: If all P0 fixes are implemented (confidence intervals, fair model comparison, contamination analysis) and the P1 recommendations are addressed (temporal NLI validity check, expanded human baseline), the paper's methodological rigor would substantially improve, supporting a score in the 7.5-8.0 range. The upper bound reflects that the benchmark's long-term value depends on community adoption and external validation of its coverage claims, which cannot be fully assessed at the current stage.