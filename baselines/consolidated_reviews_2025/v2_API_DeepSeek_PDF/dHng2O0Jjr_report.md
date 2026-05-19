## Summary
This paper presents ToolLLM, a comprehensive framework for improving tool-use capabilities in open-source large language models. The contributions are three-fold: (1) **ToolBench**, a large-scale instruction-tuning dataset with 16,464 real-world REST APIs and 126,486 instruction-solution path pairs covering both single-tool and multi-tool scenarios, constructed automatically using ChatGPT; (2) **DFSDT** (Depth-First Search-based Decision Tree), a multi-path reasoning strategy that outperforms ReACT by exploring multiple action trajectories during solution search; and (3) **ToolEval**, an automatic evaluation protocol with pass rate and win rate metrics backed by ChatGPT. Fine-tuning LLaMA-2 7B on ToolBench yields **ToolLLaMA**, which achieves pass rates competitive with ChatGPT (66.7% vs. 64.8% average) and outperforms Text-Davinci-003 and Claude-2 across held-out instructions and unseen APIs. The paper also demonstrates zero-shot generalization to the APIBench dataset and develops a neural API retriever with high retrieval precision (NDCG@1 of 78.0%).

The paper is well-organized and the scale of the dataset is a clear strength. However, several systematic concerns reduce scientific rigor: (1) the circular dependency between ChatGPT as both data annotator and evaluation judge is not adequately addressed as a limitation; (2) key claims about "comparable to ChatGPT" and "outperforming Gorilla" are presented without proper statistical qualification and with selective evidence; (3) the DFSDT algorithm lacks reproducibility-critical details (hyperparameters, cost breakdown, diversity operationalization); (4) the Related Work section reads as a citation list without comparative analysis; and (5) the Conclusion contains overclaims and omits limitations entirely. External novelty verification was unavailable in this run, so all novelty verdicts are marked deferred.

## Strengths
**1. Large-scale, real-world API dataset.** ToolBench is the largest instruction-tuning dataset for tool use by a substantial margin (16,464 APIs, 126k instances, 469k real API calls). The use of real RESTful APIs from RapidAPI with live calls and responses makes the dataset more realistic than prior simulated or small-scale benchmarks. This is a meaningful contribution to the open-source tool-learning ecosystem.

**2. Clear and reproducible pipeline.** The three-stage construction process (API collection, instruction generation, solution path annotation) is well-documented, with prompts and seed examples provided in the Appendix. The code, models, and demo are publicly released, supporting reproducibility and downstream use.

**3. DFSDT shows measurable improvement over ReACT.** The decision-tree reasoning strategy is clearly motivated by the limitations of single-trajectory methods, and the experimental results confirm a substantial pass rate improvement (63.8% vs 35.3% for ReACT on ChatGPT). The efficiency-oriented pre-order traversal variant is a practical design choice.

**4. Strong generalization evaluation design.** The three-level generalization setting (unseen instructions, unseen tools, unseen categories) and the OOD evaluation on APIBench provide a more thorough assessment than many prior tool-learning papers. The finding that ToolLLaMA generalizes to unseen API categories is practically significant.

**5. Candid discussion of evaluation difficulty.** The paper acknowledges that tool-use evaluation is "far more intricate than traditional tasks" and that human experts often disagree, which reflects honest scientific reporting of the evaluation challenge.

**6. Practical retriever integration.** The neural API retriever achieves 78.0% NDCG@1, significantly outperforming BM25 and Ada embeddings, and the finding that retrieved APIs can outperform ground-truth APIs (by discovering better alternatives) is an insightful result.

## Weaknesses
The following weaknesses are organized by severity and research-value impact.

### W1: Teacher-Student Circularity and Evaluation Bias (Major)

Both the training data annotation (ChatGPT generating DFSDT solution paths) and the evaluation (ToolEval using ChatGPT as judge) rely on the same underlying model family (gpt-3.5-turbo-16k). This creates an unaddressed systematic bias: ToolEval may systematically prefer solution paths that match ChatGPT's reasoning style, inflating ToolLLaMA's assessed performance since ToolLLaMA is trained on ChatGPT-generated data. The paper reports 87.1% pass-rate and 80.3% win-rate agreement with human annotators, but does not report human-human agreement as a baseline — if human annotators only agree at ~75-80% on win rate, then 80.3% is near ceiling; if they agree at 90%, there is a meaningful gap. Additionally, no cross-evaluator validation (e.g., using GPT-4 as an independent evaluator) is performed.

*Anchors: Page 3 (ToolEval), Page 6 (ToolEval description), Page 15 (Appendix A.5 — human disagreement discussion).*

### W2: Selective and Unbounded Comparative Claims (Major)

Several central claims are presented without proper scope boundaries or statistical qualification:
- "ToolLLaMA matches the performance of ChatGPT" (Page 9, Conclusion): the actual pass rate is 66.7% vs 64.8% (ChatGPT+DFSDT) — competitive, but "matches" implies statistical equivalence without significance testing.
- "Outperforms Gorilla" and "remarkable OOD generalization" (Page 8): In Table 5, ToolLLaMA+Our Retriever underperforms Gorilla-RS+BM25 on TensorHub AST (40.59 vs 41.90) and has 65% higher hallucination on HuggingFace (10.60 vs 6.42). With oracle retriever, Gorilla-RS achieves higher AST on all three domains. The narrative is selectively favorable.
- "Only slightly inferior to GPT4" (Page 3): The average pass rate gap is 4.4 points (ToolLLaMA 66.7% vs GPT4 71.1%), which is not trivially small for a 7B model comparison.

*Anchors: Page 3 (findings bullet), Page 8 (APIBench results narrative), Page 9 (Conclusion).*

### W3: Reproducibility Gaps in DFSDT Description (Major)

The DFSDT algorithm description (Page 6, Section 2.3) lacks several details necessary for independent reproduction:
- Maximum tree depth and branching factor are not specified.
- The "diversity" prompt mechanism that generates distinct child nodes is not operationally defined (is diversity measured by API name overlap, text similarity, or a free-form LLM instruction?).
- Average per-instance cost (ChatGPT calls or tokens) is not reported, so the efficiency claim underlying the ReACT@N comparison cannot be verified.
- The cost-equalization procedure for ReACT@N is described qualitatively ("until the total costs reach the same level") without specifying the stopping criterion.

*Anchors: Page 6 (DFSDT description), Page 13 (Appendix A.4 — pre-order traversal discussion).*

### W4: Related Work Lacks Comparative Depth (Major)

The Related Work section (Page 9) is organized as three broad paragraphs with dense citation lists. It does not:
- Map each prior work to the three claimed limitations (limited APIs, constrained scenario, inferior reasoning).
- Provide explicit comparison axes or tables beyond what was already shown in Table 1.
- Synthesize how this paper's approach differs from the strongest prior method on each dimension.
- The distinction between DFSDT and ToT is asserted rather than demonstrated: "DFSDT targets general decision-making problems where the decision space is infinite" is an unsupported claim.

*Anchors: Page 9 (Section 4 — Related Work).*

### W5: Dataset Quality Assurance Lacking Quantitative Verification (Minor-Major)

The dataset construction pipeline uses ChatGPT with "minimal human supervision" (Page 3) but no human quality audit statistics are reported for the 126k instruction-solution pairs. The filtering only removes hallucinated API references and failed solution paths; there is no reported verification of whether the generated instructions are natural, the solution paths are optimal, or the API parameters are correctly used. A human-verification rate on a random sample would substantially increase trust.

*Anchors: Page 3 (Section 2 overview), Page 5 (instruction generation filtering).*

### W6: Conclusion Omits All Limitations (Minor-Major)

The Conclusion (Page 9) does not mention any limitation, failure mode, or caveat. This is a significant omission for a paper that introduces a new dataset and model — readers cannot assess the boundaries of ToolBench's coverage or ToolLLaMA's failure cases. The paper's own APIBench results show higher hallucination rates, yet this is not acknowledged in the conclusion.

*Anchors: Page 9 (Section 5 — Conclusion).*

### W7: Strong Adjectives Without Empirical Anchor (Minor)

Throughout the paper, terms like "remarkable," "compelling," "robust," and "excellent" are used without precise empirical anchors. For example, "remarkable retrieval precision" (Page 3) should be replaced with the specific NDCG numbers. This weakens the objective tone expected in scientific writing.

## Key Issues
### Ranked Error Board (Top 5 Core Defects)

| Rank | Defect | Severity | Research-Value Impact | Validity Risk | Fixability | Confidence |
|------|--------|----------|----------------------|--------------|------------|------------|
| 1 | Teacher-student circularity (ChatGPT as both annotator and evaluator) | Major | High: Undermines independence of evaluation | Medium: 87% human agreement mitigates but does not eliminate systematic bias | Fixable: Add cross-evaluator validation, report human-human agreement | High |
| 2 | Selective comparative claims about ChatGPT/Gorilla | Major | High: Central claims overstate contribution | Medium: Raw numbers in Table 4/5 partially contradict narrative | Fixable: Bound claims to evidence, add significance tests | High |
| 3 | DFSDT lacks reproducibility-critical details | Major | Medium: Hinders adoption and verification | Low: Algorithm is intuitively correct, but unreproducible without parameters | Fixable: Add hyperparameters, cost data, diversity definition | High |
| 4 | Related Work is a flat citation list without comparative analysis | Major | Medium: Weakens novelty positioning | Low: Does not affect core results but undermines reader trust | Fixable: Restructure by comparison axes | High |
| 5 | Conclusion omits all limitations | Major | High: Damages scientific credibility and completeness | Low: Omission, not factual error | Fixable: Add limitation paragraph | High |

### Additional Notable Issues

| Issue | Severity | Anchor |
|-------|----------|--------|
| Abstract uses non-falsifiable adjectives ("remarkable", "comparable") | Minor | Page 1 Abstract |
| API filtering process lacks quantitative stage-by-stage breakdown | Minor | Page 4 Section 2.1 |
| Figure 2 caption interrupts paragraph flow in Introduction | Minor | Page 2 |
| "Only slightly inferior to GPT4" is author's judgment, not evidence | Minor | Page 3 |
| No multi-seed variance/confidence intervals for any experiment | Minor-Major | All experiment tables |
| Novelty verification deferred (Retrieval-Disabled Mode) | Deferred | Entire paper |

## Actionable Suggestions
### S1: Address Teacher-Student Circularity (Must)

**Problem:** Both data annotation (ChatGPT+DFSDT) and evaluation (ToolEval with ChatGPT) use the same model family, creating potential systematic bias.

**Action plan:**
1. Report human-human agreement on the win rate task as a baseline for interpreting ToolEval's 80.3% agreement.
2. Evaluate a random subset (e.g., 200 instructions) using GPT-4 as an independent evaluator and report cross-evaluator agreement.
3. Add a paragraph to the Limitations section explicitly discussing this circularity and why it does not invalidate the results (or proposing mitigation).

### S2: Bound Comparative Claims to Evidence (Must)

**Problem:** "Matches ChatGPT," "outperforms Gorilla," and "only slightly inferior to GPT4" overstate the evidence.

**Action plan:**
1. Replace "matches the performance of ChatGPT" (Conclusion) with "achieves comparable pass rates within 2 points of ChatGPT under the evaluated settings, though with higher hallucination rates on some domains."
2. In the APIBench results paragraph, replace the selective outperformance claim with a balanced assessment that acknowledges TensorHub underperformance and higher hallucination rates.
3. Remove "only slightly" from the GPT-4 comparison — let the raw numbers speak.
4. Add a note that no statistical significance tests were performed, and the observed differences may not be significant without variance estimates.

### S3: Complete DFSDT Reproducibility Details (Must)

**Problem:** Missing algorithmic hyperparameters and cost analysis prevent independent reproduction.

**Action plan:**
Add to Section 2.3 or Appendix A.4:
1. Maximum tree depth, branching factor, and node expansion budget.
2. Operational definition of "distinct node" generation.
3. Average ChatGPT calls/tokens per instruction for DFSDT vs ReACT vs ReACT@N.
4. Dollar cost estimate per 1,000 annotated instructions.

### S4: Restructure Related Work by Comparison Axes (Must)

**Problem:** The Related Work section reads as a chronological citation dump.

**Action plan:**
Reorganize into three thematic paragraphs matching the three claimed limitations:
- **Paragraph 1 — API Scale and Realism:** Compare ToolBench vs APIBench, API-Bank, ToolAlpaca, ToolBench-Xu on real API calls, number of APIs, and diversity. End with: "In contrast, ToolBench covers 16k real REST APIs with live execution."
- **Paragraph 2 — Multi-tool Composition:** Discuss which datasets support multi-tool instructions. End with: "ToolBench is the first to systematically cover intra-category and intra-collection multi-tool scenarios."
- **Paragraph 3 — Reasoning and Search:** Compare CoT, ReACT, Reflexion, ToT, and DFSDT. Clearly explain the technical difference between DFSDT and ToT (e.g., "DFSDT uses pre-order traversal with diversity prompting, while ToT uses BFS with value function scoring").

### S5: Add Limitations to Conclusion (Must)

**Problem:** The Conclusion has no limitation or caveat.

**Action plan (replace the final sentence):**
Replace "paves the way for future research" with:
"Limitations include: (1) dependence on ChatGPT for data annotation, which may introduce systematic biases; (2) higher inference cost of DFSDT compared to ReACT; (3) evaluation circularity since ToolEval also uses ChatGPT; and (4) higher hallucination rates on out-of-distribution benchmarks compared to domain-tuned models like Gorilla-RS. Future work should address these limitations by exploring weaker-supervision annotation, more cost-efficient search strategies, and independent evaluation protocols."

### S6: Add Quantitative Filtering Statistics (Nice-to-have)

**Problem:** API filtering is described as "rigorous" without stage-by-stage breakdown.

**Action plan:** Add a short table or sentence in Section 2.1 reporting: initial APIs (53,190), removed for basic functionality failure (X%), removed for slow response (Y%), removed for low-quality response (Z%), final (16,464).

### S7: Add Statistical Variance Reporting (Nice-to-have)

**Problem:** No confidence intervals, standard deviations, or significance tests reported anywhere.

**Action plan:** For the main results (Table 4), run each condition with at least 3 random seeds and report mean ± std. Add a paired significance test (e.g., bootstrap or Wilcoxon) for the ToolLLaMA vs ChatGPT comparison on pass rates.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current Introduction follows this arc:
- **P1:** Tool learning motivation + open-source gap vs closed-source strength.
- **P2 (split by Figure 2):** Three limitations of prior work + urgency statement.
- **P3 (on Page 3):** ToolLLM framework overview + three-phase bullet list + findings preview.

**Weakness:** The three limitations are listed after the urgency statement, creating a reverse order (motivation → urgency → gap → solution). A more natural flow is: gap → urgency → solution → evidence preview. Additionally, the Figure 2 caption interrupts the limitation paragraph, and the findings preview (on Page 3) belongs after the method description, not before it.

### Proposed Abstract Outline (Compact 5-Sentence Structure)

| Sentence | Role | Content | Evidence Anchor |
|----------|------|---------|-----------------|
| S1 | Problem + Domain | Open-source LLMs lack tool-use capabilities compared to closed-source models despite instruction tuning. | Page 1 Abstract |
| S2 | Prior Gap | Existing tool-learning datasets are limited in API scale, multi-tool coverage, and reasoning depth. | Page 2-3 Table 1 |
| S3 | Proposed Solution | ToolLLM framework with ToolBench (16k APIs, 126k instructions), DFSDT reasoning, and ToolEval evaluation. | Page 1, 2-3 |
| S4 | Key Result (bounded) | ToolLLaMA achieves competitive pass rates with ChatGPT across held-out instructions and generalizes to unseen APIs. | Page 8 Table 4 |
| S5 | Limitation + Scope | Performance depends on API documentation quality; hallucination rates remain higher on OOD benchmarks than domain-tuned models. | Page 8-9 Table 5 |

### Proposed Introduction Outline (Paragraph-by-Paragraph)

**P1 — Big Picture + Problem:** 
*Role:* Establish the importance of tool learning for LLMs. State that open-source LLMs underperform in this area.
*Claim:* Tool use is a critical capability for deploying LLMs in real-world applications, but it requires a combination of API understanding and multi-step reasoning that current open-source models lack.
*Transition:* "This gap stems from three limitations in existing tool-learning datasets and methods."

**P2 — Concrete Gap Analysis:**
*Role:* Identify three specific, falsifiable gaps in prior work, each with a brief explanation.
*Claim:*
1. API scale and realism: Prior datasets use simulated or small-scale APIs, not 16k+ real-world REST APIs.
2. Multi-tool composition: No prior dataset covers multi-tool instructions with real API responses.
3. Reasoning robustness: CoT/ReACT use single-trajectory search, causing error cascades.
*Transition:* "To address these gaps simultaneously, we introduce ToolLLM."

**P3 — Solution Overview:**
*Role:* High-level description of the three components: ToolBench, DFSDT, ToolEval.
*Claim:* The framework is fully automatic, requiring only ChatGPT as the annotation backbone, and can be extended to new APIs with minimal effort.
*Transition:* (No explicit transition needed — leads into Section 2.)

**P4 — Contribution Summary (replaces the current findings bullet list):**
*Role:* Precise enumeration of contributions with scoped claims.
*Claim:*
1. ToolBench: Largest tool-use instruction-tuning dataset (16k APIs, 126k instances).
2. DFSDT: Multi-path decision tree that improves pass rate by 28.5 points over ReACT on average.
3. ToolLLaMA: Competitive with ChatGPT within 2 points pass rate; outperforms Claude-2 and Text-Davinci-003.
4. Generalization: Zero-shot transfer to APIBench with competitive AST accuracy.

### Title Suggestion

Current title: "TOOL LLM: FACILITATING LARGE LANGUAGE MODELS TO MASTER 16000+ REAL-WORLD APIS"

Revised: **"ToolLLM: A Framework for Open-Source LLMs to Master 16,000+ Real-World REST APIs through Instruction Tuning and Multi-Path Reasoning"**

Rationale: Adds "Instruction Tuning and Multi-Path Reasoning" to signal the two key methodological contributions.

### Alignment Checks

| Check | Current | Proposed |
|-------|---------|----------|
| Problem-method alignment | Gap stated then framework introduced | Same, but gaps are explicitly falsifiable |
| Variable alignment | Core concepts (API, tool, instruction, solution path) appear consistently | Same, no change needed |
| Contribution-evidence alignment | Bullet claims are promotional without bounds | Each claim references a specific metric and setting |

## Priority Revision Plan
The following revision plan is ordered by impact on manuscript quality and scientific credibility.

### P0 — Critical (Must Fix Before Resubmission)

| ID | Task | Effort | Impact | Sections Affected |
|----|------|--------|--------|-------------------|
| P0.1 | Add limitations to Conclusion (replace generic closing) | Low | High: Restores scientific completeness | Section 5 |
| P0.2 | Bound comparative claims (ChatGPT, Gorilla, GPT-4) | Low | High: Removes overclaim risk | Abstract, Intro, Conclusion, Section 3.3 |
| P0.3 | Add DFSDT hyperparameters and cost data | Low | High: Enables reproduction | Section 2.3, Appendix A.4 |
| P0.4 | RAG: add cross-evaluator validation for ToolEval | Medium | High: Addresses circularity concern | Section 3.1, Appendix A.5 |

### P1 — Major (Should Fix for Strong Submission)

| ID | Task | Effort | Impact | Sections Affected |
|----|------|--------|--------|-------------------|
| P1.1 | Restructure Related Work by comparison axes | Medium | High: Strengthens novelty positioning | Section 4 |
| P1.2 | Add human-human agreement baseline for ToolEval | Low | Medium: Clarifies evaluation reliability | Section 3.1, Appendix A.5 |
| P1.3 | Add API filtering stage-by-stage breakdown | Low | Medium: Improves dataset transparency | Section 2.1 |
| P1.4 | Replace promotional adjectives with evidence-grounded language throughout | Medium | Medium: Improves scientific tone | All sections |

### P2 — Nice-to-Have

| ID | Task | Effort | Impact | Sections Affected |
|----|------|--------|--------|-------------------|
| P2.1 | Add multi-seed variance reporting to main results | Medium | Medium: Enables significance assessment | Section 3.2, Table 4 |
| P2.2 | Human quality verification rate on sampled ToolBench instructions | Medium | Medium: Increases dataset trustworthiness | Section 2 |
| P2.3 | Ablation study: impact of API retriever quality on ToolLLaMA performance | High | Medium: Strengthens practical pipeline claims | Section 3.2 |
| P2.4 | Update title to include methodological keywords | Low | Low: Improves discoverability | Title |

### Revision Sequence (Recommended Order)

```text
Stage 1 (Today — 2 hours):
  P0.1 + P0.2 + P0.3 + P1.3 + P1.4

Stage 2 (This week — 1-2 days):
  P0.4 + P1.1 + P1.2 + P2.1

Stage 3 (Before submission — 2-3 days):
  P2.2 + P2.3 + P2.4
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 — API Retriever (Table 2) | Test whether Sentence-BERT dense retriever outperforms BM25 and Ada embeddings | I1/I2/I3 split, NDCG@1 and @5 | NDCG | Ours: 78.0/84.9 (NDCG@1/@5) vs BM25: 18.5/17.0 | Retriever is effective | No evaluation on unseen API categories |
| E2 — DFSDT vs ReACT (Table 3) | Test whether DFSDT improves pass rate over ReACT at matched cost | ChatGPT backbone, I1/I2/I3 | Pass rate | DFSDT 63.8% vs ReACT 35.3% vs ReACT@N 44.5% | DFSDT significantly improves reasoning | Cost matching procedure is vaguely described; actual cost numbers not reported |
| E3 — Main Results (Table 4) | Compare ToolLLaMA against baselines on generalization | Multi-level (Inst/Tool/Cat), I1/I2/I3 | Pass rate, Win rate | ToolLLaMA+DFSDT avg pass: 66.7%; ChatGPT+DFSDT: 64.8%; ToolLLaMA competitive with ChatGPT | ToolBench elicits tool-use capability | No variance reporting; win rate baseline is ChatGPT-ReACT only |
| E4 — OOD to APIBench (Table 5) | Test zero-shot generalization of ToolLLaMA to APIBench | TorchHub, TensorHub, HuggingFace; vs Gorilla | AST accuracy, Hallucination rate | Mixed: ToolLLaMA slightly ahead on HF/TorchHub with Our Retriever, behind with Oracle | Generalization is partially supported | Higher hallucination rates; underperforms Gorilla-RS on TensorHub and with Oracle |
| E5 — Human-ToolEval Agreement | Validate ToolEval reliability | 300 instructions, 4 methods | Agreement % | Pass rate: 87.1%, Win rate: 80.3% | ToolEval correlates with human judgment | Human-human agreement not reported; no cross-evaluator check |

### Research-Theme Gap Diagnosis

| Core Value | Current Support Level | Gap |
|------------|----------------------|-----|
| New knowledge (how open-source LLMs acquire tool-use ability) | Partial | The paper shows that ToolBench + SFT improves performance, but does not analyze *why* (e.g., which training data properties matter most) |
| Reproducibility/reusability | Good | Code, models, and demo are open-source, but DFSDT hyperparameters missing |
| Potential to change practice | Moderate | The framework could enable wider deployment of tool-use LLMs, but lack of limitation discussion reduces adoption confidence |

### Proposed Research Experiments (P0/P1/P2)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Quality Gain |
|--------|-------------|------------|---------------|-------------------|---------|-------------------|----------------|----------------------|
| P0-E1 | DFSDT efficiency | DFSDT is more cost-effective than ReACT@N per successful solution | Run DFSDT and ReACT@N on 1,000 instructions, count API calls per pass | Same backbone (ChatGPT), same budget | Calls per solved instruction, $ per 1k solutions | DFSDT < ReACT@N on calls/pass | 2 days, ~$50 API cost | Validates core efficiency claim; fills current gap |
| P0-E2 | ToolEval independence | GPT-4 as evaluator agrees with ChatGPT-based ToolEval | Evaluate 200 solution pairs with GPT-4 ToolEval | Compare against ChatGPT-ToolEval and human judges | Agreement rate, Cohen's kappa | >82% agreement | 1 day, ~$30 | Addresses circularity concern directly |
| P1-E1 | Statistical reliability | Observed gains are not due to chance | Run 3 seeds for main Table 4 conditions (ChatGPT, ToolLLaMA, GPT4 with DFSDT) | Same settings as Table 4 | Mean±std pass rate | All gains >2σ above baseline variance | 3-5 days GPU | Enables significance assessment |
| P1-E2 | Training data scaling | More instructions improve generalization | Train ToolLLaMA on 25%, 50%, 75%, 100% of ToolBench | Same base model, same hyperparameters | Pass rate on I1-Cat and I2-Cat | Monotonic improvement with data size | 5-7 days GPU | Quantifies data efficiency |
| P2-E1 | Retriever impact analysis | Better retriever → better tool-use performance | Vary retriever (BM25, Ada, Ours) as input to ToolLLaMA | Same ToolLLaMA model | Pass rate, win rate | Positive correlation NDCG → Pass rate | 2 days | Strengthens practical pipeline claim |
| P2-E2 | Hallucination reduction | ToolLLaMA hallucination can be reduced via preference tuning | Apply DPO or rejection sampling on APIBench incorrect outputs | ToolLLaMA baseline | Hallucination rate, AST accuracy | Hallucination < 7% on all domains | 5 days GPU | Addresses OOD weakness |

```text
ASCII Diagram — Experiment Upgrade Plan

P0-E1 (DFSDT cost) ──> P0-E2 (cross-evaluator)
         │                       │
         ▼                       ▼
    Core efficiency        Evaluation validity
         │                       │
         └───────┬───────────────┘
                 ▼
         P1-E1 (multi-seed variance)
                 │
                 ▼
         P1-E2 (data scaling curve)
                 │
                 ▼
         P2-E1 (retriever ablation) ──> P2-E2 (hallucination reduction)
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5 / 10

*Score rationale:* The paper demonstrates a clear engineering contribution (large-scale dataset, practical pipeline) and the experiments show convincing improvements over ReACT. However, the score is reduced due to: (1) unaddressed teacher-student circularity in evaluation (ChatGPT as both annotator and judge), (2) selective and unbounded comparative claims that overstate the results, (3) missing reproducibility details for the core algorithmic contribution (DFSDT), (4) a Related Work section that reads as a citation list rather than comparative analysis, and (5) a Conclusion with no limitations. The novelty dimension cannot be fully assessed in this run due to Retrieval-Disabled Mode, but the methodological weaknesses are independently verifiable and directly affect the reliability of the claimed findings.

**Post-Revision Target:** [7.5, 8.5] / 10

*Target rationale:* If the authors address the P0 and P1 items (particularly adding limitations to the Conclusion, bounding all comparative claims, adding DFSDT details, cross-evaluator validation, and restructuring Related Work), the scientific rigor would improve substantially. The core dataset and empirical results are strong enough to support a score in this range. The upper bound assumes the authors also add multi-seed variance and address the hallucination concern on APIBench. Novelty verification by external literature search could further adjust this target upward or downward depending on overlap with existing work.