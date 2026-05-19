## Summary
# Final Review Report

## Summary

This paper introduces **MMA (Multi-Modal Large Language Models in Ambiguity Contexts)**, a benchmark dataset designed to evaluate whether MLLMs can use visual context to resolve textual ambiguity. The benchmark contains 261 ambiguous questions in multiple-choice VQA format, each paired with two divergent-context images that lead to different correct answers. The key metric is Ambiguity Accuracy (Amb_A)—the proportion of image pairs where the model correctly answers both. The authors evaluate 17 MLLMs (6 proprietary, 11 open-source) across lexical, syntactic, and semantic ambiguity types.

**Key findings from the manuscript:**
- The best model (Claude 3.5 Sonnet) achieves 74% Amb_A vs. 89% human accuracy
- Models perform best on lexical ambiguity and worst on syntactic ambiguity
- Open-source models underperform proprietary models by ~12-15%
- Error analysis reveals cross-modal text bias as the dominant error type (50%)

**Strengths:** MMA addresses an underexplored capability gap in MLLMs (visual disambiguation of ambiguous language). The paired-image design is a clean way to isolate whether models use visual context. The 17-model evaluation across three ambiguity types provides useful comparative data.

**Major weaknesses identified in this audit:** (1) Factual inconsistencies in model counts (abstract: 24, intro: 16, experiments: 17). (2) The 261-question dataset is small, with some sub-categories having <15 samples. (3) Human evaluation uses only 5 annotators with high individual variance (80-93%). (4) AI-generated images for some samples without ablation for confound analysis. (5) The conclusion contains inaccurate accuracy numbers and overclaims. (6) Statistical significance testing and confidence intervals are absent throughout. (7) Novelty claims cannot be verified without external literature search in this run (deferred).

## Strengths
1. **Well-motivated research question.** The paper addresses a genuinely underexplored capability gap in MLLMs—whether they can use visual context to disambiguate language. This is practically important for real-world multimodal interaction.

2. **Clean experimental design.** The paired-image VQA format, where the same question has two different correct answers depending on the image, is a simple but effective way to isolate whether models are truly using visual context or just relying on textual priors. The Amb_A metric follows naturally from this design.

3. **Comprehensive model coverage.** Evaluating 17 state-of-the-art MLLMs (proprietary + open-source) provides a useful snapshot of the field's current capabilities. The inclusion of multiple model families (GPT-4V, Gemini, Claude, LLaVA, VILA, InternVL, Qwen-VL) allows for cross-architecture comparison.

4. **Systematic ambiguity categorization.** The three-category taxonomy (lexical, syntactic, semantic) with eight sub-types is linguistically grounded and allows for fine-grained analysis. The finding that syntactic ambiguity is hardest for all models is a meaningful insight that can guide future research.

5. **Error analysis.** The three-type error taxonomy (uni-modal image, uni-modal text, cross-modal text bias) provides a useful framework for understanding failure modes. The dominance of cross-modal text bias (50%) is a clear signal that helps motivate future work on balanced multimodal integration.

6. **Transparency about limitations.** The manuscript explicitly acknowledges the small dataset size, use of AI-generated images, and the need for future expansion. This candor is appreciated and helps frame the benchmark as an initial contribution rather than a final evaluation.

## Weaknesses
### Critical / Major Weaknesses

1. **W1 — Factual inconsistencies across sections (Major).** The abstract states "24 proprietary and open-sourced MLLMs," the Introduction says "16 MLLMs" (contribution (b)), and Section 4.1 says "17 recent multimodal LLMs." Table 3 shows 6 proprietary + 11 open-source = 17 models. This internal contradiction undermines the paper's credibility. *(Anchored: Page 1 - Abstract, Page 2 - Introduction contribution (b), Page 6 - Section 4.1)*

2. **W2 — Small dataset size for a benchmark (Major).** With only 261 questions (522 images) and some sub-categories having as few as 14 samples (Structural ambiguity) or 16 samples (Verb ambiguity), the per-category performance breakdown has high variance. No confidence intervals or statistical significance tests are reported. *(Anchored: Page 7 - Table 3, Page 9 - Section 5 Limitation)*

3. **W3 — Human evaluation uses only 5 annotators (Major).** Individual human accuracy ranges from 80% to 93% (Table 6), a 13% spread. No inter-annotator agreement metric is reported. The central claim that "humans significantly outperform MLLMs" rests on this fragile baseline. *(Anchored: Page 6 - Section 3.4 Human Evaluation)*

4. **W4 — Conclusion contains accuracy errors and overclaiming (Major).** The conclusion states "the MLLMs average only 50.59% accuracy" and "the top-performing model... attains only about 70.00% accuracy." However: Table 3 shows Claude 3.5 Sonnet at 74%, and the abstract says 53.22%—different from 50.59%. The final sentence implies human-level performance on MMA equals "human-level understanding and reasoning in complex, real-world scenarios," which is a significant over-claim. *(Anchored: Page 10 - Conclusion)*

5. **W5 — Limited evidence for visual neglect mechanism (Major).** The text-only and ECR experiments suggest text bias but do not fully isolate the mechanism. Alternative explanations (task difficulty, option design bias, random sensitivity) are not ruled out. Per-image accuracy is not reported, making it impossible to distinguish between models that understand images but fail to switch context vs. models that ignore images entirely. *(Anchored: Page 8 - Section 4.3.2)*

### Minor Weaknesses

6. **W6 — Scaling law analysis overclaimed.** Only two model families (VILA1.5 and LLaVA) are used, and LLaVA shows a counterexample (middle-sized model best for semantic ambiguity). A true "scaling law" requires more evidence. *(Anchored: Page 9 - Section 4.3.5)*

7. **W7 — Related Work section reads as a list.** The MLLM paragraph is a chronological paper list rather than a structured comparison. The ambiguity datasets paragraph does not provide explicit differentiation from LAVA, the most closely related prior work. *(Anchored: Pages 2-3 - Section 2)*

8. **W8 — Amb_A metric lacks chance baseline and per-image reporting.** Without reporting expected Amb_A under random choice (6.25% for 4-option MCQ) or per-image accuracy, the metric provides incomplete information. *(Anchored: Page 7 - Section 4.2)*

9. **W9 — AI-generated image confound not analyzed.** The proportion of generated vs. sourced images is not reported, and no ablation tests whether models perform differently on each type. This threatens the benchmark's real-world validity claim. *(Anchored: Page 5 - Data Collection, Page 10 - Section 5)*

10. **W10 — Missing statistical rigor.** No variance reporting, confidence intervals, significance tests, or inter-annotator agreement metrics are provided anywhere in the paper. *(Anchored: Pages 6-9 - Section 4)*

## Key Issues
### Ranked Error Board (Top-5 Core Defects)

| Rank | Issue | Severity | Validity Risk | Research-Value Impact | Fixability | Confidence |
|------|-------|----------|---------------|----------------------|------------|------------|
| 1 | Factual inconsistency in model counts (24 vs 16 vs 17) | Major | High — undermines paper credibility | Medium — doesn't affect core contribution but erodes trust | Easy — correct to 17 | High |
| 2 | Small dataset (261 questions) with tiny sub-categories (14-16 samples) without CI | Major | Medium-High — per-category claims may be unreliable | High — benchmark value depends on reliable per-type measurement | Moderate — needs data expansion | High |
| 3 | Human evaluation with only 5 annotators (80-93% spread), no agreement metric | Major | High — the central "human gap" claim is statistically fragile | High — the paper's main finding depends on this comparison | Moderate — recruit more annotators, report agreement | High |
| 4 | Conclusion contains accuracy errors (70% vs 74%, 50.59% vs 53.22%) and overclaim | Major | High — inaccurate reporting and overreaching claims | Medium — conclusion should accurately summarize findings | Easy — correct numbers, bound claims | High |
| 5 | Limited causal evidence for visual neglect mechanism | Major | Medium-High — alternative explanations not ruled out | Medium — the diagnosis is likely correct but insufficiently supported | Moderate — add controlled experiments | Medium |

### Cross-Cutting Problem

A recurring issue is **insufficient statistical rigor**: no confidence intervals, no variance reporting, no significance tests, no inter-annotator agreement. For a benchmark paper whose main contribution is comparative evaluation, this is a significant gap. Readers cannot assess whether performance differences between models or ambiguity types are meaningful or due to noise.

## Actionable Suggestions
### S1 — Fix factual inconsistencies (Must, Easy)
- **Where:** Abstract, Page 1 (contribution (b)), Page 6 (Section 4.1), Page 10 (Conclusion)
- **What:** Unify all model counts to 17 (6 proprietary + 11 open-source as shown in Table 3). Change abstract to "evaluating 17 proprietary and open-sourced MLLMs." Fix Introduction contribution (b) from "16 MLLMs" to "17 MLLMs." Fix Conclusion: change "about 70.00% accuracy" to "74.32% (Claude 3.5 Sonnet)" and change "50.59%" to "53.22%" or whatever the correct average from Table 3 is.
- **Why:** These are easily fixable errors that undermine credibility.

### S2 — Expand human evaluation pool and report agreement (Must, Moderate effort)
- **Where:** Page 6 (Section 3.4)
- **What:** Recruit at least 20 annotators. Report mean, standard deviation, and 95% CI for human Amb_A. Report Fleiss' kappa or Krippendorff's alpha for inter-annotator agreement. If 20 annotators is infeasible, clearly caveat the human baseline as preliminary.
- **Why:** The central claim that humans outperform MLLMs depends on this comparison.

### S3 — Report confidence intervals throughout (Must, Moderate effort)
- **Where:** All tables reporting Amb_A, especially Table 3 and Figure 3-5
- **What:** For each model's Amb_A per category, compute and report 95% confidence intervals (bootstrap or exact binomial). Add a note specifying whether reported differences between models or ambiguity types are statistically significant.
- **Why:** Without CI, readers cannot distinguish signal from noise.

### S4 — Add per-image accuracy and chance baseline (Must, Easy)
- **Where:** Page 7 (Section 4.2, Table 3)
- **What:** Report per-image accuracy alongside Amb_A for all models. Report the random-chance Amb_A (for 4-option MCQ: 6.25%) as a reference baseline. Add a scatter plot of per-image accuracy vs. Amb_A to separate visual understanding from cross-context sensitivity.
- **Why:** Amb_A alone conflates two different capabilities.

### S5 — Add ablation for AI-generated vs. natural images (Nice-to-have, Moderate effort)
- **Where:** Page 5 (Data Collection) and Page 10 (Limitation)
- **What:** Categorize all 522 images as "generated" or "sourced" (with criteria). Report the proportion per category. Add an ablation comparing Amb_A on generated vs. natural images for at least 3 models.
- **Why:** Validates that the benchmark measures ambiguity handling, not artifact sensitivity.

### S6 — Rewrite Conclusion with accurate numbers and bounded claims (Must, Easy)
- **Where:** Page 10 (Conclusion)
- **What:** (a) Fix accuracy numbers to match Table 3. (b) Remove the overclaim about "human-level understanding and reasoning." (c) Restate the key limitations from Section 5. (d) End with specific, actionable future directions.

**Mentor Revised Version:**
"This paper introduces MMA, a benchmark for evaluating MLLMs' ability to use visual context for disambiguating ambiguous language. Our evaluation of 17 MLLMs reveals a substantial gap: models achieve 50-74% Amb_A versus 89% for humans. The gap is largest for syntactic ambiguities and smallest for lexical ambiguities. Error analysis indicates that models tend to rely on textual priors rather than visual context. These findings highlight a critical capability gap in current MLLMs. Limitations include the modest dataset size, the use of AI-generated images for some samples, and the limited set of ambiguity types and languages evaluated."

### S7 — Restructure Related Work around comparison axes (Nice-to-have, Easy)
- **Where:** Pages 2-3 (Section 2)
- **What:** Replace the chronological list with a structured comparison. For MLLMs, group by architecture type (joint embedding, modality-specific encoder, etc.). For ambiguity datasets, organize by modality (text-only vs. multimodal) and ambiguity type coverage. Add a paragraph explicitly differentiating MMA from LAVA.

### S8 — Expand the dataset (Nice-to-have, High effort)
- **Where:** All sections
- **What:** Target at least 500 questions with minimum 30 samples per sub-category. Prioritize expanding the smallest categories (Structural: 14, Verb: 16, Adjective: 30, Idiom: 22).
- **Why:** Reliable per-category analysis needs more samples.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction structure is:
1. **P1:** General MLLM capabilities and applications ("transformative potential")
2. **P2:** Ambiguity problem with examples (lexical, syntactic, semantic)
3. **P3:** MMA benchmark design description
4. **P4:** Contribution enumeration

**Problem:** The first paragraph is generic MLLM background that does not establish research stakes. The paper's core problem (ambiguity handling in MLLMs) only appears in P2. The reader must wait until P3 to understand the solution. This structure buries the lead.

### Recommended Storyline (Best Candidate)

A more compelling structure follows the arc: **Big Problem → Current Gap → Solution → Key Evidence → Contribution**

```
P1: Big Picture + Problem Hook
    "Ambiguity is pervasive in human communication: the same phrase can mean different things 
     in different contexts. For MLLMs deployed in real-world multimodal interactions, failing to 
     resolve ambiguity using visual context can lead to unpredictable errors. Yet current 
     benchmarks do not systematically test this capability."

P2: Gap in Prior Work  
    "Existing ambiguity datasets are predominantly text-only (WiC, AmbiEnt, AmbigQA) or 
     address ambiguity only as a secondary task (LAVA, 3AM, MMMU). None uses a paired-image 
     design where the same ambiguous question requires different answers depending on visual 
     context, directly isolating whether models use images for disambiguation."

P3: Our Solution — MMA Benchmark
    "We introduce MMA, a benchmark with 261 ambiguous questions, each paired with two 
     images depicting divergent scenarios. The key metric, Ambiguity Accuracy (Amb_A), 
     measures whether models correctly answer both images, testing contextual sensitivity."

P4: Key Findings Preview
    "Evaluating 17 MLLMs reveals a large gap: the best model (Claude 3.5 Sonnet) achieves 
     74% Amb_A vs. 89% for humans. Models perform best on lexical ambiguity and worst on 
     syntactic ambiguity. Error analysis shows cross-modal text bias accounts for 50% of errors."

P5: Contribution Summary
    "(a) First benchmark for MLLM ambiguity resolution with visual context, (b) comprehensive 
     17-model evaluation revealing significant human-model gap, (c) fine-grained analysis across 
     three ambiguity types and eight sub-types, (d) error taxonomy identifying text bias as the 
     dominant failure mode."
```

### Alignment Checks

| Check | Current | Recommended |
|-------|---------|-------------|
| **Problem Alignment** (stated challenge matches solution) | Partial — ambiguity introduced in P2, but P1 is generic | Strong — problem stated in P1, solution in P3 |
| **Variable Alignment** (core concepts appear in method) | Adequate — ambiguity types map to benchmark categories | Same |
| **Contribution-Evidence Alignment** (claims supported by experiments) | Weak — contribution (b) says "16 MLLMs" while Table 3 shows 17 | Fixed — use consistent 17 models |

### Abstract Outline (Sentence-Level Plan)

**S1 (Problem + Domain):** "Ambiguity in language is a fundamental challenge for MLLMs deployed in real-world multimodal interaction, where visual context could help disambiguate meaning but current benchmarks do not test whether models leverage this capability."

**S2 (Gap):** "Existing ambiguity datasets are text-only or address ambiguity only as a secondary task, lacking a controlled design that isolates visual disambiguation."

**S3 (Method):** "We introduce MMA, a benchmark of 261 ambiguous questions in multiple-choice VQA format, each paired with two divergent-context images that yield different correct answers."

**S4 (Key Result):** "Evaluating 17 MLLMs, we find a substantial gap: the best model achieves 74% Amb_A versus 89% for humans, with particularly poor performance on syntactic ambiguity."

**S5 (Implication):** "These results reveal a critical limitation in current MLLMs' ability to integrate visual context for disambiguation, highlighting an important direction for future model development."

### Title Suggestion

Current: "MMA: Benchmarking Multi-Modal Large Language Models in Ambiguity Contexts"

Improved: "MMA: Can MLLMs Use Visual Context to Resolve Ambiguity? A Benchmark and Evaluation"

This title better conveys the research question and evaluative nature of the work.

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[Problem: Factual inconsistencies (24 vs 16 vs 17 models)]
    -> [Fix: Unify to 17 across all sections]
    -> [Expected impact: Restored credibility]

[Problem: Weak human baseline (n=5, 80-93% spread)]
    -> [Fix: Recruit ≥20 annotators, report agreement stats]
    -> [Expected impact: Robust central comparison]

[Problem: No statistical rigor (no CI, no significance)]
    -> [Fix: Add 95% CI to all metrics, bootstrap confidence]
    -> [Expected impact: Claims become statistically grounded]

[Problem: Conclusion errors + overclaim]
    -> [Fix: Correct numbers, bound claims, restate limitations]
    -> [Expected impact: Accurate, defensible conclusion]

[Problem: AI-generated image confound]
    -> [Fix: Report proportions, add ablation analysis]
    -> [Expected impact: Validated real-world validity]

[Problem: Related Work reads as list]
    -> [Fix: Restructure as comparison axes, differentiate LAVA]
    -> [Expected impact: Stronger novelty positioning]
```

### Priority Order (P0/P1/P2)

| Priority | Action | Effort | Impact | Associated Issue |
|----------|--------|--------|--------|-----------------|
| **P0 (Pre-submission critical)** | Fix factual inconsistencies (model counts, accuracy numbers) | 1 hour | High | W1, W4 |
| **P0 (Pre-submission critical)** | Add confidence intervals and statistical rigor | 2-3 days | High | W2, W8 |
| **P0 (Pre-submission critical)** | Fix Conclusion: correct numbers, bound claims | 1 hour | High | W4 |
| **P1 (Before next submission)** | Expand human evaluation (≥20 annotators, report agreement) | 1-2 weeks | High | W3 |
| **P1 (Before next submission)** | Add per-image accuracy and chance baseline | 1-2 days | Medium | W5, W8 |
| **P1 (Before next submission)** | Report AI-generated vs. natural image split and ablation | 2-3 days | Medium | W9 |
| **P2 (Quality improvement)** | Restructure Related Work around comparison axes | 1-2 days | Medium | W7 |
| **P2 (Quality improvement)** | Expand dataset to 500+ questions with balanced sub-categories | 2-4 weeks | High | W2 |
| **P2 (Quality improvement)** | Add controlled experiment to isolate visual neglect mechanism | 1-2 weeks | High | W5 |
| **P2 (Quality improvement)** | Rename "Scaling Law" to "Effect of Model Size" | 30 min | Low | W6 |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|--------------|-----------------|-------------------|
| E1 | Main evaluation: Measure MLLM ability to use visual context for disambiguation | 261 ambiguous questions, each with 2 paired images; 17 MLLMs evaluated zero-shot | Amb_A (paired-image accuracy) | Best model (Claude 3.5 Sonnet): 74%; Humans: 89% | C1, C2, C3 | No CI, no per-image accuracy, no chance baseline |
| E2 | Text-only input: Test whether task complexity causes performance gap | MLLMs given only text (no images), selecting correct answer | % matching one correct answer | 83-90% correct | Used to rule out task complexity | Measures single-answer accuracy, not comparable to Amb_A |
| E3 | Error Consistency Rate (ECR): Measure text bias | Rate of same answer across two images | ECR | 71-84% across models | Cross-modal text bias | Does not isolate cause of consistency |
| E4 | Scaling analysis: Effect of parameter count | VILA1.5 (3B/13B/40B), LLaVA-NeXT (7B/13B/34B) | Amb_A per size | Positive trend for VILA1.5; LLaVA exception on semantic | C3 (partial) | Only 2 families, no significance test, one counterexample |
| E5 | Ablation: Question type (synonym vs. reasoning) | Noun ambiguity questions compared | Amb_A | Synonym > Reasoning for all models | Explains lexical vs. semantic gap | Only noun category tested |
| E6 | Human evaluation baseline | 5 annotators (CEFR C1) | Amb_A per person | 80-93% individual, 89% avg | C2 | Only 5 annotators, no agreement metric |

### Research-Theme Gap Diagnosis

**New Knowledge (partially supported):** The paper demonstrates that MLLMs struggle with visual disambiguation. This is a novel finding. However, the statistical fragility (small human sample, no CI, small sub-categories) weakens confidence in the precise magnitude of the gap.

**Reproducibility/Reusability (moderate):** The benchmark data and code are promised as available. The evaluation protocol is clearly described and can be reproduced. However, the use of AI-generated images without specification makes exact reproduction of the image set difficult.

**Potential to Change Practice/Understanding (moderate):** The finding that cross-modal text bias dominates errors (~50%) is actionable for model developers. The finding that syntactic ambiguity is hardest could guide benchmark design. However, the limited dataset size and statistical gaps reduce the paper's immediate impact.

### Proposed Research Experiments (P0/P1/P2)

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Before resubmission):
┌──────────────────────────────────────────────┐
│ Add 95% CI (bootstrap) to all Amb_A scores    │
│ Add per-image accuracy alongside Amb_A        │
│ Add random-chance baseline (6.25% for 4-option)│
│ Report inter-annotator agreement (Fleiss' κ)   │
└──────────────────────────────────────────────┘

P1 (Within 2 months):
┌──────────────────────────────────────────────┐
│ Controlled experiment: same image pair,       │
│ swap correct answer → test visual sensitivity │
│ Ablation: generated vs. natural image split   │
│ Expand human evaluation to ≥20 annotators     │
│ Report ECR on correct answers too             │
└──────────────────────────────────────────────┘

P2 (Long-term):
┌──────────────────────────────────────────────┐
│ Expand dataset to 500+ questions              │
│ Add audio modality (future work section)      │
│ Add non-English ambiguity types               │
│ Image-only condition for visual understanding │
└──────────────────────────────────────────────┘
```

### Detailed Experiment Proposals

**P0-1: Statistical Grounding** (Target: All claims)
- **Hypothesis:** Reported performance differences between models and ambiguity types are statistically significant.
- **Design:** Bootstrap 10,000 samples for each model-category pair to compute 95% CI.
- **Success Criterion:** Any pairwise comparison with non-overlapping CIs is considered significant.
- **Cost:** 1-2 days of computation.
- **Expected Gain:** All comparative claims become evidence-grounded.

**P0-2: Per-Image Accuracy** (Target: W5, W8)
- **Hypothesis:** Models with high per-image accuracy but low Amb_A suffer from cross-context insensitivity, not visual neglect.
- **Design:** For each model, compute accuracy on individual images (not pairs). Scatter plot per-image accuracy vs. Amb_A.
- **Success Criterion:** If per-image accuracy > Amb_A, the model understands images but fails to switch between contexts.
- **Cost:** Trivial (already have the per-image data).
- **Expected Gain:** Disentangles two distinct failure modes.

**P1-1: Controlled Visual Sensitivity Test** (Target: W5)
- **Hypothesis:** Models fail to adjust answers when visual context changes, even when they correctly understand each image individually.
- **Design:** For each question pair, present images in random order. Measure the probability of answer-switching when the image changes.
- **Controls:** Same model, same question, same options, only image changes.
- **Success Criterion:** Answer-switching rate > 50% indicates visual sensitivity.
- **Cost:** 1 week.
- **Expected Gain:** Direct causal test of the visual neglect claim.

**P1-2: Generated vs. Natural Image Ablation** (Target: W9)
- **Hypothesis:** Models perform differently on AI-generated vs. natural images.
- **Design:** Split all images into "generated" and "natural" sets (this requires manual annotation). Compare Amb_A on each subset for at least 3 models (GPT-4o, Claude 3.5 Sonnet, InternVL).
- **Control:** Same question distribution across subsets.
- **Success Criterion:** If Amb_A differs by <5%, the confound is minimal.
- **Cost:** 2-3 days for annotation + 1 day for evaluation.
- **Expected Gain:** Validates the benchmark's real-world validity claim.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5/10**

**Rationale:** The paper addresses a well-motivated and underexplored research question, with a clean experimental design and comprehensive model coverage. However, the score is moderated by several significant weaknesses:

- **Novelty (deferred verification):** Whether MMA is genuinely the "first benchmark" for multimodal ambiguity resolution cannot be fully assessed without external literature search, which was unavailable in this run. The paper's novelty claim is plausible but unverified.
- **Research Value (moderate):** The finding that MLLMs struggle with visual disambiguation is meaningful, but the statistical fragility (small human sample, no CI, small dataset) reduces confidence in the precise magnitude of findings.
- **Validity/Soundness (moderate):** Factual inconsistencies (model counts, accuracy numbers) indicate insufficient proofreading. The causal claim that models "fail to use visual information" is partially supported but not fully isolated from alternatives.
- **Reproducibility (moderate):** The evaluation protocol is clear, but the use of AI-generated images without specification of proportions makes exact reproduction difficult.

**Major deduction factors:** (1) Factual inconsistencies across sections. (2) Human evaluation with only 5 annotators. (3) No statistical significance testing or confidence intervals. (4) Conclusion contains errors and overclaims. (5) Per-image accuracy not reported.

**Post-Revision Target: [6.5, 7.5]/10**

This target assumes the following fixes are implemented:
- Factual inconsistencies corrected (all model counts unified to 17, accuracy numbers matched to Table 3)
- 95% confidence intervals added to all metrics
- Human evaluation expanded to ≥20 annotators with agreement metrics
- Conclusion corrected and bounded
- Per-image accuracy and chance baseline reported
- AI-generated vs. natural image proportion and ablation reported

If these P0/P1 items are fully addressed, the paper could reach 7-7.5/10 for its solid motivation and clean experimental design. Further expansion of the dataset (P2) could push it higher.