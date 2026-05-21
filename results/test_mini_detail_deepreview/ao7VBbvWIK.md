Now I have enough calibration data. Let me synthesize the final review.

## Final Calibration Summary

**Round-1 bracket** (initial bracketing): Based on three queries, the HASTE paper clearly does not belong in the strong band (>7.5). The middle-band anchors (4.00–6.25) all have functioning evaluations with baseline comparisons, even if imperfect. The weak-band anchors (1.67–3.00) share the most characteristics with HASTE: underspecified methods, missing crucial comparisons.

**Narrowing within bracket (Round 2):** The most comparable papers are:

1. **Improve Code Generation with Feedback** (3.00): Had actual baseline comparisons (even if questionable numbers), missing key related-method comparison, vague implementation details. HASTE is *worse* on the baseline front — it defines baselines but reports *zero* comparative results.
2. **FALCON** (3.00): Underspecified method, missing hyperparameters, vague experiments. Similar severity of method underspecification.
3. **CodeChain** (4.00): Large-scale dataset contribution, but had incorrect baseline presentation. Still had evaluations with comparisons.
4. **AST-T5** (5.67): Full experiments on standard benchmarks with clear comparisons.

The HASTE paper's two fatal flaws — (a) defining baselines but never using them, and (b) describing the core "token-bounded extraction" in one sentence — place it clearly in the 3.0 range. Papers at 4.0+ all have some form of comparative evaluation working. Papers at 3.0 share comparable fundamental gaps.

---

## Review of ICLR 2026 Submission: HASTE

## Summary

HASTE proposes a hybrid framework for code context retrieval that combines AST-guided structural pruning with lexical and semantic search, aiming to provide LLMs with compact yet syntactically coherent code context for automated editing tasks. The pipeline integrates BM25 and dense retrieval via Reciprocal Rank Fusion, then expands candidates through call-graph traversal and filters under a token budget. The paper evaluates on 6 curated Python files and 12 SWE-PolyBench instances using an LLM-as-Judge metric.

## Strengths

- **Clear problem framing and concrete illustrative example.** The paper articulates a genuine tension between structure-aware (syntactically complete but semantically blind) and relevance-focused (semantically precise but structurally fragmented) context retrieval. The test3.py case study in Section 5.1 concretely demonstrates how call-graph expansion preserved a dependent class definition that enabled a correct complex type hint — a compelling illustration of the mechanism working as designed.

- **Formal specification of the hybrid retrieval fusion.** Section 3.3 provides the explicit Reciprocal Rank Fusion equation used to combine BM25 and semantic scores. While RRF itself is standard, having the precise formulation with the k=60 parameter choice enables reproducibility of the ranking stage.

- **Open-source implementation.** The Data Availability section states the framework is packaged and available on PyPI ('HasteContext'). This is a concrete step toward reproducibility, even if the core algorithm's specification is incomplete (see Weaknesses).

- **Transparent failure documentation on SWE-PolyBench.** Section 5.3 candidly discusses low-scoring cases (e.g., a 0 from a fundamentally flawed suggestion, scores of 5 and 10 from task misinterpretation), acknowledging that context quality alone cannot fix poor task specifications or LLM reasoning failures.

## Weaknesses

### Fatal

1. **No comparative results against any baseline.** Section 4.1.3 defines three baselines (IR-only, AST-only, naïve truncation) "to contextualize HASTE's performance." **No baseline results appear anywhere in the paper.** Table 2 and Figure 2 report only HASTE's scores. The paper's central thesis — that HASTE resolves the trade-off between structure-aware and relevance-focused approaches — is entirely unsubstantiated without comparing to either type of method. A system that achieves Judge Scores of 90–100 on simple tasks without comparison could be no better than naïve truncation or random chunk selection. This is not a missing experiment; it is the absence of evidence required by the paper's own stated claim.

2. **Core algorithm is underspecified.** The title features "Token-bounded Extraction," yet the Selection stage (§3.3) describes this mechanism in a single sentence: "The expanded set is then filtered under a strict token budget." No algorithm is given for how AST subtrees are selected or pruned when the budget is exceeded, what optimization criterion governs the selection, how the "configurable depth" for call-graph expansion is set, or how the call graph itself is constructed (static vs. dynamic analysis, which tool). This is the claimed technical contribution; the reader cannot evaluate or reproduce it.

### Major

3. **Evaluation scale is far too small.** The curated dataset contains **6 Python files**. The SWE-PolyBench evaluation reports results on **12 instances** (7 of which are trivial "no-op" tasks). Six files and twelve tasks cannot support claims about "reliable and scalable" context compression. The paper states that SWE-PolyBench "excludes instances that resulted in processing errors" without quantifying how many were excluded or why — raising selection-bias concerns.

4. **6-point correlation with no statistical rigor.** The reported Pearson r = −0.97 between compression ratio and Judge Score (RQ2) is computed from **6 data points**, with one high-compression outlier (test3.py) visibly driving the correlation. No confidence intervals, significance tests, or leave-one-out analysis are provided. The paper does not report the correlation without the outlier. A correlation from 6 points with no error quantification is not statistically meaningful.

5. **No per-instance variance or significance tests.** Section 4.1.4 states each task was "executed three times and averaged," but no per-instance variance, standard deviation, or error bars are reported anywhere. The SWE-PolyBench results appear to be single runs. The LLM-as-Judge evaluation uses a single judge model (Gemini 1.5 Flash) with no calibration, no human validation, and no inter-rater reliability assessment.

6. **Defined metrics never reported.** Section 4.2 defines "Hallucination Rate" as an evaluation metric but it is never reported in any results table or figure. Given the paper's stated motivation that HASTE reduces hallucination by providing coherent context, this omission is notable.

### Minor

7. **Python-only evaluation.** All experiments use Python files. While the paper claims extensibility via Tree-sitter, no cross-language evidence is provided.

8. **RRF parameter k=60 not justified.** The smoothing parameter is set to 60 without analysis of its effect. While not a fatal issue, it would strengthen the paper to show sensitivity or motivate the choice.

9. **LLM-as-Judge prompt not provided.** The evaluation relies on a single LLM (Gemini 1.5 Flash) as the judge, but the judge prompt is not included, making it impossible to assess evaluation quality.

### Trivial

10. The placeholder citation (Zhang et al., 2025, marked "for illustrative purposes") is acknowledged by the paper itself but still weakens the scholarly presentation.

## Nice-to-Haves

- Ablation studies isolating the contribution of each HASTE component (call-graph expansion, hybrid search, AST-bounded pruning) would significantly strengthen the paper.
- Expanding evaluation to standard, larger benchmarks (e.g., SWE-bench, CrossCodeEval) with meaningful instance counts.
- Reporting compression ratios for every evaluation instance, not just the curated-dataset outlier.

## Removed Points

- **"References rely on arXiv preprints"** — Rule: do not question existence or release status of cited references. The paper's references are its own contextual choices.
- **"Missing related work discussion"** — Rule: do not mention missing related works without external sources to confirm.
- **"Formatting/typo nitpicks"** — These are parser artifacts, not submission errors.
- **"The correlation analysis criticism about structure-agnostic methods failing at similar compression"** — The paper already acknowledges the limitation of this claim in §5.2 ("In contrast, structure-agnostic pruning would likely lead to a catastrophic drop"). This is a stated limitation, not an error.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations sharpen the paper's known shortcomings but do not surface unanticipated findings about method behavior.

## Suggestions

1. Report baseline results for IR-only, AST-only, and naïve truncation on the same 6 tasks and 12 SWE-PolyBench instances. This single addition would determine whether the paper has a contribution or is merely a demo.
2. Provide a precise algorithmic description of token-bounded extraction: the scoring criterion, pruning strategy (greedy? optimal?), and budget-enforcement mechanism.
3. Scale up the evaluation: even holding the method fixed, testing on 100+ instances from a standard benchmark like SWE-bench with proper statistical reporting (confidence intervals, error bars) would substantially strengthen the evidence.
4. Report the hallucination rate that is defined but never used.

## Score and Decision

HASTE identifies a real problem and proposes a plausible pipeline, but the paper in its current form has two fatal gaps: (1) zero comparative results against any baseline despite defining three, and (2) the core "token-bounded extraction" algorithm — the paper's claimed technical contribution — is described in one sentence. The evaluation is also far too small (6 curated files, 12 benchmark instances) and statistically unsound (6-point correlation, no variance reporting). These are not speculative concerns; they are verifiable from the published content.

**Bracketing:** Round 1 placed the paper below any anchor in the 4.00–6.25 band, all of which have at least some baseline comparisons. Round 2 narrowed the comparison to papers at 3.00 (Improve Code Generation with Feedback, FALCON), which share the pattern of underspecified methods and missing key comparisons. HASTE is comparable to these papers in severity: it has clearer problem framing than FALCON but worse evaluation completeness than either (the feedback paper at least reported baseline numbers).

**Final score relative to anchors:** HASTE is below REPOFILTER (5.60, has baselines, larger evaluation) and CodeChain (4.00, has evaluation with comparisons). It is comparable to Improve Code Generation with Feedback (3.00) and FALCON (3.00) in the severity of its gaps.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>